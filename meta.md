# 🚀 리더십 성향 추론 엔진
## 통합 메타데이터 설계서 v1.0
> Leadership Profiling Engine — Integrated Metadata Schema
> 2026.04.09 | Based on Design v2.0

---

## 📌 문서 목적

본 문서는 리더십 성향 추론 엔진(v2.0)에서 수집·생성되는 모든 데이터를 체계적으로 정의한 통합 메타데이터 설계서입니다.

| 목적 | 설명 | 주요 활용처 |
|---|---|---|
| ① 개인 인사이트 | 사용자 프로필 + 진단 결과를 결합한 개인 맞춤 분석 | 테스트 결과 리포트, 개인 코칭 제안, 리스크 경고 |
| ② 집단 분석 | 여러 사용자 결과를 집계하여 패턴·트렌드 탐색 | HR 대시보드, 조직 리더십 진단, 업종·직급별 비교 |
| ③ 이력 추적 | 동일 사용자의 시간 흐름에 따른 성향 변화 추적 | 리더십 프로그램 효과 측정, 성장 가시화 |

---

# PART 1. 사용자 프로필 메타데이터

테스트 응시자의 기본 정보 및 맥락 정보를 저장하는 필드 정의입니다. 진단 결과 해석의 기준이 됩니다.

## 1-1. 기본 식별자 (User Identity)

| 필드명 | 타입 | 필수여부 | 설명 |
|---|---|---|---|
| user_id | UUID | Required | 사용자 고유 식별자 (익명화 처리) |
| session_id | UUID | Required | 테스트 세션 고유 ID — 동일 사용자의 반복 테스트 구분 |
| created_at | DateTime | Required | 최초 가입·등록 타임스탬프 (ISO 8601) |
| test_taken_at | DateTime | Required | 현재 테스트 응시 시각 |
| source_channel | String | Optional | 유입 경로 (web / app / enterprise / api) |

## 1-2. 인구통계 정보 (Demographics)

집단 분석 및 맥락 보정(Context Layer)에 활용됩니다. 모든 필드는 선택 동의 기반입니다.

| 필드명 | 타입 | 허용값 예시 | 활용 목적 |
|---|---|---|---|
| age_group | Enum | 20s / 30s / 40s / 50s+ | 연령대별 리더십 성향 분포 비교 |
| gender | Enum | M / F / N / Prefer not | 성별 리더십 패턴 연구 (선택) |
| industry | String | IT / 금융 / 제조 / 의료 등 | 업종별 Trait 분포 집계 |
| job_level | Enum | 사원 / 대리 / 과장 / 팀장 / 임원 | 직급별 리더십 갭 분석 |
| management_years | Integer | 0 ~ 30 | 관리자 경력 연수 — Confidence 보정에 활용 |
| team_size | Enum | 1-5 / 6-15 / 16-50 / 50+ | 팀 규모별 리더십 유형 차이 분석 |
| organization_type | Enum | 스타트업 / 중소 / 대기업 / 공공 | 조직 유형별 기준값 비교 |
| country_region | String | KR / US / JP 등 | 문화권별 리더십 패턴 비교 |

## 1-3. 테스트 맥락 정보 (Test Context)

| 필드명 | 타입 | 값 | 설명 |
|---|---|---|---|
| test_type | Enum | choice / narrative / hybrid | 응시한 테스트 유형 (선택형/서술형/복합형) |
| test_version | String | v1.0 / v2.0 | 테스트 문항 버전 — 결과 비교 시 버전 통제 |
| context_tag | Enum | crisis / normal / innovation | Context Layer 적용 맥락 태그 |
| response_time_avg | Float | 초(sec) | 문항당 평균 응답 시간 — 신뢰도 보정 참고 |
| completion_rate | Float | 0.0 ~ 1.0 | 문항 완료율 — 낮을 경우 Confidence Low 처리 |
| device_type | Enum | mobile / desktop / tablet | 디바이스 유형 (UX 개선 분석용) |
| language | String | ko / en / ja | 응시 언어 |

---

# PART 2. 진단 결과 메타데이터

Pattern Engine이 생성하는 추론 결과 전체를 저장합니다. 개인 리포트와 집단 분석의 핵심 데이터입니다.

## 2-1. Trait 결과 (trait_results[ ])

Primary / Secondary / Hybrid / Negative Trait 모두 동일 구조로 저장됩니다.

| 필드명 | 타입 | 범위/예시 | 설명 |
|---|---|---|---|
| trait_id | String | T01 ~ T12, T_RISK_* | Trait 고유 ID |
| trait_name | String | Strategic Decisive... | Trait 명칭 |
| trait_type | Enum | primary / secondary / hybrid / negative | 결과 내 역할 분류 |
| strength_raw | Float | 0.0 ~ ∞ | 로그 정규화 전 Raw Strength 값 |
| strength_log | Float | 0.0 ~ ∞ | Log 정규화 후 값 (수확 체감 반영) |
| strength_normalized | Float | 0.0 ~ 1.0 | K-Trait 기준 최종 정규화 값 |
| strength_level | Enum | Strong / Moderate / Weak | 0.8↑Strong, 0.5~0.8 Moderate, 0.5↓Weak |
| confidence | Float | 0.0 ~ 1.0 | 신뢰도 점수 (Volume+NLP+Consistency 가중합) |
| confidence_level | Enum | High / Medium / Low | 0.75↑High, 0.45~0.75 Medium, 0.45↓Low |
| is_primary | Boolean | true / false | Primary Trait 여부 |
| context_applied | String | crisis / normal / innovation | 적용된 Context 태그 |
| context_multiplier | Float | 1.0 ~ 1.5 | Context에 의해 적용된 가중치 |
| hard_conflict_triggered | Boolean | true / false | Hard Conflict 발생 여부 (Confidence Low 강제) |
| forbidden_triggered | Array[String] | [N08-01, N15-03] | 실제 탐지된 Hard Forbidden Label 목록 |

## 2-2. 근거 레이블 (evidence[ ])

각 Trait 판정의 근거가 된 Micro Label 목록입니다. 투명성 확보 및 설명 가능 AI(XAI) 구현에 활용됩니다.

| 필드명 | 타입 | 예시 | 설명 |
|---|---|---|---|
| label_id | String | M33-01 / N08-01 | Micro Label 고유 ID (M=긍정, N=부정) |
| label_type | Enum | M / N | 긍정(M) 또는 부정(N) 레이블 구분 |
| role | Enum | REQ / OPT / SOFT_FORBIDDEN | Trait 내 역할 (Required/Optional/Soft Forbidden) |
| nlp_confidence | Float | 0.0 ~ 1.0 | NLP 모델이 추출한 해당 레이블의 신뢰도 |
| weight | Float | 0.0 ~ 1.0 | Trait 설계 시 지정된 레이블 가중치 |
| penalty | Float | 0.0 ~ 1.0 | N 레이블의 감점 값 (Soft Forbidden만 해당) |
| is_critical | Boolean | true / false | critical: true 레이블 여부 (N08-01, N34-01 등) |
| source_question_id | String | NQ1 / SQ2 / HQ3 | 해당 레이블이 추출된 문항 ID |
| extracted_text_snippet | String | "팀원이 실수했고..." | 레이블 추출 근거가 된 응답 텍스트 일부 (서술형) |

## 2-3. 부정 리더십 및 리스크 결과

### negative_traits[ ]

| 필드명 | 타입 | 예시 | 설명 |
|---|---|---|---|
| trait_id | String | T10 / T11 / T_RISK_* | Negative Trait ID |
| trait_name | String | Risk: Avoidant | 부정 성향 명칭 |
| severity_score | Float | 0.0 ~ 1.0 | 부정 성향 강도 점수 |
| severity_level | Enum | high / medium / low | 0.7↑high, 0.4~0.7 medium, 0.4↓low |
| required_labels_met | Array[String] | [N08-01, N08-02] | Required Label 충족 목록 |
| optional_labels_found | Array[String] | [N10-01] | Optional Label 감지 목록 |
| conflict_with_positive | Array[String] | [T01, T07] | 충돌하는 Positive Trait ID 목록 |

### risks[ ]

| 필드명 | 타입 | 예시 | 설명 |
|---|---|---|---|
| risk_id | String | R01 / R02 / R03 | 리스크 고유 ID |
| risk_name | String | Toxic Leader Risk | 리스크 명칭 |
| severity | Enum | high / medium / low | 리스크 심각도 |
| risk_score | Float | 0.0 ~ 1.0 | 리스크 종합 점수 |
| trigger_condition | String | NLabel 3개 이상 | 리스크 발동 조건 설명 |
| triggered_labels | Array[String] | [N08-01, N15-03, N28-01] | 리스크 발동에 기여한 N Label 목록 |
| coaching_flag | Boolean | true / false | 코칭 제안 트리거 여부 |

## 2-4. Hybrid Trait 결과 (hybrid_traits[ ])

| 필드명 | 타입 | 예시 | 설명 |
|---|---|---|---|
| hybrid_id | String | H01 / H02 | Hybrid 규칙 ID |
| hybrid_name | String | Strategic Analytical | Hybrid Trait 명칭 |
| source_traits | Array[String] | [T01, T05] | 결합된 원본 Trait ID 목록 |
| hybrid_weight | Float | 1.0 ~ 1.5 | Hybrid 가중치 (설계안 정의값) |
| combined_strength | Float | 0.0 ~ 1.0 | 결합 후 최종 Strength |

## 2-5. Resolution Layer 처리 결과 (resolution)

| 필드명 | 타입 | 예시 | 설명 |
|---|---|---|---|
| conflict_detected | Boolean | true / false | Trait 간 충돌 감지 여부 |
| conflict_type | Enum | competitive / complementary / contradiction | 경쟁/보완/모순 충돌 유형 |
| conflict_pairs | Array[Array] | [[T01, T04]] | 충돌이 감지된 Trait 쌍 목록 |
| resolution_action | Enum | select_dominant / generate_hybrid / suspend | 충돌 처리 결과 액션 |
| suspended_judgment | Boolean | true / false | 판단 유보 여부 (모순 충돌 시) |

---

# PART 3. 이력 추적 메타데이터

동일 사용자의 반복 응시 결과를 시간 축으로 연결합니다. 리더십 성장 추적 및 프로그램 효과 측정에 사용됩니다.

## 3-1. 응시 이력 (test_history[ ])

| 필드명 | 타입 | 예시 | 설명 |
|---|---|---|---|
| attempt_number | Integer | 1, 2, 3... | 동일 사용자의 응시 순번 |
| test_taken_at | DateTime | 2026-01-15T09:30:00 | 응시 일시 |
| primary_trait_id | String | T01 | 해당 회차 Primary Trait |
| primary_strength | Float | 0.82 | 해당 회차 Primary Strength |
| negative_traits_count | Integer | 0 ~ N | 감지된 Negative Trait 수 |
| risk_score_max | Float | 0.0 ~ 1.0 | 가장 높은 Risk Score |
| context_tag | String | normal | 적용된 Context 태그 |
| test_type | String | hybrid | 응시 유형 |
| snapshot_hash | String | sha256 hash | 결과 불변성 검증용 해시 |

## 3-2. 성향 변화 추적 (trait_delta)

회차 간 Trait Strength 변화를 계산하여 성장 방향과 속도를 측정합니다.

| 필드명 | 타입 | 계산 방식 | 설명 |
|---|---|---|---|
| trait_id | String | — | 비교 대상 Trait ID |
| prev_strength | Float | 이전 회차 값 | 이전 응시의 Strength |
| curr_strength | Float | 현재 회차 값 | 현재 응시의 Strength |
| delta | Float | curr - prev | 변화량 (양수=성장, 음수=약화) |
| delta_pct | Float | delta / prev × 100 | 변화율 (%) |
| trend | Enum | improving / stable / declining | 3회 이상 데이터 기반 트렌드 |
| sessions_compared | Integer | 2 ~ N | 비교에 사용된 회차 수 |
| confidence_trend | Enum | increasing / stable / decreasing | 신뢰도 변화 방향 |

## 3-3. 리더십 프로그램 효과 측정 (program_impact)

| 필드명 | 타입 | 예시 | 설명 |
|---|---|---|---|
| program_id | String | PROG-2026-Q1 | 참여한 리더십 프로그램 ID |
| pre_test_session_id | UUID | — | 프로그램 참여 전 테스트 세션 |
| post_test_session_id | UUID | — | 프로그램 참여 후 테스트 세션 |
| target_trait_id | String | T07 | 프로그램이 목표한 Trait |
| target_strength_change | Float | +0.15 | 목표 Strength 변화량 |
| actual_strength_change | Float | +0.21 | 실제 Strength 변화량 |
| negative_reduction | Float | -0.30 | Negative Trait Severity 감소량 |
| goal_achieved | Boolean | true / false | 목표 달성 여부 (|actual| ≥ |target|) |
| effect_size | Float | Cohen's d | 효과 크기 (집단 비교 분석용) |

---

# PART 4. 집단 분석 메타데이터

HR 담당자 및 조직 관리자가 팀·조직 단위로 리더십 분포를 분석하는 데 사용됩니다.

## 4-1. 집단 집계 단위 (cohort)

| 필드명 | 타입 | 예시 | 설명 |
|---|---|---|---|
| cohort_id | String | COHORT-IT-2026Q1 | 집단 분석 단위 ID |
| cohort_type | Enum | department / industry / program / custom | 집단 구분 기준 |
| cohort_name | String | 개발팀 Q1 진단 | 집단 명칭 |
| member_count | Integer | 45 | 집단 내 응시자 수 |
| date_range | DateRange | 2026-01 ~ 2026-03 | 집계 기간 |
| avg_confidence | Float | 0.71 | 집단 평균 Confidence |
| dominant_trait | String | T02 | 가장 많이 나온 Primary Trait |
| dominant_negative | String | T10 | 가장 많이 나온 Negative Trait |
| risk_prevalence | Float | 0.23 | 리스크 보유 비율 (risk 1개 이상 비율) |

## 4-2. Trait 분포 통계 (trait_distribution[ ])

| 필드명 | 타입 | 예시 | 설명 |
|---|---|---|---|
| trait_id | String | T01 | 집계 대상 Trait |
| primary_count | Integer | 12 | 해당 Trait이 Primary인 응시자 수 |
| primary_ratio | Float | 0.267 | Primary 비율 |
| avg_strength | Float | 0.74 | 집단 내 평균 Strength |
| std_strength | Float | 0.11 | Strength 표준편차 |
| high_confidence_ratio | Float | 0.58 | High Confidence 비율 |
| by_job_level | Object | {팀장: 0.4, 사원: 0.1} | 직급별 분포 |
| by_industry | Object | {IT: 0.35, 제조: 0.18} | 업종별 분포 |
| percentile_50 | Float | 0.72 | 중앙값 (P50) |
| percentile_90 | Float | 0.91 | 상위 10% 기준값 (P90) |

## 4-3. 리더십 갭 분석 (gap_analysis)

집단 내 리더십 유형 불균형 및 특정 Trait 부재를 감지합니다.

| 필드명 | 타입 | 예시 | 설명 |
|---|---|---|---|
| missing_traits | Array[String] | [T04, T09] | 집단 내 Primary 보유자 0명인 Trait |
| underrepresented_traits | Array[String] | [T07] | 비율이 전체 평균 대비 50% 미만인 Trait |
| overrepresented_traits | Array[String] | [T11] | 비율이 전체 평균 대비 2배 초과인 Trait |
| negative_cluster_risk | Boolean | true / false | 부정 Trait 집중 여부 (동일 Trait 30%↑) |
| recommended_programs | Array[String] | [PROG-T04, PROG-T07] | 갭 해소를 위한 추천 프로그램 ID |

---

# PART 5. 인사이트 생성 메타데이터

사용자·집단·이력 데이터를 결합하여 실질적인 인사이트를 자동 생성하는 규칙과 출력 구조입니다.

## 5-1. 개인 맞춤 인사이트 트리거 규칙

| ID | 인사이트 유형 | 트리거 조건 | 출력 메시지 템플릿 |
|---|---|---|---|
| INS-01 | 강점 부각 | primary.strength_level = Strong AND confidence_level = High | 당신의 [Trait명] 성향이 매우 강하게 나타납니다. 이 강점은 [상황]에서 특히 빛납니다. |
| INS-02 | 리스크 경고 | risks 존재 AND risk.severity = high | [리스크명]이 감지되었습니다. [발동 레이블] 패턴이 반복적으로 나타나고 있습니다. |
| INS-03 | 성향 충돌 알림 | resolution.conflict_type = contradiction | 두 성향([T1], [T2]) 사이의 모순이 감지되어 결과의 신뢰도가 낮게 설정되었습니다. |
| INS-04 | Context 재해석 | context_tag = crisis AND trait = T04 | 위기 상황에서는 당신의 통제형 성향이 '문제 해결형 리더'로 긍정적으로 작용할 수 있습니다. |
| INS-05 | Hybrid 발현 | hybrid_traits 존재 | 두 가지 강점이 결합된 [Hybrid명] 유형이 나타났습니다. 이는 전체 응시자의 [N]%에서만 나타납니다. |
| INS-06 | 성장 축하 | delta.trend = improving AND delta_pct > 15 | 지난 응시 대비 [Trait명] 성향이 [N]% 강화되었습니다. 꾸준한 성장이 데이터로 확인됩니다. |
| INS-07 | 코칭 제안 | negative_traits 존재 AND coaching_flag = true | [Negative Trait명] 패턴을 완화하기 위한 [프로그램명] 과정을 추천드립니다. |
| INS-08 | 동료 비교 | cohort 존재 AND primary.strength < cohort.percentile_50 | 같은 직급 평균 대비 [Trait명] 성향이 낮게 나타났습니다. 집중 개발 영역으로 추천됩니다. |

## 5-2. 집단 인사이트 트리거 규칙

| ID | 인사이트 유형 | 트리거 조건 | 출력 메시지 템플릿 |
|---|---|---|---|
| CIN-01 | 리더십 공백 경고 | gap_analysis.missing_traits 존재 | 조직 내 [Trait명] 리더십이 전무합니다. [상황]에서 취약점이 될 수 있습니다. |
| CIN-02 | 권위주의 집중 경보 | T11 비율 > 30% | 권위주의 성향(T11)이 집단의 30%를 초과합니다. 심리적 안전감 저하 위험이 높습니다. |
| CIN-03 | 혁신 역량 부족 | T03+T06 합산 비율 < 15% | 혁신·실행 리더십이 부족합니다. 변화 추진 역량 강화 프로그램을 권장합니다. |
| CIN-04 | 프로그램 효과 검증 | program_impact.effect_size > 0.5 | 이번 프로그램에서 Cohen's d [N]의 유의미한 효과가 측정되었습니다. |

---

# PART 6. 통합 JSON 스키마 (구현 참조용)

실제 DB 저장 및 API 응답 구조의 참조 스키마입니다. 필드 이름은 snake_case를 기준으로 합니다.

```json
{
  "user_id": "uuid-xxxx",
  "session_id": "uuid-yyyy",
  "test_taken_at": "2026-04-09T10:30:00Z",

  "profile": {
    "age_group": "30s",
    "job_level": "팀장",
    "industry": "IT",
    "management_years": 5,
    "team_size": "6-15",
    "organization_type": "대기업"
  },

  "test_context": {
    "test_type": "hybrid",
    "test_version": "v2.0",
    "context_tag": "normal",
    "completion_rate": 0.96
  },

  "results": {
    "primary_trait": {
      "trait_id": "T01",
      "trait_name": "Strategic Decisive Leader",
      "strength_normalized": 0.87,
      "strength_level": "Strong",
      "confidence": 0.81,
      "confidence_level": "High",
      "context_multiplier": 1.0,
      "hard_conflict_triggered": false
    },

    "secondary_traits": [
      {
        "trait_id": "T05",
        "strength_level": "Moderate",
        "confidence_level": "Medium"
      }
    ],

    "hybrid_traits": [
      {
        "hybrid_id": "H01",
        "hybrid_name": "Strategic Analytical",
        "source_traits": ["T01", "T05"],
        "combined_strength": 0.83
      }
    ],

    "negative_traits": [
      {
        "trait_id": "T10",
        "trait_name": "Risk: Avoidant",
        "severity_score": 0.42,
        "severity_level": "medium"
      }
    ],

    "risks": [
      {
        "risk_id": "R03",
        "risk_name": "Integrity Risk",
        "severity": "medium",
        "risk_score": 0.55,
        "coaching_flag": true
      }
    ],

    "evidence": [
      {
        "label_id": "M01-01",
        "role": "REQ",
        "nlp_confidence": 0.92,
        "is_critical": false
      },
      {
        "label_id": "N08-01",
        "role": "SOFT_FORBIDDEN",
        "penalty": 0.7,
        "is_critical": true
      }
    ],

    "resolution": {
      "conflict_detected": false,
      "suspended_judgment": false
    }
  },

  "history": {
    "attempt_number": 2,
    "trait_delta": [
      {
        "trait_id": "T01",
        "delta": 0.12,
        "trend": "improving"
      }
    ]
  }
}
```

---

# PART 7. 핵심 용어 정의 및 필드 네이밍 규칙

## 7-1. 핵심 용어 정의 (Glossary)

| 용어 | 표기/범위 | 정의 |
|---|---|---|
| Micro Label | M/N Code | NLP가 텍스트에서 추출하는 최소 행동 신호 단위. M=긍정, N=부정. |
| Trait | T + 번호 | 복수의 Micro Label 패턴으로 정의되는 리더십 성향 유형. |
| Strength | 0.0 ~ 1.0 | Trait이 얼마나 강하게 나타났는지를 나타내는 정규화 점수. |
| Confidence | 0.0 ~ 1.0 | 추론 결과의 신뢰 가능성. 데이터 양·NLP 정확도·일관성 합산. |
| Hard Forbidden | 즉시 무효 | 해당 N Label 탐지 시 Trait Strength를 0으로 강제하는 규칙. |
| Soft Forbidden | 감점 적용 | Strength를 약화시키고 Risk로 출력하는 N Label 규칙. |
| Hybrid Trait | 복합 성향 | 두 Positive Trait이 동시에 강하게 나타날 때 생성되는 결합 성향. |
| Resolution Layer | 충돌 처리 | 복수 Trait 간 경쟁·보완·모순 관계를 처리하는 엔진 레이어. |
| Context Tag | 맥락 태그 | 응시자가 처한 상황 맥락 (crisis/normal/innovation). Trait 해석에 영향. |
| Delta | 변화량 | 연속 응시 간 Strength 차이값. 양수=강화, 음수=약화. |
| Effect Size | Cohen's d | 프로그램 전후 집단 평균 차이를 표준화한 효과 크기 지표. |
| Cohort | 집단 분석 단위 | 동일 기준(부서, 프로그램, 업종 등)으로 묶인 응시자 집합. |

## 7-2. 필드 네이밍 규칙

| 규칙 | 적용 대상 | 예시 |
|---|---|---|
| snake_case | 모든 필드 | user_id, trait_name, strength_level |
| _id 접미사 | 고유 식별자 필드 | user_id, session_id, cohort_id |
| _at 접미사 | 타임스탬프 필드 | created_at, test_taken_at |
| _level 접미사 | 등급 Enum 필드 | strength_level, confidence_level, severity_level |
| _count 접미사 | 정수 집계 필드 | member_count, attempt_number |
| _ratio / _score | 소수 비율/점수 | primary_ratio, risk_score, effect_size |
| _flag | Boolean 트리거 | coaching_flag, is_critical, is_primary |
| [ ] 표기 | 배열 필드 | evidence[ ], trait_results[ ], risks[ ] |

---

*리더십 성향 추론 엔진 통합 메타데이터 설계서 v1.0 | 2026.04.09 | Based on Design v2.0*
