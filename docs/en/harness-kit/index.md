# The complete harness

Skills get the attention, but in the reference projects most of the day-to-day value came from simpler pieces: a short rules file, a project memory, one-page decision records, approved plans, a few commands and hooks, and one gate that can fail. This section documents each piece with a template you can copy.

!!! info "Evidence level: reference implementation"
    In a production backend (anonymized) over about two months (roughly 1,000 commits), the artifacts people and agents actually wrote most were decision records (over 100) and plans (about 27). Its skill catalog shrank from 27 flat skills to 9 entry points. One team, one codebase: read it as a signal of where the value is, not as a benchmark.

## The starter kit

It works in a repository you already have, in any language. Only the skills are written for a Python stack today; the [skills section](#skills) below says what to adapt.

```text
your-repo/
├── AGENTS.md          short rules + "how big is the task?" table
├── CLAUDE.md          one line that imports AGENTS.md (for Claude Code)
├── memory/            README.md · context.md · learnings.md · patterns.md
├── docs/adr/          README.md (when to write one) + 0000-template.md
├── docs/plans/        approved plans
├── <tool>/skills/     the 7 starter skills, in the folder your tool reads
└── make check         or the command that already verifies your project
```

### `AGENTS.md`

The one file every tool reads. Keep it short enough to read in a minute: it is loaded on every session.

```markdown
# AGENTS.md

## What this project is
<One paragraph: what it does, who uses it, and what must never break.>

## How to work here
Use the loop: understand, plan when needed, execute, verify, learn.
Scale the ceremony to the task:

| If the task is... | Do this |
| --- | --- |
| Small and clear (typo, one-line fix) | Make the change, run the narrowest check |
| Bounded (a bug, a small feature) | Quick brainstorm, short plan, execute, verify |
| New or ambiguous (new module, risky change) | Write a design, get it approved, then plan and execute |

## Before you start
- Read `memory/context.md` and skim `memory/learnings.md`.
- Search the code before editing it.

## Done means
- `make check` passes (or: <your verification command>).
- A decision that is hard to reverse has a record in `docs/adr/`.
- Anything non-obvious you learned goes to `memory/learnings.md`.

## Never
- Commit, push, or merge without asking.
- Put secrets, personal data, or customer data in code, logs, or memory.
```

### `CLAUDE.md`

Claude Code reads `CLAUDE.md` and can import other files with `@path`, so one line keeps a single source of rules:

```markdown
@AGENTS.md
```

### `memory/`

```text
memory/
├── README.md       how to write an entry
├── context.md      where the project is now: focus, open threads
├── learnings.md    non-obvious facts: gotchas, dead ends, why things are so
└── patterns.md     conventions others should follow
```

Every entry has the same shape:

```markdown
## <short title>: <YYYY-MM-DD>

<One or two sentences of fact.>

**Why it matters:** <the consequence>
**How to apply:** <what to do next time>
```

### `docs/adr/`

One page per decision that is hard to reverse. Copy this as `docs/adr/0000-template.md`:

```markdown
# ADR-NNNN: <the decision, as a sentence>

- **Status:** Proposed <!-- Proposed | Accepted | Superseded by ADR-XXXX -->
- **Date:** YYYY-MM-DD
- **Deciders:** <names or roles>
- **Related:** <other ADRs, memory entries, docs>

## Context
What forced a decision? State the facts so someone who was not there understands.

## Decision
"We will ..." Specific enough to act on.

## Consequences
What becomes easier, what becomes harder, what follow-up work it creates.

## Alternatives considered
- <Option>: why it was not chosen.
```

### `docs/plans/`

One file per approved plan, named `YYYY-MM-DD-<topic>.md`: the steps, the files each step touches, and how each step is verified. A plan starts after the design is approved and does not reopen it.

### Skills { #skills }

The seven starter skills are the template's `minimal` harness level. [Start with few skills](few-skills.md) explains why seven and what each one is for.

| Skill | Source in `ml-python-base` |
| --- | --- |
| `brainstorm_quick` | [.github/skills/brainstorm_quick.md](https://github.com/marcosdh1987/ml-python-base/blob/main/.github/skills/brainstorm_quick.md) |
| `plan_and_execute_feature` | [.github/skills/plan_and_execute_feature.md](https://github.com/marcosdh1987/ml-python-base/blob/main/.github/skills/plan_and_execute_feature.md) |
| `research_current_info` | [.github/skills/research_current_info.md](https://github.com/marcosdh1987/ml-python-base/blob/main/.github/skills/research_current_info.md) |
| `systematic_debugging` | [.github/skills/systematic_debugging.md](https://github.com/marcosdh1987/ml-python-base/blob/main/.github/skills/systematic_debugging.md) |
| `verify_changes` | [.github/skills/verify_changes.md](https://github.com/marcosdh1987/ml-python-base/blob/main/.github/skills/verify_changes.md) |
| `writing-plans` | [.github/skills-external/writing-plans/SKILL.md](https://github.com/marcosdh1987/ml-python-base/blob/main/.github/skills-external/writing-plans/SKILL.md) |
| `requesting-code-review` | [.github/skills-external/requesting-code-review/SKILL.md](https://github.com/marcosdh1987/ml-python-base/blob/main/.github/skills-external/requesting-code-review/SKILL.md) |

Each tool reads skills from its own folder. These are the folders the reference template projects to; check your tool's documentation if they change:

| Tool | Folder |
| --- | --- |
| Claude Code | `.claude/skills/<name>/SKILL.md` |
| OpenCode | `.opencode/skills/<name>/SKILL.md` |
| Codex | `.codex/skills/<name>/SKILL.md` |
| Antigravity | `.agents/skills/<name>/SKILL.md` |
| GitHub Copilot | No native skills folder: put the rules and the routing table in `.github/copilot-instructions.md` |

In the template, those per-tool folders are symlinks generated by `make sync-skills`, so downloading them from GitHub gives you a path, not the skill. Copy from the governed source instead:

```bash
mkdir -p .claude/skills/verify_changes
curl -fsSL https://raw.githubusercontent.com/marcosdh1987/ml-python-base/main/.github/skills/verify_changes.md \
  -o .claude/skills/verify_changes/SKILL.md
```

Outside a Python stack, adapt a few lines in each internal skill:

- The verification command (`make check`, `pytest`) becomes your build and test command.
- References to `.github/architecture.md`, `.github/standards.md`, and `.github/domain-boundaries.md` point to your own `AGENTS.md`, or go away.
- The language-specific sources in `research_current_info` (Python docs, `uv`, `ruff`) become your stack's official documentation.

Starting a new Python project instead? The template brings the whole kit and the `minimal` level by default:

```bash
git clone https://github.com/marcosdh1987/ml-python-base my-project
cd my-project
make init NAME=my_project LEVEL=minimal
```

## How the pieces map to the loop

| Loop step | Pieces |
| --- | --- |
| Understand | `AGENTS.md`, `memory/context.md`, `memory/learnings.md` |
| Plan or design | The routing table, `docs/plans/` |
| Execute | Skills, commands |
| Verify | `make check`, hooks |
| Learn | `memory/learnings.md`, `docs/adr/` |

## Pages in this section

- [Start with few skills](few-skills.md): the seven starter skills and when to add more.
