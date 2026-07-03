# 리더십 Trait·Micro Label 비판적 검증 원장 (Validation Ledger) — 활성본

**최초 작성**: 2026-06-23 · **현재 갱신**: 2026-07-01
**전제(Principle)**: 우리가 만든 Trait과 Micro Label은 **옳다고 가정하지 않는다.** 기본 상태는 `unverified`이며, 논문 근거가 **(1) 구인 타당성**과 **(2) 우리 라벨 operationalization** 을 모두 뒷받침할 때만 상향한다. 지지 근거뿐 아니라 **반증·위험(counter-evidence)** 을 반드시 병기한다.

> 이 문서는 "근거를 모아 정당화"하는 문서가 아니라, **"우리 데이터가 틀렸을 가능성을 적극적으로 검사"** 하는 문서다.
> 2026-06-24 이전에 실행된 검증 조치(T08→T11 통합, T10 비활성화, T01/T06/T12 재매핑 등)는 `docs/archive/leadership_validation_ledger.md` §상단 참조.

**현재 규모**: 이론 12 · Trait 18(긍정 12 / 위험 6) · Micro Label 178(긍정 98 / 부정 80)
**근거 매핑 커버리지**: `research/evidence_mapping/label_evidence_map.json` = **긍정 31개 라벨만**(전체의 17%). 부정 80개는 **근거 0건**.

---

## 0. 전 항목 공통 한계

| # | 한계 | 의미 |
|---|------|------|
| L1 | **자체 데이터 경험적 검증 전무** | 178 라벨·18 Trait은 EFA/CFA·신뢰도(α)·평가자간 일치(κ)를 거친 적 없음 → 최고 등급은 `construct_supported`, `verified`는 없음 |
| L2 | **이론 매핑이 사후적(post-hoc)** | Trait를 먼저 만들고 이론을 붙임 → 확증편향. 논문이 "설명"할 수는 있어도 "검증"한 것 아님 |
| L3 | **라벨이 검증된 척도 문항에서 유래하지 않음** | 178 라벨은 자체 정의, MLQ/SLS 문항과 1:1 대응 미확인 |
| L4 | **텍스트 단일 출처 추론** | R05~R07은 360도 다면평가를 보여주나 우리는 단일 텍스트 추론 → 관점 편향 |
| **L5** | **인용 논문 원문 부재(2026-07-01 신규)** | 근거 매핑이 인용한 **P009·P010·P011·P012의 원문이 저장소에 없음** → page/section 대조 불가 = 해당 인용 자체가 검증 불가 |

---

## 1. 검증 상태 어휘

| 상태 | 의미 |
|------|------|
| 🔴 `unverified` | 직접근거 부족 또는 구인 미확립 / **근거 원문 부재로 대조 불가** |
| 🟠 `partially_supported` | 구인은 인정되나 판별타당도·라벨-이론 불일치 등 결함 존재 |
| 🟡 `construct_supported` | 학계가 구인 인정. 단 우리 라벨의 측정 타당성은 미검증 |
| ⛔ `contradicted` | 문헌과 충돌 |
| 🟢 `verified` | 구인 + 우리 라벨 모두 경험적 검증 — **현재 해당 없음** |

`trait_theory_mapping.json` 실측 분포: 🟡 construct_supported 12 · 🟠 partially 4 · 🔴 unverified 2 · 🟢 0

---

## 2. 긍정 Trait 검증 원장 (2026-07-01 실측)

| Trait | JSON 상태 | 근거 논문(원문 유무) | 반증·위험 |
|-------|-----------|----------------------|-----------|
| **T01** Strategic Decisive | 🟡 construct/medium | R02·P007(✅) + **P009 MacKenzie(❌부재)** | 거래적 근거의 핵심(M06-01,M10-01)이 P009 의존인데 원문 부재 → medium 근거 **하향 위험** |
| **T02** Collaborative | 🟡 construct/strong | R03·P005(✅) | SLS 경청/의견청취 라벨은 SLS에 '경청' 차원 없음 → empowerment로 **느슨 매핑**(교정 반영) |
| **T03** Innovative | 🟡 construct/strong | R02·P004(✅) | R08(Ravet-Brown)은 EL↔TL 판별타당도 경고 → 혁신 독립 trait 근거 약화 가능 |
| **T04** Crisis Manager | 🔴 unverified/medium | P010 arXiv(❌부재)·P006(✅ 간접) | 위기관리가 안정적 '성향'인지 논쟁적. **유일 직접근거 P010 원문 부재** |
| **T05** Analytical | 🔴 unverified/weak | P006(✅ 계량서지) | required 라벨 1개(M34-01) → 구인 취약. 데이터기반 의사결정은 검증된 '스타일' 아님 |
| **T06** Execution Driver | 🟡 construct/strong | R05·P009(❌부재) | 라벨은 순수 실행(보상 부여 라벨 없음) → 'contingent reward' 주장과 불일치. T04와 M10-01/M19-01 중복 |
| **T07** Coaching | 🟡 construct/strong | R03·P005·P012(❌부재) | 인재육성 M39-01 근거가 P012 원문 부재. IC 문항 매핑 미확인 |
| **T09** Visionary | 🟡 construct/strong | X01·R02·P010(❌부재) | 변혁적 II/IM 견고하나 M01-04 등 라벨-문항 대응 미확인 |
| **T11** Empathetic | 🟡 construct/strong | R03·R04(✅) | **반증: SLS 개발 시 empathy 항목은 안정적 요인 미형성·탈락**(원문 §Development). 공감 라벨의 SLS 척도 직접 지지 약함 |
| **T12** Balanced | 🟠 partially/medium | R05·R09(✅) | '균형/ambidextrous' 조작적 정의 모호, 측정 곤란 |
| **T13** Ethical Courageous | 🟡 construct/strong | **P011 arXiv(❌부재)·P004(✅)** | ⚠ **주의: T13의 근거 매핑(M28-01,M30-01,M33-01) 전부가 P011 의존인데 원문 부재.** strong 등급은 원문 확보 전까지 **과대 표기** — 하향 검토 필요 |
| **T14** Learning Agile | 🟠 partially/medium | R09·P004(✅) | 'digital' 주장 근거는 계량서지(R09)뿐, required 2개로 취약 |

---

## 3. 위험(Negative) Trait 검증 원장

| Trait | JSON 상태 | 근거 | 반증·위험 |
|-------|-----------|------|-----------|
| **T101** Avoidant | 🟡 construct/strong | MLQ 자유방임(R01/R02) | 우리 회피 라벨↔MLQ-LF 문항 대응 미확인 |
| **T102** Authoritarian | 🟠 partially/weak | R05 위계지향(간접) | ref data 직접 1차근거 없음 |
| **T103** Integrity Violation | 🟠 partially/medium | authenticity 역구인(R03) | '위반' 행동 경계 모호 |
| **T104** Narcissistic | 🟡 construct/strong | 다크 트라이어드 | **원전(Paulhus&Williams 2002 등) ref data 외부** |
| **T105** Manipulative | 🟡 construct/strong | 마키아벨리즘 | 원전 외부, 우리 라벨 미검증 |
| **T106** Volatile | 🟡 construct/strong | HDS 탈선요인 | 원전(Hogan&Hogan 2001) 외부 |

> **부정 Micro Label 80개 전체: 근거 매핑 0건.** 위험 Trait의 required 부정 라벨(N08-01, N15-03, N30-01 등)은 논문 대조가 전무하여 **전부 `unverified`** 로 간주해야 한다. 위 Trait의 `construct_supported`는 상위 구인(다크 트라이어드 등)에 대한 것이지, **우리 부정 라벨의 타당성 근거가 아니다.**

---

## 4. 2026-07-01 감사에서 새로 확인된 사항

| # | 발견 | 조치/상태 |
|---|------|-----------|
| A1 | **P009·P010·P011·P012 원문이 저장소에 없음** — 이들에 의존하는 라벨(M01-01, M06-01, M10-01, M05-02, M19-01, M20-01, M28-01, M30-01, M33-01, M39-01)의 인용 대조 불가 | 해당 라벨·연관 Trait(T01·T04·T07·T13) 근거를 **unverified 수준으로 취급**. 원문 확보 전 상향 금지 |
| A2 | **SLS 'Interpersonal Acceptance' 차원명 오류** — 최종 8차원(standing back/forgiveness/courage/empowerment/accountability/authenticity/humility/stewardship)에 없음 | `label_evidence_map.json`의 M11-01/M12-01/M15-01/M15-03 차원명·note **교정 완료**(2026-07-01) |
| A3 | **SLS empathy 항목이 안정적 요인을 형성하지 못하고 탈락**(원문 확인) | 공감 라벨(M12-01, T11)의 척도 직접 지지 **약함**으로 명시 |
| A4 | **T13(윤리)의 근거가 전부 부재 논문 P011에 의존** | 현재 `construct_supported/strong`은 과대 → 원문 확보 또는 대체근거 전까지 **하향 검토 대상** |
| A5 | **RESEARCH_REPORT §5.2·§11.1이 현재 trait_definitions.json과 불일치** (T06·T07·T11·T12 required 상이; "T01↔T09가 M01-01 공유"는 현 JSON상 사실 아님) | 보고서를 구 버전 기준으로 명시. 단일 진실원천은 JSON |
| A6 | **근거 커버리지 31/178(17%), 부정 80개 0건** | 미커버 라벨 전부 `unverified` 기본값 유지 |

---

## 4b. 2026-07-01 (2차) — `papers/` 컬렉션(227편) 반영

새 논문 컬렉션(`papers/`: 초록 227 + PDF 75)을 유입하여 갭을 부분 해소함. **모든 신규 근거는 초록(abstract) 수준**이며 전문 대조는 미실시 → `source_level=abstract_only`.

| 개선 | 대상 | 신규 근거(등록 ID) | 효과 |
|------|------|--------------------|------|
| **거래적 공백 해소** | T01·T06, M06-01·M10-01 | R10 Bono&Judge(2004) 메타·R14 Pillai(1999) SEM·R15 Bass(1999) | 부재 논문 P009 의존 → 실제 메타분석/SEM 근거로 대체(초록) |
| **윤리 공백 해소** | T13, M28-01·M30-01·M33-01 | R13 Schaubroeck(2013)·R11 Walumbwa ALQ | 부재 논문 P011 의존 → 확립된 윤리/진정성 구인으로 대체(초록) |
| **진정성 이론 실근거 확보** | Authentic 이론·M32-01·M41-01(신규) | R11 Walumbwa 2008 ALQ(5개국·CFA 4차원) | 종전 'NEW·근거약함' → 검증된 척도 확보. self-awareness/transparency 라벨 지지 |
| **서번트 보강** | T02·T11 | R16 de Waal(2012) 성과 실증 | 서번트→성과 경로 추가 근거 |
| **참여/임파워링 신규** | M43-01(신규) | R17 Kang(2023) 실증 | 임파워링→혁신행동 |

### 새로 확인된 반증·한계 (2026-07-01)
| # | 반증/한계 | 의미 |
|---|-----------|------|
| **C1** | **R12 Min&Jung(2022) 진정성 리더십 비판적 리뷰(184편):** "개념이 이론적으로 불명확하고 측정이 현실을 정확히 반영 못함" | 진정성 기반 라벨(M32-01·M41-01)·T13/T103의 **측정 타당성에 미해결 위험**. construct는 인정되나 판별/측정은 논쟁적 → 상향 시 주의 |
| **C2** | 신규 근거 전부 **abstract 수준** | 페이지·문항 대조 불가. R02/R03가 보여준 척도검증 표준에 미달 → `construct_supported` 유지, `verified` 아님 |
| **C3** | **부정/독성 리더십 직접 근거 여전히 0** | papers/ 227편에도 toxic/abusive/destructive/dark-triad 논문 없음. 위험 Trait(T102–T106)·부정 라벨 80개는 계속 `unverified` |
| **C4** | 이론 논문(거래적·윤리·진정성 등)은 **전부 meta(초록)뿐, PDF 아님** | 75개 PDF는 주로 AI/디지털군. 핵심 이론의 full-text 확보가 다음 과제 |

> 조치: `data/traits/trait_theory_mapping.json` paper_registry에 R10–R17 등록, 해당 trait citations·`counter_evidence`·`validation_gap` 갱신. `research/evidence_mapping/label_evidence_map.json`에 보강·신규 라벨 반영(총 34 라벨). **validation_status 상향은 없음**(초록 수준·측정 미검증이므로 보수적 유지).

---

## 4c. 2026-07-02 (3차) — 컬렉션 226편 trait/label 연결

`papers/` 226편(리더십 초록 195 + 전문 31)을 내용 기반으로 이론 분류하여 trait/label에 연결. 산출물: `research/evidence_mapping/paper_corpus.json`(258편 매핑), `label_corpus_candidates.json`(라벨 후보), `papers/extracted/`(PDF 전문).

### 커버리지 변화
| 지표 | 이전 | 현재(07-02) |
|------|------|-------------|
| Trait 근거(corpus, 이론연계) | 17편 매핑 | **137편 매핑, 18/18 trait**에 통합 (긍정 trait당 23~64편) |
| 라벨 **검증완료**(hand) | 34/178 (19%) | **36/178 (20%)** — R18 전문 3건 추가 |
| 라벨 **후보 포함**(keyword) | — | **98/178 (55%)** ※후보는 unverified |

### 정직한 한계 (상향 아님)
| # | 한계 |
|---|------|
| D1 | **trait corpus_evidence는 '이론 연계'일 뿐** 우리 라벨 operationalization 검증이 아님. 대부분 초록 수준 → validation_status **상향 없음** |
| D2 | **라벨 후보 98/178은 키워드 매칭**이라 오탐 다수(특히 부정 라벨: 실제 다크리더십 논문 부재로 일반 논문에 잘못 매칭). `label_corpus_candidates.json`에 격리, 검증완료와 분리 |
| D3 | **위험 trait 여전히 공백**: T106=0, T104·T105=1, T102=1편. 다크 트라이어드/HDS/권위주의 원전 미확보 |
| D4 | **전문(full-text) 리더십은 실질 6~8편뿐** (331 Cortellazzo 디지털, 199, 235, 342, 230, 167 등). 75 PDF 대다수는 AI/기술로 metadata와 별개 집합 |
| D5 | T12 Balanced는 corpus 5편으로 최약 — 균형/양손잡이 구인 근거 여전히 취약 |

> 조치: R18(Cortellazzo 2019 전문) 등재, T03/T05/T14 citations·M21-01/M35-01/M37-01 반영. corpus는 trait 근거로 통합하되 **검증 상태는 보수적 유지**.

### 4c-1. 후보 정독 승격 (2026-07-03)
후보(candidate)를 **초록/전문 정독으로 검증**해 정식 등재. **오탐은 기각**(예: M03-03↔계량경제 p27, M27-02↔환자안전 p304, M25-01↔진정성논문). 승격:
| 라벨 | 근거 | 수준 |
|------|------|------|
| M16-01 이해관계자 관계 구축 | R20 Hartnell&Lemoine(2025) 서번트 '다수 이해관계자' | 초록 |
| M24-02 권한 위임 | R17 임파워링 + 최은수(2006) '권한위임 리더십' | 초록 |
| M25-01 글로벌/다문화 | **R21 Nosratabadi 문화지능** | 전문(PAGE) |
| M15-05 신뢰 형성 | R14 Pillai(신뢰 매개) + R22 integrity→trust | 초록 |
| M47-01 공유 리더십 | **R19 주영경·김명소(2022) 공유리더십 척도(내용타당도)** | 전문(PAGE) |
| M43-01 참여적 의사결정(보강) | R19 수평적 상호작용 요인 | 전문(PAGE) |

**결과: 라벨 검증완료 36→41/178 (긍정 41.8%).** registry R19~R22 추가(총 27). 부정 라벨은 여전히 0(승격 대상 없음).

---

## 5. 검증 우선순위 (다음 작업 가이드)

| 순위 | 대상 | 필요한 것 |
|------|------|-----------|
| 1 | P009·P011 원문 확보 | MacKenzie(2001), 윤리적 리더십 1차 논문 — 없으면 T01(거래적)·T13(윤리) 근거 붕괴 |
| 2 | 부정 라벨 80개 근거 착수 | 다크 트라이어드/자유방임/권위주의 원전 → N-라벨 매핑 시작 |
| 3 | T04·T05 구인 보강 | 위기관리·데이터기반 의사결정 실증 원전 |
| 4 | 전 Micro Label 측정 타당성 | 검증된 척도 문항(MLQ 45, SLS 30)과 1:1 매핑표 |
| 5 | 우리 데이터 자체 검증 | 라벨링 데이터로 α·κ·CFA 수행 (논문 아님) |

---

## 6. 갱신 규칙

논문 1편 검토 시마다: (1) 지지뿐 아니라 **반증·약화**도 기록 → (2) `trait_theory_mapping.json`의 `validation_status` 갱신(상향·하향 모두 가능) → (3) 본 원장 표 갱신 → (4) 변경 이력 기록.

> 상태는 **하향도 가능**하다. 새 근거가 기존 가정을 반증하면 `contradicted`로 내린다. 이것이 이 프로젝트의 목적이다.
