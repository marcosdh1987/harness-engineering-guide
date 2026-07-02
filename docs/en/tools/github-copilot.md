# GitHub Copilot

GitHub Copilot occupies a different place in the harness: it usually appears inside the editor, close to the file being changed, so it needs durable instructions that are easy to discover from repository context. In [`ml-python-base`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0), Copilot consumes an adapted version of the shared rules through `.github/copilot-instructions.md`.

## Role in the workflow

Copilot helps with inline suggestions, editor chat, conceptual navigation, and snippet generation. The harness should not assume Copilot will execute the entire development loop on its own; its strength is keeping suggestions aligned with repository rules while the developer remains in control.

The goal is for Copilot to understand:

- architecture and style conventions;
- boundaries between `src/`, `tests/`, notebooks, and data;
- expected validation commands;
- when a suggestion needs tests, docs, or additional review.

## What Copilot Reads

| Artifact | What it provides | Source |
|---|---|---|
| [`.github/copilot-instructions.md`](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.github/copilot-instructions.md) | Persistent repository instructions for Copilot. | Generated from shared rules |
| [`.github/architecture.md`](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.github/architecture.md) | Layers, boundaries, and design criteria. | Governed source |
| [`.github/standards.md`](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.github/standards.md) | Python, `uv`, Ruff, mypy, and validation checklist standards. | Governed source |
| [`adapters/templates/copilot.md.j2`](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/adapters/templates/copilot.md.j2) | Template that packages shared rules for Copilot. | Adapter |

Copilot does not need a native skills folder like `.opencode/skills/` or `.codex/skills/`; its integration relies on persistent instructions and context near the file.

## Files and Folders Involved

The `.github/` folder has a double role. First, it contains the human-governed harness sources: architecture, standards, automation, domain boundaries, and orchestration. Second, it hosts the file Copilot discovers as persistent instruction: `.github/copilot-instructions.md`.

The `copilot.md.j2` adapter avoids hand-copying the same policies. When shared rules change, `make sync-skills` can regenerate Copilot's instruction file, and `make check-sync` can detect drift.

## Source of Truth vs Generated

The source of truth is the governed rules and adapter templates. `.github/copilot-instructions.md` is output prepared for Copilot. If a rule applies to all tools, change it in the shared layer, not only in the Copilot file.

This distinction matters because Copilot works very close to the code: a duplicated or stale instruction can produce suggestions that look locally correct but contradict the harness.

## Mini Study Flow

1. Read [rules](../reference-implementation/ml-python-base/rules.md) to see the shared policies.
2. Open [`.github/copilot-instructions.md`](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.github/copilot-instructions.md) and observe how they are compacted for Copilot.
3. Review [adapters](../reference-implementation/ml-python-base/adapters.md) and locate `copilot.md.j2`.
4. Finish with [automation](../reference-implementation/ml-python-base/automation.md) to understand which commands validate suggestions before they are merged.

## Official Documentation

- [GitHub Copilot Docs](https://docs.github.com/copilot): main Copilot documentation.
- [Repository custom instructions](https://docs.github.com/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot): how to add persistent repository instructions.
- [About customizing Copilot responses](https://docs.github.com/copilot/concepts/about-customizing-github-copilot-chat-responses): instruction types and precedence.
- [Copilot cloud agent](https://docs.github.com/copilot/concepts/agents/cloud-agent/about-cloud-agent): context for delegated agentic workflows on GitHub.

## References

- [`ml-python-base` on GitHub](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0)
- [Reference implementation rules](../reference-implementation/ml-python-base/rules.md)
- [Artifact inventory](../reference-implementation/ml-python-base/inventory.md)
- [Adapter projection](../reference-implementation/ml-python-base/adapters.md)
