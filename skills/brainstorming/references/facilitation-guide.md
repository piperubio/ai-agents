# Facilitation Guide

## Contents

- Match the session to the question
- Generate before converging
- Evaluate under uncertainty
- Propose an experiment
- Use visuals selectively
- Example: reopen a provisional decision
- Review the record, not implementation readiness
- Upstream inspiration

## Match the Session to the Question

Choose the next useful activity, not a mandatory path to implementation:

| User's need | Activity | Useful outcome |
|-------------|----------|----------------|
| Unclear problem or opportunity | Frame and explore | Question, hypotheses, open issues |
| Generate possibilities | Diverge, then group | Varied idea inventory |
| Compare known alternatives | Agree criteria and assess | Comparison with evidence gaps |
| Make a decision | Examine trade-offs and authority | Confirmed or provisional choice, or deferral |
| Test a doubtful assumption | Propose a small probe | Experiment question and observable result |
| Revisit prior work | Read the record and note new evidence | Traceable update, not a restarted interview |

Match the time budget and decision stakes. A short session can end with a useful
record and one unresolved question. Do not presume that more process is always
better, or that acknowledging an idea commits the user to a product.

## Generate Before Converging

Use the lightest technique that expands the option space:

- **Different lenses:** consider the offer, relationship, process, incentives,
  skills, and tools rather than proposing several versions of the same app.
- **Reframe:** ask what would change if the underlying problem is different.
- **Combine:** merge promising elements, preserving their source ideas.
- **Counterfactual:** consider manual delivery, using existing tools, or leaving
  the situation unchanged to expose the value of a new solution.

Invite user additions. Group duplicates without deleting their rationale or
attribution. Avoid leading with a preferred solution before alternatives have
been considered. Do not apply feasibility or YAGNI as an initial censorship
filter; evaluate scope and effort during convergence.

A shortlist is for comparison, not a limit on generation. Keep ideas outside
the shortlist in the record with a reason for deferral. Visual comparisons may
show only a few options at a time without shrinking the overall inventory.

## Evaluate Under Uncertainty

Use criteria relevant to the question: customer value, evidence of demand,
feasibility, effort, risk, reversibility, or strategic fit. Distinguish user
constraints from criteria the assistant suggests.

Prefer qualitative comparisons when evidence is sparse. A matrix with
"unknown" cells is more informative than arbitrary scores. If scoring is
useful, make the scale, direction, evidence or estimation basis, and any weights
explicit. Keep estimates labeled; do not treat a weighted total as proof.

When asked for a definitive winner without supporting data, provide the useful
comparison you can substantiate and explain its limits. A provisional
recommendation may identify the cheapest informative test, not the best final
solution. Urgency, authority, and work already invested are constraints or
preferences, not evidence of customer demand.

Treat conflicting stakeholder views as competing views until resolved. Record
who decides and why. Only mark a decision confirmed when the relevant person has
actually made it; clarify ambiguous approval when it affects the next step.

## Propose an Experiment

Describe:

1. The uncertain claim and which decision it affects.
2. The smallest useful observation or test and who would be involved.
3. What result would support, weaken, or leave the claim unresolved.
4. Known constraints and the proposed next review point.

Interviews, manual pilots, and reviewing existing data are valid probes; not
every experiment needs code. Avoid inventing acceptance thresholds, budget,
owners, or dates as if agreed. Label suggestions explicitly. Approval to discuss
or record a probe is not approval to recruit people, spend money, build it, or
start an external project.

## Use Visuals Selectively

Offer a diagram, idea map, wireframe, or side-by-side comparison only when seeing
it would improve understanding of this question. Match fidelity to the question:
a rough sketch is enough to discuss relationships. A polished mockup does not
make the underlying assumptions validated.

Keep conversation available and treat it as the primary feedback channel.
Clicks or selections can reveal interest; confirm them in conversation before
recording a consequential decision. No browser companion, server, telemetry, or
Superpowers installation is required by this skill.

## Example: Reopen a Provisional Decision

User: "Ana chose monthly support provisionally, but two customers now ask for
diagnostics. Reopen the choice; we have not interviewed them yet."

Useful record excerpt:

| ID | Status | Basis |
|----|--------|-------|
| I-01: monthly support | Provisional selection under review | Ana's earlier continuity rationale; demand unvalidated |
| I-02: diagnostics | Back under evaluation | Two requests; payment willingness and delivery capacity unknown |
| D-01 | Reopened by Ana; no replacement decision | New requests warrant comparison, not a definitive winner |

Change: assistant records Ana's reopening of D-01, retaining its previous
status and reason. Proposed next step: clarify what the two customers need and
would pay for, then compare capacity and economics. Owner and timing remain
unassigned unless already agreed. This is a complete update, not an approved
service design.

## Review the Record, Not Implementation Readiness

Check for missing relevant ideas, unsupported assertions, mistaken attribution,
accidental contradictions, and unrecorded changes. Preserve intentional
alternatives and unresolved interpretations; do not "fix" them by inventing a
decision. Unknowns are acceptable when their significance is visible.

A good stopping point has a coherent record and an explicit next step or
deferral. It need not have a winner, an architecture, or resolved pricing.

If the user requests design, hand over the chosen idea IDs, purpose, rationale,
evidence, constraints, and unresolved questions. Design can explore those
questions separately. Neither ideation-record approval nor design-brief approval
authorizes implementation or a git commit.

## Upstream Inspiration

Adapted conceptually from [Superpowers brainstorming](https://github.com/obra/superpowers/blob/8ca22dba9a94f28898bbce59f2537ff4d87c747d/skills/brainstorming/SKILL.md),
especially shared understanding, proportional facilitation, and stage-specific
approval, and its [visual companion guide](https://github.com/obra/superpowers/blob/8ca22dba9a94f28898bbce59f2537ff4d87c747d/skills/brainstorming/visual-companion.md).
The positive output contract follows the approach discussed in
[writing-skills](https://github.com/obra/superpowers/blob/8ca22dba9a94f28898bbce59f2537ff4d87c747d/skills/writing-skills/SKILL.md).
This local skill deliberately separates ideation from mandatory specification
and implementation; these upstream sources are provenance, not dependencies.
