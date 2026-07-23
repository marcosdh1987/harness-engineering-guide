# Getting Started with OpenCode

The harness is **tool-agnostic**: the governance docs and skills under `.github/` are the
same ones Claude Code uses — only the **adapter file** OpenCode reads and the native
layout differ. Learn the shared model once, then apply this short delta.

## The on-ramp is shared

Do these pages from the Claude path — they are identical for OpenCode, because they operate
on the governed source (`.github/skills/`, `make sync-skills`), not on any one tool:

1. [Claude Code Basics](claude-code-basics.md) — the mental model (durable context, plan vs. direct, sessions).
2. [Minimal Setup](minimal-setup.md) — the minimal governance file + `SKILL.md`.
3. [Use and Modify Skills](use-and-modify-skills.md) and [Create Your First Skill](create-your-first-skill.md) — creating/using skills is the same flow.

!!! tip "One substitution"
    Wherever those pages say `CLAUDE.md`, your adapter is **`OPENCODE.md`**. Everything else —
    the `.github/skills/<name>.md` source, `make sync-skills`, `make check-sync`, and the
    `<!-- BEGIN/END GENERATED SKILLS -->` sentinel region — is identical.

## What OpenCode reads

| Artifact | What it provides |
|---|---|
| `OPENCODE.md` | OpenCode's integration profile, tool-use rules, and safety policy (its `CLAUDE.md` equivalent) |
| `.opencode/skills/` | Governed skills projected for OpenCode discovery |
| `.opencode/agents/` | Governed agents in OpenCode's native format |
| `opencode.jsonc` | OpenCode workspace/model configuration |

For the full study guide, see [Tools › OpenCode](../tools/opencode.md).

## The OpenCode-specific delta

!!! note "Native OpenCode capability"
    OpenCode reads persistent instructions, discovers skills projected into its native
    layout, and is configured via JSON/JSONC — see the
    [official docs](https://opencode.ai/docs/).

!!! tip "How ml-python-base applies it"
    `OPENCODE.md`, `.opencode/skills/`, and `.opencode/agents/` are all **generated** from the
    same governed source by `make sync-skills`. Edit `.github/skills/` and `.github/agents/`,
    never the `.opencode/` output — then re-sync. `make check-sync` fails if `.opencode/`
    drifts.

## Next

- Create a skill (shared flow) → [Create Your First Skill](create-your-first-skill.md)
- The features map → [Leverage More](leverage-more.md)
- OpenCode depth → [Tools › OpenCode](../tools/opencode.md)

## Official documentation

- [OpenCode Docs](https://opencode.ai/docs/)
- [OpenCode Config](https://opencode.ai/docs/config/)

## References

- [Tools › OpenCode](../tools/opencode.md)
- [Reference › Skills](../reference-implementation/ml-python-base/skills.md)
- [Reference › Adapters](../reference-implementation/ml-python-base/adapters.md)
