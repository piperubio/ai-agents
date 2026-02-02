# Example Risks & Issues

Use these examples to validate the Risk & Issue Management skill.

## Example 1 — Resource availability risk

Observations
```yaml
observations:
  - "Key architect availability is uncertain next month"
```

Expected output highlights
- New risk R-003: architect availability — probability: medium, impact: high,
  exposure: high → status: escalated. Mitigation: secure backup or adjust timeline.

## Example 2 — Scope issue from client request

Observations
```yaml
observations:
  - "Client requested additional reporting not in original scope"
```

Expected output highlights
- Issue I-002: client requesting additional reporting — severity: medium,
  impact_area: scope, recommended action: scope impact analysis and change
  discussion, escalation_required: true.

## Example 3 — External dependency degradation

Observations
```yaml
observations:
  - "Third-party API rate limits have been reduced"
```

Expected output highlights
- Risk: third-party API rate limit change — probability: high, impact: medium,
  exposure: medium → recommended mitigation: implement caching and retry
  policies; monitor and escalate if service-level failures are observed.
