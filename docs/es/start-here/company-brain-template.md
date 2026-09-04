# El template de Company Brain

La página [Del proyecto a la organización](proyecto-a-organizacion.md)
introduce el Company Brain como concepto. Esta página documenta su
**implementación concreta**: el repositorio
[`company-brain-template`](https://github.com/marcosdh1987/company-brain-template)
— un punto de partida materializado para la capa de contexto
organizacional, consolidado a partir de operaciones reales y engagements con clientes.

!!! tip "Cuándo usar este template"
    No el día uno. Un engagement de un solo repo mantiene su contexto
    *adentro* del repo (`memory/`, `docs/adr/`) — ese **project brain**
    in-repo alcanza. Este template se gana su lugar cuando el alcance
    abarca más de un repo, más de un proyecto, o una relación operativa
    donde la evidencia y las decisiones deben sobrevivir a cualquier
    codebase individual. La progresión completa está en
    [Adopción en un proyecto existente](adopt-existing-project.md).

## La idea central: un pipeline de evidencia → conocimiento

El brain se organiza como un pipeline de promoción. El material crudo es
**evidencia, no hechos**; solo el contenido citado y con estado se vuelve
conocimiento canónico:

```text
material crudo            promoción                conocimiento canónico
99-inbox/            →    analizar, extraer,   →   06-decisions/   05-requirements/
01-meetings/              validar, citar           00-context/     03-work/ …
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

## Dos arquetipos: Engagement Brain vs. Operating Company Brain

Un aprendizaje arquitectónico clave derivado de la práctica es que las organizaciones operan dos arquetipos diferenciados de Company Brain según su horizonte operativo:

```text
┌──────────────────────────────────────┐     ┌──────────────────────────────────────┐
│          Engagement Brain            │     │       Operating Company Brain        │
├──────────────────────────────────────┤     ├──────────────────────────────────────┤
│ • Misión orientada a cliente         │     │ • Función u org interna (p. ej. XL)  │
│ • Ciclo acotado (semanas/meses)      │     │ • Operaciones continuas y evolución  │
│ • Foco en minutas y entrevistas      │     │ • Taxonomía de trabajo (03-work/)    │
│ • Objetivo: Discovery y Handoff      │     │ • Objetivo: Ejecución y Capacidades  │
└──────────────────────────────────────┘     └──────────────────────────────────────┘
```

| Dimensión | Engagement Brain | Operating Company Brain |
|---|---|---|
| **Alcance principal** | Cliente específico, auditoría o consultoría externa | Departamento, organización de ingeniería o empresa |
| **Ciclo de vida** | Acotado en el tiempo (semanas a meses) | Continuo y permanente |
| **Unidad central de trabajo** | Hitos del engagement, entregables, revisiones formales | Iniciativas estructuradas, discovery spikes, capacidades (`03-work/`) |
| **Perfil de evidencia** | Transcripts de reuniones cliente, insumos externos, inbox | Sistemas de registro (Jira, GitHub, Slack), retrospectivas internas |
| **Stakeholders principales** | Sponsors del cliente, líder de consultoría | Engineering managers, tech leads, agentes autónomos internos |
| **Salida clave** | Recomendaciones, informes de auditoría, traspaso técnico | Ejecución operativa, ADRs corporativos, biblioteca de capacidades |

Identificar qué arquetipo se está construyendo evita desajustes estructurales: un engagement brain prioriza la trazabilidad de evidencia y entregables al cliente, mientras que un operating company brain se enfoca en taxonomías de trabajo continuo, capacidades internas y hubs por rol.

## Estructura (modular)

Los módulos se activan por despliegue en `brain.config.json`; el validador
solo exige los activos. `make init ORG="…" PROFILE=…` los preselecciona
(perfiles: `consulting`, `delivery-oversight`, `management`, `development`, `full`).

| Módulo | Core | Contenido |
|---|---|---|
| `00-context/` | ✔ | visión de la empresa, alcance operativo, stakeholders, glosario |
| `01-meetings/` | ✔ | transcripts (evidencia) + minutas revisadas + template de intake |
| `02-organization/` | | ways of working, convenciones (ingeniería, git, **ticketing**, comunicación), política de IA, ownership, runbooks de la org |
| `03-work/` | | unidades de trabajo estructuradas: iniciativas, discovery, capacidades, cadencias operativas (overview → status → plan → execution log) |
| `04-architecture/` | | mapa de sistemas, `repos.yaml` (registro de repos de código), integraciones |
| `05-requirements/` | | funcionales, no funcionales, reglas de negocio, preguntas abiertas |
| `06-decisions/` | ✔ | log de decisiones `DEC-XXX` inmutable |
| `07-delivery/` | | estado, roadmap, action items, matriz de validación, chequeos de salud periódicos |
| `08-vendors/` | | registro de vendors + evaluaciones |
| `09-references/` | ✔ | fuentes primarias + source registers con registro de conflictos |
| `99-inbox/` | ✔ | zona de aterrizaje; los archivos salen marcados `processed--` |

`02-organization/` es donde viven los modos de trabajo de la organización
como **declaraciones** — el harness de ingeniería las *aplica* en cada repo;
el brain las *declara* una vez. Incluye `conventions/ticketing.md`: las
skills genéricas ("planificar desde un ticket") lo leen para adaptarse al
tracker, los estados del workflow y las definiciones de ready/done de la
organización.

---

## Lecciones de operar un management brain real

La evolución del Company Brain desde los templates iniciales de consultoría hacia sistemas operativos de gestión en producción (como brains de gestión ejecutiva tipo `em-xl`) aportó aprendizajes esenciales:

### 1. La transición de `03-projects/` a `03-work/`
Las arquitecturas tempranas modelaban la actividad organizacional exclusivamente como "proyectos" (`03-projects/`). En la operativa real de management esto resultó excesivamente restrictivo:
- Gran parte del trabajo organizacional consiste en cadencias operativas recurrentes, picos de descubrimiento técnico, mantenimiento de infraestructura o desarrollo de capacidades internas —ninguno de los cuales es un proyecto de software tradicional.
- `03-work/` unifica toda la actividad operativa bajo una **taxonomía de unidades de trabajo** coherente.

### 2. Stage vs. Folder (Desacoplar el estado de la ruta del archivo)
Un antipatrón habitual consiste en mover archivos entre carpetas para reflejar cambios de estado (p. ej., de `work/active/` a `work/completed/`).
- Mover archivos rompe enlaces internos de markdown, invalida memorias previas de los agentes y ensucia el historial de Git.
- **Solución**: La estructura de carpetas refleja el dominio o la jerarquía, mientras que el estado del ciclo de vida (`stage`: `draft`, `active`, `review`, `done`, `paused`) se gestiona en metadatos YAML frontmatter legibles por máquinas.

### 3. Tier vs. Type
Las unidades de trabajo deben clasificarse en dos dimensiones ortogonales:
- **Type (Tipo)**: La naturaleza del trabajo (`initiative`, `discovery`, `capability`, `operations`).
- **Tier (Nivel)**: El radio de impacto y criticidad operativa (`Tier 1`: estratégico/compañía, `Tier 2`: equipo/departamento, `Tier 3`: local/operativo).

### 4. Rigor graduado (Graduated Rigor)
No todas las tareas justifican la misma sobrecarga administrativa:
- Imponer registros de evidencia exhaustivos y gates formales de decisión a un script operativo trivial genera fricción y abandono del sistema.
- Bajo el **rigor graduado**, las iniciativas Tier 1 exigen justificación explícita de problemas, source registers formales, aprobaciones de stakeholders y entradas `DEC-XXX` inmutables; las tareas Tier 3 solo requieren un plan conciso y una checklist de verificación.

### 5. Biblioteca de capacidades (Capability Library)
Operar una organización requiere capacidades duraderas (p. ej., rúbricas de evaluación estandarizadas, playbooks de onboarding, marcos de post-mortem de incidentes) que sobreviven a proyectos o trimestres individuales. Separar las capacidades reutilizables en una biblioteca específica evita que la memoria institucional quede sepultada en carpetas de proyectos cerrados.

### 6. Índices generados para evitar la saturación de contexto
Los agentes nunca deben realizar recorridos recursivos sobre cientos de archivos en `03-work/`. En su lugar, automatizaciones ligeras (`make index`) parsean el frontmatter YAML de las unidades de trabajo y generan tablas de catálogo compactas (como `work-index.md`). Esto permite a los agentes ejecutar el [Patrón de Selective Context](../concepts/context-engineering.md#el-patron-de-selective-context) sin agotar sus presupuestos de tokens.

### 7. Hubs orientados a roles
Las organizaciones integran distintos perfiles: líderes ejecutivos, engineering managers, tech leads y agentes autónomos. Proveer archivos hub orientados a roles (p. ej., `hub-leadership.md`, `hub-engineering.md`) ofrece puntos de entrada con alta relación señal-ruido, adaptados a las decisiones y supervisión específicas de cada perfil.

---

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
