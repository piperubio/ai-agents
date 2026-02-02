---
name: project-high-level-planning
description: >
  High-Level Planning: produce a concise, risk-aware, consultant-ready
  high-level plan from an intake-level project state. Use after a successful
  intake when `project_state` contains clear objectives, scope, stakeholders,
  and identified information gaps have been resolved or accepted.
---

# High-Level Planning

Purpose
- Turn the structured outputs from Project Intake & Charter into a
  consultant-quality high-level plan that is sufficient to: select a delivery
  approach, identify major milestones, surface critical dependencies and
  resource needs, and enable a subsequent detailed planning step.
- This skill intentionally avoids fine-grained scheduling, task-level
  breakdowns, or precise cost estimates.

Scope: What this skill does and does not do
- This skill WILL:
  - Produce a `plan_high_level` that contains phases, milestones, and
    acceptance criteria
  - Provide a high-level estimate expressed as ranges or T-shirt sizes (S/M/L)
  - Identify major dependencies, constraints, and resource needs
  - Update risks and assumptions based on planning analysis
  - Mark readiness for detailed planning (or escalate if blocking unknowns exist)

- This skill WILL NOT:
  - Produce a detailed task list or sprint backlog
  - Commit to exact timelines or precise cost figures
  - Replace stakeholder negotiation or contractual decisions

Inputs (OpenCode-friendly)
```yaml
inputs:
  project_state: object
  planning_parameters?: object  # optional preferences (e.g., preferred cadence)
```

Outputs (contract)
```yaml
outputs:
  updated_project_state: object
  plan_high_level:
    phases:
      - name: string
        goals: string
        milestones: [string]
        acceptance_criteria: [string]
    estimated_size: S|M|L
    duration_range: { min_weeks: int, max_weeks: int } | null
  clarifying_questions:              # only if unresolved gaps remain
    - question: string
      impact: low|medium|high
  notes: string
```

Fields this skill may write in project_state
- Allowed writes: `plan_high_level`, `risks` (update/add), `open_questions`,
  `meta.current_phase` (e.g., `detailed-planning-ready`), `resource_needs`.
- Must NOT write or modify: `decisions_log`, `communication`.

Guardrails (must follow)
1. Use only information already present in `project_state` or explicitly
   provided by the caller. Do not invent data.
2. When estimating, use ranges or qualitative sizes (S/M/L) and document
   assumptions that drove the sizing.
3. Elevate any unresolved `open_questions` with `impact: high` rather than
   guessing answers.
4. Keep the plan consultant-ready and actionable but avoid commit-level language
   (no "we will deliver by X date" unless a date range is explicitly requested
   and supported by evidence).

Skill prompt (use this prompt when invoking the skill)
```
You are a High-Level Planning skill for consulting projects. Your input is a
project_state produced by the Project Intake & Charter skill.

Your task is to produce a concise, risk-aware high-level plan that:
- Defines 2–5 logical phases with clear goals and 1–3 milestones each
- Provides measurable acceptance criteria for each milestone
- Gives a high-level size estimate (S/M/L) and a conservative duration range
- Identifies major dependencies and resource needs
- Updates risks and open questions (escalate high-impact gaps)

You must NOT:
- Produce task-level plans, exact schedules, or precise cost commitments
- Invent missing facts

When important information is missing, create `clarifying_questions` with an
impact rating. Prefer conservative assumptions and document them clearly.
All outputs must be structured and directly usable by downstream agents.
```

Example execution (based on intake example)

Input (derived from intake)
```yaml
project_state:
  meta:
    name: Customer Data Platform Migration
    current_phase: intake
  objectives:
    problem_statement: "Current data platform does not support timely and
      reliable reporting"
    business_objectives: ["Improve data freshness", "Increase stakeholder trust"]
  scope: {...}
  stakeholders: [...]
```

Output (summarized)
```yaml
plan_high_level:
  phases:
    - name: Assessment
      goals: Inventory sources, map pipelines, identify quick wins
      milestones: ["Data sources inventory complete", "Initial QA report"]
      acceptance_criteria: ["Inventory covers >90% of BI reports"]
    - name: Target Architecture & Prioritization
      goals: Define target architecture and migration phasing
      milestones: ["Target architecture approved", "MVP scope defined"]
      acceptance_criteria: ["MVP covers priority reports"]
    - name: Pilot & Handoff
      goals: Implement pilot migration for prioritized sources
      milestones: ["Pilot implemented", "Operational handoff"]
      acceptance_criteria: ["Pilot meets SLA and quality thresholds"]
  estimated_size: M
  duration_range: { min_weeks: 8, max_weeks: 20 }

clarifying_questions:
  - question: "Which data sources must be in phase 1?"
    impact: high

notes: >
  Estimates assume existing data sources are accessible and client can allocate
  one dedicated data engineer part-time during Assessment.
```

Interaction with the PM Core Agent
- PM Core Agent invokes High-Level Planning after intake completes and no
  unresolvable high-impact open questions remain.
- If planning returns `clarifying_questions` with `impact: high`, PM Core
  Agent should pause and escalate to a human PM.
- If the plan is ready, PM Core Agent marks `meta.current_phase` =
  `detailed-planning-ready` and invokes the Detailed Planning skill.

Validation and testing
- Test with 3 scenarios: small (S), medium (M), and large (L) projects. Verify
  that the skill produces phase-based plans and escalates high-impact unknowns.
