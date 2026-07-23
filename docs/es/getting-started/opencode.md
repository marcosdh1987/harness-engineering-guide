# Primeros pasos con OpenCode

El harness es **agnóstico de la herramienta**: la documentación de gobernanza y las skills
bajo `.github/` son las mismas que usa Claude Code — solo cambian el **archivo adapter** que
OpenCode lee y la estructura nativa. Aprendé el modelo compartido una vez y después aplicá
este delta corto.

## La rampa de entrada es compartida

Hacé estas páginas del recorrido de Claude — son idénticas para OpenCode, porque operan sobre
la fuente gobernada (`.github/skills/`, `make sync-skills`), no sobre ninguna herramienta en
particular:

1. [Fundamentos de Claude Code](claude-code-basics.md) — el modelo mental (contexto duradero, plan vs. directo, sesiones).
2. [Configuración mínima](minimal-setup.md) — el archivo de gobernanza mínimo + `SKILL.md`.
3. [Usar y modificar skills](use-and-modify-skills.md) y [Creá tu primera skill](create-your-first-skill.md) — crear/usar skills es el mismo flujo.

!!! tip "Una sola sustitución"
    Donde esas páginas digan `CLAUDE.md`, tu adapter es **`OPENCODE.md`**. Todo lo demás —
    la fuente `.github/skills/<name>.md`, `make sync-skills`, `make check-sync` y la región
    de sentinels `<!-- BEGIN/END GENERATED SKILLS -->` — es idéntico.

## Qué lee OpenCode

| Artefacto | Qué aporta |
|---|---|
| `OPENCODE.md` | Perfil de integración de OpenCode, reglas de uso de herramientas y política de seguridad (su equivalente a `CLAUDE.md`) |
| `.opencode/skills/` | Skills gobernados proyectados para que OpenCode los descubra |
| `.opencode/agents/` | Agentes gobernados en el formato nativo de OpenCode |
| `opencode.jsonc` | Configuración de workspace/modelo de OpenCode |

Para la guía de estudio completa, mirá [Herramientas › OpenCode](../tools/opencode.md).

## El delta específico de OpenCode

!!! note "Capacidad nativa de OpenCode"
    OpenCode lee instrucciones persistentes, descubre skills proyectadas en su estructura
    nativa y se configura vía JSON/JSONC — mirá la
    [documentación oficial](https://opencode.ai/docs/).

!!! tip "Cómo lo aplica ml-python-base"
    `OPENCODE.md`, `.opencode/skills/` y `.opencode/agents/` se **generan** todos desde la
    misma fuente gobernada con `make sync-skills`. Editá `.github/skills/` y `.github/agents/`,
    nunca el output en `.opencode/` — después re-sincronizá. `make check-sync` falla si `.opencode/`
    diverge.

## Siguiente

- Creá una skill (flujo compartido) → [Creá tu primera skill](create-your-first-skill.md)
- El mapa de funciones → [Aprovechá más funciones](leverage-more.md)
- Profundidad en OpenCode → [Herramientas › OpenCode](../tools/opencode.md)

## Documentación oficial

- [OpenCode Docs](https://opencode.ai/docs/)
- [OpenCode Config](https://opencode.ai/docs/config/)

## Referencias

- [Herramientas › OpenCode](../tools/opencode.md)
- [Referencia › Skills](../reference-implementation/ml-python-base/skills.md)
- [Referencia › Adaptadores](../reference-implementation/ml-python-base/adapters.md)
