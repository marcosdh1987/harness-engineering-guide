# Create Your First Skill in 3 Steps

You have the [minimal `SKILL.md` template](minimal-setup.md).
Here is the whole flow to turn it into a skill Claude can discover.

## Before you start

Reuse the minimal template. The only required frontmatter is:

```markdown
---
name: <skill_name>
description: <one line — when Claude should use this>
---
```

`name` must equal the filename without `.md`. The `description` is the semantic trigger —
write it as "Use when …" so Claude knows when to reach for the skill.

## The 3-step flow

1. **Write** the source file `.github/skills/<name>.md` using the minimal template
   (frontmatter + `# Skill: <name>` + Purpose / Required Input / Output Format / Execution
   Rules, ending with a governance-compliance line).
2. **Sync** it into the native layout:
   ```bash
   make sync-skills          # full: ingest + link + regenerate adapter regions
   # or, just the Claude symlink:
   make setup-claude-skills
   ```
3. **Verify** there's no drift (this is the CI gate):
   ```bash
   make check-sync
   ```

## What the engine does for you

`make sync-skills` doesn't just copy a file — it wires the skill into every tool adapter:

- creates the symlink `.claude/skills/<name>/SKILL.md → ../../../.github/skills/<name>.md`;
- regenerates the managed region **between the sentinels** in `CLAUDE.md`, so your new
  skill appears in the "Internal skills" list;
- refreshes the other adapters (OpenCode, Codex, Copilot, Antigravity) from the same
  source, so the skill is available everywhere without hand-copying.

See [Reference › Adapters](../reference-implementation/ml-python-base/adapters.md) and
[Reference › Drift Control](../reference-implementation/ml-python-base/drift-control.md).

## A worked example

A tiny, realistic skill — summarize a pull request:

```markdown
---
name: summarize_pr
description: Use to produce a concise, reviewer-facing summary of a pull request's diff.
---

# Skill: summarize_pr

## Purpose
Turn a PR diff into a short summary a reviewer can read in under a minute.

## Required Input
- The PR number or the diff to summarize.

## Output Format
- A 3–5 bullet summary: what changed, why, and any risk to review.

## Execution Rules
1. Read the diff (`gh pr diff <n>` or the provided patch).
2. Group changes by intent, not by file.
3. Flag anything that touches public APIs or data.
4. Comply with `.github/architecture.md`, `.github/standards.md`.
```

Save it as `.github/skills/summarize_pr.md`, run `make sync-skills`, then `make
check-sync`. It now shows up in `.claude/skills/` and in the `CLAUDE.md` skills region.

## Go deeper

This page is the quickstart. For the full authoring discipline — scenario framing,
validation, failure modes, and reflection — do the lab:

- [Lab: Create a Skill](../labs/create-a-skill.md)
- [Patterns › Skill Design](../patterns/skill-design.md)

## Official documentation

- [Claude Code Skills](https://docs.anthropic.com/en/docs/claude-code/skills)

## References

- [Reference › Adapters](../reference-implementation/ml-python-base/adapters.md)
- [Reference › Drift Control](../reference-implementation/ml-python-base/drift-control.md)
- [Lab: Validate a Change](../labs/validate-a-change.md)
