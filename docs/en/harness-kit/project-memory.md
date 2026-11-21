# Project memory

## What it is

A few plain files in the repository that people and agents read at the start of work and append to when they learn something worth keeping. Memory holds what the code and the git history do not say: why something is the way it is, the trap someone already fell into, the convention nobody wrote down.

## Why it pays off

An agent starts every session without memory of the last one. Without a written memory, the same facts are rediscovered every time, slowly and sometimes wrongly. A small, tended memory turns one-off discoveries into an asset the whole team and every tool can use.

!!! info "Evidence level: reference implementation"
    A production backend (anonymized) kept about 30 dated learnings over about two months. Its instructions and a session-start hook told the agent to read `memory/context.md` and `memory/learnings.md` before starting work, and a `/retro` command appended new entries at the end. The Harness Lab and `ml-python-base` use the same three files.

## Template

| File | Holds | Update it when |
| --- | --- | --- |
| `context.md` | Where the project is now: what is in progress, active goals, constraints, open threads | A working session starts or ends, or the focus shifts |
| `learnings.md` | Non-obvious facts: gotchas, why something is the way it is, dead ends to avoid | You learn something that would have saved you time |
| `patterns.md` | Conventions specific to this codebase: naming, layering, test style | You notice or establish a pattern others should follow |

Every entry has the same shape:

```markdown
## <short title>: <YYYY-MM-DD>

<One or two sentences of fact.>

**Why it matters:** <the consequence>
**How to apply:** <what to do next time>
```

Rules to put in `memory/README.md`:

```markdown
- One fact per entry. If it grows, split it.
- Absolute dates (2026-11-21), never "yesterday".
- Delete an entry that turns out to be wrong; do not leave it to mislead.
- Do not repeat what the code, the README, or a commit message already says.
- Link the decision record when an entry explains a decision.
```

## When to use it and when to skip it

Write an entry the moment you learn something that would have saved you time, when the focus of the project shifts, or when a convention appears that others should follow.

Skip it for anything the code, the documentation, or the commit message already says, for tiny changes where nothing surprising happened, and for temporary debugging notes. Those notes are working state: they belong to the task and disappear with it.

## What failed in practice

- **Memory grew without limit.** In one reference repository `learnings.md` passed 3,500 lines. Nobody, person or agent, skims that at the start of a session, so the memory stopped doing its job.
- **Entries outlived the facts.** A conventions file cited a CI workflow that no longer existed. The agent trusted a rule that nothing enforced anymore.

!!! tip "Evidence level: guide recommendation"
    Give memory a size budget: `learnings.md` should be skimmable in about two minutes. When it grows past that, move settled facts into `patterns.md` or the regular documentation, and delete what is no longer true. Pruning is part of the work, not a cleanup project.

## How to check it is healthy

- `context.md` changed during the last week of active work.
- `learnings.md` still fits the size budget.
- Every file path, command, or workflow an entry names still exists.
- Wrong entries were deleted, not left with a note.

## Go deeper

- [State and continuity](../concepts/state-and-continuity.md): the difference between working state, project memory, and organizational knowledge.
- [Decision records](decision-records.md): where decisions go when they are hard to reverse.
- [The starter kit](index.md): the `memory/` folder in context.
