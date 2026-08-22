# Horner Archive Source-Card Extraction & Grounding Harness

This is the first proof-of-work evaluation in the Technical Prompt Engineer portfolio. It tests a narrow task: whether an LLM can build a structured source card from short **public Horner Archive** passages without turning oral history, index entries, research plans, or interpretive notes into established facts. Empty strings and empty arrays represent absent fields in the strict output schema.

## What This Measures

| Measure | Meaning |
| --- | --- |
| Valid-schema rate | The output parses and matches the strict source-card schema. |
| Gold-check accuracy | The output satisfies the manually reviewed target checks associated with each real source passage. |
| Source-URL preservation | The output retains the immutable public source URL. |
| Possible grounding flags | A deterministic lexical-overlap heuristic identifies claims that may require human review. |
| Boundary violations | The output presents a case-specific forbidden claim as verified. |

> The lexical grounding check is deliberately conservative. It is a reproducible screening heuristic, not a historical-truth adjudicator. Human review remains necessary for all flagged outputs.

## Corpus and Boundaries

The dataset builder downloads 50 cases from a [pinned public commit](https://github.com/daniel-lingar/horner-archive/tree/1ce7f7062559b2e132d9690f6f91df8f4452784e) of the Horner Archive. Cases use public source-oriented research notes: CMSR research, modern-parcel research, the audience evidence matrix, GLO field-notes research, and estate-research notes.

The harness intentionally excludes the personal manuscript and the trauma-focused WRH/Rescue Boat materials from model input. It does not make clinical, legal, genealogical, or historical conclusions beyond the provided excerpts.

## Run Locally

This runner uses an OpenAI-compatible endpoint. Set environment variables without committing secrets:

```bash
export OPENAI_API_KEY="..."
export OPENAI_API_BASE="https://your-compatible-endpoint/v1"

python3 evaluation-harness/horner_source_card/build_dataset.py
python3 evaluation-harness/horner_source_card/eval_runner.py --version v1_baseline --model gpt-5-mini
python3 evaluation-harness/horner_source_card/eval_runner.py --version v2_schema --model gpt-5-mini
python3 evaluation-harness/horner_source_card/eval_runner.py --version v3_evidence_boundary --model gpt-5-mini
python3 evaluation-harness/horner_source_card/eval_runner.py --version v4_status_handling --model gpt-5-mini
```

Raw responses are written to `results/<version>_raw.jsonl`; aggregate metrics are written to `results/<version>_summary.json`.

## Current Execution Status

The source corpus and deterministic integrity validator are complete. The full model run is intentionally not summarized as a performance result because the available proxy returned a credit-check error during most bulk calls. See [`results/EXECUTION_STATUS.md`](results/EXECUTION_STATUS.md) for the recorded limitation and re-run contract.

## Methodological Limits

This benchmark is a controlled extraction task, not a production-reliability claim. Its cases are selected from one public archive and its deterministic checks use manually reviewed target fragments. Results do not demonstrate clinical efficacy, legal accuracy, historical certainty beyond cited text, or general performance in other domains.
