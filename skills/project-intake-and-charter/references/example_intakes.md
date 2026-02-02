# Example Intakes

This file contains realistic example inputs and expected outputs to help test
the Project Intake & Charter skill. Use these examples in automated tests or
manual validation.

## Example 1 — Data platform migration (minimal input)

Input
```yaml
project_state:
  meta:
    name: Customer Data Platform Migration
    type: data
    client: ACME Corp
    current_phase: intake

user_input: >
  We want to migrate our current data platform to something more modern
  because reporting is slow and teams don’t trust the data.
```

Expected highlights
- Problem statement: slow reporting and low trust in analytics
- Business objectives: improve freshness and reliability; increase trust
- Scope: assessment and design in-scope; full dashboard implementation out-of-scope
- Clarifying questions: which data sources, expected SLAs

## Example 2 — Feature request for mobile app (partial input)

Input
```yaml
project_state:
  meta:
    name: Mobile Push Notifications
    type: product
    client: BetaApps
    current_phase: intake

user_input: >
  We need push notifications for new messages. PM asked to make it opt-in.
```

Expected highlights
- Clarify whether notifications are for all message types or only certain
  channels (e.g., direct message vs system alerts).
- Business objectives: increase engagement; reduce missed messages
- Success criteria: % of users who opt in, delivery rate
- Risks: privacy/regulatory concerns; platform fragmentation

## Example 3 — New marketing campaign analytics (rich input)

Input
```yaml
project_state:
  meta:
    name: Campaign Analytics Dashboard
    type: analytics
    client: RetailCo
    current_phase: intake

user_input: >
  Marketing needs a dashboard to measure channel ROI for the upcoming
  holiday campaign. They want daily KPIs, channel attribution, and a
  way to filter by region. Budget is limited and timeline is 6 weeks.
```

Expected highlights
- Separate business objectives (measure channel ROI, support daily
  decision-making) from solution requests (dashboard, filters).
- Success criteria: daily refresh, accuracy of attribution, time-to-insight
- Scope: analytics design and dashboard MVP in-scope; long-term attribution
  model out-of-scope unless budget permits
- Clarifying questions: precise definition of ROI, data availability, region list
