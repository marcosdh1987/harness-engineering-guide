# The Company Brain Template

The [From Project to Organization](project-to-organization.md) page introduces the
Company Brain as a concept: the governed organizational context that can be shared
across projects, teams, and AI agents. This page documents its **concrete
implementation**: the
[`company-brain-template`](https://github.com/marcosdh1987/company-brain-template)
repository — a materialized starting point for that organizational context layer.

!!! tip "When to reach for this template"
    Not on day one. A single-repo engagement keeps its context *inside* the repo
    (`memory/`, `docs/adr/`, domain docs) — that in-repo **project brain** is
    enough. This template earns its place when a **second repository starts
    duplicating the first one's context**. The full progression is in
    [Adopting an Existing Project](adopt-existing-project.md).

## What it is

`company-brain-template` is a documentation-only repository template that
instantiates a **company brain** for one organization: the canonical, agent-readable
source of truth for its domain, decisions, vocabulary, conventions, systems map,
and operational runbooks. It contains no product code. Everything is versioned
Markdown, owned by the organization that instantiates it.

It deliberately completes the two-layer model this guide describes:

```text
Shared engineering harness (ml-python-base releases)   → how work is done (execution)
        +
Company brain (one instance per organization)          → what the organization knows (context)
        =
Effective context of every repository (adapters import both)
```

The engineering harness is reusable across organizations and updated through semver
releases. The brain is unique per organization and evolves with its business. Code
repositories import both layers from their adapters (`CLAUDE.md`, `AGENTS.md`).

## Structure

| Section | Contents |
|---|---|
| `brain/00-index.md` | Entry point: maps tasks to the sections worth loading (selective injection) |
| `brain/ai-policy.md` | The organization's AI posture — approved tools, data rules, agent permissions |
| `brain/domain/` | Business overview, entities, numbered business rules (BR-NNN), stakeholders |
| `brain/glossary.md` | Canonical vocabulary of the business |
| `brain/decisions/` | Organization-level ADRs (single-repo ADRs stay in that repo) |
| `brain/conventions/` | Engineering, git and communication conventions that apply to all repos |
| `brain/architecture/` | Systems map and external integrations inventory |
| `brain/runbooks/` | Step-by-step operational procedures, executable by a newcomer or an agent |
| `brain/team/ownership.md` | Every shared section has an explicit human owner |
| `memory/` | Organization-level learnings and patterns |

## Lifecycle

The template ships with governed skills (same format as the reference
implementation's skills) covering the full lifecycle:

- **`bootstrap_company_brain`** — instantiates and populates the brain for a new
  organization: mines real sources first (repos, docs, configs), interviews humans
  only for what mining cannot answer, and never invents domain facts. Visible
  `_PENDIENTE_` markers beat plausible fiction.
- **`update_domain_context`**, **`record_decision`**, **`add_runbook`** — absorb
  business changes consistently instead of patching one file.
- **`quarterly_context_review`** — the anti-drift mechanism: every ~90 days the
  brain is audited against reality, stale content is flagged, and marker debt is
  reported to section owners. Stale context is worse than missing context.

Validation is automated (`make validate`: structure, links, marker debt) and the
folder structure is treated as a public interface — consumer repositories reference
it from their adapters, so restructuring is a `MAJOR` version change.

## Relationship to the rest of the ecosystem

- The **guide** (this site) explains the concepts and the adoption levels.
- **`ml-python-base`** provides the execution layer and distributes the brain
  lifecycle skills with its releases.
- The **lab** can measure which brain sections agents actually consult, informing
  the quarterly review: sections never read are candidates to merge or delete.

!!! note "Ownership boundary"
    The template (structure + skills) is a reusable engineering asset. Each
    instantiated brain belongs to the organization it describes — including when a
    consultancy operates the bootstrap. This separation is what keeps the motor
    reusable and the client's knowledge theirs.
