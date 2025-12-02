# Lecture Notes 업데이트 프롬프트

> **목적**: `examples_introduction_top_tier_patterns.md`에 추가된 실제 논문 예제들을 `lecture_notes.md`에 반영하여 강의 노트를 업데이트
> 
> **기준 파일**: 
> - 현재: `week3/lecture_notes.md`
> - 참고: `week3/examples_introduction_top_tier_patterns.md`

---

## 📋 업데이트 전략

### 1. 실제 논문 예제 통합

**현재 상태**:
- `lecture_notes.md`는 이론적 설명과 가상 예제 중심
- `examples_introduction_top_tier_patterns.md`에는 실제 논문 예제 4개 포함

**업데이트 목표**:
- 실제 논문 예제를 강의 노트에 직접 통합
- 각 Gap 패턴별로 실제 예제 참조 추가
- 실습 활동에 실제 예제 활용 방법 포함

---

## 📋 구체적 업데이트 항목

### A. Section 1: 탑티어 저널의 "Gap" 기준 업데이트

**현재 위치**: `lecture_notes.md` 라인 43-55

**추가할 내용**:

```markdown
### 1.3 실제 예제: 탑티어 저널의 Gap-Driven 구조

**실제 논문 예제** (자세한 분석은 `examples_introduction_top_tier_patterns.md` 참조):

1. **Conceptual Gap**: PNAS (2022) - "Why are people antiscience, and what can we do about it?"
   - 기존 모델들(attitude roots, jiu jitsu)과 classic perspective on attitudes and persuasion의 연결 부재
   - 4가지 basis를 통한 통합 프레임워크 제시

2. **Mechanistic Gap**: JAMA Psychiatry (2021) - "Reinforcement Learning Disruptions in Individuals With Depression and Sensitivity to Symptom Change Following Cognitive Behavioral Therapy"
   - CBT 효과는 알려져 있으나 강화학습 메커니즘과의 관계 불명
   - Computational model-based analyses로 정밀한 메커니즘 규명

3. **Translational Gap**: Science Advances (2020) - "A psychological intervention strengthens students' peer social networks and promotes persistence in STEM"
   - 개인 수준 개입 효과는 알려져 있으나 사회적 네트워크로의 전이 불명
   - Values affirmation → 사회적 네트워크 강화 → STEM 지속성 향상

4. **Paradox Gap**: PNAS (2020) - "Gender stereotypes can explain the gender-equality paradox"
   - 성평등 국가에서 오히려 성별 격차가 큰 모순
   - 문화적 gender identity 프레임워크로 설명

**학습 방법**:
- 각 예제의 Introduction을 읽고 4단계 구조(Established Knowledge → Emerging Challenges → Critical Gap → Research Opportunity)를 직접 확인
- 자신의 gap과 비교하여 어떤 패턴에 해당하는지 판단
```

---

### B. Section 4: Gap-Driven 문헌 리뷰 구조화 업데이트

**현재 위치**: `lecture_notes.md` 라인 250-298

**추가할 내용**:

```markdown
### 4.3 실제 예제로 학습하기

**실습 활동**: `examples_introduction_top_tier_patterns.md`의 실제 논문 예제 분석

**Step 1: 예제 선택**
- 자신의 연구 주제와 가장 유사한 Gap 패턴의 예제 선택
- 예: 임상심리학 연구 → Mechanistic Gap 예제 (JAMA Psychiatry)

**Step 2: 4단계 구조 분석**
```
각 예제의 Introduction을 읽으면서:

1. Established Knowledge (확립된 지식)
   - [ ] 어떤 consensus를 통합하는가?
   - [ ] 어떤 인용 전략을 사용하는가? (숫자 인용 vs 상세 인용)
   - [ ] 다층적 증거(행동, 신경, 이론)를 제시하는가?

2. Emerging Challenges (새로운 도전)
   - [ ] 어떤 모순/한계를 제시하는가?
   - [ ] Paradox를 명명하는가? ("gender-equality paradox")
   - [ ] 이론적 도전을 구체화하는가?

3. Critical Gap (핵심 공백)
   - [ ] Gap statement가 명확한 질문으로 제시되는가?
   - [ ] Bold로 강조하는가?
   - [ ] 구체적 하위 질문으로 세분화하는가?

4. Research Opportunity (연구 기회)
   - [ ] Named framework를 제시하는가?
   - [ ] 구체적 방법을 명시하는가?
   - [ ] Testable prediction을 포함하는가?
   - [ ] Broader impact를 언급하는가?
```

**Step 3: 자신의 Introduction과 비교**
- 자신의 Introduction을 같은 4단계 구조로 분석
- 각 단계에서 실제 예제와 비교하여 부족한 점 파악
- AI로 개선 요청

**AI 프롬프트 예시**:
```
"다음은 실제 PNAS 논문의 Introduction 구조입니다:

[예제 1.1의 4단계 구조 발췌]

내 Introduction은 다음과 같습니다:

[내 Introduction]

실제 예제와 비교하여:
1. 각 단계에서 부족한 점은 무엇인가?
2. 어떤 표현/구조를 참고할 수 있는가?
3. Nature/Science 수준으로 개선하려면 어떻게 해야 하는가?"
```
```

---

### C. Section 6: 참고 자료 업데이트

**현재 위치**: `lecture_notes.md` 라인 568-596

**업데이트 내용**:

```markdown
## 참고 자료

### 📚 핵심 자료: 탑티어 Introduction 예제 모음

**`examples_introduction_top_tier_patterns.md`** (⭐ 필수 읽기)

**실제 논문 예제 4개** (모두 상위 10% 저널):

1. **Conceptual Gap**: PNAS (2022, IF ~12)
   - 제목: "Why are people antiscience, and what can we do about it?"
   - URL: https://www.pnas.org/doi/10.1073/pnas.2120755119
   - 핵심: 기존 모델들과 classic perspective on attitudes and persuasion의 연결 부재
   - 4가지 basis를 통한 통합 프레임워크

2. **Mechanistic Gap**: JAMA Psychiatry (2021, IF ~25)
   - 제목: "Reinforcement Learning Disruptions in Individuals With Depression and Sensitivity to Symptom Change Following Cognitive Behavioral Therapy"
   - URL: https://jamanetwork.com/journals/jamapsychiatry/fullarticle/2782452
   - 핵심: CBT 효과는 알려져 있으나 강화학습 메커니즘과의 관계 불명
   - Computational model-based analyses로 메커니즘 규명

3. **Translational Gap**: Science Advances (2020, IF ~14, Science family)
   - 제목: "A psychological intervention strengthens students' peer social networks and promotes persistence in STEM"
   - URL: https://www.science.org/doi/10.1126/sciadv.aba9221
   - 핵심: 개인 수준 개입 → 사회적 네트워크 → STEM 지속성
   - Values affirmation이 사회적 방어를 줄여 네트워크 강화

4. **Paradox Gap**: PNAS (2020, IF ~12)
   - 제목: "Gender stereotypes can explain the gender-equality paradox"
   - URL: https://www.pnas.org/doi/10.1073/pnas.2008704117
   - 핵심: 성평등 국가에서 오히려 성별 격차가 큰 모순
   - 문화적 gender identity 프레임워크로 설명

**학습 방법**:
1. 각 예제의 Introduction을 직접 읽기 (URL 클릭)
2. 4단계 구조를 직접 확인하며 분석
3. 자신의 연구 주제와 유사한 패턴의 예제를 선택하여 심층 분석
4. 자신의 Introduction과 비교하여 개선점 도출

**실습 활동**:
- Workshop Phase 1에서 실제 예제 1개를 선택하여 4단계 구조 분석
- 자신의 gap statement와 비교하여 어떤 패턴에 해당하는지 판단
- 실제 예제의 표현/구조를 참고하여 자신의 gap statement 강화
```

---

### D. Workshop 실습 활동 업데이트

**현재 위치**: `lecture_notes.md` 라인 409-451

**추가할 활동**:

```markdown
### Phase 0: 실제 예제 분석 (10분) - NEW!

**Activity 0: 탑티어 Introduction 패턴 학습**
- `examples_introduction_top_tier_patterns.md`에서 자신의 연구 주제와 유사한 Gap 패턴의 예제 선택
- 선택한 예제의 Introduction을 읽고 4단계 구조 직접 확인
- 각 단계에서 어떤 표현/구조를 사용하는지 체크리스트로 분석
- 동료와 선택한 예제 공유 및 패턴 비교

**체크리스트**:
- [ ] Established Knowledge: Consensus 통합 방식 확인
- [ ] Emerging Challenges: 모순/한계 제시 방식 확인
- [ ] Critical Gap: Gap statement 작성 방식 확인
- [ ] Research Opportunity: Framework 제시 및 방법 명시 방식 확인
```

---

### E. 과제 업데이트

**현재 위치**: `lecture_notes.md` 라인 455-519

**추가할 요구사항**:

```markdown
### "My Research Gap - Validated & Justified"

**제출물:**

1. **Gap Discovery Documentation (800 words)**
   [...기존 내용...]

2. **Gap Statement (150-200 words)**
   [...기존 내용...]
   
   **NEW**: 자신의 gap이 `examples_introduction_top_tier_patterns.md`의 어떤 패턴에 해당하는지 명시
   - Conceptual / Mechanistic / Translational / Paradox 중 선택
   - 선택한 패턴의 실제 예제와 비교하여 유사점/차이점 설명 (100 words)

3. **Gap-driven 문헌 리뷰 구조 (500 words)**
   [...기존 내용...]
   
   **NEW**: 실제 예제를 참고하여 작성
   - 선택한 패턴의 실제 예제 구조를 참고
   - 각 단계에서 실제 예제의 표현/구조를 어떻게 적용했는지 설명

4. **AI 활용 과정 (500 words)**
   [...기존 내용...]

5. **Peer Review 반영 (300 words)**
   [...기존 내용...]

6. **실제 예제 비교 분석 (200 words) - NEW!**
   - 자신의 gap과 유사한 패턴의 실제 예제 선택
   - 실제 예제의 4단계 구조와 자신의 구조 비교
   - 실제 예제에서 배운 점 및 적용한 점
   - 개선이 필요한 부분 및 계획
```

---

## 📋 업데이트 실행 순서

### Step 1: 파일 읽기
```
1. 현재 lecture_notes.md 전체 읽기
2. examples_introduction_top_tier_patterns.md의 실제 예제 4개 확인
3. 각 예제의 저널, 연도, 제목, URL 정보 확인
```

### Step 2: Section별 업데이트

**A. Section 1 업데이트** (라인 43-55 이후)
- 1.3 실제 예제 섹션 추가
- 각 Gap 패턴별 실제 논문 예제 1개씩 요약

**B. Section 4 업데이트** (라인 250-298 이후)
- 4.3 실제 예제로 학습하기 섹션 추가
- 실습 활동 및 AI 프롬프트 예시 포함

**C. Section 6 업데이트** (라인 568-596)
- 참고 자료 섹션을 실제 논문 정보로 업데이트
- 각 예제의 저널, IF, URL, 핵심 내용 포함

**D. Workshop 실습 업데이트** (라인 409-451)
- Phase 0: 실제 예제 분석 활동 추가
- 기존 Phase 번호 조정 (Phase 1 → Phase 2 등)

**E. 과제 업데이트** (라인 455-519)
- 실제 예제 비교 분석 요구사항 추가
- 평가 기준에 실제 예제 활용도 추가

### Step 3: 일관성 검증

**확인 사항**:
- [ ] 모든 실제 논문 정보가 정확한가? (저널, 연도, 제목, URL)
- [ ] Gap 패턴 분류가 일관되는가?
- [ ] 실제 예제 참조가 명확한가?
- [ ] 실습 활동이 실제 예제를 활용하는가?
- [ ] 과제 요구사항이 실제 예제를 포함하는가?

### Step 4: 최종 검토

**검토 체크리스트**:
- [ ] 실제 논문 예제 4개가 모두 언급되는가?
- [ ] 각 예제의 핵심 내용이 정확히 요약되는가?
- [ ] 학생들이 실제 예제를 활용할 수 있는 구체적 가이드가 있는가?
- [ ] AI 프롬프트 예시가 실제 예제를 활용하는가?
- [ ] Workshop 활동이 실제 예제 분석을 포함하는가?

---

## 📋 업데이트 시 주의사항

### 1. 기존 내용 보존
- 기존 이론적 설명은 그대로 유지
- 실제 예제는 **보완**하는 형태로 추가
- 가상 예제는 유지하되, 실제 예제를 우선 참조하도록 안내

### 2. 실제 논문 정보 정확성
- 저널명, IF, 연도, 제목, URL 모두 정확히 확인
- `examples_introduction_top_tier_patterns.md`의 정보와 일치하는지 확인

### 3. 학습 흐름 자연스러움
- 이론 설명 → 실제 예제 → 실습 활동 순서 유지
- 실제 예제가 자연스럽게 통합되도록 배치

### 4. 학생 접근성
- 실제 예제 URL이 클릭 가능한지 확인
- 각 예제의 핵심 내용이 명확히 요약되어 있는지 확인
- 실습 활동이 구체적이고 실행 가능한지 확인

---

## 📋 업데이트 후 검증

### 최종 검증 질문

1. **완전성**: 실제 논문 예제 4개가 모두 언급되는가?
   - [ ] Conceptual Gap: PNAS (2022)
   - [ ] Mechanistic Gap: JAMA Psychiatry (2021)
   - [ ] Translational Gap: Science Advances (2020)
   - [ ] Paradox Gap: PNAS (2020)

2. **정확성**: 모든 정보가 정확한가?
   - [ ] 저널명
   - [ ] Impact Factor
   - [ ] 연도
   - [ ] 제목
   - [ ] URL

3. **활용성**: 학생들이 실제 예제를 활용할 수 있는가?
   - [ ] 실습 활동에 실제 예제 분석 포함
   - [ ] AI 프롬프트 예시에 실제 예제 활용
   - [ ] 과제에 실제 예제 비교 분석 요구

4. **일관성**: 전체 강의 노트가 일관되는가?
   - [ ] Gap 패턴 분류 일관
   - [ ] 실제 예제 참조 일관
   - [ ] 학습 목표와 실제 예제 연결

---

## 📋 실행 명령어 (참고용)

### 실제 업데이트 시 사용할 명령어

```python
# Step 1: 파일 읽기
read_file("week3/lecture_notes.md")
read_file("week3/examples_introduction_top_tier_patterns.md", offset=33, limit=100)  # 예제 1.1
read_file("week3/examples_introduction_top_tier_patterns.md", offset=183, limit=70)  # 예제 2.1
read_file("week3/examples_introduction_top_tier_patterns.md", offset=319, limit=60)  # 예제 3.1
read_file("week3/examples_introduction_top_tier_patterns.md", offset=413, limit=60)  # 예제 4.1

# Step 2: Section별 업데이트
# A. Section 1에 1.3 추가
search_replace(
    file_path="week3/lecture_notes.md",
    old_string="### 1.2 실습: Gap Quality 평가",
    new_string="### 1.2 실습: Gap Quality 평가\n\n[1.3 실제 예제 섹션 추가]"
)

# B. Section 4에 4.3 추가
# C. Section 6 업데이트
# D. Workshop 실습 업데이트
# E. 과제 업데이트
```

---

## 📋 예상 소요 시간

- **파일 읽기 및 분석**: 10분
- **Section별 업데이트**: 30-40분
  - Section 1: 5분
  - Section 4: 10분
  - Section 6: 5분
  - Workshop: 10분
  - 과제: 10분
- **일관성 검증**: 10분
- **최종 검토**: 10분

**총 예상 시간**: 60-70분

---

## 📋 성공 기준

### 최종 성공 기준

1. ✅ **실제 논문 예제 통합**: 4개 예제가 모두 강의 노트에 언급됨
2. ✅ **학습 가이드 제공**: 학생들이 실제 예제를 어떻게 활용할지 명확한 가이드
3. ✅ **실습 활동 통합**: Workshop에 실제 예제 분석 활동 포함
4. ✅ **과제 연계**: 과제에 실제 예제 비교 분석 요구사항 포함
5. ✅ **정보 정확성**: 모든 저널, IF, 연도, 제목, URL 정확
6. ✅ **일관성**: 전체 강의 노트가 일관된 구조와 내용

---

**주의**: 이 프롬프트는 실행하지 말고, 검토 후 실행하세요.

