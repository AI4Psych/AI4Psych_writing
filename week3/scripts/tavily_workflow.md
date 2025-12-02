# Tavily를 사용한 실제 논문 Introduction 발췌 워크플로우

## 목표

실제 탑티어 저널 논문에서 Introduction 섹션을 발췌하여 `examples_introduction_top_tier_patterns.md`를 업데이트

## 단계별 실행

### Step 1: 논문 검색 (각 패턴별)

#### Conceptual Gap 예제 찾기

```bash
# Nature Human Behaviour - Working Memory & Attention
mcp_tavily_tavily-search \
  --query "Nature Human Behaviour working memory capacity attention control introduction full text" \
  --max-results 5 \
  --search-depth advanced \
  --include-raw-content true

# Nature Human Behaviour - Cognitive Psychology
mcp_tavily_tavily-search \
  --query "Nature Human Behaviour cognitive psychology conceptual framework introduction" \
  --max-results 5 \
  --search-depth advanced
```

#### Mechanistic Gap 예제 찾기

```bash
# JAMA Psychiatry - CBT Neural Mechanisms
mcp_tavily_tavily-search \
  --query "JAMA Psychiatry cognitive behavioral therapy neural mechanisms introduction full text" \
  --max-results 5 \
  --search-depth advanced \
  --include-raw-content true

# Nature Neuroscience - Mindfulness
mcp_tavily_tavily-search \
  --query "Nature Neuroscience mindfulness meditation neural pathways introduction" \
  --max-results 5 \
  --search-depth advanced
```

#### Translational Gap 예제 찾기

```bash
# Science - Early Intervention
mcp_tavily_tavily-search \
  --query "Science early childhood intervention long-term effects mechanisms introduction" \
  --max-results 5 \
  --search-depth advanced \
  --include-raw-content true

# PNAS - Intervention Programs
mcp_tavily_tavily-search \
  --query "PNAS intervention program mechanisms long-term introduction" \
  --max-results 5 \
  --search-depth advanced
```

#### Paradox Gap 예제 찾기

```bash
# Nature Human Behaviour - Gender Differences
mcp_tavily_tavily-search \
  --query "Nature Human Behaviour gender differences cognitive abilities paradox introduction" \
  --max-results 5 \
  --search-depth advanced \
  --include-raw-content true

# Science - Moral Judgment
mcp_tavily_tavily-search \
  --query "Science moral judgment cross-cultural contradiction introduction" \
  --max-results 5 \
  --search-depth advanced
```

### Step 2: 논문 URL 추출 및 텍스트 발췌

검색 결과에서 실제 논문 URL을 찾아서:

```bash
# 예시: Nature Human Behaviour 논문
mcp_tavily_tavily-extract \
  --urls "https://www.nature.com/articles/s41562-020-xxxx-x" \
  --extract-depth advanced \
  --format markdown

# 예시: JAMA Psychiatry 논문
mcp_tavily_tavily-extract \
  --urls "https://jamanetwork.com/journals/jamapsychiatry/fullarticle/xxxxx" \
  --extract-depth advanced \
  --format markdown
```

### Step 3: Introduction 섹션 발췌

발췌한 텍스트에서 Introduction 섹션만 추출:

1. "Introduction" 또는 "INTRODUCTION" 제목 찾기
2. 다음 섹션("Methods", "METHODS", "Results" 등) 전까지 추출
3. 4단계 구조 분석:
   - Established Knowledge
   - Emerging Challenges
   - Critical Gap
   - Research Opportunity

### Step 4: Gap Type 분류

각 Introduction을 다음 중 하나로 분류:

- **Conceptual Gap**: 새로운 프레임워크/이론 필요
- **Mechanistic Gap**: 작동 원리(mechanism) 불명확
- **Translational Gap**: 기초→응용 연결 안 됨
- **Paradox Gap**: 모순되는 결과들 존재

### Step 5: 예제 파일 업데이트

발췌한 Introduction을 `examples_introduction_top_tier_patterns.md`에 추가:

```markdown
## 🎯 패턴 1: Conceptual Gap (개념적 공백)

### 예제 1.1: [실제 논문 제목]

**저널**: Nature Human Behaviour  
**연도**: 2023  
**저자**: [저자명]  
**URL**: [논문 URL]

#### 단계 1: Established Knowledge
[발췌된 텍스트]

#### 단계 2: Emerging Challenges
[발췌된 텍스트]

#### 단계 3: Critical Gap
[발췌된 텍스트]

#### 단계 4: Research Opportunity
[발췌된 텍스트]
```

## 검색 전략

### 효과적인 검색 쿼리 작성

1. **저널명 포함**: "Nature Human Behaviour", "JAMA Psychiatry" 등
2. **주제 키워드**: "working memory", "cognitive behavioral therapy" 등
3. **섹션 명시**: "introduction" 추가
4. **전체 텍스트**: "full text" 추가 (가능한 경우)

### 필터링 기준

- ✅ 최근 5년 이내 논문 우선
- ✅ 심리학/행동과학 분야
- ✅ Introduction이 명확히 구분된 논문
- ✅ Gap-driven 구조가 뚜렷한 논문

## 예상 소요 시간

- 논문 검색: 각 패턴당 5-10분
- 텍스트 발췌: 각 논문당 2-3분
- Introduction 분석: 각 논문당 5-10분
- 파일 업데이트: 각 예제당 10-15분

**총 예상 시간**: 패턴당 1-2시간, 전체 4-8시간

## 체크리스트

각 패턴별로 최소 1-2개 예제 수집:

- [ ] Conceptual Gap: Nature Human Behaviour 예제 1-2개
- [ ] Mechanistic Gap: JAMA Psychiatry 예제 1-2개
- [ ] Translational Gap: Science/PNAS 예제 1-2개
- [ ] Paradox Gap: Nature Human Behaviour/Science 예제 1-2개

## 다음 단계

1. ✅ 워크플로우 문서 작성 완료
2. ⏳ 실제 논문 검색 시작
3. ⏳ Introduction 발췌
4. ⏳ 예제 파일 업데이트

