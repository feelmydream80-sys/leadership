#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_leadership_catalog.py

리더십 Trait / Micro Label / 이론 매핑 JSON을 단일 진실원천으로 삼아
docs/leadership_catalog.md (정리된 카탈로그)를 자동 생성한다.

지속적으로 논문을 추가/정리할 때, JSON만 갱신하고 본 스크립트를 재실행하면
카탈로그가 항상 동기화된다.

사용법:
    python scripts/build_leadership_catalog.py
"""
import json
import os
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TRAIT_DEFS = os.path.join(ROOT, "data/traits/trait_definitions.json")
THEORY_MAP = os.path.join(ROOT, "data/traits/trait_theory_mapping.json")
POS_LABELS = os.path.join(ROOT, "data/micro_labels/positive_micro_labels.json")
NEG_LABELS = os.path.join(ROOT, "data/micro_labels/negative_micro_labels.json")
OUT = os.path.join(ROOT, "docs/leadership_catalog.md")

KOR_NAME = {
    "T01": "결단형", "T02": "협업형", "T03": "혁신형", "T04": "위기 대응형",
    "T05": "분석형", "T06": "실행형", "T07": "코칭형", "T08": "감정 지능형",
    "T09": "비전 제시형", "T10": "전략 실행형", "T11": "공감형", "T12": "균형형",
    "T13": "윤리적 용기형", "T14": "학습 민첩형",
    "T101": "회피형", "T102": "권위주의", "T103": "정직성 위반",
    "T104": "자기애적", "T105": "조작적", "T106": "기복형",
}


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def main():
    defs = load(TRAIT_DEFS)
    tmap = load(THEORY_MAP)
    pos = load(POS_LABELS)
    neg = load(NEG_LABELS)

    traits = {t["trait_id"]: t for t in defs["traits"]}
    mappings = {m["trait_id"]: m for m in tmap["trait_mappings"]}
    registry = tmap["paper_registry"]

    label_name = {}
    for src in (pos, neg):
        for m in src["micro_labels"]:
            label_name[m["label_id"]] = m["label_name"]

    def cite_str(ids):
        out = []
        for c in ids:
            r = registry.get(c, {})
            mark = "" if r.get("in_ref_data") else " *(외부)*"
            out.append(f"{c}:{r.get('citation', c)}{mark}")
        return "; ".join(out)

    lines = []
    A = lines.append
    A("# 리더십 통합 카탈로그 (Leadership Catalog)")
    A("")
    A("> **자동 생성 문서** — `scripts/build_leadership_catalog.py`로 생성. 직접 수정 금지.")
    A("> JSON 원천을 갱신한 뒤 스크립트를 재실행하세요. 변경 이력은 `docs/CHANGELOG_leadership.md` 참조.")
    A("")
    A(f"- 생성일: {date.today().isoformat()}")
    A(f"- Trait 정의 버전: {defs.get('trait_library_version', '?')} / 이론매핑 버전: {tmap.get('version', '?')}")
    A(f"- Trait: {len(traits)}개 (긍정 {sum(1 for t in traits.values() if t['trait_type']=='positive')} / 위험 {sum(1 for t in traits.values() if t['trait_type']=='negative')})")
    A(f"- Micro Label: 긍정 {pos['total_count']} + 부정 {neg['total_count']} = {pos['total_count']+neg['total_count']}개")
    A(f"- 근거 논문: ref data {sum(1 for r in registry.values() if r.get('in_ref_data'))}편 + 외부 원전 {sum(1 for r in registry.values() if not r.get('in_ref_data'))}편")
    vsum = tmap.get("validation_summary", {})
    A(f"- **검증 상태(전제: 미검증)**: 구인지지 {vsum.get('construct_supported',0)} · 부분지지 {vsum.get('partially_supported',0)} · 미검증 {vsum.get('unverified',0)} · 반증 {vsum.get('contradicted',0)}")
    A("")
    A("> ⚠️ **전제**: 어떤 Trait도 우리 자체 데이터에 대한 경험적 검증(요인분석/신뢰도/평가자간 일치도)을 거치지 않았다.")
    A("> 따라서 최고 등급은 `construct_supported`(학계가 구인을 인정)이며, 우리 라벨의 측정 타당성이 증명된 항목은 아직 없다.")
    A("> 비판적 감사는 `docs/leadership_validation_ledger.md` 참조.")
    A("")
    A("---")
    A("")

    # 1. 리더십 이론(종류)
    A("## 1. 리더십 종류 (참조 이론)")
    A("")
    for th in tmap["reference_theories"]:
        A(f"- {th}")
    A("")

    # 2. 근거 논문 레지스트리
    A("## 2. 근거 논문 레지스트리")
    A("")
    A("| ID | 인용 | 유형 | ref data | 파일 |")
    A("|----|------|------|----------|------|")
    for pid, r in registry.items():
        inrd = "O" if r.get("in_ref_data") else "X(외부)"
        A(f"| {pid} | {r.get('citation','')} | {r.get('type','')} | {inrd} | {r.get('file','-')} |")
    A("")

    # 3. Trait 카탈로그
    STATUS_ICON = {
        "construct_supported": "🟡 구인지지",
        "partially_supported": "🟠 부분지지",
        "unverified": "🔴 미검증",
        "contradicted": "⛔ 반증",
    }

    def trait_block(title, kind):
        A(f"## {title}")
        A("")
        A("| ID | 명칭(영/한) | Primary 이론 | 검증상태 | 근거강도 | 근거논문 | Required Labels |")
        A("|----|-------------|--------------|----------|----------|----------|-----------------|")
        for tid, t in traits.items():
            if t["trait_type"] != kind:
                continue
            m = mappings.get(tid, {})
            strength = m.get("evidence_strength", "—")
            status = STATUS_ICON.get(m.get("validation_status"), "🔴 미검증")
            prim = m.get("primary_theory", "(매핑 없음)")
            cites = ",".join(m.get("citations", [])) or "—"
            req = ", ".join(f"{l}({label_name.get(l,'?')})" for l in t.get("required", []))
            kor = KOR_NAME.get(tid, "")
            A(f"| {tid} | {t['trait_name']} / {kor} | {prim} | {status} | {strength} | {cites} | {req} |")
        A("")

    trait_block("3. 긍정 Trait 카탈로그 (Positive)", "positive")
    trait_block("4. 위험 Trait 카탈로그 (Negative)", "negative")

    # 5. Trait 상세 (이론 근거)
    A("## 5. Trait별 학술 근거 상세")
    A("")
    for tid, t in traits.items():
        m = mappings.get(tid)
        A(f"### {tid} · {t['trait_name']} ({KOR_NAME.get(tid,'')})")
        A(f"- 정의: {t.get('description','')}")
        if m:
            A(f"- Primary 이론: {m.get('primary_theory','')}")
            if m.get("secondary_theory"):
                A(f"- Secondary 이론: {m.get('secondary_theory')}")
            A(f"- 근거: {m.get('evidence','')}")
            A(f"- 근거강도: {m.get('evidence_strength','')} / 인용: {cite_str(m.get('citations', []))}")
            A(f"- **검증상태: {m.get('validation_status','unverified')}**")
            if m.get("validation_gap"):
                A(f"- ⚠️ 검증 공백/반증: {m.get('validation_gap')}")
        else:
            A("- ⚠️ 이론 매핑 없음 (보완 필요)")
        A("")

    # 6. Micro Label 인벤토리
    def label_block(title, src):
        A(f"## {title} (총 {src['total_count']}개)")
        A("")
        A("| Label ID | 명칭 | Macro |")
        A("|----------|------|-------|")
        for ml in src["micro_labels"]:
            A(f"| {ml['label_id']} | {ml.get('label_name','')} | {ml.get('macro','')} |")
        A("")

    label_block("6. Positive Micro Label 인벤토리", pos)
    label_block("7. Negative Micro Label 인벤토리", neg)

    # 8. 무결성 점검
    A("## 8. 무결성 점검 (자동)")
    A("")
    missing = [tid for tid in traits if tid not in mappings]
    A(f"- 이론 매핑 누락 Trait: {missing if missing else '없음 ✅'}")
    weak = [tid for tid, m in mappings.items() if m.get("evidence_strength") == "weak"]
    A(f"- 근거강도 weak(보강 필요): {weak if weak else '없음'}")
    # 공유 required label
    from collections import defaultdict
    shared = defaultdict(list)
    for tid, t in traits.items():
        if t["trait_type"] == "positive":
            for l in t.get("required", []):
                shared[l].append(tid)
    multi = {k: v for k, v in shared.items() if len(v) > 1}
    A(f"- 복수 긍정 Trait가 공유하는 required Label(판별타당도 주의):")
    for k, v in sorted(multi.items()):
        A(f"  - {k}({label_name.get(k,'?')}) → {', '.join(v)}")
    A("")

    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"생성 완료: {OUT} ({len(lines)} lines)")


if __name__ == "__main__":
    main()
