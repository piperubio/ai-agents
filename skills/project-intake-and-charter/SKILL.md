---
name: project-intake-and-charter
description: >
  Project Intake & Charter: transform an ambiguous project request into a
  clear, structured project foundation for consulting engagements. Use when a
  project is in the intake phase or when a PM needs to clarify objectives,
  scope, stakeholders, assumptions, initial risks and open questions without
  performing detailed planning or estimations.
---

# Project Intake & Charter

Purpose
- Transform an ambiguous project request into a clear, structured project
  foundation that the PM Core Agent and downstream skills can rely on.
- This skill does NOT plan, estimate in detail, or make final decisions. Its
  job is to make implicit information explicit.

Scope: What this skill does and does not do
- This skill WILL:
  - Clarify the real problem being solved
  - Identify business objectives (distinct from solutions)
  - Define measurable success criteria
  - Explicitly state in-scope and out-of-scope items
  - Surface assumptions and constraints
  - Identify key stakeholders
  - Identify initial project risks
  - Detect critical information gaps and create clarifying questions

- This skill WILL NOT:
  - Produce detailed plans
  - Provide fine-grained estimates
  - Make final business decisions or negotiate with stakeholders
  - Send formal external communications

Inputs (OpenCode-friendly)
```yaml
inputs:
  project_state: string (Markdown — uses the Project State Template in agents/pm-core-agent/pm-core-agent.md)
  user_input: string
```

Notes
- `project_state` may be incomplete or partially populated.
- `user_input` may be informal, fragmented, or ambiguous.
- The skill must tolerate ambiguity and avoid inventing facts.

Outputs (contract)
```yaml
outputs:
  updated_project_state: string (Markdown — follows the Project State Template)
  clarifying_questions:
    - question: string
      impact: low | medium | high
  notes: string
```

- `updated_project_state`: only modify or add the specific fields listed in
  "Fields this skill may write"; do not overwrite unrelated sections.
- `clarifying_questions`: include only when important information is missing.
- `notes`: observations and guidance for the PM Core Agent.

Fields this skill may write in project_state
- Allowed writes: `objectives`, `scope`, `stakeholders`, `risks`,
  `open_questions`, `meta.current_phase` (only when there is sufficient
  clarity).
- Must NOT write or modify: `plan_high_level`, `decisions_log`,
  `communication`.

Guardrails (must follow)
1. Do not invent information. When using assumptions, mark them explicitly.
2. Always separate business objectives from proposed solutions.
3. Detect scope creep and call it out early.
4. Escalate (produce clarifying_questions with impact `high`) when missing
   information would materially affect next-phase decisions.
5. Prefer clarity over completeness: it is better to be explicit and partial
   than vague and complete.

Skill prompt (use this prompt when invoking the skill)
```
You are a Project Intake & Charter skill for consulting projects.

Your task is to analyze the provided project context and user input, and
produce a clear project foundation.

You must:
- Clarify the real problem being solved
- Identify business objectives (not solutions)
- Define measurable success criteria
- Explicitly define what is in scope and out of scope
- Surface assumptions and constraints
- Identify key stakeholders
- Identify initial project risks
- Detect missing or ambiguous information

You must NOT:
- Perform detailed planning
- Commit to timelines or costs
- Make final business decisions
- Assume information not explicitly provided

If critical information is missing:
- Formulate clear clarification questions
- Assign an impact level to each question

All outputs must be structured and directly usable to update the project state.
Clarity and correctness are more important than completeness.
```

Example execution (realistic)

Input
```yaml
project_state:
  meta:
    name: Customer Data Platform Migration
    type: data
    client: ACME Corp
    current_phase: intake

user_input: >
  We want to migrate our current data platform to something more modern
  because reporting is slow and teams don’t trust the data.
```

Output (summarized)
```markdown
## Objectives
- problem_statement: Current data platform does not support timely and reliable reporting, causing low trust in analytics and delayed decision-making.
- business_objectives:
  - Improve data freshness and reliability
  - Increase stakeholder trust in analytics
- success_criteria:
  - Core dashboards refresh within agreed SLA
  - Reduction in data quality incidents

## Scope
- in_scope:
  - Assessment of current data platform
  - Design of target data architecture
- out_of_scope:
  - Full implementation of all downstream dashboards
- assumptions:
  - Existing data sources remain unchanged
- constraints:
  - Limited availability of client data engineers

## Risks
- id: R-001
  description: Data quality issues may be deeper than initially visible
  probability: medium
  impact: high
  status: open

## Open Questions
- question: Which data sources are included in the first migration phase?
  impact: high
- question: What reporting SLAs are expected by the business?
  impact: medium

## Clarifying Questions
- question: Which data sources are included in the first migration phase?
  impact: high
- question: What reporting SLAs are expected by the business?
  impact: medium

## Notes
Scope intentionally limited to assessment and design pending clarification on data sources and SLAs.
```


Interaction with the PM Core Agent
- PM Core Agent detects `meta.current_phase` == `intake` and invokes this
  skill.
- After execution, PM Core Agent checks `open_questions` and `clarifying_questions`.
  - If any question has `impact: high` -> escalate to a human PM.
  - If no high-impact open questions -> advance to planning (or mark
    `meta.current_phase` = `planning-ready` if appropriate).

Maturity signal
- A healthy intake reduces uncertainty but does not eliminate it. If the
  skill returns zero clarifying questions for a real, non-trivial project,
  treat that as a potential failure mode.

Next steps
1. Use outputs as the single source of truth for downstream planning.
2. If satisfied, invoke Skill 2: High-Level Planning using only the
   returned `updated_project_state`.

Validation and testing
- Provide three test scenarios: minimal input, partial input, and rich
  input. Verify that high-impact information gaps produce `clarifying_questions`.
