# 4주차 과제: Methods/Results Bulletproofing 및 Self-Audit

## 과제 개요
수업 중 AI 활용 audit과 Red Team/Blue Team 연습을 바탕으로 Methods/Results를 수정하고, Self-Audit Report를 작성합니다.

## 제출 기한
5주차 수업 시작 전

---

## 제출물

### 1. Methods 섹션 수정본 (800-1200 words)

**요구사항:**
- 수업 중 AI Reproducibility Audit 결과 반영
- 6요소 Reproducibility Checklist 충족
- Red Team 공격에 대한 방어 반영

**필수 포함 6가지 요소:**

| 요소 | 필수 포함 내용 | 체크 |
|------|---------------|------|
| 1. Participants | N, 모집방법, 인구통계, inclusion/exclusion, IRB | ☐ |
| 2. Materials | 도구명, 출처, 신뢰도/타당도, 예시 문항 | ☐ |
| 3. Procedure | 시간순서, 각 단계 타이밍, 지시문 | ☐ |
| 4. Parameters | 자극 파라미터, 조건별 차이, 임계값 | ☐ |
| 5. Software/Equipment | 소프트웨어명+버전, 하드웨어 스펙 | ☐ |
| 6. Data Processing | 전처리, 이상치 처리, 결측치 처리 | ☐ |

---

### 2. Results 섹션 수정본 (600-1000 words)

**요구사항:**
- Overclaiming 제거 확인
- 완전한 통계 보고 (effect size + CI 포함)
- Cherry-picking 방지 증거 (모든 분석 결과 포함)

**필수 포함 통계 형식:**
```
[검정명] revealed [유의/비유의], [통계량]([자유도]) = [값], p [값],
95% CI [하한, 상한], [효과크기 지표] = [값].
```

**효과크기 보고 기준:**

| 분석 유형 | 효과크기 지표 | 해석 기준 |
|-----------|-------------|----------|
| t-test | Cohen's d | 0.2/0.5/0.8 (small/medium/large) |
| ANOVA | partial η² | 0.01/0.06/0.14 |
| Correlation | r | 0.1/0.3/0.5 |
| Regression | R² | 보고 + 개별 β |

---

### 3. Self-Audit Report (필수, 500-700 words)

**목적:** AI 활용 과정과 발견 사항 문서화

**양식:**

```markdown
## Self-Audit Report

### 1. AI Reproducibility Audit 결과

**사용한 AI 도구:** [ChatGPT / Claude / 기타]

**발견한 취약점 (최소 5개):**

| # | 취약점 | 카테고리 | 수정 여부 |
|---|--------|---------|----------|
| 1 | | ☐ Methods / ☐ Results | ☐ 완료 / ☐ 미완료 |
| 2 | | ☐ Methods / ☐ Results | ☐ 완료 / ☐ 미완료 |
| 3 | | ☐ Methods / ☐ Results | ☐ 완료 / ☐ 미완료 |
| 4 | | ☐ Methods / ☐ Results | ☐ 완료 / ☐ 미완료 |
| 5 | | ☐ Methods / ☐ Results | ☐ 완료 / ☐ 미완료 |

### 2. 가장 효과적인 AI 프롬프트 (3개)

**프롬프트 1:**
```
[사용한 프롬프트 전문]
```
**결과 요약:**
**유용했던 이유:**

**프롬프트 2:**
```
[사용한 프롬프트 전문]
```
**결과 요약:**
**유용했던 이유:**

**프롬프트 3:**
```
[사용한 프롬프트 전문]
```
**결과 요약:**
**유용했던 이유:**

### 3. Red Team/Blue Team 결과

**받은 주요 공격:**
1.
2.
3.

**방어 조치:**
| 공격 | 방어 전략 | 본문 수정 내용 |
|------|----------|---------------|
| 1 | | |
| 2 | | |
| 3 | | |

### 4. Before/After 비교 (1개 필수)

**수정 전:**
```
[원래 문장/단락]
```

**수정 후:**
```
[개선된 문장/단락]
```

**변경 이유:**

### 5. Reproducibility Checklist 자기 평가

| 요소 | 수정 전 점수 | 수정 후 점수 | 개선 내용 |
|------|------------|------------|----------|
| Participants | /5 | /5 | |
| Materials | /5 | /5 | |
| Procedure | /5 | /5 | |
| Parameters | /5 | /5 | |
| Software | /5 | /5 | |
| Data Processing | /5 | /5 | |
| **총점** | /30 | /30 | |

### 6. 남은 취약점 및 향후 계획

**아직 해결되지 않은 문제:**
1.
2.

**향후 개선 계획:**
-
```

---

### 4. 개선된 초록 최종본 (선택)

Week 2에서 작성한 초록에 Methods/Results 수정 내용을 반영한 버전

---

## 형식 요구사항

### 분량
- Methods: 800-1200 words
- Results: 600-1000 words
- Self-Audit Report: 500-700 words
- **총 2000-3000 words**

### 글꼴 및 서식
- 글꼴: 맑은 고딕 또는 Times New Roman, 12pt
- 줄간격: 2.0 (Double space)
- 여백: 상하좌우 2.5cm

### 파일 구성
```
성명_Week4_Assignment.docx (또는 .pdf)

내용 순서:
1. 표지 (제목, 성명, 날짜)
2. Methods 섹션 (수정본)
3. Results 섹션 (수정본)
4. Self-Audit Report
5. 참고문헌 (해당 시)
6. 표/그림 (해당 시)
```

---

## 체크리스트

### Methods 체크리스트 (Top 5 거부 사유 방지)

**1. Insufficient Detail 방지**
- [ ] 다른 연구자가 이 Methods만 보고 재현할 수 있는가?
- [ ] 6가지 필수 요소가 모두 포함되었는가?
- [ ] 구체적 수치(N, 시간, 파라미터)가 제시되었는가?

**2. Inadequate Controls 방지**
- [ ] 잠재적 confound 변수가 통제되었는가?
- [ ] 통제 조건/집단이 명시되었는가?
- [ ] Manipulation check가 포함되었는가? (해당 시)

**3. Sample Size Issues 방지**
- [ ] 표본 크기 결정 근거가 제시되었는가? (power analysis 등)
- [ ] Multiple comparison 시 보정 계획이 있는가?
- [ ] Attrition/exclusion criteria가 명확한가?

**4. Inappropriate Statistics 방지**
- [ ] 분석 방법이 연구 설계에 적합한가?
- [ ] 통계적 가정 확인 방법이 언급되었는가?
- [ ] 분석 소프트웨어와 버전이 명시되었는가?

**5. Validation Gaps 방지**
- [ ] 측정 도구의 신뢰도가 보고되었는가?
- [ ] 타당도 근거가 제시되었는가?
- [ ] 이전 연구에서의 사용 사례가 인용되었는가?

---

### Results 체크리스트 (Top 5 거부 사유 방지)

**6. Overclaiming 방지**
- [ ] 모든 주장이 데이터로 직접 뒷받침되는가?
- [ ] Correlation을 causation으로 오해하지 않았는가?
- [ ] "필요하다", "충분하다" 등 강한 표현을 피했는가?

**7. Cherry-picking 방지**
- [ ] 모든 분석 결과가 보고되었는가? (유의/비유의 모두)
- [ ] 사전 등록된 분석과 탐색적 분석이 구분되었는가?
- [ ] 제외된 데이터가 있다면 이유가 명시되었는가?

**8. Statistical Issues 방지**
- [ ] 다중 비교 보정이 적용되었는가? (Bonferroni, FDR 등)
- [ ] 모든 통계량이 완전하게 보고되었는가?
- [ ] Outlier 처리가 투명하게 기술되었는가?

**9. Unclear Presentation 방지**
- [ ] 주요 결과가 먼저 제시되었는가?
- [ ] Primary와 secondary outcomes가 구분되었는가?
- [ ] Figure/Table 번호가 본문에서 언급되었는가?

**10. Weak Effect Sizes 방지**
- [ ] 모든 분석에 효과크기가 보고되었는가?
- [ ] 95% 신뢰구간이 포함되었는가?
- [ ] 실질적 의미(practical significance)가 언급되었는가?

---

## AI 활용 가이드

### ✅ 허용되는 AI 활용
- Reproducibility vulnerability scanning
- Overclaiming detection
- Statistical reporting format checking
- 문법 및 표현 개선
- Preemptive reviewer question 생성

### ❌ 금지되는 AI 활용
- 통계 수치 생성 또는 변경
- 연구 절차 허위 작성
- 존재하지 않는 데이터 생성
- 참고문헌 검증 없이 AI 추천 인용

### ⚠️ 주의사항
- AI 출력은 반드시 비판적으로 검토
- 통계 관련 AI 조언은 전문가 확인 권장
- Self-Audit Report에 AI 활용 과정 상세히 기록

---

## 평가 기준

| 항목 | 배점 | 세부 기준 |
|------|------|-----------|
| **Methods 재현성** | 25% | - 6요소 Checklist 충족 (≥24/30 목표)<br>- 구체적 수치와 파라미터<br>- 통제 전략 명확성 |
| **Results 통계 완결성** | 25% | - 완전한 통계 보고 (통계량+df+p+CI+효과크기)<br>- Overclaiming 제거<br>- Cherry-picking 방지 |
| **Self-Audit Report** | 25% | - 취약점 5개 이상 발견<br>- AI 프롬프트 3개 문서화<br>- Before/After 비교 포함 |
| **Red Team 방어** | 15% | - 받은 공격 3개 대응<br>- 구체적 수정 내용<br>- 방어 전략 적절성 |
| **형식 및 언어** | 10% | - APA 형식 준수<br>- 문법 정확성<br>- 일관된 시제 |

### 등급 기준

| 등급 | Reproducibility Score | 특징 |
|------|----------------------|------|
| A | ≥27/30 | 탑티어 저널 제출 준비 완료 |
| B | 24-26/30 | 약간의 수정 필요 |
| C | 21-23/30 | 상당한 수정 필요 |
| D | 18-20/30 | 재작성 권장 |
| F | <18/30 | 기본 요소 미충족 |

---

## 자주 묻는 질문

**Q1: Self-Audit Report에서 취약점 5개를 못 찾았으면?**
A: AI 프롬프트를 다양하게 시도해보세요. Recipe #35-40을 활용하면 대부분 5개 이상 발견됩니다. 정말 없다면, "취약점을 찾기 어려웠다"고 기술하고 그 이유를 분석하세요.

**Q2: Before/After 비교는 어느 정도 수정이어야 하나요?**
A: 단순 문법 수정보다는 내용적 개선이 좋습니다. 예: 재현성 향상, 통제 변수 추가, 효과크기 보고 추가 등.

**Q3: Red Team 공격을 받지 못했으면?**
A: 스스로 Red Team이 되어 자신의 논문을 공격해보세요. template_4.2의 8가지 공격 유형을 참고하세요.

**Q4: 통계 결과가 아직 없는 경우는?**
A: 예상 결과를 가정하여 작성하되, "예상 분석 계획" 또는 "가상 결과"임을 명시하세요. 통계 보고 형식은 완전하게 작성하세요.

**Q5: AI가 찾은 모든 취약점을 다 수정해야 하나요?**
A: 아닙니다. Self-Audit Report에서 "수정됨/미수정" 표시하고, 미수정 항목은 이유(시간, 데이터 제약 등)를 기술하세요.

---

## 제출 방법

**파일명:** `성명_Week4_Assignment.docx` 또는 `.pdf`

**제출처:** [온라인 시스템 또는 이메일]

**마감:** [날짜] 23:59

---

## 다음 주 준비 (Week 5)

- 전체 원고 통합본 (서론-방법-결과) 준비
- Discussion 섹션 초안 작성 시작
- 동료 전체 원고 교환 준비

**Week 5 Focus:** Discussion 작성 전략 및 전체 논리 일관성 검토
