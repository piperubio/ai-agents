---
description: Orchestrate a Claude Code agent team to implement a change in parallel. ONLY FOR MEDIUM AND LARGE IMPLEMENTATIONS
---

Orchestrate an agents team to implement a change in parallel using the distribution plan.

**Input**: Optionally specify a change name. If omitted, check if it can be inferred from conversation context. If vague or ambiguous you MUST prompt for available changes.

**Steps**

1. **Select the change**

   If a name is provided, use it. Otherwise:
   - Infer from conversation context if the user mentioned a change
   - Auto-select if only one active change exists
   - If ambiguous, run `openspec list --json` to get available changes and use the **AskUserQuestion tool** to let the user select

   Always announce: "Using change: <name>"

2. **Validate the change uses dispec-driven schema**
   ```bash
   openspec status --change "<name>" --json
   ```
   Parse the JSON to get `schemaName`. If it is NOT `dispec-driven`:
   - Inform the user that multi-agent apply requires the `dispec-driven` schema
   - Suggest using `/opsx-apply` for single-agent execution instead
   - Stop

   If `distribution` artifact is not `done`:
   - Report which artifacts are missing
   - Suggest running `/opsx-multiagent` to complete the planning phase
   - Stop

3. **Read the distribution plan and context**

   Read the following files from the change directory:
   - `distribution.md` — agent assignments, file ownership, cross-agent dependencies
   - `dependencies.md` — task dependency matrix
   - `tasks.md` — full task list with file annotations
   - `proposal.md` — change context
   - `design.md` — technical decisions (if exists)

   Extract from `distribution.md`:
   - Agent count and names
   - Each agent's assigned task IDs, file ownership, execution order
   - Cross-agent dependency table

4. **Populate the internal task tracking**

   Use your internal memory or task-tracking capabilities to manage the overall progress of the change.
   - Register all tasks from `tasks.md` into your own tracking context.
   - Ensure each task record includes its metadata: the assigned agent, execution order, and any blocking dependencies.

5. **Spawn and instruct sub-agents**

   Delegate the work by invoking parallel sub-agents, child instances, or background processes for each agent in the distribution plan. Provide each delegated agent with the following prompt/context:
   
   - **Context**:
     - The agent's assigned task IDs and descriptions.
     - File ownership list and execution order.
     - Cross-agent dependencies (what to wait for).
     - The absolute path to their specific git worktree (`../<change-name>-<agent-name>`).
     - The absolute path to `tasks.md` in the main change directory.
   - **Instructions**: "Use your available file reading, writing, and terminal tools to complete your assigned tasks. **After completing each task, you MUST read and update `tasks.md`** in the main change directory: find the line matching your task description and change `- [ ]` to `- [x]`. If a task is blocked, wait and periodically read `tasks.md` until your blockers are marked as complete. Reply with a summary when all your assigned tasks are done."

   Spawn sub-agents with no cross-agent dependencies first. For those with dependencies, spawn them immediately after with strict instructions to monitor `tasks.md` for their unblockers.

6. **Monitor progress**

   - Continuously evaluate the status of your delegated sub-agents as they work and return responses.
   - Update your internal task tracking as sub-agents report tasks completed.
   - Intervene if a sub-agent reports an error or needs clarification to resolve a blocker.

   **Tasks.md sync (orchestrator as backup):**
   - When a sub-agent reports a task completed, read `tasks.md` from the main change directory to verify the corresponding line is marked `- [x]`. 
   - If the sub-agent failed to update it, use your file editing capabilities to update it yourself. This ensures the source of truth remains accurate.

7. **Shutdown and report**

   When your internal tracking shows all tasks are completed and all sub-agents have returned their final summaries:

   **Pre-shutdown tasks.md sync:**
   - Read the final `tasks.md` from the main change directory.
   - Compare every task line against your internal tracking status.
   - Any line still marked `- [ ]` that corresponds to a completed task must be updated to `- [x]` by you.

   Then, display the final summary:

   ```
   ## Multi-Agent Implementation Complete

   **Change:** <change-name>
   **Schema:** dispec-driven
   **Agents:** N agents used
    **Tasks:** M/M complete (tasks.md synced ✓)

   ### Agent Summary
   - <agent-1>: N tasks completed (branch: <worktree-branch>)
   - <agent-2>: N tasks completed (branch: <worktree-branch>)
   ...

   ### Next Steps
   - Review with `/opsx-verify`
   - Run tests to verify integration
   - Archive the change with `/opsx-archive`
   ```

**Guardrails**
- MUST validate schema is `dispec-driven` before proceeding
- MUST validate all artifacts are complete (especially `distribution`)
- MUST keep `tasks.md` in sync: agents update it on task completion, orchestrator verifies on monitoring and pre-shutdown
- If the distribution plan shows file ownership conflicts (two agents writing same file), warn the user and ask whether to proceed or reassign
- If a teammate reports a blocker, try to help resolve it before escalating to the user
- Do not create the team or spawn agents if the user cancels at the confirmation step
