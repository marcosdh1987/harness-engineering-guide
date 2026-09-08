# The Company Brain Template

The [From Project to Organization](project-to-organization.md) page introduces
the Company Brain as a concept. This page documents its **concrete
implementation**: the
[`company-brain-template`](https://github.com/marcosdh1987/company-brain-template)
repository, a materialized starting point for the organizational
context layer, consolidated from real-world operations and client engagements.

!!! tip "When to reach for this template"
    Not on day one. A single-repo engagement keeps its context *inside* the
    repo (`memory/`, `docs/adr/`, domain docs), that in-repo **project
    brain** is enough. This template earns its place when the scope
    spans more than one repo, more than one project, or an operational
    relationship where evidence and decisions must outlive any individual codebase. The
    full progression is in [Adopting an Existing Project](adopt-existing-project.md).

## The core idea: an evidence → knowledge pipeline

The brain is organized as a promotion pipeline. Raw material is **evidence,
not facts**; only cited, statused content becomes canonical knowledge:

```text
raw material              promotion                canonical knowledge
99-inbox/            →    analyze, extract,    →   06-decisions/   05-requirements/
01-meetings/              validate, cite           00-context/     03-work/ …
09-references/
```

Every non-obvious statement carries one of five statuses, `CONFIRMED`,
`PENDING VALIDATION`, `INFERRED`, `SUPERSEDED`, `BLOCKED`, and a source.
Sources get IDs (`SRC-XXX`) in a **source register** that also records
conflicts between sources and the precedence rule adopted, without ever
editing the original evidence. Decisions are immutable `DEC-XXX` entries.
The single source of operating rules is `AGENTS.md`; every tool adapter
(`CLAUDE.md`, Copilot) defers to it, so two rule sets can never drift apart.

## Two Archetypes: Engagement Brain vs. Operating Company Brain

A critical architectural insight from practice is that organizations operate two distinct archetypes of Company Brains depending on their operational horizon:

```text
┌──────────────────────────────────────┐     ┌──────────────────────────────────────┐
│          Engagement Brain            │     │       Operating Company Brain        │
├──────────────────────────────────────┤     ├──────────────────────────────────────┤
│ • Client-facing / consulting mission │     │ • Internal function or org (e.g. XL) │
│ • Time-bound lifecycle (weeks/months)│     │ • Continuous, evolving operations    │
│ • Heavy external meeting transcripts │     │ • Work-unit taxonomy (03-work/)      │
│ • Focus: Discovery & Client Handoff  │     │ • Focus: Execution & Capability Lib  │
└──────────────────────────────────────┘     └──────────────────────────────────────┘
```

| Dimension | Engagement Brain | Operating Company Brain |
|---|---|---|
| **Primary Scope** | Specific client, audit, or consulting engagement | Department, engineering organization, or entire company |
| **Lifecycle** | Time-bound (typically weeks to months) | Continuous and permanent |
| **Core Work Unit** | Engagement milestones, client deliverables, review gates | Structured initiatives, discovery spikes, capabilities (`03-work/`) |
| **Evidence Profile** | External client transcripts, uploaded artifacts, inbox intake | Systems of record (Jira, GitHub, Slack), internal retrospectives |
| **Primary Stakeholders** | External client sponsors, consulting lead | Engineering managers, tech leads, internal autonomous agents |
| **Key Output** | Recommendations, client reports, architectural handoff | Operational execution, company-wide ADRs, capability libraries |

Recognizing which archetype you are building prevents structural mismatch: an engagement brain focuses heavily on evidence audit trails and client deliverables, while an operating company brain focuses on work taxonomies, internal capabilities, and role hubs.

## Structure (modular)

Modules are activated per deployment in `brain.config.json`; the validator
enforces only active ones. `make init ORG="…" PROFILE=…` preselects them
(profiles: `consulting`, `delivery-oversight`, `management`, `development`, `full`).

| Module | Core | Contents |
|---|---|---|
| `00-context/` | ✔ | company overview, operating scope, stakeholders, glossary |
| `01-meetings/` | ✔ | transcripts (evidence) + reviewed minutes + intake template |
| `02-organization/` | | ways of working, conventions (engineering, git, **ticketing**, communication), AI policy, ownership, org runbooks |
| `03-work/` | | structured work units: initiatives, discovery, capabilities, operational cadences (overview → status → plan → execution log) |
| `04-architecture/` | | systems map, `repos.yaml` (code repo registry), integrations |
| `05-requirements/` | | functional, non-functional, business rules, open questions |
| `06-decisions/` | ✔ | immutable `DEC-XXX` decision log |
| `07-delivery/` | | status, roadmap, action items, validation matrix, periodic health checks |
| `08-vendors/` | | vendor register + evaluations |
| `09-references/` | ✔ | primary sources + source registers with conflict tracking |
| `99-inbox/` | ✔ | landing zone; files leave marked `processed--` |

`02-organization/` is where the organization's ways of working live as
**declarations**: the engineering harness *enforces* them in each repo; the
brain *declares* them once. This includes `conventions/ticketing.md`: generic
skills ("plan from ticket") read it to adapt to the organization's tracker,
workflow states, and definitions of ready/done.

---

## Lessons from Operating a Real Management Brain

The evolution of the Company Brain from early consulting templates into production operating systems (such as executive engineering brains like `em-xl`) generated essential lessons learned:

### 1. The Transition from `03-projects/` to `03-work/`
Early brain architectures modeled organizational activity strictly as "projects" (`03-projects/`). In real management operations, this proved too rigid:
- Much of organizational work consists of recurring operational rhythms, cross-cutting discovery spikes, infrastructure maintenance, or internal capability building, none of which are traditional software projects.
- `03-work/` unifies all operational activity under a cohesive **work-unit taxonomy**.

### 2. Stage vs. Folder (Decoupling Status from File Paths)
A major anti-pattern is moving files between directories to reflect status changes (e.g., `work/active/` to `work/completed/`).
- Moving files breaks internal markdown hyperlinks, invalidates agent memories, and pollutes Git commit history.
- **Solution**: The folder structure reflects domain or hierarchy, while lifecycle state (`stage`: `draft`, `active`, `review`, `done`, `paused`) is stored in machine-readable YAML frontmatter metadata.

### 3. Tier vs. Type
Work units must be classified along two orthogonal dimensions:
- **Type**: The nature of the work (`initiative`, `discovery`, `capability`, `operations`).
- **Tier**: The organizational blast radius and operational impact (`Tier 1`: strategic/company-wide, `Tier 2`: team/departmental, `Tier 3`: local/operational).

### 4. Graduated Rigor
Not every task warrants the same administrative overhead:
- Imposing heavy evidence registers and formal decision gates on a trivial operational script causes friction and abandonment.
- Under **graduated rigor**, Tier 1 initiatives require formal problem statements, explicit source registers, stakeholder sign-offs, and immutable `DEC-XXX` entries; Tier 3 tasks require only a concise plan and verification checklist.

### 5. Capability Library
Operating an organization requires durable capabilities (e.g., standard evaluation rubrics, onboarding playbooks, incident post-mortem frameworks) that outlive individual projects or quarters. Separating reusable capabilities into a distinct library prevents organizational memory from being buried inside completed project archives.

### 6. Generated Indexes to Prevent Context Flooding
Agents should never perform recursive filesystem traversals across hundreds of files in `03-work/`. Instead, lightweight automation (`make index`) parses the YAML frontmatter of all work units to generate compact catalog tables (such as `work-index.md`). This enables agents to follow the [Selective Context Pattern](../concepts/context-engineering.md#the-selective-context-pattern) without exceeding token budgets.

### 7. Role-Oriented Hubs
Large organizations contain diverse participants: executive leadership, engineering managers, tech leads, and autonomous agents. Providing role-oriented hub files (e.g., `hub-leadership.md`, `hub-engineering.md`) provides high-signal entry points curated for the specific decisions and oversight needs of that persona.

---

## The workspace model: brain + code repos

When the organization has code repositories, the layout is **hub-and-spoke
with sibling clones, never submodules, never nested**:

```text
~/work/acme/
├── acme-brain/          ← the hub
├── api-payments/        ← spoke: its CLAUDE.md imports @../acme-brain/…
└── web-portal/          ← spoke
```

A developer's day 1 is `git clone <brain> && make workspace`, the target
reads `04-architecture/repos.yaml` and clones every registered repo
alongside. Submodules are rejected deliberately: a submodule pins a commit
(stale context by design), adds clone/permission friction, and inverts the
dependency, context must not depend on code. The sibling convention makes
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
IDs, decisions without sources, and reports placeholder/inbox debt. The brain also **syncs working skills** (brainstorming, planning, research, writing) from the harness (declared in `brain.config.json`, locked per sha256) and projects every skill into `.claude/`, `.codex/`, and `.agents/` layouts so Claude Code, Codex, and Antigravity discover them natively (`make sync-skills`).

## Relationship to the rest of the ecosystem

The guide explains the concepts; `ml-python-base` provides the execution
layer and distributes the brain lifecycle skills; the lab can measure which
brain sections agents actually consult. The template (structure + skills) is
a reusable engineering asset; each instantiated brain belongs to the
organization it describes.
