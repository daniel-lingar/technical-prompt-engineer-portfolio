# Flagship Case Study Specification: Source-Card Extraction & Grounding Harness

## Purpose

This case study will test whether an LLM can extract a constrained factual source card from a short, publicly available Horner Archive excerpt **without inventing missing facts or treating interpretive notes as verified evidence**. It is a deliberately narrow evaluation: the goal is not to summarize history or make legal, medical, or genealogical conclusions. The goal is to measure faithful structured extraction from a controlled record.

## Why This Is the First Case Study

The Horner Archive provides public, document-oriented historical material with stable repository URLs, source categories, dates, places, named records, and stated research statuses. It allows a reviewer to inspect the source text and compare every expected field against a visible record. It also avoids using the sensitive memoir and trauma-related sites as evaluation inputs.

## Task Contract

Given one public-source excerpt and its source URL, return one JSON object following this schema:

```json
{
  "source_title": "string; use an empty string when absent",
  "record_type": "string; use an empty string when absent",
  "people_named": ["string"],
  "date_or_year": "string; use an empty string when absent",
  "place": "string; use an empty string when absent",
  "research_status": "open | closed | index_only | not_stated",
  "verified_claims": ["string"],
  "not_established": ["string"],
  "source_url": "https://..."
}
```

The model must extract only direct statements from the provided excerpt. When a field is absent, ambiguous, or merely proposed as a research question, it must use `null`, `not_stated`, or an item in `not_established` rather than infer an answer.

## Real Corpus Scope

The initial dataset will use only public Horner Archive records with stable source URLs and factual, documentary content. Candidate source files include:

| Source record | Suitable factual fields | Exclusion rule |
| --- | --- | --- |
| `sources/glo-field-notes-oq22.md` | record citation, survey sections, named land features, status, source institution | Do not convert interpretive terrain observations into named archaeological claims. |
| `sources/estate-oq20-research.md` | estate record, indexed people, year, administrator, file status, retrieval plan | Do not claim the indexed file has been retrieved or that an inferred buyer is established. |
| `sources/1942_transcript_excerpts.txt` | source type, named speaker/subject, explicitly quoted facts, date references | Do not elevate oral-history statements into independently verified facts. |
| `sources/cmsr-oq12-oq13.md` | military-record metadata, stated status, source citations | Do not infer service, injury, or death details beyond the excerpt. |
| `sources/oq-ppan-001.md` | public-record identifiers, source status, documented locations | Do not turn research hypotheses into resolved claims. |

## Dataset Standard

Create **50 real cases** selected from these public records. Each row must preserve the exact source excerpt, source URL, human-reviewed expected JSON, and a source-review note. The dataset is not synthetic: every case must point to a real public passage and every gold field must be manually confirmed from that passage.

| Category | Target cases | What it proves |
| --- | ---: | --- |
| Direct factual extraction | 20 | The system identifies explicit names, dates, records, and places. |
| Missing-field abstention | 10 | The system does not fill absent fields. |
| Open / unresolved status | 10 | The system preserves uncertainty and research boundaries. |
| Oral-history or index-only qualifiers | 5 | The system distinguishes source status from verified fact. |
| Conflicting or ambiguous record language | 5 | The system reports uncertainty rather than choosing a convenient answer. |

## Prompt Versions

| Version | Change | Hypothesis |
| --- | --- | --- |
| `v1_baseline` | Ask for a JSON source card. | Baseline shows formatting and inference failure modes. |
| `v2_schema` | Add the formal output schema and valid-JSON requirement. | Valid-schema rate improves. |
| `v3_evidence_boundary` | Require direct extraction, explicit nulls, and a `not_established` list. | Unsupported inferences decline. |
| `v4_status_handling` | Define `open`, `closed`, `index_only`, and `not_stated` using source wording. | Status classification and abstention improve. |

## Deterministic Metrics

| Metric | Definition |
| --- | --- |
| Valid-schema rate | Percentage of outputs that parse and satisfy required types/enums. |
| Field-level exactness | Percentage of gold fields matched after documented normalization. |
| Unsupported-inference rate | Percentage of outputs stating a claim not supported by the excerpt. |
| Correct-abstention rate | Percentage of absent or unresolved fields handled using the required null/status behavior. |
| Source-URL preservation | Percentage of outputs retaining the supplied canonical source URL. |
| Status accuracy | Percentage of cases with the correct research-status label. |

## Failure Taxonomy

| Code | Failure |
| --- | --- |
| `F01` | Invalid JSON or schema violation |
| `F02` | Unsupported factual inference |
| `F03` | Missing explicit fact |
| `F04` | Incorrect source-status label |
| `F05` | Failure to abstain on absent or unresolved information |
| `F06` | Source URL loss or substitution |
| `F07` | Oral-history, index-only, or interpretive language presented as verified fact |

## Reproducibility Standard

The public project must contain versioned prompts, the real source dataset, a deterministic validator, raw model outputs, aggregation code, and a single documented command that reruns all cases. The site may display only metrics generated by that exact command. The README must document model/provider, run date, temperature, known scoring limitations, and any fields requiring manual review.

## Explicit Boundaries

This case study will not use the personal memoir as model input, will not make clinical or legal determinations, will not present historical hypotheses as settled facts, and will not display fabricated test counts or improvements. Adversarial or prompt-injection testing is deferred until a real, reviewed input set is available that supports it without synthetic data.
