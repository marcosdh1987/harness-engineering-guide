# Leverage More: Native Features You're Not Using Yet

Claude Code is more than `CLAUDE.md` and skills. This page maps the native features worth
knowing — and, honestly, which ones the `ml-python-base` reference actually uses versus
leaves on the table. Learn the tool; then choose deliberately for your own project.

## Native capability vs. how `ml-python-base` applies it

| Native Claude Code capability (docs / Architect cert) | What it does | How `ml-python-base` applies it |
|---|---|---|
| `CLAUDE.md` memory + `@path` imports | Project memory overrides user/global; modular imports keep context lean | Single governed adapter; **does not** use `@path` — directs context via governance prose |
| Conditional rules `.claude/rules/` (YAML + glob `paths:`) | Inject context only when editing files matching a glob | **Not used** — each skill restates its governance compliance instead of glob injection |
| Custom skills `.claude/skills/` | Team-persistent, reusable procedures | Used — but **generated** from `.github/skills/`; never hand-edited |
| `context: fork` | Isolate a high-output task in a subagent | Available via skill frontmatter; not set on the minimal internal skills |
| `allowed-tools` | Restrict a skill's tools for safety | Available; internal skills keep minimal frontmatter, so not set there |
| Plan Mode vs. Direct Execution | Plan mandatory for large structural change; direct for small fixes | Encoded in the working loop `Ground → Plan → Delegate → Verify → Compound` |
| Headless `claude -p` / `--print`, `--output-format json` + `--json-schema` | Non-interactive runs for CI/CD with structured output | CI runs read-only gates (`make check`, `make check-sync`) rather than model calls |
| Clean-session code review | Review in a fresh session to avoid confirmation bias toward Claude's own work | Reviews are run in a separate, clean session |
| `fork_session` / `--resume` | Explore divergent paths; resume; notify Claude when a human edited files | Session hygiene practice |

!!! note "Read this as: capability vs. choice"
    The left columns are what **Claude Code can do** (per the
    [official docs](https://docs.anthropic.com/en/docs/claude-code/overview) and the
    Architect certification). The right column is one **opinionated application** of those
    capabilities. Your project may choose differently — that's fine, as long as it's
    deliberate.

## Where to go deep for each

- **Rules & context injection** → [Concepts › AI Rules Architecture](../concepts/ai-rules-architecture.md), [Patterns › Rule Layering](../patterns/rule-layering.md), [Reference › Rules](../reference-implementation/ml-python-base/rules.md)
- **Governance / skills / automation / orchestration** → [Concepts › Governance, Skills, Automation, Orchestration](../concepts/governance-skills-automation-orchestration.md)
- **Skills mechanics (`fork`, `allowed-tools`, toolbelt)** → [Tools › Claude Code](../tools/claude-code.md)
- **Working loop & plan mode** → [Reference › Working Loop](../reference-implementation/ml-python-base/working-loop.md)
- **CI / drift control** → [Reference › Automation](../reference-implementation/ml-python-base/automation.md), [Reference › Drift Control](../reference-implementation/ml-python-base/drift-control.md)

## Honest gaps

Two native features are intentionally **unused** by the reference template:

- **`.claude/rules/` glob-conditional injection** — the template directs context by
  instruction, not by file-glob rules.
- **`@path` imports in `CLAUDE.md`** — the template keeps a single adapter file.

If your project wants either, that's a valid divergence — just document why, the same way
this guide documents its choices.

## Where to next

- [Learning Path](../learning-path.md) — the full study sequence.
- [Labs](../labs/index.md) — practice creating rules, skills, and validating changes.

## Official documentation

- [Claude Code Overview](https://docs.anthropic.com/en/docs/claude-code/overview)
- [Claude Code Skills](https://docs.anthropic.com/en/docs/claude-code/skills)
- [Claude Code Memory](https://docs.anthropic.com/en/docs/claude-code/memory)
- [Claude Agent SDK Overview](https://code.claude.com/docs/en/agent-sdk/overview)

## References

- [Tools › Claude Code](../tools/claude-code.md)
- [Concepts › AI Rules Architecture](../concepts/ai-rules-architecture.md)
- [Reference Implementation › ml-python-base](../reference-implementation/ml-python-base/index.md)
