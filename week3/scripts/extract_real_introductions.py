#!/usr/bin/env python3
"""
실제 논문에서 Introduction 섹션을 발췌하는 스크립트

사용법:
    python extract_real_introductions.py

이 스크립트는:
1. Tavily로 실제 논문 검색
2. 논문 URL에서 Introduction 섹션 발췌
3. Gap-driven 구조 패턴별로 분류
4. examples_introduction_top_tier_patterns.md 업데이트
"""

import os
import json
import re
from typing import List, Dict, Optional
from pathlib import Path

# API 키는 환경변수에서 가져오거나 직접 설정
# 사용자가 제공한 API 키들을 여기에 설정할 수 있음

# 검색할 논문 쿼리 (패턴별)
SEARCH_QUERIES = {
    "conceptual_gap": [
        "Nature Human Behaviour working memory attention control introduction",
        "Nature Human Behaviour cognitive psychology conceptual framework introduction",
    ],
    "mechanistic_gap": [
        "JAMA Psychiatry cognitive behavioral therapy neural mechanisms introduction",
        "Nature Neuroscience mindfulness meditation neural pathways introduction",
    ],
    "translational_gap": [
        "Science early childhood intervention long-term effects introduction",
        "PNAS intervention program mechanisms introduction",
    ],
    "paradox_gap": [
        "Nature Human Behaviour gender differences cognitive abilities paradox introduction",
        "Science moral judgment cross-cultural contradiction introduction",
    ],
}

def extract_introduction_from_text(text: str) -> Optional[str]:
    """
    텍스트에서 Introduction 섹션을 발췌
    
    패턴:
    - "Introduction" 또는 "INTRODUCTION" 제목 찾기
    - 다음 섹션("Methods", "METHODS", "Background" 등) 전까지 추출
    """
    # Introduction 섹션 시작 패턴
    intro_patterns = [
        r'(?i)(?:^|\n)\s*(?:1\.\s*)?Introduction\s*(?:\n|$)',
        r'(?i)(?:^|\n)\s*INTRODUCTION\s*(?:\n|$)',
        r'(?i)(?:^|\n)\s*Introduction\s*\n',
    ]
    
    # 다음 섹션 패턴 (Introduction 종료 지점)
    next_section_patterns = [
        r'(?i)(?:^|\n)\s*(?:2\.\s*)?(?:Methods?|METHODS?|Materials?\s+and\s+Methods?|Experimental\s+Procedures?|Study\s+Design)\s*(?:\n|$)',
        r'(?i)(?:^|\n)\s*(?:Results?|RESULTS?|Findings?)\s*(?:\n|$)',
        r'(?i)(?:^|\n)\s*(?:Background|BACKGROUND)\s*(?:\n|$)',
    ]
    
    # Introduction 시작 찾기
    intro_start = None
    for pattern in intro_patterns:
        match = re.search(pattern, text)
        if match:
            intro_start = match.start()
            break
    
    if intro_start is None:
        return None
    
    # 다음 섹션 시작 찾기
    remaining_text = text[intro_start:]
    next_section_start = len(remaining_text)
    
    for pattern in next_section_patterns:
        match = re.search(pattern, remaining_text)
        if match and match.start() > 100:  # 최소 100자 이상 떨어져야 함
            next_section_start = match.start()
            break
    
    introduction = remaining_text[:next_section_start].strip()
    
    # 너무 짧으면 None 반환
    if len(introduction) < 200:
        return None
    
    return introduction

def analyze_gap_structure(introduction: str) -> Dict:
    """
    Introduction의 Gap-driven 구조 분석
    
    Returns:
        {
            "established_knowledge": str,
            "emerging_challenges": str,
            "critical_gap": str,
            "research_opportunity": str,
            "gap_type": str,  # conceptual, mechanistic, translational, paradox
        }
    """
    # 단락으로 분리
    paragraphs = [p.strip() for p in introduction.split('\n\n') if p.strip()]
    
    analysis = {
        "established_knowledge": "",
        "emerging_challenges": "",
        "critical_gap": "",
        "research_opportunity": "",
        "gap_type": "unknown",
    }
    
    # 패턴 기반 분석
    # Established Knowledge: 초반 단락들, "established", "well-known", "extensive research" 등
    # Emerging Challenges: "however", "but", "challenge", "paradox", "contradiction" 등
    # Critical Gap: "gap", "unknown", "unclear", "remains to be", "we do not know" 등
    # Research Opportunity: "here", "we propose", "we test", "this study" 등
    
    established_keywords = ["established", "well-known", "extensive", "previous", "prior", "consensus"]
    challenge_keywords = ["however", "but", "although", "challenge", "paradox", "contradiction", "puzzling"]
    gap_keywords = ["gap", "unknown", "unclear", "remains", "lacks", "we do not know", "critical question"]
    opportunity_keywords = ["here", "we propose", "we test", "this study", "we investigate", "we examine"]
    
    established_paragraphs = []
    challenge_paragraphs = []
    gap_paragraphs = []
    opportunity_paragraphs = []
    
    for para in paragraphs:
        para_lower = para.lower()
        
        # Established Knowledge
        if any(kw in para_lower for kw in established_keywords) and not any(kw in para_lower for kw in challenge_keywords):
            established_paragraphs.append(para)
        
        # Emerging Challenges
        if any(kw in para_lower for kw in challenge_keywords):
            challenge_paragraphs.append(para)
        
        # Critical Gap
        if any(kw in para_lower for kw in gap_keywords):
            gap_paragraphs.append(para)
        
        # Research Opportunity
        if any(kw in para_lower for kw in opportunity_keywords):
            opportunity_paragraphs.append(para)
    
    analysis["established_knowledge"] = "\n\n".join(established_paragraphs[:2])  # 최대 2개 단락
    analysis["emerging_challenges"] = "\n\n".join(challenge_paragraphs[:2])
    analysis["critical_gap"] = "\n\n".join(gap_paragraphs[:1])
    analysis["research_opportunity"] = "\n\n".join(opportunity_paragraphs[:2])
    
    # Gap type 판단
    if any("mechanism" in p.lower() or "how" in p.lower() for p in gap_paragraphs):
        analysis["gap_type"] = "mechanistic"
    elif any("paradox" in p.lower() or "contradiction" in p.lower() for p in challenge_paragraphs):
        analysis["gap_type"] = "paradox"
    elif any("translate" in p.lower() or "application" in p.lower() or "intervention" in p.lower() for p in gap_paragraphs):
        analysis["gap_type"] = "translational"
    elif any("framework" in p.lower() or "theory" in p.lower() or "model" in p.lower() for p in gap_paragraphs):
        analysis["gap_type"] = "conceptual"
    
    return analysis

def format_introduction_example(
    title: str,
    journal: str,
    year: str,
    authors: str,
    url: str,
    introduction: str,
    analysis: Dict
) -> str:
    """
    Introduction 예제를 마크다운 형식으로 포맷팅
    """
    gap_type_map = {
        "conceptual": "Conceptual Gap (개념적 공백)",
        "mechanistic": "Mechanistic Gap (기전적 공백)",
        "translational": "Translational Gap (전이적 공백)",
        "paradox": "Paradox Gap (모순 공백)",
    }
    
    gap_type_kr = gap_type_map.get(analysis["gap_type"], "Unknown")
    
    markdown = f"""### 예제: {title}

**저널**: {journal}  
**연도**: {year}  
**저자**: {authors}  
**URL**: {url}  
**Gap Type**: {gap_type_kr}

---

#### **단계 1: Established Knowledge (확립된 지식)**

{analysis["established_knowledge"] or "*[발췌 실패 - 원문 확인 필요]*"}

**분석**:
- ✅ Consensus 통합 여부 확인
- ✅ 다층적 증거 제시 여부
- ✅ 인용 전략 분석

---

#### **단계 2: Emerging Challenges (새로운 도전)**

{analysis["emerging_challenges"] or "*[발췌 실패 - 원문 확인 필요]*"}

**분석**:
- ✅ 구체적 모순/한계 제시 여부
- ✅ Paradox 제시 여부
- ✅ 이론적 도전 명확성

---

#### **단계 3: Critical Gap (핵심 공백)**

{analysis["critical_gap"] or "*[발췌 실패 - 원문 확인 필요]*"}

**분석**:
- ✅ 명확한 Gap Statement 여부
- ✅ Gap Type 분류 정확성
- ✅ 구체적 하위 질문 제시 여부

---

#### **단계 4: Research Opportunity (연구 기회)**

{analysis["research_opportunity"] or "*[발췌 실패 - 원문 확인 필요]*"}

**분석**:
- ✅ 구체적 방법 제시 여부
- ✅ Testable Prediction 여부
- ✅ Broader Impact 언급 여부

---

#### **전체 Introduction (원문)**

```
{introduction[:2000]}...
```

*[전체 텍스트는 URL에서 확인]*

---

"""
    return markdown

def main():
    """
    메인 실행 함수
    
    실제로는 Tavily API를 호출하거나,
    이미 다운로드한 논문 텍스트를 분석해야 함
    """
    print("실제 논문 Introduction 발췌 스크립트")
    print("=" * 50)
    print("\n이 스크립트는 Tavily MCP 서버를 통해 실행되어야 합니다.")
    print("또는 이미 다운로드한 논문 텍스트 파일을 분석할 수 있습니다.")
    print("\n사용법:")
    print("1. Tavily로 논문 검색 및 텍스트 추출")
    print("2. 이 스크립트로 Introduction 발췌")
    print("3. Gap-driven 구조 분석")
    print("4. examples_introduction_top_tier_patterns.md 업데이트")

if __name__ == "__main__":
    main()

