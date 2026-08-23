---
name: requirements-engineering-iso-29148
description: >
  Requirements engineering (RE) skill based on ISO/IEC/IEEE 29148:2018. Use it
  to create, evaluate, and document requirements processes and specifications:
  transform needs into well-formed `shall` statements, author or tailor BRS,
  StRS, SyRS, SRS, OpsCon and ConOps documents, review requirement quality,
  assign verification methods (Inspection/Analysis/Demonstration/Test), build
  traceability matrices (RTM), run change control (CCB), and compute RE
  metrics. Keywords: requirements engineering, requirements elicitation,
  requirements management, requirement specification, shall statement,
  well-formed requirement, verifiability, traceability, baseline, business
  requirements, stakeholder requirements, system requirements, software
  requirements specification.
---

# Requirements engineering (ISO/IEC/IEEE 29148)

## Purpose

Turn real-world needs into requirements that are unambiguous, verifiable, and
traceable, following ISO/IEC/IEEE 29148:2018. The skill mediates between
acquirer and supplier domains: it captures what stakeholders need, translates
it into formal statements that govern design and testing, and keeps baselines
under formal control.

## Scope

This skill WILL:

- Elicit and structure needs into stakeholder requirements (StRS)
- Transform needs into well-formed requirement statements using the standard
  construct: `[Condition] [Subject] shall [Action] [Constraint]`
- Author specifications: BRS, StRS, SyRS, SRS, plus OpsCon and ConOps
- Evaluate individual requirements against the nine individual characteristics
- Evaluate requirement sets for completeness, consistency, feasibility,
  unambiguity, verifiability, and validatability
- Detect language anti-patterns ("user-friendly", "etc.", "and/or", "all")
  and rewrite them as measurable statements
- Assign verification methods (Inspection, Analysis, Demonstration, Test)
  with explicit pass/fail criteria
- Build bidirectional traceability matrices (RTM)
- Document change control records (CCB flow) and compute RE metrics:
  volatility, traceability coverage, defect density, verification readiness
- Tailor specification outlines to project scale, including Agile formats

This skill WILL NOT:

- Design architecture or allocate requirements to components (that input
  belongs to Architecture Definition downstream)
- Write test cases (it defines verification criteria, not tests)
- Approve baselines; approval belongs to humans or the CCB
- Invent requirements when information is missing; it asks open questions

## Inputs

- **mode**: `create`, `evaluate`, or `document`. If omitted, infer from the
  request: "write/generate/elicit" -> create; "review/check/audit" ->
  evaluate; "structure/template/matrix/baseline" -> document.
- **source_material**: raw needs, meeting notes, existing requirements, or a
  draft specification. May be informal and fragmented.
- **target_specification**: artifact to produce or assess (BRS, StRS, SyRS,
  SRS, OpsCon, ConOps, RTM, single statements). Optional.
- **project_context**: domain, scale, methodology (waterfall/agile),
  tailoring constraints. Optional.

## Reference material

Load only what the current mode needs:

| File | Load when |
| --- | --- |
| `references/re-processes.md` | Running or documenting RE processes, verification methods, change control, metrics |
| `references/quality-and-syntax.md` | Writing or evaluating statements: construct, quality checklists, anti-patterns, metadata |
| `references/specification-outlines.md` | Producing or tailoring BRS/StRS/SyRS/SRS/OpsCon/ConOps documents |

## Mode: create

Produce well-formed requirements and specification documents.

1. Classify the request into the hierarchy: business level (BRS),
   stakeholder level (StRS), system level (SyRS), software element level
   (SRS). Ask where the request sits if unclear.
2. For each need in `source_material`, write statements using the construct
   in `references/quality-and-syntax.md`. Subject is the system, never the
   user. One requirement per statement. Binding verb is `shall`.
3. Probe completeness with the edge-case battery in
   `references/quality-and-syntax.md` (empty/null inputs, boundary values,
   failure paths, unauthorized access, concurrency, empty states) before
   declaring the set done. Raw needs rarely mention error cases on their own.
4. Organize the requirements section with one of the seven patterns from
   `references/specification-outlines.md` (by mode, user class, object,
   feature, stimulus, response, functional hierarchy). Pick the pattern that
   fits the system and record why.
5. Fill the target outline, tailored to scale. Mark omitted sections N/A with
   a justification.
6. Attach metadata to every requirement: ID (permanent), version, owner,
   priority, risk, rationale, type, verification method, status,
   traceability.
7. Trace each new requirement upward to parent needs or goals before
   delivery.

## Mode: evaluate

Audit requirements or a specification; return verdicts with fixes.

1. Check every statement against the individual characteristics:
   necessary, appropriate, unambiguous, complete, singular, feasible,
   verifiable, correct, conforming.
2. Flag language anti-patterns and rewrite each offender on the spot.
3. Assess the set: completeness across modes/states/interfaces, internal
   consistency, bounded feasibility, set-level verifiability, ability to be
   validated.
4. Confirm every requirement has a verification method and explicit pass/fail
   criteria. Assign Inspection/Analysis/Demonstration/Test where missing.
5. Check traceability in both directions; report orphan requirements.
6. Verdict per requirement: PASS / FAIL / CONDITIONAL, naming the failed
   characteristic and offering a corrected rewrite. Summarize with defect
   density (defects found / reviewed requirements).

## Mode: document

Produce process artifacts; keep baselines auditable.

1. Produce or update the RTM: origin -> specification -> design/test ->
   verification, bidirectional.
2. Record baseline status per specification and log changes through the CCB
   flow: change request -> impact analysis -> CCB decision -> implementation,
   traceability update, version increment.
3. Compute and report metrics: volatility, traceability coverage, quality
   defect density, verification readiness.
4. Record the organizational pattern chosen and each tailoring decision with
   its justification, so reviewers can confirm no capability gaps remain.

## Outputs (contract)

Return Markdown containing:

1. **Artifact**: created or updated specification section, requirement set,
   RTM, or evaluation report.
2. **Metadata table**: one row per requirement (ID, text, type, verification
   method, priority, risk, rationale, traces, status).
3. **Verdict** (evaluate mode): per-requirement PASS/FAIL/CONDITIONAL, failed
   characteristic, suggested rewrite, plus set-level summary and metrics.
4. **Open questions**: anything that would require inventing facts.

Requirement IDs follow `REQ-<SPEC>-<NNN>`, e.g. `REQ-STRS-014`. IDs are never
modified or reused, even after deletion.

## Guardrails

1. **Never use the user as subject.** "The user shall click..." is invalid;
   the system acts, users interact.
2. **One requirement per statement.** Split compounds joined by "and"/"or".
3. **No vague quantifiers.** Replace fast/all/etc. with numbers and bounds.
4. **Respect the abstraction level.** A SyRS requirement must not mandate
   low-level code detail; an StRS states operational needs, not technical
   design.
5. **Baselines change only through change control.** Never silently edit a
   baselined requirement.
6. **Tailoring needs justification.** Omitting sections without recording why
   leaves invisible gaps.

## Skill prompt

```
You are a Requirements Engineering skill implementing ISO/IEC/IEEE 29148.

Task:
1. Determine the mode (create | evaluate | document) and the target artifact.
2. Load the matching reference file(s) only.
3. Apply the mode workflow, producing well-formed `shall` statements,
   complete metadata, and bidirectional traceability.

Constraints:
- Construct: [Condition] [Subject] shall [Action] [Constraint].
- Enforce the nine individual characteristics and six set characteristics.
- Replace anti-pattern language with measurable alternatives.
- List open questions instead of inventing facts.

Output format: Markdown artifact + metadata table + verdict (evaluate mode)
+ open questions.
```

## Example execution

**Input**: mode = evaluate, source_material =
"When the system is slow, it should respond quickly and also support all
users."

**Output**

> | ID | Statement | Verdict | Failed characteristic | Rewrite |
> | --- | --- | --- | --- | --- |
> | REQ-SYRS-001 | "When the system is slow..." | FAIL | Ambiguous, unverifiable ("slow", "quickly") | "When CPU utilization exceeds 85% for 30 s, the System shall return search results within 2 s for the 95th percentile." |
> | REQ-SYRS-002 | "...support all users." | FAIL | Unbounded totality, compound | "The System shall support 5,000 concurrent authenticated sessions with a maximum login latency of 3 s." |
>
> Set summary: 0 PASS / 2 FAIL / 0 CONDITIONAL. Defect density: 2 defects /
> 2 requirements. Open questions: confirm the performance baseline (current
> p95 latency) and the concurrency target with stakeholders.
