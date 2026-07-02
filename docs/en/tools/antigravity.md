# Antigravity

Antigravity can be studied as another consumer of the same multi-tool harness. In [`ml-python-base`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0), its integration shows an important difference from OpenCode or Codex: some capabilities are copied into a native `.agents/` structure instead of being exposed only as symlinks.

## Role in the workflow

Antigravity receives durable policies, workspace rules, and adapted skills for guided work. The harness should give it the same intent as the other tools, but packaged in the shape its runtime expects.

Its role in the system is to:

- read rules compatible with the Gemini/Antigravity ecosystem;
- discover skills in `.agents/skills/`;
- respect workspace boundaries defined by shared rules;
- participate in the same sync and drift-control loop.

## What Antigravity Reads

| Artifact | What it provides | Source |
|---|---|---|
| [`GEMINI.md`](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/GEMINI.md) | Root rules for Gemini/Antigravity when present. In the current snapshot it is absent at the root. | Generated |
| [`.agents/`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.agents/) | Native Antigravity adapter directory. | Generated |
| [`.agents/rules/`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.agents/rules/) | Native rules, including the adapter's `GEMINI.md` variant. | Generated |
| [`.agents/skills/`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.agents/skills/) | Skills copied into native format, along with a generated manifest. | Generated |
| [`adapters/templates/gemini.md.j2`](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/adapters/templates/gemini.md.j2) | Template that renders rules for Gemini/Antigravity. | Adapter |

The inventory page marks root `GEMINI.md` as absent in the current snapshot, but it does detect `.agents/rules/` and `.agents/skills/` as generated Antigravity output.

## Files and Folders Involved

Skills originate in `.github/skills/` and `.github/skills-external/`. For Antigravity, the sync engine does more than create links: it copies skills into `.agents/skills/` and distinguishes them with a generated manifest. This lets the native environment read them directly without changing where the content is governed.

The `gemini.md.j2` adapter turns shared rules into compatible instructions. `make sync-skills` regenerates this structure, and `make check-sync` validates that the result stays aligned.

## Source of Truth vs Generated

The source of truth is not `.agents/skills/`; it is the governed rules and skills. `.agents/` is an operational projection. If a generated copy is edited, the change may be lost on the next sync and remain invisible to the other tools.

The study rule is simple: read `.agents/` to understand how Antigravity consumes the harness, but edit `.github/` and `adapters/` to change the harness.

## Mini Study Flow

1. Read the [inventory](../reference-implementation/ml-python-base/inventory.md) and compare the status of `GEMINI.md`, `.agents/`, `.agents/rules/`, and `.agents/skills/`.
2. Read [skills](../reference-implementation/ml-python-base/skills.md) and observe the difference between symlinks for other tools and native copies for Antigravity.
3. Review [adapters](../reference-implementation/ml-python-base/adapters.md) to locate `gemini.md.j2`.
4. Finish with [drift control](../reference-implementation/ml-python-base/drift-control.md) to understand how native copies are kept from becoming parallel policies.

## Official Documentation

- [Google Antigravity Documentation](https://antigravity.google/docs/home): main Antigravity documentation.
- [Agent Skills](https://antigravity.google/docs/skills): how Antigravity understands folder-based skills with `SKILL.md`.
- [Getting Started with Google Antigravity](https://codelabs.developers.google.com/getting-started-google-antigravity): official codelab for installation and early concepts.

## References

- [`ml-python-base` on GitHub](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0)
- [Artifact inventory](../reference-implementation/ml-python-base/inventory.md)
- [Governed skills](../reference-implementation/ml-python-base/skills.md)
- [Adapter projection](../reference-implementation/ml-python-base/adapters.md)
