# AGENTS.md - Leadership Label Vector DB Project

> **Project Compass**  
> 이 문서는 프로젝트의 중앙 나침반입니다. 어떤 파일이 어디에 있고 무엇을 하는지, 그리고 현재 상태는 어떤지 한눈에 파악할 수 있습니다.  
> **버전:** v2.3 | **라벨:** 178개 | **샘플:** 12,460개 | **마지막 업데이트:** 2026-07-01

---

## 현재 상태

| 항목 | 수치 | 상태 |
|------|------|------|
| 총 라벨 | 178개 (Positive 98 + Negative 80) | ✅ 완료 |
| 학습 샘플 | 12,460개 (라벨당 70개) | ✅ 완료 |
| Vector DB | 178 vectors (KoE5, 768-dim) | ✅ 완료 |
| 중복 텍스트 | 0개 | ✅ 완료 |
| 배치 파일 | 18개 | ✅ 완료 |
| 통합 파일 | `training_data_all_labels.json` | ✅ 완료 |

---

## 문서 지도

어떤 정보를 찾고 계신가요? 아래 표를 참조하세요.

| 찾는 정보 | 문서 위치 | 설명 |
|-----------|-----------|------|
| **파일 구조, 라벨 계층도, 배치 매핑** | [FILE_STRUCTURE.md](FILE_STRUCTURE.md) | 전체 디렉토리 트리, Macro→Micro 관계도, 18개 배치 ↔ 라벨 ID 매핑표, JSON 스키마 |
| **파이프라인 상세 명세** | [docs/core.md](docs/core.md) | Vector DB → LLM → Trait 추론 흐름, 컴포넌트 명세, 임계값 설정, API 응답 포맷 |
| **시스템 운영 방법** | [docs/HANDOVER.md](docs/HANDOVER.md) | 웹 서버 실행, 데이터 수정 워크플로우, API 엔드포인트, 해결된 이슈, 남은 과제 |
| **Vector DB + LLM 설계 계획** | [docs/vector_db_vs_llm_plan.md](docs/vector_db_vs_llm_plan.md) | 아키텍처 비교, 실패 사례 분석(T04-B, T105-A), 개발 결과, 성능 지표 |
| **웹 수정 시스템 계획** | [docs/WEB_EDIT_PLAN.md](docs/WEB_EDIT_PLAN.md) | 웹 기반 라벨/트레이트 편집, 통합 파일 생성, 백업 시스템 |
| **라벨 감사 보고서** | [docs/label_audit_report.md](docs/label_audit_report.md) | 178개 라벨의 정의, when/not_when, 예시 문장 |
| **Trait/라벨 근거·비판적 검증** | [docs/leadership_validation_ledger.md](docs/leadership_validation_ledger.md) | 논문 근거·반증·검증상태 원장(활성). 근거 커버리지·부재 논문·미검증 항목 |
| **종합 연구 보고서** | [RESEARCH_REPORT_2026-06-26.md](RESEARCH_REPORT_2026-06-26.md) | 12이론·20Trait·178라벨 조사 이력(2026-06-26 기준, 정리 후 동기화 주의 포함) |
| **구 문서 (아카이브)** | [docs/archive/](docs/archive/) | RAG_PLAN.md, architecture.md, leadership_catalog.md 등 8개 |
| **연구 참고자료** | [research/](research/) | 학술 논문(papers/), 서베이(surveys/), 증거 매핑(evidence_mapping/) |
| **논문 컬렉션 인덱스** | [papers/INDEX.md](papers/INDEX.md) | 신규 227편(초록) + 75 PDF 이론별 분류. 근거 채택은 evidence_mapping에서 확정 |
| **PDF 전문 추출본(영구)** | [papers/extracted/](papers/extracted/) | PDF→텍스트 1회 추출(PAGE 마커). 근거 검색은 PDF 대신 여기 참조. `manifest.json`·README 참조. 재생성: `python scripts/extract_pdfs.py` |
| **논문↔trait 코퍼스 매핑** | [research/evidence_mapping/paper_corpus.json](research/evidence_mapping/paper_corpus.json) | 258편 내용기반 이론→trait 매핑(137편 연결). trait별 근거 논문 목록 |
| **라벨 근거 후보(미검증)** | [research/evidence_mapping/label_corpus_candidates.json](research/evidence_mapping/label_corpus_candidates.json) | 라벨↔논문 키워드 후보. **검증완료(label_evidence_map)와 분리, unverified** |

---

## 데이터 지도

프로젝트의 핵심 데이터 파일과 그 역할입니다.

### 라벨 정의 (수정 시 주의)

| 파일 | 위치 | 역할 | 의존성 |
|------|------|------|--------|
| `positive_micro_labels_enhanced.json` | `dataset/ori/` | 98개 긍정 라벨 정의 (벡터DB 유일 소스) | `build_vector_db.py`가 직접 읽음 |
| `negative_micro_labels_enhanced.json` | `dataset/ori/` | 80개 부정 라벨 정의 (벡터DB 유일 소스) | `build_vector_db.py`가 직접 읽음 |
| `positive_labels.json` | `data/labels/` | 48개 긍정 매크로 카테고리 | 매크로 분류용 |
| `negative_labels.json` | `data/labels/` | 32개 부정 매크로 카테고리 | 매크로 분류용 |

### 학습 데이터

| 파일 | 위치 | 역할 | 생성 방법 |
|------|------|------|-----------|
| `batch1~20.json` | `dataset/ori/` | 18개 배치 파일 (12,460개 샘플) | AI 생성 후 품질 검증 |
| `training_data_all_labels.json` | `dataset/ori/` | 18개 배치 통합 마스터 파일 | `batch*.json` 단순 병합 |

### Vector DB 산출물

| 파일 | 위치 | 역할 | 재생성 방법 |
|------|------|------|-------------|
| `label_vectors.faiss` | `data/vectors/` | FAISS 인덱스 (178 vectors) | `python build_vector_db.py` |
| `metadata.json` | `data/vectors/` | 라벨 ID/텍스트 메타데이터 | `python build_vector_db.py` |
| `test_results.json` | `data/vectors/` | T04-B, T105-A 테스트 결과 | `python build_vector_db.py` |

### 핵심 스크립트

| 파일 | 위치 | 역할 |
|------|------|------|
| `app.py` | 루트 | Flask 웹 서버 (분석 API + 라벨/트레이트 수정 UI) |
| `build_vector_db.py` | 루트 | KoE5 임베딩 → FAISS 인덱스 생성 (178개 라벨 대상) |

---

## 품질 기준

모든 배치 데이터는 다음 기준을 충족해야 합니다.

- **문장 길이:** 20-120자
- **중복:** 0개 (모든 텍스트 고유)
- **라벨당 샘플:** 정확히 70개 (clean 50 + hard_negative 20)
- **스타일 분포:** 4가지 균등 (`direct_speech`, `indirect_report`, `scene_description`, `euphemism`)
- **플레이스홀더:** 금지 (`~`, `[content]`, `{content}`)
- **Hard Negative:** 표면적으로 유사하나 `not_when` 조건을 실제로 위반하는 문장

---

## 빠른 시작

### 1. 웹 서버 실행
```bash
cd C:\dev\leadership
python app.py
# http://localhost:5000
```

### 2. Vector DB 재구축
```bash
python build_vector_db.py
```

### 3. 배치 데이터 검증
```bash
python -c "import json; d=json.load(open('dataset/ori/training_data_all_labels.json')); print(f'Total: {len(d)}, Labels: {len(set(x[\"label_id\"] for x in d))}')"
```

### 4. 라벨 수정 → AI 검토
```
1. http://localhost:5000/edit/labels 접속
2. 라벨 수정 후 저장 (자동 백업)
3. [AI 검토용 통합] 버튼 클릭
4. AI에게 "temp/integrated_data.json 읽고 검토해줘" 요청
```
> 참고: `temp/integrated_data.json`은 `/api/edit/integrate` 호출 시 생성되는 임시 파일입니다.

---

## 버전 역사

### v2.3 (2026-07-01) — Current
- `papers/` 컬렉션 유입(초록 227 + PDF 75) → `papers/INDEX.md` 이론별 분류 생성
- 갭 근거 확보(초록): 거래적(R10 Bono&Judge·R14 Pillai·R15 Bass)·윤리(R13 Schaubroeck)·진정성(R11 Walumbwa ALQ) → 부재 논문 P009/P011 의존 해소
- 반증 확보: R12 Min&Jung(2022) 진정성 리더십 비판적 리뷰
- `trait_theory_mapping.json` registry R10–R17 등록, `label_evidence_map.json` 34라벨(신규 M32-01·M41-01·M43-01)
- 검증 원장 §4b 반영. 부정/독성 리더십 근거는 여전히 공백(과제)

### v2.2 (2026-06-30)
- 폴더 구조 정리 완료 (Step 1-4)
- `temp/` 구 라벨 시스템 파일 14개 삭제
- `temp/reftext/` → `research/papers/` 이동 (9개 논문)
- `dataset/real_world/` → `dataset/test_real_world/` 이동
- `ref data/` → `research/surveys/` + `research/evidence_mapping/` 분할 이동
- `docs/archive/` 생성, 구 문서 8개 이동
- `scripts/` 불필요 3개 → `docs/archive/scripts/` 이동
- `data/vectors/` 테스트 출력물 3개 삭제
- `backup_20260630/` 삭제
- AGENTS.md v2.2, FILE_STRUCTURE.md 갱신
- `research/` 폴더 신설 (papers/, surveys/, evidence_mapping/)

### v2.1 (2026-05-18)
- 178개 라벨 완성 (98 긍정 + 80 부정)
- 12,460개 고품질 학습 샘플 생성
- Vector DB 178 vectors로 재구축
- 18개 배치 파일 표준화, 중복 제거
- FILE_STRUCTURE.md 신규 작성
- AGENTS.md 나침반 역할로 개편

### v2.0 (2026-04-30)
- 54개 신규 마이크로 라벨 추가 (31 긍정 + 23 부정)
- 웹 기반 라벨/트레이트 수정 시스템 구축
- 개별 마이크로 라벨 JSON 파일 생성

### v1.0
- 98개 긍정 + 27개 부정 라벨
- 초기 Vector DB 구축

---

## 문제 해결

| 증상 | 원인 | 해결책 | 참고 문서 |
|------|------|--------|-----------|
| Vector DB 검색 실패 | 인덱스 손상/불일치 | `python build_vector_db.py` 재실행 | [docs/core.md](docs/core.md) #8 |
| 라벨 스키마 오류 | enhanced JSON 로드 실패 | `dataset/ori/*_enhanced.json` 경로 확인 | [FILE_STRUCTURE.md](FILE_STRUCTURE.md) |
| LLM JSON 파싱 오류 | 코드블록 포함 출력 | 프롬프트에 "순수 JSON만" 강화 | [docs/core.md](docs/core.md) #8 |
| 웹 수정 저장 실패 | 개별 파일 권한 | 백업 폴더 `data/*/backups/` 확인 | [docs/HANDOVER.md](docs/HANDOVER.md) #4 |

---

## 중요 규칙

1. **Vector DB 소스:** 반드시 `dataset/ori/*_enhanced.json`만 사용. `data/micro_labels/`는 참조하지 않음.
2. **배치 수정:** 개별 `batch*.json` 수정 후 반드시 `training_data_all_labels.json`을 재생성할 것.
3. **문서 업데이트:** 파일 구조/라벨 변경 시 `FILE_STRUCTURE.md`와 `AGENTS.md`를 함께 갱신할 것.
4. **백업:** 라벨 수정 전 자동 백업이 생성되지만, 대규모 변경 전 수동 백업 권장.

---

> **이 문서를 처음 읽는다면:** [FILE_STRUCTURE.md](FILE_STRUCTURE.md) → [docs/core.md](docs/core.md) 순서로 읽는 것을 권장합니다.
