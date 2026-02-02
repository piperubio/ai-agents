# Example Monitoring Scenarios

Use these examples to validate the Monitoring & Control skill.

## Example 1 — Early warning (yellow)

Input
```yaml
latest_updates:
  - "Stakeholder validation sessions delayed two weeks"
  - "Team reports slower progress due to unclear requirements"
```

Expected highlights
- project_health: status: yellow
- deviations: timeline and assumptions, severity: medium
- forecast: likely next milestone delay if conditions persist
- alerts: recommend risk_issue_management

## Example 2 — Severe blocker (red)

Input
```yaml
latest_updates:
  - "Critical third-party service outage affecting data ingestion"
```

Expected highlights
- project_health: status: red
- deviations: quality/timeline, severity: high
- forecast: immediate milestone slippage and elevated risk
- alerts: recommend risk_issue_management and pm_core
