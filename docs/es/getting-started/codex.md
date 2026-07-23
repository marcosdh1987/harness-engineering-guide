# Primeros pasos con Codex

No necesitás una rampa de entrada aparte para Codex. El harness es **agnóstico de la
herramienta**: la documentación de gobernanza y las skills bajo `.github/` son las mismas
que usa Claude Code — solo cambian el **archivo adapter** que Codex lee y la estructura
nativa. Aprendé el modelo compartido una vez y después aplicá este delta corto.

## La rampa de entrada es compartida

Hacé estas páginas del recorrido de Claude — son idénticas para Codex, porque operan sobre
la fuente gobernada (`.github/skills/`, `make sync-skills`), no sobre ninguna herramienta en
particular:

1. [Fundamentos de Claude Code](claude-code-basics.md) — el modelo mental (contexto duradero, plan vs. directo, sesiones).
2. [Configuración mínima](minimal-setup.md) — el archivo de gobernanza mínimo + `SKILL.md`.
3. [Usar y modificar skills](use-and-modify-skills.md) y [Creá tu primera skill](create-your-first-skill.md) — crear/usar skills es el mismo flujo.

!!! tip "Una sola sustitución"
    Donde esas páginas digan `CLAUDE.md`, tu adapter es **`AGENTS.md`**. Todo lo demás —
    la fuente `.github/skills/<name>.md`, `make sync-skills`, `make check-sync` y la región
    de sentinels `<!-- BEGIN/END GENERATED SKILLS -->` — es idéntico.

## Qué lee Codex

| Artefacto | Qué aporta |
|---|---|
| `AGENTS.md` | Perfil de integración de Codex y roles de agente (su equivalente a `CLAUDE.md`) |
| `.codex/skills/` | Skills gobernados proyectados para que Codex los descubra |
| `.codex/agents/` | Agentes gobernados como archivos `.toml` de subagentes de Codex |

Para la guía de estudio completa, mirá [Herramientas › Codex](../tools/codex.md).

## El delta específico de Codex

!!! note "Capacidad nativa de Codex"
    Codex carga instrucciones del proyecto desde `AGENTS.md`, empaqueta procedimientos como
    skills y soporta subagentes especializados — mirá la
    [documentación oficial](https://developers.openai.com/codex).

!!! tip "Cómo lo aplica ml-python-base"
    `AGENTS.md`, `.codex/skills/` y `.codex/agents/*.toml` se **generan** todos desde la
    misma fuente gobernada con `make sync-skills`. Editá `.github/skills/` y `.github/agents/`,
    nunca el output en `.codex/` — después re-sincronizá. `make check-sync` falla si `.codex/` diverge.

## Siguiente

- Creá una skill (flujo compartido) → [Creá tu primera skill](create-your-first-skill.md)
- El mapa de funciones → [Aprovechá más funciones](leverage-more.md)
- Profundidad en Codex → [Herramientas › Codex](../tools/codex.md)

## Documentación oficial

- [Codex Docs](https://developers.openai.com/codex)
- [Custom instructions with `AGENTS.md`](https://developers.openai.com/codex/guides/agents-md)
- [Agent Skills](https://developers.openai.com/codex/skills)
- [Subagents](https://developers.openai.com/codex/subagents)

## Referencias

- [Herramientas › Codex](../tools/codex.md)
- [Referencia › Agentes](../reference-implementation/ml-python-base/agents.md)
- [Referencia › Adaptadores](../reference-implementation/ml-python-base/adapters.md)
