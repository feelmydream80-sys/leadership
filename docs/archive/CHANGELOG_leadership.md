# 리더십 체계 변경 이력 (CHANGELOG)

> 리더십 **종류(이론)·Trait·Micro Label·근거 논문**의 모든 변경을 기록한다.
> 논문을 추가로 확보·정리할 때마다 본 파일에 **항목을 추가**하고, 영향을 받은 JSON을 갱신한 뒤
> `python scripts/build_leadership_catalog.py`로 카탈로그를 재생성한다.
>
> 관련 산출물: 근거 보고서 `docs/leadership_evidence_validation_report.md` · 카탈로그 `docs/leadership_catalog.md`

## 형식 규칙 (Semantic Versioning)

- **MAJOR**: Trait 추가/삭제, 이론 체계 개편, required Label 구조 변경
- **MINOR**: 근거 논문 추가, 이론 매핑 재정렬, 인용/근거강도 부여
- **PATCH**: 오탈자, 설명 보강, 문서 동기화

각 항목은 아래 5요소를 포함한다: **버전 · 일자 · 추가/근거 논문 · 변경 내용 · 영향 파일**.

---

## 현재 버전: 이론매핑 v4.0 / Trait 정의 v2.0 / Micro Label v2.0

---

## 변경 이력

### [v5.0] — 2026-06-24 — 검증 결과를 데이터에 실제 반영: Trait 삭제·수정 (MAJOR)

**계기**: 검증을 "상태 표기"에 그치지 말고, 근거에 맞지 않으면 실제로 삭제/수정하라는 지시. 9편 논문의 검증된 구인(MLQ 9요인, SLS 8차원, 경쟁가치 4지향, EL, EI)과 우리 Trait을 1:1 대조 후 실행.

#### 삭제 (DELETE)

| Trait | 사유 | 처리 |
|-------|------|------|
| **T08** Emotional Intelligence | T11과 required 2/3(M12-01,M14-01) 동일 → 판별타당도 실패. "EI"는 자기인식/자기조절 포함 개념이나 라벨은 공감-only → 명칭 과대표현 | **T11로 흡수**(서번트 R03 기반이 더 견고). optional M12-02·M12-03 T11로 이전 |
| **T10** Strategic Execution | required {M01-01,M10-01,M10-02} ⊂ T01∪T06∪T09 → 독립 구인 아님 | 삭제. 증강효과는 hybrid로 표현(엔진 hybrid_eligible 지원) |

#### 수정 (FIX)

| Trait | Before | After | 근거 |
|-------|--------|-------|------|
| **T01** Strategic Decisive | required=[M01-01(비전),M06-01,M10-01] | required=[M06-01,M19-01] (결단 구인 정제, 비전→T09/실행→T06 분리) | 구인 혼재 제거 |
| **T06** Execution | 이론=Contingent Reward(라벨 불일치) | 이론=**경쟁가치 과업지향** | R05 |
| **T12** Balanced | 이론=Ambidextrous(연결 약함) | 이론=**경쟁가치 행동적 복잡성** | R05 |
| **T102** Authoritarian | unverified(ref data 근거 없음) | partially(**위계지향** 근거 확보, 상향) | R05 |

#### 미삭제·보류

- **Micro Label 삭제 0건**: 125개 라벨은 학습데이터(dataset/)가 직접 참조 → 삭제 시 학습 예제 고아화. 라벨은 trait와 독립 유지(trait 삭제해도 라벨 보존). 라벨 수정/삭제는 데이터셋 영향 분석 후 별도 진행.
- **ADD 보류(Contingent Reward 양성 Trait)**: 진짜 공백이나 지지 라벨 1개(M08-02 공정한 성과 인정)뿐 → 1-라벨 Trait는 방금 삭제한 약점(T05類) 반복. 보상/인정 라벨 1개 이상 신설 후 추가 예정.

#### 검증(엔진 무결성)
- `LeadershipEngine` 18 trait 로드 OK, 양성/음성 추론 OK, 부정 trait T101~106 무손상.
- 설정 파일(auto_mapping_rules·context_rules·negative_mapping_rules·keyword_weights·resolution_rules) T08→T11, T10→T06 리매핑 완료.

#### 영향 파일
- `data/traits/trait_definitions.json` (20→18 trait, v2.0→v2.1) — 백업: `backups/trait_definitions_pre-validation_20260624.json`
- `data/traits/trait_theory_mapping.json` (v4.1→v5.0 상당, 18 매핑) + 중복 사본
- 엔진 설정 6종, 카탈로그 재생성, 검증원장·CHANGELOG 갱신

#### 남은 OPEN (검증 우선순위 = 다음 논문 가이드)
- OPEN-1 해소: T08/T11 판별 → T08 삭제로 해결. T01/T06 중복도 완화(T10 삭제)
- 잔존: T04·T05·T12 미검증/부분 → 데이터기반 의사결정·위기관리·복잡성 실증 논문 필요
- T104~106 원전(ref data 외부) 확보, 전 Micro Label의 검증척도 문항 1:1 대조(§4)

---

### [v4.1] — 2026-06-23 — 비판적 검증 체계 전환 (MINOR)

**계기**: 검증 태도 전환 — Trait/Micro Label을 "옳다"고 전제하지 않고, 기본값 `unverified`에서 논문으로 옳은지를 증명/반증하며 진행. (지지 근거만 모으던 v4.0의 확증 편향 교정)

#### 변경 내용

| # | 항목 | 내용 |
|---|------|------|
| 1 | `validation_status` 필드 신설 | 전 Trait에 검증 상태 부여(unverified/partially_supported/construct_supported/contradicted). **fully-verified는 0개** |
| 2 | `validation_gap` 필드 신설 | 각 Trait의 반증·위험·미해결 결함 명시 |
| 3 | `validation_policy`·`validation_summary` 블록 | 전제(기본 미검증)와 경험적 검증 부재(L1) 명시 |
| 4 | 정직한 1차 판정 | 🟡 구인지지 9 · 🟠 부분지지 7 · 🔴 미검증 4 (T04·T05·T12·T102) |
| 5 | 신규 문서 | `docs/leadership_validation_ledger.md` — 항목별 지지/반증/검증요건 원장 |
| 6 | 카탈로그 갱신 | 검증상태 컬럼·전제 경고 추가 후 재생성 |

#### 핵심 판정(반증 위주)
- T01·T06: 주장 이론과 라벨 구성 **불일치**(비전/실행 혼재, 보상 라벨 부재)
- T08↔T11, T01↔T06↔T10: **판별타당도 실패**(required 라벨 대거 중복)
- T05: required 라벨 **1개**로 구인 취약
- 전 항목: 우리 데이터에 대한 경험적 검증(α/κ/CFA) **전무** → 최고 등급 construct_supported

#### 영향 파일
- `data/traits/trait_theory_mapping.json` (validation_* 필드 추가, 중복 사본 동기화)
- `scripts/build_leadership_catalog.py`, `docs/leadership_catalog.md`(재생성)
- 신규: `docs/leadership_validation_ledger.md`

---

### [v4.0] — 2026-06-23 — 근거 논문 9편 1차 정리 (MINOR)

**계기**: `ref data/` 리더십 논문 9편 입수 → 근거·검증 보고서 작성(`leadership_evidence_validation_report.md`) → 후속 개선.

#### 추가된 근거 논문 (9편 + 외부 원전 5편)

| ID | 논문 | 연결 Trait |
|----|------|-----------|
| R01 | Dumdum, Lowe & Avolio (2002) 변혁·거래 메타분석 | T01, T03, T06, T09, T10, T101 |
| R02 | Batista-Foguet et al. (2021) MLQ 측정검증 | T01, T05, T06, T09, T101 |
| R03 | van Dierendonck & Nuijten (2010) 서번트 척도 | T02, T07, T08, T11, T13, T103 |
| R04 | Indarta et al. (2024) 서번트 문헌고찰 | T02, T11 |
| R05 | 최루디아 (2020) 경쟁가치 다면평가 | T12, T102 |
| R06 | Das & Rajini (2024) 360도 개발 | T07 |
| R07 | Emam et al. (2024) 간호 360도 실험 | T07, T14 |
| R08 | Soomro et al. (2024) 기업가적 리더십 리뷰 | T03 |
| R09 | Azhar & Ayobami (2026) 역량 계량서지 | T04, T05, T08, T12, T13, T14 |
| X01~X05 | Bass(1985), Paulhus&Williams(2002), Rosenthal&Pittinsky(2006), Hogan&Hogan(2001), Goleman(1995) — 외부 원전 | T09, T104, T105, T106, T08 |

#### 변경 내용 (Before → After)

| # | 항목 | Before (v3.0) | After (v4.0) | 근거 |
|---|------|---------------|--------------|------|
| 1 | T01 이론 | Ethical / "도덕성+구성원 보호" | **Full-Range(Transactional/Active)** / 목표 기반 결단 | R01,R02 |
| 2 | T03 이론 | Ethical / "신뢰 형성" | **Transformational(지적자극)** | R01,R08 |
| 3 | T04 이론 | Servant / "공감 중심" | **Adaptive** / 능동적 예외관리 | R09 |
| 4 | T05 이론 | Servant / "안전감→혁신" | **Data-Driven** | R09,R02 |
| 5 | T06 이론 | Transformational / "개별적 배려" | **Transactional(상황적 보상)** | R01,R02 |
| 6 | T07 이론 | Servant / "이타성" | **Transformational(개별적 배려)** | R06,R07 |
| 7 | T08 이론 | Transactional / "성과 중심 실행" | **Emotional Intelligence** | R09,R03,X05 |
| 8 | T09 이론 | Transactional / "결과 책임" | **Transformational(II·IM)** | X01,R01,R02 |
| 9 | **T10 매핑** | **누락** | **신규 추가**: Full-Range 증강효과 | R01 |
| 10 | **T11 매핑** | **누락** | **신규 추가**: Servant(humility 등) | R03,R04 |
| 11 | T101 이론 | Passive / "책임 회피" | **Laissez-Faire/Passive** + MLQ 2차요인 근거 | R02,R01 |
| 12 | T102 이론 | Authoritarian (근거 없음) | Authoritarian + 경쟁가치 위계지향 *(weak, 보강필요)* | R05 |
| 13 | T103 이론 | Authentic / "언행 불일치" | **Authentic(역) + Ethical** | R03 |
| 14 | 스키마 | evidence 1줄 | **citations·evidence_strength·paper_registry 필드 신설** | — |

#### 신규 산출물
- `docs/leadership_evidence_validation_report.md` — 근거·개선·검증 보고서
- `docs/leadership_catalog.md` — 자동 생성 통합 카탈로그
- `scripts/build_leadership_catalog.py` — 카탈로그 생성기
- `docs/CHANGELOG_leadership.md` — 본 이력 문서

#### 영향 파일
- `data/traits/trait_theory_mapping.json` (v3.0 → v4.0)
- `data/leadership_data_updated/trait_theory_mapping.json` (동기화)
- 백업: `data/traits/backups/trait_theory_mapping_v3_20260623.json`

#### 미반영(OPEN) — 후속 과제로 추적

| ID | 과제 | 우선순위 | 사유/제안 |
|----|------|----------|-----------|
| OPEN-1 | **T08·T11 판별타당도** — 두 Trait가 required 중 M12-01·M14-01 공유 → 변별 곤란 | 높음 | required Label 재배정(한쪽 optional 강등) 또는 통합. 엔진/학습데이터 영향 → 별도 검증 후 적용 |
| OPEN-2 | T05·T102 근거강도 **weak** → 1차 근거 논문 확보 | 중 | 데이터기반 의사결정·권위주의 실증 논문 추가 |
| OPEN-3 | T102·T104·T105·T106 **부정 Trait 1차 원전** ref data 미포함 | 중 | Paulhus&Williams(2002), Hogan&Hogan(2001) 원문 확보 |
| OPEN-4 | `leadership_trait_system.md` §3 Trait 표가 JSON과 불일치(stale) | 낮음 | 카탈로그로 대체, 해당 표 deprecated 처리 |

---

### [v3.0] — 2026-04-23 — (기존) Trait/이론 매핑 체계 (이전 기록)

- T13(윤리적 용기형), T14(학습 민첩형), 부정 Trait T104~T106 추가, 이론 매핑 100% 달성.
- 상세: `docs/leadership_trait_system.md` 참조. (v4.0 이전 이력은 해당 문서에 산재)

---

## 다음 논문 추가 시 작성 템플릿 (복사해서 사용)

```markdown
### [vX.Y] — YYYY-MM-DD — <요약> (MAJOR/MINOR/PATCH)

**계기**: <왜 추가하는가>

#### 추가된 근거 논문
| ID | 논문 | 연결 Trait |
|----|------|-----------|
| R## | <저자(연도) 제목> | <T..> |

#### 변경 내용 (Before → After)
| # | 항목 | Before | After | 근거 |
|---|------|--------|-------|------|
| 1 | <T## 이론/Label/...> | <기존> | <변경> | R## |

#### 영향 파일
- data/traits/trait_theory_mapping.json (paper_registry에 R## 추가)
- (필요 시) data/traits/trait_definitions.json
- (필요 시) data/micro_labels/*.json

#### 절차 체크리스트
- [ ] paper_registry에 논문 ID 등록 (in_ref_data 표기)
- [ ] 해당 Trait의 citations / evidence_strength 갱신
- [ ] `python scripts/build_leadership_catalog.py` 재실행
- [ ] OPEN 과제 해소 여부 점검
```
