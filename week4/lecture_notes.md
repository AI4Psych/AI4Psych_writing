# 4주차 강의노트: AI 활용Ⅲ – Methods/Results Bulletproofing 전략

> **전제**: 윤경생 박사님 강의에서 Chain-of-Thought (CoT) 프롬프팅을 이미 학습했다는 전제하에 진행합니다. 본 강의에서는 CoT **기법**이 아닌, "어떻게 하면 탑티어 저널 리뷰어의 methodological/statistical 공격을 방어할 수 있는 Methods/Results를 작성하는가?"에 집중합니다.

## 학습 목표
- **탑티어 저널의 Methods/Results 거부 사유** 파악 및 예방
- **Reproducibility, control, statistical rigor** 체크리스트 실행
- **Overclaiming 방지 및 transparent reporting** 전략 적용
- AI를 활용한 self-critique 및 preemptive reviewer response
- **궁극 목표: 리뷰어의 methodological/statistical 공격을 방어할 수 있는 Methods/Results 작성 능력 개발**

---

## 📚 수업 전 준비 (과제)

**필수 과제**: Methods & Results 섹션 초안 작성
- **Methods** (800-1000 words): Participants, Materials, Procedure, Analysis 포함
- **Results** (600-800 words): 주요 결과 + 최소 1개 Figure/Table
- Week 3의 gap을 해결하는 연구 방법론 제시
- 완벽하지 않아도 됨 - 수업에서 AI로 bulletproofing할 예정

**사전 읽기 (선택):**
- Genesis Mission Executive Order (AI-Accelerated Science Discovery)
  - https://www.whitehouse.gov/presidential-actions/2025/11/launching-the-genesis-mission/
  - "AI가 과학 연구를 어떻게 변화시키는가"에 대한 토론 준비

---

## 🎓 100분 Workshop 구조 (확장)

**Opening Discussion 15분** + **강의 15분** + **Workshop/Discussion 70분**

---

## 🌍 Opening Discussion: Genesis Mission & AI in Science (15분)

### Genesis Mission: 미국의 AI 과학 가속화 전략

**배경 읽기**: [Genesis Mission Executive Order (2025.11)](https://www.whitehouse.gov/presidential-actions/2025/11/launching-the-genesis-mission/)

> "This order launches the Genesis Mission as a dedicated, coordinated national effort to unleash a new age of AI-accelerated innovation and discovery that can solve the most challenging problems of this century."

#### 핵심 내용 요약

**Genesis Mission의 목표:**
- 연방 과학 데이터셋(세계 최대 규모)을 활용해 과학 기반 모델 훈련
- AI 에이전트를 통한 가설 테스트, 연구 워크플로우 자동화
- 과학 발견의 극적 가속화

**American Science and Security Platform:**
1. 고성능 컴퓨팅 자원 (국립연구소 슈퍼컴퓨터 + 클라우드 AI)
2. AI 모델링 및 분석 프레임워크
3. 도메인별 기반 모델 (foundation models)
4. 자율/AI-증강 실험 및 제조 도구

**국가적 과학기술 도전 과제 (20개 이상 선정):**
- 첨단 제조, 바이오테크놀로지, 핵심 재료
- 핵분열/핵융합 에너지, 양자정보과학, 반도체

#### 토론 질문 (10분)

**[전체 토론]** 다음 질문에 대해 생각해보고, 2-3명과 짧게 논의하세요:

1. **AI와 연구 방법론의 변화**
   - "AI가 Methods 섹션을 어떻게 바꿀 것인가?"
   - 현재: 연구자가 설계, 수행, 분석
   - 미래: AI 에이전트가 가설 생성, 실험 설계, 자동 분석?

2. **재현성과 AI**
   - "AI가 생성한 연구 방법론은 더 재현 가능할까, 덜 재현 가능할까?"
   - AI 코드와 파라미터가 완벽히 기록된다면?
   - "Black box" AI 모델의 해석 가능성 문제는?

3. **내 연구에 적용한다면**
   - "Genesis Mission 스타일의 AI 플랫폼이 있다면, 내 연구에서 어떻게 활용할 수 있을까?"
   - 데이터 수집 자동화? 문헌 분석? 가설 생성?
   - 한계와 윤리적 고려사항은?

#### 연결점: 왜 지금 Methods/Results Bulletproofing이 중요한가

**핵심 메시지:**

> AI 시대에도 (어쩌면 AI 시대이기에 더욱) **투명하고 재현 가능한 연구 방법론**이 중요합니다.
>
> - AI가 분석을 돕더라도, 인간이 **설계의 논리와 타당성을 검증**해야 합니다
> - AI 도구 사용 시 **버전, 파라미터, 프롬프트**까지 Methods에 기술해야 합니다
> - "AI가 했다"는 변명이 아닌, **AI를 어떻게 사용했는지** 투명하게 보고해야 합니다

**이번 강의의 목표:**
- 리뷰어 공격을 방어할 수 있는 철저한 Methods/Results 작성
- AI 시대에도 변하지 않는 원칙: Reproducibility, Control, Rigor, Transparency

---

**강의 15-20분** + **Workshop/Discussion 70-75분**

학생들은 자신의 Methods/Results를 가지고 와서:
- AI로 reproducibility audit (취약점 10개 찾기)
- Control strategy 검증 (alternative explanation 배제)
- Statistical rigor 체크 (power, assumptions, effect size)
- Overclaiming 방지 (claim-evidence match)
- Preemptive reviewer response (예상 질문 대응)
- 동료 피드백 및 개선

---

## 📊 90분 In-Class Workshop 진행

### 짧은 강의 (15-20분)

**핵심 개념 리뷰:**

## 1. 탑티어 저널의 Methods/Results 거부 사유

### 1.1 Common Rejection Patterns

#### Methods 섹션 거부 사유 (Top 5)

1. **Insufficient detail for reproduction**
   - "다른 연구자가 이 연구를 재현할 수 없다"
   - 예: 자극 생성 과정 불명확, 통계 파라미터 누락

2. **Inadequate controls**
   - "대안 설명을 배제하지 못했다"
   - 예: Confound 변수 통제 안 됨, negative control 없음

3. **Sample size/power issues**
   - "통계적 검정력이 부족하다"
   - 예: N 정당화 없음, multiple comparison 고려 안 됨

4. **Inappropriate statistics**
   - "분석 방법이 데이터 구조에 맞지 않다"
   - 예: 가정 위배, 잘못된 검정 선택

5. **Validation gaps**
   - "측정 도구/방법의 타당성 입증 부족"
   - 예: Manipulation check 없음, 신뢰도/타당도 보고 안 됨

#### Results 섹션 거부 사유 (Top 5)

1. **Overclaiming**
   - "데이터가 뒷받침하지 않는 주장"
   - 예: Correlation을 causation으로 주장

2. **Cherry-picking**
   - "일부 결과만 선택적 보고"
   - 예: Hypothesis에 맞는 것만 보고, 안 맞는 것 숨김

3. **Statistical issues**
   - "다중 비교 보정 누락, p-hacking 의심"
   - 예: 20개 비교 중 1개만 유의 → 그것만 보고

4. **Unclear presentation**
   - "핵심 결과가 무엇인지 불명확"
   - 예: 엄청난 양의 결과 나열, 중요도 구분 안 됨

5. **Weak effect sizes**
   - "통계적 유의성은 있지만 실질적 의미 미약"
   - 예: p < 0.001 but Cohen's d = 0.1

### 1.2 실습: Rejection Reason 진단

**활동:**
교수가 제시하는 3개의 Methods/Results 예시를 읽고, 각각의 거부 사유를 10가지 카테고리에서 찾기

**AI 프롬프트 레시피:**
```
"다음 Methods 섹션을 Nature 리뷰어 관점에서 평가해줘:
[Methods text]

다음 5가지 측면에서 약점을 지적:
1. Reproducibility (재현성)
2. Controls (통제)
3. Sample size/power (샘플/검정력)
4. Statistical appropriateness (통계 적절성)
5. Validation (타당성)

각 약점에 대해:
- 구체적 문제점
- 리뷰어가 제기할 질문
- 개선 방안"
```

---

## 2. Methods 섹션 Bulletproofing 전략

### 2.1 Reproducibility Checklist

**"다른 연구자가 정확히 재현할 수 있는가?"**

#### 필수 포함 요소

- [ ] **Participants/Subjects**
  - 모집 방법 및 장소
  - Inclusion/exclusion criteria (구체적 기준)
  - N (최종 분석 포함 + excluded N + 이유)
  - Demographics (M age, SD, gender, education 등)

- [ ] **Materials**
  - 자극/도구의 구체적 설명
  - 출처 (published source, custom-made)
  - 버전 (소프트웨어, 척도)
  - 신뢰도/타당도 (Cronbach's α, validation reference)

- [ ] **Procedure**
  - Step-by-step protocol (순서대로)
  - 각 단계의 타이밍/지속 시간
  - 지시문 (verbatim or paraphrased)
  - 실험 환경 (조명, 거리, 화면 크기 등)

- [ ] **Parameters**
  - 모든 변수의 정확한 값
  - 범위, 단위
  - Randomization/counterbalancing 방법

- [ ] **Software/Equipment**
  - 이름, 버전, manufacturer
  - 설정값 (resolution, sampling rate 등)

- [ ] **Data processing**
  - Raw data → analyzed data 변환 과정
  - Preprocessing steps (filtering, normalization 등)
  - Exclusion criteria for trials/participants

#### AI-assisted Reproducibility Audit

```
프롬프트:
"다음 Methods 섹션을 읽고, 다른 연구자가 재현하려 할 때
막힐 수 있는 지점 10가지를 찾아줘:
[Methods text]

각 지점에 대해:
1. 무엇이 불명확한가?
2. 어떤 정보가 추가로 필요한가?
3. 구체적으로 어떻게 기술해야 하는가?
   (Before → After 예시 포함)"
```

**예시 출력:**
```
지점 1: "Participants were recruited online"
문제: 어떤 플랫폼? 어떤 광고 문구?
필요 정보: 모집 플랫폼, 광고 내용, screening 절차
개선:
Before: "Participants were recruited online"
After: "Participants were recruited via Prolific (www.prolific.co)
       using the screening criteria: native English speakers,
       18-35 years old, no history of neurological disorders"
```

---

### 2.2 Control Strategy Validation

**"대안 설명을 충분히 배제했는가?"**

#### 4가지 Control 유형

1. **Positive controls**
   - 기대되는 효과가 실제로 나타나는가?
   - 예: Known effective manipulation이 예상대로 작동하는지 확인

2. **Negative controls**
   - 효과가 없어야 할 조건에서 실제로 없는가?
   - 예: Sham stimulation 조건에서 효과 없음

3. **Confound controls**
   - 혼재 변수를 통제했는가?
   - 예: Task difficulty, arousal, expectation 통제

4. **Validation controls**
   - 측정이 의도한 것을 측정하는가?
   - 예: Manipulation check, attention check

#### AI-powered Alternative Explanation Generator

```
프롬프트:
"내 연구 디자인:
- Manipulation: [설명]
- Measurement: [설명]
- Expected result: [설명]

다음을 생성해줘:
1. Alternative explanations
   (내 조작 외에 결과를 설명할 수 있는 요인 5가지)
2. 각 alternative를 배제하기 위한 control 조건
3. 리뷰어가 지적할 가능성이 높은 confound 3가지
4. 각 confound를 다루는 방법

그리고 현재 내 Methods에서:
- 충분히 다뤄진 alternative는?
- 추가해야 할 control은?"
```

---

### 2.3 Statistical Power & Sample Size Justification

**"샘플 사이즈가 충분한가?"**

#### ❌ 약한 정당화 (거부 위험)
- "Previous studies used similar N" → 관례만 따름
- "We recruited as many as possible" → 계획 없음
- "N=30 is standard" → 근거 없음

#### ✅ 강한 정당화 (통과 가능)
- **A priori power analysis**
  - 예상 효과 크기 (d = 0.5, based on pilot study)
  - α = 0.05, power (1-β) = 0.80
  - 필요 N 계산 (G*Power 사용)

- **Effect size justification**
  - 왜 이 효과 크기를 기대하는가?
  - Pilot data or previous work citation

- **Sensitivity analysis**
  - 달성 가능한 minimum detectable effect
  - "With N=60, we can detect d ≥ 0.52"

- **Multiple comparisons**
  - Bonferroni/FDR 보정 후에도 충분한 power

#### AI-assisted Power Analysis Reviewer

```
프롬프트:
"내 연구 계획:
- Expected effect size: d = [value]
  (근거: [pilot/previous work])
- Sample size: N = [value]
- Alpha: 0.05
- Planned comparisons: [number]

리뷰어 관점에서 평가해줘:
1. Expected effect size가 현실적인가?
   (너무 크거나 작지 않은가?)
2. Multiple comparison 보정을 고려하면 power가 충분한가?
3. 샘플 사이즈 정당화에서 보강할 점은?
4. Sensitivity analysis 결과를 어떻게 제시해야 하는가?

그리고:
- 리뷰어가 제기할 가능성 높은 질문 3가지
- 각 질문에 대한 방어 전략"
```

---

## 3. Results 섹션 Bulletproofing 전략

### 3.1 Overclaiming Prevention

**"주장이 데이터를 넘어서지 않는가?"**

#### 흔한 Overclaiming 패턴

| Claim | Data | Problem | Conservative Alternative |
|-------|------|---------|--------------------------|
| "X **causes** Y" | Correlation between X and Y | Correlation ≠ Causation | "X is **associated with** Y" |
| "X is **necessary** for Y" | Y decreases when X is removed | Sufficiency not tested | "X **contributes to** Y" |
| "Our method **works in general**" | Tested in one specific condition | Generalization unsupported | "Our method works **in [condition]**" |
| "This **proves** theory Z" | Consistent with theory Z | Alternative theories not ruled out | "These findings are **consistent with** theory Z" |

#### AI-powered Claim Checker

```
프롬프트:
"다음 Results 문장들을 분석해줘:
[Results text with claims]

각 문장에 대해:
1. Claim type (causal/correlational/mechanistic/general)
2. Evidence level (direct/indirect/suggestive)
3. Overclaiming risk (1-10)
4. Conservative alternative phrasing

그리고:
- 가장 위험한 overclaim 3개 지적
- 각각을 데이터에 맞게 수정하는 방법"
```

---

### 3.2 Statistical Rigor Verification

**"통계 분석이 방어 가능한가?"**

#### Critical Checkpoints

- [ ] **Assumption testing**
  - Normality, homogeneity of variance, independence
  - 가정 위배 시 대안 분석 (non-parametric, transformation)

- [ ] **Multiple comparisons**
  - 보정 방법 명시 (Bonferroni, FDR, permutation)
  - Family-wise error rate vs false discovery rate

- [ ] **Effect sizes**
  - p-value만이 아닌 effect size + CI 보고
  - Cohen's d, η², r 등 (분석에 맞게)

- [ ] **Outlier handling**
  - 처리 방법 (removal, winsorization, robust methods)
  - 영향 평가 (with vs without outliers)

- [ ] **Missing data**
  - 처리 방법 (listwise deletion, imputation, mixed models)
  - Sensitivity analysis (different methods 비교)

- [ ] **Robustness checks**
  - Alternative analysis로 결과 확인
  - 예: Parametric + non-parametric 둘 다 보고

#### AI-assisted Statistical Review

```
프롬프트:
"내 Results 섹션:
- Analysis: [통계 분석 방법]
- Comparisons: [비교 횟수]
- Reported stats: [제시한 통계량]

리뷰어가 통계적으로 문제 삼을 수 있는 부분:
1. Assumption violations (어떤 가정이 문제?)
2. Multiple comparison issues (보정이 충분한가?)
3. P-hacking risks (의심받을 수 있는 분석 선택은?)
4. Missing robustness checks (어떤 추가 분석 필요?)

각 문제에 대해:
- 구체적 지적 내용
- 방어 전략
- 추가할 분석/보고 내용"
```

---

### 3.3 Transparent Reporting

**"모든 결과를 투명하게 보고했는가?"**

#### Selective reporting 위험 신호
- ❌ Hypothesis에 맞지 않는 결과 누락
- ❌ 일부 조건/측정치만 보고
- ❌ Failed manipulation checks 언급 없음
- ❌ Exploratory analysis를 confirmatory처럼 보고

#### ✅ 완전 투명 보고 전략

**Main Results:**
- 모든 planned comparison 보고 (유의/비유의 모두)
- Primary outcome measures 전부

**Supplementary:**
- 모든 측정 변수 결과 (메인에 안 들어간 것도)
- Manipulation checks
- Assumption testing 결과
- Robustness checks
- Excluded data + 이유
- Exploratory analyses (명확히 표시)

**Open Science:**
- Pre-registration (있다면 링크)
- Data/code availability statement
- Materials availability

#### AI-powered Transparency Checker

```
프롬프트:
"내 연구 계획:
- Hypotheses: [list]
- Planned comparisons: [list]
- Measured variables: [list]

현재 Results 섹션:
[Results text]

투명성 평가:
1. Planned 대비 보고된 비율 (%)
2. 누락된 결과가 있는가? 어떤 것?
3. Exploratory vs Confirmatory 구분이 명확한가?
4. Selective reporting 의심받을 수 있는 부분은?

개선 방안:
- Main에 추가할 결과
- Supplementary로 옮길 결과
- 투명성 강화를 위한 문구 제안"
```

---

## 4. Preemptive Reviewer Response 전략

### 4.1 "Reviewer가 물어볼 질문" 예측

#### AI를 활용한 Anticipated Questions 생성

```
프롬프트:
"내 Methods/Results:
[전체 텍스트]

Nature/Science 리뷰어가 제기할 가능성이 높은 질문 10가지를 생성해줘.
각 질문에 대해:
1. 질문 유형 (reproducibility/controls/statistics/interpretation)
2. 심각도 (critical/major/minor)
3. 현재 Methods/Results에서 답변이 있는가?
4. 없다면, Methods/Results에 추가할 내용
5. Rebuttal letter에서 답변할 내용

우선순위 순으로 정렬해줘."
```

#### Preemptive Defense 삽입
- **Critical questions** → Methods/Results에 직접 답변 추가
- **Major questions** → Supplementary에서 다룸
- **Minor questions** → Rebuttal에서만 대응

---

### 4.2 Methods/Results Cross-Validation

**"Methods에서 약속한 것을 Results에서 전부 다뤘는가?"**

#### 흔한 불일치
- ❌ Methods에서 언급한 분석이 Results에 없음
- ❌ Results의 분석이 Methods에 설명 안 됨
- ❌ Control 조건을 Methods에서 언급했지만 Results에 결과 없음
- ❌ Exclusion criteria 언급했지만 excluded N 보고 안 됨

#### AI-powered Consistency Checker

```
프롬프트:
"내 Methods 섹션:
[Methods text]

내 Results 섹션:
[Results text]

일관성 체크:
1. Methods에 있지만 Results에 없는 분석/측정/조건
2. Results에 있지만 Methods에 설명 없는 분석
3. 용어 불일치 (같은 것을 다르게 지칭)
4. 숫자 불일치 (N, df 등)

각 불일치에 대해:
- 문제 유형
- 수정 방법 (Methods 추가 vs Results 추가 vs 삭제)"
```

---

## 5. Effect Size & Significance 통합 보고

### 5.1 P-value만으로는 부족

#### ❌ 약한 보고
"p < 0.05이므로 유의하다"

#### ✅ 강한 보고 (권장 템플릿)
```
"Group A (M = 85.3, SD = 12.1) significantly outperformed
Group B (M = 72.4, SD = 10.8), t(98) = 5.43, p < .001,
Cohen's d = 1.12, 95% CI [0.71, 1.53]"
```

**포함 요소:**
- Descriptive stats (M, SD)
- Inferential stats (t, df, p)
- Effect size (Cohen's d)
- Confidence interval (95% CI)

---

### 5.2 Practical Significance vs Statistical Significance

**"통계적으로 유의하지만 실질적 의미는?"**

#### AI를 활용한 Practical Significance 평가

```
프롬프트:
"내 주요 발견:
- Effect size: Cohen's d = [value]
- Comparison: [experimental vs control/baseline/previous work]

다음을 평가해줘:
1. 이 effect size가 해당 분야에서 어느 정도 크기인가?
   (small/medium/large 절대 기준 말고, 분야 맥락에서)
2. Practical significance는?
   - 실제 응용 관점에서 의미 있는 차이인가?
   - Minimum clinically/practically important difference와 비교하면?
3. Effect size를 보고할 때 추가할 맥락 정보
   - 비교 대상 (이전 연구, 이론적 예측, 실용적 기준)
   - 신뢰구간 해석

리뷰어가 '통계적으로만 유의하고 실질적 의미 없다'고
지적할 위험이 있는가?"
```

---

## 6. 동료 Methods/Results Review 프로토콜

### 6.1 Structured Peer Review Template

**각 학생이 2명의 동료 Methods/Results를 평가:**

```
=== METHODS 평가 ===

1. Reproducibility (1-5점): ___
   - 내가 이 연구를 재현하려 할 때 막힐 부분:
   - 추가로 필요한 정보:

2. Controls (1-5점): ___
   - Alternative explanations이 충분히 배제됐는가?
   - 내가 리뷰어라면 추가할 control:

3. Statistical Justification (1-5점): ___
   - Sample size 정당화가 설득력 있는가?
   - 분석 방법이 데이터 구조에 적합한가?

=== RESULTS 평가 ===

4. Claim-Evidence Match (1-5점): ___
   - Overclaiming 위험이 있는 문장 (있다면 지적):
   - 보수적으로 수정할 방법:

5. Statistical Rigor (1-5점): ___
   - 빠진 통계량/검정:
   - Multiple comparison 처리 적절한가?

6. Transparency (1-5점): ___
   - 선택적 보고 의심 부분:
   - 추가로 보고해야 할 결과:

=== 종합 ===
- 가장 큰 약점 1가지:
- 개선 우선순위 top 3:
- Nature/Science 제출 준비도 (1-10):
```

---

## Workshop 실습 (85분)

> **수업 구조 (100분 총)**:
> - Opening Discussion: Genesis Mission (15분)
> - Workshop 실습 (85분)

### Phase 1: Bulletproofing Audit (20분)

**Activity 1 (10분): Methods reproducibility check**
- AI로 재현성 취약점 10가지 도출
- 각 취약점 개선 방법 논의

**Activity 2 (10분): Results claim checker**
- Overclaiming 위험 문장 식별
- Effect size + practical significance 평가

### Phase 2: Statistical Rigor (15분)

**Activity 3 (10분): Power analysis review**
- AI로 sample size 정당화 강화
- Multiple comparison 보정 체크

**Activity 4 (5분): Transparency audit**
- Selective reporting 위험 평가
- 추가 보고 필요 항목 리스트

### Phase 3: 저널 예제 & 학생 예시 비교 (20분) ⭐ NEW

> **저널 사례를 먼저 보고, 자신/동료의 글과 비교합니다.**
> 자세한 진행 방법은 **Section 8** 참조

**Activity 5 (5분): Quick Journal Benchmark**
- Section 7.6-7.7의 Nature/Science 템플릿 훑어보기
- 핵심 체크포인트 3가지 확인

**Activity 6 (10분): 동료 예시 교환 & 비교 분석**
- 2-3명 그룹 형성
- Section 8.2 비교 분석 템플릿 사용
- 저널 예제 vs 내 글 gap 분석

**Activity 7 (5분): 그룹 토론 & 개선점 도출**
- 가장 큰 gap 공유
- 즉시 수정 가능한 항목 리스트

### Phase 4: Peer Review (15분)

**Activity 8: Structured peer review**
- 2명 동료 평가 (Section 6.1 template 사용)
- 리뷰어 질문 예측 및 방어 전략 논의

### Phase 5: 최종 개선 + 공유 (15분)

**Activity 9 (10분): AI로 피드백 통합**
- 받은 피드백 반영한 개선안 생성
- Recipe #44, #45 활용

**Activity 10 (5분): 전체 공유 및 정리**
- 가장 효과적이었던 bulletproofing 전략 공유
- 저널 예제에서 가장 놀랐던 점 공유
- 교수 피드백: 공통 gap 패턴

**총 Workshop 시간: 85분 (Opening Discussion 15분 포함 = 100분)**

---

## 과제 (다음 주까지)

### "My Methods/Results - Bulletproofed"

**제출물:**

1. **Methods 섹션 완성 (800-1000 words)**
   - Reproducibility checklist 전부 충족
   - Control strategy 정당화
   - Statistical power/sample size 근거
   - 6가지 필수 요소 모두 포함

2. **Results 섹션 완성 (600-800 words)**
   - 모든 주요 결과 (effect size + CI + p)
   - Figure/Table 최소 1개
   - Overclaiming 없는 conservative claims
   - Transparent reporting

3. **Bulletproofing Documentation (800 words)**
   - **AI를 활용한 self-critique 결과**
     - Reproducibility audit (10 vulnerable points)
     - Alternative explanation check
     - Statistical review
   - **예상 리뷰어 질문 5개 + 방어 전략**
     - Critical questions (어떻게 Methods/Results에 답변?)
     - Major questions (Supplementary plan)
   - **Transparency checklist 충족 증빙**
     - 모든 planned comparison 보고 확인
     - Exploratory vs confirmatory 구분

4. **AI 활용 과정 (500 words)**
   - 사용한 프롬프트 레시피 **5개 이상**
   - 각 레시피의 효과 및 한계
   - AI의 한계 및 인간 판단이 필요했던 지점

5. **Peer Review 반영 (300 words)**
   - 받은 피드백 요약 (6가지 평가 항목별)
   - 각 피드백을 어떻게 반영했는지

### 평가 기준

- **Reproducibility & Rigor (40%)**
  - 재현성 (6가지 요소 충족)
  - Control (alternative explanation 배제)
  - 통계 정당화 (power analysis, appropriate tests)

- **Transparent Reporting (25%)**
  - 완전한 결과 보고 (모든 planned comparison)
  - Overclaiming 방지 (claim-evidence match)
  - Open science practices

- **Reviewer-Ready (20%)**
  - 예상 질문 대응 (preemptive defense)
  - Methods/Results 일관성
  - Effect size + practical significance

- **AI 활용 & Peer Review (15%)**
  - 효과적 프롬프트 (5개 이상)
  - 비판적 검토 및 개선
  - 동료 피드백 반영

---

## 핵심 메시지

### Bulletproof Methods/Results의 조건
```
Reproducibility (6가지 요소)
     +
Control (alternative explanation 배제)
     +
Statistical Rigor (power, assumptions, effect size)
     +
Transparent Reporting (모든 결과, no overclaiming)
     +
Preemptive Defense (예상 질문에 미리 답변)
     =
Nature/Science 리뷰어가 공격할 틈 없는 Methods/Results
```

### CoT의 역할
> "윤경생 강의에서 CoT **기법**을 배웠다면,
> 본 강의에서는 CoT를 '리뷰어 공격 방어'라는 **목표**에 전략적으로 활용."

---

## 토론 주제

1. **Reproducibility**: 자신의 Methods에서 가장 취약한 부분은? 어떻게 보강할 것인가?

2. **Overclaiming**: Results에서 데이터를 넘어서는 주장을 하고 있지 않은가?

3. **Statistical rigor**: Multiple comparison을 고려하면 결과가 여전히 유의한가?

4. **Reviewer questions**: 리뷰어가 가장 공격할 가능성이 높은 부분은?

---

## 다음 주 준비사항

- **Discussion 섹션 초안 작성**
  - 결과의 broader implications
  - 한계점 및 future directions
  - Conclusion

- **전체 논문 통합**
  - Abstract → Introduction → Methods → Results → Discussion
  - 일관성 체크
  - 최종 검토

---

## 참고 자료

### 추천 읽기
- Nature/Science Methods 섹션 10편
  - 어떻게 reproducibility를 달성하는지
  - Control strategy 패턴 파악

- APA Publication Manual (7th ed.)
  - Statistical reporting guidelines
  - Effect size reporting standards

### 프롬프트 레시피 라이브러리
- 공유 게시판에서 동료들의 효과적 bulletproofing 프롬프트 참고
- Reproducibility audit, statistical review 프롬프트 적극 공유

### AI 도구 추천
- **ChatGPT**: Reproducibility audit, alternative explanation generation
- **Claude**: Statistical review, reviewer question prediction
- **Perplexity**: 통계 방법 best practices 검색
- **G*Power**: Power analysis (AI가 아닌 전용 소프트웨어)

---

## 📚 Top-Tier Journal 실제 사례 및 Best Practices

> **Note**: 이 섹션은 Nature, Science, Nature Human Behaviour, PNAS 등 top-tier 저널의 실제 가이드라인과 모범 사례를 정리한 것입니다.

### 7.1 Nature Human Behaviour의 재현성 이니셔티브 (2024)

**Institute for Replication (I4R) 협력**

Nature Human Behaviour는 2024년부터 Institute for Replication (I4R)과 협력하여 재현성 검증을 강화했습니다.

**핵심 요구사항:**

| 요소 | Nature Human Behaviour 기준 | 일반 저널 기준 |
|------|----------------------------|---------------|
| Sample size justification | A priori power analysis 필수 | 권장 |
| Pre-registration | 권장 (Registered Reports 트랙 별도) | 선택 |
| Data availability | 공개 또는 통제 접근 필수 | 선택 |
| Code availability | 분석 코드 공개 필수 | 권장 |
| Effect size reporting | Cohen's d, η², r 등 필수 | 권장 |

**실제 저널 가이드라인에서 발췌:**

> "Authors must report effect sizes and confidence intervals for all statistical tests. P-values alone are insufficient for evaluating the practical significance of findings."
> — Nature Human Behaviour Author Guidelines (2024)

---

### 7.2 Effect Size 보고 기준: 종합 가이드

**Cohen's d (독립표본 비교)**

| 크기 | 값 | 해석 | 실제 예시 |
|------|-----|------|----------|
| Small | d = 0.2 | 육안으로 구분 어려움 | 약한 개입 효과 |
| Medium | d = 0.5 | 육안으로 구분 가능 | 전형적 심리치료 효과 |
| Large | d = 0.8 | 명확히 구분 가능 | 강력한 실험 조작 |

**Nature/Science급 보고 예시:**

```
❌ 부적절한 보고:
"The experimental group showed significantly higher scores than the control group (p < .05)."

✅ Nature-level 보고:
"The experimental group (M = 85.3, SD = 12.1, n = 48) demonstrated
significantly higher scores than the control group (M = 72.4, SD = 10.8, n = 52),
t(98) = 5.43, p < .001, Cohen's d = 1.12, 95% CI [0.71, 1.53],
representing a large effect size."
```

**Partial Eta-Squared (η²p) - ANOVA용**

| 크기 | 값 | 해석 |
|------|-----|------|
| Small | η²p = 0.01 | 분산의 1% 설명 |
| Medium | η²p = 0.06 | 분산의 6% 설명 |
| Large | η²p = 0.14 | 분산의 14% 이상 설명 |

**ANOVA 완전 보고 예시:**

```
"A 2 (Condition: experimental vs. control) × 3 (Time: pre, post, follow-up)
mixed ANOVA revealed a significant interaction effect, F(2, 196) = 8.42,
p < .001, η²p = .079, 90% CI [.03, .13]. Simple effects analyses
with Bonferroni correction (α = .017) showed..."
```

---

### 7.3 Power Analysis 현황: 심리학 연구의 변화 (2015-2021)

**체계적 리뷰 결과** (903편 논문 분석, PNAS 2025)

| 연도 | Power analysis 보고율 | 평균 목표 power |
|------|---------------------|----------------|
| 2015 | 9.5% | 0.80 |
| 2018 | 18.2% | 0.80 |
| 2021 | 30.0% | 0.80-0.95 |

**주요 발견:**
- Top-tier 저널일수록 power analysis 요구가 엄격
- 2015년 이후 보고율 3배 이상 증가
- 그러나 여전히 70%가 power analysis 미보고

**Best Practice: Power Analysis 보고 템플릿**

```markdown
**Sample Size Determination**

An a priori power analysis was conducted using G*Power 3.1
(Faul et al., 2009) based on the following parameters:

- Test: Independent samples t-test (two-tailed)
- Expected effect size: Cohen's d = 0.50
  (based on meta-analysis by Smith et al., 2020, k = 15 studies)
- Alpha: α = 0.05
- Power: 1 - β = 0.80

Required sample size: N = 128 (64 per group)

We recruited N = 140 to allow for ~10% attrition,
yielding a final sample of N = 132 after exclusions.

Sensitivity analysis: With our final sample (N = 132),
we had 80% power to detect effects of d ≥ 0.49.
```

---

### 7.4 Multiple Comparison 보정: APA JARS 기준

**Journal Article Reporting Standards (JARS) - 통계 보고 요구사항**

| 상황 | 권장 보정 방법 | 예시 |
|------|--------------|------|
| 2-3 비교 | Bonferroni | α/k (α = .05/3 = .017) |
| 4-10 비교 | Holm-Bonferroni | 순차적 보정 |
| >10 비교 | False Discovery Rate (FDR) | Benjamini-Hochberg |
| 탐색적 분석 | FDR 또는 별도 섹션 | "Exploratory analyses" 명시 |

**실제 보고 예시:**

```
❌ 문제적 보고:
"We conducted 12 comparisons and found that 3 were significant
at p < .05."

✅ 적절한 보고:
"We conducted 12 planned comparisons. To control the family-wise
error rate, we applied the Benjamini-Hochberg procedure to control
the false discovery rate at q = .05. Three comparisons survived
correction (adjusted p-values: .008, .012, .041). The remaining
9 comparisons were not significant after correction (all adjusted
ps > .10; see Supplementary Table S2 for complete results)."
```

---

### 7.5 TOP Guidelines: 투명성 수준별 기준

**Transparency and Openness Promotion (TOP) Guidelines**

Level 0-3으로 투명성 수준을 평가:

| Level | Data Citation | Materials | Code | Pre-registration |
|-------|--------------|-----------|------|------------------|
| 0 | 언급 없음 | 언급 없음 | 언급 없음 | 언급 없음 |
| 1 | 저널 권장 | 저널 권장 | 저널 권장 | 저널 권장 |
| 2 | 필수 요구 | 필수 요구 | 필수 요구 | 필수 요구 |
| 3 | 검증 절차 | 검증 절차 | 검증 절차 | 검증 절차 |

**Nature Human Behaviour: Level 2-3 수준 요구**

**Data Availability Statement 예시:**

```
❌ 부적절:
"Data are available upon reasonable request."

✅ Nature-level:
"The anonymized data and analysis scripts that support the findings
of this study are available at [OSF link]
(https://osf.io/xxxxx). Materials are available at [GitHub link].
Due to IRB restrictions, raw audio recordings cannot be shared,
but processed transcripts are provided."
```

---

### 7.6 Nature/Science 수준 Methods 섹션 구조

**실제 Nature Human Behaviour 논문 구조 분석:**

```markdown
## Methods

### Participants
Participants (N = 245; 142 female, 98 male, 5 non-binary;
M_age = 23.4 years, SD = 4.2, range: 18-40) were recruited
via [platform]. Exclusion criteria included: (a) history of
neurological disorders, (b) non-native English proficiency,
(c) participation in related studies within 6 months.

Sample size was determined by a priori power analysis
(see Supplementary Methods).

### Materials
#### Experimental stimuli
Stimuli consisted of 120 images selected from the IAPS
(Lang et al., 2008) based on normative arousal ratings
(M = 5.2, SD = 1.1 on 9-point scale) and valence ratings
(negative: M = 2.3; neutral: M = 5.0; positive: M = 7.1).

#### Self-report measures
Emotional intensity was assessed using a 7-point Likert scale
(1 = "not at all intense" to 7 = "extremely intense"),
adapted from [citation]. Internal consistency was high
(Cronbach's α = .89).

### Procedure
[Timeline figure reference]
Participants completed the study in a single 45-minute session.
After providing informed consent (approved by [IRB], #12345),
participants were randomly assigned to experimental (n = 123)
or control (n = 122) conditions using block randomization
(block size = 4).

The procedure consisted of:
1. Baseline assessment (5 min): [description]
2. Manipulation phase (20 min): [detailed description]
3. Test phase (15 min): [detailed description]
4. Debriefing (5 min): [description]

### Data analysis
All analyses were conducted in R (v4.2.0) using the lme4 package
(v1.1-30) for mixed-effects models. Analysis scripts are available
at [link].

Pre-registered hypotheses and analysis plan: [OSF link]
```

---

### 7.7 Nature/Science 수준 Results 섹션 구조

**실제 논문 패턴 분석:**

```markdown
## Results

### Manipulation check
The manipulation was successful: participants in the experimental
condition reported significantly higher [measure] (M = 5.8, SD = 1.2)
than those in the control condition (M = 3.2, SD = 1.4),
t(243) = 15.42, p < .001, d = 1.97, 95% CI [1.68, 2.26].

### Primary analyses
#### Hypothesis 1: [Statement]
Consistent with our hypothesis, [DV] was significantly higher
in the experimental condition (M = 72.3, SD = 14.2) than in the
control condition (M = 64.1, SD = 13.8), t(243) = 4.68, p < .001,
d = 0.60, 95% CI [0.34, 0.85] (Fig. 2a).

#### Hypothesis 2: [Statement]
[Similar detailed reporting]

### Secondary analyses
[Pre-registered secondary analyses with same detail level]

### Exploratory analyses
Note: The following analyses were not pre-registered and should
be interpreted as exploratory.

We examined whether [variable] moderated the effect of condition
on [DV]. A significant interaction emerged, B = 0.34, SE = 0.12,
t(241) = 2.83, p = .005 (Fig. 3). However, this finding requires
replication.

### Robustness checks
Results were robust to: (a) exclusion of outliers (>3 SD; n = 4),
(b) alternative operationalization of [DV], and (c) non-parametric
tests (Mann-Whitney U = 5842, p < .001). See Supplementary Tables
S3-S5 for complete results.
```

---

### 7.8 흔한 실수와 수정 예시

**Example 1: Insufficient Reproducibility**

```
❌ Before (거부 위험):
"Participants viewed emotional images and rated their feelings."

✅ After (Nature-level):
"Participants viewed 60 images (20 negative, 20 neutral, 20 positive)
from the validated OASIS database (Kurdi et al., 2017), presented
for 2000 ms each with a 500 ms inter-trial interval. After each
image, participants rated their emotional intensity on a 7-point
scale (1 = 'not at all' to 7 = 'extremely') with a 4000 ms response
window. Image order was randomized within valence-blocked
presentation, counterbalanced across participants."
```

**Example 2: Missing Control Strategy**

```
❌ Before (거부 위험):
"We compared the treatment group to the control group."

✅ After (Nature-level):
"To isolate the effect of [active ingredient], we employed a
2 × 2 design: (1) full treatment vs. (2) treatment minus active
ingredient (process control), (3) active ingredient only vs.
(4) no treatment (baseline). This design allows us to distinguish
the specific effect of [ingredient] from demand characteristics
and general engagement effects (see Supplementary Fig. S1 for
design schematic)."
```

**Example 3: Overclaiming**

```
❌ Before (거부 위험):
"Our intervention caused improvements in emotional regulation."

✅ After (Nature-level):
"Participants who received the intervention showed significantly
better performance on the emotional regulation task compared to
controls, consistent with—though not definitively demonstrating—
a causal effect of the intervention. The within-session design
limits causal inference; a randomized controlled trial with
follow-up assessment would provide stronger evidence."
```

**Example 4: Incomplete Statistical Reporting**

```
❌ Before (거부 위험):
"There was a significant difference between groups (p < .05)."

✅ After (Nature-level):
"The experimental group (M = 78.4, SD = 11.2, n = 64) significantly
outperformed the control group (M = 71.2, SD = 12.8, n = 68),
t(130) = 3.45, p < .001, d = 0.60, 95% CI [0.25, 0.94]. This
effect remained significant after controlling for baseline
performance, F(1, 128) = 11.23, p < .001, η²p = .081."
```

---

### 7.9 AI 프롬프트 레시피: Top Journal 수준 진단

**Recipe #41: Nature-Level Reproducibility Audit**

```
다음 Methods 섹션을 Nature Human Behaviour 수준으로 평가해줘:

[Methods 전문]

Nature Human Behaviour의 기준:
1. 모든 실험 파라미터가 수치로 명시되어 있는가?
2. Sample size가 a priori power analysis로 정당화되었는가?
3. 자극/도구의 출처와 타당도가 명시되어 있는가?
4. Randomization/counterbalancing 방법이 명확한가?
5. Data/code availability가 명시되어 있는가?
6. Pre-registration 정보가 있는가?

각 기준에 대해:
- 현재 상태 평가 (0-5점)
- 누락된 정보
- 추가해야 할 문장 (Before → After 예시)
```

**Recipe #42: Effect Size Completeness Check**

```
다음 Results 섹션의 통계 보고를 검토해줘:

[Results 전문]

각 통계 검정에 대해 확인:
1. Effect size 보고됨? (Cohen's d, η², r, OR 등)
2. 95% CI 포함됨?
3. Exact p-value 또는 적절한 inequality?
4. N/df 보고됨?
5. 기술 통계 (M, SD) 포함됨?

누락된 항목이 있다면:
- 어떤 통계량이 빠졌는가?
- 완전한 보고로 수정한 문장 제시
```

**Recipe #43: TOP Guidelines Compliance Check**

```
다음 논문 초안을 TOP Guidelines 수준으로 평가해줘:

[논문 전체 또는 Methods + References]

각 영역 평가 (Level 0-3):
1. Data Citation: 데이터 출처 명시 수준
2. Data Transparency: 데이터 공개 계획
3. Materials Transparency: 자료/도구 공개
4. Code Transparency: 분석 코드 공개
5. Pre-registration: 사전등록 여부
6. Replication: 재현 가능성

현재 수준과 개선 방안:
- 현재 Level: X
- 목표 Level (Nature Human Behaviour 기준): 2-3
- 업그레이드를 위해 추가할 문장/정보
```

---

### 7.10 주요 저널별 Methods/Results 가이드라인 링크

| 저널 | 가이드라인 URL | 특이 요구사항 |
|------|---------------|--------------|
| Nature | nature.com/nature/for-authors | Reporting Summary 필수 |
| Science | science.org/content/page/instructions-authors | Structured Abstract |
| Nature Human Behaviour | nature.com/nathumbehav/submission | I4R 재현성 검토 가능 |
| PNAS | pnas.org/authors/submitting-your-manuscript | SI Appendix 권장 |
| Psychological Science | psychologicalscience.org/publications | Badge system (Open Data/Materials/Pre-reg) |

---

## 📋 Quick Reference: Bulletproofing Checklist

**Methods Section (6 Elements):**
- [ ] Participants: N, demographics, recruitment, inclusion/exclusion
- [ ] Materials: Sources, versions, reliability/validity
- [ ] Procedure: Timeline, timing, verbatim instructions
- [ ] Parameters: Exact values, units, randomization
- [ ] Software/Equipment: Names, versions, settings
- [ ] Data Processing: Preprocessing, exclusion criteria, transformations

**Results Section (5 Checks):**
- [ ] Complete stats: Test, df, p, effect size, 95% CI
- [ ] All comparisons: Including non-significant results
- [ ] Exploratory vs Confirmatory: Clearly labeled
- [ ] Manipulation checks: Reported before main analyses
- [ ] Robustness: Alternative analyses in Supplementary

**Transparency (TOP Level 2+):**
- [ ] Data availability statement with repository link
- [ ] Code availability statement with repository link
- [ ] Materials availability or explanation
- [ ] Pre-registration link (if applicable)
- [ ] Ethics approval number

---

## 8. 학생 예시 리뷰 세션: 저널 vs 내 Methods/Results 비교

> **목적**: Section 7의 top-tier 저널 사례를 기준으로 삼아, 자신과 동료의 Methods/Results를 비교 분석하고 개선점을 도출합니다.

### 8.1 세션 구조 (20분)

**Step 1: Quick Journal Benchmark (5분)**
- Section 7.6-7.7의 Nature/Science Methods/Results 구조 템플릿 훑어보기
- 핵심 체크포인트 3가지 머릿속에 새기기:
  1. Reproducibility: 파라미터가 수치로 명시되어 있는가?
  2. Effect Size: 모든 통계량이 완전히 보고되었는가?
  3. Transparency: Exploratory vs Confirmatory가 구분되었는가?

**Step 2: 동료 예시 교환 & 비교 분석 (10분)**
- 2-3명이 한 그룹을 형성
- 각자 자신의 Methods OR Results 중 1개 섹션 선택
- Section 7.8의 Before/After 예시를 참조하며 동료 글 분석

**Step 3: 그룹 토론 & 개선점 도출 (5분)**
- 저널 사례와 비교했을 때 가장 큰 gap은?
- 즉시 개선 가능한 부분 vs 추가 데이터/분석 필요한 부분 구분

---

### 8.2 학생 예시 비교 분석 템플릿

**저널 vs 내 Methods/Results 비교표:**

```markdown
## Methods/Results 비교 분석표

### 분석 대상
- **내 섹션**: ☐ Methods / ☐ Results
- **동료**: _____________

---

### A. Reproducibility Check (Nature 기준 vs 내 글)

| 요소 | Nature 예시에서 | 내 글에서 | Gap | 즉시 수정 가능? |
|------|----------------|----------|-----|----------------|
| Participants N + demographics | "N = 245; 142 female, 98 male..." | | | ☐ Yes / ☐ No |
| 자극/도구 파라미터 | "presented for 2000 ms each with 500 ms ITI" | | | ☐ Yes / ☐ No |
| Power analysis | "G*Power 3.1, d = 0.50, power = 0.80" | | | ☐ Yes / ☐ No |
| Software versions | "R (v4.2.0), lme4 (v1.1-30)" | | | ☐ Yes / ☐ No |

---

### B. Statistical Reporting Check (완전성)

| 통계량 | Nature 형식 | 내 보고 형식 | 누락 항목 |
|--------|------------|-------------|----------|
| 기술 통계 | "M = 85.3, SD = 12.1, n = 48" | | |
| 검정 통계량 | "t(98) = 5.43, p < .001" | | |
| Effect size | "Cohen's d = 1.12" | | |
| 신뢰구간 | "95% CI [0.71, 1.53]" | | |

---

### C. Transparency Check

| 항목 | Nature 기준 | 내 글 상태 |
|------|------------|-----------|
| Confirmatory vs Exploratory 구분 | 명확히 라벨링 | ☐ 구분됨 / ☐ 혼재 / ☐ N/A |
| Manipulation check 보고 | 주 분석 전에 제시 | ☐ 있음 / ☐ 없음 / ☐ N/A |
| Non-significant results | 모두 보고 | ☐ 완전 / ☐ 일부 누락 |
| Robustness checks | Supplementary에 포함 | ☐ 있음 / ☐ 계획 중 / ☐ 없음 |

---

### D. 종합 진단

**내 글과 Nature 수준의 Gap 점수 (0-10):**
- Reproducibility: ___/10
- Statistical completeness: ___/10
- Transparency: ___/10
- **Overall Gap**: ___/10

**가장 시급한 개선 3가지:**
1.
2.
3.

**동료로부터 받은 추가 제안:**
-
```

---

### 8.3 그룹 토론 가이드 질문

**저널 예제와 비교하며 답변:**

1. **가장 놀라운 차이점**
   - "Nature 논문은 _____ 수준까지 상세히 기술하는데, 내 글은 _____만 언급했다"
   - 예: "ITI를 밀리초 단위로 명시" vs "자극 사이에 잠시 쉼"

2. **즉시 추가할 수 있는 정보**
   - 내가 **알고 있지만 쓰지 않은** 정보는?
   - 예: 사용한 R 패키지 버전, 정확한 시간 파라미터

3. **추가 작업이 필요한 정보**
   - 내가 **아직 없어서 생성해야 하는** 정보는?
   - 예: Power analysis (아직 안 돌림), Effect size 계산

4. **동료의 글에서 배운 점**
   - 동료가 더 잘 기술한 부분은?
   - 내 글에 적용할 아이디어는?

---

### 8.4 AI 프롬프트: 저널 수준 Gap 분석

**Recipe #44: Journal-Level Gap Analyzer**

```
다음 두 텍스트를 비교해줘:

[Reference: Nature Human Behaviour 수준 Methods 예시]
(Section 7.6의 예시 사용)

[내 Methods]:
(내 Methods 전문)

비교 분석:
1. **Reproducibility Gap**
   - 내 글에서 누락된 수치/파라미터 5가지
   - 각각을 Nature 수준으로 보강하는 문장

2. **Structure Gap**
   - Nature 구조와 내 구조의 차이점
   - 재배열 제안

3. **Detail Level Gap**
   - Nature가 명시하지만 내가 생략한 정보 유형
   - 예: "Nature는 IRB 번호까지 명시하지만 나는 '승인 받음'만 기재"

4. **Priority Ranking**
   - 가장 시급히 수정해야 할 gap (Critical/Major/Minor)
   - 각 gap의 Before → After 예시

출력 형식: 비교표 + 수정 문장 제안
```

**Recipe #45: Peer Comparison Facilitator**

```
다음 두 학생의 Methods 섹션을 비교해줘:

[학생 A - 나]:
(내 Methods)

[학생 B - 동료]:
(동료 Methods)

비교 분석:
1. **각각의 강점** (서로 배울 점)
   - 학생 A가 더 잘한 부분:
   - 학생 B가 더 잘한 부분:

2. **공통 약점** (둘 다 개선 필요)
   - Nature 기준 대비 둘 다 부족한 영역:

3. **Best of Both** 통합 버전
   - 두 글의 강점을 합친 이상적 Methods outline

4. **상호 제안**
   - A가 B에게 제안할 개선점:
   - B가 A에게 제안할 개선점:
```

---

### 8.5 실습 후 전체 공유 (선택, 5분)

**클래스 전체 토론 (시간 여유 시):**

- **가장 큰 깨달음**: "저널 예제를 보고 가장 놀란 점은?"
- **Best Practice 공유**: "동료 글에서 발견한 좋은 표현/구조는?"
- **공통 Gap 발견**: "우리 반 전체적으로 부족한 영역은?"

**교수 정리:**
- 가장 흔히 발견되는 gap 패턴 피드백
- 다음 주 과제에서 특히 주의할 점
- 추가 참고 자료 안내

---

### 8.6 세션 Takeaways

**이 세션 후 학생들이 얻어가야 할 것:**

1. **구체적 Gap 인식**: "내 Methods/Results가 Nature 수준과 어디서 차이 나는지 정확히 안다"

2. **즉시 실행 리스트**: "수업 끝나고 바로 수정할 3가지가 있다"

3. **동료 학습**: "다른 학생의 글에서 좋은 표현을 배웠다"

4. **현실적 목표 설정**: "완벽하지 않아도, 어느 수준까지는 도달할 수 있다"

**핵심 메시지:**

> "Top-tier 저널 논문은 특별한 재능이 아니라, **세부 사항에 대한 집착과 투명한 보고**에서 나옵니다.
> 오늘 저널 예제와 동료 예시를 비교하며, 그 gap을 인식하는 것이 첫 번째 단계입니다."
