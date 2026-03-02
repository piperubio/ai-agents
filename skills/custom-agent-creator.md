---
name: custom-agent-creator
description: Skill to define focused agents, with a clear purpose, up to three concrete goals, and selected enabled skills.
version: 0.2.0
author: your_name_or_github
---

# Custom Agent Creator Skill

This skill provides a step-by-step workflow to define a high-confidence, purposeful agent: clear mission, up to three actionable goals, personality, I/O, and allowed agent skills. Follows best practices for agent clarity, reusability, and modularity inspired by the top open skills.

## Agent Definition Workflow

1. **Agent Name:**  
   _Example_: "Incident Supervisor"

2. **Main Purpose:**  
   _Describe in a single, clear sentence why this agent exists._
   - Example: "Monitor and classify incidents for automated prioritization."

3. **Goals (up to 3):**  
   - 1. _Example_: Detect critical incidents in real-time.
   - 2. _Example_: Notify the relevant people according to severity.
   - 3. _Example_: Generate weekly trend reports.

4. **Personality & Behavior:**  
   - _Example_: Formal and precise, never uses colloquial language.
   - Restrictions: Must never delete reports or ignore unresolved incidents.

5. **Expected Inputs:**  
   - _Example_: System logs, alerts, support tickets.

6. **Outputs / Actions:**  
   - _Example_: Email alerts, dashboard updates, PDF report generation.

7. **Enabled Skills:**  
   _Select from installed/available skills the agent can use._
   - [ ] notifications
   - [ ] email-sender
   - [ ] github-issues
   - [ ] pdf-generator
   - [ ] weather
   - ...

8. **(Optional) Template inspiration:**  
   - Base on: [Task Organizer], [Scraper], [Data Analyst], etc.

## Example Agent Definition

```yaml
agent:
  name: Incident Supervisor
  purpose: Monitor and classify incidents for automated prioritization.
  goals:
    - Detect critical incidents in real-time.
    - Notify the relevant people according to severity.
    - Generate weekly trend reports.
  personality: Formal and precise.
  restrictions: Must never delete reports or ignore unresolved incidents.
  inputs: System logs, alerts, tickets.
  outputs: Email alerts, PDF reports.
  skills:
    - github-issues
    - email-sender
    - pdf-generator
```

## Validation & Best Practices Checklist

- [x] Purpose is clear and actionable
- [x] 1-3 goals, each measurable
- [x] Personality and boundaries defined
- [x] Inputs/outputs concrete
- [x] Only necessary skills enabled
- [x] Example included
- [x] Follows markdown skill metadata in frontmatter

## Activation & Usage

Follow the guided prompts to collect details and generate your agent definition file. Ready for install or extension.
