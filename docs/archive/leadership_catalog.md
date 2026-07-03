# 리더십 통합 카탈로그 (Leadership Catalog)

> **자동 생성 문서** — `scripts/build_leadership_catalog.py`로 생성. 직접 수정 금지.
> JSON 원천을 갱신한 뒤 스크립트를 재실행하세요. 변경 이력은 `docs/CHANGELOG_leadership.md` 참조.

- 생성일: 2026-06-24
- Trait 정의 버전: v2.1 / 이론매핑 버전: v4.2
- Trait: 18개 (긍정 12 / 위험 6)
- Micro Label: 긍정 67 + 부정 58 = 125개
- 근거 논문: ref data 9편 + 외부 원전 5편
- **검증 상태(전제: 미검증)**: 구인지지 12 · 부분지지 4 · 미검증 2 · 반증 0

> ⚠️ **전제**: 어떤 Trait도 우리 자체 데이터에 대한 경험적 검증(요인분석/신뢰도/평가자간 일치도)을 거치지 않았다.
> 따라서 최고 등급은 `construct_supported`(학계가 구인을 인정)이며, 우리 라벨의 측정 타당성이 증명된 항목은 아직 없다.
> 비판적 감사는 `docs/leadership_validation_ledger.md` 참조.

---

## 1. 리더십 종류 (참조 이론)

- Full-Range Leadership (Transformational / Transactional / Laissez-faire)
- Servant Leadership
- Ethical Leadership
- Authentic Leadership
- Adaptive Leadership
- Ambidextrous Leadership
- Digital Leadership
- Data-Driven Decision Making
- Emotional Intelligence (Goleman)
- Competing Values Framework
- Dark Triad Research
- Hogan Development Survey (HDS)

## 2. 근거 논문 레지스트리

| ID | 인용 | 유형 | ref data | 파일 |
|----|------|------|----------|------|
| R01 | Dumdum, U. R., Lowe, K. B., & Avolio, B. J. (2002) | meta-analysis | O | DumdumLoweAvolioFinalVersion.doc |
| R02 | Batista-Foguet, J. M., Esteve, M., & van Witteloostuijn, A. (2021) | measurement-validation | O | journal.pone.0254329.pdf |
| R03 | van Dierendonck, D., & Nuijten, I. (2010) | scale-development | O | s10869-010-9194-1.pdf |
| R04 | Indarta, Y., et al. (2024) | systematic-review | O | 596-Article Text-2269-1-10-20241120.pdf |
| R05 | 최루디아 (2020) | empirical-multirater | O | KCI_FI002613507.pdf |
| R06 | Das, B. K., & Rajini, G. (2024) | intervention-case | O | LeadershipDevelopment.pdf |
| R07 | Emam, S. M., et al. (2024) | true-experiment | O | s12912-024-02395-w.pdf |
| R08 | Soomro et al. (2024) | systematic-review | O | s11846-023-00649-6.pdf |
| R09 | Azhar, Z., & Ayobami, A. (2026) | bibliometric | O | s43621-026-02809-6.pdf |
| X01 | Bass, B. M. (1985) | foundational-theory | X(외부) | - |
| X02 | Paulhus, D. L., & Williams, K. M. (2002) | foundational-theory | X(외부) | - |
| X03 | Rosenthal, S. A., & Pittinsky, T. L. (2006) | foundational-theory | X(외부) | - |
| X04 | Hogan, R., & Hogan, J. (2001) | foundational-theory | X(외부) | - |
| X05 | Goleman, D. (1995) | foundational-theory | X(외부) | - |

## 3. 긍정 Trait 카탈로그 (Positive)

| ID | 명칭(영/한) | Primary 이론 | 검증상태 | 근거강도 | 근거논문 | Required Labels |
|----|-------------|--------------|----------|----------|----------|-----------------|
| T01 | Strategic Decisive Leader / 결단형 | Full-Range Leadership (Transactional/Active) | 🟡 구인지지 | medium | R01,R02 | M06-01(목표 설정 및 기대치 명확화), M19-01(신속한 의사결정) |
| T02 | Collaborative Leader / 협업형 | Servant Leadership | 🟡 구인지지 | strong | R03,R04 | M11-01(적극적 경청), M15-01(심리적 안전감 조성_L15), M15-03(적극적 의견 청취) |
| T03 | Innovative Leader / 혁신형 | Transformational Leadership (Intellectual Stimulation) | 🟡 구인지지 | strong | R01,R08 | M03-03(새로운 접근 유도), M05-02(변화 실행 장려), M23-01(혁신 아이디어 발굴) |
| T04 | Crisis Manager / 위기 대응형 | Adaptive Leadership | 🔴 미검증 | medium | R09 | M19-01(신속한 의사결정), M10-01(실행력 및 완수), M20-01(위기 대응 및 문제 해결) |
| T05 | Analytical Leader / 분석형 | Data-Driven Decision Making | 🔴 미검증 | weak | R09,R02 | M34-01(데이터 기반 의사결정_L34) |
| T06 | Execution Driver / 실행형 | Competing Values Framework (Task Orientation, 과업지향) | 🟡 구인지지 | strong | R05,R01 | M10-01(실행력 및 완수), M10-02(목표 지향 실행), M19-01(신속한 의사결정) |
| T07 | Coaching Leader / 코칭형 | Transformational Leadership (Individualized Consideration) | 🟡 구인지지 | strong | R06,R07 | M02-02(성장 기회 제공), M07-02(성장 지향 피드백) |
| T09 | Visionary Leader / 비전 제시형 | Transformational Leadership (Idealized Influence & Inspirational Motivation) | 🟡 구인지지 | strong | X01,R01,R02 | M01-01(명확한 비전 제시), M01-04(비전 공유) |
| T11 | Empathetic Leader / 공감형 | Servant Leadership (Humility, Standing Back, Forgiveness) | 🟡 구인지지 | strong | R03,R04 | M12-01(공감 및 감정적 배려), M14-01(타인 우선 행동), M14-02(희생적 지원) |
| T12 | Balanced Leader / 균형형 | Competing Values Framework (Behavioral Complexity) | 🟠 부분지지 | medium | R05,R09 | M24-01(운영 안정성 유지), M28-01(투명한 소통) |
| T13 | Ethical Courageous Leader / 윤리적 용기형 | Ethical Leadership | 🟡 구인지지 | strong | R03,R09 | M33-01(도덕적 용기), M33-02(부당행위 대응), M30-01(언행 일치 및 일관성) |
| T14 | Learning Agile Leader / 학습 민첩형 | Adaptive Leadership | 🟠 부분지지 | medium | R09,R07 | M21-01(학습 및 디지털 민첩성), M22-01(혁신 기회 탐색_L22) |

## 4. 위험 Trait 카탈로그 (Negative)

| ID | 명칭(영/한) | Primary 이론 | 검증상태 | 근거강도 | 근거논문 | Required Labels |
|----|-------------|--------------|----------|----------|----------|-----------------|
| T101 | Risk: Avoidant / 회피형 | Laissez-Faire / Passive Leadership | 🟡 구인지지 | strong | R02,R01 | N08-01(직접 책임 전가), N08-02(책임 회피 발언) |
| T102 | Risk: Authoritarian / 권위주의 | Authoritarian Leadership | 🟠 부분지지 | weak | R05 | N15-03(공개적 비난), N19-01(독단 결정) |
| T103 | Risk: Integrity Violation / 정직성 위반 | Authentic Leadership (inverse) | 🟠 부분지지 | medium | R03 | N30-01(말과 행동 불일치), N28-01(정보 은폐), N34-01(데이터 조작) |
| T104 | Risk: Narcissistic Leadership / 자기애적 | Dark Triad Research | 🟡 구인지지 | strong | X02,X03 | N04-01(개인 숭배 유도), N09-01(공로 독점) |
| T105 | Risk: Manipulative Leadership / 조작적 | Dark Triad Research (Machiavellianism) | 🟡 구인지지 | strong | X02 | N02-02(보상 과장 약속), N02-03(감정적 압박) |
| T106 | Risk: Volatile Leadership / 기복형 | Hogan Development Survey (HDS) | 🟡 구인지지 | strong | X04 | N17-01(상황 무시 강경 대응), N24-01(과도한 통제) |

## 5. Trait별 학술 근거 상세

### T01 · Strategic Decisive Leader (결단형)
- 정의: 목표를 설정하고 신속·명확하게 의사결정하는 결단형 리더 (비전 제시는 T09, 실행 추진은 T06과 구분)
- Primary 이론: Full-Range Leadership (Transactional/Active)
- Secondary 이론: Adaptive Leadership
- 근거: 목표 설정과 신속·명확한 의사결정(결단). 비전 라벨 제거로 구인 정제.
- 근거강도: medium / 인용: R01:Dumdum, U. R., Lowe, K. B., & Avolio, B. J. (2002); R02:Batista-Foguet, J. M., Esteve, M., & van Witteloostuijn, A. (2021)
- **검증상태: construct_supported**
- ⚠️ 검증 공백/반증: 재정의 후 결단 구인으로 정렬됨. 우리 데이터 신뢰도 검증은 미실시

### T02 · Collaborative Leader (협업형)
- 정의: 팀워크와 소통 중심의 협력형 리더
- Primary 이론: Servant Leadership
- Secondary 이론: Transformational Leadership (Individualized Consideration)
- 근거: 팀 결속·소통·권한 위임(empowerment). 서번트 리더십 핵심 차원.
- 근거강도: strong / 인용: R03:van Dierendonck, D., & Nuijten, I. (2010); R04:Indarta, Y., et al. (2024)
- **검증상태: construct_supported**
- ⚠️ 검증 공백/반증: 서번트 empowerment 구인 견고(R03). 단, 우리 데이터 대상 신뢰도/요인 검증 없음

### T03 · Innovative Leader (혁신형)
- 정의: 새로운 시도와 변화를 주도하는 리더
- Primary 이론: Transformational Leadership (Intellectual Stimulation)
- Secondary 이론: Ambidextrous Leadership
- 근거: 지적 자극을 통한 새로운 시도와 변화 주도. 탐색(exploration) 행동.
- 근거강도: strong / 인용: R01:Dumdum, U. R., Lowe, K. B., & Avolio, B. J. (2002); R08:Soomro et al. (2024)
- **검증상태: construct_supported**
- ⚠️ 검증 공백/반증: 변혁적 지적자극 구인 견고. 라벨-이론 정합. 경험적 검증 없음

### T04 · Crisis Manager (위기 대응형)
- 정의: 위기 상황에서 빠르고 강력한 대응을 하는 리더
- Primary 이론: Adaptive Leadership
- Secondary 이론: Transactional Leadership (Active Management-by-Exception)
- 근거: 위기 상황에서의 적응적 대응과 능동적 예외 관리.
- 근거강도: medium / 인용: R09:Azhar, Z., & Ayobami, A. (2026)
- **검증상태: unverified**
- ⚠️ 검증 공백/반증: 위기관리를 안정적 "성향(trait)"으로 볼지 논쟁적; ref data 근거는 계량서지(R09)뿐

### T05 · Analytical Leader (분석형)
- 정의: 데이터 기반 의사결정을 선호하는 리더
- Primary 이론: Data-Driven Decision Making
- Secondary 이론: Transactional Leadership
- 근거: 데이터·근거 기반 의사결정 선호. 분석적 역량.
- 근거강도: weak / 인용: R09:Azhar, Z., & Ayobami, A. (2026); R02:Batista-Foguet, J. M., Esteve, M., & van Witteloostuijn, A. (2021)
- **검증상태: unverified**
- ⚠️ 검증 공백/반증: required 라벨 1개(M34-01)로 구인 취약; 데이터기반 의사결정은 역량이며 검증된 리더십 스타일 아님

### T06 · Execution Driver (실행형)
- 정의: 빠른 실행과 성과 창출 리더
- Primary 이론: Competing Values Framework (Task Orientation, 과업지향)
- Secondary 이론: Transactional Leadership
- 근거: 과업지향·성과 실행. 경쟁가치모형의 과업지향이 효과성과 연관(R05); 거래적 실행.
- 근거강도: strong / 인용: R05:최루디아 (2020); R01:Dumdum, U. R., Lowe, K. B., & Avolio, B. J. (2002)
- **검증상태: construct_supported**
- ⚠️ 검증 공백/반증: 과업지향 구인은 R05에서 검증. "contingent reward"(보상)와는 구분 — 보상형은 별도 라벨/Trait 필요(미보유)

### T07 · Coaching Leader (코칭형)
- 정의: 구성원 성장을 지원하는 리더
- Primary 이론: Transformational Leadership (Individualized Consideration)
- Secondary 이론: Servant Leadership
- 근거: 구성원 개별 배려·개발·피드백. 360도 개발 개입에서 실증 효과.
- 근거강도: strong / 인용: R06:Das, B. K., & Rajini, G. (2024); R07:Emam, S. M., et al. (2024)
- **검증상태: construct_supported**
- ⚠️ 검증 공백/반증: 변혁적 개별배려/코칭 구인 견고(R06,R07 개발효과 실증). 우리 라벨 매핑은 미검증

### T09 · Visionary Leader (비전 제시형)
- 정의: 미래 방향 제시 리더
- Primary 이론: Transformational Leadership (Idealized Influence & Inspirational Motivation)
- 근거: 비전 제시·영감적 동기부여. 변혁적 리더십의 증강효과 핵심.
- 근거강도: strong / 인용: X01:Bass, B. M. (1985) *(외부)*; R01:Dumdum, U. R., Lowe, K. B., & Avolio, B. J. (2002); R02:Batista-Foguet, J. M., Esteve, M., & van Witteloostuijn, A. (2021)
- **검증상태: construct_supported**
- ⚠️ 검증 공백/반증: 변혁적 II·IM 구인 견고, 라벨 정합. 경험적 검증 없음

### T11 · Empathetic Leader (공감형)
- 정의: 공감·겸손·정서적 배려를 바탕으로 구성원을 지원하는 리더 (구 T08 Emotional Intelligence 흡수, 서번트 8차원 기반)
- Primary 이론: Servant Leadership (Humility, Standing Back, Forgiveness)
- 근거: 공감·겸손·정서 배려(서번트 humility/standing back/forgiveness). 구 T08 흡수.
- 근거강도: strong / 인용: R03:van Dierendonck, D., & Nuijten, I. (2010); R04:Indarta, Y., et al. (2024)
- **검증상태: construct_supported**
- ⚠️ 검증 공백/반증: 구 T08 흡수로 판별타당도 문제 해소. 서번트 척도(R03) 문항 대비 매핑 검증은 미실시

### T12 · Balanced Leader (균형형)
- 정의: 균형 잡힌 리더십
- Primary 이론: Competing Values Framework (Behavioral Complexity)
- Secondary 이론: Ambidextrous Leadership
- 근거: 경쟁가치 간 균형·행동적 복잡성. R05가 리더십 복잡성의 효과성을 검정.
- 근거강도: medium / 인용: R05:최루디아 (2020); R09:Azhar, Z., & Ayobami, A. (2026)
- **검증상태: partially_supported**
- ⚠️ 검증 공백/반증: R05의 리더십 복잡성과 연결되나 우리 라벨(운영안정·투명소통)의 복잡성 측정 타당성 미검증

### T101 · Risk: Avoidant (회피형)
- 정의: 의사결정 회피 성향
- Primary 이론: Laissez-Faire / Passive Leadership
- 근거: 자유방임·수동적 회피. MLQ 독립 2차요인 및 메타분석에서 효과성과 부적 관계.
- 근거강도: strong / 인용: R02:Batista-Foguet, J. M., Esteve, M., & van Witteloostuijn, A. (2021); R01:Dumdum, U. R., Lowe, K. B., & Avolio, B. J. (2002)
- **검증상태: construct_supported**
- ⚠️ 검증 공백/반증: 자유방임이 MLQ 독립요인으로 검증(R02), 라벨 정합. 우리 데이터 검증 없음

### T102 · Risk: Authoritarian (권위주의)
- 정의: 과도한 권위주의 성향
- Primary 이론: Authoritarian Leadership
- Secondary 이론: Competing Values Framework (Hierarchy Orientation, 위계지향)
- 근거: 통제·위계지향. R05에서 위계지향이 주요 행동 차원으로 측정됨(부하·상사 평가).
- 근거강도: weak / 인용: R05:최루디아 (2020)
- **검증상태: partially_supported**
- ⚠️ 검증 공백/반증: R05 위계지향으로 ref data 근거 확보(unverified→상향). 다만 위계지향≠권위주의 위험, 부정성 입증엔 원전 추가 필요

### T103 · Risk: Integrity Violation (정직성 위반)
- 정의: 언행 불일치 및 투명성 위반
- Primary 이론: Authentic Leadership (inverse)
- Secondary 이론: Ethical Leadership
- 근거: 언행 불일치·진정성 위반. 서번트 척도의 authenticity 차원의 역(逆) 구인.
- 근거강도: medium / 인용: R03:van Dierendonck, D., & Nuijten, I. (2010)
- **검증상태: partially_supported**
- ⚠️ 검증 공백/반증: 진정성(역) 구인은 그럴듯하나 ref data 근거 간접적

### T13 · Ethical Courageous Leader (윤리적 용기형)
- 정의: 윤리적 판단과 도덕적 용기를 바탕으로 원칙을 지키는 리더
- Primary 이론: Ethical Leadership
- Secondary 이론: Servant Leadership (Courage, Accountability) / Authentic Leadership
- 근거: 윤리적 판단과 도덕적 용기. 서번트의 courage·accountability 차원과 정합.
- 근거강도: strong / 인용: R03:van Dierendonck, D., & Nuijten, I. (2010); R09:Azhar, Z., & Ayobami, A. (2026)
- **검증상태: construct_supported**
- ⚠️ 검증 공백/반증: 윤리·용기·진정성이 SLS courage/accountability/authenticity와 정합. 우리 라벨 검증은 미실시

### T14 · Learning Agile Leader (학습 민첩형)
- 정의: 실패에서 학습하고 디지털·AI 환경에 빠르게 적응하는 리더
- Primary 이론: Adaptive Leadership
- Secondary 이론: Digital Leadership
- 근거: 실패 학습과 디지털·AI 환경 적응. 역량 추세에서 디지털·적응 부상.
- 근거강도: medium / 인용: R09:Azhar, Z., & Ayobami, A. (2026); R07:Emam, S. M., et al. (2024)
- **검증상태: partially_supported**
- ⚠️ 검증 공백/반증: learning agility 구인은 존재하나 "digital" 주장 근거는 계량서지(R09)뿐; required 2개로 취약

### T104 · Risk: Narcissistic Leadership (자기애적)
- 정의: 자기 과대평가·착취 기반 자기애적 리더십
- Primary 이론: Dark Triad Research
- Secondary 이론: Destructive Leadership
- 근거: 자기 과대평가·착취. 다크 트라이어드 나르시시즘 구인.
- 근거강도: strong / 인용: X02:Paulhus, D. L., & Williams, K. M. (2002) *(외부)*; X03:Rosenthal, S. A., & Pittinsky, T. L. (2006) *(외부)*
- **검증상태: construct_supported**
- ⚠️ 검증 공백/반증: 다크 트라이어드 나르시시즘 구인 견고하나 원전이 ref data 외부(X02,X03); 우리 라벨 미검증

### T105 · Risk: Manipulative Leadership (조작적)
- 정의: 감정 조작·보상 과장·공포 기반 동기 유도 리더십
- Primary 이론: Dark Triad Research (Machiavellianism)
- Secondary 이론: Abusive Supervision
- 근거: 조작·냉소·허위 약속·감정 압박. 마키아벨리즘 핵심 행동.
- 근거강도: strong / 인용: X02:Paulhus, D. L., & Williams, K. M. (2002) *(외부)*
- **검증상태: construct_supported**
- ⚠️ 검증 공백/반증: 마키아벨리즘 구인 견고하나 원전 ref data 외부(X02); 우리 라벨 미검증

### T106 · Risk: Volatile Leadership (기복형)
- 정의: 감정 기복·과잉 통제로 혁신과 학습 문화를 억제하는 리더십
- Primary 이론: Hogan Development Survey (HDS)
- Secondary 이론: Destructive Leadership
- 근거: 감정 기복·과잉 통제. HDS Excitable·Cautious 탈선요인.
- 근거강도: strong / 인용: X04:Hogan, R., & Hogan, J. (2001) *(외부)*
- **검증상태: construct_supported**
- ⚠️ 검증 공백/반증: HDS 탈선요인 견고하나 원전 ref data 외부(X04); 우리 라벨 미검증

## 6. Positive Micro Label 인벤토리 (총 67개)

| Label ID | 명칭 | Macro |
|----------|------|-------|
| M01-01 | 명확한 비전 제시 | L01 |
| M01-02 | 장기 방향 설정 | L01 |
| M01-03 | 목표 정렬 | L01 |
| M01-04 | 비전 공유 | L01 |
| M02-01 | 내재적 동기 자극 | L02 |
| M02-02 | 성장 기회 제공 | L02 |
| M02-03 | 격려 및 인정 | L02 |
| M02-04 | 목표 몰입 유도 | L02 |
| M03-01 | 문제 재정의 | L03 |
| M03-02 | 창의적 질문 | L03 |
| M03-03 | 새로운 접근 유도 | L03 |
| M04-01 | 카리스마적 영향력 | L04 |
| M04-02 | 롤모델 행동 | L04 |
| M05-01 | 변화 필요 성명 | L05 |
| M05-02 | 변화 실행 장려 | L05 |
| M05-03 | 변화 문화 조성 | L05 |
| M06-01 | 목표 설정 및 기대치 명확화 | L06 |
| M06-02 | 세부 실행 지침 | L06 |
| M07-01 | 구체적 피드백 | L07 |
| M07-02 | 성장 지향 피드백 | L07 |
| M08-01 | 책임 및 원칙 준수 | L08 |
| M08-02 | 공정한 성과 인정_L08 | L08 |
| M09-01 | 공정한 성과 인정_L09 | L09 |
| M10-01 | 실행력 및 완수 | L10 |
| M10-02 | 목표 지향 실행 | L10 |
| M11-01 | 적극적 경청 | L11 |
| M11-02 | 개방적 의견 수용 | L11 |
| M12-01 | 공감 및 감정적 배려 | L12 |
| M12-02 | 감정적 지지 | L12 |
| M12-03 | 심리적 안전감 조성 | L12 |
| M14-01 | 타인 우선 행동 | L14 |
| M14-02 | 희생적 지원 | L14 |
| M15-01 | 심리적 안전감 조성_L15 | L15 |
| M15-02 | 개방적 소통 | L15 |
| M15-03 | 적극적 의견 청취 | L15 |
| M15-04 | 정보 투명 공유 | L15 |
| M15-05 | 신뢰 형성 | L15 |
| M15-06 | 심리적 보호 | L15 |
| M17-01 | 상황적 유연성 | L17 |
| M18-01 | 불확실성 속 안정감 제공 | L18 |
| M18-02 | 데이터 기반 의사결정_L18 | L18 |
| M19-01 | 신속한 의사결정 | L19 |
| M20-01 | 위기 대응 및 문제 해결 | L20 |
| M21-01 | 학습 및 디지털 민첩성 | L21 |
| M21-02 | 실패 수용 및 회복 | L21 |
| M22-01 | 혁신 기회 탐색_L22 | L22 |
| M22-02 | 실험 및 도전 장려 | L22 |
| M23-01 | 혁신 아이디어 발굴 | L23 |
| M23-02 | 아이디어 발굴 장려 | L23 |
| M24-01 | 운영 안정성 유지 | L24 |
| M26-01 | 실험 및 도전 장려_L26 | L26 |
| M27-01 | 전략적 자원 배분 | L27 |
| M28-01 | 투명한 소통 | L28 |
| M28-02 | 포용성 및 다양성 존중 | L28 |
| M30-01 | 언행 일치 및 일관성 | L30 |
| M31-01 | 포용성 및 다양성 존중_L31 | L31 |
| M32-01 | 자기인식 및 자기성찰 | L32 |
| M32-02 | 자기성찰 및 개선 | L32 |
| M33-01 | 도덕적 용기 | L33 |
| M33-02 | 부당행위 대응 | L33 |
| M33-03 | 압력 저항 | L33 |
| M33-04 | 공정한 의사결정 | L33 |
| M33-05 | 책임 있는 행동 | L33 |
| M34-01 | 데이터 기반 의사결정_L34 | L34 |
| M35-01 | 디지털 도구 활용 및 자동화 | L35 |
| M37-01 | AI 및 기술 기반 혁신 주도 | L37 |
| M37-02 | 디지털 리터러시 전파 | L37 |

## 7. Negative Micro Label 인벤토리 (총 58개)

| Label ID | 명칭 | Macro |
|----------|------|-------|
| N01-01 | 비현실적 목표 제시 | N01 |
| N01-02 | 비전 과장 | N01 |
| N01-03 | 방향성 불일치 | N01 |
| N02-01 | 공포 기반 동기 유도 | N02 |
| N02-02 | 보상 과장 약속 | N02 |
| N02-03 | 감정적 압박 | N02 |
| N03-01 | 아이디어 무시 | N03 |
| N03-02 | 비판 금지 | N03 |
| N03-03 | 질문 억제 | N03 |
| N04-01 | 개인 숭배 유도 | N04 |
| N04-02 | 권위 과시 | N04 |
| N05-01 | 의견 없이 변화 강행 | N05 |
| N05-02 | 준비 없는 변화 추진 | N05 |
| N05-03 | 변화 반대 억압 | N05 |
| N06-01 | 목표 불명확 전달 | N06 |
| N06-02 | 우선순위 불명확 | N06 |
| N07-01 | 성과만으로 평가 | N07 |
| N07-02 | 공개적 질책 | N07 |
| N08-01 | 직접 책임 전가 | N08 |
| N08-02 | 책임 회피 발언 | N08 |
| N08-03 | 의사결정 지연 | N08 |
| N09-01 | 공로 독점 | N09 |
| N09-02 | 타인 업적 가로채기 | N09 |
| N10-01 | 실행 부진 | N10 |
| N10-02 | 마감 무시 | N10 |
| N11-01 | 경청 거부 | N11 |
| N11-02 | 의견 폄하 | N11 |
| N12-01 | 공감 결여 | N12 |
| N12-02 | 정서적 무관심 | N12 |
| N12-03 | 심리적 압박 | N12 |
| N14-01 | 자기 이익 우선 | N14 |
| N14-02 | 공로 가로채기 | N14 |
| N14-03 | 팀 희생 강요 | N14 |
| N15-01 | 의견 무시 | N15 |
| N15-02 | 발언 차단 | N15 |
| N15-03 | 공개적 비난 | N15 |
| N15-04 | 실수 처벌 | N15 |
| N15-05 | 불신 조장 | N15 |
| N15-06 | 보복 암시 | N15 |
| N17-01 | 상황 무시 강경 대응 | N17 |
| N18-01 | 불안 조장 발언 | N18 |
| N18-02 | 위기 과장 | N18 |
| N19-01 | 독단 결정 | N19 |
| N21-01 | 디지털 거부 | N21 |
| N22-01 | 실패 은폐 | N22 |
| N22-02 | 책임 회피 학습 차단 | N22 |
| N23-01 | 혁신 아이디어 차단 | N23 |
| N24-01 | 과도한 통제 | N24 |
| N26-01 | 실험 실패 처벌 | N26 |
| N27-01 | 자원 독점 | N27 |
| N28-01 | 정보 은폐 | N28 |
| N30-01 | 말과 행동 불일치 | N30 |
| N31-01 | 차별 행동 | N31 |
| N33-01 | 부당행위 묵인 | N33 |
| N33-02 | 문제 회피 | N33 |
| N34-01 | 데이터 조작 | N34 |
| N35-01 | 도구 남용 | N35 |
| N37-01 | AI 부정 사용 | N37 |

## 8. 무결성 점검 (자동)

- 이론 매핑 누락 Trait: 없음 ✅
- 근거강도 weak(보강 필요): ['T05', 'T102']
- 복수 긍정 Trait가 공유하는 required Label(판별타당도 주의):
  - M10-01(실행력 및 완수) → T04, T06
  - M19-01(신속한 의사결정) → T01, T04, T06
