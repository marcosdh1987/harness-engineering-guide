# Usar y modificar skills existentes

La mayor parte del valor llega antes de que jamás escribas una skill: aprendé a *ejecutar* las
que un repo ya trae, y a *modificarlas* de forma segura.

## Qué es una skill acá

Una skill empaqueta una tarea de ingeniería repetible con entrada explícita y salida
estructurada, de modo que Claude la realiza de forma consistente en lugar de improvisar. Para
el marco conceptual ver [Skills vs prompts](../concepts/skills-vs-prompts.md) y
[Patrones › Diseño de skills](../patterns/skill-design.md) — esta página es sobre la mecánica.

## Interna vs. externa vs. proyectada

Tres ubicaciones, y solo una es tuya para editar:

| Tipo | Ubicación | ¿Editar acá? | De dónde viene |
|---|---|---|---|
| Interna | `.github/skills/<name>.md` | **Sí** | Escrita a mano (fuente de verdad) |
| Externa | `.github/skills-external/<name>/SKILL.md` | No | Instaladores + `make sync-skills` |
| Proyectada | `.claude/skills/<name>/SKILL.md` | No (se sobreescribe) | Generada por el motor de sync (un symlink a la fuente) |

!!! warning "Editá la fuente, nunca la proyección"
    `.claude/skills/` es salida generada (symlinks de vuelta a la fuente). Si cambiás una
    copia proyectada, el cambio es frágil y se va a sobreescribir en el próximo sync — y no
    va a llegar a los otros adapters de herramientas. Editá siempre `.github/skills/<name>.md`.

## Usar una skill en una sesión

Claude descubre skills desde `.claude/skills/`, haciendo match de tu pedido contra el
`description` de cada skill. Para explorar lo que un repo realmente trae, leé el inventario en
vivo en [Referencia › Skills](../reference-implementation/ml-python-base/skills.md), después
pedile a Claude que realice una tarea que una skill cubre y dejá que la maneje.

## Modificar una skill interna de forma segura

1. Abrí la fuente: `.github/skills/<name>.md`.
2. Editá el `description` (su disparador) y/o el cuerpo (`Purpose` / `Required Input` /
   `Output Format` / `Execution Rules`).
3. Reproyectala con `make sync-skills` (ver [Creá tu primera skill](create-your-first-skill.md)
   para el flujo completo).
4. Confirmá que nada se desincronizó con `make check-sync`.

Nunca edites la copia proyectada ni una skill externa; ver
[Referencia › Control de drift](../reference-implementation/ml-python-base/drift-control.md)
para entender por qué el harness lo impone.

## `context: fork` y `allowed-tools` en la práctica

Dos campos nativos del frontmatter de skills vale la pena conocer temprano:

!!! note "Capacidad nativa de Claude Code"
    - **`context: fork`** ejecuta la skill en un subagente aislado, para que una tarea de alta
      salida (como explorar un codebase grande) no inunde el contexto de tu conversación principal.
    - **`allowed-tools`** restringe qué herramientas puede usar una skill — por ejemplo,
      solo lectura, para prevenir ediciones destructivas accidentales.

!!! tip "Cómo lo aplica ml-python-base"
    Las skills internas mantienen frontmatter mínimo, así que estos campos no están seteados en
    ellas por defecto. La página [Herramientas › Claude Code](../tools/claude-code.md) documenta
    `context: fork`, `allowed-tools` y `argument-hint` para cuando los quieras.

## Mini flujo de estudio

1. Leé el [inventario de skills](../reference-implementation/ml-python-base/skills.md) y elegí una.
2. Ejecutá una tarea que cubra; observá cómo estructura el trabajo.
3. Ajustá su `description` de fuente o una regla; `make sync-skills`; reejecutá.
4. Verificá con `make check-sync`. Después creá las tuyas → [Creá tu primera skill](create-your-first-skill.md).

## Documentación oficial

- [Claude Code Skills](https://docs.anthropic.com/en/docs/claude-code/skills)

## Referencias

- [Skills vs prompts](../concepts/skills-vs-prompts.md)
- [Patrones › Diseño de skills](../patterns/skill-design.md)
- [Referencia › Control de drift](../reference-implementation/ml-python-base/drift-control.md)
