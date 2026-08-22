# Evidence Matrix

**Audit date:** 2026-08-22  
**Purpose:** Identify what each public project proves, how strong the evidence is, and what still needs to be done.

## Capability Matrix

Legend: **✓** = direct evidence; **△** = supporting evidence; **—** = not a primary demonstration.

| Project | AI | Eval | Docs | Knowledge | Curriculum | Git | Deployed | Evidence Strength | Current Action |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|---|
| Technical Prompt Engineer Portfolio | ✓ | ✓ | ✓ | △ | △ | ✓ | ✓ | **High** | Build executable experiments |
| `PROMPT_SCHEMAS.md` | ✓ | ✓ | ✓ | — | — | ✓ | — | **Very High potential** | Add dataset + baseline + measured results |
| WRH Master Curriculum | △ | — | ✓ | ✓ | ✓ | ✓ | ✓ | **Very High** | Package as knowledge-system case study |
| The Rescue Boat | — | — | ✓ | ✓ | △ | ✓ | ✓ | **High** | Use as publication/documentation case study |
| Capitol Contracts | — | — | ✓ | ✓ | — | ✓ | — | **High** | Extract strongest SOP/process artifacts |
| Horner Archive | — | △ | ✓ | ✓ | — | ✓ | ✓ | **Medium–High** | Clean README and frame as research archive |
| From the Storm to the Fire | — | — | ✓ | △ | — | ✓ | ✓ | **Medium** | Supporting publication/revision evidence |
| Book Production | — | — | ✓ | △ | — | ✓ | — | **Medium** | Supporting production-workflow evidence |
| 2026 Working Manuscript | — | — | ✓ | △ | — | ✓ | — | **Medium** | Supporting source/revision provenance |

## Role-Specific Evidence

### AI Evaluation / AI QA

**Strongest evidence:**

1. `PROMPT_SCHEMAS.md`
2. Technical portfolio application materials
3. Planned Evaluation Lab experiments
4. Failure taxonomy and regression results once built
5. WRH only as secondary evidence of structured information handling

**Current gap:** The portfolio currently contains strong *design artifacts* but does not yet contain a published, repeatable benchmark showing measured before/after model behavior. Experiment #001 closes this gap.

### Technical Writing / AI Documentation

**Strongest evidence:**

1. WRH Master Curriculum documentation
2. Technical portfolio Markdown architecture
3. Capitol Contracts documentation
4. Rescue Boat publication/build documentation
5. Horner research archive

**Current gap:** Recruiter-facing case studies should explain the documentation problem, audience, information architecture, implementation process, and maintenance model instead of merely linking to repositories.

### Knowledge Systems / Content Operations

**Strongest evidence:**

1. WRH Master Curriculum
2. Rescue Boat
3. Horner Archive
4. Book production repositories

**Current gap:** Make the information architecture explicit: source-of-truth rules, content model, navigation, search, generated artifacts, and deployment.

### Curriculum / Instructional Design

**Strongest evidence:**

1. WRH Master Curriculum
2. Session Explorer
3. Facilitator/implementation documentation
4. Curriculum source structure

**Current gap:** Resolve the 75-vs-77 count discrepancy and present learning architecture without relying on the recruiter to infer it from source files.

## Evidence Quality Rules

A claim should be classified as:

- **Direct:** A reviewer can inspect the artifact and verify the claim.
- **Measured:** The claim is supported by repeatable test results or quantitative output.
- **Demonstrated:** The artifact shows the capability but does not yet include formal measurement.
- **Self-described:** The claim depends primarily on the author's description.
- **Planned:** The artifact does not yet exist and must not be presented as completed work.

## Current High-Priority Gaps

### GAP-001 — Measured AI Evaluation

**Status:** Open  
**Fix:** Build Experiment #001 with a fixed dataset, scoring rubric, baseline, revision, and regression comparison.

### GAP-002 — Portfolio Count Consistency

**Status:** Open  
**Fix:** Reconcile the portfolio's 75-session references with the current WRH repository's 77 source records.

### GAP-003 — Recruiter Navigation

**Status:** Partially solved  
**Fix:** Keep `PROJECT_SYSTEM_MAP.md` as the master index and add role-specific paths on the website.

### GAP-004 — Application Contact Placeholder

**Status:** Open  
**Fix:** Replace `[EMAIL]` before submitting applications.

### GAP-005 — Horner Archive Framing

**Status:** Open  
**Fix:** Replace the generic deployment README with a finished research-archive README describing the actual artifact, methodology, sources, and public result.

## Evidence Priority

| Priority | Evidence | Why |
|---|---|---|
| P0 | Experiment #001 | Converts AI claims into measured proof |
| P0 | 75/77 reconciliation | Removes avoidable credibility friction |
| P0 | Application Profile cleanup | Makes immediate job applications safer |
| P1 | Documentation case study | Converts WRH into recruiter-readable technical evidence |
| P1 | Knowledge-system case study | Makes architecture visible rather than implicit |
| P1 | Horner README cleanup | Improves research evidence credibility |
| P2 | Experiments #002–#004 | Expands the AI evaluation body of evidence |
| P3 | Interactive evaluation explorer | Useful differentiator after core evidence exists |

## Bottom Line

The portfolio does **not** need more claims. It needs more **inspectable and measured evidence**.

The highest-value transformation is:

`PROMPT_SCHEMAS.md` → `dataset` → `baseline` → `failure analysis` → `revision` → `regression test` → `published case study`
