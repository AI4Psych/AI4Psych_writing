# Top Tier Journal Introduction 예제 수집 프롬프트

> **목적**: Impact Factor 상위 10% 탑티어 저널에서만 실제 Introduction 예제 수집
> **대상**: 심리학/행동과학 분야 중심
> **제외**: Journal of Political Economy (경제학 저널), Frontiers in Psychology (IF 낮음)

---

## 📋 1단계: 저널 선별 기준

### ✅ 포함 저널 (Impact Factor 상위 10%)

**Tier 1 (IF > 20)**
- Nature (IF ~69)
- Science (IF ~63)
- Nature Human Behaviour (IF ~29)
- JAMA Psychiatry (IF ~25)
- Nature Neuroscience (IF ~25)
- Trends in Cognitive Sciences (IF ~24)
- Annual Review of Psychology (IF ~24)

**Tier 2 (IF 10-20)**
- PNAS (IF ~12)
- Psychological Science (IF ~11)
- Current Biology (IF ~15)
- Neuron (IF ~16)
- Psychological Review (IF ~13)
- Nature Communications (IF ~17)

### ❌ 제외 저널
- Journal of Political Economy (경제학 저널, 심리학 아님)
- Frontiers in Psychology (IF 낮음, 상위 10% 아님)
- 기타 IF < 10 저널

---

## 📋 2단계: 검색 전략

### A. Mechanistic Gap 예제 (Frontiers in Psychology 대체)

**타겟 저널**: JAMA Psychiatry, Nature Neuroscience, Nature Human Behaviour

**검색 쿼리**:
```
Tavily Search:
1. "JAMA Psychiatry" cognitive behavioral therapy CBT neural mechanisms fMRI introduction 2020 2021 2022 2023
2. "Nature Neuroscience" psychotherapy treatment mechanisms brain introduction 2020 2021 2022
3. "Nature Human Behaviour" clinical intervention mechanisms introduction 2020 2021 2022
```

**필터링 기준**:
- ✅ 2020-2024년 논문
- ✅ Introduction 섹션 포함
- ✅ Mechanistic gap 명확 (현상은 알려져 있으나 기전 불명)
- ✅ 심리학/행동과학 관련
- ❌ Review/Opinion 제외 (Original Research만)

**우선순위**:
1. JAMA Psychiatry (임상심리학, IF 25)
2. Nature Neuroscience (신경과학, IF 25)
3. Nature Human Behaviour (행동과학, IF 29)

---

### B. Translational Gap 예제 (Journal of Political Economy 대체)

**타겟 저널**: Science, Nature, Nature Human Behaviour, PNAS

**검색 쿼리**:
```
Tavily Search:
1. "Science" psychology intervention program long-term effects mechanisms introduction 2020 2021 2022
2. "Nature" cognitive training educational policy translation introduction 2020 2021 2022
3. "Nature Human Behaviour" early childhood intervention mechanisms introduction 2020 2021 2022
4. "PNAS" psychology intervention real-world application introduction 2020 2021 2022
```

**필터링 기준**:
- ✅ 2020-2024년 논문
- ✅ Introduction 섹션 포함
- ✅ Translational gap 명확 (기초 연구 → 실제 응용 연결 불명)
- ✅ 심리학/행동과학/교육 관련
- ❌ Review/Opinion 제외

**우선순위**:
1. Science (IF 63, 최고 권위)
2. Nature (IF 69, 최고 권위)
3. Nature Human Behaviour (IF 29, 행동과학 전문)
4. PNAS (IF 12, 다학제)

---

## 📋 3단계: 논문 선별 및 검증

### 검증 체크리스트

각 논문에 대해 확인:

1. **저널 Impact Factor 확인**
   - [ ] IF > 10 (최소 기준)
   - [ ] 상위 10% 저널인지 확인
   - [ ] 심리학/행동과학 분야인지 확인

2. **Gap Type 확인**
   - [ ] Mechanistic Gap: 현상은 알려져 있으나 기전 불명
   - [ ] Translational Gap: 기초 연구 → 실제 응용 연결 불명
   - [ ] Introduction에서 gap이 명확히 제시되는지

3. **Introduction 구조 확인**
   - [ ] Established Knowledge (확립된 지식)
   - [ ] Emerging Challenges (새로운 도전)
   - [ ] Critical Gap (핵심 공백)
   - [ ] Research Opportunity (연구 기회)

4. **심리학/행동과학 관련성**
   - [ ] 주제가 심리학/행동과학인지
   - [ ] 인지심리학, 사회심리학, 임상심리학, 발달심리학, 행동경제학 등

---

## 📋 4단계: Introduction 발췌 및 분석

### 발췌 프로세스

1. **논문 URL 확인**
   - Tavily search 결과에서 실제 논문 URL 추출
   - Nature, Science, PNAS, JAMA Psychiatry 등 공식 사이트 URL 확인

2. **Introduction 섹션 추출**
   - Tavily-extract 사용하여 전체 논문 추출
   - Introduction 섹션만 발췌 (보통 "Introduction" 또는 "## Introduction" 헤딩 이후)

3. **4단계 구조 분석**
   - 각 단계별로 텍스트 발췌
   - 분석 포인트 작성:
     - Established Knowledge: Consensus 통합 여부
     - Emerging Challenges: 구체적 모순/한계 제시 여부
     - Critical Gap: 명확한 Gap Statement 여부
     - Research Opportunity: 구체적 방법과 예측 포함 여부

4. **예제 파일 업데이트**
   - `examples_introduction_top_tier_patterns.md`에 추가
   - 기존 Frontiers in Psychology, Journal of Political Economy 예제 교체

---

## 📋 5단계: 품질 검증

### 최종 검증 기준

각 예제는 다음을 만족해야 함:

1. **저널 권위**
   - ✅ IF > 10
   - ✅ 상위 10% 저널
   - ✅ 심리학/행동과학 분야

2. **Gap Type 명확성**
   - ✅ Mechanistic 또는 Translational Gap이 명확
   - ✅ Introduction에서 gap이 직접적으로 제시됨

3. **구조 완성도**
   - ✅ 4단계 구조 모두 포함
   - ✅ 각 단계가 명확히 구분됨

4. **분석 품질**
   - ✅ 각 단계별 분석 포인트 작성
   - ✅ 학습 포인트 명시

---

## 📋 6단계: 실행 순서

### Step 1: Mechanistic Gap 예제 찾기
```
1. Tavily search: "JAMA Psychiatry" + "CBT" + "neural mechanisms" + "introduction"
2. 결과에서 실제 논문 URL 추출
3. Tavily-extract로 Introduction 발췌
4. 4단계 구조 분석
5. 예제 파일에 추가 (Frontiers in Psychology 대체)
```

### Step 2: Translational Gap 예제 찾기
```
1. Tavily search: "Science" OR "Nature" + "intervention" + "long-term" + "introduction"
2. 결과에서 실제 논문 URL 추출
3. Tavily-extract로 Introduction 발췌
4. 4단계 구조 분석
5. 예제 파일에 추가 (Journal of Political Economy 대체)
```

### Step 3: 품질 검증
```
1. 각 예제의 저널 IF 확인
2. Gap type 명확성 확인
3. 구조 완성도 확인
4. 분석 품질 확인
```

---

## 📋 7단계: 대체 전략 (Plan B)

### 만약 Tier 1 저널에서 적합한 논문을 찾지 못할 경우

**Mechanistic Gap 대체 저널**:
- Psychological Science (IF 11)
- Current Biology (IF 15)
- Neuron (IF 16)

**Translational Gap 대체 저널**:
- PNAS (IF 12)
- Nature Human Behaviour (IF 29) - 이미 사용 중이지만 다른 주제로
- Psychological Review (IF 13)

---

## 📋 8단계: 최종 출력 형식

### 예제 파일 업데이트 형식

```markdown
### 예제 2.1: [주제] - [세부 주제] (실제 논문)

**저널**: [저널명] (Impact Factor: [IF])  
**연도**: [연도]  
**저자**: [저자명]  
**제목**: "[논문 제목]"  
**URL**: [논문 URL]

---

#### **단계 1: Established Knowledge (확립된 지식)**

[Introduction 발췌]

**분석**:
- ✅ [분석 포인트 1]
- ✅ [분석 포인트 2]
- ✅ [분석 포인트 3]

---

#### **단계 2: Emerging Challenges (새로운 도전)**

[Introduction 발췌]

**분석**:
- ✅ [분석 포인트 1]
- ✅ [분석 포인트 2]

---

#### **단계 3: Critical Gap (핵심 공백)**

[Introduction 발췌]

**분석**:
- ✅ [분석 포인트 1]
- ✅ [분석 포인트 2]

---

#### **단계 4: Research Opportunity (연구 기회)**

[Introduction 발췌]

**분석**:
- ✅ [분석 포인트 1]
- ✅ [분석 포인트 2]
```

---

## 📋 9단계: 실행 전 체크리스트

### 실행 전 확인사항

- [ ] 저널 선별 기준 명확 (IF > 10, 상위 10%)
- [ ] 검색 쿼리 구체화 완료
- [ ] 필터링 기준 명확
- [ ] 우선순위 설정 완료
- [ ] 대체 전략 준비 완료
- [ ] 출력 형식 확정

### 실행 시 주의사항

1. **저널 IF 확인**: 각 논문의 저널 IF를 반드시 확인
2. **Gap Type 명확성**: Introduction에서 gap이 명확히 제시되는지 확인
3. **심리학 관련성**: 주제가 심리학/행동과학인지 확인
4. **구조 완성도**: 4단계 구조가 모두 있는지 확인
5. **품질 우선**: 양보다 질, 탑티어 저널 논문만 선택

---

## 📋 10단계: 예상 소요 시간

- **Mechanistic Gap 예제 찾기**: 30-45분
  - 검색: 10분
  - 발췌: 15분
  - 분석: 20분

- **Translational Gap 예제 찾기**: 30-45분
  - 검색: 10분
  - 발췌: 15분
  - 분석: 20분

- **품질 검증**: 15분

**총 예상 시간**: 1.5-2시간

---

## 📋 11단계: 성공 기준

### 최종 성공 기준

1. ✅ **저널 권위**: 모든 예제가 IF > 10, 상위 10% 저널
2. ✅ **Gap Type**: Mechanistic과 Translational Gap 예제 각각 1개 이상
3. ✅ **구조 완성도**: 4단계 구조 모두 포함
4. ✅ **분석 품질**: 각 단계별 분석 포인트 작성
5. ✅ **심리학 관련성**: 모든 예제가 심리학/행동과학 분야

---

## 📋 12단계: 실행 명령어 (참고용)

### 실제 실행 시 사용할 명령어

```python
# Step 1: Mechanistic Gap 검색
tavily_search(
    query="JAMA Psychiatry cognitive behavioral therapy CBT neural mechanisms fMRI introduction 2020 2021 2022 2023",
    max_results=5,
    search_depth="advanced"
)

# Step 2: 논문 URL 추출 후 Introduction 발췌
tavily_extract(
    urls=["https://jamanetwork.com/journals/jamapsychiatry/article-abstract/..."],
    extract_depth="advanced",
    format="markdown"
)

# Step 3: Translational Gap 검색
tavily_search(
    query="Science psychology intervention program long-term effects mechanisms introduction 2020 2021 2022",
    max_results=5,
    search_depth="advanced"
)
```

---

**주의**: 이 프롬프트는 실행하지 말고, 검토 후 실행하세요.

