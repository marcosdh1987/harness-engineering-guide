# Aprovechá más: funciones nativas que todavía no usás

Claude Code es más que `CLAUDE.md` y skills. Esta página mapea las funciones nativas que vale
la pena conocer — y, siendo honestos, cuáles usa realmente la referencia `ml-python-base`
frente a las que deja de lado. Aprendé la herramienta; después elegí de forma deliberada para
tu propio proyecto.

## Capacidad nativa vs. cómo la aplica `ml-python-base`

| Capacidad nativa de Claude Code (docs / cert Architect) | Qué hace | Cómo la aplica `ml-python-base` |
|---|---|---|
| Memoria `CLAUDE.md` + imports `@path` | La memoria de proyecto anula la de usuario/global; los imports modulares mantienen el contexto liviano | Adapter único gobernado; **no** usa `@path` — dirige el contexto vía prosa de gobernanza |
| Reglas condicionales `.claude/rules/` (YAML + glob `paths:`) | Inyectar contexto solo al editar archivos que hacen match con un glob | **No usado** — cada skill reafirma su cumplimiento de gobernanza en lugar de inyección por glob |
| Skills personalizadas `.claude/skills/` | Procedimientos reutilizables y persistentes para el equipo | Usadas — pero **generadas** desde `.github/skills/`; nunca editadas a mano |
| `context: fork` | Aislar una tarea de alta salida en un subagente | Disponible vía frontmatter de skill; no seteado en las skills internas mínimas |
| `allowed-tools` | Restringir las herramientas de una skill por seguridad | Disponible; las skills internas mantienen frontmatter mínimo, así que no está seteado ahí |
| Plan Mode vs. ejecución directa | Plan obligatorio para cambio estructural grande; directo para arreglos pequeños | Codificado en el ciclo de trabajo `Ground → Plan → Delegate → Verify → Compound` |
| Headless `claude -p` / `--print`, `--output-format json` + `--json-schema` | Ejecuciones no interactivas para CI/CD con salida estructurada | CI ejecuta gates de solo lectura (`make check`, `make check-sync`) en lugar de llamadas al modelo |
| Code review con sesión limpia | Revisar en una sesión nueva para evitar el sesgo de confirmación hacia el propio trabajo de Claude | Las revisiones se ejecutan en una sesión separada y limpia |
| `fork_session` / `--resume` | Explorar caminos divergentes; retomar; avisarle a Claude cuando una persona editó archivos | Práctica de higiene de sesión |

!!! note "Leé esto como: capacidad vs. elección"
    Las columnas de la izquierda son lo que **Claude Code puede hacer** (según la
    [documentación oficial](https://docs.anthropic.com/en/docs/claude-code/overview) y la
    certificación Architect). La columna de la derecha es una **aplicación con criterio** de esas
    capacidades. Tu proyecto puede elegir distinto — está bien, siempre que sea
    deliberado.

## Dónde profundizar en cada una

- **Reglas e inyección de contexto** → [Conceptos › Arquitectura de reglas de IA](../concepts/ai-rules-architecture.md), [Patrones › Capas de reglas](../patterns/rule-layering.md), [Referencia › Reglas](../reference-implementation/ml-python-base/rules.md)
- **Gobernanza / skills / automatización / orquestación** → [Conceptos › Gobernanza, skills, automatización, orquestación](../concepts/governance-skills-automation-orchestration.md)
- **Mecánica de skills (`fork`, `allowed-tools`, toolbelt)** → [Herramientas › Claude Code](../tools/claude-code.md)
- **Ciclo de trabajo y plan mode** → [Referencia › Ciclo de trabajo](../reference-implementation/ml-python-base/working-loop.md)
- **CI / control de drift** → [Referencia › Automatización](../reference-implementation/ml-python-base/automation.md), [Referencia › Control de drift](../reference-implementation/ml-python-base/drift-control.md)

## Huecos honestos

Dos funciones nativas están intencionalmente **sin usar** por el template de referencia:

- **Inyección condicional por glob de `.claude/rules/`** — el template dirige el contexto por
  instrucción, no por reglas de file-glob.
- **Imports `@path` en `CLAUDE.md`** — el template mantiene un único archivo adapter.

Si tu proyecto quiere alguna de las dos, es una divergencia válida — solo documentá por qué, de
la misma forma en que esta guía documenta sus elecciones.

## Hacia dónde seguir

- [Ruta de aprendizaje](../learning-path.md) — la secuencia de estudio completa.
- [Labs](../labs/index.md) — practicá crear reglas, skills y validar cambios.

## Documentación oficial

- [Claude Code Overview](https://docs.anthropic.com/en/docs/claude-code/overview)
- [Claude Code Skills](https://docs.anthropic.com/en/docs/claude-code/skills)
- [Claude Code Memory](https://docs.anthropic.com/en/docs/claude-code/memory)
- [Claude Agent SDK Overview](https://code.claude.com/docs/en/agent-sdk/overview)

## Referencias

- [Herramientas › Claude Code](../tools/claude-code.md)
- [Conceptos › Arquitectura de reglas de IA](../concepts/ai-rules-architecture.md)
- [Implementación de referencia › ml-python-base](../reference-implementation/ml-python-base/index.md)
