# Commands

## What it is

A command is a short, named shortcut a person types, such as `/plan`, `/adr`, `/retro`, or `/verify`, that tells the agent which procedure to follow at a key moment of the loop. A good command is thin: it points at skills, memory, and the gate instead of repeating them.

## Why it pays off

Commands put the important moments of the loop one keystroke away, and they make a team work the same way without memorizing procedures. Because each one is a small file in the repository, it is reviewed and versioned like code.

!!! info "Evidence level: reference implementation"
    A production backend (anonymized) shipped six commands, each about 20 lines long. The ones tied to an existing habit were used most: `/adr` appears about 30 times across its documents and history, while `/orchestrate`, for running parallel agents, appears about 6 times. The Harness Lab and `ml-python-base` ship the same core: `/plan`, `/adr`, `/retro`, `/verify`.

## Template

The core four, and what each one points at:

| Command | What it does | Points at |
| --- | --- | --- |
| `/plan <goal>` | Reads the code and memory first, picks the ideation skill, writes a phased plan, writes no code | `memory/`, `brainstorm_quick`, `writing-plans` |
| `/adr <decision>` | Scaffolds a decision record from the template, adds it to the index, asks what it had to assume | `docs/adr/` |
| `/retro` | Reviews the diff, appends short entries to memory, suggests `/adr` if a decision was made | `memory/`, `docs/adr/` |
| `/verify` | Runs the gate and reports pass or fail honestly | `make check`, `verify_changes` |

In Claude Code, a command is a Markdown file in `.claude/commands/`; `$ARGUMENTS` is replaced with what you type after the command name. For example, `.claude/commands/retro.md`:

```markdown
---
description: Close out work with a short retrospective and update project memory.
allowed-tools: Read, Edit, Write, Bash(git diff:*), Bash(git log:*)
---

Run a brief retrospective on the work done in this session.

1. Review what changed: `git diff`, `git log` for this branch, and the conversation.
2. Keep only durable, non-obvious knowledge: gotchas, why a choice was made,
   dead ends, new conventions. Skip what the code or commit messages already say.
3. Append short entries, one fact each, using the format in `memory/README.md`:
   facts to `memory/learnings.md`, conventions to `memory/patterns.md`,
   current focus to `memory/context.md`.
4. If a decision that is hard to reverse was made, suggest running `/adr`.
5. Summarize what you recorded in three to five bullets.
```

Other tools have their own mechanism for reusable prompts; keep the same names so people can move between tools.

## When to use it and when to skip it

Create a command for a moment that happens several times a week: starting a plan, recording a decision, closing a session, verifying. Skip it for procedures you run once in a while; a skill or a note is enough. Never copy a skill's body into a command: point at the skill.

## What failed in practice

- **Commands for habits the team did not have yet were used least.** The decision command thrived because the team already wrote decisions; the parallel-agents command stayed rare. A command makes a habit easier; it does not create one.

!!! tip "Evidence level: guide recommendation"
    Keep four to six commands. If a command grows past one screen, part of it belongs in a skill or in `AGENTS.md`.

## How to check it is healthy

- Each command file fits on one screen.
- Each command names the skill, folder, or target it relies on.
- Every command was used in the last month; remove the ones that were not.
- The command names are the same across the tools your team uses.

## Go deeper

- [Claude Code basics](../start-here/claude-code-basics.md): how commands, skills, and `CLAUDE.md` fit together.
- [Decision records](decision-records.md) and [project memory](project-memory.md): what `/adr` and `/retro` write to.
- [Quality gates](quality-gates.md): what `/verify` runs.
