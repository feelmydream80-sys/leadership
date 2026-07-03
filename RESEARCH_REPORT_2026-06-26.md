# Leadership System — 종합 연구 보고서

> **Comprehensive Research Report on Paper Investigation, Theory–Trait–Label Mapping, and Data Organization**
>
> **작성일:** 2026-06-26 | **마지막 갱신:** 2026-07-01 (정리 후 동기화)
> **이론:** 12개 | **Trait:** 20개 | **Micro Label:** 178개 | **분석 논문:** 108편(원본 metadata.csv 기준)
>
> ⚠️ **동기화 주의(2026-07-01):** 본 보고서는 2026-06-26 `ref data/` 워크스페이스 기준으로 작성되었습니다.
> 2026-06-30 폴더 정리로 `ref data/`는 `research/`로 통합되었고, **저장소에 실재하는 원문은 핵심 논문 9편(`research/papers/`) + 서베이 1편(`research/surveys/`) + 근거 매핑(`research/evidence_mapping/label_evidence_map.json`)뿐**입니다.
> `metadata.csv`, `consolidated_summary.*`, `pdfs/`, `meta/`, `theory/`, `non_leadership/` 등 §2·§9·§10·§13·Appendix A에 서술된 자산은 **현재 저장소에 부재**(정리 시 제외)하며, 아래 본문은 당시 조사 이력으로 보존합니다. 실제 파일 위치는 §10.1(갱신본)을 따르세요.

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Paper Investigation Overview](#2-paper-investigation-overview)
3. [Core Leadership Papers (18 Papers)](#3-core-leadership-papers-18-papers)
4. [12 Leadership Theories](#4-12-leadership-theories)
5. [Trait System (20 Traits)](#5-trait-system-20-traits)
6. [Micro Label Inventory (178 Labels)](#6-micro-label-inventory-178-labels)
7. [Label Evidence Mapping](#7-label-evidence-mapping)
8. [Negative Trait & Label Analysis](#8-negative-trait--label-analysis)
9. [Non-Leadership Paper Separation](#9-non-leadership-paper-separation)
10. [Folder Structure & Change History](#10-folder-structure--change-history)
11. [Key Issues & Improvement Recommendations](#11-key-issues--improvement-recommendations)
12. [System Integration (Vector DB Pipeline)](#12-system-integration-vector-db-pipeline)
13. [External Evidence Registry](#13-external-evidence-registry)
14. [Appendices](#14-appendices)

---

## 1. Executive Summary

### 1.1 Project Background

The Leadership Label Vector DB Project builds an AI-powered leadership analysis engine that infers leadership traits from text. The engine is grounded in academic leadership research, with every trait and micro label anchored to peer-reviewed empirical studies.

### 1.2 Scope of This Report

| Domain | Count | Details |
|--------|-------|---------|
| Total papers in metadata | 108 | Master index in `metadata.csv` |
| Leadership papers | ~88 | 8 core PDFs + 17 additional PDFs + 38 metadata records + 25 metadata-only |
| Non-leadership excluded | 20 | Moved to `non_leadership/` folder |
| Leadership theories | 12 | Including 4 newly identified |
| Positive Traits | 12 (active) | T01–T14 (T08 merged into T11, T10 inactive) |
| Risk (Negative) Traits | 6 | T101–T106 |
| Positive Macro Labels | 48 | L01–L48 |
| Negative Macro Labels | 32 | N01–N43 |
| Positive Micro Labels | 98 | M01-01 through M48-01 |
| Negative Micro Labels | 80 | N01-01 through N43-01 |
| Training samples | 12,460 | 70 per label (50 clean + 20 hard negative) |
| Vector DB | 178 vectors | KoE5 embedding, 768-dim |
| FAISS index | 1 | `data/vectors/label_vectors.faiss` |

### 1.3 Key Findings

1. **12 distinct leadership theories** ground the system, up from originally 8. New additions: Ambidextrous, Authentic, Emotional Intelligence, Transactional Leadership.
2. **20 Trait system** (14 positive originally, 12 currently active + 6 risk). T08 (Emotional Intelligence) was absorbed into T11 (Empathetic). T10 (Strategic Execution) is defined but unmapped.
3. **178 micro labels** provide granular behavioral units — 98 positive, 80 negative, each with When/Not_When conditions.
4. **Discriminant validity concerns** exist between several trait pairs (e.g., T01↔T09 sharing M01-01), consistent with academic critiques by Soomro et al. (2024) and MLQ literature.
5. **20 non-leadership papers** were identified and isolated — all misclassified due to the keyword "transactional" appearing in quantum physics, computer science, and economics contexts.

---

## 2. Paper Investigation Overview

### 2.1 Master Metadata (metadata.csv)

The master CSV contains 108 papers with the following fields:
- `id` (1–108)
- `title`
- `authors`
- `source` (OpenAlex, Crossref, arXiv)
- `published_date`
- `url`
- `pdf_url`
- `keywords`
- `abstract` (English)
- `abstract_ko` (Korean translation)
- `domain` (classification tag: `leadership` or other)
- `downloaded_at`, `created_at`

### 2.2 Source Distribution

| Source | Count | Notes |
|--------|-------|-------|
| **OpenAlex** | ~60 | Full PDFs for IDs 54, 55, 57, 59, 103, 105 + metadata for 52, 71–80 |
| **Crossref** | ~49 | Metadata only (IDs 11–20, 41–50, 61–70, 89–98) |
| **arXiv** | 33 | Full PDFs; 16 leadership, 17 non-leadership |
| **Root PDFs** | 8 | Core leadership papers manually collected |

### 2.3 Domain Classification

```
Total (108)
├── Leadership (~88)
│   ├── Core PDF in root (8)
│   ├── Leadership PDF in pdfs/ (17)
│   ├── Leadership metadata in meta/ (38)
│   └── Metadata-only leadership (25)
│
└── Non-leadership (20)
    ├── Physics — Transactional Interpretation (3)
    ├── CS — Transactional Memory / Testing / Spectroscopy (12)
    ├── Economics — CBDC Transactional Currency (1)
    └── Test / Statistics (4)
```

### 2.4 Collection Methods

- **Root PDFs**: Manually curated leadership papers (Azhar, Batista-Foguet, Das, Dumdum/Lowe/Avolio, Emam, Indarta, Joo, Ravet-Brown, van Dierendonck)
- **arXiv papers**: API-based retrieval using keyword searches for "leadership," "transformational," "transactional"
- **OpenAlex papers**: API-based retrieval using keyword searches for leadership constructs
- **Crossref papers**: DOI-based metadata collection through Crossref REST API
- **Metadata extraction**: PDF text extraction using PyMuPDF (fitz) stored in `temp/reftext/`

---

## 3. Core Leadership Papers (12 Analyzed; 8 with source text in repo)

> 아래 표는 매핑에 사용된 12편(P001–P012)입니다. 이 중 **저장소에 원문 텍스트가 실재하는 것은 P001–P008 + Dumdum 메타분석(9편)**이며, **P009(MacKenzie 2001)·P010(arXiv_32)·P011(arXiv_34)·P012(arXiv_33)는 원문이 저장소에 없어 인용의 page/section 대조가 불가**합니다(§7·§11.4 참조).

### 3.1 Paper Overview Table

| ID | File | Author(s) | Year | Journal | Theory | Key Traits |
|----|------|-----------|------|---------|--------|------------|
| P001 | Das_2024_LeadershipDevelopment_360Feedback.pdf | Barttanu Kumar Das, Rajini G. | 2024 | Environment and Social Psychology | Leadership Development, Adaptive | T12, T14, T07 |
| P002 | BatistaFoguet_2021_MLQ_ConstructValidity.pdf | Batista-Foguet, Esteve, van Witteloostuijn | 2021 | PLoS ONE | Transformational | T01, T09 |
| P003 | vanDierendonck_2010_ServantLeadershipSurvey.pdf | Dirk van Dierendonck, Inge Nuijten | 2010 | J. Business and Psychology | Servant | T02, T07, T11 |
| P004 | RavetBrown_2024_EntrepreneurialTransformational_Review.pdf | T. Ravet-Brown et al. | 2024 | Review of Managerial Science | Entrepreneurial, Transformational | T03, T13, T14 |
| P005 | Emam_2024_NursingLeadership.pdf | Emam et al. | 2024 | BMC Nursing | Context-Specific | T02, T11, T07 |
| P006 | Azhar_2026_LeadershipCompetencies_Bibliometric.pdf | Azhar, Ayobami | 2026 | Discover Sustainability | Adaptive, Digital | T12, T14, T03, T05 |
| P007 | Joo_2020_CVF_LeadershipComplexity.pdf | Joo Young-joo (최루디아) | 2020 | Korean HRD Research | Strategic | T12, T01, T06 |
| P008 | Indarta_2024_ServantLeadership_SystematicReview.pdf | Yose Indarta et al. | 2024 | J. Scientech R&D | Servant | T02, T07, T11 |
| P009 | paper_105_OpenAlex.pdf | Scott B. MacKenzie, Philip M. Podsakoff, Gregory A. Rich | 2001 | J. Academy of Marketing Science | Transformational, Transactional | T01, T09, T06 |
| P010 | paper_32_arXiv.pdf | Various | 2024 | arXiv preprint | Transformational, Adaptive | T01, T09, T04 |
| P011 | paper_34_arXiv.pdf | Various | 2024 | arXiv preprint | Ethical | T13, T01 |
| P012 | paper_33_arXiv.pdf | Star Dawood Mir et al. | 2024 | arXiv preprint | Context-Specific, Adaptive | T06, T07 |

### 3.2 Detailed Paper Analysis

#### P001 — Das & Rajini (2024): Leadership Development through 360-Degree Multi-Rater Feedback

- **Location**: Root PDF
- **Theories**: Leadership Development, Adaptive
- **Key Findings**:
  - 360-degree feedback provides multi-source insights for leadership development
  - Feedback from peers, subordinates, managers, and customers creates strong ground for behavioral change
  - Process requires sensitivity to hidden conflicts as much as tangible results
- **Trait Mapping**: T12 (Balanced), T14 (Learning Agile), T07 (Coaching)
- **Macro Mapping**: L32 (Self-Awareness/Self-Reflection), L17 (Situational Flexibility), L39 (Talent Development)
- **Micro Labels**: M32-01, M32-02, M17-01, M39-01, M11-01
- **Evidence Location**: pp. 1-3 (Introduction & Literature Review)

#### P002 — Batista-Foguet et al. (2021): MLQ Construct Validity

- **Location**: Root PDF
- **Theories**: Transformational
- **Key Findings**:
  - MLQ-5X construct validity assessed using CTT framework
  - Full-range theory questioned: multidimensional structure shows inconsistencies
  - Original Bass study used PCA with varimax rotation on 104 military officers
  - Formative vs. reflective measurement model debate
- **Trait Mapping**: T01 (Strategic Decisive), T09 (Visionary)
- **Macro Mapping**: L01–L04 (Transformational constructs)
- **Micro Labels**: M01-01 through M04-02
- **Evidence Location**: pp. 1-3 (Introduction & Background)

#### P003 — van Dierendonck & Nuijten (2010): Servant Leadership Survey (SLS)

- **Location**: Root PDF
- **Theories**: Servant
- **Key Findings**:
  - Developed validated 8-dimension Servant Leadership Survey (SLS)
  - 99 items reduced to 30 through EFA and CFA across 8 samples (N=1,571)
  - Dimensions: Empowerment, Accountability, Standing Back, Humility, Authenticity, Courage, Interpersonal Acceptance, Stewardship
  - Strong convergent and discriminant validity demonstrated
- **Trait Mapping**: T02 (Collaborative), T07 (Coaching), T11 (Empathetic)
- **Macro Mapping**: L11, L12, L14, L15, L38, L42, L48
- **Micro Labels**: M11-01 through M48-01 (18 labels)
- **Evidence Location**: pp. 1-5 (scale development, validation samples)

#### P004 — Ravet-Brown et al. (2024): Entrepreneurial vs. Transformational Leadership Review

- **Location**: Root PDF
- **Theories**: Entrepreneurial, Transformational
- **Key Findings**:
  - EL overlaps significantly with TL but is distinct in opportunity-focused, risk-taking behaviors
  - Integration with mainstream leadership literature remains fragmentary
  - TL continues to be used as routine framework for examining EL
  - 46-page comprehensive review of 25 studies
- **Trait Mapping**: T03 (Innovative), T13 (Ethical Courageous), T14 (Learning Agile)
- **Macro Mapping**: L23 (Innovation Opportunity), L26 (Experimentation), L36 (Strategic), L46 (Entrepreneurial)
- **Micro Labels**: M23-01, M23-02, M26-01, M36-01 through M36-04, M46-01, M46-02
- **Evidence Location**: pp. 1-8 (throughout)

#### P005 — Emam et al. (2024): Nursing Leadership

- **Location**: Root PDF
- **Theories**: Context-Specific
- **Key Findings**:
  - Nursing leadership crucial for high-quality healthcare and positive outcomes
  - Many nurses in leadership positions lack formal training
  - Communication and empathy are critical in healthcare leadership
  - True experimental design (treatment 40 / control 40) with follow-up
- **Trait Mapping**: T02 (Collaborative), T11 (Empathetic), T07 (Coaching)
- **Macro Mapping**: L11, L12, L15, L29
- **Micro Labels**: M11-01, M12-01, M12-02, M12-03, M15-01, M15-02, M15-03, M29-01
- **Evidence Location**: pp. 2-3 (Introduction)

#### P006 — Azhar & Ayobami (2026): Leadership Competencies Bibliometric Review

- **Location**: Root PDF
- **Theories**: Adaptive, Digital, Emotional Intelligence
- **Key Findings**:
  - Leadership competencies as multidimensional constructs influencing individual, team, and organizational outcomes
  - Intrapersonal, interpersonal, and cognitive skills are essential
  - Digital transformation and AI are emerging as critical for future leaders
  - 65-year bibliometric analysis (1960–2025)
- **Trait Mapping**: T12 (Balanced), T14 (Learning Agile), T03 (Innovative), T05 (Analytical)
- **Macro Mapping**: L17, L18, L21, L22, L34, L37
- **Micro Labels**: M17-01, M18-01, M18-02, M21-01, M21-02, M22-01, M22-02, M22-03, M34-01, M37-01, M37-02
- **Evidence Location**: pp. 2-5 (Literature Review & Results)

#### P007 — Joo (2020): Competing Values Framework Leadership Complexity

- **Location**: Root PDF
- **Theories**: Strategic
- **Key Findings**:
  - Competing Values Framework (CVF) applied to leadership behavioral complexity
  - VUCA era demands flexible leadership combining multiple roles
  - Korean public organization context validates CVF's cultural applicability
  - CVF identifies 8 leadership roles across 4 quadrants
- **Trait Mapping**: T12 (Balanced), T01 (Strategic Decisive), T06 (Execution Driver)
- **Macro Mapping**: L16, L25, L27, L36, L43, L44, L46, L47
- **Micro Labels**: M16-01, M25-01, M27-01, M27-02, M36-01 through M36-04, M43-01 through M43-03, M44-01, M44-02, M46-01, M46-02, M47-01, M47-02
- **Evidence Location**: pp. 95-105 (Korean public sector CVF validation)

#### P008 — Indarta et al. (2024): Servant Leadership Systematic Review

- **Location**: Root PDF
- **Theories**: Servant
- **Key Findings**:
  - Systematic review of 435 peer-reviewed articles from Scopus (2020–2024)
  - Servant leadership relevance grown significantly due to global challenges (COVID-19, economic uncertainty)
  - Mixed-methods approach combining systematic review with bibliometric analysis
  - PRISMA-guided methodology
- **Trait Mapping**: T02, T07, T11 (same as P003 but with broader scope)
- **Macro Mapping**: L11, L12, L14, L15, L29, L38, L42, L48
- **Micro Labels**: 18 labels (same as P003 coverage)
- **Evidence Location**: pp. 1-3 (Abstract & Methodology)

#### P009 — MacKenzie et al. (2001): TL and Salesperson Performance

- **Location**: `pdfs/paper_105_OpenAlex.pdf`
- **Theories**: Transformational, Transactional
- **Key Findings**:
  - Transformational leader behaviors have stronger direct and indirect relationships with sales performance than transactional behaviors
  - Trust and role ambiguity mediate the leadership-performance relationship
  - Transformational leadership predicts OCB above and beyond transactional leadership
  - Sample of 228 salespeople in 84 retail stores
- **Trait Mapping**: T01, T09, T06
- **Macro Mapping**: L01–L04, L06, L07, L09
- **Micro Labels**: M01-01 through M09-01 (wide coverage)
- **Evidence Location**: pp. 1-5

#### P010 — paper_32_arXiv (2024): TL and Change in Construction

- **Location**: `pdfs/paper_32_arXiv.pdf`
- **Theories**: Transformational, Adaptive
- **Key Findings**:
  - TL influences team members' readiness for change in construction industry
  - Leadership as key driver for organizational change initiatives
  - Empirical study in construction project context
- **Trait Mapping**: T01, T09, T04
- **Macro Mapping**: L01, L05, L19, L20
- **Micro Labels**: M01-01 through M01-04, M05-01 through M05-03, M19-01, M20-01
- **Evidence Location**: pp. 1-2

#### P011 — paper_34_arXiv (2024): Ethical Leadership in AI Era

- **Location**: `pdfs/paper_34_arXiv.pdf`
- **Theories**: Ethical, Authentic
- **Key Findings**:
  - Ethical leadership framework needed for AI era
  - Challenges include algorithmic bias, transparency, and accountability
  - Leaders must balance innovation with ethical considerations
  - AI-specific ethical dimensions beyond traditional frameworks
- **Trait Mapping**: T13, T01
- **Macro Mapping**: L28, L30, L31, L33, L45
- **Micro Labels**: M28-01, M28-02, M30-01, M31-01, M33-01 through M33-05, M45-01, M45-02
- **Evidence Location**: pp. 1-4

#### P012 — Mir et al. (2024): Delegation in Software Management

- **Location**: `pdfs/paper_33_arXiv.pdf`
- **Theories**: Context-Specific, Adaptive
- **Key Findings**:
  - Effective delegation is critical leadership competency in software management
  - Leadership style impacts project outcomes and team satisfaction
  - Domain-specific delegation behaviors
- **Trait Mapping**: T06, T07
- **Macro Mapping**: L10, L39, L08
- **Micro Labels**: M10-01, M10-02, M39-01, M08-01, M08-02
- **Evidence Location**: pp. 1-2

---

## 4. 12 Leadership Theories

### 4.1 Theory Overview

| # | Theory (KR) | Theory (EN) | Founders | Core Papers | Traits |
|---|-------------|-------------|----------|-------------|--------|
| 1 | 변혁적 리더십 | Transformational | Bass, Avolio | P002, P009, P010, P004 | T01, T03, T04, T09 |
| 2 | 서번트 리더십 | Servant | Greenleaf, van Dierendonck | P003, P008 | T02, T07, T11 |
| 3 | 기업가적 리더십 | Entrepreneurial | Renko, Ravet-Brown | P004 | T03, T13, T14 |
| 4 | 윤리적 리더십 | Ethical | Brown, Treviño | P011 | T13, T01 |
| 5 | 적응적/민첩 리더십 | Adaptive & Agile | Heifetz, Yukl, Azhar | P006, P001, P012 | T04, T12, T14 |
| 6 | 양손잡이 리더십 | Ambidextrous | Tushman, O'Reilly | P004, P007 | T03, T12 |
| 7 | 진정성 리더십 | Authentic | Avolio, Walumbwa | P001, P011 | T13, T14 |
| 8 | 감성지능 리더십 | Emotional Intelligence | Goleman, Boyatzis | P006, P003 | T11, T02 |
| 9 | 거래적 리더십 | Transactional | Bass, Avolio | P009 | T01, T06 |
| 10 | 전략적 리더십 | Strategic | Boal, Hooijberg, Joo | P007 | T01, T05, T06, T12 |
| 11 | 디지털/혁신 리더십 | Digital & Innovation | Cortellazzo, Azhar | P006 | T03, T05, T14 |
| 12 | 맥락별 리더십 | Context-Specific | Fiedler, Vroom, Emam | P005, P012 | T02, T07, T11 |

### 4.2 Detailed Theory Descriptions

#### 4.2.1 Transformational Leadership (변혁적 리더십)

**Founders:** Bernard M. Bass, Bruce J. Avolio

**Core Constructs (4 I's):**
- **Idealized Influence (II):** Charisma, role modeling, ethical standards
- **Inspirational Motivation (IM):** Vision articulation, goal setting, meaning creation
- **Intellectual Stimulation (IS):** Creativity encouragement, assumption questioning, innovation
- **Individualized Consideration (IC):** Personal attention, coaching, developmental support

**Evidence Base:**
- MLQ-5X (Avolio, Bass & Jung, 1999): 6 lower-order factors → 3 higher-order factors validated across 14 samples (N=3,786)
- Judge & Piccolo (2004) meta-analysis: ρ=.44 overall validity
- MacKenzie et al. (2001): TL predicts OCB and sales performance beyond transactional leadership
- Dumdum/Lowe/Avolio (2002): Meta-analysis confirming TL→effectiveness relationship

**Trait Mapping:**
| Trait | Connection |
|-------|-----------|
| T01 Strategic Decisive | Goal setting, vision communication (II/IM) |
| T03 Innovative | Intellectual stimulation, creativity (IS) |
| T04 Crisis Manager | Change readiness, adaptive vision (IM/IS) |
| T09 Visionary | Idealized influence, inspirational motivation (II/IM) |

**Macro Labels:** L01 (Vision), L02 (Motivation), L03 (Intellectual Stimulation), L04 (Charisma), L05 (Change)

**Micro Labels:** M01-01 through M05-03 (21 labels)

**Key Evidence Sources:**
| Paper | Pages | Section | Key Finding |
|-------|-------|---------|-------------|
| P002 | 1-3 | Introduction & Background | MLQ construct validity, Bass 1985 origins |
| P009 | 1-2 | Abstract & Introduction | TL > Transactional for sales performance |
| P004 | 1-3 | Abstract & Introduction | TL as baseline framework for EL comparison |

---

#### 4.2.2 Servant Leadership (서번트 리더십)

**Founders:** Robert K. Greenleaf, Dirk van Dierendonck

**Core Constructs (8 Dimensions of SLS):**
1. **Empowerment:** Enabling self-directed decision-making
2. **Accountability:** Holding followers responsible for outcomes
3. **Standing Back:** Prioritizing follower interests
4. **Humility:** Acknowledging limitations and mistakes
5. **Authenticity:** Being genuine and transparent
6. **Courage:** Taking principled stands
7. **Interpersonal Acceptance:** Creating psychological safety
8. **Stewardship:** Taking responsibility for organizational impact

**Evidence Base:**
- van Dierendonck & Nuijten (2010): SLS development with 99→30 items, 8 samples (N=1,571), EFA+CFA
- Indarta et al. (2024): Systematic review of 435 Scopus articles confirming SL's growing relevance

**Trait Mapping:**
| Trait | SLS Dimension Connection |
|-------|-------------------------|
| T02 Collaborative | Empowerment, Interpersonal Acceptance |
| T07 Coaching | Individualized Consideration, Accountability |
| T11 Empathetic | Standing Back, Humility, Interpersonal Acceptance |

**Macro Labels:** L11 (Listening), L12 (Empathy), L14 (Altruism), L15 (Psychological Safety), L29 (Well-being), L38 (Listening/Empathy), L42 (Employee Centric), L48 (Benevolent)

**Micro Labels:** M11-01 through M48-01 (18 labels)

**Key Evidence Sources:**
| Paper | Pages | Section | Key Finding |
|-------|-------|---------|-------------|
| P003 | 1-3 | Abstract & Introduction | SLS development with 8 dimensions |
| P008 | 1-3 | Abstract & Methodology | PRISMA review of 435 Scopus articles |

---

#### 4.2.3 Entrepreneurial Leadership (기업가적 리더십)

**Founders:** Renko et al., Leitch et al., Ravet-Brown et al. (2024)

**Core Constructs:**
- **Opportunity Recognition:** Identifying new business opportunities
- **Risk-Taking:** Willingness to pursue uncertain ventures
- **Innovation:** Creating novel products/processes
- **Vision Communication:** Articulating entrepreneurial vision
- **Resource Leveraging:** Efficiently using limited resources

**Evidence Base:**
- Ravet-Brown et al. (2024): 46-page systematic review of 25 studies concluding EL overlaps significantly with TL but is distinct in opportunity-focused, risk-taking behaviors
- Key concern: EL's integration with mainstream leadership literature remains fragmentary

**Trait Mapping:**
| Trait | EL Connection |
|-------|---------------|
| T03 Innovative | Opportunity recognition, innovation seeking |
| T13 Ethical Courageous | Risk-taking with ethical boundaries |
| T14 Learning Agile | Adaptability, continuous learning |

**Macro Labels:** L23 (Innovation Opportunity), L26 (Experimentation), L36 (Strategic), L46 (Entrepreneurial)

**Micro Labels:** M23-01, M23-02, M26-01, M36-01 through M36-04, M46-01, M46-02

---

#### 4.2.4 Ethical Leadership (윤리적 리더십)

**Founders:** Michael Brown, Linda Treviño

**Core Constructs:**
- **Moral Person:** Personal integrity and ethical character
- **Moral Manager:** Actively promoting ethical conduct
- **Fairness:** Equitable treatment of followers
- **Integrity:** Consistency between words and actions
- **Ethical Decision-Making:** Principled decisions
- **AI Ethics:** Algorithmic transparency and accountability (emerging)

**Evidence Base:**
- Brown, Treviño & Harrison (2005): Define ethical leadership as "demonstration of normatively appropriate conduct through personal actions and interpersonal relationships"
- P011 (paper_34_arXiv): AI-specific ethical leadership challenges including bias, transparency, accountability

**Trait Mapping:**
| Trait | Ethical Connection |
|-------|-------------------|
| T13 Ethical Courageous | Moral courage, integrity, ethical decision-making |
| T01 Strategic Decisive | Ethical considerations in decision-making |

**Macro Labels:** L28 (Transparency), L30 (Consistency), L31 (Inclusivity), L33 (Moral Courage), L45 (CSR)

**Micro Labels:** M28-01, 02, M30-01, M31-01, M33-01 through M33-05, M45-01, 02

---

#### 4.2.5 Adaptive & Agile Leadership (적응적/민첩 리더십)

**Founders:** Ronald Heifetz, Gary Yukl, Azhar & Ayobami (2026)

**Core Constructs:**
- **Situational Flexibility:** Adapting style to context
- **VUCA Readiness:** Navigating volatility, uncertainty, complexity, ambiguity
- **Change Management:** Leading organizational transformation
- **Behavioral Complexity:** Switching between competing leadership roles
- **Continuous Learning:** Constantly developing new competencies

**Evidence Base:**
- Azhar & Ayobami (2026): Bibliometric review identifying intrapersonal, interpersonal, and cognitive skills as critical
- Das (2024): 360-degree feedback as tool for adaptive development
- Emam (2024): Adaptive leadership contextualized in healthcare

**Trait Mapping:**
| Trait | Adaptive Connection |
|-------|---------------------|
| T04 Crisis Manager | Crisis response, VUCA readiness |
| T12 Balanced | Behavioral complexity, role switching |
| T14 Learning Agile | Continuous learning, adaptability |

**Macro Labels:** L13 (Resilience), L17 (Flexibility), L18 (Stability in Uncertainty), L19 (Quick Decisions), L20 (Crisis Response), L22 (Failure Acceptance)

**Micro Labels:** M13-01, M17-01, M18-01, M18-02, M19-01, M20-01, M22-01, M22-02, M22-03

---

#### 4.2.6 Ambidextrous Leadership (양손잡이 리더십) — NEW

**Founders:** Michael Tushman, Charles O'Reilly, Wendy K. Smith

**Core Constructs:**
- **Exploration (탐험):** Innovation, experimentation, risk-taking
- **Exploitation (활용):** Efficiency, refinement, execution
- **Contextual Ambidexterity:** Creating organizational context that enables both simultaneously

**Evidence Base:**
- Tushman & O'Reilly's theory: Leaders must balance exploration and exploitation for organizational success
- Ravet-Brown et al. (2024): Confirms exploration/exploitation tension in entrepreneurial leadership
- Joo (2020): CVF demonstrates behavioral complexity enables ambidexterity through role switching

**Trait Mapping:**
| Trait | Ambidextrous Connection |
|-------|------------------------|
| T03 Innovative | Exploration, innovation seeking |
| T12 Balanced | Balancing exploration and exploitation |

**Macro Labels:** L23 (Innovation), L24 (Stability), L26 (Experimentation), L27 (Resource Allocation), L43 (Participation), L46 (Entrepreneurial), L47 (Distributed)

**Micro Labels:** 14 labels

---

#### 4.2.7 Authentic Leadership (진정성 리더십) — NEW

**Founders:** Bruce J. Avolio, Fred O. Walumbwa

**Core Constructs:**
- **Self-Awareness:** Understanding strengths, weaknesses, and values
- **Relational Transparency:** Openness and truthfulness in relationships
- **Internalized Moral Perspective:** Self-regulation guided by internal moral standards
- **Balanced Processing:** Objectively analyzing information before deciding

**Evidence Base:**
- Avolio & Walumbwa's Authentic Leadership Theory identifies 4 core dimensions
- Das (2024): 360-degree feedback linked to self-awareness development
- P011: Ethical leadership literature shows overlap with authentic leadership in transparency

**Trait Mapping:**
| Trait | Authentic Connection |
|-------|---------------------|
| T13 Ethical Courageous | Moral perspective, transparency |
| T14 Learning Agile | Self-awareness, balanced processing |

**Macro Labels:** L28 (Transparency), L30 (Consistency), L32 (Self-Reflection), L41 (Self-Awareness)

**Micro Labels:** M28-01, 02, M30-01, M32-01, 02, M41-01

---

#### 4.2.8 Emotional Intelligence Leadership (감성지능 리더십) — NEW

**Founders:** Daniel Goleman, Richard Boyatzis

**Core Constructs:**
- **Self-Awareness:** Recognizing own emotions and their impact
- **Self-Regulation:** Managing disruptive emotions and impulses
- **Motivation:** Drive to achieve beyond expectations
- **Empathy:** Understanding others' emotional makeup
- **Social Skill:** Proficiency in managing relationships and building networks

**Evidence Base:**
- Goleman (1995): Five-component EI framework
- Azhar & Ayobami (2026): EI identified as emerging leadership competency in VUCA environments
- van Dierendonck (2010): Interpersonal acceptance overlaps between servant leadership and EI

**Trait Mapping:**
| Trait | EI Connection |
|-------|---------------|
| T11 Empathetic (formerly T08) | Empathy, social skill |
| T02 Collaborative | Interpersonal acceptance, relationship management |

**Macro Labels:** L11 (Listening), L12 (Empathy), L15 (Psychological Safety), L38 (Listening/Empathy), L42 (Employee Centric)

**Micro Labels:** M11-01, M12-01, M12-02, M12-03, M14-01, M15-01, M15-02, M15-03

---

#### 4.2.9 Transactional Leadership (거래적 리더십) — NEW

**Founders:** Bernard M. Bass, Bruce J. Avolio

**Core Constructs:**
- **Contingent Reward:** Exchange-based motivation with clear expectations and rewards
- **Management by Exception (Active):** Monitoring deviations and taking corrective action
- **Management by Exception (Passive):** Intervening only when problems become serious

**Evidence Base:**
- MacKenzie, Podsakoff & Rich (2001): Transactional leadership's direct effects on sales performance
- Dumdum, Lowe & Avolio (2002): Meta-analysis confirming transactional leadership as valid predictor

**Trait Mapping:**
| Trait | Transactional Connection |
|-------|------------------------|
| T01 Strategic Decisive | Goal setting, contingent reward expectations |
| T06 Execution Driver | Performance management, exception handling |

**Macro Labels:** L06 (Goal Setting), L07 (Feedback), L08 (Responsibility), L09 (Performance Recognition), L10 (Execution), L40 (Exception Management)

**Micro Labels:** M06-01 through M10-02, M24-01, 02 (9 labels)

---

#### 4.2.10 Strategic Leadership (전략적 리더십)

**Founders:** Robert Boal, Rick Hooijberg, Michael Quinn

**Core Constructs:**
- **Competing Values Framework (CVF):** Four leadership quadrants
- **Behavioral Complexity:** Ability to enact multiple leadership roles
- **Strategic Thinking:** Long-term organizational perspective
- **Resource Allocation:** Strategic deployment of organizational resources

**Evidence Base:**
- Joo (2020): CVF applied to Korean public organizations, validating behavioral complexity theory
- CVF identifies 8 roles across 4 quadrants (Innovator-Broker, Producer-Director, Coordinator-Monitor, Facilitator-Mentor)

**Trait Mapping:**
| Trait | Strategic Connection |
|-------|---------------------|
| T01 Strategic Decisive | Producer-Director roles |
| T05 Analytical | Coordinator-Monitor roles |
| T06 Execution Driver | Producer role |
| T12 Balanced | All CVF quadrants (behavioral complexity) |

**Macro Labels:** L16, L25, L27, L36, L43, L44, L46, L47, L48

**Micro Labels:** 17 labels

---

#### 4.2.11 Digital & Innovation Leadership (디지털/혁신 리더십)

**Founders:** Cortellazzo et al., Azhar & Ayobami (2026)

**Core Constructs:**
- **Digital Mindset:** Embracing technology-driven transformation
- **Data-Driven Decision Making:** Using analytics for decisions
- **AI/Tech Adoption:** Implementing emerging technologies
- **Virtual Team Leadership:** Managing distributed teams

**Evidence Base:**
- Azhar & Ayobami (2026): Digital transformation and AI as emerging critical competencies
- Digital leadership distinct from e-leadership in requiring active technology adoption

**Trait Mapping:**
| Trait | Digital Connection |
|-------|-------------------|
| T03 Innovative | Tech innovation, AI adoption |
| T05 Analytical | Data-driven decisions |
| T14 Learning Agile | Digital learning, continuous adaptation |

**Macro Labels:** L21 (Learning/Digital Agility), L34 (Data-Driven), L35 (Digital Tools), L37 (AI Innovation)

**Micro Labels:** M21-01, 02, M34-01, M35-01, M37-01, 02

---

#### 4.2.12 Context-Specific Leadership (맥락별 리더십)

**Founders:** Fiedler, Vroom, Emam (2024)

**Core Constructs:**
- **Situational Adaptation:** Adjusting style based on context
- **Domain-Specific Competencies:** Industry-specific leadership skills
- **Nursing Leadership:** Communication, empathy, situational awareness in healthcare
- **Software Management:** Delegation-specific competencies

**Evidence Base:**
- Emam (2024): Nursing leadership requires specific competencies in healthcare contexts
- Mir et al. (2024): Effective delegation as critical competency in software management

**Trait Mapping:**
| Trait | Context-Specific Connection |
|-------|---------------------------|
| T02 Collaborative | Healthcare team collaboration |
| T07 Coaching | Domain-specific development |
| T11 Empathetic | Patient-centered care context |

**Macro Labels:** L11 (Listening), L29 (Well-being), L39 (Talent Development), L42 (Employee Centric)

**Micro Labels:** M11-01, 02, M29-01, M39-01, M42-01

---

### 4.3 Theory–Trait Mapping Matrix

| Theory | T01 | T02 | T03 | T04 | T05 | T06 | T07 | T09 | T11 | T12 | T13 | T14 |
|--------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| **Transformational** | ✓ | | ✓ | ✓ | | | | ✓ | | | | |
| **Servant** | | ✓ | | | | | ✓ | | ✓ | | | |
| **Entrepreneurial** | | | ✓ | | | | | | | | ✓ | ✓ |
| **Ethical** | ✓ | | | | | | | | | | ✓ | |
| **Adaptive** | | | | ✓ | | | | | | ✓ | | ✓ |
| **Ambidextrous** | | | ✓ | | | | | | | ✓ | | |
| **Authentic** | | | | | | | | | | | ✓ | ✓ |
| **Emotional Intelligence** | | ✓ | | | | | | | ✓ | | | |
| **Transactional** | ✓ | | | | | ✓ | | | | | | |
| **Strategic** | ✓ | | | | ✓ | ✓ | | | | ✓ | | |
| **Digital** | | | ✓ | | ✓ | | | | | | | ✓ |
| **Context-Specific** | | ✓ | | | | | ✓ | | ✓ | | | |

---

## 5. Trait System (20 Traits)

### 5.1 Positive Traits (12 Active)

| ID | Name (EN) | Name (KR) | Primary Theory | Validation | Evidence Strength |
|----|-----------|-----------|----------------|------------|-----------------|
| T01 | Strategic Decisive Leader | 전략적 결단 리더 | Full-Range (Transactional) | construct_supported | medium |
| T02 | Collaborative Leader | 협업형 리더 | Servant | construct_supported | strong |
| T03 | Innovative Leader | 혁신형 리더 | Transformational (IS) | construct_supported | strong |
| T04 | Crisis Manager | 위기 대응형 리더 | Adaptive | **unverified** | medium |
| T05 | Analytical Leader | 분석형 리더 | Data-Driven | **unverified** | weak |
| T06 | Execution Driver | 실행형 리더 | CVF (Task) | construct_supported | strong |
| T07 | Coaching Leader | 코칭형 리더 | Transformational (IC) | construct_supported | strong |
| T09 | Visionary Leader | 비전 제시형 리더 | Transformational (II/IM) | construct_supported | strong |
| T11 | Empathetic Leader | 공감형 리더 | Servant | construct_supported | strong |
| T12 | Balanced Leader | 균형형 리더 | CVF (Behavioral Complexity) | partially_supported | medium |
| T13 | Ethical Courageous Leader | 윤리적 용기형 리더 | Ethical + Servant | construct_supported | strong |
| T14 | Learning Agile Leader | 학습 민첩형 리더 | Adaptive + Digital | partially_supported | medium |

### 5.2 Trait Detail: Required / Optional / Forbidden Labels

#### T01 — Strategic Decisive Leader
- **Definition:** 목표를 설정하고 신속·명확하게 의사결정하는 결단형 리더
- **Required:** M06-01 (Goal Setting), M19-01 (Quick Decision-Making)
- **Optional:** M01-01, M10-01, M01-02, M06-02, M01-03
- **Hard Forbidden:** N08-01, N08-02 (Responsibility Evasion), N14-01 (Selfish Behavior)
- **Soft Forbidden:** N19-01 (Arbitrary Decision, penalty 0.4)
- **Context Weights:** crisis: 1.3, normal: 1.0, innovation: 1.1
- **Hybrid Eligible:** Yes (k_trait: 1.2)
- **Evidence Papers:** P002, P009, P007

#### T02 — Collaborative Leader
- **Definition:** 팀워크와 소통 중심의 협력형 리더
- **Required:** M11-01 (Active Listening), M15-01 (Psychological Safety), M15-03 (Opinion Seeking)
- **Optional:** M11-02, M12-01, M12-02, M15-02, M15-04, M15-05, M15-06, M14-02
- **Hard Forbidden:** N11-01, N11-02 (Listening Rejection), N15-03 (Public Blame), N04-02 (Charisma Abuse)
- **Soft Forbidden:** N19-01 (Arbitrary Decision, penalty 0.3)
- **Evidence Papers:** P003, P005, P008

#### T03 — Innovative Leader
- **Definition:** 창의성과 혁신을 촉진하고 새로운 기회를 탐색하는 혁신형 리더
- **Required:** M03-03 (New Approach Encouragement), M05-02 (Change Implementation), M23-01 (Innovation Idea Discovery)
- **Optional:** M03-01, M03-02, M23-02
- **Hard Forbidden:** N03-01, N03-02, N03-03, N03-04 (Intellectual Suppression)
- **Evidence Papers:** P004, P006

#### T04 — Crisis Manager
- **Definition:** 위기 상황에서 신속하고 효과적으로 대응하는 리더
- **Required:** M19-01 (Quick Decision), M10-01 (Execution), M20-01 (Crisis Response)
- **Optional:** M18-01, M17-01
- **Evidence Papers:** P010, P006

#### T05 — Analytical Leader
- **Definition:** 데이터와 논리를 기반으로 의사결정하는 분석형 리더
- **Required:** M34-01 (Data-Driven Decision Making)
- **Optional:** M08-02, M18-02
- **Evidence Papers:** P006, P007

#### T06 — Execution Driver
- **Definition:** 목표 달성과 실행을 중시하는 실행형 리더
- **Required:** M10-01 (Execution), M06-01 (Goal Setting)
- **Optional:** M08-01, M24-01, M24-02
- **Hard Forbidden:** N06-01, N08-01, N08-02
- **Evidence Papers:** P007, P009

#### T07 — Coaching Leader
- **Definition:** 구성원의 성장과 발전을 지원하는 코칭형 리더
- **Required:** M02-02 (Growth Opportunity), M39-01 (Talent Development)
- **Optional:** M02-03, M07-01, M07-02
- **Evidence Papers:** P003, P005, P012

#### T09 — Visionary Leader
- **Definition:** 명확한 비전을 제시하고 공유하여 팀을 영감하는 비전형 리더
- **Required:** M01-01 (Clear Vision), M01-04 (Vision Sharing)
- **Optional:** M01-02, M01-03, M04-01, M04-02
- **Hard Forbidden:** N01-01, N01-02, N01-03 (Vision Distortion)
- **Evidence Papers:** P002, P009, P010

#### T11 — Empathetic Leader
- **Definition:** 구성원의 감정과 관점을 이해하고 배려하는 공감형 리더
- **Required:** M12-01 (Empathy Expression), M15-02 (Consideration)
- **Optional:** M11-01, M11-02, M12-02, M12-03, M15-01
- **Hard Forbidden:** N12-01, N12-02, N12-03 (Lack of Empathy)
- **Evidence Papers:** P003, P005, P008

#### T12 — Balanced Leader
- **Definition:** 다양한 리더십 역할을 상황에 맞게 균형 있게 수행하는 균형형 리더
- **Required:** M17-01 (Situational Flexibility), M27-01 (Strategic Resource Allocation)
- **Optional:** M18-01, M18-02, M27-02
- **Evidence Papers:** P006, P007, P001

#### T13 — Ethical Courageous Leader
- **Definition:** 윤리적 원칙을 수호하고 도덕적 용기를 발휘하는 리더
- **Required:** M33-01 (Moral Principles), M30-01 (Consistency)
- **Optional:** M33-02, M33-03, M33-04, M33-05, M28-01, M28-02
- **Hard Forbidden:** N28-01 (Transparency Violation), N30-01 (Inconsistency), N33-01, N33-02 (Lack of Moral Courage)
- **Evidence Papers:** P011, P004

#### T14 — Learning Agile Leader
- **Definition:** 지속적 학습과 변화에 민첩하게 대응하는 적응형 리더
- **Required:** M21-01 (Continuous Learning), M22-01 (Innovation Opportunity Seeking)
- **Optional:** M21-02, M22-02, M22-03, M26-01
- **Hard Forbidden:** N38-01, N38-02, N38-03 (Laissez-Faire / Neglect)
- **Evidence Papers:** P006, P004, P001

### 5.3 Risk (Negative) Traits (6)

| ID | Name | Primary Theory | Validation | Evidence Strength |
|----|------|---------------|------------|-----------------|
| T101 | Risk: Avoidant (회피형) | Laissez-Faire / Passive | construct_supported | strong |
| T102 | Risk: Authoritarian (권위주의) | Authoritarian Leadership | partially_supported | weak |
| T103 | Risk: Integrity Violation (정직성 위반) | Authentic (inverse) | partially_supported | medium |
| T104 | Risk: Narcissistic (자기애적) | Dark Triad | construct_supported | strong |
| T105 | Risk: Manipulative (조작적) | Dark Triad (Machiavellianism) | construct_supported | strong |
| T106 | Risk: Volatile (기복형) | Hogan Development Survey (HDS) | construct_supported | strong |

### 5.4 Removed / Inactive Traits

| ID | Name | Reason | Date |
|----|------|--------|------|
| T08 | Emotional Intelligence Leader | Merged into T11 (Empathetic) — discriminant validity issue | 2026-06-24 |
| T10 | Strategic Execution | Defined in JSON but no theory mapping; hybrid rules used instead | Inactive |

---

## 6. Micro Label Inventory (178 Labels)

### 6.1 Positive Micro Labels (98 Labels)

The 98 positive micro labels are organized under 48 macro labels (L01–L48). Key categories:

#### Transformational Group (L01–L05)
| Macro | Name | Labels | Count |
|-------|------|--------|-------|
| L01 | 비전 제시 및 방향 설정 | M01-01~04 | 4 |
| L02 | 동기부여 및 성장 지원 | M02-01~04 | 4 |
| L03 | 지적 자극 | M03-01~03 | 3 |
| L04 | 카리스마적 영향력 | M04-01~02 | 2 |
| L05 | 변화 주도 | M05-01~04 | 4 |

#### Performance & Responsibility Group (L06–L10)
| Macro | Name | Labels | Count |
|-------|------|--------|-------|
| L06 | 목표 설정 및 기대치 명확화 | M06-01~02 | 2 |
| L07 | 성과 기반 피드백 | M07-01~02 | 2 |
| L08 | 책임 및 원칙 준수 | M08-01~02 | 2 |
| L09 | 공정한 성과 인정 | M09-01 | 1 |
| L10 | 실행력 및 완수 | M10-01~02 | 2 |

#### Servant & Empathetic Group (L11–L15)
| Macro | Name | Labels | Count |
|-------|------|--------|-------|
| L11 | 적극적 경청 | M11-01~02 | 2 |
| L12 | 공감 및 감정적 배려 | M12-01~03 | 3 |
| L13 | 회복력 리더십 | M13-01 | 1 |
| L14 | 이타적 행동 및 희생 | M14-01~02 | 2 |
| L15 | 심리적 안전감 조성 | M15-01~06 | 6 |

#### Adaptive & Agile Group (L17–L22)
| Macro | Name | Labels | Count |
|-------|------|--------|-------|
| L17 | 상황적 유연성 | M17-01~02 | 2 |
| L18 | 불확실성 속 안정감 제공 | M18-01~02 | 2 |
| L19 | 신속한 의사결정 | M19-01~02 | 2 |
| L20 | 위기 대응 및 문제 해결 | M20-01~02 | 2 |
| L21 | 학습 및 디지털 민첩성 | M21-01~02 | 2 |
| L22 | 실패 수용 및 회복 | M22-01~03 | 3 |

#### Ambidextrous & Entrepreneurial Group (L23–L27)
| Macro | Name | Labels | Count |
|-------|------|--------|-------|
| L23 | 혁신 기회 탐색 | M23-01~02 | 2 |
| L24 | 운영 안정성 유지 | M24-01~02 | 2 |
| L25 | 글로벌 리더십 | M25-01 | 1 |
| L26 | 실험 및 도전 장려 | M26-01~02 | 2 |
| L27 | 전략적 자원 배분 | M27-01~02 | 2 |

#### Ethical & Authentic Group (L28–L34)
| Macro | Name | Labels | Count |
|-------|------|--------|-------|
| L28 | 투명한 소통 | M28-01~02 | 2 |
| L29 | 팀 웰빙 | M29-01 | 1 |
| L30 | 언행 일치 및 일관성 | M30-01~02 | 2 |
| L31 | 포용성 및 다양성 존중 | M31-01~02 | 2 |
| L32 | 자기인식 및 자기성찰 | M32-01~02 | 2 |
| L33 | 도덕적 용기 | M33-01~05 | 5 |
| L34 | 데이터 기반 의사결정 | M34-01~02 | 2 |

#### Digital & Innovation Group (L35–L37)
| Macro | Name | Labels | Count |
|-------|------|--------|-------|
| L35 | 디지털 도구 활용 및 자동화 | M35-01~02 | 2 |
| L36 | 전략적 리더십 | M36-01~04 | 4 |
| L37 | AI 및 기술 기반 혁신 | M37-01~02 | 2 |

#### Other Macro Labels (L38–L48)
- L38 경청과 공감 (M38-01~02)
- L39 인재 육성 (M39-01~02)
- L40 예외 관리 (M40-01~02)
- L41 자기인식 (M41-01~02)
- L42 직원 중심 (M42-01)
- L43 참여와 조정 (M43-01~03)
- L44 전략적 영향 (M44-01~02)
- L45 CSR 리더십 (M45-01~02)
- L46 기업가적 리더십 (M46-01~02)
- L47 분산 리더십 (M47-01~02)
- L48 자애적 리더십 (M48-01)

### 6.2 Negative Micro Labels (80 Labels)

Organized under 32 negative macro labels (N01–N43):

| Macro | Name | Labels | Associated Risk Traits |
|-------|------|--------|----------------------|
| N01 | 비전 왜곡 | N01-01~03 | T102, T105 |
| N02 | 동기 조작 | N02-01~03 | T105 |
| N03 | 지적 억압 | N03-01~04 | T102 |
| N04 | 카리스마 악용 | N04-01~02 | T104, T105 |
| N05 | 변화 강요 | N05-01~04 | T102 |
| N06 | 목표 모호화 | N06-01~03 | T101 |
| N07 | 성과 기반 비난 | N07-01~02 | T105 |
| N08 | 책임 전가 | N08-01~02 | T101, T106 |
| N11 | 경청 거부 | N11-01~02 | T102 |
| N12 | 공감 결여 | N12-01~03 | T104 |
| N14 | 이기적 행동 | N14-01~02 | T104 |
| N15 | 심리적 안전 파괴 | N15-01~07 | T102, T105 |
| N28 | 투명성 위반 | N28-01~02 | T103 |
| N30 | 언행 불일치 | N30-01~02 | T103 |
| N33 | 도덕적 용기 결여 | N33-01~02 | T101, T103 |
| N38 | 방임형 리더십 | N38-01~03 | T101 |
| N39 | 독성 리더십 | N39-01~04 | T105 |
| N42 | 권위주의 | N42-01 | T102 |
| N43 | 사회적 무책임 | N43-01 | T103 |

---

## 7. Label Evidence Mapping

### 7.1 Coverage

The `label_evidence_map.json` currently provides academic evidence citations for **30 micro labels**, each with:
- Paper ID (P001–P012)
- File name
- Page numbers
- Section reference
- Evidence note

### 7.2 Sample Evidence Entry

```json
"M01-01": {
  "label_name": "명확한 비전 제시",
  "macro": "L01",
  "macro_name": "비전 제시 및 방향 설정",
  "traits": ["T01", "T09"],
  "theory": "transformational",
  "evidence": [
    {
      "paper_id": "P002",
      "paper": "BatistaFoguet_2021_MLQ_ConstructValidity.pdf",
      "pages": "1-3",
      "section": "MLQ Idealized Influence dimension",
      "note": "MLQ measures vision articulation as core of idealized influence (Bass & Avolio Full Range Model)"
    },
    {
      "paper_id": "P009",
      "paper": "MacKenzie_2001_TransformationalTransactional_SalesPerformance.pdf",
      "pages": "1-2",
      "section": "Abstract & Introduction",
      "note": "Transformational leadership includes communicating compelling vision"
    }
  ]
}
```

### 7.3 Labels with Evidence (Complete List)

| Label | Paper(s) | Page(s) |
|-------|----------|---------|
| M01-01 (Clear Vision) | P002, P009 | 1-3, 1-2 |
| M01-02 (Long-term Direction) | P002 | 2-4 |
| M02-01 (Intrinsic Motivation) | P003 | 2-4 |
| M02-02 (Growth Opportunity) | P003, P005 | 2-4, 2-3 |
| M03-01 (Creative Thinking) | P002, P004 | 1-2, 3-5 |
| M04-01 (Charismatic Inspiration) | P002 | 1-3 |
| M05-02 (Change Implementation) | P010 | 1-2 |
| M06-01 (Goal Setting) | P009 | 3-5 |
| M10-01 (Quick Execution) | P009 | 3-5 |
| M11-01 (Active Listening) | P003, P005 | 4-6, 2-3 |
| M12-01 (Empathy Expression) | P003, P005 | 2-4, 2-3 |
| M14-01 (Others First) | P003 | 3-5 |
| M15-01 (Psychological Safety) | P003 | 3-5 |
| M15-03 (Opinion Seeking) | P003 | 4-6 |
| M17-01 (Situational Flexibility) | P006, P007 | 2-4, 95-100 |
| M18-02 (Data Diagnosis) | P006 | 3-5 |
| M19-01 (Quick Decision) | P010, P006 | 1-2, 3-4 |
| M20-01 (Crisis Response) | P010 | 1-2 |
| M21-01 (Continuous Learning) | P006 | 2-5 |
| M22-01 (Failure Acceptance) | P006 | 3-5 |
| M23-01 (Innovation Discovery) | P004 | 3-6 |
| M26-01 (Experimentation) | P004 | 4-7 |
| M27-01 (Strategic Allocation) | P007 | 100-105 |
| M28-01 (Transparency) | P011 | 1-3 |
| M30-01 (Consistency) | P011 | 2-4 |
| M33-01 (Moral Principles) | P011 | 1-3 |
| M34-01 (Data-Driven Decision) | P006 | 3-5 |
| M36-01 (Strategic Thinking) | P007 | 95-100 |
| M39-01 (Talent Development) | P012 | 1-2 |
| M44-01 (Strategic Influence) | P007 | 100-105 |
| M46-01 (Entrepreneurial Opportunity) | P004 | 5-8 |

---

## 8. Negative Trait & Label Analysis

### 8.1 Negative Trait ↔ Label Mapping

| Negative Macro | Negative Labels | Risk Trait | Theory | Evidence Papers |
|---------------|----------------|------------|--------|----------------|
| N01 (Vision Distortion) | N01-01~03 | T102, T105 | Transformational_Negative | P009 |
| N02 (Motivation Manipulation) | N02-01~03 | T105 | Transformational_Negative | P009 |
| N03 (Intellectual Suppression) | N03-01~04 | T102 | Transformational_Negative | P002 |
| N04 (Charisma Abuse) | N04-01~02 | T104, T105 | Transformational_Negative | P009 |
| N05 (Forced Change) | N05-01~04 | T102 | Transformational_Negative | P010 |
| N06 (Goal Ambiguity) | N06-01~03 | T101 | Transactional_Negative | P009 |
| N07 (Performance Blame) | N07-01~02 | T105 | Transactional_Negative | P009 |
| N08 (Responsibility Evasion) | N08-01~02 | T101, T106 | Transactional_Negative | P009 |
| N11 (Listening Rejection) | N11-01~02 | T102 | Servant_Negative | P003, P005 |
| N12 (Lack of Empathy) | N12-01~03 | T104 | Servant_Negative | P003, P005 |
| N14 (Selfish Behavior) | N14-01~02 | T104 | Servant_Negative | P003 |
| N15 (Psychological Safety Destruction) | N15-01~07 | T102, T105 | Servant_Negative | P003, P008 |
| N28 (Transparency Violation) | N28-01~02 | T103 | Ethical_Negative | P011 |
| N30 (Inconsistency) | N30-01~02 | T103 | Ethical_Negative | P011 |
| N33 (Lack of Moral Courage) | N33-01~02 | T101, T103 | Ethical_Negative | P011 |
| N38 (Laissez-Faire) | N38-01~03 | T101 | Adaptive_Negative | P006 |
| N39 (Toxic Leadership) | N39-01~04 | T105 | Servant_Negative | P003 |
| N42 (Authoritarianism) | N42-01 | T102 | Strategic_Negative | P007 |
| N43 (Social Irresponsibility) | N43-01 | T103 | Ethical_Negative | P011 |

### 8.2 Evidence Strength Gap

**Key Issue:** The risk traits T102 (Authoritarian), T103 (Integrity Violation), T104 (Narcissistic), T105 (Manipulative), and T106 (Volatile) rely on foundational external references (Paulhus & Williams 2002, Hogan & Hogan 2001) that are **not included in the ref data folder**. Direct empirical evidence from the 18 core papers is strongest for:
- T101 (Avoidant) — supported by MLQ literature (P002)
- T105 (Manipulative) — supported by servant/transactional reverse indicators (P003, P009)
- T104 (Narcissistic) — supported indirectly by charisma abuse indicators (P009)

**Recommendation:** Secure full-text PDFs for Paulhus & Williams (2002), Rosenthal & Pittinsky (2006), and Hogan & Hogan (2001) to strengthen the negative trait evidence base.

---

## 9. Non-Leadership Paper Separation

### 9.1 Rationale

20 papers in the metadata were classified under `domain=leadership` due to containing the keyword "transactional." However, these papers belong to entirely different academic domains:

- **Transactional Interpretation** (physics) — quantum mechanics interpretation by Cramer, Kastner
- **Transactional Memory** (computer science) — concurrency control mechanism for shared-memory systems
- **Transactional Currency** (economics) — CBDC money demand models
- **Transaction Analysis** (test/statistics) — statistical hypothesis testing

### 9.2 Separation Results

| Source Folder | Non-Leadership Files | Moved To |
|---------------|---------------------|----------|
| `pdfs/` | paper_3,4,5,6,7,8,9,10 (CS/testing) | `non_leadership/computer_science/` |
| `pdfs/` | paper_81,82,83,87 (CS/TM) | `non_leadership/computer_science/` |
| `pdfs/` | paper_84,86,88 (physics) | `non_leadership/physics/` |
| `pdfs/` | paper_85 (econ) | `non_leadership/economics/` |
| `meta/` | paper_11~20 (CrossRef test) | `non_leadership/meta_non_leadership/` |
| `meta/` | paper_24 (Holm statistics) | `non_leadership/meta_non_leadership/` |

### 9.3 File Inventory

| Subfolder | Files | Reason |
|-----------|-------|--------|
| `physics/` | 3 PDFs (84, 86, 88) | Quantum "transactional interpretation" — unrelated to leadership |
| `computer_science/` | 12 PDFs (3–10, 81–83, 87) | Transactional memory, mutation testing, spectroscopy, software testing |
| `economics/` | 1 PDF (85) | CBDC transactional money demand — monetary economics |
| `meta_non_leadership/` | 11 TXT files (11–20, 24) | Test CrossRef records + Holm-Bonferroni statistical method |

---

## 10. Folder Structure & Change History

### 10.1 Current Folder Structure (2026-07-01 갱신 — 정리 후 실측)

> 아래는 2026-06-30 폴더 정리 **이후 저장소에 실재하는 구조**입니다.
> 정리 이전 `ref data/` 워크스페이스(metadata.csv, consolidated_summary.*, pdfs/, meta/, theory/, non_leadership/ 등)는 아래 "정리 이전 구조(이력)"에 이력으로만 남기며, 현재는 존재하지 않습니다.

```
research/                                              [연구 참고자료 — 신설]
├── papers/                                            [핵심 리더십 논문 원문 텍스트 — 9개]
│   ├── 596-Article Text-...txt                        # P008 Indarta 2024 (Servant SR)
│   ├── DumdumLoweAvolio.txt                           # R01 Dumdum/Lowe/Avolio 메타분석
│   ├── KCI_FI002613507.txt                            # P007 최루디아(Joo) 2020 CVF
│   ├── LeadershipDevelopment.txt                      # P001 Das 2024 360도
│   ├── journal.pone.0254329.txt                       # P002 Batista-Foguet 2021 MLQ
│   ├── s10869-010-9194-1.txt                          # P003 van Dierendonck 2010 SLS
│   ├── s11846-023-00649-6.txt                         # P004 Ravet-Brown 2024 EL
│   ├── s12912-024-02395-w.txt                         # P005 Emam 2024 Nursing
│   └── s43621-026-02809-6.txt                         # P006 Azhar 2026 Bibliometric
├── surveys/                                           [리더십 서베이 도구]
│   └── vanDierendonck_2010_ServantLeadershipSurvey.pdf
└── evidence_mapping/                                  [라벨-증거 논문 매핑]
    └── label_evidence_map.json                        [31개 긍정 라벨 근거]

docs/archive/                                          [구 설계문서 아카이브]
├── leadership_catalog.md · leadership_trait_system.md
├── leadership_evidence_validation_report.md · leadership_validation_ledger.md
├── CHANGELOG_leadership.md · IMPROVEMENT_GUIDE.md · RAG_PLAN.md · architecture.md
└── scripts/ (benchmark.py, build_leadership_catalog.py, add_past_tense_exclusion.py)
```

<details>
<summary><b>정리 이전 구조(이력) — 현재 저장소에 부재</b></summary>

```
ref data/                                              [정리 전 워크스페이스, 2026-06-26]
├── GUIDE.md / history.md / index.md / readme.md
├── consolidated_summary.json / consolidated_summary.md
├── metadata.csv                                       [108편 마스터 메타데이터]
├── *.pdf (9 files)
├── non_leadership/ (physics 3 / computer_science 12 / economics 1 / meta 11)
├── pdfs/ (17) · meta/ (38) · theory/ (9 folders)
└── trait_mapping/label_evidence_map.json
```
</details>

### 10.2 Change Log Summary

| Date | Change Type | Description | Theories | Traits | Labels |
|------|-------------|-------------|----------|--------|--------|
| 2026-06-25 | Initial | 폴더 구조 생성, index.md/readme.md 작성, consolidated_summary.json 생성 | 8 | 20 | 178 |
| 2026-06-25 | Initial | theory/ 9개 폴더 생성, label_evidence_map.json 생성 (15 labels) | 8 | 20 | 178 |
| 2026-06-26 | Restructure | non_leadership/ 생성, 20편 비관련 논문 분리 | 8 | 20 | 178 |
| 2026-06-26 | Documentation | GUIDE.md 생성 (종합 참조 지침서) | 8 | 20 | 178 |
| 2026-06-26 | Documentation | history.md 생성 (변경 로그) | 8 | 20 | 178 |
| 2026-06-26 | Data Expansion | 이론 8→12개 확장 (+Ambidextrous/Authentic/EI/Transactional) | **12** | 20 | 178 |
| 2026-06-26 | Documentation | consolidated_summary.md 4개 신규 섹션 추가, 번호 재조정 | 12 | 20 | 178 |
| 2026-06-26 | Data Expansion | label_evidence_map.json 15→30개 라벨 근거로 확장 | 12 | 20 | 178 |
| 2026-06-26 | Documentation | index.md/readme.md 비관련 논문 경로 변경, 구조 트리 업데이트 | 12 | 20 | 178 |

---

## 11. Key Issues & Improvement Recommendations

### 11.1 Discriminant Validity (판별타당도) Issues

Based on detailed analysis from `leadership_evidence_validation_report.md`:

> ⚠️ **정합성 주의(2026-07-01):** 아래 표는 구 trait 구성 기준입니다. 현재 `data/traits/trait_definitions.json` 실측에서는 T01↔T09가 M01-01을 **공유하지 않으며**(T01 required=M06-01,M19-01 / T09=M01-01,M01-04), T02↔T11도 M15-01을 공유하지 않습니다. **실제 공유 required는 M19-01(T01/T04/T06)·M10-01(T04/T06)뿐**입니다. 단일 진실원천은 JSON이며, 상세는 `docs/leadership_validation_ledger.md` §4(A5) 참조.

**Problem:** Multiple positive traits share the same required micro labels, making behavioral distinction difficult.

| Trait Pair | Shared Required Label(s) | Severity |
|------------|-------------------------|----------|
| **T01 ↔ T09** | M01-01 (Clear Vision) | High |
| **T01 ↔ T04 ↔ T06** | M10-01 (Execution), M19-01 (Quick Decision) | High |
| **T02 ↔ T11** | M15-01 (Psychological Safety) | Medium |
| **T08 ↔ T11** | M12-01 (Empathy), M14-01 (Others First) | **Resolved** (T08→T11 merge) |

**Recommendations:**
1. (a) Demote shared labels from `required` to `optional` in one of the affected traits
2. (b) Assign at least one exclusive distinguishing label per trait pair
3. (c) Consider merging T01/T04/T06 into a single "Execution-Oriented" trait

### 11.2 Missing Trait Theory Mapping

| Trait | Issue | Recommendation |
|-------|-------|---------------|
| T04 Crisis Manager | Unverified; relies only on P010 (arXiv) and P006 (indirect) | Secure dedicated crisis/adaptive leadership paper (e.g., Heifetz primary source) |
| T05 Analytical Leader | Unverified; only M34-01 required with weak evidence | Add data-driven decision-making literature |
| T10 Strategic Execution | Defined in `trait_definitions.json` but no theory mapping | Either activate with theory mapping or officially deprecate |

### 11.3 Evidence Strength Imbalance

| Trait Group | Evidence Strength | Gap |
|-------------|------------------|-----|
| Transformational traits (T01, T03, T09) | Strong | Well-supported by MLQ literature |
| Servant traits (T02, T07, T11) | Strong | SLS 8-dimension validated scale |
| Risk traits (T104–T106) | Strong (external) | **Source papers not in ref data** |
| Adaptive traits (T04, T12, T14) | Medium–Weak | Need primary source papers |

### 11.4 Ref Data Gaps

**Missing primary sources** (needed for negative trait validation):
- Paulhus & Williams (2002) — Dark Triad
- Rosenthal & Pittinsky (2006) — Narcissistic Leadership
- Hogan & Hogan (2001) — HDS Derailers
- Goleman (1995) — Emotional Intelligence
- Heifetz (1994) — Adaptive Leadership primary text

### 11.5 Single-Source Bias

The system currently infers traits from single-source text. Academic literature (Choi 2020, Das 2024, Emam 2024) suggests multi-rater feedback significantly improves validity.

**Recommendation:** For real-world data labeling, use multi-source texts (manager, peer, subordinate perspectives) where possible and report Cohen's κ inter-rater agreement.

---

## 12. System Integration (Vector DB Pipeline)

### 12.1 Data Flow

```
[Academic Research]
research/papers/ (원문 텍스트 9편)
research/evidence_mapping/label_evidence_map.json
        │
        ▼
[Label Definitions]
dataset/ori/positive_micro_labels_enhanced.json (98 labels)
dataset/ori/negative_micro_labels_enhanced.json (80 labels)
        │
        ▼
[Vector DB Construction]
python build_vector_db.py
  ├── KoE5 embedding model (768-dimensional)
  ├── FAISS index creation (178 vectors)
  ├── Test queries (T04-B, T105-A sample tests)
  └── Output: data/vectors/label_vectors.faiss + metadata.json
        │
        ▼
[Analysis Engine]
app.py (Flask web server)
  ├── POST /api/analyze (Trait inference endpoint)
  ├── Edit endpoints for labels/traits
  └── Test result viewer
        │
        ▼
[Pattern Engine]
For each text input:
  1. Extract micro labels from text (Vector DB similarity search)
  2. Score each trait based on required/optional label matches
  3. Apply hard_forbidden penalties (instant disqualification)
  4. Apply soft_forbidden penalties (reduced score)
  5. Apply context_weight multipliers (crisis=1.3, innovation=1.1)
  6. Apply hybrid_eligible cross-trait combination rules
  7. Return top traits with confidence scores
```

### 12.2 Key System Files

| File | Location | Purpose |
|------|----------|---------|
| `app.py` | Root | Flask server (API + Web UI) |
| `build_vector_db.py` | Root | FAISS index builder |
| `trait_definitions.json` | `data/traits/` | 18 trait definitions with rules |
| `positive_micro_labels_enhanced.json` | `dataset/ori/` | 98 positive label definitions |
| `negative_micro_labels_enhanced.json` | `dataset/ori/` | 80 negative label definitions |
| `training_data_all_labels.json` | `dataset/ori/` | 12,460 training samples |
| `label_vectors.faiss` | `data/vectors/` | 178 FAISS vectors |
| `metadata.json` | `data/vectors/` | Vector metadata |

### 12.3 Training Data Specifications

| Specification | Value |
|---------------|-------|
| Total samples | 12,460 |
| Samples per label | 70 (50 clean + 20 hard negative) |
| Label count | 178 |
| Sentence length | 20–120 characters |
| Duplicates | 0 |
| Style distribution | 4 styles (direct_speech, indirect_report, scene_description, euphemism) |
| Placeholders | Forbidden (~, [content], {content}) |
| Hard negative requirement | Surface-level similarity but violates `not_when` condition |

---

## 13. External Evidence Registry

### 13.1 Reference Papers (R01–R09: In Ref Data)

| ID | Citation | Type | File |
|----|----------|------|------|
| R01 | Dumdum, U. R., Lowe, K. B., & Avolio, B. J. (2002) | Meta-analysis | Dumdum_Unknown_LoweAvolio_TransformationalLeadership.doc |
| R02 | Batista-Foguet, J. M., Esteve, M., & van Witteloostuijn, A. (2021) | Measurement validation | BatistaFoguet_2021_MLQ_ConstructValidity.pdf |
| R03 | van Dierendonck, D., & Nuijten, I. (2010) | Scale development | vanDierendonck_2010_ServantLeadershipSurvey.pdf |
| R04 | Indarta, Y., et al. (2024) | Systematic review | Indarta_2024_ServantLeadership_SystematicReview.pdf |
| R05 | 최루디아 (2020) | Empirical multi-rater | Joo_2020_CVF_LeadershipComplexity.pdf |
| R06 | Das, B. K., & Rajini, G. (2024) | Intervention case | Das_2024_LeadershipDevelopment_360Feedback.pdf |
| R07 | Emam, S. M., et al. (2024) | True experiment | Emam_2024_NursingLeadership.pdf |
| R08 | Soomro et al. (2024) | Systematic review | RavetBrown_2024_EntrepreneurialTransformational_Review.pdf |
| R09 | Azhar, Z., & Ayobami, A. (2026) | Bibliometric | Azhar_2026_LeadershipCompetencies_Bibliometric.pdf |

### 13.2 External Sources (X01–X05: Not in Ref Data)

| ID | Citation | Type | Relevance |
|----|----------|------|-----------|
| X01 | Bass, B. M. (1985). *Leadership and performance beyond expectations*. | Foundational theory | Full-Range Leadership Model origin |
| X02 | Paulhus, D. L., & Williams, K. M. (2002). "The Dark Triad of personality." *J. Research in Personality*, 36(6), 556–563. | Foundational theory | T104, T105 primary source |
| X03 | Rosenthal, S. A., & Pittinsky, T. L. (2006). "Narcissistic leadership." *The Leadership Quarterly*, 17(6), 617–633. | Foundational theory | T104 primary source |
| X04 | Hogan, R., & Hogan, J. (2001). "Assessing leadership: A view from the dark side." *International J. Selection and Assessment*, 9(1–2), 40–51. | Foundational theory | T106 primary source |
| X05 | Goleman, D. (1995). *Emotional intelligence*. Bantam Books. | Foundational theory | Emotional Intelligence origin |

### 13.3 Evidence Flow Diagram

```
R01 Dumdum (2002) ──────► T01, T06, T09 (Meta-analytic support)
R02 Batista-Foguet (2021) ──► T01, T09 (MLQ construct validity)
R03 van Dierendonck (2010) ──► T02, T07, T11 (SLS 8-dimension)
R04 Indarta (2024) ──────► T02, T07, T11 (Systematic review)
R05 최루디아 (2020) ────────► T01, T06, T12 (CVF validation)
R06 Das (2024) ─────────► T07, T12, T14 (360 feedback)
R07 Emam (2024) ────────► T02, T07, T11 (Experimental design)
R08 Soomro (2024) ──────► T03, T13, T14 (EL vs TL)
R09 Azhar (2026) ───────► T03, T05, T12, T14 (Bibliometric)
X01 Bass (1985) ────────► T01, T03, T06, T09 (Origin)
X02 Paulhus (2002) ──────► T104, T105 (Dark Triad)
X03 Rosenthal (2006) ────► T104 (Narcissistic)
X04 Hogan (2001) ────────► T106 (HDS)
X05 Goleman (1995) ──────► T11, T02 (EI)
```

---

## 14. Appendices

### Appendix A: File Inventory (2026-07-01 갱신 — 정리 후 실측)

> 정리 후 저장소에 **실재하는** 연구 자산만 기재합니다. 정리 이전 `ref data/` 인벤토리는 §10.1 "정리 이전 구조(이력)" 참조.

| # | Path | Type | Notes |
|---|------|------|-------|
| 1 | `research/papers/` | Directory | 핵심 논문 원문 텍스트 9개 (P001–P008 + Dumdum) |
| 2 | `research/surveys/vanDierendonck_2010_ServantLeadershipSurvey.pdf` | PDF | SLS 서베이 도구 |
| 3 | `research/evidence_mapping/label_evidence_map.json` | Data | 31개 긍정 라벨 근거 매핑 |
| 4 | `docs/archive/` | Directory | 구 설계문서 8개 + scripts/ 3개 |
| 5 | `data/traits/trait_theory_mapping.json` | Data | Trait↔이론 매핑, validation_status |
| 6 | `data/traits/trait_definitions.json` | Data | 18개 Trait 정의 (required/optional/forbidden) |

**부재(정리 시 제외):** `metadata.csv`, `consolidated_summary.*`, `ref data/pdfs|meta|theory|non_leadership/`, P009–P012 원문.

### Appendix B: Trait Validation Status Summary

| ID | Name | Academic Construct | Ref Data Evidence | Internal Validation |
|----|------|-------------------|-------------------|-------------------|
| T01 | Strategic Decisive | ✅ Supported (Transactional) | ✅ Medium | ❌ Not conducted |
| T02 | Collaborative | ✅ Supported (Servant) | ✅ Strong | ❌ Not conducted |
| T03 | Innovative | ✅ Supported (TL-IS) | ✅ Strong | ❌ Not conducted |
| T04 | Crisis Manager | ❌ Unverified | ⚠️ Weak | ❌ Not conducted |
| T05 | Analytical | ❌ Unverified | ❌ Weak | ❌ Not conducted |
| T06 | Execution Driver | ✅ Supported (Transactional) | ✅ Strong | ❌ Not conducted |
| T07 | Coaching | ✅ Supported (TL-IC) | ✅ Strong | ❌ Not conducted |
| T09 | Visionary | ✅ Supported (TL-II/IM) | ✅ Strong | ❌ Not conducted |
| T11 | Empathetic | ✅ Supported (Servant) | ✅ Strong | ❌ Not conducted |
| T12 | Balanced | ⚠️ Partial (CVF) | ⚠️ Medium | ❌ Not conducted |
| T13 | Ethical Courageous | ✅ Supported (Ethical) | ✅ Strong | ❌ Not conducted |
| T14 | Learning Agile | ⚠️ Partial (Adaptive) | ⚠️ Medium | ❌ Not conducted |
| T101 | Avoidant | ✅ Supported (Laissez-Faire) | ✅ Strong | ❌ Not conducted |
| T102 | Authoritarian | ⚠️ Partial | ❌ Weak | ❌ Not conducted |
| T103 | Integrity Violation | ⚠️ Partial | ⚠️ Medium | ❌ Not conducted |
| T104 | Narcissistic | ✅ Supported (Dark Triad) | ✅ Strong* | ❌ Not conducted |
| T105 | Manipulative | ✅ Supported (Mach) | ✅ Strong* | ❌ Not conducted |
| T106 | Volatile | ✅ Supported (HDS) | ✅ Strong* | ❌ Not conducted |

*\*External primary sources not in ref data folder*

### Appendix C: Key Acronyms

| Acronym | Full Name |
|---------|-----------|
| CFA | Confirmatory Factor Analysis |
| CVF | Competing Values Framework |
| EFA | Exploratory Factor Analysis |
| EI | Emotional Intelligence |
| EL | Entrepreneurial Leadership |
| FAISS | Facebook AI Similarity Search |
| HDS | Hogan Development Survey |
| IC | Individualized Consideration |
| II | Idealized Influence |
| IM | Inspirational Motivation |
| IS | Intellectual Stimulation |
| MLQ | Multifactor Leadership Questionnaire |
| OCB | Organizational Citizenship Behavior |
| SLS | Servant Leadership Survey |
| TL | Transformational Leadership |
| TM | Transactional Memory (non-leadership) |
| VUCA | Volatility, Uncertainty, Complexity, Ambiguity |

### Appendix D: Related Documentation

| Document | Location | Purpose |
|----------|----------|---------|
| AGENTS.md | `C:\dev\leadership\AGENTS.md` | Project compass (central navigation) |
| FILE_STRUCTURE.md | `C:\dev\leadership\FILE_STRUCTURE.md` | Complete file tree |
| core.md | `C:\dev\leadership\docs\core.md` | Vector DB → LLM pipeline |
| HANDOVER.md | `C:\dev\leadership\docs\HANDOVER.md` | System operations manual |
| leadership_catalog.md | `docs\archive\leadership_catalog.md` | (아카이브) Auto-generated trait/label catalog |
| leadership_trait_system.md | `docs\archive\leadership_trait_system.md` | (아카이브) Trait inference engine documentation |
| leadership_evidence_validation_report.md | `docs\archive\leadership_evidence_validation_report.md` | (아카이브) Academic evidence validation |
| leadership_validation_ledger.md | `docs\archive\leadership_validation_ledger.md` | (아카이브) 비판적 검증 원장 |

---

**— End of Report —**

*원 조사 자료: 2026-06-26 `ref data/` 워크스페이스(정리 후 `research/`로 통합, metadata.csv 등 일부 자산 제외).*

*현재 유효 데이터 소스: `research/papers/`, `research/evidence_mapping/label_evidence_map.json`, `data/traits/trait_theory_mapping.json`, `docs/archive/leadership_evidence_validation_report.md`*
