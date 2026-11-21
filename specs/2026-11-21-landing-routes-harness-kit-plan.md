# Route Map Landing, Route Pages and Harness Kit Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the guide's entry into an interactive ecosystem map with four audience routes, add a "complete harness" section that documents the non-skill practices, refresh the reference snapshot, and clean up trust-costing inconsistencies, in English and Spanish.

**Architecture:** Each language's overview page carries a JSON data block plus a Markdown fallback; a dependency-free `route-map.js` draws the SVG map from that data and reads every href from fallback anchors so `mkdocs build --strict` validates all links. Route pages and kit pages are plain Markdown with `md_in_html` blocks styled by one `extra.css`. Pytest guards data parity, nav parity and the kit page template.

**Tech Stack:** MkDocs 1.6.1, Material 9.7.6, `mkdocs-redirects` (new), vanilla JS (no libraries), CSS using Material custom properties, pytest, PyYAML (already installed with MkDocs), headless Google Chrome for rendering checks.

**Spec:** `specs/2026-11-21-landing-routes-harness-kit-design.md` (read it before any task; sections are cited as "spec 5.1" etc.).

## Global Constraints

- Prose: no `--`, no em dash, no en dash as punctuation, including text inside raw HTML and the JSON data blocks (`make check-style` scans all of `docs/`). Arrows `→` are fine.
- Every EN page has a semantically aligned ES page; `mkdocs.yml` nav is mirrored symmetrically. ES copy uses the guide's existing voseo ("Elegí", "Mantené").
- ES slugs: `es/rutas/`, `es/harness-completo/`, and the file names listed in spec 5.3 and 5.4.
- Evidence boxes are admonitions titled exactly: EN `Evidence level: reference implementation` / `Evidence level: industry` / `Evidence level: guide recommendation`; ES `Nivel de evidencia: implementación de referencia` / `Nivel de evidencia: industria` / `Nivel de evidencia: recomendación de la guía`. Reference implementation boxes state the sample size.
- Privacy (spec 7): never name the private production backend, its company, client, product, ticket prefixes, people, or domain; call it "a production backend (anonymized)" / "un backend de producción (anonimizado)"; rounded aggregates only; no quotes from it; keep it separate from Xmartlabs attributions.
- Node ids exactly `guide`, `template`, `brain`, `work`, `observatory`, `lab`. Route ids exactly, in order, `dev`, `lead`, `docs`, `champion`. Default route `dev`.
- No hard-coded URLs in JSON; all hrefs come from fallback anchors carrying `data-route="<id>"` or `data-node="<id>"`.
- No external JS libraries; scripts run on normal page load (`navigation.instant` stays off).
- Time tags read as estimates (EN "about", "~" or a "times are estimates" note; ES equivalent).
- Do not modify any other repository.
- `make check` passes at the end of every task.
- Work on branch `feature/landing-routes-harness-kit`; commit per task; do not push.

## Review Focus

1. JavaScript disabled, or the JSON block malformed: the reader still sees all four routes with steps and links (fallback), never an empty box. Pinned in Task 2 (headless Chrome with scripts disabled) and by the fallback-anchor assertions in `tests/test_route_map.py`.
2. Phone width (375 px): no horizontal scroll; the panel stacks under the map; route buttons wrap. Pinned in Task 2 (375 px screenshot) and Task 10.
3. Keyboard only: route buttons are real buttons, boxes take focus with Tab and open with Enter or Space, the panel announces changes. Pinned in Task 2 (DOM assertions on `tabindex`, `role`, `aria-pressed`, `aria-live`).
4. A route or node whose anchor is missing from the fallback: the map renders the step or detail without a link rather than `href="null"`. Pinned in Task 2 (`hrefFor` returns `null`, render skips the link) and statically by `tests/test_route_map.py`.
5. Search: a reader searching "starter kit" or "Programo con IA" finds the landing and route pages. Pinned in Task 2 and Task 5 (assert the terms appear in `site/search/search_index.json`).

---

### Task 1: Branch, housekeeping and reference refresh (delivery 0)

**Files:**
- Modify: `.gitignore` (add `.superpowers/`)
- Modify: `specs/2026-11-21-landing-routes-harness-kit-design.md` (Status line to `Approved, 2026-11-21`)
- Regenerate (by script): `docs/reference-data/ml-python-base-snapshot.json`, `docs/en/reference-implementation/ml-python-base/*.md`, `docs/es/reference-implementation/ml-python-base/*.md`, evidence pages the script writes
- Possibly modify: `scripts/sync_reference_template.py` (only if the run fails)

**Interfaces:**
- Consumes: local clone at `REF_REPO_PATH` (from `.env`), already fast-forwarded to `ml-python-base` v2.2.0 (`68ed781`).
- Produces: a snapshot whose `commit_sha` is the v2.2.0 mirror commit; later tasks cite the template's `minimal` harness level from it.

- [ ] **Step 1:** `git switch -c feature/landing-routes-harness-kit` from `main`.
- [ ] **Step 2:** Confirm the reference clone: `git -C "$(grep REF_REPO_PATH .env | cut -d= -f2)" log -1 --oneline` prints `68ed781 chore: mirror xmartlabs/sdlc-ml-python-template main (1d9d30f, v2.2.0)`.
- [ ] **Step 3:** Add `.superpowers/` to `.gitignore`; set the spec Status line.
- [ ] **Step 4:** Run `make sync-reference`. Expected: exits 0 and rewrites the snapshot and reference pages.
- [ ] **Step 5:** Review `git diff --stat` and read the regenerated `docs/en/reference-implementation/ml-python-base/skills.md` and `index.md`: skill count and names match `ls .github/skills .github/skills-external` in the clone; nothing claims the template lacks harness levels. If the script crashed, fix the scan in `scan_repository(repo_path)` and add a pytest for the fix in `tests/test_sync_reference_template.py` before re-running.
- [ ] **Step 6:** Run `make check-drift`. Expected: no drift reported, exit 0.
- [ ] **Step 7:** Run `make check`. Expected: all gates pass.
- [ ] **Step 8:** Commit spec, plan, `.gitignore` and regenerated files: `git commit -m "docs: refresh ml-python-base reference to v2.2.0 and add route map spec and plan"`.

---

### Task 2: Route map component and landing pages (delivery 1)

**Files:**
- Create: `tests/test_route_map.py`
- Create: `docs/javascripts/route-map.js`
- Create: `docs/stylesheets/extra.css`
- Modify: `docs/en/index.md`, `docs/es/index.md` (full rewrite)
- Modify: `mkdocs.yml` (`extra_css: [stylesheets/extra.css]`; append `javascripts/route-map.js` to `extra_javascript`)

**Interfaces:**
- Produces, data block (one per landing), inside `<script type="application/json" id="route-map-data">`:
  ```json
  {
    "ui": {"question": "", "routeFor": "", "openRoute": "", "tapHint": "", "what": "", "who": "", "first": "", "learnTemplate": "", "learnGuide": "", "signals": "", "mapLabel": ""},
    "nodes": {"guide": {"label": "", "sub": "", "what": "", "who": "", "first": ""}, "...": {}},
    "routes": [{"id": "dev", "label": "", "audience": "", "steps": [{"node": "guide", "text": "", "tags": [{"text": "10 min", "easy": true}]}]}]
  }
  ```
  Copy for every field comes from spec 5.1 tables (EN and ES columns).
- Produces, fallback markup: `<div class="route-map-fallback" markdown>` containing four Material grid cards (one per route, numbered steps in text, a link `[...](...){ data-route="<id>" }` to the route page) and a list of the six boxes, each a link `[...](...){ data-node="<id>" }` to that box's first-step page.
- Produces, mount point: `<div id="route-map" class="route-map"></div>` placed above the fallback.
- Produces, CSS classes later tasks reuse: `.hk-facts`, `.hk-onmap`, `.hk-steps`, `.hk-step`, `.hk-meta`, `.hk-tag`, `.hk-tag.is-easy`, `.hk-loop`, `.hk-honest`.
- Produces, JS (IIFE, no globals): `readData(): object|null`, `hrefFor(kind: "route"|"node", id: string): string|null`, `buildMap(root: HTMLElement, data: object): void`, `render(state: {route: string, node: string|null}): void`, `init(): void` run on `DOMContentLoaded` or immediately if the document is already loaded. Geometry lives in a JS constant `LAYOUT` (viewBox `0 0 640 430`, boxes 170 x 56, positions and edges from spec 5.1). Success adds class `route-map-ready` to the mount's parent, and CSS hides `.route-map-ready .route-map-fallback`.

**Node link targets in the fallback during this task** (final targets in Task 7): `guide` → `patterns/working-loop.md`; `template` → `start-here/minimal-setup.md`; `brain` → `start-here/company-brain-template.md`; `work` → `patterns/working-loop.md`; `observatory` → `measure-and-improve/engineering-delivery-observatory.md` (ES `medir-y-mejorar/...`); `lab` → `reference-implementation/ai-agentic-harness-lab/index.md`. Route anchors must point at real files (no `#` placeholders, the strict build would not check them), so this task creates the four route pages per language as one-line stubs (`# <title>`) that Task 3 fills.
- Produces, SVG markup the render checks rely on: each box is a `<g class="rm-node" data-node="<id>" tabindex="0" role="button" aria-label="<label>: <sub>">`; lit boxes add `is-lit`, dimmed add `is-dim`; route buttons carry `class="rm-route"` and `aria-pressed`; the panel is `<div class="rm-panel" aria-live="polite">`.

- [ ] **Step 1: Write the failing test** `tests/test_route_map.py`:

```python
NODE_IDS = {"guide", "template", "brain", "work", "observatory", "lab"}
ROUTE_IDS = ["dev", "lead", "docs", "champion"]
LANDINGS = {"en": "docs/en/index.md", "es": "docs/es/index.md"}

def load_data(path) -> dict: ...  # regex the JSON between the script tags, json.loads

def test_each_landing_declares_all_nodes_and_routes_in_order():
    for lang, path in LANDINGS.items():
        data = load_data(path)
        assert set(data["nodes"]) == NODE_IDS, lang
        assert [r["id"] for r in data["routes"]] == ROUTE_IDS, lang

def test_languages_have_the_same_step_structure():
    en, es = (load_data(p) for p in LANDINGS.values())
    shape = lambda d: [[s["node"] for s in r["steps"]] for r in d["routes"]]
    assert shape(en) == shape(es) == [
        ["guide", "template", "work", "lab"],
        ["guide", "brain", "work", "observatory"],
        ["guide", "brain", "work"],
        ["observatory", "lab", "template", "guide"],
    ]

def test_every_route_and_node_has_a_fallback_anchor():
    for path in LANDINGS.values():
        text = Path(path).read_text(encoding="utf-8")
        for rid in ROUTE_IDS:
            assert f'data-route="{rid}"' in text, (path, rid)
        for nid in NODE_IDS:
            assert f'data-node="{nid}"' in text, (path, nid)

def test_data_blocks_have_no_forbidden_dashes_or_urls():
    for path in LANDINGS.values():
        raw = json.dumps(load_data(path), ensure_ascii=False)
        assert "--" not in raw and "—" not in raw and "–" not in raw
        assert "http" not in raw and "](" not in raw
```

- [ ] **Step 2:** Run `uv run pytest tests/test_route_map.py -v`. Expected: FAIL (no data block yet).
- [ ] **Step 3:** Write both landing pages per spec 5.1 (heading, lede, mount point, data block, fallback, loop strip using the existing common loop verbatim, the "will and will not tell you" box). Create the eight route-page stubs.
- [ ] **Step 4:** Implement `route-map.js` and `extra.css` per the Interfaces block and spec 5.2 (accessibility, responsive breakpoint about 860 px, Material custom properties, `hrefFor` returning `null` when the anchor is missing and the renderer omitting the link). Register both in `mkdocs.yml`.
- [ ] **Step 5:** Run `uv run pytest tests/test_route_map.py -v`. Expected: 4 passed.
- [ ] **Step 6: Render check.** `make docs-build`, serve `site/` with `uv run python -m http.server 8765 --directory site` (background), then:
  - `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --dump-dom http://127.0.0.1:8765/en/ > /tmp/en.html` and the same for `/es/`. Expected in each: 6 elements with class `rm-node`, each with `tabindex="0"` and `role="button"`; 4 `<button` elements with `aria-pressed`; one element with `aria-live="polite"`; the `route-map-ready` class present; no `href="null"`.
  - Same command with `--blink-settings=scriptEnabled=false`. Expected: no `rm-node`, fallback cards present with all four route links.
  - `--screenshot=/tmp/en-375.png --window-size=375,1600` and `--window-size=1280,1100`; open both images and confirm no horizontal overflow, panel stacked at 375.
  - `grep -c "Programo con IA" site/search/search_index.json` ≥ 1.
- [ ] **Step 7:** `make check`. Expected: pass.
- [ ] **Step 8:** Commit: `git commit -m "feat(landing): add interactive route map with Markdown fallback (EN/ES)"`.

---

### Task 3: Route pages (delivery 1)

**Files:**
- Modify (fill stubs): `docs/en/routes/build-with-ai.md`, `lead-a-team.md`, `documents-not-code.md`, `improve-the-system.md`; `docs/es/rutas/programo-con-ia.md`, `lidero-un-equipo.md`, `documentos-no-codigo.md`, `mejoro-el-sistema.md`

**Interfaces:**
- Consumes: CSS classes from Task 2 (`.hk-facts`, `.hk-onmap`, `.hk-steps`, `.hk-step`, `.hk-meta`, `.hk-tag`).
- Produces: route pages that Task 7 relinks to kit pages.

Page structure per spec 5.3: title; `.hk-facts` with For / Time / You take away (ES: Para / Tiempo / Te llevás); `.hk-onmap` strip of the route's boxes in order; `.hk-steps` with one `.hk-step` per step (H3 numbered title, `.hk-meta` line, 2 to 5 lines, link deeper); closing `!!! success` admonition ("You finished the route" / "Terminaste la ruta") naming the next route. The dev route's step 2 includes the starter kit tree and the routing table from spec 5.4 and a reference implementation evidence box with the few-skills numbers (lab: 25 skills, 3 opened in 18 runs on six models; production backend (anonymized): 27 to 9 entry points).

Step links in this task (final targets come in Task 7): dev 1 `patterns/working-loop.md`, 2 `start-here/minimal-setup.md`, 3 `concepts/state-and-continuity.md`, 4 `reference-implementation/ai-agentic-harness-lab/index.md`; lead 1 `concepts/harness-engineering.md`, 2 `start-here/company-brain-template.md`, 3 `start-here/agentic-sdlc-for-teams.md`, 4 `adoption/maturity-model.md` and the Observatory page; docs 1 `understand/engineering-vs-knowledge-harness.md`, 2 `use/knowledge-work.md` (ES `use/trabajo-de-conocimiento.md`) and the Company Brain template page, 3 `understand/company-role-second-brain.md`; champion 1 the Observatory page, 2 the lab page and `patterns/failure-to-regression.md`, 3 `start-here/use-and-modify-skills.md`, 4 `adoption/continuous-harness-improvement.md`. ES pages use the ES counterpart of each path as listed in the ES nav.

- [ ] **Step 1:** Write the four EN route pages.
- [ ] **Step 2:** Write the four ES route pages (same structure, voseo).
- [ ] **Step 3:** `make check`. Expected: pass (strict build validates every link).
- [ ] **Step 4:** Spot-check one route page in headless Chrome at 375 px (same server as Task 2): steps stack, no overflow.
- [ ] **Step 5:** Commit: `git commit -m "docs(routes): add four audience route pages (EN/ES)"`.

---

### Task 4: Navigation restructure and redirects (delivery 1)

**Files:**
- Create: `tests/test_nav_parity.py`
- Modify: `mkdocs.yml` (nav, `plugins`), `pyproject.toml`, `uv.lock`
- Delete: `docs/en/use/choose-your-path.md`, `docs/es/use/elegi-tu-camino.md`, `docs/en/start-here/index.md`, `docs/es/start-here/index.md`, `docs/en/learning-path.md`, `docs/es/learning-path.md`
- Modify (links to deleted pages): `docs/en/start-here/leverage-more.md:49`, `docs/es/start-here/leverage-more.md:50`, `docs/en/start-here/onboarding-guide.md:64`, `docs/es/start-here/onboarding-guide.md:65`, `README.md:73`

**Interfaces:**
- Produces: a top-level section "The complete harness" / "El harness completo" whose only child for now is the group "Tool and task guides" / "Guías por herramienta y tarea"; Tasks 5 to 7 insert kit pages above that group.

Target EN nav (ES mirrors it with existing ES titles; new ES titles: Rutas, Programo con IA, Lidero un equipo, Trabajo con documentos, no código, Mejoro el sistema, El harness completo, Guías por herramienta y tarea):

```yaml
- English:
    - Overview: en/index.md
    - Routes:
        - I code with AI: en/routes/build-with-ai.md
        - I lead a team: en/routes/lead-a-team.md
        - I work with documents, not code: en/routes/documents-not-code.md
        - I improve the system: en/routes/improve-the-system.md
    - The complete harness:
        - Tool and task guides:
            - Claude Code basics: en/start-here/claude-code-basics.md
            - Codex: en/start-here/codex.md
            - OpenCode: en/start-here/opencode.md
            - Minimal setup: en/start-here/minimal-setup.md
            - Adopt an existing project: en/start-here/adopt-existing-project.md
            - Create your first skill: en/start-here/create-your-first-skill.md
            - Use and modify skills: en/start-here/use-and-modify-skills.md
            - Onboarding guide: en/start-here/onboarding-guide.md
            - More capabilities: en/start-here/leverage-more.md
    - Understand:
        # existing Understand items, plus, after "Practical introduction":
        # Working loop, Agentic SDLC for teams, then after
        # "Company Brain, Role Brain and Second Brain": Knowledge work,
        # Company Brain template, Project to organization
    - Measure & Improve: # unchanged
    - Reference: # unchanged
```

Redirects (`plugins: [search, redirects]` with `redirect_maps`): the six deleted pages → their language's `index.md`. (`skills-by-intention` is redirected in Task 5.)

- [ ] **Step 1: Write the failing test** `tests/test_nav_parity.py`: load `mkdocs.yml` with a `yaml.SafeLoader` subclass that maps unknown tags (the `!!python/name:` fence formatter) to `None`; flatten the `English` and `Español` subtrees into lists of `(depth, is_group)`; assert they are equal; assert every page path in either subtree exists under `docs/`; assert the first three top-level EN titles are `Overview`, `Routes`, `The complete harness` and ES are `Visión general`, `Rutas`, `El harness completo`.
- [ ] **Step 2:** `uv run pytest tests/test_nav_parity.py -v`. Expected: FAIL on the title assertion.
- [ ] **Step 3:** `uv add mkdocs-redirects`, then pin the resolved version with `==` in `pyproject.toml` to match the existing style; `uv sync`.
- [ ] **Step 4:** Rewrite both nav subtrees, add the plugin and `redirect_maps`, delete the six pages, fix the five links (README points to the site root `https://marcosdh1987.github.io/harness-engineering-guide/en/`).
- [ ] **Step 5:** `uv run pytest tests/test_nav_parity.py -v`. Expected: pass.
- [ ] **Step 6:** `make check`. Expected: pass. Then confirm `site/en/use/choose-your-path/index.html` exists and contains a redirect to the overview.
- [ ] **Step 7:** Commit: `git commit -m "docs(nav): put routes and the complete harness first; redirect old entry pages"`.

---

### Task 5: Kit overview, starter kit and few skills (delivery 2)

**Files:**
- Create: `tests/test_harness_kit_pages.py`
- Create: `docs/en/harness-kit/index.md`, `docs/en/harness-kit/few-skills.md`, `docs/es/harness-completo/index.md`, `docs/es/harness-completo/pocas-skills.md`
- Delete: `docs/en/use/skills-by-intention.md`, `docs/es/use/skills-por-intencion.md` (content moves into few-skills)
- Modify: `mkdocs.yml` (nav entries at the top of "The complete harness"; redirects for the two deleted pages to few-skills), `docs/en/start-here/agentic-sdlc-for-teams.md:176,189` and ES `:176,189` (links to few-skills)

**Interfaces:**
- Produces, page template (headings, exact text) used by Tasks 5 to 7 for `few-skills` and every practice page:
  - EN H2s in order: `What it is`, `Why it pays off`, `Template`, `When to use it and when to skip it`, `What failed in practice`, `How to check it is healthy`, `Go deeper`.
  - ES H2s in order: `Qué es`, `Por qué rinde`, `Plantilla`, `Cuándo usarlo y cuándo no`, `Qué falló en la práctica`, `Cómo saber si está sano`, `Para profundizar`.
- Produces, `KIT_PAGES` mapping in the test (EN file → ES file) that Tasks 6 and 7 extend.

- [ ] **Step 1: Write the failing test** `tests/test_harness_kit_pages.py`:

```python
EN_H2 = ["What it is", "Why it pays off", "Template",
         "When to use it and when to skip it", "What failed in practice",
         "How to check it is healthy", "Go deeper"]
ES_H2 = ["Qué es", "Por qué rinde", "Plantilla", "Cuándo usarlo y cuándo no",
         "Qué falló en la práctica", "Cómo saber si está sano", "Para profundizar"]
KIT_PAGES = {"few-skills.md": "pocas-skills.md"}  # extended in Tasks 6 and 7

def h2s(path) -> list[str]: ...  # lines starting with "## ", stripped

def test_practice_pages_follow_the_template_in_both_languages():
    for en, es in KIT_PAGES.items():
        assert h2s(f"docs/en/harness-kit/{en}") == EN_H2, en
        assert h2s(f"docs/es/harness-completo/{es}") == ES_H2, es

def test_every_kit_page_has_an_evidence_box():
    for en, es in KIT_PAGES.items():
        assert '"Evidence level:' in Path(f"docs/en/harness-kit/{en}").read_text()
        assert '"Nivel de evidencia:' in Path(f"docs/es/harness-completo/{es}").read_text()

def test_kit_index_shows_the_starter_tree_and_routing_table():
    for path in ("docs/en/harness-kit/index.md", "docs/es/harness-completo/index.md"):
        text = Path(path).read_text(encoding="utf-8")
        for needle in ("AGENTS.md", "memory/", "docs/adr/", "docs/plans/",
                       "make check", "LEVEL=minimal"):
            assert needle in text, (path, needle)
```

- [ ] **Step 2:** `uv run pytest tests/test_harness_kit_pages.py -v`. Expected: FAIL (files missing).
- [ ] **Step 3:** Write the kit index (EN, ES) per spec 5.4: why most value is not in skills; the starter tree; copyable `AGENTS.md` (short rules, routing table), one-line `CLAUDE.md`, `memory/README.md` with the entry format, `docs/adr/README.md` and `0000-template.md` (all rewritten generically, as fenced code blocks); approach A for skills (links to the seven files in `ml-python-base`, the per-tool folder table taken only from `docs/en/reference-implementation/ml-python-base/skills.md` and `docs/en/tools/*.md`, the symlink note, lines to adapt outside Python); `make init NAME=... LEVEL=minimal` for new Python projects; how each piece maps to the working loop.
- [ ] **Step 4:** Write few-skills (EN, ES) with the template headings: the seven skills and what each is for; evidence box with the lab and production numbers and sample sizes from spec 5.4; "harness level" vs "skill profile" naming note; adding one trialled skill at a time; the intention families table from the deleted skills-by-intention pages under "Go deeper".
- [ ] **Step 5:** Nav entries, redirects, and the two link fixes.
- [ ] **Step 6:** `uv run pytest tests/ -v`. Expected: all pass.
- [ ] **Step 7:** `make check`; then `grep -c "starter kit" site/search/search_index.json` ≥ 1.
- [ ] **Step 8:** Commit: `git commit -m "docs(harness-kit): add starter kit and few-skills pages (EN/ES)"`.

---

### Task 6: Memory, decision records, plans and specs (delivery 2)

**Files:**
- Create: `docs/en/harness-kit/{project-memory,decision-records,plans-and-specs}.md`, `docs/es/harness-completo/{memoria-del-proyecto,registros-de-decision,planes-y-specs}.md`
- Modify: `tests/test_harness_kit_pages.py` (extend `KIT_PAGES`), `mkdocs.yml` (nav)

**Interfaces:**
- Consumes: page template and `KIT_PAGES` from Task 5.

Content per spec 5.4 "Content facts to use": memory (three files, entry format, rules, the 3,500-line and stale-reference failures, size budget and pruning); decision records (template header and four sections, one page, when to write and skip, supersede, `/adr`, index; over 100 ADRs in about two months with decision-sentence titles, more than half still "Proposed", recommendation to accept on merge); plans and specs (approved design, plan, execution without reopening; the design gate referenced far more than specs were written; keep the gate for new or ambiguous work only). Each links to `concepts/state-and-continuity.md` and the relevant reference pages under "Go deeper".

- [ ] **Step 1:** Extend `KIT_PAGES` with the three pairs. Run `uv run pytest tests/test_harness_kit_pages.py -v`. Expected: FAIL.
- [ ] **Step 2:** Write the three EN pages.
- [ ] **Step 3:** Write the three ES pages.
- [ ] **Step 4:** Nav entries; `uv run pytest tests/ -v` passes; `make check` passes.
- [ ] **Step 5:** Commit: `git commit -m "docs(harness-kit): add memory, decision records, plans and specs pages (EN/ES)"`.

---

### Task 7: Commands, hooks, quality gates, health check; final relinking (delivery 2)

**Files:**
- Create: `docs/en/harness-kit/{commands,hooks,quality-gates,health-check}.md`, `docs/es/harness-completo/{comandos,hooks,gates-de-calidad,chequeo-de-salud}.md`
- Modify: `tests/test_harness_kit_pages.py` (extend `KIT_PAGES` with commands, hooks, quality-gates; the health check is a checklist page, not on the template), `mkdocs.yml` (nav), both landing pages (node anchors), all eight route pages (step links)

**Interfaces:**
- Consumes: page template and `KIT_PAGES` from Task 5; landing fallback anchors from Task 2; route pages from Task 3.

Content per spec 5.4: commands (`/plan`, `/adr`, `/retro`, `/verify` as thin shortcuts with generic example files); hooks (session start reminder, end-of-turn reminder, ask-before-commit permissions; remind versus block; Claude Code specifics cited to vendor docs, other tools only where the existing tool pages already document them); quality gates (one `make check` that can fail, does not rewrite the tree, CI runs the same; architecture-layer test; docs-with-code check); health check (the eight checks with names exactly as in spec 5.4, each with "how to check by reading" and "why", budget 200 lines or about 2,500 tokens, then `git clone https://github.com/marcosdh1987/ai-agentic-harness-lab` and `make harness-check REPO=../your-repo`, stating setup `git`, `uv`, `make`, no Docker, no model, about 30 seconds per run).

Final link targets: landing `template` → `harness-kit/index.md`, `work` → `harness-kit/index.md`, `lab` → `harness-kit/health-check.md`. Route steps: dev 2 → kit index, dev 3 → project memory, dev 4 → health check; lead 3 → decision records (keep Agentic SDLC as second link); champion 3 → few skills. ES equivalents.

- [ ] **Step 1:** Extend `KIT_PAGES` with the three template pairs and add `test_health_check_lists_the_eight_checks` asserting each of the eight check names (EN) appears in `health-check.md` and the ES translations appear in `chequeo-de-salud.md`. Run tests. Expected: FAIL.
- [ ] **Step 2:** Write the four EN pages.
- [ ] **Step 3:** Write the four ES pages.
- [ ] **Step 4:** Nav entries; relink landings and route pages to the final targets.
- [ ] **Step 5:** `uv run pytest tests/ -v` passes; `make check` passes; re-run the Task 2 render check for `/en/` and `/es/` (node links now point to kit pages; still no `href="null"`).
- [ ] **Step 6:** Commit: `git commit -m "docs(harness-kit): add commands, hooks, gates and health check; relink routes (EN/ES)"`.

---

### Task 8: Naming, ecosystem list, migration example, private repo notes (delivery 3)

**Files:**
- Modify: `README.md`, `CLAUDE.md`, `AGENTS.md`, `docs/en/reference-implementation/index.md`, `docs/es/reference-implementation/index.md`, `docs/en/start-here/agentic-sdlc-for-teams.md`, `docs/es/start-here/agentic-sdlc-for-teams.md`, and every page the greps below return

**Interfaces:**
- Consumes: final landing and kit pages (Tasks 2 to 7) so new copy already uses the canonical names.

- [ ] **Step 1:** `grep -rn "Agentic Harness Lab\|ai-agentic-harness-lab\|sdlc-ml-python-harness-lab" docs README.md CLAUDE.md AGENTS.md`. In prose, use "Harness Lab"; keep repository names only on `reference-implementation/ai-agentic-harness-lab/*` pages and in clone commands. Lab repository links point to `https://github.com/marcosdh1987/ai-agentic-harness-lab` (public mirror of `xmartlabs/sdlc-ml-python-harness-lab`).
- [ ] **Step 2:** Make the ecosystem list identical in `README.md` (text and Mermaid), `CLAUDE.md` ("5-Layer Ecosystem" becomes the spec 5.6 list), `AGENTS.md` (add the list under Repository Purpose) and both reference-implementation index pages: Guide; `ml-python-base` (Engineering Harness template); `company-brain-template` (Knowledge Harness); Engineering Delivery Observatory (`ai-gateway` reference); Harness Lab (evaluation); `ml-langchain-agent` (product runtime reference).
- [ ] **Step 3:** Every link to `ai-gateway` or `ml-langchain-agent` gets the note "(not public yet)" / "(todavía no público)" next to it.
- [ ] **Step 4:** `grep -rn "80%\|never suffer" docs README.md`: label the migration scenario as illustrative in an admonition (EN `Illustrative scenario` / ES `Escenario ilustrativo`), remove "will never suffer that failure mode again" and its ES equivalent.
- [ ] **Step 5:** `make check` passes.
- [ ] **Step 6:** Commit: `git commit -m "docs: unify lab naming and ecosystem list; mark illustrative example; note private repos"`.

---

### Task 9: Lab reference pages caught up to lab main (delivery 3)

**Files:**
- Modify: `docs/en/reference-implementation/ai-agentic-harness-lab/index.md`, `evaluation-workflow.md`, and the ES pair

**Interfaces:**
- Consumes: the lab mirror at `marcosdh1987/ai-agentic-harness-lab` main (`bb7ad2e`, tree equal to upstream `84a4f65`). Read facts from it (clone or `gh api`), never from the private production backend.

- [ ] **Step 1:** Rewrite the opening of the lab overview in plain words (what it answers, who it is for, how to start), with no ADR numbers, mode letters or hashes in the first two sections; move those details lower.
- [ ] **Step 2:** Add the spec 5.6 lab items: guided flows; skill profiles and "removal must be earned"; `make harness-check`; taking a harness home with `make harness-export` (preview first, `APPLY=1` writes); the six one-page journeys; evaluation modes as the lab home phrases them; Codex and Gemini harnesses and reasoning effort. Explain that the public repository is a mirror of the organization's, where development happens; keep the existing Xmartlabs attribution.
- [ ] **Step 3:** Mirror in ES.
- [ ] **Step 4:** `make check` passes.
- [ ] **Step 5:** Commit: `git commit -m "docs(lab): catch the Harness Lab pages up to lab main (EN/ES)"`.

---

### Task 10: Final verification

**Files:** none (verification only; fix and commit anything it finds in the owning task's style).

- [ ] **Step 1:** Privacy grep with the maintainer's term list kept outside the repository (scratchpad file, never committed): `grep -rniF -f <term-list> docs README.md CLAUDE.md AGENTS.md site`. Expected: no output.
- [ ] **Step 2:** `make check`. Expected: pass.
- [ ] **Step 3:** Headless Chrome render check for `/en/`, `/es/`, one route page and one kit page per language at 375 px and 1280 px; JS-disabled check of both landings; open the screenshots and confirm.
- [ ] **Step 4:** Click-through check from `dump-dom`: every href inside `#route-map` resolves to a built file under `site/`.
- [ ] **Step 5:** `git log --oneline main..` lists one commit per task; working tree clean.
