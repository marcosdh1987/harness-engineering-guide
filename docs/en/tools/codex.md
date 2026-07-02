# Codex

Codex represents the case of a tool that executes code changes with persistent instructions, specialized agents, and clear validation steps. In [`ml-python-base`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0), Codex consumes the harness through agent profiles, projected skills, and shared rules that reduce ambiguity before code is changed.

## Role in the workflow

Codex works best when the repository gives it an explicit contract: which architecture to preserve, which commands to run, when to plan, when to delegate, and how to close a task with evidence. In that loop, Codex can act as implementer, reviewer, documenter, or tester depending on the invoked agent.

The harness provides:

- persistent working instructions;
- agents with clear responsibilities;
- reusable skills for repeatable tasks;
- validation gates before a change is considered done.

## What Codex Reads

| Artifact | What it provides | Source |
|---|---|---|
| [`AGENTS.md`](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/AGENTS.md) | Subagent profile, standard roles, and coordination paths. | Source of truth for Codex/OpenAI Agents |
| [`.codex/`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.codex/) | Adapter configuration and local workspace hooks. | Generated |
| [`.codex/skills/`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.codex/skills/) | Governed skills exposed for Codex discovery. | Generated from `.github/skills/` |
| [`adapters/templates/agents.md.j2`](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/adapters/templates/agents.md.j2) | Template that renders the agent profile from shared rules. | Adapter |

`AGENTS.md` is the conceptual entry point: it explains how Codex should behave inside the repository. `.codex/` is the native layer that makes this intent available to the tool.

## Files and Folders Involved

Agents are governed under [`.github/agents/`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.github/agents/). Skills live in `.github/skills/` and `.github/skills-external/`. The [`src/ml_python_base/skills_sync/`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/src/ml_python_base/skills_sync/) engine compiles those sources into formats Codex can use.

Automation closes the loop: `make sync-skills` regenerates the projection, and `make check-sync` validates that `.codex/` has not drifted.

## Source of Truth vs Generated

Edit agents under `.github/agents/` and shared rules under `.github/*.md`. Treat `.codex/` and `.codex/skills/` as generated adapter output. This rule keeps a Codex-specific fix from becoming invisible to Claude Code, OpenCode, Copilot, or Antigravity.

## Mini Study Flow

1. Read [agents](../reference-implementation/ml-python-base/agents.md) to understand roles such as `documenter`, `reviewer`, `tester`, and `orchestrator`.
2. Open [`AGENTS.md`](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/AGENTS.md) and observe how those roles are presented to Codex.
3. Review [skills](../reference-implementation/ml-python-base/skills.md) and locate the same capability projected into `.codex/skills/`.
4. Use [drift control](../reference-implementation/ml-python-base/drift-control.md) to understand why projection must be verifiable.

## Official Documentation

- [Codex Docs](https://developers.openai.com/codex): main Codex documentation on OpenAI Developers.
- [Custom instructions with `AGENTS.md`](https://developers.openai.com/codex/guides/agents-md): how Codex reads `AGENTS.md` to load project instructions.
- [Agent Skills](https://developers.openai.com/codex/skills): how to package instructions, resources, and scripts as skills.
- [Subagents](https://developers.openai.com/codex/subagents): using specialized agents and parallel workflows.

## References

- [`ml-python-base` on GitHub](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0)
- [Governed agents](../reference-implementation/ml-python-base/agents.md)
- [Artifact inventory](../reference-implementation/ml-python-base/inventory.md)
- [Adapter projection](../reference-implementation/ml-python-base/adapters.md)
