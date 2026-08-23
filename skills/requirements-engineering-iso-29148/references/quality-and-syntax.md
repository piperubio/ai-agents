# Requirement quality and syntax (ISO/IEC/IEEE 29148)

Distilled from the vault notes on ISO/IEC/IEEE 29148:2018, Key Concepts and
Requirements Fundamentals. Use this file in create and evaluate modes.

## Needs vs requirements

- **Needs**: capabilities and outcomes expressed in business or user terms.
- **Requirements**: formal, structured, measurable statements that govern
  design and implementation.

RE mediates between the two. Validation asks "did we build the right
system?" and applies to stakeholder requirements. Verification asks "did we
build the system right?" and applies to system/software requirements.

## Requirement construct

```
[Condition] + [Subject] + shall + [Action] + [Object] + [Constraint]
```

Components:

1. **Condition** (optional): when the requirement applies. "When operating in
   emergency mode..." / "Upon receipt of a reset signal..."
2. **Subject**: the system, software, or element being constrained ("The
   System", "The Billing Service"). Never the user or operator.
3. **Binding verb**:
   - `shall`: mandatory binding provision; must be fulfilled and verified
   - `should`: recommendation, non-mandatory goal
   - `may`: permission
   - `is/are/was`: descriptive context only, never binding
4. **Action**: precise function, behavior, or quantitative output.
5. **Constraint**: measurable limits, tolerance ranges, environmental bounds.

Patterns:

- Functional: "When engine temperature exceeds 100 °C, the Cooling Control
  System shall activate the secondary coolant pump within 500 ms."
- Interface: "The Billing Service shall transmit invoice records to the
  Accounting Database via TLS 1.3 encrypted REST API."
- Performance: "The Radar Tracker shall update object positional coordinates
  at a minimum frequency of 60 Hz."

### EARS-compatible phrasings

Teams using EARS (Easy Approach to Requirements Syntax) map directly onto
this construct; keep the ISO components when writing, but recognize these
shapes on input:

| EARS shape | Construct mapping |
| --- | --- |
| WHEN [event] THEN [system] SHALL [response] | Condition + Subject + shall + Action |
| IF [precondition] THEN [system] SHALL [response] | Same; condition is a state, not an event |
| WHEN [event] AND [condition] THEN ... | Compound condition, still one requirement |

## Edge-case battery

Raw needs describe the happy path. To reach set-level completeness, probe
each capability with these questions before closing the set:

- What if the input is empty, null, malformed, or at a boundary value?
- What if the operation fails mid-way (timeout, network drop, crash)?
- What if the actor is not authenticated or lacks permission?
- What happens under concurrent access to the same resource?
- What does the system show when a list or result set is empty?
- Which operational mode or state applies, and what changes in degraded
  modes?

Each gap found becomes one new `shall` statement with its own ID, not a note
or assumption.

## Individual characteristics (checklist)

| Characteristic | Test question |
| --- | --- |
| Necessary | Does removal leave a critical capability gap? |
| Appropriate | Is it at the right abstraction level for this specification? |
| Unambiguous | Do all readers reach exactly one interpretation? |
| Complete | Can it be understood without hidden assumptions? |
| Singular | Does it state exactly one requirement? |
| Feasible | Is it achievable within technology, budget, schedule? |
| Verifiable | Can objective evidence prove it (I/A/D/T)? |
| Correct | Does it accurately represent the real need? |
| Conforming | Does it follow templates, syntax rules, style guides? |

## Set-level characteristics

| Characteristic | Test question |
| --- | --- |
| Complete | Do requirements cover all goals, modes, states, interfaces, safety/security concerns? |
| Consistent | Do any two requirements conflict? Are terminology and units uniform? |
| Bounded/feasible | Can the set be realized within cost, schedule, space, weight, power? |
| Unambiguous | Does the integrated text yield one interpretation? |
| Verifiable | Can evidence prove the integrated system meets the set? |
| Able to be validated | Can the set be validated against operational goals? |

## Language anti-patterns

| Category | Forbidden phrases | Fix |
| --- | --- | --- |
| Subjective quality | user-friendly, easy to use, rapid, high quality | Give numbers: "a trained user shall complete checkout within 3 minutes" |
| Loopholes | if possible, as appropriate, where practical | State explicit trigger conditions or separate mandatory options |
| Open-ended | including but not limited to, etc., and so on | Enumerate the closed list of items or states |
| Comparative | better than, faster, superior | Anchor to a baseline: "process requests in less than 200 ms" |
| Logical ambiguity | and/or, ambiguous "or" | Split into separate singular statements |
| Unbounded totality | all, always, never, every | Define exact boundaries and trigger conditions |

## Metadata attributes

Every requirement carries these attributes:

| Attribute | Purpose | Example |
| --- | --- | --- |
| ID | Permanent unique tag. Never modified or reused. | REQ-SYRS-042 |
| Version | Revision tracking; indicates volatility | v2.1 |
| Owner | Role authorized to approve changes and report status | Lead systems engineer |
| Priority | Stakeholder importance for trade-offs | High |
| Risk | Technical maturity / feasibility rating | Medium (new technology) |
| Rationale | Why it exists; link to trade studies or goals | "Required for accessibility compliance" |
| Type | Functional, performance, interface, quality, usability, security, constraint | Functional |
| Verification method | Inspection, Analysis, Demonstration, or Test | Test |
| Traceability | Upward (parent need), downward (design/tests), horizontal (interfaces) | Up: STRS-015; Down: SRS-102 |
| Status | Draft -> Approved -> Baselined | Approved |
| Stability | Expected likelihood of future change | Stable |

Mark unresolved content explicitly with TBD (to be determined), TBR (to be
resolved), or TBS (to be supplied) rather than leaving silent gaps.
