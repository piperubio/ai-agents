This is a project for managing AI agents configurations, templates, and skill suites for commercial and project management flows.

## General Principles

- **State as "Brain":** Each pipeline uses a single state file (`commercial-state.md`, `project-state.md`) as the source of truth.
- **Traceability:** All state updates must be logged with the author and reason (no silent changes).
- **Progressive Disclosure:** Agents and skills should only consume and expose information relevant to their current stage.

## Agents

Main agents are the orchestrators of the pipelines and are located in the `agents/` folder.

- **Orchestration:** Always start orchestration from the core agents:
  - `commercial-core-agent`: Manages the B2B consulting sales pipeline.
  - `pm-core-agent`: Manages the execution and control of consulting projects.
- **Integration:** The output of one agent (e.g., a workplan from the commercial suite) should feed directly into the next orchestrator (e.g., the PM suite intake).

## Skills

- **Creation & Validation:** Always use the `skill-creator` tool to create or validate skills.
- **Skill Discovery:** Before creating a new skill, use the `find-skill` tool to search for existing skills within the `skills.sh` registry. These can be reused, used as a reference, or serve as inspiration.
- **Storage:** All skills are stored in the `skills/` folder and organized by pipeline prefix (`commercial-*`, `project-*`).
- **Naming Convention:** Use `kebab-case` (lowercase and hyphens), for example: `consulting-project-planner`.
- **Documentation:** Each skill must have a description explaining its purpose and invocation criteria, including technical keywords for agent identification.
