# El template de Company Brain

La página [Del proyecto a la organización](proyecto-a-organizacion.md)
introduce el Company Brain como concepto. Esta página documenta su
**implementación concreta**: el repositorio
[`company-brain-template`](https://github.com/marcosdh1987/company-brain-template)
(v1.0) — un punto de partida materializado para la capa de contexto
organizacional, consolidado a partir de engagements reales con clientes.

!!! tip "Cuándo usar este template"
    No el día uno. Un engagement de un solo repo mantiene su contexto
    *adentro* del repo (`memory/`, `docs/adr/`) — ese **project brain**
    in-repo alcanza. Este template se gana su lugar cuando el engagement
    abarca más de un repo, más de un proyecto, o una relación de consultoría
    donde la evidencia y las decisiones deben sobrevivir a cualquier
    codebase. La progresión completa está en
    [Adopción en un proyecto existente](adopt-existing-project.md).

## La idea central: un pipeline de evidencia → conocimiento

El brain se organiza como un pipeline de promoción. El material crudo es
**evidencia, no hechos**; solo el contenido citado y con estado se vuelve
conocimiento canónico:

```text
material crudo            promoción                conocimiento canónico
99-inbox/            →    analizar, extraer,   →   06-decisions/   05-requirements/
01-meetings/              validar, citar           00-context/     03-projects/ …
09-references/
```

Toda afirmación no obvia lleva uno de cinco estados — `CONFIRMED`,
`PENDING VALIDATION`, `INFERRED`, `SUPERSEDED`, `BLOCKED` — y una fuente.
Las fuentes reciben IDs (`SRC-XXX`) en un **source register** que además
registra conflictos entre fuentes y la regla de precedencia adoptada, sin
editar jamás la evidencia original. Las decisiones son entradas `DEC-XXX`
inmutables. La fuente única de reglas operativas es `AGENTS.md`; todo adapter
de herramienta (`CLAUDE.md`, Copilot) remite a él, así dos juegos de reglas
nunca pueden divergir.

## Estructura (modular)

Los módulos se activan por engagement en `brain.config.json`; el validador
solo exige los activos. `make init ORG="…" PROFILE=…` los preselecciona
(perfiles: `consulting`, `delivery-oversight`, `development`, `full`).

| Módulo | Core | Contenido |
|---|---|---|
| `00-context/` | ✔ | visión de la empresa, alcance del engagement, stakeholders, glosario |
| `01-meetings/` | ✔ | transcripts (evidencia) + minutas revisadas + template de intake |
| `02-organization/` | | ways of working, convenciones (ingeniería, git, **ticketing**, comunicación), política de IA, ownership, runbooks de la org |
| `03-projects/` | | una carpeta por proyecto: overview → estado actual → estado objetivo → plan → checklist → change log |
| `04-architecture/` | | mapa de sistemas, `repos.yaml` (registro de repos de código), integraciones |
| `05-requirements/` | | funcionales, no funcionales, reglas de negocio, preguntas abiertas |
| `06-decisions/` | ✔ | log de decisiones `DEC-XXX` inmutable |
| `07-delivery/` | | estado, roadmap, action items, matriz de validación, check periódico que completa el cliente |
| `08-vendors/` | | registro de vendors + evaluaciones |
| `09-references/` | ✔ | fuentes primarias + source registers con registro de conflictos |
| `99-inbox/` | ✔ | zona de aterrizaje; los archivos salen marcados `processed--` |

`02-organization/` es donde viven los modos de trabajo de la organización
como **declaraciones** — el harness de ingeniería las *aplica* en cada repo;
el brain las *declara* una vez. Incluye `conventions/ticketing.md`: las
skills genéricas ("planificar desde un ticket") lo leen para adaptarse al
tracker, los estados del workflow y las definiciones de ready/done de la
organización.

## El modelo workspace: brain + repos de código

Cuando la organización tiene repos de código, el layout es **hub-and-spoke
con clones hermanos — nunca submódulos, nunca anidado**:

```text
~/work/acme/
├── acme-brain/          ← el hub
├── api-pagos/           ← spoke: su CLAUDE.md importa @../acme-brain/…
└── portal-web/          ← spoke
```

El día 1 de un dev es `git clone <brain> && make workspace` — el target lee
`04-architecture/repos.yaml` y clona cada repo registrado al lado. Los
submódulos se descartan deliberadamente: un submódulo pinea un commit
(contexto viejo por diseño), agrega fricción de clones/permisos, e invierte
la dependencia — el contexto no debe depender del código. La convención de
hermanos hace la ruta de import relativa predecible en toda máquina; si el
brain falta, los imports degradan sin romper, y en CI el brain se chequea
como segundo repo. Racional completo: `docs/workspace.md` del template.

## Ciclo de vida

Las skills gobernadas cubren el ciclo completo: `bootstrap_company_brain`
(arranque en limpio o **modo migración** para organizaciones con historia:
todo al inbox → source register con conflictos → promoción gradual),
`process_meeting` (transcript → minutas → conocimiento promovido),
`update_domain_context`, `record_decision`, `add_runbook` y
`quarterly_context_review` (la auditoría anti-drift). La validación es
automática y semántica: `make validate` chequea estructura según config,
links, IDs duplicados, decisiones sin fuente, y reporta deuda de
placeholders e inbox. El brain además **sincroniza skills de trabajo** (brainstorming, planificación, research, escritura) desde el harness — declaradas en `brain.config.json`, lockeadas por sha256 — y proyecta cada skill a los layouts `.claude/`, `.codex/` y `.agents/` para que Claude Code, Codex y Antigravity las descubran nativamente (`make sync-skills`).

## Relación con el resto del ecosistema

La guía explica los conceptos; `ml-python-base` aporta la capa de ejecución y
distribuye las skills del ciclo de vida del brain; el lab puede medir qué
secciones consultan realmente los agentes. El template (estructura + skills)
es un activo de ingeniería reutilizable; cada brain instanciado pertenece a
la organización que describe.
