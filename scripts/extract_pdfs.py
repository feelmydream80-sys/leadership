"""Extract full text from papers/pdfs/*.pdf into papers/extracted/*.txt (persistent).

Each output .txt keeps a header + '===== PAGE n =====' markers so evidence can be
cited at page granularity. Download-stub PDFs (<500 chars body) are moved to
papers/extracted/_no_content_stub/. Writes papers/extracted/manifest.json.

Usage:  python scripts/extract_pdfs.py
Requires: PyMuPDF (import fitz)
"""
import os
import re
import csv
import json
import shutil

import fitz  # PyMuPDF

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "papers", "pdfs")
OUT = os.path.join(ROOT, "papers", "extracted")
STUB = os.path.join(OUT, "_no_content_stub")
META = os.path.join(ROOT, "papers", "metadata.csv")

LEAD_KW = ["leader", "leadership", "리더", "servant", "transformational",
           "transactional", "ethical", "authentic", "manager", "organization",
           "employee", "follower", "supervis"]


def load_metadata():
    meta = {}
    if not os.path.exists(META):
        return meta
    with open(META, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            row = {k.lstrip("﻿"): v for k, v in row.items()}
            if row.get("id", "").isdigit():
                meta[int(row["id"])] = row
    return meta


def main():
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(STUB, exist_ok=True)
    meta = load_metadata()
    papers = []
    for fn in sorted(os.listdir(SRC)):
        if not fn.lower().endswith(".pdf"):
            continue
        m = re.match(r"paper_(\d+)_", fn)
        pid = int(m.group(1)) if m else None
        info = meta.get(pid, {})
        rec = {"paper_id": pid, "file": fn, "txt": fn[:-4] + ".txt",
               "title": info.get("title", ""), "authors": info.get("authors", ""),
               "year": (info.get("published_date", "") or "")[:10],
               "source": info.get("source", "")}
        try:
            doc = fitz.open(os.path.join(SRC, fn))
            parts = [f"### SOURCE: {fn}", f"### PAPER_ID: {pid}",
                     f"### TITLE: {info.get('title', '')}",
                     f"### AUTHORS: {info.get('authors', '')}",
                     f"### YEAR: {info.get('published_date', '')}",
                     f"### PAGES: {doc.page_count}", ""]
            body_chars = 0
            for i, page in enumerate(doc, 1):
                t = page.get_text("text")
                body_chars += len(t)
                parts.append(f"\n===== PAGE {i} =====")
                parts.append(t.rstrip())
            doc.close()
            text = "\n".join(parts)
            rec["body_chars"] = body_chars
            stub = body_chars < 500
            dest = os.path.join(STUB if stub else OUT, rec["txt"])
            with open(dest, "w", encoding="utf-8") as f:
                f.write(text)
            if stub:
                rec["status"] = "no_content_stub"
                rec["leadership_relevant"] = False
            else:
                low = text.lower()
                hits = sum(low.count(k) for k in LEAD_KW)
                rec["kw_hits"] = hits
                rec["leadership_relevant"] = hits >= 8
                rec["status"] = "leadership" if hits >= 8 else "off_topic"
        except Exception as e:  # noqa: BLE001
            rec["status"] = "error"
            rec["error"] = str(e)[:160]
        papers.append(rec)

    counts = {s: sum(1 for p in papers if p.get("status") == s)
              for s in ("leadership", "off_topic", "no_content_stub", "error")}
    manifest = {
        "generated": "2026-07-02",
        "tool": "PyMuPDF(fitz)",
        "source_dir": "papers/pdfs",
        "text_dir": "papers/extracted",
        "stub_dir": "papers/extracted/_no_content_stub",
        "note": "각 txt는 ### 헤더 + '===== PAGE n =====' 마커로 페이지 구분. 근거 인용 시 PAGE 마커 사용.",
        "total": len(papers),
        "counts": counts,
        "papers": papers,
    }
    with open(os.path.join(OUT, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)
    print(f"extracted {len(papers)} pdfs -> {counts}")


if __name__ == "__main__":
    main()
