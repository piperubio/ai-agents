---
name: brainstorming
description: "Facilitate ideation and decision-making. Use when the user wants to brainstorm, explore an unclear problem or opportunity, generate alternatives, compare ideas, examine assumptions, or revisit a decision before committing to a solution. Applies to business, services, products, processes, and software; not routine edits or execution of an already approved plan."
---

# Brainstorming: Ideas, Evidence, and Decisions

## Purpose

Help people explore possibilities and make informed choices. Produce a living
record of ideas, analysis, decisions, and uncertainty, not a mandatory design
specification. **Closing a session does not mean closing the solution.**

## Facilitate the Current Stage

Start from the user's requested outcome: explore, compare, decide, or revisit.
Scale depth to the stakes, uncertainty, and available time; return to exploration
when new evidence changes the question. Resume existing records rather than
repeating discovery. Read project context only when it informs the discussion.

1. **Establish shared understanding.** Reflect the purpose, audience, constraints,
   and success criteria. Separate user statements, evidence, and assumptions;
   invite correction. Ask one focused question when missing context prevents a
   useful next step. When enough context exists, generate ideas now instead of
   withholding them behind a questionnaire.
2. **Open possibilities.** Generate distinct alternatives before recommending
   one. Include changes to services, processes, or behavior, not just software.
   Consider improving existing tools or doing nothing when relevant. Preserve
   ideas before filtering them; no fixed number of ideas is required.
3. **Organize and evaluate.** Group related ideas, then compare a manageable
   shortlist against explicit criteria. Explain benefits, trade-offs, effort,
   risks, and supporting evidence. Mark unknowns as unknowns. Score only when
   the scale and basis are explicit; label estimates and do not manufacture
   numbers or certainty to satisfy a ranking request.
4. **Record the outcome.** Distinguish an idea, preference, assistant
   recommendation, provisional selection, and user-confirmed decision.
   Preserve alternatives and reasons for selecting, deferring, or rejecting
   them. Keep unresolved assumptions and competing interpretations visible.
5. **Close or continue deliberately.** Summarize what changed, what remains
   open, and the next useful step. If evidence is insufficient, propose a small
   validation with an observable result. Mark proposed owners, dates, and
   thresholds as proposals until agreed. Ask only for the next decision that
   actually requires the user's input.

For generation techniques, uncertain comparisons, experiments, and visual aids,
read [the facilitation guide](references/facilitation-guide.md) as needed.

## Keep a Reusable Record

Use [the record template](assets/brainstorm-record-template.md) when preparing
or updating the deliverable. Adapt its length and sections to the session;
write in the user's language. A brief Markdown record in chat is sufficient
when no saved document is requested. When a saved document is requested, honor
the agreed format and destination; do not impose a path or make a git commit.

- Retain the question, ideas, evaluation basis, decisions, unknowns, and next
  steps needed to resume. State when there is no decision yet.
- Keep existing identifiers. For multiple ideas or decisions, assign stable
  IDs so comparisons and later changes can reference them.
- Log substantive changes with author, reason, and prior status. Reopen a
  decision without erasing its history; never attribute an assistant proposal
  to the user as an agreement.
- Treat an existing pipeline state as authoritative. Keep the brainstorm as
  supporting material, not a replacement state; do not silently alter it.

## Handoffs Are Choices

A valid outcome is an idea inventory, shortlist, provisional recommendation,
validation experiment, confirmed decision, deferral, or explicit move to design.
No outcome automatically authorizes another stage.

When the user explicitly requests design, provide a brief linking the selected
ideas, rationale, evidence, constraints, and open questions. Keep the ideation
record; design is a separate deliverable, not a rewrite of history. Use an
appropriate next-stage skill only if available and requested. Do not require
`writing-plans` or assume that approval of an idea authorizes implementation.
Do not write product code, install dependencies, create external projects, or
commit changes as a side effect of brainstorming. A visual preference or click
is not approval of a design or an execution plan.

## Review Before Closing

Check that the record reflects the user's intent, preserves relevant ideas,
distinguishes evidence from assumptions and proposals from agreements, and
explains decisions and remaining uncertainty. Resolve accidental contradictions
by clarification, not by silently choosing an interpretation. A record can be
complete while its questions remain open.
