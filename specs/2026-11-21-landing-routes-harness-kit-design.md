# Design: route map landing, route pages, and the complete harness kit

- **Date:** 2026-11-21
- **Status:** Approved, 2026-11-21
- **Repository:** `harness-engineering-guide` (MkDocs Material, bilingual EN/ES)

## 1. Intent

Make the guide inviting for developers and for people who are not developers, so they
use the guide, the Harness Lab, and the templates to improve AI-assisted software and
knowledge work.

Today a newcomer meets six competing entry pages (Home, Overview, Choose your path,
Start here, Learning path, Agentic SDLC for teams), research jargon on intro pages
(Mode A/B/C, ADR numbers, condition hash), and a "minimal setup" that assumes the
`ml-python-base` adapter. Nothing gives a first concrete result.

The Harness Lab web UI already solved this for its own audience: "What do you want to
try today?", four doors, a four-step loop, "a first journey by what you have, 15 to 45
minutes each", "start in 30 seconds", and an honest "what the lab will and will not tell
you". Its guided flows draw a diagram that lights up step by step. The guide should
borrow that pattern.

Two learnings from real projects must also reach the guide:

1. **Few skills beat many.** Both reference projects converged on a small skill set
   plus a routing table by task size.
2. **Most of the value is not in skills.** Project memory, decision records (ADRs),
   plans, thin commands, hooks, and quality gates carry much of the day-to-day value.

## 2. Goals, non-goals, anti-goals

**Goals**

- A landing page per language that shows the ecosystem as an interactive map of boxes,
  where the reader picks a route and the boxes light up in order (approved prototype C).
- Four route pages, one per audience, each a short guided journey.
- A new section, "The complete harness" (ES: "El harness completo"), with one practical
  page per non-skill practice plus a copyable starter kit.
- Present real-project learnings as reference implementation evidence, with sample
  sizes, and with no private data.
- Reduce entry-page sprawl and fix inconsistencies that cost trust.

**Non-goals**

- No changes to other repositories (`ml-python-base`, the lab, `company-brain-template`,
  `ai-gateway`, `ml-langchain-agent`).
- No dark-mode toggle or theme redesign beyond what the map needs.
- No new languages.
- Not covered in this round: requirements registry with tests, closing tickets from the
  agent, model tiers per task (planner, executor, fast).

**Anti-goals** (failure even if it technically works)

- A landing that only works with JavaScript, or that search cannot index.
- More ceremony: pages that make a small change feel like it needs an ADR and a plan.
- Overclaiming: presenting small-sample lab results as general laws.
- Any private data from the anonymized production project (see section 7).
- Broken inbound links to pages that move or disappear.

## 3. Constraints

- Editorial prose policy in `CLAUDE.md` and `docs/en/contributing/writing-style.md`: no
  `--`, em dashes, or en dashes as punctuation in prose. This also applies to text
  inside raw HTML and the JSON data blocks, because `make check-style` scans `docs/`.
- Bilingual parity: every EN page has a semantically aligned ES page; nav mirrored in
  `mkdocs.yml`. ES uses Spanish slugs where the existing ES tree already does (for
  example `es/medir-y-mejorar/`).
- Assertion rigor: distinguish Industry Evidence (with a primary source), Guide
  Recommendation, and Reference Implementation facts.
- `make check` must pass (lint, prose style, reference drift, tests, `mkdocs build
  --strict`).
- Material for MkDocs with `navigation.instant` disabled (scripts run on normal page
  load). Existing extensions: `admonition`, `attr_list`, `md_in_html`,
  `pymdownx.superfences` (Mermaid), `pymdownx.details`, `pymdownx.arithmatex`.
- **Mirrors (done 2026-11-21, user decision).** The guide keeps pointing at the
  maintainer's own repositories, which now mirror the organization's:
  - `marcosdh1987/ml-python-base` main = `xmartlabs/sdlc-ml-python-template` main at
    `1d9d30f` (v2.2.0), tags v1.1.0 to v2.2.0 added, v1.0.0 moved to upstream's (old
    one kept as `archive/pre-mirror/v1.0.0`).
  - `marcosdh1987/ai-agentic-harness-lab` main = `xmartlabs/sdlc-ml-python-harness-lab`
    main at `84a4f65`.
  - Done as a merge commit whose tree is upstream's (old history is the first parent),
    so later syncs are plain merges of upstream main on each upstream release. No
    force push was needed.
- Facts about `ml-python-base` (v2.2.0): it ships the seven `minimal` skills (five
  internal in `.github/skills/`, two external in `.github/skills-external/`) and a
  `.github/harness-levels.toml` where `minimal` is the default of `make init`
  (`LEVEL=minimal|full`), backed by a usage review of three derived repositories
  ("16 of 25 skills were never invoked"). The template calls it a **harness level**;
  the lab calls the same idea a **skill profile**. The guide uses "harness level" when
  talking about the template and explains that the lab's "skill profile" is the same
  idea. The five internal skills are still written for the Python stack (they name
  `make check`, `pytest`, and `.github/` governance files), and per-tool skill folders
  are generated symlinks.
- Repository visibility (checked 2026-11-21): **public**: this guide,
  `marcosdh1987/ml-python-base`, `marcosdh1987/company-brain-template`,
  `marcosdh1987/ai-agentic-harness-lab` (the lab mirror, made public on 2026-11-21
  after a secret scan of its history), `xmartlabs/sdlc-ml-python-harness-lab`,
  `xmartlabs/sdlc-ml-python-template`. **Private**: `marcosdh1987/ai-gateway`,
  `marcosdh1987/ml-langchain-agent`. The user plans to
  publish `ai-gateway` and `ml-langchain-agent`; keep them referenced and linked, with
  a visible "not public yet" note, because they are where observability will live.
- `make harness-check` lives in the Harness Lab. It needs a clone of the lab plus
  `git`, `uv`, and `make`; it needs no Docker, no model, and no network once installed.
  The "30 seconds" is the run time of the check after that setup, and the guide must
  say so. Every "clone the lab" instruction points at
  `marcosdh1987/ai-agentic-harness-lab`; the lab reference page explains that it
  mirrors `xmartlabs/sdlc-ml-python-harness-lab`, where development happens.

## 4. Approaches considered

Decision to make: how to build the interactive map inside MkDocs.

| Approach | Trade-off | Outcome |
| --- | --- | --- |
| A. Custom component: HTML container, per-language JSON data in the page, small `route-map.js` drawing an SVG, plus `extra.css`. Markdown fallback with the same routes. | Matches the approved prototype (light-up boxes, click for detail). About 200 lines of JS to maintain. Works without JS through the fallback. | **Chosen** by the user. |
| B. One Mermaid diagram per route inside content tabs, highlighted with `classDef`. | No custom JS, but no click-for-detail, limited styling, and 8 diagrams (4 routes x 2 languages) to keep in sync by hand. | Rejected. |
| C. Static SVG with CSS-only tabs (radio inputs), details in `<details>`. | No JS, but brittle CSS and the weakest experience. | Rejected. |

Landing layout options shown in the browser: A (doors by intent, like the lab), B (tabs
by role), C (ecosystem map with routes). The user picked **C**.

## 5. Decided design

### 5.1 Landing page (`docs/en/index.md`, `docs/es/index.md`)

Top to bottom:

1. Short heading and one-line lede: what Harness Engineering helps you do, in plain
   words. Question above the routes: "Where do I start?" (ES: "¿Por dónde empiezo?").
2. **Route selector**: four buttons, each with a label and an audience line.
3. **Map**: six boxes and arrows, as in the approved prototype.
4. **Side panel** (stacks under the map on narrow screens): the selected route's
   numbered steps with time tags and a link to the route page; below it, the detail of
   the clicked box ("what it is", "who it is for", "first step", with a link).
5. **Below the map**, two boxes: the working loop as a strip, using the guide's
   existing common loop verbatim ("Understand, Plan or Design when needed, Execute,
   Test, Verify, Review, Learn"; the ceremony follows the risk) so it matches
   `patterns/working-loop.md` (builder call: the five-step wording in the prototype was
   a sketch, not a new canonical loop), and "What this
   guide will and will not tell you" (a stable method, not the tool of the month; it
   separates industry evidence, guide recommendation, and repository facts; it measures
   systems and workflows, never people).

**Boxes (nodes)**

| id | EN label / subtitle | ES label / subtitle | Detail: what, who, first step |
| --- | --- | --- | --- |
| `guide` | Guide / the method | Guía / el método | Working with AI without depending on one tool. Everyone. First step: the working loop (10 min read). |
| `template` | Template / your repo with AI | Template / tu repo con IA | `ml-python-base`: rules, skills, and gates versioned in the repo, projected to Claude Code, Codex, OpenCode, Copilot. Developers and tech leads. First step: the starter kit. Mention `ml-langchain-agent` here for people building agent products. |
| `brain` | Company Brain / shared context | Company Brain / contexto compartido | `company-brain-template`: sources, decisions, provenance, owners, in a place AI can read. Managers, PMs, teams; no code needed to start. First step: pick a question the team keeps asking and record its sources. |
| `work` | Real work / loop + few skills | Trabajo real / ciclo + pocas skills | Day to day: a routing table says when a direct change is enough and when to design first. Whoever does the work. First step: one week using the loop on real tasks. |
| `observatory` | Observatory / what happens day to day | Observatorio / qué pasa en el día a día | Flow, quality, and AI usage signals; measures the process, not content or people. Managers, AI champions. First step: maturity model and the six dimensions. |
| `lab` | Harness Lab / does this really help? | Harness Lab / ¿esto ayuda de verdad? | Compares two configurations on the same case (a skill, a model, a rule) and says what won and with how much confidence. Tech leads, AI champions. First step: read the eight-item health checklist against your repo, or clone the lab and run `make harness-check` (the check runs in about 30 seconds; no Docker, no model). |

Layout (SVG `viewBox="0 0 640 430"`, boxes 170 x 56): `guide` top center; `template`
and `brain` on the second row; `work` center; `observatory` and `lab` on the bottom row.
Solid arrows: guide to template, guide to brain, template to work, brain to work, work
to observatory, work to lab, observatory to lab. Dashed "learning" arrows: lab back to
template ("what wins in the Lab goes back to the template") and lab back to guide ("and
to the guide").

**Routes**

| id | EN label (audience) | ES label (audience) | Steps: node, text, tags |
| --- | --- | --- | --- |
| `dev` | I code with AI (Developers) | Programo con IA (Developers) | 1 guide: understand the loop and why few skills (10 min). 2 template: copy the starter kit into your repo (15 min, terminal). 3 work: use it for a week on real tasks (1 week). 4 lab: check your harness with the eight-item checklist (or `make harness-check` from the lab), then measure the skill you doubt. |
| `lead` | I lead a team (Tech leads and managers) | Lidero un equipo (Tech leads y managers) | 1 guide: why the system matters more than the model (10 min). 2 brain: decisions, sources, and owners in one place (no code). 3 work: a pilot with one repo, one loop, one-page decisions (2 weeks). 4 observatory: measure adoption without measuring people. |
| `docs` | I work with documents, not code (PMs, operations, analysis) | Trabajo con documentos, no código (PMs, operaciones, análisis) | 1 guide: the Knowledge Harness in 5 minutes. 2 brain: one recurring question, its sources, and who maintains them (no terminal). 3 work: use AI with that context and note what failed (no terminal). |
| `champion` | I improve the system (AI champions and Harness Engineers) | Mejoro el sistema (AI champions y Harness Engineers) | 1 observatory: find where it hurts (rework, cost, repeated failures). 2 lab: turn the failure into a case and compare v1 against v2 (45 min). 3 template: promote what won, one skill at a time. 4 guide: share what you learned. |

Default selected route on load: `dev`. Time tags are estimates and must read as such.

### 5.2 Map component

- **Files**: `docs/javascripts/route-map.js`, `docs/stylesheets/extra.css`, registered
  in `mkdocs.yml` (`extra_javascript`, `extra_css`).
- **Data**: each landing page embeds a `<script type="application/json"
  id="route-map-data">` block with nodes (label, subtitle, what, who, first step),
  routes (label, audience, steps with node id, text, tags), and UI strings (panel
  headings, "Tap a box to see what it is"). Translation stays in each language's page.
  Node ids, route ids, and layout coordinates live in the JS, so both languages share
  one geometry.
- **Links**: every href the map shows must be validated by `mkdocs build --strict`.
  The route and box links are written in the Markdown fallback (so MkDocs resolves and
  checks them), tagged with `attr_list` data attributes (for example
  `{ data-route="dev" }`, `{ data-node="lab" }`), and the JS reads hrefs from those
  anchors. No hard-coded URLs in the JSON.
- **Fallback**: the same page contains, in Markdown, the four routes as grid cards with
  their numbered steps and links, plus a short list of the six boxes. When the JS
  renders the map it adds a class that hides the fallback visually. Without JS the
  fallback is the page. Search indexes the fallback text.
- **Theming**: use Material CSS custom properties (`--md-primary-fg-color`,
  `--md-accent-fg-color`, `--md-default-fg-color--light`, `--md-default-bg-color`,
  `--md-code-bg-color`) so it follows the palette, including dark mode if it is ever
  enabled.
- **Accessibility**: route selectors are `<button>` elements with `aria-pressed`;
  boxes are focusable (`tabindex="0"`, `role="button"`, Enter and Space activate) with
  an accessible name; the panel is `aria-live="polite"`; lit and dimmed states do not
  rely on color alone (numbered badges on lit boxes).
- **Responsive**: SVG scales to width; panel stacks under the map below about 860 px;
  no horizontal scroll at 375 px.
- **Robustness**: if the data block is missing or malformed, the JS does nothing and
  the fallback stays visible. No external libraries.

### 5.3 Route pages

Paths: `docs/en/routes/{build-with-ai,lead-a-team,documents-not-code,improve-the-system}.md`
and `docs/es/rutas/{programo-con-ia,lidero-un-equipo,documentos-no-codigo,mejoro-el-sistema}.md`.

Each page follows the approved route-page mockup:

1. Breadcrumb-like line and title.
2. Three facts: **For**, **Time**, **You take away**.
3. "On the map": the route's boxes in order (static, can be a simple inline strip).
4. Steps as a vertical sequence of boxes, each with: title, meta line (box, time),
   two to five lines of what to do, a link to the page that goes deeper. Step content
   may include a small table or code block (the dev route shows the starter kit tree and
   the routing table).
5. A green "You finished the route" box with the next route suggestion.

Implementation: Markdown with admonitions or `md_in_html` blocks styled by
`extra.css`. No JS needed on route pages.

### 5.4 "The complete harness" section

Paths: `docs/en/harness-kit/` and `docs/es/harness-completo/`.

| EN page | ES page | Content |
| --- | --- | --- |
| `index.md` Overview and starter kit | `index.md` | Why most value is not in skills; the starter kit as a copyable tree and files (below); how each piece maps to the loop. |
| `few-skills.md` Start with few skills | `pocas-skills.md` | The seven-skill starter set, when to add a skill (one at a time, measured), and the intention families table moved from `use/skills-by-intention.md` as "when you need more". |
| `project-memory.md` Project memory | `memoria-del-proyecto.md` | Three files, entry format, when to write and when not, gardening and size budget. |
| `decision-records.md` Decision records (ADRs) | `registros-de-decision.md` | One-page template, title as the decision sentence, when to write and skip, supersede instead of edit, index, status hygiene. |
| `plans-and-specs.md` Plans and specs | `planes-y-specs.md` | Approved design, then plan, then execution without reopening the design; where they live; size of each. |
| `commands.md` Commands | `comandos.md` | Thin shortcuts (`/plan`, `/adr`, `/retro`, `/verify`) that point at skills and memory; example files. |
| `hooks.md` Hooks | `hooks.md` | Session start reminder, end-of-turn reminder, ask-before-commit permissions; remind versus block. |
| `quality-gates.md` Quality gates | `gates-de-calidad.md` | One `make check` that can fail, does not rewrite the tree, and that CI runs too; architecture-layer test; docs-with-code check. |
| `health-check.md` Harness health check | `chequeo-de-salud.md` | The eight checks as a checklist anyone can apply by reading their repo (primary path), then the automated version: clone the public Harness Lab and run `make harness-check REPO=../your-repo` (setup: `git`, `uv`, `make`). |

**Page template** for each practice page: what it is (two lines); why it pays off
(evidence box, labeled by evidence level); copyable template; when to use it and when to
skip it; what failed in practice; how to check it is healthy; links to the concept page
and to the reference implementation.

**Starter kit** (tool-agnostic, works in an existing repo, any language):

```text
your-repo/
├── AGENTS.md          short rules + "how big is the task?" routing table
├── CLAUDE.md          one line pointing to AGENTS.md (for Claude Code)
├── memory/            README.md, context.md, learnings.md, patterns.md
├── docs/adr/          README.md (when to write) + 0000-template.md
├── docs/plans/        approved plans
├── <tool>/skills/     the 7 starter skills, in the folder your tool reads
└── make check         or the command that already verifies the project
```

Delivery of the kit (approach A, confirmed by the user on 2026-11-21): everything except the skills is written by the guide, generically, as
copyable code blocks on the kit pages (no separate folder in this repository). The
skills are **not** copied into the guide: the kit links each of the seven to its file
in `ml-python-base`, gives a table of which folder each tool reads skills from (verify
against the existing tool pages and vendor docs), notes that the template's per-tool
folders are symlinks so readers must copy from `.github/skills/` and
`.github/skills-external/`, and lists the few lines to adapt outside a Python stack
(verification command, test runner, governance file paths). For a new Python project
the kit points to `make init NAME=... LEVEL=minimal` in `ml-python-base`.

Routing table to include in `AGENTS.md`:

| If the task is... | Use |
| --- | --- |
| Small and clear | Direct change, then verify |
| Bounded | Quick brainstorm, then plan and execute |
| New or ambiguous | Approved design, then plan, then execution |

Seven starter skills (the template's `minimal` harness level; link each to its file in
`ml-python-base`):
`brainstorm_quick`, `plan_and_execute_feature`, `research_current_info`,
`systematic_debugging`, `verify_changes` (internal, `.github/skills/`), and
`writing-plans`, `requesting-code-review` (external, `.github/skills-external/`).
Explain that each tool reads skills from its own folder and point to the existing tool
pages for where. `ml-python-base` stays the option for starting a new project.

**Content facts to use** (Reference Implementation evidence; state sample sizes):

- Few skills, lab: every run carried 25 skills (about 5,000 characters of descriptions
  in each adapter file); across 18 runs on six models only 3 skills were ever opened.
  A `minimal` profile of 7 skills became the default for new projects. Measured
  comparisons are small (Haiku 4.5, 3 to 6 cases); the lab treats profile contents as
  provisional and requires that removing a skill be earned by evidence, adding one
  trialled skill at a time.
- Few skills, production backend (anonymized): a flat catalog of 27 skills became 9
  entry points; the generated adapter block shrank 19%; routing went from 0 to 30
  evaluation scenarios.
- Memory: three files (`context.md` current state, `learnings.md` non-obvious facts,
  `patterns.md` conventions). Entry format: `## <title>: <YYYY-MM-DD>`, one or two
  sentences of fact, **Why it matters**, **How to apply**. Rules: one fact per entry,
  absolute dates, delete wrong entries, link ADRs. Failure seen: in one reference repo
  `learnings.md` grew past 3,500 lines, too long to skim at session start; another
  memory file cited a CI workflow that no longer existed. Hence a size budget and
  periodic pruning.
- ADRs: template header (Status, Date, Deciders, Related) and four sections (Context,
  Decision "We will...", Consequences, Alternatives considered); "one page is plenty";
  write when hard to reverse or when future contributors (human or agent) would have to
  reverse-engineer it; skip for routine reversible changes (use memory or the commit
  message); a `/adr` command scaffolds from the template, adds the index entry, and asks
  for assumptions. Observed in the production backend: over 100 ADRs in about two months
  (roughly 1,000 commits), many recording behavior decisions rather than only
  architecture, with decision-sentence titles; more than half were still "Proposed"
  after their work had shipped. Recommendation: make accepting the ADR part of merging.
- Design gate: the brainstorming skill blocks code until a design is approved; in
  practice the gate was referenced far more often than design specs were written (7
  specs in the same period). Recommendation: keep the gate for new or ambiguous work
  only, and let the routing table send everything else down the cheap path.
- Commands: `/plan` (ground, pick the ideation skill, phased plan, no code), `/adr`,
  `/retro` (review the diff, append memory entries, suggest `/adr`), `/verify`.
- Hooks: a SessionStart hook prints the loop and points at memory (non-blocking); a
  Stop hook reminds to verify, update docs, and record learnings when code changed
  (non-blocking); commit, push, merge, and branch deletion require confirmation. The
  lab's health check asks for at least one hook that can block, which shows the
  difference between reminding and enforcing.
- Gates: `make check` bundling secret scan, prose check, formatter check, lint,
  security lint, type check, tests with coverage; a test that parses imports and fails
  on layer violations; a CI check that fails when source or tests change without a docs
  change.
- Health check (lab `make harness-check`, deterministic, no model): verification can
  fail; verification does not rewrite the tree; hooks can enforce, not only remind;
  always-loaded instructions stay a map (budget 200 lines or about 2,500 tokens); skills
  are discoverable; MCP servers are pinned; CI runs the same gate the agent runs; the
  harness version is declared.

### 5.5 Navigation and redirects

Target top-level nav per language (ES mirrors with existing ES titles):

1. **Overview** (the map): `en/index.md`
2. **Routes**: the four route pages
3. **The complete harness**: the nine kit pages, then a group "Tool and task guides"
   holding the existing software task guides (Claude Code basics, Codex, OpenCode,
   Minimal setup, Adopt an existing project, Create your first skill, Use and modify
   skills, Onboarding guide, More capabilities)
4. **Understand**: existing concept pages, plus Working loop, Agentic SDLC for teams,
   Knowledge work, Company Brain template, Project to organization
5. **Measure & Improve**: unchanged
6. **Reference**: unchanged, minus items moved above

Add the `mkdocs-redirects` plugin (dependency in `pyproject.toml`, `uv.lock` updated)
and remove these pages, redirecting:

| Removed | Redirect to |
| --- | --- |
| `en/use/choose-your-path.md`, `es/use/elegi-tu-camino.md` | language overview (map) |
| `en/start-here/index.md`, `es/start-here/index.md` | language overview (map) |
| `en/learning-path.md`, `es/learning-path.md` | language overview (map) |
| `en/use/skills-by-intention.md`, `es/use/skills-por-intencion.md` | `few-skills` / `pocas-skills` |

Update every internal link to removed pages (the strict build will list them). The root
`docs/index.md` stays a language chooser.

### 5.6 Cleanup

- **One name for the lab**: "Harness Lab" in prose everywhere. Repository names
  (`sdlc-ml-python-harness-lab`, `ai-agentic-harness-lab`) appear only on the lab
  reference page, where the two implementations are explained.
- **One list of ecosystem pieces** across `README.md`, `CLAUDE.md`, `AGENTS.md`, and
  the landing: Guide, `ml-python-base` (Engineering Harness template),
  `company-brain-template` (Knowledge Harness), Engineering Delivery Observatory
  (`ai-gateway` reference), Harness Lab (evaluation), and `ml-langchain-agent` as the
  product runtime reference.
- **Migration example** in `start-here/agentic-sdlc-for-teams.md` (and anywhere it is
  repeated): label it as an illustrative scenario, not a measured result; remove "will
  never suffer that failure mode again".
- **Jargon off entry pages**: on the landing, route pages, and the lab overview's
  opening, explain in plain words and move ADR numbers, mode letters, and hashes lower
  or to reference pages.
- `.superpowers/` added to `.gitignore`.

- **Lab reference pages caught up to lab main** (`84a4f65`). The guide's lab pages
  describe the lab as of late August. Add, in plain words: guided flows (one question
  per step, a diagram that lights up, a review with cost before anything is created);
  skill profiles and the rule that removing a skill must be earned; `make
  harness-check`; taking a harness home (`make harness-export`, preview first); the six
  one-page journeys; the evaluation modes as the lab's home now phrases them; Codex and
  Gemini harnesses and reasoning effort as run parameters.
- **Private repo links**: `ai-gateway` and `ml-langchain-agent` stay linked with a
  "not public yet" note (see section 3).

## 6. Delivery order

Four deliveries, each passing `make check` and shippable alone:

0. **Reference refresh**: `make sync-reference` against the mirrored `ml-python-base`
   (v2.2.0); adapt `scripts/sync_reference_template.py` if the new layout breaks it
   (since v1.1 internal skills may be folders with `SKILL.md`); regenerated reference
   pages and snapshot; `make check-drift` green.
1. **Map and routes**: component, landing (both languages), four route pages (both
   languages), nav, redirects for entry pages.
2. **The complete harness**: the nine kit pages (both languages); route pages relinked
   to them; skills-by-intention redirect.
3. **Cleanup**: naming, ecosystem list, migration example, jargon, lab pages caught
   up to lab main, private-repo notes, `.gitignore`.

During delivery 1, route steps that will point at kit pages link to the closest
existing page and are relinked in delivery 2, so the strict build stays green.

## 7. Privacy rules (hard)

The production backend used as evidence is private. In anything published:

- Never name the project, the company, the client, the product, ticket prefixes, people,
  or any business domain detail (industry, systems integrated, workflow names).
- Refer to it only as "a production backend (anonymized)".
- "The company" here means the owner of that backend and its clients. Xmartlabs,
  already named publicly as the Harness Lab's origin, is not on the list and stays on
  the lab reference page. Keep the anonymized backend evidence visually and textually
  separate from lab attributions so it is never read as a Xmartlabs project.
- Use aggregated, rounded numbers only (commit counts, ADR counts, skill counts, file
  sizes). No quotes from its ADRs, memory entries, or code.
- Templates shown in the guide are rewritten generically, not copied.

## 8. Verification

- `make check` passes after each delivery.
- `make docs-serve`, both languages: each route lights the right boxes in order; each
  box opens its detail; every link resolves; the fallback appears with JS disabled; no
  horizontal scroll at 375 px; keyboard-only navigation works.
- Spot-check prose style inside the JSON data blocks.
- Grep `docs/`, `README.md`, and `site/` for the forbidden names in section 7. The term
  list is kept outside the repository (never committed) and run by the maintainer
  before each delivery is merged.

## 9. Left to the builder

- Exact copy for every page within the outlines and facts above, in both languages.
- Visual details of the map and route pages within the prototype's look.
- Whether to add a small pytest that checks both landings declare the same node and
  route ids.
- Exact grouping order inside Understand and Reference.
