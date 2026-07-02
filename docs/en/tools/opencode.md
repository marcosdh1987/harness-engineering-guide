# OpenCode

OpenCode is a useful example for studying how a harness separates stable repository intent from the native shape each tool expects. In [`ml-python-base`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0), OpenCode is not treated as an island: it consumes shared rules, governed skills, and generated adapters from the same system that serves the other tools.

## Role in the workflow

OpenCode acts as a guided exploration, editing, and execution tool. It becomes more useful when the repository already explains which architecture to respect, which commands validate changes, and which repeatable workflows should be invoked as skills.

In the harness, OpenCode does three jobs:

- reads persistent repository instructions before improvising;
- discovers skills projected into its native structure;
- executes changes against shared gates such as `make check` and `make check-sync`.

## What OpenCode Reads

In the reference implementation, the main artifacts are:

| Artifact | What it provides | Source |
|---|---|---|
| [`OPENCODE.md`](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/OPENCODE.md) | Integration profile, tool-use rules, MCP guidance, and safety policies. | Rendered source of truth for OpenCode |
| [`.opencode/`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.opencode/) | Workspace configuration, modules, and native adapter links. | Generated |
| [`.opencode/skills/`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.opencode/skills/) | Governed skills exposed in a shape OpenCode can discover. | Generated from `.github/skills/` |
| [`adapters/templates/opencode.md.j2`](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/adapters/templates/opencode.md.j2) | Template that turns shared rules into OpenCode-specific instructions. | Adapter |

The teaching point is that OpenCode reads a layer compiled for its experience, but that layer should not become a second independent policy.

## Files and Folders Involved

Stable content lives under `.github/`: architecture, standards, domain boundaries, automation, orchestration, internal skills, and locked external skills. The [`src/ml_python_base/skills_sync/`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/src/ml_python_base/skills_sync/) engine takes that intent and projects it into `.opencode/`.

`make sync-skills` updates links, generated blocks, and manifests. `make check-sync` verifies that no one edited generated output by hand. OpenCode can therefore have its own native shape without drifting from the shared harness.

## Source of Truth vs Generated

Edit rules and skills in the governed sources: `.github/*.md`, `.github/skills/`, `.github/skills-external/`, `adapters/`, and the sync registry. Do not treat files under `.opencode/skills/` as primary sources, because the engine may overwrite them.

This separation gives you two study layers:

- **Intent**: what the repository wants any assistant to do.
- **Adapter**: how that intent is packaged for OpenCode to discover and execute.

## Mini Study Flow

1. Read the [`ml-python-base` inventory](../reference-implementation/ml-python-base/inventory.md) and locate `OPENCODE.md`, `.opencode/`, and `.opencode/skills/`.
2. Read [adapters](../reference-implementation/ml-python-base/adapters.md) to understand how `opencode.md.j2` participates in projection.
3. Read [skills](../reference-implementation/ml-python-base/skills.md) and compare a skill in `.github/skills/` with its link in `.opencode/skills/`.
4. Finish with [automation](../reference-implementation/ml-python-base/automation.md) and [drift control](../reference-implementation/ml-python-base/drift-control.md) to see how the native copy is validated.

## Official Documentation

- [OpenCode Docs](https://opencode.ai/docs/): introduction, installation, configuration, and general usage.
- [OpenCode Config](https://opencode.ai/docs/config/): JSON/JSONC configuration format and `opencode.jsonc` options.

## References

- [`ml-python-base` on GitHub](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0)
- [Artifact inventory](../reference-implementation/ml-python-base/inventory.md)
- [Adapter projection](../reference-implementation/ml-python-base/adapters.md)
- [Governed skills](../reference-implementation/ml-python-base/skills.md)
