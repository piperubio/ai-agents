# RE processes (ISO/IEC/IEEE 29148)

Distilled from the vault notes on ISO/IEC/IEEE 29148:2018, Requirements
Engineering Processes.

## Process taxonomy

Requirements engineering runs hierarchically from enterprise strategy down to
continuous project management. Each level yields a specification that drives
the next:

- Business or Mission Analysis -> BRS + ConOps
- Stakeholder Needs and Requirements Definition -> StRS + OpsCon
- System/Software Requirements Definition -> SyRS / SRS
- Requirements Management cuts across all levels: baselines, CCB,
  measurement

## Business or mission analysis

Purpose: define the business problem or opportunity, characterize the
solution space, and establish business requirements and high-level
operational concepts.

| Activity | Tasks | Deliverable |
| --- | --- | --- |
| Prepare for analysis | Identify enterprise strategy, key stakeholders, scope, governance | Analysis plan |
| Define problem/opportunity | Analyze current state, gaps, constraints, business goals | Problem statement |
| Characterize solution space | Identify feasible candidate solution concepts | Feasibility study |
| Evaluate options | Assess against cost, schedule, risk, strategy fit | Option evaluation report |
| Define business requirements | Formulate BRS and organization-wide ConOps | BRS, ConOps |
| Manage outputs | Traceability to enterprise objectives; business baseline | Baselined BRS |

## Stakeholder needs and requirements definition

Purpose: define stakeholder requirements for a system that provides needed
capabilities in its real operational environment.

Flow: identify stakeholders -> elicit needs -> transform into StRS ->
analyze and validate -> baseline with traceability.

| Activity | Key tasks |
| --- | --- |
| Prepare for StRS | Select elicitation techniques: interviews, workshops, prototypes, surveys, observation |
| Define context and needs | Capture expectations, environmental constraints, human factors, scenarios, modes/states |
| Transform needs | Formalize raw needs into `shall` statements in the StRS |
| Analyze requirements | Check completeness, consistency, feasibility, verifiability; develop the OpsCon |
| Manage requirements | Obtain stakeholder agreement, baseline the StRS, trace upward to business goals |

## System/software requirements definition

Purpose: transform stakeholder requirements into a technical specification of
functions, performance, interfaces, quality attributes, and design
constraints (SyRS / SRS).

| Activity | Focus | Deliverable |
| --- | --- | --- |
| Preparation | Review StRS; establish tools, repository schemas, allocation strategies | Definition strategy |
| Technical definition | Specify functions, performance metrics, interfaces, quality attributes, constraints | Draft SyRS / SRS |
| Technical analysis | Assess technical risk, trade-offs, verification criteria, language rules | Analysis report + RTM |
| Management and baseline | Engineering sign-off, baselining, strict change control | Baselined SyRS / SRS |

## Interactions with downstream technical processes

- **Architecture definition**: allocates SyRS requirements to architectural
  elements (hardware, software, manual operations) and derives architectural
  requirements from quality attributes (fault tolerance, latency, security).
  Feasibility feedback flows back into requirements.
- **Verification**: every requirement gets explicit pass/fail criteria.
  Verification method assignment:
  - Inspection: visual audit of an artifact, code, or document
  - Analysis: proof, calculation, modeling, or simulation
  - Demonstration: qualitative observation without instrumentation
  - Test: quantitative measurement under controlled conditions
- **Validation**: confirms requirements express real operational intent, so
  the delivered system satisfies actual user needs.

## Change control (CCB)

Baselined specifications change only through this flow:

1. Change request submission (formal proposal)
2. Impact analysis (technical, cost, schedule, safety, risk)
3. CCB review and decision (approve / reject / defer)
4. Implementation: apply change, increment version, update bidirectional
   traceability

## Metrics

| Metric | Purpose | Calculation |
| --- | --- | --- |
| Requirements volatility | Specification stability | (added + modified + deleted) / total baselined * 100% |
| Traceability coverage | No orphan requirements | requirements with 100% up+down trace / total baselined * 100% |
| Quality defect density | Writing quality in reviews | defects found / reviewed requirements |
| Verification readiness | Progress toward testing | requirements with approved criteria / total baselined * 100% |

## Iteration and recursion

RE is not linear. Iteration refines requirements at the same abstraction
level based on feedback and trade studies. Recursion re-applies the
requirements process at lower structural levels: system -> subsystem ->
software configuration item -> component.
