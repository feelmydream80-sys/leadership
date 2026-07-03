# papers/extracted/ — PDF 전문 추출 텍스트 (영구 저장)

**생성:** 2026-07-02 · **도구:** PyMuPDF(fitz) · **원본:** `papers/pdfs/` (75 PDF)

> PDF를 매번 변환하지 않도록 전문을 텍스트로 1회 추출해 여기 저장한다.
> **근거를 찾을 때는 원본 PDF가 아니라 이 폴더의 `.txt`를 참조**하고, 인용은 `===== PAGE n =====` 마커로 페이지를 표기한다.

## 파일 형식
각 `paper_<id>_<source>.txt`:
```
### SOURCE / PAPER_ID / TITLE / AUTHORS / YEAR / PAGES   (헤더)
===== PAGE 1 =====
<1페이지 본문>
===== PAGE 2 =====
...
```
→ 페이지 단위 인용 가능(줄 단위는 미지원). 예: "paper_331 PAGE 3".

## 인벤토리 (`manifest.json` 참조)
| 상태 | 편수 | 의미 |
|------|------|------|
| `leadership` | 31 | 리더십 관련 전문 확보 — **근거 후보** |
| `off_topic` | 28 | AI/보안 등 비(非)리더십 — 근거 제외 |
| `no_content_stub` | 15 | 다운로드 실패 스텁(내용 없음) → `_no_content_stub/`로 격리 |
| 실패 | 1 | paper_241(Elsevier XML 오류 응답, PDF 아님) |

## 중요한 한계 (정직 고지)
- **이 75 PDF는 `papers/metadata.csv`(227편 초록)와 교집합 0** — 별개 컬렉션이며 메타데이터(제목/저자)가 비어 있음.
- 따라서 **핵심 이론 논문(거래적 Bono&Judge, 윤리, 진정성 Walumbwa 등)은 여전히 초록만** 존재. 전문 확보분은 대부분 디지털/AI 리더십.
- 근거로 채택되는 것은 오직 `research/evidence_mapping/label_evidence_map.json`에 등재된 항목뿐. 여기 텍스트가 있다고 자동으로 근거가 되는 것은 아님.

## 주목할 전문 확보 논문 (근거 활용 후보)
- **paper_331** = Cortellazzo, Bruni & Zampieri (2019) *The Role of Leadership in a Digitalized World: A Review* (Frontiers in Psychology) — 디지털 리더십 이론의 실제 원문(종전 인용만 있고 부재했음).
- 그 외 `manifest.json`의 `status=leadership` 목록 참조.

## 재생성
```bash
# 원본 PDF에서 재추출 (papers/extracted/ 갱신)
python scripts/extract_pdfs.py   # (파이프라인은 대화 이력의 fitz 스크립트 기준)
```
