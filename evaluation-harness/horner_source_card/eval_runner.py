#!/usr/bin/env python3
"""Run the public Horner Archive source-card evaluation against an OpenAI-compatible endpoint.

Design note — Calibration Lab / evidence-first portfolio:
The runner stores raw completions, validates a strict schema, evaluates manually
reviewed target checks, and flags possible lexical grounding violations. The
lexical guard is a reproducible heuristic, not a substitute for historical review.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import json
import os
import pathlib
import re
import sys
from collections import Counter

from openai import OpenAI


ROOT = pathlib.Path(__file__).resolve().parent
DATASET = ROOT / "datasets" / "horner_source_cards_v1.jsonl"
PROMPTS = ROOT / "prompts"
RESULTS = ROOT / "results"
VALID_STATUSES = {"open", "closed", "partial", "index_only", "not_stated"}
SCHEMA = {
    "type": "object",
    "properties": {
        "source_title": {"type": "string"},
        "record_type": {"type": "string"},
        "people_named": {"type": "array", "items": {"type": "string"}},
        "date_or_year": {"type": "string"},
        "place": {"type": "string"},
        "research_status": {"type": "string", "enum": sorted(VALID_STATUSES)},
        "verified_claims": {"type": "array", "items": {"type": "string"}},
        "not_established": {"type": "array", "items": {"type": "string"}},
        "source_url": {"type": "string"},
    },
    "required": [
        "source_title", "record_type", "people_named", "date_or_year", "place",
        "research_status", "verified_claims", "not_established", "source_url",
    ],
    "additionalProperties": False,
}


def load_cases() -> list[dict]:
    return [json.loads(line) for line in DATASET.read_text(encoding="utf-8").splitlines() if line.strip()]


def normalise(value: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]+", " ", value.casefold())).strip()


def flattened(value: object) -> str:
    return normalise(json.dumps(value, ensure_ascii=False))


def validate_shape(payload: object) -> list[str]:
    if not isinstance(payload, dict):
        return ["output is not a JSON object"]
    issues: list[str] = []
    if set(payload) != set(SCHEMA["required"]):
        issues.append("output keys do not exactly match the required schema")
    for field in ["source_title", "record_type", "date_or_year", "place"]:
        if field in payload and not isinstance(payload[field], str):
            issues.append(f"{field} must be a string")
    for field in ["people_named", "verified_claims", "not_established"]:
        if field in payload and (not isinstance(payload[field], list) or not all(isinstance(item, str) for item in payload[field])):
            issues.append(f"{field} must be an array of strings")
    if payload.get("research_status") not in VALID_STATUSES:
        issues.append("research_status is outside the allowed enum")
    if not isinstance(payload.get("source_url"), str):
        issues.append("source_url must be a string")
    return issues


def lexical_support(claim: str, excerpt: str) -> float:
    claim_tokens = [token for token in normalise(claim).split() if len(token) > 2]
    excerpt_tokens = set(normalise(excerpt).split())
    if not claim_tokens:
        return 1.0
    return sum(token in excerpt_tokens for token in claim_tokens) / len(claim_tokens)


def evaluate(case: dict, payload: object) -> dict:
    shape_issues = validate_shape(payload)
    output = payload if isinstance(payload, dict) else {}
    gold = case["gold"]
    checks = gold["checks"]
    passed = 0
    check_results = []
    for rule in checks:
        value = output.get(rule["field"])
        rendered = flattened(value)
        if "equals" in rule:
            ok = normalise(str(value)) == normalise(rule["equals"])
        else:
            ok = normalise(rule["contains"]) in rendered
        passed += int(ok)
        check_results.append({**rule, "passed": ok})

    supported_claims = []
    for claim in output.get("verified_claims", []) if isinstance(output.get("verified_claims"), list) else []:
        supported_claims.append({"claim": claim, "lexical_support": round(lexical_support(claim, case["source_excerpt"]), 3)})
    weak_claims = [item for item in supported_claims if item["lexical_support"] < 0.70]
    forbidden_text = normalise(" ".join(output.get("verified_claims", []))) if isinstance(output.get("verified_claims"), list) else ""
    forbidden_hits = [term for term in gold["forbidden_verified_claims"] if normalise(term) in forbidden_text]

    return {
        "schema_valid": not shape_issues,
        "schema_issues": shape_issues,
        "gold_checks_passed": passed,
        "gold_checks_total": len(checks),
        "gold_check_results": check_results,
        "source_url_preserved": output.get("source_url") == case["source_url"],
        "possible_grounding_violations": weak_claims,
        "forbidden_claim_hits": forbidden_hits,
    }


def call_model(case: dict, prompt: str, model: str, base_url: str, api_key: str) -> dict:
    client = OpenAI(api_key=api_key, base_url=base_url, timeout=45, max_retries=1)
    try:
        envelope = client.chat.completions.create(
            model=model,
            temperature=0,
            max_completion_tokens=700,
            extra_body={"reasoning": {"effort": "minimal"}},
            messages=[
                {"role": "system", "content": prompt + "\nUse no more than five concise verified_claims and five concise not_established items."},
                {
                    "role": "user",
                    "content": (
                        f"Canonical source URL: {case['source_url']}\n\n"
                        f"Public source excerpt:\n---\n{case['source_excerpt']}\n---\n\n"
                        "Return the source card now."
                    ),
                },
            ],
            response_format={
                "type": "json_schema",
                "json_schema": {"name": "source_card", "strict": True, "schema": SCHEMA},
            },
        )
        if not envelope.choices or not envelope.choices[0].message.content:
            return {
                "raw_content": None,
                "output": None,
                "api_error": json.dumps(envelope.model_dump(), ensure_ascii=False),
                "usage": envelope.usage.model_dump() if envelope.usage else None,
            }
        content = envelope.choices[0].message.content
        return {
            "raw_content": content,
            "output": json.loads(content or "null"),
            "api_error": None,
            "usage": envelope.usage.model_dump() if envelope.usage else None,
        }
    except Exception as error:  # Preserve SDK/proxy diagnostics in the raw output log.
        return {"raw_content": None, "output": None, "api_error": str(error), "usage": None}


def aggregate(records: list[dict]) -> dict:
    total = len(records)
    schema_valid = sum(record["evaluation"]["schema_valid"] for record in records)
    passed = sum(record["evaluation"]["gold_checks_passed"] for record in records)
    checks = sum(record["evaluation"]["gold_checks_total"] for record in records)
    source_urls = sum(record["evaluation"]["source_url_preserved"] for record in records)
    grounding_flags = sum(len(record["evaluation"]["possible_grounding_violations"]) for record in records)
    forbidden_hits = sum(len(record["evaluation"]["forbidden_claim_hits"]) for record in records)
    failure_counts = Counter()
    for record in records:
        evaluation = record["evaluation"]
        if not evaluation["schema_valid"]:
            failure_counts["F01_schema"] += 1
        if evaluation["gold_checks_passed"] < evaluation["gold_checks_total"]:
            failure_counts["F03_target_miss"] += 1
        if evaluation["possible_grounding_violations"]:
            failure_counts["F02_lexical_grounding_flag"] += 1
        if evaluation["forbidden_claim_hits"]:
            failure_counts["F05_boundary_violation"] += 1
        if not evaluation["source_url_preserved"]:
            failure_counts["F06_source_url_loss"] += 1
    return {
        "cases": total,
        "valid_schema_rate": round(schema_valid / total, 4) if total else 0,
        "gold_check_accuracy": round(passed / checks, 4) if checks else 0,
        "source_url_preservation_rate": round(source_urls / total, 4) if total else 0,
        "possible_grounding_flags": grounding_flags,
        "forbidden_claim_hits": forbidden_hits,
        "failure_counts": dict(failure_counts),
        "scoring_note": "Lexical grounding flags are deterministic overlap heuristics and require human review; they are not semantic truth judgments.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", choices=["v1_baseline", "v2_schema", "v3_evidence_boundary", "v4_status_handling"], required=True)
    parser.add_argument("--model", default="gpt-5-mini")
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--case-id", help="Run one named case for request-shape diagnosis.")
    arguments = parser.parse_args()
    if not DATASET.exists():
        sys.exit("Dataset missing. Run build_dataset.py first.")
    api_key = os.environ.get("OPENAI_API_KEY")
    base_url = os.environ.get("OPENAI_API_BASE")
    if not api_key or not base_url:
        sys.exit("OPENAI_API_KEY and OPENAI_API_BASE are required for model execution.")
    prompt = (PROMPTS / f"{arguments.version}.txt").read_text(encoding="utf-8")
    cases = load_cases()
    if arguments.case_id:
        cases = [case for case in cases if case["id"] == arguments.case_id]
        if not cases:
            sys.exit(f"Unknown case ID: {arguments.case_id}")
    RESULTS.mkdir(parents=True, exist_ok=True)

    def run(case: dict) -> dict:
        response = call_model(case, prompt, arguments.model, base_url, api_key)
        response["evaluation"] = evaluate(case, response["output"])
        return {"case_id": case["id"], "source_url": case["source_url"], "gold": case["gold"], **response}

    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, arguments.workers)) as pool:
        records = list(pool.map(run, cases))
    report = {
        "run_at_utc": dt.datetime.now(tz=dt.timezone.utc).isoformat(),
        "model": arguments.model,
        "prompt_version": arguments.version,
        "dataset": str(DATASET.relative_to(ROOT)),
        "dataset_cases": len(cases),
        "metrics": aggregate(records),
    }
    (RESULTS / f"{arguments.version}_raw.jsonl").write_text(
        "".join(json.dumps(record, ensure_ascii=False) + "\n" for record in records), encoding="utf-8"
    )
    (RESULTS / f"{arguments.version}_summary.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
