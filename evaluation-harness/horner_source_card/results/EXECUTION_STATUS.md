# Execution Status — Horner Archive Source-Card Harness

## Validated Artifacts

The dataset builder created **50 distinct cases** from five real, public Horner Archive research files pinned to commit `1ce7f7062559b2e132d9690f6f91df8f4452784e`. The deterministic corpus-integrity validator passed with zero source-reference or gold-fragment failures. See [`dataset_integrity.json`](dataset_integrity.json).

## Model-Run Status

The runner successfully completed a one-case structured-output probe using `gpt-5-mini`, demonstrating that the schema and request path work. A subsequent full 50-case baseline attempt encountered a proxy-side `Failed to check credits` error for 48 of 50 calls. That output is retained as a blocked-attempt log only; it is **not** a model-performance result and must not be used to calculate or display quality metrics.

The repository deliberately presents **no accuracy, improvement, failure-rate, or prompt-version comparison claim** until all 50 calls for each version complete and their raw outputs are preserved.

## Re-run Procedure

When model execution capacity is available, run the corpus builder and all four prompt versions from the project root:

```bash
python3 evaluation-harness/horner_source_card/build_dataset.py
python3 evaluation-harness/horner_source_card/validate_dataset.py
python3 evaluation-harness/horner_source_card/eval_runner.py --version v1_baseline --model gpt-5-mini --workers 2
python3 evaluation-harness/horner_source_card/eval_runner.py --version v2_schema --model gpt-5-mini --workers 2
python3 evaluation-harness/horner_source_card/eval_runner.py --version v3_evidence_boundary --model gpt-5-mini --workers 2
python3 evaluation-harness/horner_source_card/eval_runner.py --version v4_status_handling --model gpt-5-mini --workers 2
```

Only complete runs should be compared. Any run with an API error, partial case count, or missing raw-output file should be marked invalid and excluded from portfolio metrics.
