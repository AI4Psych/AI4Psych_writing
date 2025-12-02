# 실제 논문 Introduction 발췌 시스템

## 개요

이 시스템은 실제 탑티어 저널 논문에서 Introduction 섹션을 발췌하고, Gap-driven 구조 패턴별로 분류하여 `examples_introduction_top_tier_patterns.md`를 업데이트합니다.

## 워크플로우

### 1단계: 논문 검색 (Tavily MCP 사용)

```bash
# 각 패턴별로 논문 검색
# Conceptual Gap
mcp_tavily_tavily-search "Nature Human Behaviour working memory attention control introduction"

# Mechanistic Gap  
mcp_tavily_tavily-search "JAMA Psychiatry cognitive behavioral therapy neural mechanisms introduction"

# Translational Gap
mcp_tavily_tavily-search "Science early childhood intervention long-term effects introduction"

# Paradox Gap
mcp_tavily_tavily-search "Nature Human Behaviour gender differences cognitive abilities paradox introduction"
```

### 2단계: 논문 텍스트 추출 (Tavily Extract)

검색 결과에서 실제 논문 URL을 찾아서:

```bash
mcp_tavily_tavily-extract --urls "https://www.nature.com/articles/..." --extract-depth advanced
```

### 3단계: Introduction 발췌

`extract_real_introductions.py` 스크립트를 사용하여:
- Introduction 섹션 자동 발췌
- Gap-driven 구조 분석 (4단계)
- Gap type 분류

### 4단계: 예제 파일 업데이트

발췌한 Introduction을 `examples_introduction_top_tier_patterns.md`에 추가

## 사용 방법

### 방법 1: Python 스크립트 사용

```python
from scripts.extract_real_introductions import extract_introduction_from_text, analyze_gap_structure

# 논문 텍스트 읽기
with open("paper.txt", "r") as f:
    text = f.read()

# Introduction 발췌
introduction = extract_introduction_from_text(text)

# 구조 분석
analysis = analyze_gap_structure(introduction)
```

### 방법 2: 수동 발췌

1. Tavily 검색 결과에서 논문 URL 확인
2. 논문 PDF 또는 웹 페이지에서 Introduction 섹션 복사
3. `examples_introduction_top_tier_patterns.md`에 수동 추가

## 필요한 패키지

```bash
pip install requests beautifulsoup4
```

## API 키 설정

API 키는 환경변수로 설정하거나 스크립트에 직접 입력:

```python
# .env 파일 또는 환경변수
TAVILY_API_KEY=your_key_here
```

## 출력 형식

각 예제는 다음 형식으로 저장:

```markdown
### 예제: [논문 제목]

**저널**: [저널명]
**연도**: [연도]
**저자**: [저자]
**URL**: [URL]
**Gap Type**: [Conceptual/Mechanistic/Translational/Paradox]

#### 단계 1: Established Knowledge
[발췌된 텍스트]

#### 단계 2: Emerging Challenges
[발췌된 텍스트]

#### 단계 3: Critical Gap
[발췌된 텍스트]

#### 단계 4: Research Opportunity
[발췌된 텍스트]
```

## 다음 단계

1. ✅ 스크립트 작성 완료
2. ⏳ Tavily로 실제 논문 검색
3. ⏳ Introduction 발췌
4. ⏳ 예제 파일 업데이트

