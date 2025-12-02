# 코드 온보딩 가이드

## 📚 프로젝트 개요

**심리과학 연구방법 - 롸이팅**은 6주 집중 대학원 논문 작성 과정입니다.

### 핵심 목표
> "어떻게 하면 탑티어 저널에 출판할 만한 탑 5%의 논문을 쓸 것인가"

### 주요 특징
- **대상**: 심리학과 대학원생 (석사/박사)
- **기간**: 6주 (주 1회, 90분)
- **형식**: IMRaD (Introduction, Methods, Results, and Discussion)
- **AI 도구**: ChatGPT, Claude, Perplexity, Elicit
- **교수법**: 실전 전략 중심 (AI 개념 설명 제거)

---

## 📁 디렉토리 구조

```
.
├── README.md                    # 프로젝트 메인 문서
├── CLAUDE.md                    # AI 어시스턴트 컨텍스트 (중요!)
├── 강의계획.md                  # 상세 강의 계획
├── overlap_analysis.md          # 윤경생 박사님 강의와의 중복 분석
│
├── claudedocs/                  # 강사용 전략 문서
│   ├── comprehensive_revision_plan.md
│   ├── week2_revision_strategy.md
│   ├── week3_revision_strategy.md
│   ├── week4_revision_strategy.md
│   └── figma_workshop_weeks2-6.md
│
├── week1/                       # Week 1: 인간 중심 글쓰기 (AI 미사용)
│   ├── lecture_notes.md         # 원본 상세 강의노트 (참고용)
│   ├── lesson_notes_compressed_90min.md  # 압축 강의노트 (23슬라이드)
│   ├── workshop_materials.md     # 실습 자료 (Bad Sentences + Smart Revising)
│   ├── teaching_guide_90min.md   # 분 단위 강의 가이드
│   ├── figma_workshop_guide.md   # Figma 워크샵 가이드
│   ├── create_notion_workshop_simple.py  # Notion 워크샵 생성 스크립트 ✅
│   └── [기타 실습/과제 파일들]
│
├── week2/                       # Week 2: AI 활용 I - 초록 작성
│   ├── lecture_notes.md         # Nature/Science급 초록 전략 (1421 lines)
│   ├── lesson_slides_15min.md    # 15분 강의 슬라이드
│   ├── peer_feedback_session_plan.md  # 피어 피드백 세션 설계
│   ├── selected_papers.md        # Nature/Science 논문 예시
│   ├── upload_lecture_notes.py  # Notion 업로드 스크립트 ✅
│   └── [기타 실습/과제 파일들]
│
├── week3/                       # Week 3: AI 활용 II - 체계적 Research Gap 발견
│   └── lecture_notes.md         # Gap 발견 워크플로우 (553 lines)
│
├── week4/                       # Week 4: AI 활용 III - Methods/Results Bulletproofing
│   └── lecture_notes.md         # Methods/Results 방어 전략 (718 lines)
│
├── week5/                       # Week 5: Discussion 섹션
│   └── lecture_notes.md
│
├── week6/                       # Week 6: Peer Review & Revision
│   └── lecture_notes.md
│
├── scientific_writing_workbook/  # 웹 기반 워크북
│   ├── index.html
│   ├── week1.html
│   ├── week2.html
│   └── [assets, script.js, style.css]
│
└── materials/                   # 기타 자료
    └── [PDF, PPTX 파일들]
```

---

## 🔑 핵심 문서

### 1. **README.md** - 프로젝트 메인 문서
- 전체 강의 개요
- 주차별 스케줄
- 학습 목표 및 성과 지표
- **처음 읽어야 할 문서**

### 2. **CLAUDE.md** - AI 어시스턴트 컨텍스트
- 강의 철학 및 원칙
- Week 2-4 수정 원칙 (윤경생 박사님 강의와 중복 제거)
- Figma/Notion 워크샵 구조
- **AI 어시스턴트가 참고하는 핵심 문서**

### 3. **overlap_analysis.md** - 중복 분석
- 윤경생 박사님의 AI 개념 강의와의 중복 분석
- Week 2-4에서 제거해야 할 개념 설명
- 실전 전략으로 전환하는 방법

### 4. **강의계획.md** - 상세 강의 계획
- 주차별 상세 수업 계획
- 90분 수업 구조
- 과제 및 평가 기준

---

## 🐍 Python 스크립트

### Notion 통합 스크립트

#### 1. `week1/create_notion_workshop_simple.py` ✅
**목적**: Week 2-6 Notion 워크샵 기본 구조 생성

**기능**:
- Student Submissions Database 생성
- AI Recipe Library Database 생성
- Week 2-6 페이지 생성

**사용법**:
```bash
export NOTION_TOKEN='your_token'
python week1/create_notion_workshop_simple.py <parent_page_id>
```

**생성 결과**:
- 2개 데이터베이스 (Student Submissions, AI Recipe Library)
- 5개 Week 페이지 (Week 2-6)

#### 2. `week2/upload_lecture_notes.py` ✅
**목적**: Markdown 파일을 Notion 페이지에 업로드

**기능**:
- Markdown → Notion blocks 변환
- 100개 블록 단위 배치 처리
- 인라인 포맷팅 지원 (bold, italic, code, strikethrough)
- 테이블, 코드 블록, 리스트 처리

**사용법**:
```bash
export NOTION_TOKEN='your_token'
python week2/upload_lecture_notes.py <page_id>
```

**성공 사례** (2025-01-04):
- `lecture_notes.md` (1421 lines, 69KB)
- → 617 blocks in 7 batches
- < 2 minutes

**중요**: Notion 업로드는 **항상 이 스크립트 사용** (수동 복사-붙여넣기 금지)

#### 3. `week2/download_notion_to_md.py`
**목적**: Notion 페이지를 Markdown으로 다운로드

**사용법**:
```bash
python week2/download_notion_to_md.py <page_id> <output.md>
```

#### 4. `week2/update_page_title.py`
**목적**: Notion 페이지 제목 업데이트

**사용법**:
```bash
python week2/update_page_title.py <page_id> "New Title"
```

### 기타 스크립트

#### `week1/create_notion_workshop_week2_6.py`
- 복잡한 버전 (참고용)
- Notion API 제한으로 인해 일부 기능 미구현

#### `week1/test_notion_db.py`
- Notion 데이터베이스 테스트 스크립트

---

## 🎯 주요 워크플로우

### 1. 강의 자료 준비

#### Week 1 (Figma 워크샵)
1. `week1/lesson_notes_compressed_90min.md` 확인 (23슬라이드)
2. `week1/workshop_materials.md` 확인 (실습 자료)
3. `week1/figma_workshop_guide.md` 참고하여 Figma 설정
4. 수업 전 10분: Figma 템플릿 복사 및 링크 공유

#### Week 2-6 (Notion 워크샵)
1. `weekN/lecture_notes.md` 확인
2. Notion 페이지에 강의 자료 업로드:
   ```bash
   python week2/upload_lecture_notes.py <page_id>
   ```
3. 수업 전: Notion 워크샵 페이지 확인

### 2. Notion 워크샵 설정 (최초 1회)

```bash
# 1. 환경 변수 설정
export NOTION_TOKEN='your_notion_integration_token'

# 2. 기본 구조 생성
python week1/create_notion_workshop_simple.py <parent_page_id>

# 3. 각 Week 페이지에 강의 자료 업로드
python week2/upload_lecture_notes.py <week2_page_id>
python week2/upload_lecture_notes.py <week3_page_id>
# ... (Week 4-6도 동일)
```

### 3. 강의 자료 수정

1. `weekN/lecture_notes.md` 수정
2. Notion에 업로드:
   ```bash
   python week2/upload_lecture_notes.py <page_id>
   ```
   **주의**: 기존 내용을 덮어쓰지 않으므로, Notion에서 수동 삭제 후 업로드하거나 새 페이지 생성

---

## 📖 주차별 핵심 내용

### Week 1: 인간 중심 글쓰기 (AI 미사용)
- **목표**: 기본 글쓰기 원칙 마스터
- **형식**: Figma 워크샵 (50분 실습)
- **핵심 원칙**: 10가지 (주어-동사, 응집성, 간결성)
- **실습**: Bad Sentences 수술실, Smart Revising 7단계

### Week 2: AI 활용 I - 초록 작성
- **목표**: Nature/Science급 초록 작성
- **전략**: 4가지 Opening 패턴, Broad significance framing
- **AI 레시피**: 40+ 프롬프트
- **형식**: Notion 워크샵

### Week 3: AI 활용 II - 체계적 Research Gap 발견
- **목표**: Conceptual Gap 발견 및 검증
- **전략**: 3단계 Gap Validation 워크플로우
- **AI 레시피**: 30+ 프롬프트
- **형식**: Notion 워크샵

### Week 4: AI 활용 III - Methods/Results Bulletproofing
- **목표**: 탑티어 저널 거부 사유 방어
- **전략**: Reproducibility Checklist, Control validation
- **AI 레시피**: 40+ 프롬프트
- **형식**: Notion 워크샵

### Week 5-6: Discussion, Peer Review, Revision
- **목표**: 논문 완성 및 피어 리뷰
- **형식**: Notion 워크샵

---

## ⚠️ 중요 원칙

### 1. AI 개념 설명 금지 (Week 2-4)
학생들은 윤경생 박사님 강의에서 이미 다음을 학습했습니다:
- ✅ Prompt Engineering 기초
- ✅ Parameters (Temperature, Top-k, Top-p)
- ✅ In-context Learning (zero-shot, one-shot, few-shot)
- ✅ RAG (Retrieval-Augmented Generation)
- ✅ Chain-of-Thought (CoT)

**따라서 Week 2-4는 개념 설명을 완전히 제거하고 실전 전략에만 집중합니다.**

### 2. Notion 업로드는 항상 Python 스크립트 사용
- ❌ 수동 복사-붙여넣기 금지
- ❌ Notion import 기능 사용 금지
- ✅ `upload_lecture_notes.py` 사용

**이유**:
- 자동화 가능 (반복 작업)
- 배치 처리 (API 제한 자동 처리)
- 빠름 (< 2분 vs 30+분 수동)

### 3. 실전 전략 중심
모든 내용은 다음 질문에 답해야 합니다:
- "이것이 Nature/Science 출판에 어떻게 도움이 되나?"
- "탑 5% 논문은 어떤 전략을 사용하나?"
- "내 연구에 어떻게 적용하나?"

---

## 🛠️ 개발 환경 설정

### 필수 요구사항
```bash
# Python 3.7+
python --version

# 필수 패키지
pip install notion-client requests

# 환경 변수
export NOTION_TOKEN='your_notion_integration_token'
```

### Notion Integration 설정
1. Notion → Settings → Connections → Develop integrations
2. 새 Integration 생성
3. Integration Token 복사
4. 워크스페이스에 Integration 추가 (페이지 공유)

### 테스트
```bash
# Notion 연결 테스트
python week1/test_notion_db.py
```

---

## 📝 파일 작성 가이드

### 강의노트 작성 시
1. **Markdown 형식** 사용
2. **구조화된 섹션**: Heading 1-3 활용
3. **코드 블록**: 프롬프트는 코드 블록으로
4. **예시 포함**: 실제 Nature/Science 논문 예시
5. **평가 기준**: 각 전략에 대한 평가 기준 명시

### 프롬프트 레시피 작성 형식
```markdown
### [번호]. [레시피 이름]
**목적**: [이 레시피가 달성하는 것]
**프롬프트**:
```
[실제 프롬프트 템플릿]
```
**결과 평가 기준**: [출력을 평가하는 방법]
```

---

## 🔍 문제 해결

### Notion 업로드 실패
1. `NOTION_TOKEN` 확인
2. 페이지 ID 형식 확인 (하이픈 포함/미포함)
3. Integration이 페이지에 접근 권한 있는지 확인

### Figma 워크샵 문제
- `week1/figma_workshop_guide.md` 참고
- 학생 접근 권한 확인 (Edit 권한 필요)

### 강의 자료 수정
1. Markdown 파일 수정
2. Notion 업로드 스크립트 실행
3. **주의**: 기존 내용 덮어쓰기 안 됨 → 새 페이지 또는 수동 삭제

---

## 📚 추가 리소스

### 강사용 문서
- `claudedocs/comprehensive_revision_plan.md`: 전체 수정 계획
- `claudedocs/weekN_revision_strategy.md`: 주차별 전략

### 학생용 자료
- `weekN/lecture_notes.md`: 강의노트
- `weekN/practice.md`: 실습 자료
- `weekN/assignment.md`: 과제 안내

### 워크샵 가이드
- `week1/figma_workshop_guide.md`: Figma 워크샵 완전 가이드
- `week1/NOTION_WORKSHOP_DESIGN.md`: Notion 워크샵 설계 문서

---

## 🎓 빠른 시작 체크리스트

### 첫 설정 (최초 1회)
- [ ] `README.md` 읽기
- [ ] `CLAUDE.md` 읽기
- [ ] `overlap_analysis.md` 읽기
- [ ] Notion Integration 설정
- [ ] `NOTION_TOKEN` 환경 변수 설정
- [ ] Notion 워크샵 기본 구조 생성

### 주차별 준비
- [ ] 해당 주차 `lecture_notes.md` 확인
- [ ] Notion 페이지에 강의 자료 업로드
- [ ] 실습 자료 준비 (Figma/Notion)
- [ ] 과제 확인

### 수업 후
- [ ] 학생 제출물 확인
- [ ] 성공한 AI 레시피 Recipe Library에 추가
- [ ] 다음 주차 자료 준비

---

## 💡 팁

1. **CLAUDE.md를 항상 참고**: AI 어시스턴트가 이 문서를 기반으로 답변합니다
2. **Notion 스크립트 활용**: 수동 작업은 피하고 자동화 스크립트 사용
3. **실전 예시 중심**: 추상적 설명보다 실제 Nature/Science 논문 예시
4. **학생 피드백 수집**: Recipe Library에 성공 사례 축적

---

**Last Updated**: 2025-01-09
**Maintained by**: 차지욱 (Jiook Cha), 서울대학교 심리학과

