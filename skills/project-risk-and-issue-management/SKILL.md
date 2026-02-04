---
name: project-risk-and-issue-management
description: >
  Risk & Issue Management: identify, assess, prioritize and manage risks and
  active issues in consulting projects. Use when monitoring project health,
  reviewing observations, or responding to new signals that may affect
  scope, timeline, cost, quality or trust.
---

# Risk & Issue Management

Purpose
- Identify, assess, prioritize, and manage project risks and active issues to
  enable proactive decision-making and controlled escalation. The skill is
  both preventive (risks) and reactive (issues) and focuses on practical
  recommendations, not theoretical models.

Risk vs Issue (key distinction)
- Risk: an uncertain event that could affect the project.
- Issue: a problem that is already occurring and affects execution.
- Never conflate risks and issues in outputs or recommendations.

Role: what this skill does and does not do
- This skill WILL:
  - Identify new risks and issues from observations
  - Re-evaluate existing risks and adjust probability/impact
  - Convert materialized risks into issues
  - Prioritize by probability and impact (qualitative)
  - Define mitigation/response strategies and recommended actions
  - Recommend escalation when exposure or severity is high

- This skill WILL NOT:
  - Make final executive decisions
  - Change project objectives, scope, or high-level plans
  - Execute technical mitigation actions
  - Normalize or downplay legitimate risks for political reasons

Inputs
```yaml
inputs:
  project_state: string (Markdown — uses the Project State Template in agents/pm-core-agent/pm-core-agent.md)
  observations: object
```

`observations` may include unstructured signals such as:
- schedule slips, team friction, ambiguous requirements, dependency changes,
- client feedback, organizational changes, new constraints

Outputs (contract)
```yaml
outputs:
  updated_project_state: string (Markdown — follows the Project State Template)
  risks:
    - id: string
      description: string
      probability: low | medium | high
      impact: low | medium | high
      exposure: low | medium | high
      mitigation_strategy: string
      status: open | monitored | escalated
  issues:
    - id: string
      description: string
      severity: low | medium | high
      impact_area: scope | timeline | cost | quality | trust
      recommended_action: string
      escalation_required: boolean
  escalation_notes: string
```

Risk evaluation model
- Use a simple qualitative exposure matrix:
  - High impact + High probability -> Escalate
  - High impact + Medium probability -> Act now
  - Low impact + High probability -> Monitor
  - Low impact + Low probability -> Acknowledge
- Avoid complex numeric scoring; prefer clear rationale and traceability.

Fields this skill may modify in project_state
- Allowed writes: `risks`, `issues`, `meta.project_health`, `meta.last_risk_review`.
- Must NOT modify: `objectives`, `scope`, `plan_high_level`, `milestones`.

Response strategies (valid options)
- For risks: Avoid, Mitigate, Transfer, Accept (with explicit justification)
- For issues: Contain, Resolve, Escalate
- Every recommended strategy must include a short rationale and an owner
  suggestion where possible.

Guardrails (must follow)
1. Always separate risks vs issues in outputs and narrative.
2. Be explicit about uncertainty and assumptions.
3. Do not hide political or reputational risks; surface them with care.
4. Avoid alarmist language without evidence; use factual observations.
5. Force escalation for high exposure or high-severity items.
6. Maintain traceability via stable IDs and timestamped changes.

Skill prompt (use this when invoking the skill)
```
You are a Risk & Issue Management skill for consulting projects.

Your task is to identify, assess, and manage project risks and active issues
based on the provided project state and observations.

You must:
- Clearly distinguish between risks (potential) and issues (actual)
- Identify new risks and reassess existing ones
- Detect when a risk has materialized into an issue
- Evaluate probability and impact using qualitative levels
- Define mitigation or response strategies with clear rationale
- Recommend escalation when exposure or severity is high
- Update the project state accordingly

You must NOT:
- Change objectives, scope, or the high-level plan
- Execute mitigation actions
- Minimize or hide risks for optimism
- Make executive decisions without escalation

Favor early detection, transparency, and decision support.
```

Example execution

Input
```yaml
observations:
  - "Key architect availability is uncertain next month"
  - "Client requested additional reporting not in original scope"
```

Output
```yaml
risks:
  - id: R-003
    description: Reduced availability of key architect during critical design phase
    probability: medium
    impact: high
    exposure: high
    mitigation_strategy: Secure backup resource or adjust timeline
    status: escalated

issues:
  - id: I-002
    description: Client requesting additional reporting beyond agreed scope
    severity: medium
    impact_area: scope
    recommended_action: Trigger scope impact analysis and formal change discussion
    escalation_required: true

escalation_notes: >
  Architect availability risk has high exposure and requires PM intervention.
  Scope-related issue requires client alignment before proceeding.
```

Interaction with the PM Core Agent
- Invoke this skill during regular risk reviews or when new observations arrive.
- If any risk has `exposure: high` or any issue has `escalation_required: true`,
  the PM Core Agent should escalate to a human PM and include `escalation_notes`.

Validation and testing
- Test with a set of observations covering: resource risk, scope creep,
  external dependency failure, and client dissatisfaction. Ensure outputs
  include IDs, clear rationale, and correct escalation decisions.
