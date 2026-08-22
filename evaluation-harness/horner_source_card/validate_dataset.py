#!/usr/bin/env python3
"""Validate the real source-card corpus before any model results are published."""

from __future__ import annotations

import datetime as dt
import json
import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parent
DATASET = ROOT / "datasets" / "horner_source_cards_v1.jsonl"
OUTPUT = ROOT / "results" / "dataset_integrity.json"
EXPECTED_CASES = 50
EXPECTED_COMMIT = "1ce7f7062559b2e132d9690f6f91df8f4452784e"


def normalise(value: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]+", " ", value.casefold())).strip()


def main() -> None:
    cases = [json.loads(line) for line in DATASET.read_text(encoding="utf-8").splitlines() if line.strip()]
    failures: list[dict] = []
    seen: set[str] = set()
    source_paths: set[str] = set()
    category_counts: dict[str, int] = {"closed": 0, "open": 0, "partial": 0, "index_only": 0, "not_stated": 0}
    for case in cases:
        case_id = case.get("id", "<missing>")
        if case_id in seen:
            failures.append({"id": case_id, "issue": "duplicate case ID"})
        seen.add(case_id)
        source_paths.add(case.get("source_path", ""))
        if case.get("source_commit") != EXPECTED_COMMIT:
            failures.append({"id": case_id, "issue": "source commit is not pinned to the approved revision"})
        expected_url = f"https://github.com/daniel-lingar/horner-archive/blob/{EXPECTED_COMMIT}/{case.get('source_path', '')}"
        if case.get("source_url") != expected_url:
            failures.append({"id": case_id, "issue": "source URL is not immutable or does not match the source path"})
        excerpt = normalise(case.get("source_excerpt", ""))
        if len(excerpt) < 80:
            failures.append({"id": case_id, "issue": "source excerpt is unexpectedly short"})
        status = case.get("gold", {}).get("research_status")
        if status not in category_counts:
            failures.append({"id": case_id, "issue": "unrecognized gold research status"})
        else:
            category_counts[status] += 1
        for check in case.get("gold", {}).get("checks", []):
            if "contains" in check and normalise(check["contains"]) not in excerpt:
                failures.append({"id": case_id, "issue": f"gold fragment not found in source excerpt: {check['contains']}"})

    report = {
        "validated_at_utc": dt.datetime.now(tz=dt.timezone.utc).isoformat(),
        "dataset": str(DATASET.relative_to(ROOT)),
        "expected_case_count": EXPECTED_CASES,
        "actual_case_count": len(cases),
        "unique_case_count": len(seen),
        "source_commit": EXPECTED_COMMIT,
        "source_files": sorted(source_paths),
        "research_status_distribution": category_counts,
        "failures": failures,
        "integrity_passed": len(cases) == EXPECTED_CASES and len(seen) == EXPECTED_CASES and not failures,
        "scope_note": "This validates corpus integrity and manually reviewed check fragments. It does not measure model performance.",
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not report["integrity_passed"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
