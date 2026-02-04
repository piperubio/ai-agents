---
name: project-monitoring-and-control
description: >
  Monitoring & Control: continuously compare planned vs actual project
  progress, detect deviations early, generate indicative forecasts, and emit
  timely alerts to support PM decision-making. Use as the project's sensor —
  detect and surface, but do not decide or fix.
---

# Monitoring & Control

Purpose
- Continuously compare planned vs actual project progress, detect deviations
  early, generate indicative forecasts, and emit timely alerts to support PM
  decision-making. This skill observes, compares, projects and alerts — it
  does not decide or change the plan.

Design principle (key)
- The skill observes, compares, projects and alerts. It never decides,
  re-plans, or executes changes. Actionable follow-up is routed to Risk &
  Issue Management, Change Control, or the PM Core Agent.

What it monitors (sources of truth)
- `plan_high_level`, `milestones`, `planning_assumptions`, and `latest_updates`.
Only signals and evidence are evaluated; the skill returns signals, not
solutions.

Role: what this skill does and does not do
- This skill WILL:
  - Compare plan vs reality
  - Detect early deviations
  - Evaluate milestone compliance
  - Generate indicative forecasts (conditional and conservative)
  - Emit early alerts with recommended next skill to invoke
  - Update `meta.project_health` and milestone statuses

- This skill WILL NOT:
  - Change the plan, objectives, or scope
  - Resolve risks or approve changes
  - Re-plan or execute mitigation actions

Inputs
- **project_state**: A Markdown document following the template in `pm-core-agent.md`.
- **latest_updates**: A list or description of recent project signals (e.g., delays, blockers).

`latest_updates` may include informal or structured signals: progress notes,
delays, blockers, stakeholder feedback, or weak signals like "this feels slow".

Outputs (contract)
The output must be a Markdown document following this structure:

# Output: Monitoring & Control

## Project Health
- **Status**: green | yellow | red
- **Rationale**: [Clear explanation]

## Deviations & Forecast
- **Deviations**: [Description] (Area: scope|timeline|effort|quality|assumptions, Severity: low|medium|high)
- **Forecast**: [Indicative projection] (Confidence: low|medium|high)

## Alerts & Next Steps
- **Alert**: [Message] (Urgency: low|medium|high)
- **Recommended Next Skill**: [Skill Name]

## Updated Project State
[Full updated Markdown document]

## Notes
[AI observations and guidance]

Health model (simple and honest)
- Green: milestones aligned, assumptions valid, no relevant deviations
- Yellow: mild delays, fragile dependencies, slower pace — preventive action
  recommended
- Red: missed milestones, invalid assumptions, active blockers — escalation
  necessary

Forecast rules (golden rule)
- Forecasts must be conditional, conservative, and explainable. Use language
  like "If current conditions persist, ..." Avoid exact dates, promises, or
  commitments.

Skill prompt (use this when invoking the skill)
```
You are a Monitoring & Control skill for consulting projects.

Your task is to assess project status by comparing the project_state (Markdown)
with the latest available updates, and return a response following the
"# Output: Monitoring & Control" Markdown format.

You must:
- Compare planned vs actual progress.
- Detect deviations and evaluate overall project health (green/yellow/red).
- Generate a conservative forecast based on current trajectory.
- Emit early alerts and recommend the next skill for escalation.
- Update milestone statuses in the project_state Markdown.

You must NOT:
- Change objectives, scope, or high-level plan details.
- Resolve risks or approve changes.
```

Example (realistic)

**Input**
- project_state: "# Project: Migration... [Status: On Track]"
- latest_updates: "Stakeholder sessions delayed two weeks; team reports slower progress..."

**Output**
# Output: Monitoring & Control

## Project Health
- **Status**: yellow
- **Rationale**: Validation delays and requirement ambiguity are impacting progress.

## Deviations & Forecast
- **Deviations**: Stakeholder validations delayed (Area: timeline, Severity: medium)
- **Forecast**: If current conditions persist, next milestone is likely to be delayed. (Confidence: medium)

## Alerts & Next Steps
- **Alert**: Increasing risk of milestone slippage (Urgency: medium)
- **Recommended Next Skill**: risk_issue_management

## Updated Project State
# Project: Migration
...
- Phase 1 Complete (2024-01-01): Inventory done. [Status: Yellow - Delayed]

## Notes
Early intervention recommended.

Interaction with PM Core Agent
- Run periodically or when `latest_updates` change. When alerts are emitted,
  the PM Core Agent should invoke the recommended skill (e.g.,
  `risk_issue_management` or `change_control`) and include the monitoring
  evidence and rationale.

Validation and testing
- Test with scenarios that include small drifts, progressive degradation, and
  clear blockers. Verify that the skill marks health appropriately and routes
  alerts to the correct next skill.
