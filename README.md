# IA Agents: Configurations, Templates & Skill Suites

This repository centralizes agents, skills, and reusable templates for commercial and project management flows in technology consulting (Software, Data, AI). The architecture allows robust orchestration, traceability (“state as brain”), and seamless transitions from sale to delivery and project closure—extensible to other domains.

---

## 🧭 General Structure

- **agents/**: Main agents (commercial, PM, others)
- **skills/**: Specialized skills, organized per pipeline/purpose
    - commercial skills (`commercial-*` prefix)
    - PM/project skills (`project-*` prefix)
    - utility/cross-cutting skills
- **state templates**: `commercial-state.md`, `project-state.md` as single sources of truth (created on first run)

---

## 🚦 Main Orchestrator Agents

- `agents/commercial-core-agent/commercial-core-agent.md`
  Commercial orchestrator for B2B consulting sales and pipeline. Directs each phase using a dedicated skill, manages flow, and bridges into delivery (PM Suite).

- `agents/pm-core-agent/pm-core-agent.md`
  Project Manager AI for execution and detailed control of consulting projects (software, data, cloud). Orchestrates PM skills, manages state, tasks, risks, quality, and closure.

---

## 🧩 Skills – By Pipeline

### Commercial Pipeline (Consulting Sales)
| Phase                | Skill Dir                                | Short Description                                                      |
|----------------------|------------------------------------------|-----------------------------------------------------------------------|
| Prospecting          | commercial-prospecting                   | Research, score and profile clients/leads (ICP, maturity, etc.)        |
| Outreach             | commercial-outreach                      | Omnichannel outreach sequences, consultative tone                      |
| Discovery            | commercial-discovery                     | B2B discovery meetings, SPIN, stakeholder/agenda mapping, notes        |
| Qualification        | commercial-qualification                 | Opportunity scoring (BANTT), go/no-go                                  |
| Solution Design      | commercial-solution-design               | Pre-sales technical solution, roadmap, estimation, risks               |
| Proposal             | commercial-proposal-writer               | Formal proposal, pricing, workplan export (feeds PM suite)             |
| Negotiation          | commercial-negotiation                   | Consulting negotiation playbooks, handling objections                  |
| Account Growth       | commercial-account-growth                | Expansion, upsell/cross-sell, delivery/closure feedback loop           |

### Project Management Pipeline (PM Suite)
| Phase              | Skill Dir                                | Short Description                                                     |
|--------------------|------------------------------------------|-----------------------------------------------------------------------|
| Intake & Charter   | project-intake-and-charter               | Turn an ambiguous project request into a clear foundation              |
| Planning           | project-planning                         | Detailed project plan, WBS, budget, schedule                          |
| Stewardship        | project-stewardship                      | Daily ops, task-log, status report, blocker management                |
| Quality Mgmt       | project-quality-management               | Review log, validate deliverables, quality control                    |
| Risks & Changes    | project-risks-and-changes                | Risk analysis, issue handling, change control                         |
| Stakeholder Comms  | project-stakeholder-communication        | Stakeholder-tailored comms, templates, reports                        |
| Closure & Learning | project-closure-and-learning             | Formal closure, lessons learned, final report                         |

### Utility / Cross-Cutting Skills
| Skill Dir                        | Short Description                                  |
|----------------------------------|----------------------------------------------------|
| brainstorming                    | Structured ideation/brainstorming                  |
| dispatching-parallel-agents      | Concurrent/parallel agent execution                |
| product-customer-discovery       | Product-focused exploratory discovery              |

---

## 🔗 Integration and Commercial–PM Pipeline Flow

```
Prospecting → Outreach → Discovery → Qualification → Solution Design → Proposal → Negotiation → Close
                                                                               ↓
                                                            project-intake-and-charter (PM Suite)
                                                                               ↓
Account Growth ← project-closure-and-learning ← ... PM delivery lifecycle ...
```

- The `workplan-and-estimate.md` output from the Proposal skill is fed directly into project onboarding (PM Suite).
- On project closure or learning output (`project-closure-and-learning`), Account Growth picks up for expansion/case study/etc, closing the business loop.

---

## 📚 State as "Brain" & Conventions
- Each pipeline uses a single state file (`commercial-state.md`, `project-state.md`) as the editable source of truth for agents/skills.
- All updates are logged with author and reason (no silent changes).
- Skills consume and expose only what's needed for their stage (“progressive disclosure”).
- Names and structure are consistent for easy expansion, integration and testing.

---

## ✨ Usage & Extension
- Start orchestration from `commercial-core-agent` (for sales) or `pm-core-agent` (for projects). State files will be created automatically.
- Add new skills by following local conventions (SKILL.md + references/).
- Customize or iterate on artifacts, checklists, or flows to fit your specific processes.

---

For detailed, stage-specific instructions, see each phase’s SKILL.md and the references/ folder. The entire ecosystem is intended to be extended and adapted as your operating model evolves.
