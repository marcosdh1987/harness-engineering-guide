# Minimal Setup: Copy This, Understand This

A small `CLAUDE.md` you can defend line by line beats a large one you inherited and don't
understand. This page gives you a minimal, *understood* starting point — copy it, then
grow it deliberately.

## The goal: small and owned

The reference `CLAUDE.md` in `ml-python-base` is a ~186-line governed adapter — and that
size is exactly what overwhelms newcomers. The good news: **almost all of it is editable
prose.** Only one small region is machine-managed. So start minimal and add only what you
understand.

## Minimal `CLAUDE.md`

Copy this into your project root and adjust the project name:

```markdown
# <Project> — Claude Code Adapter

## Governance
Always read and apply before generating code or plans:
- `.github/architecture.md`
- `.github/standards.md`
- `.github/domain-boundaries.md`

## Automation
Skills are generated. After adding or editing a skill under `.github/skills/`, run
`make sync-skills`. CI enforces `make check-sync`.

<!-- BEGIN GENERATED SKILLS (managed by skills_sync; do not edit) -->
<!-- END GENERATED SKILLS -->
```

What each part is, and whether you edit it:

| Part | Why it's here | Edit it? |
|---|---|---|
| `## Governance` pointer | Directs context by instruction to the three "always read" governance docs | Yes — plain prose |
| `## Automation` pointer | One line telling humans and agents how skills propagate | Yes — plain prose |
| `BEGIN/END GENERATED SKILLS` markers | Mandatory sentinels the sync engine fills with the skills list | **No** — machine-managed |

!!! warning "The two sentinels are not optional"
    The skills-sync engine regenerates everything **between** those two comment markers and
    **errors out if they are missing** (and `make check-sync` fails). Keep them exactly as
    written, even in an otherwise tiny `CLAUDE.md`. Everything *outside* them is yours.

!!! note "Native Claude Code capability"
    `CLAUDE.md` is native project memory; you could also split it with `@path` imports.

!!! tip "How ml-python-base applies it"
    The reference repo keeps a single file and fills the sentinel region from
    `.github/skills/`. Grow the governance/automation prose as your project needs it —
    the [full adapter](../reference-implementation/ml-python-base/adapters.md) shows how
    far it can go.

## Minimal internal `SKILL.md`

Skills are how you teach Claude a repeatable task. An internal skill is a single Markdown
file with two-field frontmatter and a small, structured body:

```markdown
---
name: <skill_name>
description: <one line — when Claude should use this>
---

# Skill: <skill_name>

## Purpose
<what repeatable task this automates>

## Required Input
<what the caller must provide>

## Output Format
<what it returns>

## Execution Rules
1. <step>
2. <step>
3. Comply with `.github/architecture.md`, `.github/standards.md`.
```

!!! note "Native Claude Code capability"
    Skill frontmatter can also carry fields like `allowed-tools` (restrict tools) and
    `context: fork` (run in an isolated subagent) — see
    [Use & Modify Skills](use-and-modify-skills.md).

!!! tip "How ml-python-base applies it"
    Internal skills here use **minimal frontmatter** (`name` + `description` only) and
    always end their `Execution Rules` with a governance-compliance line. Keep yours
    minimal until you need more.

You put this file to work — sync it and see it appear to Claude — on
[Create Your First Skill](create-your-first-skill.md).

## What NOT to copy

- **Do not** hand-edit files under `.claude/skills/` — that layout is *generated* and your
  change will be overwritten.
- **Do not** hand-edit `.github/skills-external/<name>/SKILL.md` — external skills arrive
  via installers and `make sync-skills`; edits there are lost on the next sync.

## Next

- Learn to run and tweak what already exists → [Use and Modify Skills](use-and-modify-skills.md)
- Author your own → [Create Your First Skill](create-your-first-skill.md)

## Official documentation

- [Claude Code Skills](https://docs.anthropic.com/en/docs/claude-code/skills)
- [Claude Code Memory](https://docs.anthropic.com/en/docs/claude-code/memory)

## References

- [Reference › Skills](../reference-implementation/ml-python-base/skills.md)
- [Reference › Adapters](../reference-implementation/ml-python-base/adapters.md)
- [Patterns › Skill Design](../patterns/skill-design.md)
