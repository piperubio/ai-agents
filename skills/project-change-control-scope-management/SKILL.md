---
name: project-change-control-scope-management
description: >
  Change Control / Scope Management: evaluate, manage, and formalize scope
  change requests for consulting projects. Use when a change request, signal,
  or event requires a decision about whether the work is a change and how to
  respond with transparency and controlled escalation.
---

# Change Control / Scope Management

Purpose
- Evaluate, manage, and formalize changes to project scope to ensure
  transparency, impact awareness, and controlled decision-making. This skill
  protects the original agreement and avoids implicit acceptance of scope
  changes.

Design principle
- This skill DOES NOT detect changes automatically. It accepts `change_request`
  inputs (informal or structured) and answers: Is this a change? If so, is it
  in-scope, out-of-scope, or unclear? What is the impact? What options exist?

What counts as a change
- Valid inputs include: client requests, new functional/technical
  requirements, priority shifts, changes to assumptions or constraints
  (deadlines, resourcing, compliance), or repeated small adjustments
  indicating scope creep.

Role: what this skill does and does not do
- This skill WILL:
  - Classify requests as `in_scope`, `out_of_scope`, or `unclear`
  - Analyze impact on scope, timeline, effort, quality, risk and trust
  - Produce response options with trade-offs
  - Recommend a decision (accept / reject / defer / escalate)
  - Formalize approved changes and update project state

- This skill WILL NOT:
  - Execute the change or negotiate directly with stakeholders
  - Unilaterally change strategic objectives
  - Perform detailed replanning

Inputs
- **project_state**: A Markdown document following the template in `pm-core-agent.md`.
- **change_request**: Informal or structured request (e.g., "Client asked for X").

`change_request` may be an informal sentence or a structured object.

Outputs (contract)
The output must be a Markdown document following this structure:

# Output: Change Control / Scope Management

## Assessment & Impact
- **Classification**: in_scope | out_of_scope | unclear
- **Rationale**: [Clear explanation]
- **Impact Analysis**: [Scope/Timeline/Effort/Quality/Risk impact levels]

## Response & Recommendation
- **Response Options**: [Description of options and trade-offs]
- **Recommendation**: accept | reject | defer | escalate (Justification: [Text])

## Updated Project State
[Full updated Markdown document]

## Notes
[AI observations and guidance]

Skill prompt (use this prompt when invoking the skill)
```
You are a Change Control and Scope Management skill for consulting projects.

Your task is to assess and manage change requests based on the project_state (Markdown),
and return a response following the "# Output: Change Control / Scope Management"
Markdown format.

You must:
- Evaluate whether a request constitutes a scope change.
- Classify the request and analyze the potential impact.
- Propose clear response options with trade-offs.
- Provide a recommendation with justification.
- Update the project_state Markdown if a change is approved.

You must NOT:
- Execute changes or negotiate directly with stakeholders.
- Minimize impact for convenience.
```

Example (quick)

**Input**
- project_state: "# Project: Migration... ## Scope ### In Scope - Data ingestion."
- change_request: "Client requested adding an additional dashboard for executives"

**Output**
# Output: Change Control / Scope Management

## Assessment & Impact
- **Classification**: out_of_scope
- **Rationale**: Additional dashboard introduces a new deliverable.
- **Impact Analysis**: Scope: high, Timeline: medium, Effort: medium, Quality: low, Risk: medium.

## Response & Recommendation
- **Response Options**: Include as paid change (extends timeline) or replace an existing deliverable.
- **Recommendation**: escalate (Justification: New deliverable requires client decision on trade-offs).

## Updated Project State
# Project: Migration
...
## Decisions Log
| Date | Decision | Rationale | Approved By |
|------|----------|-----------|-------------|
| 2024-01-01 | Dashboard request | Identified as out-of-scope. | PM Core |

## Notes
New deliverable identified.

Interaction with PM Core Agent
- This skill is invoked when a change request is received or a user asks
  whether a signal is a change. If the recommendation is `escalate` or
  the impact is medium/high, PM Core Agent should surface the decision to
  a human PM for approval.

Validation and testing
- Test with a variety of change_request samples: trivial (in-scope),
  ambiguous (unclear), and substantive (out-of-scope). Verify traceability
  and that approved changes update the `scope` or `decisions_log`.
