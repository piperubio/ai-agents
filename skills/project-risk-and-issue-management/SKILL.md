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
- **project_state**: A Markdown document following the template in `pm-core-agent.md`.
- **observations**: Informal or structured signals (e.g., schedule slips, friction).

`observations` may include unstructured signals.

Outputs (contract)
The output must be a Markdown document following this structure:

# Output: Risk & Issue Management

## Risk & Issue Assessment
- **New/Updated Risks**: [ID, Description, Probability, Impact, Exposure, Status]
- **Identified Issues**: [ID, Description, Severity, Impact Area, Action, Escalation Required]

## Escalation Notes
[Rationale for any high-exposure or high-severity items]

## Updated Project State
[Full updated Markdown document]

Skill prompt (use this when invoking the skill)
```
You are a Risk & Issue Management skill for consulting projects.

Your task is to identify and manage project risks and active issues based on the
provided project_state (Markdown) and return a response following the
"# Output: Risk & Issue Management" Markdown format.

You must:
- Clearly distinguish between risks (potential) and issues (actual).
- Identify new risks and reassess existing ones in the Markdown tables.
- Detect when a risk has materialized into an issue.
- Update the project_state Markdown sections for "Risks" and "Open Questions".
- Recommend escalation when exposure or severity is high.

You must NOT:
- Change objectives, scope, or high-level plan details.
- Execute technical mitigation actions.
```

Example execution (realistic)

**Input**
- project_state: "# Project: Migration... ## Risks | ID | Description | ..."
- observations: "Key architect availability is uncertain next month"

**Output**
# Output: Risk & Issue Management

## Risk & Issue Assessment
- **New/Updated Risks**: R1 (Architect availability), Probability: medium, Impact: high, Exposure: high, Status: escalated.
- **Identified Issues**: None identified from this observation.

## Escalation Notes
Architect availability risk has high exposure and requires PM intervention.

## Updated Project State
# Project: Migration
...
## Risks
| ID | Description | Probability | Impact | Mitigation | Status |
|----|-------------|-------------|--------|------------|--------|
| R1 | Architect availability | medium | high | Backup resource | escalated |

Interaction with the PM Core Agent
- Invoke this skill during regular risk reviews or when new observations arrive.
- If any risk has `exposure: high` or any issue has `escalation_required: true`,
  the PM Core Agent should escalate to a human PM and include `escalation_notes`.

Validation and testing
- Test with a set of observations covering: resource risk, scope creep,
  external dependency failure, and client dissatisfaction. Ensure outputs
  include IDs, clear rationale, and correct escalation decisions.
