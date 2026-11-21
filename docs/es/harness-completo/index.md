# El harness completo

Las skills se llevan la atención, pero en los proyectos de referencia la mayor parte del valor de todos los días vino de piezas más simples: un archivo de reglas corto, una memoria del proyecto, registros de decisión de una página, planes aprobados, unos pocos comandos y hooks, y un gate que puede fallar. Esta sección documenta cada pieza con una plantilla para copiar.

!!! info "Nivel de evidencia: implementación de referencia"
    En un backend de producción (anonimizado), durante unos dos meses (alrededor de 1.000 commits), lo que más escribieron las personas y los agentes fueron registros de decisión (más de 100) y planes (unos 27). Su catálogo de skills pasó de 27 skills sueltas a 9 puntos de entrada. Es un equipo y un código: leelo como una señal de dónde está el valor, no como un benchmark.

## El kit inicial

Sirve en un repositorio que ya tenés, en cualquier lenguaje. Solo las skills están escritas hoy para un stack de Python; la [sección de skills](#skills) más abajo dice qué adaptar.

```text
tu-repo/
├── AGENTS.md          reglas cortas + tabla "¿qué tamaño tiene la tarea?"
├── CLAUDE.md          una línea que importa AGENTS.md (para Claude Code)
├── memory/            README.md · context.md · learnings.md · patterns.md
├── docs/adr/          README.md (cuándo escribir uno) + 0000-template.md
├── docs/plans/        planes aprobados
├── <herramienta>/skills/   las 7 skills iniciales, en la carpeta que lee tu herramienta
└── make check         o el comando que ya verifica tu proyecto
```

### `AGENTS.md`

El archivo que leen todas las herramientas. Mantenelo lo bastante corto como para leerlo en un minuto: se carga en cada sesión. Los agentes leen bien en inglés, por eso la plantilla está en inglés; podés escribirla en el idioma de tu equipo.

```markdown
# AGENTS.md

## What this project is
<One paragraph: what it does, who uses it, and what must never break.>

## How to work here
Use the loop: understand, plan when needed, execute, verify, learn.
Scale the ceremony to the task:

| If the task is... | Do this |
| --- | --- |
| Small and clear (typo, one-line fix) | Make the change, run the narrowest check |
| Bounded (a bug, a small feature) | Quick brainstorm, short plan, execute, verify |
| New or ambiguous (new module, risky change) | Write a design, get it approved, then plan and execute |

## Before you start
- Read `memory/context.md` and skim `memory/learnings.md`.
- Search the code before editing it.

## Done means
- `make check` passes (or: <your verification command>).
- A decision that is hard to reverse has a record in `docs/adr/`.
- Anything non-obvious you learned goes to `memory/learnings.md`.

## Never
- Commit, push, or merge without asking.
- Put secrets, personal data, or customer data in code, logs, or memory.
```

### `CLAUDE.md`

Claude Code lee `CLAUDE.md` y puede importar otros archivos con `@ruta`, así que una sola línea mantiene una única fuente de reglas:

```markdown
@AGENTS.md
```

### `memory/`

```text
memory/
├── README.md       cómo escribir una entrada
├── context.md      dónde está el proyecto hoy: foco, temas abiertos
├── learnings.md    hechos no obvios: trampas, callejones sin salida, por qué algo es así
└── patterns.md     convenciones que los demás deberían seguir
```

Cada entrada tiene la misma forma:

```markdown
## <título corto>: <AAAA-MM-DD>

<Una o dos oraciones con el hecho.>

**Por qué importa:** <la consecuencia>
**Cómo aplicarlo:** <qué hacer la próxima vez>
```

### `docs/adr/`

Una página por cada decisión difícil de revertir. Copiá esto como `docs/adr/0000-template.md`:

```markdown
# ADR-NNNN: <la decisión, como una oración>

- **Estado:** Propuesto <!-- Propuesto | Aceptado | Reemplazado por ADR-XXXX -->
- **Fecha:** AAAA-MM-DD
- **Decidieron:** <nombres o roles>
- **Relacionado:** <otros ADRs, entradas de memoria, docs>

## Contexto
¿Qué obligó a decidir? Contá los hechos para que alguien que no estuvo lo entienda.

## Decisión
"Vamos a ..." Lo bastante concreto como para actuar.

## Consecuencias
Qué se vuelve más fácil, qué más difícil y qué trabajo queda pendiente.

## Alternativas consideradas
- <Opción>: por qué no se eligió.
```

### `docs/plans/`

Un archivo por plan aprobado, con el nombre `AAAA-MM-DD-<tema>.md`: los pasos, los archivos que toca cada paso y cómo se verifica cada uno. Un plan empieza después de que el diseño está aprobado y no lo reabre.

### Skills { #skills }

Las siete skills iniciales son el nivel `minimal` del template. [Empezá con pocas skills](pocas-skills.md) explica por qué siete y para qué sirve cada una.

| Skill | Fuente en `ml-python-base` |
| --- | --- |
| `brainstorm_quick` | [.github/skills/brainstorm_quick.md](https://github.com/marcosdh1987/ml-python-base/blob/main/.github/skills/brainstorm_quick.md) |
| `plan_and_execute_feature` | [.github/skills/plan_and_execute_feature.md](https://github.com/marcosdh1987/ml-python-base/blob/main/.github/skills/plan_and_execute_feature.md) |
| `research_current_info` | [.github/skills/research_current_info.md](https://github.com/marcosdh1987/ml-python-base/blob/main/.github/skills/research_current_info.md) |
| `systematic_debugging` | [.github/skills/systematic_debugging.md](https://github.com/marcosdh1987/ml-python-base/blob/main/.github/skills/systematic_debugging.md) |
| `verify_changes` | [.github/skills/verify_changes.md](https://github.com/marcosdh1987/ml-python-base/blob/main/.github/skills/verify_changes.md) |
| `writing-plans` | [.github/skills-external/writing-plans/SKILL.md](https://github.com/marcosdh1987/ml-python-base/blob/main/.github/skills-external/writing-plans/SKILL.md) |
| `requesting-code-review` | [.github/skills-external/requesting-code-review/SKILL.md](https://github.com/marcosdh1987/ml-python-base/blob/main/.github/skills-external/requesting-code-review/SKILL.md) |

Cada herramienta lee las skills desde su propia carpeta. Estas son las carpetas a las que proyecta el template de referencia; revisá la documentación de tu herramienta por si cambiaron:

| Herramienta | Carpeta |
| --- | --- |
| Claude Code | `.claude/skills/<nombre>/SKILL.md` |
| OpenCode | `.opencode/skills/<nombre>/SKILL.md` |
| Codex | `.codex/skills/<nombre>/SKILL.md` |
| Antigravity | `.agents/skills/<nombre>/SKILL.md` |
| GitHub Copilot | No tiene carpeta nativa de skills: poné las reglas y la tabla de ruteo en `.github/copilot-instructions.md` |

En el template, esas carpetas por herramienta son symlinks que genera `make sync-skills`, así que si las descargás desde GitHub recibís una ruta y no la skill. Copiá desde la fuente gobernada:

```bash
mkdir -p .claude/skills/verify_changes
curl -fsSL https://raw.githubusercontent.com/marcosdh1987/ml-python-base/main/.github/skills/verify_changes.md \
  -o .claude/skills/verify_changes/SKILL.md
```

Fuera de un stack de Python, adaptá unas pocas líneas de cada skill interna:

- El comando de verificación (`make check`, `pytest`) pasa a ser tu comando de build y tests.
- Las referencias a `.github/architecture.md`, `.github/standards.md` y `.github/domain-boundaries.md` apuntan a tu `AGENTS.md`, o se borran.
- Las fuentes específicas del lenguaje en `research_current_info` (docs de Python, `uv`, `ruff`) pasan a ser la documentación oficial de tu stack.

¿Arrancás un proyecto de Python nuevo? El template trae el kit completo y el nivel `minimal` por defecto:

```bash
git clone https://github.com/marcosdh1987/ml-python-base mi-proyecto
cd mi-proyecto
make init NAME=mi_proyecto LEVEL=minimal
```

## Cómo se conectan las piezas con el ciclo

| Paso del ciclo | Piezas |
| --- | --- |
| Entender | `AGENTS.md`, `memory/context.md`, `memory/learnings.md` |
| Planificar o diseñar | La tabla de ruteo, `docs/plans/` |
| Ejecutar | Skills, comandos |
| Verificar | `make check`, hooks |
| Aprender | `memory/learnings.md`, `docs/adr/` |

## Páginas de esta sección

- [Empezá con pocas skills](pocas-skills.md): las siete skills iniciales y cuándo sumar más.
