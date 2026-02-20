---
name: commercial-qualification
description: >
  Score and qualify B2B consulting opportunities using a custom BANTT framework
  (Budget, Authority, Need, Timeline, Tech-fit). Produce opportunity scorecards
  with a Pursue/Nurture/Disqualify verdict and recommended next actions. Use
  when evaluating whether to invest resources in an opportunity, after a
  discovery meeting, or during pipeline reviews to re-qualify stale
  opportunities.
---

# Commercial Qualification

## Purpose

- Systematically qualify consulting opportunities to ensure the pipeline contains real deals worth pursuing.
- Prevent the team from wasting time on unwinnable or unprofitable deals.
- Produce a defensible, data-backed qualification verdict using the BANTT framework.

## Scope

- This skill WILL:
  - Score opportunities across five dimensions (Budget, Authority, Need, Timeline, Tech-fit)
  - Produce a qualification scorecard with verdict and confidence level
  - Identify key risks, information gaps, and recommended next actions
  - Update pipeline state with qualification results
  - Flag deals below minimum engagement thresholds
  - Trigger re-qualification for stale opportunities (30+ days)

- This skill WILL NOT:
  - Design solutions or estimate effort (that is `solution-design`)
  - Conduct discovery meetings (that is `commercial-discovery`)
  - Make final go/no-go business decisions — it provides the data for humans to decide

## Inputs

- **discovery-notes.md** — from `commercial-discovery` (primary evidence source).
- **prospect-profile.md** — from `commercial-prospecting` (company and stakeholder context).
- **commercial-state.md** — current pipeline context (stage, history, capacity).
- **user_input** — additional intel, override context, or competitive intelligence.

Notes:
- Discovery notes may be incomplete. Score conservatively and flag gaps.
- Tolerate ambiguity — never invent evidence to fill scoring gaps.

## BANTT Framework

Score each dimension 0-20. Total score range: 0-100.

### B — Budget (0-20)

Is there money? Is it allocated? Is the range known?

### A — Authority (0-20)

Do we have access to the economic buyer? Is the champion identified and engaged?

### N — Need (0-20)

Is the pain real and urgent? Is the prospect actively looking for solutions?

### T — Timeline (0-20)

Is there a defined timeline? Is there an external deadline or event driving urgency?

### T — Tech-fit (0-20)

Does our expertise match their needs? Can we deliver meaningful value without excessive subcontracting?

For detailed scoring rubrics with criteria at each 5-point increment, see [references/scoring-models.md](references/scoring-models.md).

## Verdict Logic

| Total Score | Verdict | Action |
|-------------|---------|--------|
| 70-100 | **Pursue** | Advance to solution-design. Invest full resources. |
| 40-69 | **Nurture** | Define nurture plan with timeline. Re-qualify in 30-90 days. |
| 0-39 | **Disqualify** | Graceful exit strategy. Archive with documented reasons. |

**Confidence Level**: High / Medium / Low — based on information completeness across all dimensions.

**Critical override**: A single dimension at 0-5 should trigger concern regardless of total score (e.g., no budget = hard to pursue even if need is 20/20).

## Comparison with Other Frameworks

- **BANT**: Classic but misses tech-fit dimension critical for consulting.
- **MEDDIC/MEDDPICC**: Comprehensive but complex — BANTT captures the essentials for consulting.
- **CHAMP**: Good but less structured scoring.
- **ANUM**: Budget-first approach may miss good nurture opportunities.

BANTT extends BANT with Tech-fit to address the consulting-specific question: "Can we actually deliver this?"

## Outputs (contract)

### 1. New File: `qualification-scorecard.md`

Per opportunity, containing:

```markdown
# Qualification Scorecard: {Company Name}

## Opportunity Summary
- **Opportunity ID**:
- **Company**:
- **Opportunity description**:
- **Qualification Date**: YYYY-MM-DD

## BANTT Scores

| Dimension | Score (0-20) | Evidence |
|-----------|-------------|----------|
| Budget    |             |          |
| Authority |             |          |
| Need      |             |          |
| Timeline  |             |          |
| Tech-fit  |             |          |
| **Total** | **X/100**   |          |

## Verdict: {PURSUE / NURTURE / DISQUALIFY}

**Confidence Level**: {High / Medium / Low}

### Justification
[2-3 sentences explaining the verdict based on scores and evidence]

### Key Risks
- [Risk 1]
- [Risk 2]

### Missing Information
- [What we still need to learn]

### Recommended Next Actions
- [ ] Action 1
- [ ] Action 2

## Deal Estimate
- **Size estimate**: $X - $Y
- **Probability**: X%
```

### 2. Updated: `commercial-state.md`

Update opportunity stage, probability, and notes based on qualification verdict.

## Guardrails

1. Every dimension score must include specific evidence or cite information gaps.
2. Never default to "Pursue" without strong justification — bias toward honesty.
3. If confidence is Low, recommend information-gathering actions before final verdict.
4. A single dimension at 0-5 should trigger concern regardless of total score.
5. Re-qualification should happen if opportunity has been stale for 30+ days.
6. Compare qualification against team capacity — a qualified deal we cannot staff is still a problem.
7. Flag deals that are qualified but below minimum engagement size.

## Example

**Scenario**: Mid-market fintech (200 employees) wants to build a data platform to unify customer analytics across three product lines. Discovery meeting completed with VP Engineering.

**Scorecard**:

| Dimension | Score | Evidence |
|-----------|-------|----------|
| Budget | 14/20 | VP mentioned "low six figures" budget approved for H2. No specific allocation yet. Previous consulting spend with a competitor at ~$150K. |
| Authority | 16/20 | VP Engineering is champion and budget holder. CTO (economic buyer) aware and supportive but not yet directly engaged. |
| Need | 18/20 | Three siloed analytics systems causing duplicate reporting, 2-week lag on cross-product metrics. Board asking for unified view. Actively evaluating solutions. |
| Timeline | 12/20 | "Want something in place before Q1 planning" — soft deadline, no regulatory or contractual driver. |
| Tech-fit | 15/20 | Data platform and analytics are core capabilities. Minor gap in their specific CDP tooling — would need 1-2 sprints of ramp-up. |
| **Total** | **75/100** | |

**Verdict**: **Pursue** (75/100, Confidence: Medium)

- Key risk: CTO not yet directly engaged — authority could stall at final approval.
- Missing: Specific budget figure, CTO meeting, competitive landscape.
- Next actions: Schedule CTO introduction meeting. Prepare capability deck on data platform work. Request budget range confirmation before solution-design.
