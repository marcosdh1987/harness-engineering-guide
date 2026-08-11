# The Company Brain Template

The [From Project to Organization](project-to-organization.md) page introduces
the Company Brain as a concept. This page documents its **concrete
implementation**: the
[`company-brain-template`](https://github.com/marcosdh1987/company-brain-template)
repository (v1.0) — a materialized starting point for the organizational
context layer, consolidated from real client engagements.

!!! tip "When to reach for this template"
    Not on day one. A single-repo engagement keeps its context *inside* the
    repo (`memory/`, `docs/adr/`, domain docs) — that in-repo **project
    brain** is enough. This template earns its place when the engagement
    spans more than one repo, more than one project, or a consulting
    relationship where evidence and decisions must outlive any codebase. The
    full progression is in [Adopting an Existing Project](adopt-existing-project.md).

## The core idea: an evidence → knowledge pipeline

The brain is organized as a promotion pipeline. Raw material is **evidence,
not facts**; only cited, statused content becomes canonical knowledge:

```text
raw material              promotion                canonical knowledge
99-inbox/            →    analyze, extract,    →   06-decisions/   05-requirements/
01-meetings/              validate, cite           00-context/     03-projects/ …
09-references/
```

Every non-obvious statement carries one of five statuses — `CONFIRMED`,
`PENDING VALIDATION`, `INFERRED`, `SUPERSEDED`, `BLOCKED` — and a source.
Sources get IDs (`SRC-XXX`) in a **source register** that also records
conflicts between sources and the precedence rule adopted, without ever
editing the original evidence. Decisions are immutable `DEC-XXX` entries.
The single source of operating rules is `AGENTS.md`; every tool adapter
(`CLAUDE.md`, Copilot) defers to it, so two rule sets can never drift apart.

## Structure (modular)

Modules are activated per engagement in `brain.config.json`; the validator
enforces only active ones. `make init ORG="…" PROFILE=…` preselects them
(profiles: `consulting`, `delivery-oversight`, `development`, `full`).

| Module | Core | Contents |
|---|---|---|
| `00-context/` | ✔ | company overview, engagement scope, stakeholders, glossary |
| `01-meetings/` | ✔ | transcripts (evidence) + reviewed minutes + intake template |
| `02-organization/` | | ways of working, conventions (engineering, git, **ticketing**, communication), AI policy, ownership, org runbooks |
| `03-projects/` | | one folder per project: overview → current state → target state → plan → checklist → change log |
| `04-architecture/` | | systems map, `repos.yaml` (code repo registry), integrations |
| `05-requirements/` | | functional, non-functional, business rules, open questions |
| `06-decisions/` | ✔ | immutable `DEC-XXX` decision log |
| `07-delivery/` | | status, roadmap, action items, validation matrix, periodic client-run check |
| `08-vendors/` | | vendor register + evaluations |
| `09-references/` | ✔ | primary sources + source registers with conflict tracking |
| `99-inbox/` | ✔ | landing zone; files leave marked `processed--` |

`02-organization/` is where the organization's ways of working live as
**declarations** — the engineering harness *enforces* them in each repo; the
brain *declares* them once. This includes `conventions/ticketing.md`: generic
skills ("plan from ticket") read it to adapt to the organization's tracker,
workflow states, and definitions of ready/done.

## The workspace model: brain + code repos

When the organization has code repositories, the layout is **hub-and-spoke
with sibling clones — never submodules, never nested**:

```text
~/work/acme/
├── acme-brain/          ← the hub
├── api-payments/        ← spoke: its CLAUDE.md imports @../acme-brain/…
└── web-portal/          ← spoke
```

A developer's day 1 is `git clone <brain> && make workspace` — the target
reads `04-architecture/repos.yaml` and clones every registered repo
alongside. Submodules are rejected deliberately: a submodule pins a commit
(stale context by design), adds clone/permission friction, and inverts the
dependency — context must not depend on code. The sibling convention makes
the relative import path predictable on every machine; if the brain is
missing, imports degrade gracefully, and CI checks the brain out as a second
repo instead. Full rationale: the template's `docs/workspace.md`.

## Lifecycle

Governed skills cover the whole lifecycle: `bootstrap_company_brain`
(fresh-start or **migration mode** for organizations with existing history:
everything into the inbox → source register with conflicts → gradual
promotion), `process_meeting` (transcript → minutes → promoted knowledge),
`update_domain_context`, `record_decision`, `add_runbook`, and
`quarterly_context_review` (the anti-drift audit). Validation is automated
and semantic: `make validate` checks structure per config, links, duplicate
IDs, decisions without sources, and reports placeholder/inbox debt.

## Relationship to the rest of the ecosystem

The guide explains the concepts; `ml-python-base` provides the execution
layer and distributes the brain lifecycle skills; the lab can measure which
brain sections agents actually consult. The template (structure + skills) is
a reusable engineering asset; each instantiated brain belongs to the
organization it describes.
