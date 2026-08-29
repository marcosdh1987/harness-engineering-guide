# Claude Code Basics: Your First Session

Before any setup, get the mental model right. Claude Code is not a smarter chat box — it
is a semi-autonomous agent that reads, edits, and runs code, guided by a **durable
operating layer** you control.

## Chat vs. a durable operating layer

In raw chat you re-explain your project, conventions, and constraints every session, and
none of it persists. A harness flips that: the rules, skills, and context live in the
repository, so every teammate — and every session — starts from the same ground. This is
the difference between a one-off *prompt* and a reusable *skill*; see
[Skills vs Prompts](../concepts/skills-vs-prompts.md).

## What Claude Code reads

At a glance, Claude Code picks up context from a few well-known places:

| Artifact | What it provides |
|---|---|
| `CLAUDE.md` | Project memory: governance pointers, working loop, command policy |
| `.claude/skills/` | Skills Claude can discover and invoke |
| `.claude/hooks/` | Session reminders / non-blocking nudges |
| `.claude/settings.json` | Workspace settings |

For the full breakdown of how the reference repo wires these, read
[Tools › Claude Code](../tools/claude-code.md) — this page keeps it short on purpose.

## Project memory: the `CLAUDE.md` idea

`CLAUDE.md` is your project's memory — persistent instructions Claude reads at the start
of work.

!!! note "Native Claude Code capability"
    Per the [Memory docs](https://docs.anthropic.com/en/docs/claude-code/memory), a
    project-level `CLAUDE.md` takes precedence over your personal/global one, and you can
    split large memory into modules with `@path` imports to avoid bloating the context.

!!! tip "How ml-python-base applies it"
    The reference repo uses a **single governed `CLAUDE.md` adapter** with an
    auto-generated skills region. It does **not** use `@path` imports — it directs context
    by instruction (a short `## Governance` section that points to the governance docs).
    The full native-vs-applied map is on [Leverage More](leverage-more.md).

You build the minimal, understood version of this file on the next page.

## Plan Mode vs. Direct Execution

Match the mode to the change:

- **Plan Mode** — for large or structural work (a refactor across many files, a
  migration). Claude explores and proposes a strategy that you validate *before* it edits
  anything. This mirrors the harness working loop **Ground → Plan → Delegate → Verify →
  Compound**; see [Patterns › Working Loop](../patterns/working-loop.md) and the reference
  [working loop](../reference-implementation/ml-python-base/working-loop.md).
- **Direct Execution** — for small, well-scoped fixes where the error is obvious and no
  redesign is needed.

!!! tip "Rule of thumb"
    If you can't hold the whole change in your head, plan first. If the diff is small and
    the cause is clear, just do it.

## Sessions: resuming and telling Claude what changed

Long work spans sessions. Two habits matter:

- **Resume** an existing session (`--resume`) instead of starting cold, so Claude keeps
  the prior context.
- When **a human edits files** outside the session, tell Claude explicitly — it needs to
  re-read the changed state rather than assume it will notice on its own.

!!! note "Native Claude Code capability"
    Claude Code supports resuming sessions and forking a session to explore divergent
    approaches from a common state.

## Mini study flow

1. Open a repo that has a `CLAUDE.md` and skim its `## Governance` section.
2. Ask Claude to explain the project's working loop back to you.
3. Try one small fix in Direct Execution; try one larger ask in Plan Mode.
4. Next: build your own [Minimal Setup](minimal-setup.md).

## Official documentation

- [Claude Code Overview](https://docs.anthropic.com/en/docs/claude-code/overview)
- [Claude Code Memory](https://docs.anthropic.com/en/docs/claude-code/memory)

## References

- [Skills vs Prompts](../concepts/skills-vs-prompts.md)
- [Tools › Claude Code](../tools/claude-code.md)
- [Patterns › Working Loop](../patterns/working-loop.md)
