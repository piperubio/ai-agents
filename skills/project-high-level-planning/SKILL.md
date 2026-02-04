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
- **project_state**: A Markdown document following the template in `pm-core-agent.md`.
- **planning_parameters**: Optional preferences or constraints for the planning process.

Outputs (contract)
The output must be a Markdown document following this structure:

# Output: High-Level Planning

## Updated Project State
[Full updated Markdown document]

## Plan Details
- **Estimated Size**: S | M | L
- **Duration Range**: [Min weeks] - [Max weeks] weeks

## Clarifying Questions
- [Question] (Impact: low | medium | high)

## Notes
[AI observations and guidance]

Skill prompt (use this prompt when invoking the skill)
```
You are a High-Level Planning skill for consulting projects. Your input is a
project_state (Markdown) produced by the Project Intake & Charter skill.

Your task is to produce a concise, risk-aware high-level plan and return a
response following the "# Output: High-Level Planning" Markdown format.

You must:
- Update the "High-Level Plan", "Risks", and "Open Questions" sections in the project_state Markdown.
- Define 2–5 logical phases with clear goals and 1–3 milestones each.
- Provide measurable acceptance criteria for each milestone.
- Give a high-level size estimate (S/M/L) and a conservative duration range.
- Identify major dependencies and resource needs.

You must NOT:
- Produce task-level plans, exact schedules, or precise cost commitments.
- Invent missing facts.
```

Example execution (realistic)

**Input**
- project_state: "# Project: Customer Data Platform Migration..."
- planning_parameters: "None provided"

**Output**
# Output: High-Level Planning

## Updated Project State
# Project: Customer Data Platform Migration
...
## High-Level Plan
### Phases
- **Phase 1: Assessment**: Inventory sources, map pipelines. Deliverables: [Inventory, QA Report]. Effort: s.
- **Phase 2: Architecture**: Define target architecture. Deliverables: [Design Doc]. Effort: m.

## Plan Details
- **Estimated Size**: M
- **Duration Range**: 8 - 16 weeks

## Clarifying Questions
- Which data sources must be in phase 1? (Impact: high)

## Notes
Estimates assume access to data sources.

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
