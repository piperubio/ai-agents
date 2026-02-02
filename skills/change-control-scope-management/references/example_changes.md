# Example Change Requests

Use these examples to validate the Change Control / Scope Management skill.

## Example 1 — Small in-scope adjustment

Input
```yaml
change_request:
  description: "Minor wording change in existing dashboard copy"
```

Expected highlights
- classification: in_scope
- impact: low across scope and timeline

## Example 2 — Ambiguous request needing clarification

Input
```yaml
change_request:
  description: "Add more metrics to the analytics dashboard"
```

Expected highlights
- classification: unclear
- action: request clarification on which metrics, data availability, and priority

## Example 3 — New deliverable (out-of-scope)

Input
```yaml
change_request:
  description: "Client requests a new executive dashboard with custom KPIs"
```

Expected highlights
- classification: out_of_scope
- recommendation: escalate and present options (paid change, scope swap)
