# Template 4.5: Recipe Library (Week 4 Cumulative)

**Week 4 - Methods/Results Bulletproofing**
**Activity**: Curate and share best AI prompt recipes for reviewer attack defense
**Format**: Standalone reference + Embedded in Templates 4.1-4.4

---

## Purpose

**Week 4 Recipe Library** compiles all AI prompt recipes for bulletproofing Methods/Results sections. This enables:
- Quick reference during writing and revision
- Defense against Top 10 rejection reasons
- Systematic self-critique before submission
- Peer learning through recipe sharing
- Cumulative building (Week 2 → 3 → 4 → 5 → 6)

---

## Recipe Overview

### Core Recipes (#35-40)

| # | Recipe Name | Target | Category |
|---|------------|--------|----------|
| 35 | Reproducibility Vulnerability Scanner | Methods | Reproducibility |
| 36 | Control Strategy Auditor | Methods | Controls |
| 37 | Statistical Assumption Checker | Methods/Results | Statistics |
| 38 | Overclaiming Detector | Results | Claims |
| 39 | Statistical Rigor Validator | Results | Statistics |
| 40 | Preemptive Reviewer Response | Both | Defense |

### Bonus Recipes (B1-B4)

| # | Recipe Name | Target | Category |
|---|------------|--------|----------|
| B1 | Nature Reviewer Simulator | Methods | Evaluation |
| B2 | Transparency Checker | Results | Reporting |
| B3 | Methods-Results Consistency Checker | Both | Consistency |
| B4 | Practical Significance Evaluator | Results | Effect Size |

---

## Core Recipes (Detailed)

### Recipe #35: Reproducibility Vulnerability Scanner

**Purpose**: Find 10 points where other researchers would get stuck trying to reproduce your study

**Category**: Methods - Reproducibility (Rejection Reason #1)

**Prompt**:
```
다음 Methods 섹션을 읽고, 다른 연구자가 재현하려 할 때
막힐 수 있는 지점 10가지를 찾아줘:

[여기에 Methods 전문 붙여넣기]

각 지점에 대해:
1. 무엇이 불명확한가?
2. 어떤 정보가 추가로 필요한가?
3. 구체적으로 어떻게 기술해야 하는가?
   (Before → After 예시 포함)
```

**Example Output**:
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

**Why It Works**:
- Forces systematic review of all 6 reproducibility elements
- Generates concrete Before → After improvements
- Prevents "다른 연구자가 이 연구를 재현할 수 없다" rejection

**Related Recipes**: Use before #36 (Control Strategy), after #40 (Preemptive Response)

---

### Recipe #36: Control Strategy Auditor

**Purpose**: Identify missing controls and alternative explanations that reviewers will attack

**Category**: Methods - Controls (Rejection Reason #2)

**Prompt**:
```
내 연구 디자인:
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
- 추가해야 할 control은?
```

**Why It Works**:
- Proactively generates reviewer attacks before submission
- Covers 4 control types: positive, negative, confound, validation
- Prevents "대안 설명을 배제하지 못했다" rejection

**Related Recipes**: Use after #35 (Reproducibility), with #37 (Statistical Assumption)

---

### Recipe #37: Statistical Assumption Checker

**Purpose**: Verify sample size justification and statistical power

**Category**: Methods/Results - Statistics (Rejection Reason #3-4)

**Prompt**:
```
내 연구 계획:
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
- 각 질문에 대한 방어 전략
```

**Why It Works**:
- Validates power analysis before reviewers attack
- Generates preemptive defense for sample size questions
- Prevents "통계적 검정력이 부족하다" rejection

**Related Recipes**: Use with #39 (Statistical Rigor), before #40 (Preemptive Response)

---

### Recipe #38: Overclaiming Detector

**Purpose**: Identify claims that exceed what the data supports

**Category**: Results - Claims (Rejection Reason #6)

**Prompt**:
```
다음 Results 문장들을 분석해줘:
[Results text with claims]

각 문장에 대해:
1. Claim type (causal/correlational/mechanistic/general)
2. Evidence level (direct/indirect/suggestive)
3. Overclaiming risk (1-10)
4. Conservative alternative phrasing

그리고:
- 가장 위험한 overclaim 3개 지적
- 각각을 데이터에 맞게 수정하는 방법
```

**Example Detection**:
| Original | Risk | Conservative Alternative |
|----------|------|--------------------------|
| "X **causes** Y" | 9/10 | "X is **associated with** Y" |
| "This **proves** theory" | 10/10 | "These findings are **consistent with** theory" |
| "Our method **works in general**" | 8/10 | "Our method works **in [condition]**" |

**Why It Works**:
- Systematically checks claim-evidence match
- Provides conservative alternative phrasing
- Prevents "데이터가 뒷받침하지 않는 주장" rejection

**Related Recipes**: Use with #39 (Statistical Rigor), after analyzing results

---

### Recipe #39: Statistical Rigor Validator

**Purpose**: Check completeness of statistical reporting and identify vulnerabilities

**Category**: Results - Statistics (Rejection Reason #8)

**Prompt**:
```
내 Results 섹션:
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
- 추가할 분석/보고 내용
```

**Required Reporting Format**:
```
"Group A (M = 85.3, SD = 12.1) significantly outperformed
Group B (M = 72.4, SD = 10.8), t(98) = 5.43, p < .001,
Cohen's d = 1.12, 95% CI [0.71, 1.53]"
```

**Checklist for Complete Reporting**:
- [ ] Descriptive stats (M, SD)
- [ ] Inferential stats (t, F, χ², df, p)
- [ ] Effect size (Cohen's d, η², r)
- [ ] Confidence interval (95% CI)
- [ ] Multiple comparison correction (if applicable)

**Why It Works**:
- Covers all statistical rigor checkpoints
- Generates specific defense strategies
- Prevents "다중 비교 보정 누락" and "p-hacking 의심" rejections

**Related Recipes**: Use with #37 (Assumption Checker), #38 (Overclaiming)

---

### Recipe #40: Preemptive Reviewer Response Generator

**Purpose**: Anticipate and prepare defenses for likely reviewer questions

**Category**: Both Methods & Results - Defense

**Prompt**:
```
내 Methods/Results:
[전체 텍스트]

Nature/Science 리뷰어가 제기할 가능성이 높은 질문 10가지를 생성해줘.
각 질문에 대해:
1. 질문 유형 (reproducibility/controls/statistics/interpretation)
2. 심각도 (critical/major/minor)
3. 현재 Methods/Results에서 답변이 있는가?
4. 없다면, Methods/Results에 추가할 내용
5. Rebuttal letter에서 답변할 내용

우선순위 순으로 정렬해줘.
```

**Response Strategy Matrix**:
| Severity | Where to Address |
|----------|------------------|
| Critical | Add to Methods/Results directly |
| Major | Add to Supplementary Materials |
| Minor | Prepare rebuttal response only |

**Why It Works**:
- Simulates reviewer perspective before submission
- Prioritizes which gaps to fill in manuscript vs supplementary
- Creates defense playbook for rebuttal

**Related Recipes**: Use as final step after #35-39

---

## Bonus Recipes

### Recipe B1: Nature Reviewer Simulator

**Purpose**: Get holistic Methods evaluation from Nature reviewer perspective

**Prompt**:
```
다음 Methods 섹션을 Nature 리뷰어 관점에서 평가해줘:
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
- 개선 방안
```

---

### Recipe B2: Transparency Checker

**Purpose**: Ensure all planned analyses are reported (prevent cherry-picking)

**Prompt**:
```
내 연구 계획:
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
- 투명성 강화를 위한 문구 제안
```

---

### Recipe B3: Methods-Results Consistency Checker

**Purpose**: Find mismatches between Methods promises and Results delivery

**Prompt**:
```
내 Methods 섹션:
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
- 수정 방법 (Methods 추가 vs Results 추가 vs 삭제)
```

---

### Recipe B4: Practical Significance Evaluator

**Purpose**: Assess whether statistically significant results have real-world meaning

**Prompt**:
```
내 주요 발견:
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
지적할 위험이 있는가?
```

---

## Recipe Card Template (for Student Contributions)

```markdown
┌─────────────────────────────────────────────────────────────┐
│ Recipe #___ by 학생___                                      │
│ "[Recipe Name]"                                              │
│ ⭐⭐⭐⭐⭐ (5.0/5.0 based on N votes)                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│ 📋 Target: ☐ Methods / ☐ Results / ☐ Both                  │
│                                                              │
│ 🎯 Use Case:                                                 │
│ [어떤 상황에서 이 프롬프트를 사용하는가?]                    │
│                                                              │
│ 🤖 Prompt:                                                   │
│ ```                                                          │
│ [실제 프롬프트 텍스트 전체]                                  │
│ [복사-붙여넣기 가능하도록 raw text]                          │
│ ```                                                          │
│                                                              │
│ 💡 Why It Works:                                             │
│ [왜 이 프롬프트가 효과적인가? 어떤 원리/전략?]               │
│                                                              │
│ 📊 Results Example:                                          │
│ • Input: [brief description]                                 │
│ • Output: [key insights AI provided]                         │
│ • Outcome: [what improved - e.g., "Prevented 3 overclaims"] │
│                                                              │
│ 🛡️ Defends Against:                                         │
│ • Rejection Reason #___: [reason name]                       │
│                                                              │
│ 🔗 Related Recipes:                                          │
│ • Works well with Recipe #___                                │
│ • Use before/after Recipe #___                               │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Recipe Usage Workflow

### Recommended Sequence

```
Stage 1: Methods Audit
├── Recipe #35 (Reproducibility Scanner)
├── Recipe #36 (Control Strategy Auditor)
└── Recipe #37 (Statistical Assumption Checker)

Stage 2: Results Audit
├── Recipe #38 (Overclaiming Detector)
├── Recipe #39 (Statistical Rigor Validator)
└── Recipe B2 (Transparency Checker)

Stage 3: Cross-Validation
├── Recipe B3 (Consistency Checker)
└── Recipe B4 (Practical Significance)

Stage 4: Defense Preparation
└── Recipe #40 (Preemptive Reviewer Response)
```

### Quick Reference (Copy-Paste Ready)

**Recipe #35: Reproducibility Scanner**
```
다음 Methods에서 재현 막힘 지점 10개 찾아줘: [Methods]
```

**Recipe #36: Control Strategy Auditor**
```
다음 연구 설계에서 빠진 통제 변수와 대안 설명 찾아줘: [Methods]
```

**Recipe #37: Statistical Assumption Checker**
```
다음 통계 분석의 가정 위배 가능성 검토해줘: [Analysis description]
```

**Recipe #38: Overclaiming Detector**
```
다음 Results에서 증거를 넘어선 주장 찾아줘: [Results]
```

**Recipe #39: Statistical Rigor Validator**
```
다음 통계 보고가 완전한지 체크해줘 (effect size, CI, power): [Results]
```

**Recipe #40: Preemptive Reviewer Response**
```
다음 Methods/Results에 대해 리뷰어가 제기할 질문 5개와 대응 초안: [Text]
```

---

## Curation Process

### During Class (Instructor-Led)

**Step 1: Identify Candidates (ongoing)**
- Monitor student experiments in real-time
- React with emoji on innovative prompts
- Note variations that improved base recipes

**Step 2: Nominate (last 5 min)**
- Instructor highlights 2-3 best recipes
- Brief explanation: "Why is this excellent?"
- Student who created it explains their thinking

**Step 3: Vote (if time allows)**
- Class votes: ⭐ rating (1-5)
- Quick show of hands or digital reactions
- Top-voted recipes added to library

**Step 4: Document (after class)**
- Instructor fills recipe card
- Adds to library section
- Links to student name for credit

---

## Quality Criteria

**Excellent Recipe (5 stars)**:
- ✅ Novel variation (not just copy-paste from lecture)
- ✅ Specific target (addresses specific rejection reason)
- ✅ Demonstrated results (found real vulnerabilities)
- ✅ Transferable (others can apply it)
- ✅ Explains mechanism (why it works)

**Good Recipe (4 stars)**:
- Meets 3-4 of above criteria
- Useful but minor novelty

**Include in Library**:
- All 5-star recipes (featured prominently)
- Selected 4-star recipes (for diversity)

---

## Connection to Top 10 Rejection Reasons

| Rejection Reason | Recipe Defense |
|------------------|----------------|
| #1 Insufficient detail | Recipe #35 |
| #2 Inadequate controls | Recipe #36 |
| #3 Sample size issues | Recipe #37 |
| #4 Inappropriate statistics | Recipe #37, #39 |
| #5 Validation gaps | Recipe #36, B1 |
| #6 Overclaiming | Recipe #38 |
| #7 Cherry-picking | Recipe B2 |
| #8 Statistical issues | Recipe #39 |
| #9 Unclear presentation | Recipe B3 |
| #10 Weak effect sizes | Recipe B4 |

---

## Student Contribution Section

*This section grows each semester with student innovations*

### Student Recipes (학생 기여)

*[To be filled during and after workshops]*

#### Example Entry:
```
Recipe S1 by 김OO (2025 Spring)
"Red Team Attack Generator"
⭐⭐⭐⭐⭐ (4.8/5.0 based on 12 votes)

Target: Both Methods & Results

Prompt:
"당신은 Nature 리뷰어입니다. 이 논문을 reject시키기 위한
가장 날카로운 공격 5가지를 작성하세요:
[Methods/Results]
각 공격에 대해:
- 공격 유형 (methodological/statistical/conceptual)
- 심각도 (fatal flaw/major concern/minor issue)
- 저자가 방어하기 어려운 이유"

Why It Works:
적극적으로 reviewer 관점을 시뮬레이션하여
숨겨진 취약점을 발견함

Defends Against: All rejection reasons (comprehensive scan)

Related: Use with Recipe #40 for complete defense
```

---

## Cumulative Library (Week 2-6)

### From Week 2 (초록 쓰기)
- Recipe #1-10: Opening patterns, significance framing
- [Link to Week 2 Recipe Library]

### From Week 3 (Research Gap)
- Recipe #15-30: Gap discovery, validation workflows
- [Link to Week 3 Recipe Library]

### From Week 4 (Methods/Results) ← Current
- Recipe #35-40: Bulletproofing, reviewer defense
- Recipe B1-B4: Bonus evaluation tools

### Week 5-6 (Coming)
- Discussion section strategies
- Final polish and integration

---

## Export Options

**For Students**:
- PDF download of all recipes
- Copy-paste ready prompts
- Recipe card templates for submissions

**For Instructors**:
- Figma/Notion integration
- Semester-by-semester archives
- Best practices compilation

---

*Last Updated: Week 4 Workshop*
*Total Recipes: 10 Core + Student Contributions*
*Next Update: After Week 4 Class*
