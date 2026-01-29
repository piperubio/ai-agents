---
name: consulting-project-planner
description: "Create comprehensive project plans for consulting and engineering engagements: define scope, WBS, timeline with dependencies, resource allocation, risk register, deliverables, and client-facing artifacts. Use when you need to create a new project plan, replan after changes, prepare kickoff materials, or produce a clear PROJECT_PLAN.md for stakeholders."
---

# Consulting Project Planner

Purpose

Provide a concise, repeatable workflow to produce professional project plans for consulting and engineering engagements. Focus on clear scope definition, vertical-sliced work breakdown structures (WBS), dependency-aware timelines, resource allocation, and an auditable risk register.

When to use (examples included in description above)

- New project scoping and planning
- Replanning after delays or scope changes
- Preparing client kickoff materials and acceptance criteria
- Producing deliverables to hand to execution teams or clients

Quick triggers (natural language examples)

- "plan project [Project Name]"
- "create project plan for [Client]"
- "replan project [Project Name]"
- "quick project kickoff for [Idea]"
- "generate risk register for [Project]"

Core workflows

- Create New Project Plan
  1. Run the briefing template (references/briefing-template.md) with the client to collect objectives, constraints, stakeholders, and acceptance criteria.
  2. Write a one-liner (problem + target user + key outcome).
  3. Define V1 scope (max 5 core features/deliverables) and a "Not Yet" list.
  4. Build WBS: phases → epics → tasks (aim for 4–8 hour atomic tasks). Record owner and estimate for each task.
  5. Map dependencies and compute critical path; apply contingency (recommended 15–25%).
  6. Allocate resources by role and availability; note skill gaps.
  7. Produce `PROJECT_PLAN.md` (see assets/project-plan-template.md) and `PIPELINE_STATUS.md`.

- Update / Replan
  1. Compare actual progress vs planned (dates, completed tasks).
  2. Identify blockers and external dependencies.
 3. Recalculate dates and update dependencies.
 4. Update risk register and resource plan.
 5. Communicate changes and publish revised `PROJECT_PLAN.md`.

- Quick Kickoff (MVP/POC)
  1. One-liner and 3–5 core features.
  2. Select stack and minimal architecture assumptions.
  3. Create a 2-week sprint plan with daily checkpoints.
  4. Produce minimal project artifacts: `PROJECT_PLAN.md` (trimmed), `PIPELINE_STATUS.md`.

Outputs

- `PROJECT_PLAN.md` — canonical project plan for stakeholders (use assets/project-plan-template.md)
- `PIPELINE_STATUS.md` — current stage and checkpoint status
- `RISK_REGISTER.md` — structured list of risks with probability, impact, and mitigation
- `GANTT.csv` or simple timeline table (optional export by tooling)

References and templates

- `references/briefing-template.md` — client briefing form (use at discovery)
- `references/estimation-guidelines.md` — estimation factors and size categories
- `references/checklists.md` — kickoff, QA, and handover checklists
- `assets/project-plan-template.md` — `PROJECT_PLAN.md` skeleton to copy into project root

Best practices (short)

- Enforce a scope fence: always record what is out of V1.
- Use vertical slicing: deliver end-to-end increments instead of layered work.
- Plan for ~70% effective capacity per person to allow for meetings and context switching.
- Update the plan weekly and track assumptions explicitly.

Integration notes

This skill contains templates and references only. For automation or exports (Excel, PPTX, issue creation) attach separate tooling or scripts; keep outputs simple and human-readable by default.

See the `references/` and `assets/` folders for templates to use while running the workflows.
