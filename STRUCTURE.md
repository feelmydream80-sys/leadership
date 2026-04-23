# 리더십 분석 시스템 구조 문서

## 1. 시스템 개요

| 항목 | 값 |
|------|-----|
| 플랫폼 | Flask + SQLite |
| 포트 | 5000 |
| 핵심 모듈 | NLP Pipeline + Leadership Engine |

---

## 2. 분석 메뉴별 Stage流程

### 2.1 개별 分析 (/ 或 index.html)

| Stage | 단계 | 설명 | 백엔드/module |
|-------|------|------|-------------|
| 1 | 텍스트 입력 | 사용자 입력 텍스트 수신 | app.py:400 |
| 2 | 프롬프트 생성 | LLM용 프롬프트 구성 | nlp_pipeline.py:build_llm_prompt |
| 3 | LLM 호출 | Gemini/OpenRouter/Ollama API 호출 | nlp_pipeline.py:call_llm_with_retry |
| 4 | Confidence Calibration | 0.88 보정 계수 적용 | nlp_pipeline.py:apply_calibration |
| 5 | Low Confidence 필터링 | threshold 0.5 미만 제거 | nlp_pipeline.py:filter_low_confidence |
| 6 | 문장 Weight 적용 | 중요 키워드 포함 시 1.2 가중치 | nlp_pipeline.py:apply_sentence_weights |
| 7 | Trait 추론 | LeadershipEngine.process() 실행 | app.py:530 |
| 8 | 결과 반환 | Primary/Secondary Trait, Risks, Hybrids | app.py:584 |

#### Debug Info 출력
각 Stage별 로깅은 `debug_info` 배열에 저장되어 프론트엔드에 전송됨:
- `app.py:420-426` - Step 1: 프롬프트 생성
- `app.py:470-476` - Step 2: LLM 응답
- `app.py:484-490` - Step 3: Calibration
- `app.py:497-503` - Step 4: 필터링
- `app.py:509-515` - Step 5: 문장 Weight
- `app.py:533-539` - Step 6: Trait 추론

### 2.2 대시보드 (/dashboard)

| 기능 | 설명 |
|------|------|
| 기간별 필터 | 일/주/월/연/전체 |
| 부서/직급 필터 | 부서, 직급, 직무级别별 필터링 |
| Trait 분포 | Radar + Bar Chart |
| Positive/Negative | 비율 Doughnut Chart |
| 일별 추이 | Line Chart |
| Trait 추이 | 기간별 Trait 변화 |

### 2.3 대규모 분석 (/bulk)

- 대량 텍스트 일괄 처리

---

## 3. 테스트 메뉴

| 메뉴 | 파일 | 문항수 |
|------|------|-------|
| 선택형 테스트 | quiz_questions.json | 30 |
| 상황 카드 | situation_cards.json | 8 |
| 복합 테스트 | hybrid_tests.json | 3 |
| 부정 탐지 | negative_tests.json | 10 |

---

## 4. 설정 메뉴

| 메뉴 | 설명 |
|------|------|
| API 설정 | GEMINI_API_KEY, OPENROUTER_API_KEY, Ollama |
| 라벨 관리 | Micro Label CRUD |

---

## 5. 데이터 구조

```
data/
├── labels/
│   ├── positive_labels.json    # Macro Label (Positive)
│   └── negative_labels.json   # Macro Label (Negative)
├── micro_labels/
│   ├── positive_micro_labels.json
│   └── negative_micro_labels.json
├── traits/
│   ├── trait_definitions.json # 12개 Trait 정의
│   └── trait_theory_mapping.json
├── engine/
│   └── hybrid_rules.json      # 하이브리드 규칙
├── mappings/
├── schema/
├── test/
│   ├── test_cases_v1.json
│   ├── quiz_questions.json
│   ├── situation_cards.json
│   ├── hybrid_tests.json
│   └── negative_tests.json
├── test_results/
└── metadata/
    └── users_metadata.json     # 사용자 진단 결과
```

---

## 6. 데이터베이스

### 6.1 Tables

| Table | 설명 |
|-------|------|
| users | 사용자 계정 (SHA-256 + PBKDF2) |
| analysis_results | 분석 결과 저장 |

### 6.2 Phases

| Phase | 기능 | module |
|-------|------|-------|
| Phase 1 | 프로필 + 진단 결과 | metadata.py |
| Phase 2 | Trait Delta/Trend 추적 | metadata.py:calculate_trait_delta, calculate_trait_trend |
| Phase 3 | Cohort 분석 + Gap Analysis | metadata.py:analyze_cohort, analyze_gap |
| Phase 4 | 자동 인사이트 생성 | metadata.py:generate_insights, generate_cohort_insights |

---

## 7. 핵심 모듈

### 7.1 app.py (Flask Routes)

| Route | 기능 |
|-------|------|
| / | 메인 분석 페이지 |
| /login | 로그인 |
| /dashboard | 대시보드 |
| /bulk | 대규모 분석 |
| /api/analyze | 전체 분석 파이프라인 |
| /api/generate-prompt | 프롬프트 생성 |
| /api/auth/* | 인증 APIs |
| /api/dashboard/* | 대시보트 APIs |
| /api/metadata/* | 메타데이터 APIs |
| /api/test/* | 테스트 APIs |

### 7.2 src/nlp_pipeline.py (NLP 추출)

| Function | 기능 |
|----------|------|
| load_allowed_labels | 허용 label 로드 |
| build_llm_prompt | 프롬프트 생성 |
| validate_structure | 구조 검증 |
| create_gemini_client | Gemini API |
| create_openrouter_client | OpenRouter API |
| create_ollama_client | Ollama (로컬) |
| call_llm_with_retry | 재시도 로직 |
| apply_calibration | Confidence 보정 |
| filter_low_confidence | 저-confidence 필터링 |
| apply_sentence_weights | 문장 가중치 |
| detect_conflicts | 충돌 감지 |

### 7.3 src/leadership_engine.py (Trait 추론)

| Function | 기능 |
|----------|------|
| process | 메인 처리 (Micro Label → Trait) |
| _calculate_positive_trait | Positive Trait 계산 |
| _calculate_negative_trait | Negative Trait 계산 |
| _calculate_confidence | Confidence 계산 |
| _detect_risks | 리스크 감지 |
| _generate_hybrids | 하이브리드 생성 |

### 7.4 src/auth.py (인증/저장)

| Function | 기능 |
|----------|------|
| create_user | 회원가입 |
| verify_user | 로그인 검증 |
| save_analysis_result | 분석 결과 저장 |
| get_dashboard_stats | 대시보트 통계 |
| get_trait_distribution | Trait 분포 |
| get_daily_trend | 일별 추이 |

### 7.5 src/metadata.py (메타데이터)

| Function | 기능 |
|----------|------|
| save_analysis_metadata | 분석 Metadata 저장 |
| get_user_metadata | 사용자 Metadata 조회 |
| calculate_trait_delta | Trait 변화량 |
| calculate_trait_trend | Trait 추세 |
| analyze_cohort | 집단 분석 |
| analyze_gap | 갭 분석 |
| generate_insights | 인사이트 생성 |

---

## 8. Stage별 Debug Log 확인方法

### Frontend
1. 분석 실행 후 Debug Info 섹션이 표시됨
2. 각 Stage별로 입력/출력/상세 정보가 테이블로 표시됨

### Backend (app.py:420-539)
```python
debug_info.append({
    'step': 1,
    'name': '프롬프트 생성',
    'input': user_input[:100] + '...',
    'output': prompt[:500] + '...',
    'details': f'프롬프트 길이: {len(prompt)}자'
})
```

---

## 9. API Keys (.env)

| Key | 설명 |
|-----|------|
| GEMINI_API_KEY | Google Gemini API |
| OPENROUTER_API_KEY | OpenRouter API |
| SECRET_KEY | Flask 세션 키 |

---

## 10. 실행 방법

```bash
# Dependencies 설치
pip install -r requirements.txt

# Flask 서버 실행
python app.py

# http://localhost:5000 접속
```