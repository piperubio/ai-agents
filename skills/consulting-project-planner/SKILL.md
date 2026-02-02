---
name: consulting-project-planner
description: "General-purpose, content-first project planning assistant: create or replan project plans, generate risk registers and concise pipeline status summaries. Use when you need to scope a project, replan after changes, prepare kickoff artifacts, or produce stakeholder-ready summaries. Triggers: 'plan project', 'create project plan', 'replan project', 'generate risk register'."
---

# Consulting Project Planner

Purpose

Produce stakeholder-ready project artifacts using a content-first contract: the skill defines the required semantic contents of each output (what must be present), not a required file format. Templates in `assets/` are optional examples.

Inputs (required vs optional)

- Required (minimum to start):
  - `projectName` (string)
  - `oneLiner` (string) — problem + user + outcome
  - `objectives` (array of strings)
  - `scopeIn` (array of strings) and `scopeOut` (array of strings)
  - `milestones` (array of objects: `{name,startDate,endDate,owner}`)
  - `team` (array of objects: `{role,name,capacity}`)
- Optional:
  - `constraints`, `assumptions`, `knownDependencies`, `knownRisks`
  - `desiredOutputs` (array: any of `project_plan`, `risk_register`, `pipeline_status`, `gantt`) — default: all

How to provide missing inputs

- Run the discovery briefing (`references/briefing-template.md`) with the client or ask follow-up prompts to collect missing fields.

Invocation examples (natural language)

- "Plan project Acme Checkout — 3-month MVP, backend + frontend, target 2026-05-15"
- "Replan 'Mobile Redesign' because of a 2-week API delay — update timeline and risk register"
- "Generate a risk register for Project X focusing on external vendor dependencies"

Deterministic Workflow (step-by-step)

1. Validate inputs; if required fields are missing, ask clarifying questions or run the briefing template.
2. Produce the one-liner and confirm V1 scope (limit to 3–5 core deliverables). Record explicit "Not Yet" items.
3. Build a vertical WBS: phases → epics → tasks. Aim for 4–8h atomic tasks; for each task record owner and estimate.
4. Map dependencies between tasks, compute the critical path, and apply contingency (recommended 15–25%) with rationale.
5. Allocate resources by role and availability; flag skill gaps and capacity constraints.
6. Identify risks from inputs and WBS; score probability × impact and propose mitigations.
7. Generate content-first outputs (see Outputs) and offer optional exports (CSV, spreadsheet, PPT) on request — exports are conversions of the semantic contents, not the primary contract.

Outputs (content-first descriptions)

Each output is defined by the semantic elements it must contain. Consumers may request any format (Markdown, CSV, JSON, PPTX), but the skill guarantees the content contract below.

- PROJECT_PLAN (canonical plan) — must include:
  - Executive summary: purpose, primary objective, expected outcome, plan version & last updated
  - One-liner
  - Objectives and success metrics / KPIs
  - Scope: In scope / Out of scope (explicit)
  - Deliverables and acceptance criteria with owners
  - Schedule & Milestones: list with start/end dates and owners
  - WBS: phases → epics → tasks with owners and estimates
  - Dependencies & critical path with contingency rationale
  - Resources & roles: capacity assumptions and named owners
  - Estimates & budget summary with method and contingency
  - Assumptions, constraints
  - Risks & mitigations (summary; full register exported separately)
  - Change control and handover checklist

- RISK_REGISTER — structured list for each risk containing:
  - id, title/description, probability (High/Med/Low or %), impact (High/Med/Low or scale), mitigation actions, owner, status, notes
  - recommended monitoring cadence and trigger conditions for escalation

- PIPELINE_STATUS — concise checkpoint summary containing:
  - current phase, percent complete, top 3 blockers, next milestones (with dates), critical dependencies, and a short communications summary for stakeholders

- GANTT (semantic timeline) — list of milestones/tasks with start/end dates and dependencies suitable for export to CSV or timeline tools

References & assets

- Use `references/briefing-template.md` for discovery. Use `references/estimation-guidelines.md` and `references/checklists.md` for estimates and QA.
- Use `assets/project-plan-template.md` as a skeleton if a file-based template is requested. `assets/` contains example templates but the skill's contract is content-first.

Quality and acceptance criteria

- Each produced artifact must include the semantic elements listed above. For example, a `PROJECT_PLAN` without a WBS or without owners is incomplete.
- When asked to export to a format (Markdown, CSV, JSON), confirm that the consumer accepts converted representations of the same semantic contents.

Progressive disclosure

- Keep the generated plan concise by default; expand sections on request. Load large references only when required.

Quick example (minimal)

- Input: `projectName: 'Acme Checkout', oneLiner: 'Enable secure checkout for Acme customers', milestones: [...]`
- Output: a `PROJECT_PLAN` containing the one-liner, scope, 4 milestones, WBS with owners and estimates, a short risk summary, and a `PIPELINE_STATUS` one-pager.

Best practices

- Prefer vertical slicing and deliveries that produce end-to-end value.
- Keep task estimates at the 4–8 hour granularity; use contingency for unknowns.
- Update the plan weekly and record assumptions and changes explicitly.

See `assets/` and `references/` for templates and examples. Templates are optional: rely on the content descriptions above as the authoritative contract.
