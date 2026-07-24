# From Project Harness to Organizational Use

Harness Engineering usually begins in a single repository. A developer configures persistent rules, custom skills, and validation gates to make AI tools like Claude Code, Codex, or OpenCode effective locally. However, as organizations adopt AI-assisted development across multiple engineering teams, a critical question emerges: how do these practices scale beyond individual projects without introducing unmanageable drift, conflicting rules, or excessive centralized governance?

This page explains how project-level harnesses evolve into shared engineering assets and fit within broader organizational knowledge governance systems.

> 💡 **Quick access**: [Jump directly to the Company Brain section](#company-brain-as-an-emerging-industry-term)

## Start with one project

The foundation of Harness Engineering is always an individual repository. Within a single codebase, a project harness establishes the durable operating environment for AI assistants. Instead of relying on raw prompts or expecting developers to re-explain architectural decisions during every chat session, a project harness encapsulates:

- **Persistent instructions and architectural boundaries**: Mandatory constraints on code structure, dependencies, and style.
- **Operational skills**: Reusable procedures for running tests, refactoring, or generating documentation.
- **Tool adapters**: Specific instruction entry points (`CLAUDE.md`, `AGENTS.md`, `OPENCODE.md`) that present project guidance to different AI developer tools.
- **Validation commands and test suites**: Local check scripts (`make check`) that verify code correctness before changes are committed.
- **Contextual artifacts**: Architecture Decision Records (ADRs), domain descriptions, runbooks, and local drift controls.

By embedding these capabilities directly in the repository, the agent operates as a disciplined contributor tied to the project's actual history and standards.

## What `ml-python-base` provides

The [`ml-python-base`](../reference-implementation/ml-python-base/index.md) repository serves as a reference implementation of a project-level engineering harness. It demonstrates how to structure, version, and validate agent capabilities in Python projects.

Key shareable elements provided by `ml-python-base` include:

- **Centralized governance and rules**: Tool-agnostic rule definitions maintained under `.github/rules/` (see [Rules](../reference-implementation/ml-python-base/rules.md)).
- **Custom operational skills**: Declarative skill definitions located in `.github/skills/` (see [Skills](../reference-implementation/ml-python-base/skills.md)).
- **Multi-tool adapters**: Automatic generation of adapter files like `CLAUDE.md` and `AGENTS.md` (see [Adapters](../reference-implementation/ml-python-base/adapters.md)).
- **Sync engine and drift control**: Tooling (`scripts/sync_skills.py`, `make check-sync`) that detects when generated adapters or skills drift from canonical sources (see [Drift Control](../reference-implementation/ml-python-base/drift-control.md)).
- **Standardized working loop**: A disciplined `Ground → Plan → Delegate → Verify → Compound` interaction pattern (see [Working Loop](../reference-implementation/ml-python-base/working-loop.md)).

Rather than reinventing these structures for every project, teams can adopt `ml-python-base` as a baseline reference architecture.

## What remains project-specific

While template structures can be shared, every repository possesses unique domain context that cannot—and should not—be standardized globally.

Project-specific elements include:

- **Product vision and business rules**: The explicit business logic and domain entities unique to the application.
- **Concrete architecture and dependencies**: Specific framework choices, database schemas, and external API integrations.
- **Historical context and ADRs**: Decisions explaining why specific trade-offs were made in this particular codebase.
- **Operational runbooks and deployment scripts**: Project-specific CI/CD pipelines, environment configurations, and release steps.
- **Local test suites and exceptions**: Domain unit/integration tests and localized overrides to global guidelines.

!!! warning "Context Isolation"
    > A shared template should not erase project-specific context.

Attempting to replace local domain knowledge with a generic global template deprives AI assistants of the precise context required for local decision-making.

## Sharing the harness across repositories

When an organization manages dozens or hundreds of repositories, copying harness files manually leads to fragmentation. To address this, organizations establish a versioned baseline layer across repos.

We define a **Shared Engineering Harness** as:

> A versioned set of engineering rules, skills, adapters, and validation practices shared across multiple projects.

In this model, repository harnesses are composed dynamically:

```text
Shared engineering harness
        +
Project-local context
        =
Effective project harness
```

Shareable components across repositories typically include:

- **Engineering and security standards**: Common linting rules, security boundaries, and vulnerability policies.
- **Approved operational skills**: Tested procedures for standard tasks like dependency updates or API contract reviews.
- **Quality and validation gates**: Standardized pre-commit checks and CI validation patterns.
- **Documentation templates**: Unified formats for ADRs, pull requests, and technical specifications.

## Scaling to teams and organizations

As harness engineering scales from several repositories to entire business units or enterprise organizations, technical file-sharing via Git is no longer sufficient. Enterprise deployment introduces organizational challenges that require formal governance and infrastructure:

- **Access control and security boundaries**: Role-Based Access Control (RBAC) determining which teams or agents can view sensitive domain knowledge or execute specific tools.
- **Data classification and compliance**: Ensuring proprietary code or customer PII is never inadvertently injected into unapproved external model contexts.
- **Authoritative sources and provenance**: Establishing clear ownership and audit trails for organizational policies and technical standards.
- **Knowledge retrieval and agent registries**: Cataloging enterprise services, APIs, and approved agent tools across teams.
- **Lifecycle management**: Mechanisms for updating, deprecating, and retiring obsolete guidelines or skills enterprise-wide.

To support scaling without monolithic centralization, organizations adopt a federated structure:

```text
Organization
├── Shared governance
├── Shared engineering harness
├── Domain knowledge
├── Team conventions
└── Project-local harnesses
```

## Company Brain as an emerging industry term

As enterprises integrate AI agents across multiple operational domains, new terminology has emerged to describe these multi-project knowledge architectures.

> “Company Brain” is an emerging industry term for applying organizational knowledge management, context engineering, governance, and agent infrastructure across multiple teams and projects.

Rather than a formal technical standard or consolidated academic discipline, it is an emerging industry label used to group pre-existing practices and infrastructure.

Conceptually, the concept relies on mature foundational fields including organizational knowledge management ([ISO 30401:2018](../evidence/research.md#iso-304012018-knowledge-management-systems-requirements)), AI governance ([NIST AI RMF](../evidence/security.md#nist-artificial-intelligence-risk-management-framework-ai-rmf-10)), context engineering, and enterprise software architecture. It should not be treated as a single vendor product, standalone software binary, or monolithic database.

> In this guide, we use “Company Brain” as a convenient label for the governed organizational context that can be shared across projects, teams, and AI agents.

### Relationship to Harness Engineering

It is vital to distinguish between organizational knowledge governance and technical execution:

```text
Company Brain
    describes what the organization knows
    and how that knowledge is governed.

Harness Engineering
    makes selected knowledge executable
    through rules, skills, tools, workflows,
    context, and validation.
```

In this model, **Harness Engineering can act as the compilation layer between organizational knowledge and agent behavior.** The organization governs its policies and domain insights, while harness engineering projects relevant subsets of that knowledge into actionable, validated agent environments.

## What the template does not provide

To maintain conceptual clarity, we must highlight the boundary between project-level templates and enterprise knowledge systems.

> `ml-python-base` can provide the shared engineering-harness layer within a broader organizational knowledge and governance system. It is not, by itself, a Company Brain.

Specifically, `ml-python-base` does **not** provide out of the box:

- Enterprise search engines or organization-wide RAG pipelines.
- Identity and access management (IAM, RBAC, ABAC).
- Automated enterprise data classification or DLP filters.
- Enterprise knowledge graph databases.
- Centralized cross-repository audit logging.
- Corporate regulatory and legal policy engines.
- Enterprise agent registries or MCP server gateways.

Recognizing these boundaries prevents organizations from attempting to force a repository template to solve enterprise-level infrastructure and governance problems.

## An incremental adoption path

Scaling harness engineering should occur progressively. Teams should avoid building complex organizational infrastructure before establishing working project-level harnesses.

```text
Level 1 — Individual project
Use a small, understood harness in one repository.

Level 2 — Reference implementation
Adopt reusable rules, skills, adapters, and validation patterns.

Level 3 — Shared engineering harness
Version and synchronize selected components across repositories.

Level 4 — Team or domain layer
Add shared terminology, workflows, domain rules, and ownership.

Level 5 — Organizational layer
Add access controls, provenance, policy governance, discovery, evaluation, and auditability.
```

### Adoption Principles

1. **Do not skip levels**: Attempting to implement Level 5 governance before establishing Level 1 and Level 2 repository basics leads to bureaucratic overhead without practical engineering utility.
2. **Target real bottlenecks**: Advance levels only when cross-repository drift or governance needs create observable friction.
3. **Preserve ownership**: Every shared rule or domain skill must have an explicit human owner or team maintainer.
4. **Avoid context flooding**: Do not broadcast all organizational knowledge to every agent session. Inject only what is relevant to the active task.

## Key distinctions

To prevent common misunderstandings when scaling harness engineering, keep these core distinctions in mind:

| Concept | Purpose |
|---|---|
| Prompt | Instruction for a specific, transient interaction |
| Project context | Knowledge required to understand a single repository |
| Project harness | Durable rules, skills, tools, workflows, and validation for one project |
| Shared engineering harness | Versioned capabilities and standards shared across multiple projects |
| Organizational knowledge | Enterprise policies, definitions, architecture decisions, and domain insights |
| Company Brain | Emerging industry label for governing and applying organizational knowledge across teams and agents |

### Non-Equivalences

- **Organizational knowledge ≠ agent instructions**: Raw knowledge documents must be curated and structured into actionable instructions before AI agents can execute them effectively.
- **RAG ≠ governance**: Retrieval-Augmented Generation provides data retrieval mechanisms; it does not define or enforce security policies, access controls, or architectural rules.
- **Memory ≠ source of truth**: Agent memory stores session history and transient preferences; it does not replace canonical source code, versioned docs, or database schemas.
- **Shared template ≠ complete project context**: A shared baseline provides standard engineering patterns, but local repository domain context remains essential.
- **Tool-agnostic source ≠ identical runtime behavior**: Centralized markdown rules provide unified guidance, but individual AI tools format and execute those instructions according to their native capabilities.

## References

- [Concepts › Harness Engineering](../concepts/harness-engineering.md)
- [Concepts › Context Engineering](../concepts/context-engineering.md)
- [Concepts › AI Rules Architecture](../concepts/ai-rules-architecture.md)
- [Reference Implementation › ml-python-base Overview](../reference-implementation/ml-python-base/index.md)
- [Reference Implementation › Drift Control](../reference-implementation/ml-python-base/drift-control.md)
- [Reference Implementation › Working Loop](../reference-implementation/ml-python-base/working-loop.md)
- [Evidence › Research Literature (ISO 30401:2018)](../evidence/research.md#iso-304012018-knowledge-management-systems-requirements)
- [Evidence › Security Advisories (NIST AI RMF 1.0)](../evidence/security.md#nist-artificial-intelligence-risk-management-framework-ai-rmf-10)
- [Evidence › Vendor Documentation](../evidence/vendor-docs.md)
