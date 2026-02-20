# BANTTD Scoring Models Reference

## Table of Contents

1. [BANTTD Detailed Rubrics](#banttd-detailed-rubrics)
2. [Budget Scoring Guide](#budget-scoring-guide)
3. [Authority Mapping Guide](#authority-mapping-guide)
4. [Need Urgency Matrix](#need-urgency-matrix)
5. [Timeline Assessment](#timeline-assessment)
6. [Tech-fit Assessment Matrix](#tech-fit-assessment-matrix)
7. [Decision Date Assessment](#decision-date-assessment)
8. [Deal Size Estimation Guide](#deal-size-estimation-guide)
9. [Pipeline Stage Exit Criteria](#pipeline-stage-exit-criteria)
10. [Re-qualification Triggers](#re-qualification-triggers)
11. [Minimum Engagement Thresholds](#minimum-engagement-thresholds)

---

## BANTTD Detailed Rubrics

### Budget (0-20)

| Score | Criteria | Example |
|-------|----------|---------|
| 0 | No budget signals. Prospect explicitly states no funding available. | "We have no budget for external help this year." |
| 5 | General willingness to invest but no budget discussed. Cost sensitivity expressed. | "We might look into this eventually, but it's not a priority spend." |
| 10 | Budget exists but not allocated to this initiative. Needs internal approval. | "We'd need to get approval from finance. Our department has discretionary funds." |
| 15 | Budget range discussed and within our typical engagement size. Previous consulting spend confirmed. | "We've set aside low six figures for this initiative. We spent $150K with [competitor] last year." |
| 20 | Budget explicitly confirmed, allocated, and aligned with our engagement model. Purchase process known. | "We have $250K approved for Q3. Procurement needs a SOW and three references." |

### Authority (0-20)

| Score | Criteria | Example |
|-------|----------|---------|
| 0 | No access to anyone with influence. Contact is an individual contributor with no path upward. | Intern or junior analyst reached out "just exploring." |
| 5 | Contact is mid-level. Decision-making process unclear. No champion identified. | Director-level contact, unsure who signs off or how decisions are made. |
| 10 | Talking to an influencer. Path to the decision maker is clear but not yet navigated. | VP of Engineering knows we need CTO sign-off, willing to make the introduction. |
| 15 | Champion identified and actively engaged. Decision maker known but not yet met. | VP is championing internally, has presented to CTO, arranging a meeting. |
| 20 | Direct access to economic buyer. Champion identified and active. Buying committee mapped. | CTO in meetings, VP championing, procurement process shared. |

### Need (0-20)

| Score | Criteria | Example |
|-------|----------|---------|
| 0 | No discernible need. Prospect is browsing or fulfilling a research task. | "Just wanted to understand what's out there." |
| 5 | Latent need. Prospect does not fully recognize the problem or its impact. | "Our reporting is a bit slow, but it works." |
| 10 | Need acknowledged but positioned as "nice to have" or "future priority." | "We know we need to modernize, but it's not urgent." |
| 15 | Clear pain identified. Business impact understood but not fully quantified. Actively evaluating. | "We're losing 2 weeks per reporting cycle. We're talking to a few firms." |
| 20 | Acute, quantified pain. Prospect explicitly states "we need help now." Failed internal attempts. | "This is costing us $500K/quarter in delayed decisions. We tried internally and failed." |

### Timeline (0-20)

| Score | Criteria | Example |
|-------|----------|---------|
| 0 | No timeline. No intent to act. "Just exploring for future reference." | "No plans to start anything. Just building a vendor list." |
| 5 | "Eventually" or "when we have bandwidth." No urgency signal. | "Maybe next fiscal year, depends on other priorities." |
| 10 | "This year" or "next quarter." Intent exists but no hard deadline. | "We'd like to kick this off in Q3 if things align." |
| 15 | "Want to start within this quarter." Clear intent to move. Internal momentum building. | "We need to show progress by end of quarter. Team is ready." |
| 20 | Specific external deadline driving urgency. Regulatory, contractual, or market event. | "New regulation takes effect Jan 1. We must be compliant." |

### Tech-fit (0-20)

| Score | Criteria | Example |
|-------|----------|---------|
| 0 | No overlap with our capabilities. Would require entirely new expertise. | Prospect needs embedded firmware engineering; we do cloud platforms. |
| 5 | Minimal overlap. Would need to subcontract >50% of the work. | Core need is SAP implementation; we have some integration capability only. |
| 10 | Moderate fit. Can deliver but would need significant ramp-up or learning. | Data engineering is core for us, but their specific tooling (Kafka, Flink) requires team upskilling. |
| 15 | Strong fit. Aligns with our expertise with minor stretch areas (<20% new). | Data platform build with a small component of ML ops we've done once before. |
| 20 | Perfect match. Core capabilities, directly relevant case studies, proven delivery. | Cloud migration + API modernization — three similar engagements in portfolio. |

### Decision Date (0-20)

Is there a specific date by which the prospect expects to make a decision? Is it tied to a business event? Is it near-term enough to drive a reliable forecast?

| Score | Criteria | Example |
|-------|----------|---------|
| 0 | No decision date. No intent to decide. "We have no timeline for this." | "We are just building a vendor list, no plans to move this year." |
| 5 | Vague future intent. "Next fiscal year" or "when we get to it." No event driving it. | "Maybe next year if budget is approved." |
| 10 | Directional but imprecise. "In the next 2-3 quarters." No hard date or event named. | "Probably H2 this year, but nothing is locked in." |
| 15 | Clear and near-term. "Within this quarter." Specific window, even if no exact date. Internal alignment building. | "We want to decide by end of March. Team is aligned." |
| 20 | Specific date confirmed, tied to a business event (product launch, compliance deadline, board meeting, budget cycle). | "We need to sign by April 15 — that is when our fiscal year budget expires." |

**Why this dimension matters**: A high-scoring deal on all other dimensions but with no decision date is a pipeline liability. Without a date, urgency is unverifiable, forecasting is unreliable, and deals tend to stall indefinitely.

**Decision date vs. timeline**: Timeline (T) measures urgency to start the work. Decision Date (D) measures when they will choose a vendor. These are related but distinct — a prospect can have high urgency to solve the problem (T = 18) but no clear date for vendor selection (D = 5). Both matter.

#### Decision Date Scoring Signals

| Signal | Score Impact |
|--------|-------------|
| Specific calendar date given | 18-20 |
| Date tied to named business event (board meeting, launch, compliance deadline) | 16-20 |
| "This quarter" with named month | 14-16 |
| "This quarter" without specific month | 12-14 |
| "This year, probably H1/H2" | 8-10 |
| "Next year" or "next fiscal year" | 4-6 |
| "When we get to it" or "no particular timeline" | 0-3 |

#### Add 2-3 points if:
- Multiple stakeholders independently reference the same decision date.
- Prospect is actively requesting contract/proposal timeline from all vendors.
- Prospect mentions a budget expiration or allocation deadline.

#### Reduce 2-3 points if:
- The date has already shifted once in this process.
- The date is owned by a stakeholder we have not yet met.
- The date is contingent on another internal initiative completing first.

---

## Budget Scoring Guide

### Signs of Real Budget

- **Previous consulting spend**: Prospect has hired consultants before and knows the cost range.
- **Allocated line item**: Budget explicitly earmarked for this type of initiative.
- **Innovation or transformation fund**: Dedicated fund for strategic initiatives.
- **Department vs. project budget**: Department budgets are more flexible; project budgets signal commitment.
- **Fiscal year timing**: Early in fiscal year = more budget flexibility. Late = constrained or "use it or lose it."

### Red Flags

- "We need to build a business case first" — budget not yet secured.
- "Can you help us justify the spend?" — no champion with budget authority.
- "What's the cheapest option?" — cost-driven, not value-driven.
- Comparing to product/SaaS pricing — misunderstanding of consulting engagement model.
- No prior consulting spend — may not understand the investment level required.

### Budget Range Assessment

| Signal | Likely Range |
|--------|-------------|
| Individual contributor exploring | $0 (no real budget) |
| Department discretionary | $25K-$75K |
| Director-approved initiative | $75K-$200K |
| VP/C-level strategic initiative | $200K-$500K |
| Board-mandated transformation | $500K+ |

---

## Authority Mapping Guide

### Scoring Access to Decision Makers

Map the buying committee and score based on coverage:

| Role | Identified? | Engaged? | Supportive? |
|------|------------|----------|-------------|
| Economic Buyer (signs the check) | Y/N | Y/N | Y/N |
| Champion (sells internally for us) | Y/N | Y/N | Y/N |
| Technical Evaluator (validates fit) | Y/N | Y/N | Y/N |
| End Users (will use the solution) | Y/N | Y/N | Y/N |
| Blocker (could veto) | Y/N | Y/N | Known? |

### Scoring Rules

- Economic buyer identified AND engaged = 15+ baseline.
- Champion active but no buyer access = 10-14 ceiling.
- Only mid-level contacts, no path to buyer = 5-9 ceiling.
- No identified decision maker = 0-4.

### Champion Validation Questions

- Can the champion articulate the problem in business terms?
- Has the champion secured internal meetings for us?
- Does the champion have credibility with the economic buyer?
- Is the champion willing to share internal information (org chart, budget process, competitors)?

---

## Need Urgency Matrix

Cross-reference pain severity with pain frequency to determine urgency score.

|  | Rare (annual) | Occasional (quarterly) | Frequent (weekly/daily) |
|--|---------------|----------------------|------------------------|
| **Critical** (revenue/compliance at risk) | 12-14 | 15-17 | 18-20 |
| **Significant** (efficiency/competitive impact) | 8-11 | 10-14 | 14-17 |
| **Moderate** (inconvenience/technical debt) | 3-6 | 5-9 | 8-12 |
| **Low** (nice to have) | 0-3 | 2-5 | 4-7 |

### Need Validation Signals

- **Strong need**: Prospect quantifies the problem in dollars or time. Failed internal attempts. Multiple stakeholders confirm the pain.
- **Moderate need**: Pain is real but not quantified. Prospect is comparing options. Single stakeholder perspective.
- **Weak need**: Prospect cannot articulate specific impact. Driven by curiosity or industry trend. No internal urgency.

---

## Timeline Assessment

### Hard Deadlines (score 16-20)

External, immovable events creating urgency:

- Regulatory compliance deadlines
- Contractual obligations (SLA, partnership launch)
- Market events (product launch, competitive response)
- Board mandates with specific dates
- Fiscal year budget expiration ("use it or lose it")

### Soft Deadlines (score 8-15)

Internal, movable targets:

- Strategic planning cycles ("before Q1 planning")
- Executive aspiration ("I'd like this done by year-end")
- Team availability windows ("our architect is free starting March")
- Budget cycle alignment ("submit for next year's budget")

### No Deadline (score 0-7)

- "When we get to it"
- "After other priorities"
- "We're just exploring"
- No compelling event identified

### Timeline Compression Indicators

Add 2-3 points if:
- Prospect asks about fastest start date.
- Prospect is willing to adjust scope to meet timeline.
- Multiple stakeholders reference the same deadline independently.

---

## Tech-fit Assessment Matrix

Map our capabilities against their needs. Score based on coverage.

### Capability Categories

| Category | Our Strength (1-5) | Their Need (1-5) | Fit Score |
|----------|-------------------|------------------|-----------|
| Software Engineering | | | |
| Data Engineering | | | |
| Data Science / AI-ML | | | |
| Cloud Infrastructure | | | |
| Architecture / Strategy | | | |
| Other (specify) | | | |

### Scoring Formula

- Fit Score = min(Our Strength, Their Need) for each category.
- Weight by proportion of engagement each category represents.
- Penalize if subcontracting would exceed 30% of total effort.

### Subcontracting Penalty

| Subcontract % | Penalty |
|---------------|---------|
| 0-10% | No penalty |
| 11-20% | -2 points |
| 21-30% | -4 points |
| 31-50% | -6 points (flag as risk) |
| >50% | -10 points (recommend disqualify on tech-fit) |

### Case Study Match

Add bonus points for directly relevant case studies:
- Same industry + same problem = +3 points (cap at 20).
- Same problem, different industry = +2 points.
- Same industry, different problem = +1 point.

---

## Deal Size Estimation Guide

### Time & Materials (T&M)

```
Deal Size = Team Size x Blended Rate x Duration (months)
```

| Team Size | Typical Engagement |
|-----------|--------------------|
| 1-2 people | Staff augmentation or advisory |
| 3-5 people | Standard project team |
| 6-10 people | Large engagement or program |
| 10+ people | Transformation program |

Provide estimate as a range: optimistic (80% confidence) to conservative (50% confidence).

### Fixed Price

Scope-based estimation:
1. Define deliverables and acceptance criteria.
2. Estimate effort per deliverable.
3. Apply rate card and add risk buffer (15-25%).
4. Quote as fixed price with change order provisions.

### Outcome-Based

Value-share or success-fee model:
1. Quantify the prospect's expected business outcome.
2. Define measurable success metrics.
3. Price as percentage of value delivered (typically 10-30%).
4. Include base fee + success component.

### Estimation Confidence Levels

| Information Available | Confidence | Range Width |
|----------------------|------------|-------------|
| Detailed scope + technical assessment | High | +/- 15% |
| Discovery notes + general understanding | Medium | +/- 30% |
| Initial conversation only | Low | +/- 50% |

---

## Pipeline Stage Exit Criteria

Define minimum BANTTD scores required to advance from each stage. Scores are out of 120 (6 dimensions × 0-20).

| Stage | Minimum Total | Required Dimensions | Additional Criteria |
|-------|--------------|--------------------|--------------------|
| Lead → Qualified | 48+ | Need >= 10 | Qualification meeting completed, P.U.D.T.F >= 22 |
| Qualified → Solution Design | 84+ | Budget >= 10, Authority >= 10 | Champion identified |
| Solution Design → Proposal | 84+ | All dimensions >= 10 | Economic buyer engaged |
| Proposal → Negotiation | 90+ | Budget >= 15, Timeline >= 10, Decision Date >= 10 | Budget confirmed, decision date known |
| Negotiation → Closed Won | 96+ | Authority >= 15, Budget >= 15 | Contract terms agreed |

### Stage Regression Rules

- Move opportunity back one stage if any required dimension drops below threshold.
- Move to Nurture if total score drops below 48 at any stage.
- Move to Disqualified if any override trigger fires (see Guardrails in SKILL.md).

---

## Re-qualification Triggers

### Time-Based

- **30-day stale**: Opportunity has not advanced stages in 30 days. Trigger full BANTT re-score.
- **60-day stale**: Mandatory re-qualification. If score has not improved, move to Nurture.
- **90-day stale**: If still in Nurture with no score improvement, move to Disqualify.

### Event-Based

- **Champion leaves the organization**: Re-score Authority immediately. Likely drop to Nurture.
- **Budget cut or freeze announced**: Re-score Budget. If drops below 10, move to Nurture.
- **Competitor enters the deal**: Re-score Tech-fit relative to competitor. Assess differentiation.
- **Organizational restructure**: Re-score Authority (new decision makers) and Timeline (priorities may shift).
- **Scope change**: Re-score Need and Tech-fit. Larger scope may improve need but reduce tech-fit.
- **New regulation or market event**: Re-score Timeline (may create urgency) and Need (may increase pain).
- **Decision date slips**: Re-score Decision Date. If date slides more than one quarter, investigate root cause and re-score all dimensions — slipping dates often signal deeper disengagement or budget risk.

### Re-qualification Process

1. Pull the last scorecard.
2. Identify what has changed since last qualification.
3. Re-score only the affected dimensions (document delta).
4. Recalculate total and re-apply verdict logic.
5. Update `commercial-state.md` with new scores and reasoning.

---

## Minimum Engagement Thresholds

### By Service Line

| Service Line | Minimum Engagement Size | Minimum Duration |
|-------------|------------------------|-----------------|
| Software Engineering | $75K | 2 months |
| Data Engineering | $100K | 2 months |
| Data Science / AI-ML | $100K | 3 months |
| Strategy / Advisory | $50K | 1 month |
| Architecture Review | $25K | 2 weeks |

### Threshold Rules

- Flag any qualified deal below the minimum engagement size for its service line.
- Deals below 50% of minimum threshold should be disqualified unless strategic (document justification).
- Deals below minimum but above 50% may proceed if they are a foot-in-the-door with clear expansion potential (document the expansion hypothesis).

### Capacity Check

Before advancing a Pursue verdict, verify:
- Do we have the team available to staff this engagement in the prospect's timeline?
- If not, what is the earliest we could start?
- Would staffing this deal require pulling resources from existing commitments?
- If capacity is constrained, rank qualified deals by total BANTT score and prioritize highest-scoring opportunities.
