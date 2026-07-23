# Getting Started with Claude Code

This is the on-ramp. You do **not** need to read all of
[`ml-python-base`](https://github.com/marcosdh1987/ml-python-base) to be productive with
Claude Code. This section takes you from "chat and a copied `CLAUDE.md`" to confidently
using and creating skills — grounded in the official Anthropic docs and the Architect
certification concepts, and honest about what Claude Code does *natively* versus what the
`ml-python-base` reference actually does.

## Who this is for

Engineers who today are in one of these spots:

- using Claude in raw chat, re-explaining the project every session;
- copying a large `CLAUDE.md` from somewhere without understanding it;
- not using skills, plan mode, or other features — doing by hand what Claude could own.

## Three anti-patterns this section fixes

| Anti-pattern | Why it hurts | Where we fix it |
|---|---|---|
| Chat only — nothing persists | No durable context; you re-explain the project every time | [Basics](claude-code-basics.md) + [Minimal Setup](minimal-setup.md) |
| Copying a huge `CLAUDE.md` you don't understand | Fragile, un-owned, drifts, hard to trust | [Minimal Setup](minimal-setup.md) — small and understood |
| Ignoring skills / native features | Repeating manual work Claude could automate | [Use & Modify Skills](use-and-modify-skills.md) → [Leverage More](leverage-more.md) |

## The path

Read these in order — each is short and builds on the last:

1. **[Claude Code Basics](claude-code-basics.md)** — the mental model: durable context, what Claude reads, plan vs. direct execution, sessions.
2. **[Minimal Setup](minimal-setup.md)** — copy a small `CLAUDE.md` and a `SKILL.md` you can defend line by line.
3. **[Use and Modify Skills](use-and-modify-skills.md)** — run existing skills and change them safely.
4. **[Create Your First Skill](create-your-first-skill.md)** — a new skill in three steps.
5. **[Leverage More Features](leverage-more.md)** — the native features you're probably not using yet, and which ones this template actually uses.

## Using Codex or OpenCode?

The harness is tool-agnostic: the governance docs and skills are shared, and only the
adapter file each tool reads differs. Follow the same path above, then apply the short
per-tool delta:

- **[Getting Started with Codex](codex.md)** — adapter `AGENTS.md`.
- **[Getting Started with OpenCode](opencode.md)** — adapter `OPENCODE.md`.

## How this maps to `ml-python-base`

Each idea below is first explained as a general Claude Code capability, then grounded in
what the reference repo does. Where the two differ, we say so — so you learn the tool
*and* one real, opinionated way to apply it. When you want the full depth, the
[Reference Implementation](../reference-implementation/ml-python-base/index.md) pages and
the [Tools › Claude Code](../tools/claude-code.md) study guide go deeper than this
on-ramp intentionally does.

## Official documentation

- [Claude Code Overview](https://docs.anthropic.com/en/docs/claude-code/overview)
- [Claude Code Skills](https://docs.anthropic.com/en/docs/claude-code/skills)
- [Claude Code Memory (`CLAUDE.md`)](https://docs.anthropic.com/en/docs/claude-code/memory)
- [Claude Agent SDK Overview](https://code.claude.com/docs/en/agent-sdk/overview)

## References

- [Learning Path](../learning-path.md) — the full study sequence once you've onboarded.
- [Tools › Claude Code](../tools/claude-code.md) — how the reference repo wires Claude Code.
- [Reference Implementation › ml-python-base](../reference-implementation/ml-python-base/index.md)
