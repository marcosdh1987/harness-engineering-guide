# Getting Started with Codex

You don't need a separate on-ramp for Codex. The harness is **tool-agnostic**: the
governance docs and skills under `.github/` are the same ones Claude Code uses — only the
**adapter file** Codex reads and the native layout differ. Learn the shared model once,
then apply this short delta.

## The on-ramp is shared

Do these pages from the Claude path — they are identical for Codex, because they operate
on the governed source (`.github/skills/`, `make sync-skills`), not on any one tool:

1. [Claude Code Basics](claude-code-basics.md) — the mental model (durable context, plan vs. direct, sessions).
2. [Minimal Setup](minimal-setup.md) — the minimal governance file + `SKILL.md`.
3. [Use and Modify Skills](use-and-modify-skills.md) and [Create Your First Skill](create-your-first-skill.md) — creating/using skills is the same flow.

!!! tip "One substitution"
    Wherever those pages say `CLAUDE.md`, your adapter is **`AGENTS.md`**. Everything else —
    the `.github/skills/<name>.md` source, `make sync-skills`, `make check-sync`, and the
    `<!-- BEGIN/END GENERATED SKILLS -->` sentinel region — is identical.

## What Codex reads

| Artifact | What it provides |
|---|---|
| `AGENTS.md` | Codex's integration profile and agent roles (its `CLAUDE.md` equivalent) |
| `.codex/skills/` | Governed skills projected for Codex discovery |
| `.codex/agents/` | Governed agents as Codex subagent `.toml` files |

For the full study guide, see [Tools › Codex](../tools/codex.md).

## The Codex-specific delta

!!! note "Native Codex capability"
    Codex loads project instructions from `AGENTS.md`, packages procedures as skills, and
    supports specialized subagents — see the
    [official docs](https://developers.openai.com/codex).

!!! tip "How ml-python-base applies it"
    `AGENTS.md`, `.codex/skills/`, and `.codex/agents/*.toml` are all **generated** from the
    same governed source by `make sync-skills`. Edit `.github/skills/` and `.github/agents/`,
    never the `.codex/` output — then re-sync. `make check-sync` fails if `.codex/` drifts.

## Next

- Create a skill (shared flow) → [Create Your First Skill](create-your-first-skill.md)
- The features map → [Leverage More](leverage-more.md)
- Codex depth → [Tools › Codex](../tools/codex.md)

## Official documentation

- [Codex Docs](https://developers.openai.com/codex)
- [Custom instructions with `AGENTS.md`](https://developers.openai.com/codex/guides/agents-md)
- [Agent Skills](https://developers.openai.com/codex/skills)
- [Subagents](https://developers.openai.com/codex/subagents)

## References

- [Tools › Codex](../tools/codex.md)
- [Reference › Agents](../reference-implementation/ml-python-base/agents.md)
- [Reference › Adapters](../reference-implementation/ml-python-base/adapters.md)
