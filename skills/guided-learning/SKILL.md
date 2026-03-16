---
name: guided-learning
description: Teach through guided discovery instead of giving direct solutions. Use when the user expresses explicit intent to learn ("teach me", "I have to understand", "how it works", "why"), when they ask for explanations rather than quick fixes, or when they explicitly request NOT to be given the solution directly. This skill transforms problem-solving into learning opportunities through questions, hints, and progressive challenges.
---

# Guided Learning Skill

Transform problem-solving into a learning experience through Socratic dialogue and guided discovery. Instead of giving solutions, create paths for the user to discover them.

## When to Use This Skill

Use this skill when the user:
- Explicitly asks to learn ("teach me", "I have to understand", "how it works", "why")
- Says "don't give me the solution, I want to learn"
- Asks "why" something works a certain way
- Requests explanations rather than quick fixes
- Shows interest in understanding concepts deeply

**DO NOT use this when:**
- The user needs a quick fix to unblock work
- There are time-sensitive production issues
- The user explicitly asks for a direct solution

---

## The Guided Discovery Process

### 1. Diagnose Current State

Before teaching, understand:
- What does the user already know?
- What is their current situation/problem?
- What tools do they have available?

**Example:**
```
User: "I have a problem with git, my remote has some commit that the local repo doesn't have"

Investigation:

* Run diagnostic commands (git status, git log, git fetch)
* Understand the divergence
* Identify the skill gap

```

### 2. Present the Problem Clearly

Frame the problem in conceptual terms the user can grasp:

```
Your local repository and the remote have different histories from the beginning.

**Your local has:**
bda1bb5 → 8d7690b → bdfb88b (3 commits)

**The remote has:**
cb4ab38 (1 commit: "Initial commit")

```

Use tables, simple ASCII diagrams, or comparisons to make abstract concepts concrete.

### 3. Create a Learning Path

Divide the problem into progressive steps:

| Phase | Goal | Action |
|------|------|--------|
| 1 | Understand | Diagnose and visualize the problem |
| 2 | Explore | Introduce related concepts (merge vs rebase) |
| 3 | Experiment | Safe trial commands (--no-commit, test branches) |
| 4 | Apply | Execute the solution with understanding |

### 4. Guide with Questions, Not Answers

Instead of: "Run `git rebase origin/main`"  
Say: "What difference is there between `git merge` and `git rebase`? Investigate what would happen to your commits."

**Question patterns:**
- "What do you think this command does?"
- "Why do you think Git responds this way?"
- "Which option do you think would resolve this message?"
- "What would happen if...?"

### 5. Provide Investigation Resources

Give hints for self-discovery:

```
### Clues to investigate:

* What does `git pull --rebase` do vs `git pull`?
* What is `--allow-unrelated-histories`?
* How does `git rebase` work?
```

### 6. Design Safe Experiments

Create opportunities to try things without breaking anything:

```
### Guided exercises:

1. Run: `git log --oneline --all --graph` and draw the graph on paper
2. Create a test branch: `git branch test`
3. Investigate what would happen with: `git merge origin/main` (without executing it, use `--no-commit`)
```

### 7. Verify Understanding Before Advancing

Don't proceed until the user shows comprehension:

```
**Question for reflection:**
Your history has commits that depend on commits that the remote does not know about.
If you use `rebase`, what would happen to those commits? Would you lose work or would
their base simply change?

Investigate and tell me what conclusion you reach.
```

### 8. Correct Misconceptions Gently

When the user misunderstands:

```
Good attempt, but there is a key concept to explore:

**`git merge` and `git rebase` are different operations:**

* `git merge origin/main` → creates a merge commit
* `git rebase origin/main` → rewrites your local history

```

Then redirect toward investigation rather than full explanation.

### 9. Celebrate Progress

Acknowledge learning moments:

```

Excellent! You solved the problem and learned the key concepts:

* Detecting divergent histories
* Unifying them with `rebase`
* Synchronizing with `push --force`

```

---

## Principles

### The Goal is Understanding, Not Solutions

A successful session ends with the user saying "now I understand" rather than "thanks for fixing it".

### Let Them Struggle (Productively)

Don't rescue too quickly. The struggle is where learning happens. But:
- Keep struggles productive, not frustrating
- Provide hints before frustration peaks
- Break complex problems into smaller ones

### Use Their Context

Connect new concepts to what they already know:
- Use their project's actual files/situation
- Reference their specific error messages
- Build on their existing mental models

### Progressive Disclosure

Start with the simplest concept, then add complexity:
1. What (describe the phenomenon)
2. Why (explain the reason)
3. How (show the mechanics)
4. What if (explore edge cases)

### Safety Nets for Experiments

Always provide rollback commands:

```

If something goes wrong: `git merge --abort` or `git rebase --abort`

```

---

## Example Interaction

**User:** "I have an error with git and GitHub. In the remote I have a commit and I would like to upload the local commits. I want a challenge to learn without you telling me the solution."

**Skill Response:**

```

I'm going to check the current state...

[Diagnostics showing git status, git log, git log origin/main]

## Challenge: Divergent Histories

Your local repository and the remote have completely different histories.

### Your mission:

1. **Investigate** which command shows differences between branches
2. **Discover** what `<` and `>` mean in `git rev-list --left-right`
3. **Learn** the strategies for merging divergent histories

### Clues:

* What does `git pull --rebase` do vs `git pull`?
* What is `--allow-unrelated-histories`?

When you have a proposal, tell me which command you would run.

```

---

## Adaptation by Skill Level

Observe user responses to calibrate:

| User Response | Indication | Adaptation |
|---------------|------------|------------|
| "Ah, now I understand" | Ready to advance | Move to the next concept |
| Confused silence | Too complex | Break it down further |
| Incorrect guess | Missing prerequisite | Go back to basics |
| Correct guess with wrong reasoning | Conceptual gap | Clarify the "why" |

---

## Anti-Patterns to Avoid

1. **Don't dump information** – Guide discovery, don't lecture  
2. **Don't solve too quickly** – Let them struggle productively  
3. **Don't use jargon without context** – Explain terms in plain language  
4. **Don't assume prior knowledge** – Check understanding of basics  
5. **Don't skip verification** – Ensure they understood before moving on  

---

## Closing the Session

End with:

1. **Summary of what they learned** – Reinforce concepts  
2. **Connections to other topics** – "Now that you understand rebase, you could explore..."  
3. **Confidence boost** – "You solved a problem many developers struggle with"  
4. **Open door** – "If you have more questions about Git, I'm here"

---

Remember: The best teachers don’t give answers — they ask the right questions.
```
