# 4주차 실습: Methods/Results Bulletproofing 워크샵

## 실습 목표
- Top 10 거부 사유를 자신의 논문에서 진단하는 능력 개발
- AI 활용 Reproducibility Audit 경험
- Red Team/Blue Team 전략적 방어 연습
- 동료 피드백을 통한 취약점 발견 및 개선
- **궁극 목표: 리뷰어 공격 전에 자체 방어 완료**

---

## 준비물 확인

**필수 지참:**
- [ ] Methods 섹션 초안 (800-1000 words)
- [ ] Results 섹션 초안 (600-800 words)
- [ ] 최소 1개 Figure 또는 Table

**추천:**
- [ ] 노트북/태블릿 (AI 도구 접속용)
- [ ] 통계 분석 결과 원본 (상세 참조용)

---

## 실습 1: Rejection Reason 진단 (20분)

### 1.1 자기 진단: Methods 섹션 (10분)

**자신의 Methods를 읽고 Top 5 거부 사유 체크:**

| # | 거부 사유 | 내 Methods에서 발견? | 구체적 위치/문장 |
|---|-----------|---------------------|-----------------|
| 1 | Insufficient detail | ☐ 있음 / ☐ 없음 | |
| 2 | Inadequate controls | ☐ 있음 / ☐ 없음 | |
| 3 | Sample size issues | ☐ 있음 / ☐ 없음 | |
| 4 | Inappropriate statistics | ☐ 있음 / ☐ 없음 | |
| 5 | Validation gaps | ☐ 있음 / ☐ 없음 | |

**가장 심각한 문제 (1개 선택):**
```
문제:

왜 심각한가:

```

---

### 1.2 자기 진단: Results 섹션 (10분)

**자신의 Results를 읽고 Top 5 거부 사유 체크:**

| # | 거부 사유 | 내 Results에서 발견? | 구체적 위치/문장 |
|---|-----------|---------------------|-----------------|
| 6 | Overclaiming | ☐ 있음 / ☐ 없음 | |
| 7 | Cherry-picking | ☐ 있음 / ☐ 없음 | |
| 8 | Statistical issues | ☐ 있음 / ☐ 없음 | |
| 9 | Unclear presentation | ☐ 있음 / ☐ 없음 | |
| 10 | Weak effect sizes | ☐ 있음 / ☐ 없음 | |

**가장 심각한 문제 (1개 선택):**
```
문제:

왜 심각한가:

```

---

## 실습 2: AI Reproducibility Audit (25분)

### 2.1 Reproducibility Vulnerability Scanner (15분)

**AI 프롬프트 (Recipe #35):**
```
다음 Methods 섹션을 읽고, 다른 연구자가 재현하려 할 때
막힐 수 있는 지점 10가지를 찾아줘:

[여기에 자신의 Methods 전문 붙여넣기]

각 지점에 대해:
1. 무엇이 불명확한가?
2. 어떤 정보가 추가로 필요한가?
3. Before → After 예시 (한 문장)
```

**AI 분석 결과 기록:**

| # | 불명확한 점 | 필요한 정보 | Before → After |
|---|-------------|-------------|----------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

**6-10번은 뒷면 또는 노트에 기록**

---

### 2.2 6요소 Reproducibility Checklist (10분)

**자신의 Methods를 6가지 요소로 점수화:**

| 요소 | 내 점수 (0-5) | 부족한 부분 |
|------|--------------|-------------|
| 1. Participants | /5 | |
| 2. Materials | /5 | |
| 3. Procedure | /5 | |
| 4. Parameters | /5 | |
| 5. Software/Equipment | /5 | |
| 6. Data Processing | /5 | |
| **총점** | **/30** | |

**점수 기준:**
- 0: 전혀 언급 없음
- 1-2: 언급만 있음, 재현 불가
- 3: 부분적 재현 가능
- 4: 대부분 재현 가능
- 5: 완벽히 재현 가능

**목표: ≥24점 (80%)**

---

## 실습 3: Red Team/Blue Team Practice (25분)

### 3.1 공격 준비: Red Team (10분)

**동료와 Methods/Results 교환 후, Red Team이 되어 공격:**

**공격 대상:** ________________의 논문

**8가지 공격 유형 중 3가지 선택:**

| 공격 유형 | 내 공격 질문 |
|-----------|-------------|
| ☐ Sample Size Attack | |
| ☐ Control Attack | |
| ☐ Assumption Attack | |
| ☐ Multiple Comparison Attack | |
| ☐ Measurement Attack | |
| ☐ Overclaiming Attack | |
| ☐ Effect Size Attack | |
| ☐ Transparency Attack | |

**가장 치명적인 공격 (1개):**
```
공격:

왜 치명적인가:

```

---

### 3.2 방어 준비: Blue Team (10분)

**동료가 당신에게 한 공격에 대해 방어:**

**받은 공격 3가지:**
1.
2.
3.

**5가지 방어 전략 중 선택하여 대응:**

| 받은 공격 | 방어 전략 | 구체적 대응 |
|-----------|-----------|-------------|
| 공격 1 | ☐ Evidence-Based / ☐ Robustness / ☐ Sensitivity / ☐ Limitation / ☐ Future Work | |
| 공격 2 | ☐ Evidence-Based / ☐ Robustness / ☐ Sensitivity / ☐ Limitation / ☐ Future Work | |
| 공격 3 | ☐ Evidence-Based / ☐ Robustness / ☐ Sensitivity / ☐ Limitation / ☐ Future Work | |

---

### 3.3 라운드 결과 (5분)

**공격-방어 스코어링:**

| 라운드 | 공격 성공? (0-2) | 방어 성공? (0-2) | 점수 |
|--------|-----------------|-----------------|------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| **총점** | | | **/12** |

**스코어 기준:**
- 0: 완전 실패 (공격: 약함, 방어: 대응 못함)
- 1: 부분 성공 (어느 정도 유효)
- 2: 완전 성공 (날카로운 공격 / 완벽한 방어)

**최고의 공격 (클래스 공유용):**
```

```

**최고의 방어 (클래스 공유용):**
```

```

---

## 실습 4: Overclaiming 검증 (10분)

### 4.1 Claim-Evidence 매칭

**Results에서 주요 주장(claim) 3개 추출:**

| Claim # | 내 주장 (Results에서) | 뒷받침 증거 | 매칭 점수 (1-5) |
|---------|---------------------|------------|----------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |

**매칭 점수 기준:**
- 1: 증거 전혀 없음 (Overclaiming!)
- 2: 간접 증거만 있음
- 3: 증거 있으나 약함
- 4: 충분한 증거
- 5: 완벽한 증거-주장 매칭

---

### 4.2 AI Overclaiming Detector (선택)

**AI 프롬프트 (Recipe #38):**
```
다음 Results 섹션에서 overclaiming (과장된 주장)을 찾아줘:

[Results 전문]

각 overclaiming에 대해:
1. 문제가 되는 문장 인용
2. 왜 overclaiming인가?
3. 수정된 표현 제안
```

**AI 결과:**
```

```

---

## 실습 5: 동료 피드백 및 Priority Action (15분)

### 5.1 피드백 교환 (10분)

**피드백 대상:** ________________

**6차원 평가:**

| 차원 | 점수 (1-5) | 한 줄 코멘트 |
|------|----------|-------------|
| 1. Reproducibility | | |
| 2. Control Strategy | | |
| 3. Statistical Justification | | |
| 4. Claim-Evidence Match | | |
| 5. Statistical Rigor | | |
| 6. Transparency | | |
| **총점** | **/30** | |

**Top 3 강점:**
1.
2.
3.

**Top 3 개선 필요:**
1.
2.
3.

---

### 5.2 Priority Action Planning (5분)

**받은 피드백 요약:**
1.
2.
3.

**즉시 수정할 것 (Top 3):**

| 우선순위 | 수정 내용 | 예상 소요 시간 |
|----------|----------|---------------|
| 1 | | 분 |
| 2 | | 분 |
| 3 | | 분 |

**수정 전/후 예시 (1개):**

Before:
```

```

After:
```

```

---

## 성찰 일지

### AI 활용 성찰

**1. AI Audit에서 가장 유용했던 발견:**
```

```

**2. AI가 놓친 것 / 내가 더 잘 발견한 것:**
```

```

**3. 오늘 사용한 가장 효과적인 프롬프트:**
```

```

---

### Red Team/Blue Team 성찰

**4. 가장 예상 못한 공격:**
```

```

**5. 방어하기 가장 어려웠던 점:**
```

```

**6. 다음에 미리 대비할 것:**
```

```

---

### Methods/Results 작성 개선

**7. 오늘 발견한 내 논문의 가장 큰 취약점:**
```

```

**8. 이를 해결하기 위한 구체적 계획:**
```

```

---

## 완료 체크리스트

### 실습 완료 확인
- [ ] 실습 1: Top 10 거부 사유 자기 진단 완료
- [ ] 실습 2: AI Reproducibility Audit 완료 (≥5개 취약점 발견)
- [ ] 실습 2: 6요소 Reproducibility Checklist 점수화 완료
- [ ] 실습 3: Red Team 공격 3개 수행
- [ ] 실습 3: Blue Team 방어 3개 수행
- [ ] 실습 4: Claim-Evidence 매칭 검토 완료
- [ ] 실습 5: 동료 피드백 교환 완료
- [ ] 실습 5: Priority Action 3개 선정 완료
- [ ] 성찰 일지 작성 완료

### 과제 준비
- [ ] Methods 수정본 작성 시작
- [ ] Results 수정본 작성 시작
- [ ] Self-Audit Report 준비

---

## 핵심 AI 프롬프트 Quick Reference

### Recipe #35: Reproducibility Scanner
```
다음 Methods에서 재현 막힘 지점 10개 찾아줘: [Methods]
```

### Recipe #36: Control Strategy Auditor
```
다음 연구 설계에서 빠진 통제 변수와 대안 설명 찾아줘: [Methods]
```

### Recipe #37: Statistical Assumption Checker
```
다음 통계 분석의 가정 위배 가능성 검토해줘: [Analysis description]
```

### Recipe #38: Overclaiming Detector
```
다음 Results에서 증거를 넘어선 주장 찾아줘: [Results]
```

### Recipe #39: Statistical Rigor Validator
```
다음 통계 보고가 완전한지 체크해줘 (effect size, CI, power): [Results]
```

### Recipe #40: Preemptive Reviewer Response
```
다음 Methods/Results에 대해 리뷰어가 제기할 질문 5개와 대응 초안: [Text]
```

---

## 다음 주 준비

**Week 5 과제:**
- Methods/Results 수정 최종본
- Self-Audit Report (AI 활용 결과 포함)
- Discussion 섹션 초안

**목표 점수:**
- Reproducibility Checklist: ≥24/30
- Peer Review Rubric: ≥24/30
- Overclaiming: 0개
