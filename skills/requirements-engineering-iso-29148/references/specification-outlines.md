# Specification outlines (ISO/IEC/IEEE 29148)

Distilled from the vault notes on ISO/IEC/IEEE 29148:2018, Information Items
and Specifications + Annexes. Use this file to author or tailor documents.

## Specification hierarchy

| Spec | Level and audience | Core focus | Primary verb |
| --- | --- | --- | --- |
| BRS | Executive leadership, sponsors, enterprise architects | Business vision, goals, constraints, business model | Business intent |
| StRS | Users, operators, business analysts, acquirers | Operational needs, capabilities, scenarios, context | shall |
| SyRS | Systems engineers, architects, verification leads | System functions, quantitative performance, interfaces | shall |
| SRS | Software engineers, architects, QA/testers | Software functions, data, APIs, quality attributes | shall |

Flow: BRS drives StRS; StRS drives SyRS; SyRS allocates to SRS. ConOps
(enterprise-wide) accompanies the BRS; OpsCon (system-of-interest)
accompanies the StRS.

## Common front matter (all specifications)

1. Identification: title, unique ID, baseline version, release date, owner,
   security classification
2. Front matter: TOC, figures, tables, revision history with approvals
3. Definitions: domain-specific glossary for this project
4. References: cited standards and parent specs (compliance vs guidance)
5. Acronyms and abbreviations

## Organizational patterns (pick one for the requirements section)

No single scheme fits every project. Choose by system nature:

| Pattern | Use when | Notation |
| --- | --- | --- |
| By system mode | Behavior changes fundamentally by operational state (normal/degraded/emergency) | State machines, statecharts |
| By user class | Distinct function sets per user type | User role diagrams, RBAC matrix |
| By object/entity | Modeled on real-world entities with attributes and services | Class diagrams (OOA) |
| By feature | Discrete external services with input-response sequences | Use cases, user stories |
| By stimulus/event | Event-driven responses to environmental triggers | Event-response tables, sequence diagrams |
| By response/output | Focus on generating reports or outputs | Screen/report designs, output flows |
| By functional hierarchy | Decomposed data flows in complex systems | DFDs, data dictionaries |

Record the chosen pattern and rationale in the document overview.

## BRS outline

1. Front matter
2. Overview
3. Business purpose (background, strategic reasons, contribution to
   management objectives)
4. Business scope (domain, activities, out-of-scope entities)
5. Business overview (divisions, external entities, domain architecture)
6. Major stakeholders
7. Business environment (market trends, laws, social responsibility)
8. Mission, goals, objectives (qualitative and quantitative results)
9. Business model (products, services, channels, alliances)
10. Information environment (conceptual data model, existing systems)
11. Business processes supported or transformed
12. Business policies and rules (governance, compliance)
13. Business constraints (budget, staffing, geography, infrastructure)
14. Business modes (normal, peak season, contingency, fiscal closing)
15. Business operational quality (satisfaction, efficiency, SLAs)
16. Business structure (roles, responsibilities, org changes)
17. High-level operational concept
18. High-level operational scenarios
19. Other life-cycle concepts (acquisition, support, retirement)
20. Project constraints (contractual limits, milestones, technology bounds)

## StRS outline

1. Front matter
2. Overview
3. Stakeholder purpose (operational motivation within BRS goals)
4. Stakeholder scope (system-of-interest boundary vs user workflow)
5. Overview of solution in its operational environment
6. Stakeholder profiles and classes (operators, supervisors, maintainers;
   skill profiles)
7. User operational environment (physical, ergonomic factors)
8. Stakeholder mission, goals, objectives
9. Operational model (stakeholder-process-system interactions)
10. Operational information environment (data consumed/produced by users)
11. System processes (workflows, task sequences)
12. Operational policies and rules (security, access restrictions)
13. Operational constraints (physical, environmental, training, time limits)
14. System modes and states as perceived by users (normal, degraded,
    maintenance)
15. Operational quality (usability, reliability, safety as perceived)
16. User requirements (`shall` statements)
17. Operational concept reference (OpsCon elaboration)
18. Operational scenarios (use cases, user stories, stimulus-response)
19. Other concepts (support, training, maintenance)
20. Project constraints (milestones agreed with users, budgets,
    deployment windows)

## SyRS outline

1. Front matter
2. System purpose and overview (technical justification, objectives, SOI
   description)
3. System scope (boundaries: hardware, software, manual operations)
4. System overview:
   4.1 System context (external block diagram)
   4.2 System functions (principal capabilities summary)
   4.3 User characteristics
5. Functional requirements (capabilities, inputs, processing, outputs)
6. Usability / human-systems integration (ergonomics, HMI, error rates,
   accessibility)
7. Performance requirements (capacity, throughput, response time, tolerance)
8. Interface requirements (external/internal: electrical, mechanical,
   optical, data, network)
9. System quality requirements:
   9.1 Reliability and availability (MTBF, MTTR, availability %)
   9.2 Maintainability (diagnostics, modularity, spares)
   9.3 Safety (hazard prevention, fault tolerance)
   9.4 Other qualities (transportability, reuse, lifespan)
10. System modes and states (startup, self-test, normal, degraded, shutdown)
11. Physical characteristics (weight, dimensions, power, heat; adaptability)
12. Environmental conditions (temperature, humidity, shock, vibration, EMI)
13. Security requirements (encryption, authentication, access control, audit)
14. Information management (storage, retention, backup, restoration,
    migration)
15. Policy and regulatory compliance
16. Life-cycle sustainment (maintenance, component supply, disposal)
17. Packaging, handling, shipping, transportation, storage
18. Verification criteria matrix (every requirement -> I/A/D/T method)
19. Assumptions and dependencies

## SRS outline

1. Front matter
2. Purpose and overview (product, subsystem, or CSCI identified)
3. Software scope (tasks and operational boundaries)
4. Product perspective:
   4.1 System interfaces (relationship to architecture)
   4.2 User interfaces (screens, style guides)
   4.3 Hardware interfaces (protocols with sensors/controllers/peripherals)
   4.4 Software interfaces (OS, DB engines, libraries, middleware)
   4.5 Communications interfaces (HTTP/REST, gRPC, WebSockets; JSON/XML)
   4.6 Memory constraints (RAM, disk, cache)
   4.7 Software operations (cron jobs, maintenance tasks, auto-backup)
   4.8 Interfaces with services (microservices, third-party APIs)
5. Product functions (executive summary of capabilities)
6. User characteristics (proficiency, skills, permissions)
7. Design and implementation constraints (languages, frameworks, restricted
   patterns)
8. Assumptions and dependencies (OS versions, libraries, cloud
   availability)
9. Apportioning of requirements (allocation to releases/sprints)
10. Detailed specified requirements (`shall` statements structured under the
    selected organizational pattern; inputs, validation logic, algorithms,
    outputs)
11. Software usability requirements (learning time, error rates, WCAG 2.1)
12. Software performance requirements (latency ms, throughput rps,
    concurrency, CPU/RAM)
13. Logical database requirements (ER models, schemas, keys, volumes)
14. Design constraints (architecture rules: microservices, layered, etc.)
15. Standards compliance (coding standards, testing mandates, linting)
16. Software system attributes (reliability, availability, security e.g.
    JWT/AES, maintainability, portability, reusability)
17. Software verification criteria (unit/integration/system test mapping)
18. Supporting information and appendices (flowcharts, schemas, message
    dictionaries)

## OpsCon (Annex A) and ConOps (Annex B)

OpsCon covers one specific system-of-interest; ConOps covers the enterprise
across multiple systems.

OpsCon outline:

1. Scope (identification, system overview, document overview)
2. Referenced documents
3. Operational description (context/environment, modes and states, major
   capabilities, user profiles/personas)
4. Operational profiles (normal, degraded, emergency/maintenance)
5. Operational scenarios (primary mission, off-nominal/exception)
6. Summary of operational impacts (on users/operators; organizational/
   infrastructure)
7. Analysis of proposed system (advantages, disadvantages/limitations,
   trade-offs and alternatives considered)

ConOps key sections: current operational situation, justification for
change, proposed enterprise vision, operational policies.

## Tailoring guidelines (Annex C)

Templates adapt to project scale and methodology; never apply rigidly.

1. Omit sections that do not apply, marking them N/A with a reason tied to
   system context (e.g., skip packaging/shipping for pure cloud software).
2. Reorganize or merge sections with house standards if the technical
   content is still satisfied.
3. Justify significant deletions explicitly so no critical capability,
   safety, or quality gap is left uncovered.
4. In Agile contexts, structure StRS/SRS content as living repositories
   (backlogs, user stories with acceptance criteria) while keeping rigor in
   traceability attributes and verification methods. Map each user story to
   acceptance criteria expressed as `shall` statements so they stay
   verifiable and traceable like any other requirement.
