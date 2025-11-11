#!/usr/bin/env python3
"""
week3/lecture_notes.md를 Notion 페이지에 업로드

사용법:
    python upload_lecture_notes.py
    또는
    python upload_lecture_notes.py <page_id>
"""

import os
import sys
import re
from typing import List, Dict, Tuple
from notion_client import Client

# Notion API 설정
NOTION_TOKEN = os.getenv('NOTION_TOKEN')

# 기본 페이지 ID (URL에서 추출)
DEFAULT_PAGE_ID = "29f41454561d817c842df653dac8b2cd"


def parse_inline_markdown(text: str) -> List[Dict]:
    """
    Markdown inline formatting을 Notion rich_text로 변환
    **bold**, *italic*, `code`, ~~strikethrough~~ 지원
    """
    if not text:
        return []

    rich_text = []

    # 정규식 패턴: **bold**, *italic*, `code`, ~~strikethrough~~
    # 우선순위: code > bold > italic > strikethrough
    pattern = r'(`[^`]+`|\*\*[^*]+\*\*|\*[^*]+\*|~~[^~]+~~)'

    parts = re.split(pattern, text)

    for part in parts:
        if not part:
            continue

        annotations = {
            'bold': False,
            'italic': False,
            'code': False,
            'strikethrough': False
        }
        content = part

        # Code (highest priority)
        if part.startswith('`') and part.endswith('`'):
            content = part[1:-1]
            annotations['code'] = True
        # Bold
        elif part.startswith('**') and part.endswith('**'):
            content = part[2:-2]
            annotations['bold'] = True
        # Italic
        elif part.startswith('*') and part.endswith('*') and not part.startswith('**'):
            content = part[1:-1]
            annotations['italic'] = True
        # Strikethrough
        elif part.startswith('~~') and part.endswith('~~'):
            content = part[2:-2]
            annotations['strikethrough'] = True

        # Notion API는 빈 텍스트를 허용하지 않음
        if content:
            # 2000자 제한
            if len(content) > 2000:
                content = content[:2000]

            rich_text.append({
                'type': 'text',
                'text': {'content': content},
                'annotations': annotations
            })

    return rich_text if rich_text else [{'type': 'text', 'text': {'content': text or ' '}, 'annotations': {'bold': False, 'italic': False, 'code': False, 'strikethrough': False}}]


def parse_markdown_to_blocks(md_content: str, max_blocks: int = 100) -> List[List[Dict]]:
    """
    Markdown을 Notion blocks로 변환
    표, 코드 블록, 리스트, 인용구 등을 처리
    """
    lines = md_content.split('\n')
    all_blocks = []
    i = 0

    while i < len(lines):
        line = lines[i].rstrip()

        # 빈 줄은 단락 구분으로 처리 (건너뛰기만 하면 됨, 다음 단락이 시작될 때 처리)
        if not line:
            i += 1
            continue

        # 표 처리 - Notion API는 테이블을 한 번에 생성해야 함
        if '|' in line and line.strip().startswith('|'):
            # 테이블 시작 감지
            table_lines = []
            start_i = i
            
            # 헤더 행
            if i < len(lines) - 1 and '|' in lines[i+1] and '---' in lines[i+1]:
                table_lines.append(line)
                table_lines.append(lines[i+1])  # 구분선
                i += 2
                
                # 데이터 행들 수집
                while i < len(lines) and '|' in lines[i] and lines[i].strip().startswith('|'):
                    table_lines.append(lines[i])
                    i += 1
                
                # 테이블을 코드 블록으로 변환 (Notion API 테이블 생성이 복잡하므로)
                # 또는 간단한 텍스트로 변환
                if table_lines:
                    table_content = '\n'.join(table_lines)
                    all_blocks.append({
                        'object': 'block',
                        'type': 'code',
                        'code': {
                            'rich_text': [{'type': 'text', 'text': {'content': table_content}}],
                            'language': 'markdown',
                            'caption': []
                        }
                    })
                
                continue

        # 코드 블록 (```)
        if line.startswith('```'):
            code_lines = []
            language = line[3:].strip() if len(line) > 3 else ''
            i += 1
            
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1
            
            if code_lines:
                code_content = '\n'.join(code_lines)
                all_blocks.append({
                    'object': 'block',
                    'type': 'code',
                    'code': {
                        'rich_text': [{'type': 'text', 'text': {'content': code_content}}],
                        'language': language if language else 'plain text',
                        'caption': []
                    }
                })
            
            i += 1
            continue

        # 인용구 (>)
        if line.startswith('>'):
            quote_lines = []
            while i < len(lines) and lines[i].strip().startswith('>'):
                quote_text = lines[i].lstrip('> ').strip()
                if quote_text:
                    quote_lines.append(quote_text)
                i += 1
            
            if quote_lines:
                quote_content = ' '.join(quote_lines)
                all_blocks.append({
                    'object': 'block',
                    'type': 'quote',
                    'quote': {
                        'rich_text': parse_inline_markdown(quote_content)
                    }
                })
            continue

        # 제목 (#)
        if line.startswith('#'):
            level = len(line) - len(line.lstrip('#'))
            text = line.lstrip('# ').strip()
            
            if level == 1:
                all_blocks.append({
                    'object': 'block',
                    'type': 'heading_1',
                    'heading_1': {
                        'rich_text': parse_inline_markdown(text)
                    }
                })
            elif level == 2:
                all_blocks.append({
                    'object': 'block',
                    'type': 'heading_2',
                    'heading_2': {
                        'rich_text': parse_inline_markdown(text)
                    }
                })
            elif level == 3:
                all_blocks.append({
                    'object': 'block',
                    'type': 'heading_3',
                    'heading_3': {
                        'rich_text': parse_inline_markdown(text)
                    }
                })
            elif level == 4:
                all_blocks.append({
                    'object': 'block',
                    'type': 'heading_3',  # Notion은 heading_4가 없으므로 heading_3 사용
                    'heading_3': {
                        'rich_text': parse_inline_markdown(text)
                    }
                })
            
            i += 1
            continue

        # 리스트 (-, *, 1.) - 들여쓰기 고려
        list_match = re.match(r'^(\s*)([-*]|\d+\.)\s+(.+)', line)
        if list_match:
            indent = len(list_match.group(1))
            marker = list_match.group(2)
            item_text = list_match.group(3).strip()
            is_ordered = bool(re.match(r'^\d+\.', marker))
            
            # 현재 들여쓰기 레벨의 리스트 항목들 수집
            list_items = [(indent, item_text)]
            i += 1
            
            while i < len(lines):
                current_line = lines[i]
                current_match = re.match(r'^(\s*)([-*]|\d+\.)\s+(.+)', current_line)
                
                if not current_line.strip():
                    # 빈 줄을 만나면 리스트 종료
                    i += 1
                    break
                
                if current_match:
                    current_indent = len(current_match.group(1))
                    # 같은 들여쓰기 레벨이면 계속 수집
                    if current_indent == indent:
                        list_items.append((current_indent, current_match.group(3).strip()))
                        i += 1
                    # 더 깊은 들여쓰기면 하위 리스트 (일단 현재 리스트 종료)
                    elif current_indent > indent:
                        # 하위 리스트는 나중에 처리하기 위해 현재 위치 유지
                        break
                    # 더 얕은 들여쓰기면 상위 리스트로 복귀
                    else:
                        break
                else:
                    # 리스트가 아닌 줄을 만나면 종료
                    break
            
            # 각 리스트 항목을 별도 블록으로 추가
            for item_indent, item_text in list_items:
                if is_ordered:
                    all_blocks.append({
                        'object': 'block',
                        'type': 'numbered_list_item',
                        'numbered_list_item': {
                            'rich_text': parse_inline_markdown(item_text)
                        }
                    })
                else:
                    all_blocks.append({
                        'object': 'block',
                        'type': 'bulleted_list_item',
                        'bulleted_list_item': {
                            'rich_text': parse_inline_markdown(item_text)
                        }
                    })
            continue

        # 체크박스 (- [ ] 또는 - [x])
        if re.match(r'^[-*]\s+\[([ x])\]\s+', line):
            match = re.match(r'^[-*]\s+\[([ x])\]\s+(.+)', line)
            if match:
                checked = match.group(1) == 'x'
                text = match.group(2).strip()
                all_blocks.append({
                    'object': 'block',
                    'type': 'to_do',
                    'to_do': {
                        'rich_text': parse_inline_markdown(text),
                        'checked': checked
                    }
                })
                i += 1
                continue

        # 일반 텍스트 (단락)
        # 빈 줄을 만나면 단락을 종료하고 새 단락 시작
        paragraph_lines = []
        while i < len(lines):
            current_line = lines[i].rstrip()
            
            # 빈 줄을 만나면 현재 단락 종료
            if not current_line:
                if paragraph_lines:
                    paragraph_text = ' '.join(paragraph_lines).strip()
                    if paragraph_text:
                        all_blocks.append({
                            'object': 'block',
                            'type': 'paragraph',
                            'paragraph': {
                                'rich_text': parse_inline_markdown(paragraph_text)
                            }
                        })
                    paragraph_lines = []
                i += 1
                continue
            
            # 다른 블록 타입이면 중단
            if (current_line.startswith('#') or
                current_line.startswith('```') or
                current_line.startswith('>') or
                (current_line.startswith('|') and '|' in current_line) or
                re.match(r'^[-*]\s+', current_line) or
                re.match(r'^\d+\.\s+', current_line) or
                re.match(r'^[-*]\s+\[', current_line)):
                break
            
            paragraph_lines.append(current_line)
            i += 1
        
        # 마지막 단락 처리
        if paragraph_lines:
            paragraph_text = ' '.join(paragraph_lines).strip()
            if paragraph_text:
                all_blocks.append({
                    'object': 'block',
                    'type': 'paragraph',
                    'paragraph': {
                        'rich_text': parse_inline_markdown(paragraph_text)
                    }
                })

    # 100개 블록 단위로 배치
    batches = []
    for i in range(0, len(all_blocks), max_blocks):
        batches.append(all_blocks[i:i+max_blocks])

    return batches


def upload_to_notion(page_id: str, md_file: str):
    """Markdown 파일을 Notion 페이지에 업로드"""

    if not NOTION_TOKEN:
        print("❌ Error: NOTION_TOKEN 환경 변수가 설정되지 않았습니다.")
        print("   export NOTION_TOKEN='your_token_here'")
        return

    # Notion 클라이언트 초기화
    notion = Client(auth=NOTION_TOKEN)

    # Markdown 파일 읽기
    print(f"📖 Reading {md_file}...")
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"   File size: {len(content)} characters, {len(content.splitlines())} lines")

    # 기존 블록 삭제 (선택사항 - 주석 처리)
    # print("🗑️  Clearing existing blocks...")
    # try:
    #     existing_blocks = notion.blocks.children.list(block_id=page_id)
    #     for block in existing_blocks.get('results', []):
    #         notion.blocks.delete(block_id=block['id'])
    # except Exception as e:
    #     print(f"   ⚠️  Could not clear blocks: {e}")

    # Markdown을 Notion blocks로 변환
    print("🔄 Converting markdown to Notion blocks...")
    block_batches = parse_markdown_to_blocks(content)
    print(f"   Created {sum(len(batch) for batch in block_batches)} blocks in {len(block_batches)} batches")

    # Notion 페이지에 업로드
    print(f"📤 Uploading to Notion page: {page_id}...")

    try:
        # 페이지 정보 가져오기
        page = notion.pages.retrieve(page_id=page_id)
        try:
            title_prop = page.get('properties', {}).get('title', {})
            title_array = title_prop.get('title', [])
            if title_array and len(title_array) > 0:
                page_title = title_array[0].get('plain_text', 'Untitled')
            else:
                page_title = 'Untitled'
        except:
            page_title = 'Untitled'
        print(f"✅ Found page: {page_title}")

        # 각 배치를 순차적으로 업로드
        for idx, blocks in enumerate(block_batches, 1):
            print(f"   Uploading batch {idx}/{len(block_batches)} ({len(blocks)} blocks)...")
            notion.blocks.children.append(block_id=page_id, children=blocks)
            print(f"   ✅ Batch {idx} uploaded successfully")

        print("\n" + "="*60)
        print("✅ 업로드 완료!")
        print("="*60)
        print(f"\nNotion 페이지: https://notion.so/{page_id.replace('-', '')}")
        print(f"총 {sum(len(batch) for batch in block_batches)} blocks 업로드됨")

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()


def main():
    print("="*60)
    print("Notion 업로드: week3/lecture_notes.md")
    print("="*60)
    print()

    # 페이지 ID 확인
    if len(sys.argv) > 1:
        page_id = sys.argv[1]
    else:
        page_id = DEFAULT_PAGE_ID
        print(f"Using default page ID: {page_id}")

    # 파일 경로
    script_dir = os.path.dirname(os.path.abspath(__file__))
    md_file = os.path.join(script_dir, 'lecture_notes.md')

    if not os.path.exists(md_file):
        print(f"❌ Error: {md_file} 파일을 찾을 수 없습니다.")
        return

    upload_to_notion(page_id, md_file)


if __name__ == '__main__':
    main()

