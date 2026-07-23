# Configuración mínima: copiá esto, entendé esto

Un `CLAUDE.md` pequeño que podés defender línea por línea le gana a uno grande que heredaste y
no entendés. Esta página te da un punto de partida mínimo y *comprendido* — copialo y después
hacelo crecer de manera deliberada.

## El objetivo: pequeño y con dueño

El `CLAUDE.md` de referencia en `ml-python-base` es un adapter gobernado de ~186 líneas — y
ese tamaño es exactamente lo que abruma a los recién llegados. La buena noticia: **casi todo
es prosa editable.** Solo una pequeña región es gestionada por máquina. Así que empezá mínimo
y agregá únicamente lo que entendés.

## `CLAUDE.md` mínimo

Copiá esto en la raíz de tu proyecto y ajustá el nombre del proyecto:

```markdown
# <Project> — Claude Code Adapter

## Governance
Always read and apply before generating code or plans:
- `.github/architecture.md`
- `.github/standards.md`
- `.github/domain-boundaries.md`

## Automation
Skills are generated. After adding or editing a skill under `.github/skills/`, run
`make sync-skills`. CI enforces `make check-sync`.

<!-- BEGIN GENERATED SKILLS (managed by skills_sync; do not edit) -->
<!-- END GENERATED SKILLS -->
```

Qué es cada parte, y si la editás:

| Parte | Por qué está acá | ¿Editar? |
|---|---|---|
| Puntero `## Governance` | Dirige el contexto por instrucción a los tres documentos de gobernanza de "leer siempre" | Sí — prosa plana |
| Puntero `## Automation` | Una línea que le dice a humanos y agentes cómo se propagan las skills | Sí — prosa plana |
| Marcadores `BEGIN/END GENERATED SKILLS` | Sentinelas obligatorios que el motor de sync completa con la lista de skills | **No** — gestionados por máquina |

!!! warning "Los dos sentinelas no son opcionales"
    El motor de skills-sync regenera todo lo que hay **entre** esos dos marcadores de
    comentario y **da error si faltan** (y `make check-sync` falla). Mantenelos exactamente
    como están escritos, incluso en un `CLAUDE.md` por lo demás minúsculo. Todo lo que está
    *fuera* de ellos es tuyo.

!!! note "Capacidad nativa de Claude Code"
    `CLAUDE.md` es memoria de proyecto nativa; también podrías dividirlo con imports `@path`.

!!! tip "Cómo lo aplica ml-python-base"
    El repo de referencia mantiene un único archivo y completa la región de sentinelas desde
    `.github/skills/`. Hacé crecer la prosa de gobernanza/automatización a medida que tu
    proyecto lo necesite — el [adapter completo](../reference-implementation/ml-python-base/adapters.md)
    muestra hasta dónde puede llegar.

## `SKILL.md` interno mínimo

Las skills son la forma de enseñarle a Claude una tarea repetible. Una skill interna es un
único archivo Markdown con frontmatter de dos campos y un cuerpo pequeño y estructurado:

```markdown
---
name: <skill_name>
description: <one line — when Claude should use this>
---

# Skill: <skill_name>

## Purpose
<what repeatable task this automates>

## Required Input
<what the caller must provide>

## Output Format
<what it returns>

## Execution Rules
1. <step>
2. <step>
3. Comply with `.github/architecture.md`, `.github/standards.md`.
```

!!! note "Capacidad nativa de Claude Code"
    El frontmatter de una skill también puede llevar campos como `allowed-tools` (restringir
    herramientas) y `context: fork` (ejecutar en un subagente aislado) — ver
    [Usar y modificar skills](use-and-modify-skills.md).

!!! tip "Cómo lo aplica ml-python-base"
    Las skills internas acá usan **frontmatter mínimo** (`name` + `description` únicamente) y
    siempre terminan sus `Execution Rules` con una línea de cumplimiento de gobernanza. Mantené
    las tuyas mínimas hasta que necesites más.

Ponés este archivo a trabajar — lo sincronizás y lo ves aparecer para Claude — en
[Creá tu primera skill](create-your-first-skill.md).

## Qué NO copiar

- **No** edites a mano archivos bajo `.claude/skills/` — ese layout es *generado* y tu
  cambio se va a sobreescribir.
- **No** edites a mano `.github/skills-external/<name>/SKILL.md` — las skills externas llegan
  vía instaladores y `make sync-skills`; las ediciones ahí se pierden en el próximo sync.

## Siguiente

- Aprendé a ejecutar y ajustar lo que ya existe → [Usar y modificar skills](use-and-modify-skills.md)
- Creá las tuyas → [Creá tu primera skill](create-your-first-skill.md)

## Documentación oficial

- [Claude Code Skills](https://docs.anthropic.com/en/docs/claude-code/skills)
- [Claude Code Memory](https://docs.anthropic.com/en/docs/claude-code/memory)

## Referencias

- [Referencia › Skills](../reference-implementation/ml-python-base/skills.md)
- [Referencia › Adapters](../reference-implementation/ml-python-base/adapters.md)
- [Patrones › Diseño de skills](../patterns/skill-design.md)
