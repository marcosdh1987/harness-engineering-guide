# Codex

Codex representa el caso de una herramienta orientada a ejecutar cambios de código con instrucciones persistentes, agentes especializados y pasos de validación claros. En [`ml-python-base`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0), Codex consume el harness mediante perfiles de agente, skills proyectados y reglas compartidas que reducen la ambigüedad antes de tocar el código.

## Rol en el workflow

Codex funciona mejor cuando el repositorio le da un contrato explícito: qué arquitectura preservar, qué comandos ejecutar, cuándo planificar, cuándo delegar y cómo cerrar una tarea con evidencia. En ese flujo, Codex puede actuar como implementador, reviewer, documentador o tester según el agente invocado.

El harness le aporta:

- instrucciones de trabajo persistentes;
- agentes con responsabilidades claras;
- skills reutilizables para tareas repetibles;
- gates de validación antes de considerar terminado un cambio.

## Qué lee Codex

| Artefacto | Qué aporta | Fuente |
|---|---|---|
| [`AGENTS.md`](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/AGENTS.md) | Perfil de subagentes, roles estándar y rutas de coordinación. | Fuente de verdad para Codex/OpenAI Agents |
| [`.codex/`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.codex/) | Configuración del adapter y hooks locales del workspace. | Generado |
| [`.codex/skills/`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.codex/skills/) | Skills gobernados expuestos para descubrimiento por Codex. | Generado desde `.github/skills/` |
| [`adapters/templates/agents.md.j2`](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/adapters/templates/agents.md.j2) | Plantilla que renderiza el perfil de agentes desde reglas compartidas. | Adapter |

`AGENTS.md` es el punto de entrada conceptual: explica cómo debe comportarse Codex dentro del repositorio. `.codex/` es la capa nativa que deja esa intención disponible para la herramienta.

## Archivos y carpetas que participan

Los agentes se definen de forma gobernada en [`.github/agents/`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.github/agents/). Los skills viven en `.github/skills/` y `.github/skills-external/`. El motor [`src/ml_python_base/skills_sync/`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/src/ml_python_base/skills_sync/) compila esas fuentes hacia los formatos que Codex puede usar.

La automatización mantiene el ciclo: `make sync-skills` regenera la proyección y `make check-sync` valida que `.codex/` no haya quedado desalineado.

## Fuente de verdad vs generado

Edita los agentes bajo `.github/agents/` y las reglas compartidas bajo `.github/*.md`. Trata `.codex/` y `.codex/skills/` como salida generada del adapter. Esta regla evita que una corrección hecha solo para Codex quede invisible para Claude Code, OpenCode, Copilot o Antigravity.

## Mini flujo de estudio

1. Lee [agentes](../reference-implementation/ml-python-base/agents.md) para entender los roles de `documenter`, `reviewer`, `tester`, `orchestrator` y otros perfiles.
2. Abre [`AGENTS.md`](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/AGENTS.md) y observa cómo esos roles se presentan a Codex.
3. Revisa [skills](../reference-implementation/ml-python-base/skills.md) y ubica la misma capacidad proyectada en `.codex/skills/`.
4. Usa [control de drift](../reference-implementation/ml-python-base/drift-control.md) para entender por qué la proyección debe ser verificable.

## Documentación oficial

- [Codex Docs](https://developers.openai.com/codex): documentación principal de Codex en OpenAI Developers.
- [Custom instructions with `AGENTS.md`](https://developers.openai.com/codex/guides/agents-md): cómo Codex lee `AGENTS.md` para cargar instrucciones del proyecto.
- [Agent Skills](https://developers.openai.com/codex/skills): cómo empaquetar instrucciones, recursos y scripts como skills.
- [Subagents](https://developers.openai.com/codex/subagents): uso de agentes especializados y workflows paralelos.

## Referencias

- [`ml-python-base` en GitHub](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0)
- [Agentes gobernados](../reference-implementation/ml-python-base/agents.md)
- [Inventario de artefactos](../reference-implementation/ml-python-base/inventory.md)
- [Proyección de adaptadores](../reference-implementation/ml-python-base/adapters.md)
