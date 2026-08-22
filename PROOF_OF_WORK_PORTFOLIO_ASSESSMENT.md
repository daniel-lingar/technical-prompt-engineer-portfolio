# Proof-of-Work Portfolio Assessment

## Assessment

The supplied strategy is directionally sound: an AI-oriented portfolio becomes materially more credible when it presents reproducible evaluation artifacts, before/after comparisons, failure analysis, and documented limitations rather than a collection of prompts or polished outputs. The current portfolio already has a strong visual and documentation foundation, but it does not yet contain the verified datasets, evaluator logic, baseline/final runs, or failure records needed to display quantitative performance claims.

The recommended change is therefore **evidence first, interface second**. Do not add headline metrics, case counts, improvement percentages, named failure totals, or flagship-project labels until the underlying artifacts are built and reproducibly generated. The current portfolio should retain its truthful framing around prompt schemas, documentation, constraints, and asynchronous systems while the proof layer is created.

## External Cross-Check

The cited ObiTech Jobs article recommends showing prompt iteration against a representative test set, evaluation infrastructure, deliberate failure-mode analysis, and a repeatable run process rather than relying on screenshots or claims of improved quality. It also recommends two or three strong projects over many weak examples. The cited Zalt article similarly emphasizes retrieval evaluation, logged evidence, groundedness checks, and documented examples of caught failures over unsupported accuracy claims.

## Recommended First Flagship Case Study

Start with a controlled **structured information extraction evaluation harness**, not a broad RAG system. It has the narrowest scope, can be evaluated deterministically, avoids third-party data access, and connects naturally to the existing portfolio’s emphasis on output constraints.

| Component | Initial standard |
| --- | --- |
| Task | Extract a fixed schema from synthetic, messy customer-support records. |
| Dataset | 50 hand-authored JSONL cases split among normal, missing, contradictory, malformed, injection, and out-of-scope inputs. |
| Baseline | A simple prompt with no explicit schema or evidence-boundary rule. |
| Iterations | Versioned prompts that add a schema, evidence constraint, conflict handling, and abstention behavior. |
| Metrics | Valid-schema rate, field-level accuracy, unsupported-inference count, correct-abstention rate, and prompt-injection refusal rate. |
| Evidence | Versioned prompts, dataset, deterministic validators, raw results, aggregate report, failure taxonomy, and a one-command evaluation runner. |

## Claim Boundary

The portfolio should say only what a reviewer can verify from the public repository. Any displayed result must be generated from the included dataset and scoring code, with a README that explains the scoring limitations. No claim should imply paid AI-lab evaluation, enterprise deployment, production safety guarantees, or model training unless independently documented.

## Sources

1. [ObiTech Jobs — How to Build a Prompt Engineering Portfolio That Gets You Hired](https://www.obitechjobs.com/blog/prompt-engineering-portfolio?utm_source=chatgpt.com)
2. [Zalt — AI Portfolio Projects That Actually Prove You Can Engineer](https://zalt.me/blog/2026/07/ai-portfolio-projects-that-prove-skill?utm_source=chatgpt.com)
