# Context Engineering

**Context Engineering** is the disciplined practice of designing, structuring, curating, and selectively injecting information into an AI agent's active context window.

Context quality—not context volume—is the single greatest determinant of AI coding performance. While modern LLMs boast context windows exceeding one million tokens, indiscriminately flooding the model with documentation causes catastrophic degradation in reasoning, precision, and adherence to rules.

Effective context engineering treats the context window as **finite, high-cost working memory**, reserving the vast majority of tokens for the active code, syntax trees, test output, and reasoning traces.

---

## The Danger of Context Flooding

A frequent mistake in AI-assisted software engineering is **context flooding** (also known as context stuffing or prompt bloat): concatenating entire knowledge bases, all project documentation, and extensive histories into every agent prompt.

### Why Context Flooding Fails

1. **Needle-in-a-Haystack Degradation**: As token counts grow, the model's ability to recall and strictly prioritize critical constraints diminishes. Subtle security rules or typing requirements get lost amidst hundreds of lines of background explanations.
2. **Instruction Confusion & Drift**: Stale or conflicting historical documents cause the agent to vacillate between deprecated conventions and current standards, leading to confident but incorrect architectural decisions.
3. **Token Dilution & Latency**: High-volume prompts slow down inference speed, increase operational costs, and exhaust rate limits without improving output quality.
4. **Displacement of Working State**: Filling the prompt with static context leaves insufficient room for dynamic runtime feedback—compiler errors, test outputs, and diff validations.

> **Core Rule**: Never broadcast organizational knowledge indiscriminately. Good context engineering is about **high-signal curation**, not exhaustive ingestion.

---

## The Selective Context Pattern

To provide agents with exactly what they need without flooding their context, modern harnesses employ the **Selective Context Pattern**:

```text
┌──────────────────────────────────────────────┐
│ 1. START_HERE / Router Index                 │
│ Compact map of domains, rules & entry points │
└──────────────────────┬───────────────────────┘
                       │ 1. Identify intent & scope
                       ▼
┌──────────────────────────────────────────────┐
│ 2. Task Routing Hub                          │
│ Domain-specific catalog, skill, or subsystem │
└──────────────────────┬───────────────────────┘
                       │ 2. Select targeted references
                       ▼
┌──────────────────────────────────────────────┐
│ 3. Smallest Useful Read Set                  │
│ 1–3 precise files (ADR, schema, runbook)     │
└──────────────────────────────────────────────┘
```

### 1. START_HERE / Router Index
The root instruction files (`CLAUDE.md`, `AGENTS.md`, or `START_HERE.md`) must never act as an exhaustive manual. Instead, they act as a **lightweight routing table**:
- Global non-negotiables (e.g., "Run `make check` before concluding", "No unchecked `any` types").
- A compact high-level map of repository domains and subsystems.
- Direct pointers to domain-specific documentation hubs or generated indexes.

### 2. Task Routing Hub
When presented with a task (e.g., "Add authentication to the billing webhook"), the agent does not crawl the entire filesystem. It consults the router to determine which domain or capability is relevant:
- If the task is billing-related, route to `docs/domains/billing/` or `billing-rules.md`.
- If the task requires migrating a database, invoke the `db_migration` skill rather than loading all historical schema migrations.

### 3. Smallest Useful Read Set
Once the task scope is identified, the agent reads **only the minimum set of files necessary to fulfill the request**:
- Typically 1 to 3 specific files: the active domain ADR, the target API schema, and the relevant test fixture.
- The remaining 90%+ of the context window remains clean, allowing the agent to perform deep reasoning, analyze diffs, and inspect test runner outputs.

---

## Static Governance vs. Dynamic Context

In a well-engineered harness, context is partitioned into two distinct categories:

| Dimension | Static Governance (Projected) | Dynamic Context (Selective) |
|---|---|---|
| **What it is** | Non-negotiable constraints, linters, types, safety gates | Domain background, historical decisions, API schemas |
| **Where it lives** | `.github/rules/`, tool adapters (`CLAUDE.md`), `Makefile` | Architecture docs, ADRs, runbooks, Company Brain |
| **How it reaches the agent** | Projected automatically into every session | Discovered and read on-demand via task routing |
| **Lifecycle** | Strictly enforced via CI gates (`make check`) | Maintained as canonical reference documentation |
| **Token Cost** | Fixed and minimal (< 1,000 tokens) | Variable; loaded only when active task demands it |

---

## The Compilation Layer in Practice

The Selective Context Pattern connects directly with the **Three-Layer Architecture** described in [From Project to Organization](../start-here/project-to-organization.md#the-three-layer-architecture):

```text
Corporate Systems of Record (Jira, GitHub, Notion)
       │ (evidence / provenance)
       ▼
Company Brain (Governed canon, ADRs, capabilities)
       │
       │  [ Compilation & Selection Layer ]
       ▼
Engineering Harness (START_HERE routing → Smallest Useful Read Set)
       │ (execution & verification)
       ▼
Target Codebase & Verification Gate (make check)
```

The Engineering Harness serves as the **compilation layer**: it translates the vast, governed organizational knowledge of the Company Brain into compact, actionable, and selectively retrieved working contexts.

---

## Context Engineering Rules of Thumb

1. **Keep documentation close to code**: Colocate architecture decision records, domain definitions, and API contracts alongside the modules they describe.
2. **Use structured frontmatter and generated indexes**: Maintain machine-readable metadata (`type`, `status`, `domain`) and generate compact index catalogs (`make index`) so agents can search without broad directory scans.
3. **Prefer runnable examples over verbose prose**: One clean, passing unit test teaches an agent more about expected behavior than five pages of narrative description.
4. **Prune and archive aggressively**: Outdated documentation is worse than no documentation. Move superseded patterns to an archive or delete them.
5. **Measure context attribution**: Regularly audit what documentation and skills agents actually read during evaluation runs (see [Evaluation Workflow](../reference-implementation/ai-agentic-harness-lab/evaluation-workflow.md)) to detect unused or noisy context files.

---

## Related Resources

- **[What is Harness Engineering?](../start-here/what-is-harness-engineering.md)**
- **[From Project to Organization](../start-here/project-to-organization.md)**
- **[The Company Brain Template](../start-here/company-brain-template.md)**
- **[AI Rules Architecture](ai-rules-architecture.md)**
- **[Skills vs Prompts](skills-vs-prompts.md)**
