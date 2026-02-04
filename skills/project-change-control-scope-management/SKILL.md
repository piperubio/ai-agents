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
```yaml
inputs:
  project_state: string (Markdown — uses the Project State Template in agents/pm-core-agent/pm-core-agent.md)
  change_request: object
```

`change_request` may be an informal sentence or a structured object. Examples:
- "Client asked for X"
- "Can we add Y without moving dates?"

Outputs (contract)
```yaml
outputs:
  change_assessment:
    classification: in_scope | out_of_scope | unclear
    rationale: string
  impact_analysis:
    scope: low | medium | high
    timeline: low | medium | high
    effort: low | medium | high
    quality: low | medium | high
    risk: low | medium | high
  response_options:
    - option: string
      tradeoffs: string
  recommendation:
    decision: accept | reject | defer | escalate
    justification: string
  updated_project_state: string (Markdown — follows the Project State Template)
  notes: string
```

Classification rules
- In-scope: does not alter objectives, introduces no new deliverables, and
  has low/absorbable impact.
- Unclear: ambiguous, under-specified, or has risk of scope creep; needs
  clarification and impact analysis.
- Out-of-scope: introduces new deliverables, changes objectives, or has
  medium/high impact on time or effort.

Fields this skill may modify in project_state
- Allowed writes: `scope` (only when change is approved), `decisions_log`,
  `risks` (if new risks emerge), `meta.current_phase`, `meta.project_health`.
- Must NOT modify: `objectives` (except via formal escalation process).

Guardrails (non-negotiable)
1. Treat every change as explicit; never assume implied approval.
2. Avoid silent acceptance: always show impact even if uncomfortable.
3. Offer alternatives and trade-offs, not only rejections.
4. Escalate when impact is medium or high.
5. Maintain traceability: who requested, when, what changed, and why.

Skill prompt (use this prompt when invoking the skill)
```
You are a Change Control and Scope Management skill for consulting projects.

Your task is to assess and manage change requests based on the current project state.

You must:
- Evaluate whether a request constitutes a scope change
- Classify the request as in-scope, out-of-scope, or unclear
- Analyze the potential impact on scope, timeline, effort, quality, and risk
- Propose clear response options with trade-offs
- Provide a recommendation with justification
- Update the project state only if a change is approved

You must NOT:
- Execute changes
- Negotiate directly with stakeholders
- Change project objectives without escalation
- Minimize impact for convenience

Favor transparency, control, and long-term trust over short-term accommodation.
```

Example (quick)

Input
```yaml
change_request:
  description: "Client requested adding an additional dashboard for executives"
```

Output (summarized)
```yaml
change_assessment:
  classification: out_of_scope
  rationale: Additional dashboard introduces a new deliverable not included in original scope

impact_analysis:
  scope: high
  timeline: medium
  effort: medium
  quality: low
  risk: medium

response_options:
  - option: Include dashboard as a paid change request
    tradeoffs: Extends delivery timeline and increases effort
  - option: Replace an existing deliverable
    tradeoffs: Maintains timeline but reduces original scope

recommendation:
  decision: escalate
  justification: New deliverable requires client decision on trade-offs
```

Interaction with PM Core Agent
- This skill is invoked when a change request is received or a user asks
  whether a signal is a change. If the recommendation is `escalate` or
  the impact is medium/high, PM Core Agent should surface the decision to
  a human PM for approval.

Validation and testing
- Test with a variety of change_request samples: trivial (in-scope),
  ambiguous (unclear), and substantive (out-of-scope). Verify traceability
  and that approved changes update the `scope` or `decisions_log`.
