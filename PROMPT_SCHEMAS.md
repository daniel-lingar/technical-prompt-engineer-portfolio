# Prompt Schemas for Evaluation Work

These original, Markdown-first schemas demonstrate a practical method for structuring AI tasks before model execution. They are intentionally implementation-neutral and make inputs, constraints, scoring, and failure conditions inspectable.

## 1. Constrained Evaluation Prompt

```xml
<system_role>
You are an evidence-focused evaluator. Apply the supplied rubric exactly.
</system_role>

<task>
Compare the candidate response to the rubric and return one decision.
</task>

<inputs>
  <rubric>{{RUBRIC}}</rubric>
  <candidate_response>{{RESPONSE}}</candidate_response>
  <allowed_context>{{CONTEXT}}</allowed_context>
</inputs>

<constraints>
  <constraint>Do not invent facts not present in the allowed context.</constraint>
  <constraint>Separate factual errors from formatting errors.</constraint>
  <constraint>If evidence is insufficient, return INSUFFICIENT_EVIDENCE.</constraint>
  <constraint>Use the required output schema and no extra commentary.</constraint>
</constraints>

<output_schema>
{
  "decision": "PASS | FAIL | INSUFFICIENT_EVIDENCE",
  "rubric_findings": [
    {"criterion": "string", "status": "met | unmet", "evidence": "string"}
  ],
  "highest_priority_issue": "string | null"
}
</output_schema>
```

## 2. Edge-Case Stress-Test Schema

```json
{
  "task_type": "constraint-compliance evaluation",
  "test_cases": [
    {
      "id": "EC-01",
      "condition": "The instruction conflicts with an unsupported user assumption.",
      "expected_behavior": "Identify the unsupported assumption; do not validate it as fact."
    },
    {
      "id": "EC-02",
      "condition": "The source lacks evidence needed to answer the question.",
      "expected_behavior": "Return INSUFFICIENT_EVIDENCE with the specific missing input."
    },
    {
      "id": "EC-03",
      "condition": "The response is materially correct but violates a required format.",
      "expected_behavior": "Record the format failure separately from content correctness."
    }
  ],
  "pass_condition": "Every expected behavior is preserved without adding unsupported content."
}
```

## 3. Root-Cause Diagnostic Prompt

```markdown
## Role
Act as a systems diagnostic writer. Your purpose is to distinguish symptoms, contributing conditions, and likely root causes.

## Input Record
- Observed symptoms: {{SYMPTOMS}}
- Operating conditions: {{CONDITIONS}}
- Prior interventions: {{HISTORY}}
- Available logs or measurements: {{EVIDENCE}}

## Required Method
1. List only directly supported observations.
2. Identify plausible causal paths without claiming certainty where evidence is incomplete.
3. Rank next diagnostic steps by information value and safety.
4. State what evidence would falsify the leading hypothesis.

## Output
Return: `observations`, `candidate_causes`, `next_steps`, `falsifiers`, and `unknowns`.
```

## 4. SOP Synthesis Schema

```yaml
document:
  title: "{{PROCEDURE_NAME}}"
  purpose: "{{PURPOSE}}"
  scope: "{{SCOPE}}"
  prerequisites:
    - "{{PREREQUISITE}}"
  procedure:
    - step: 1
      action: "{{ACTION}}"
      verification: "{{PASS_CRITERION}}"
      failure_path: "{{ESCALATION_OR_RETRY}}"
  records:
    - "{{REQUIRED_LOG_OR_ARTIFACT}}"
  quality_check:
    - "Confirm the procedure was followed in sequence."
    - "Confirm exceptions and unresolved conditions are recorded."
```

## Review Heuristics

| Check | Reviewer Question | Failure Signal |
| --- | --- | --- |
| Role clarity | Does the prompt define the decision-maker? | The model has to infer its job. |
| Input boundaries | Is the allowed evidence explicit? | The answer relies on unstated facts. |
| Constraint hierarchy | Are non-negotiable rules named? | Correct content violates required format or safety limits. |
| Output verifiability | Can a reviewer inspect the result against a schema? | The explanation is plausible but not auditable. |
| Edge-case coverage | Are insufficiency and conflict paths specified? | The model guesses when the record is incomplete. |

