#!/usr/bin/env python3
"""
Notion 페이지 제목 업데이트

사용법:
    python update_page_title.py
    또는
    python update_page_title.py <page_id> <new_title>
"""

import os
import sys
from notion_client import Client

# Notion API 설정
NOTION_TOKEN = os.getenv('NOTION_TOKEN')

# 기본 페이지 ID
DEFAULT_PAGE_ID = "29f41454561d817c842df653dac8b2cd"

# 새 제목 (lecture_notes.md의 첫 번째 줄에서 가져옴)
NEW_TITLE = "3주차 강의노트: Introduction 잘쓰기"


def update_page_title(page_id: str, new_title: str):
    """Notion 페이지 제목 업데이트"""

    if not NOTION_TOKEN:
        print("❌ Error: NOTION_TOKEN 환경 변수가 설정되지 않았습니다.")
        print("   export NOTION_TOKEN='your_token_here'")
        return

    # Notion 클라이언트 초기화
    notion = Client(auth=NOTION_TOKEN)

    try:
        # 페이지 정보 가져오기
        page = notion.pages.retrieve(page_id=page_id)
        
        # 현재 제목 확인
        try:
            title_prop = page.get('properties', {}).get('title', {})
            title_array = title_prop.get('title', [])
            if title_array and len(title_array) > 0:
                current_title = title_array[0].get('plain_text', 'Untitled')
            else:
                current_title = 'Untitled'
        except:
            current_title = 'Untitled'
        
        print(f"현재 제목: {current_title}")
        print(f"새 제목: {new_title}")

        # 페이지 제목 업데이트
        notion.pages.update(
            page_id=page_id,
            properties={
                'title': {
                    'title': [
                        {
                            'text': {
                                'content': new_title
                            }
                        }
                    ]
                }
            }
        )

        print(f"\n✅ 페이지 제목이 업데이트되었습니다!")
        print(f"   {current_title} → {new_title}")

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()


def main():
    print("="*60)
    print("Notion 페이지 제목 업데이트")
    print("="*60)
    print()

    # 페이지 ID 확인
    if len(sys.argv) > 1:
        page_id = sys.argv[1].strip()
    else:
        page_id = DEFAULT_PAGE_ID
        print(f"Using default page ID: {page_id}")

    # 새 제목 확인
    if len(sys.argv) > 2:
        new_title = sys.argv[2].strip()
    else:
        new_title = NEW_TITLE
        print(f"Using default title: {new_title}")

    # URL에서 ID 추출
    if 'notion.so/' in page_id:
        page_id = page_id.split('notion.so/')[-1].split('?')[0]

    # 하이픈 없는 ID를 하이픈 있는 형식으로 변환
    if '-' not in page_id and len(page_id) == 32:
        page_id = f"{page_id[:8]}-{page_id[8:12]}-{page_id[12:16]}-{page_id[16:20]}-{page_id[20:]}"

    if not page_id:
        print("❌ Error: Page ID 필요")
        return

    print(f"\n📍 Page ID: {page_id}")
    print(f"📝 New Title: {new_title}\n")

    update_page_title(page_id, new_title)


if __name__ == '__main__':
    main()

