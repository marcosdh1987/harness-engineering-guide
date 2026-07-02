# Claude Code en el Harness de Ingeniería

## Rol en un Workflow de Desarrollo

Claude Code se integra en el flujo de trabajo como una herramienta interactiva en terminal capaz de ejecutar diagnósticos, explorar código de manera incremental y aplicar refactorizaciones. A diferencia de las herramientas que dependen puramente de prompts, Claude Code opera como un agente semi-autónomo guiado por un sistema operativo duradero: el harness.

En [`ml-python-base`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0), Claude Code es el ejemplo más completo de herramienta con instrucciones persistentes, comandos, hooks y skills nativos. La página sirve para estudiar cómo una herramienta con mucha autonomía puede seguir reglas compartidas sin duplicarlas a mano.

## Qué lee Claude Code

| Artefacto | Qué aporta | Fuente |
|---|---|---|
| [`CLAUDE.md`](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/CLAUDE.md) | Perfil de integración, políticas de comandos, toolbelt y ciclo de trabajo. | Fuente de verdad renderizada para Claude Code |
| [`.claude/`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.claude/) | Configuración del workspace, comandos, hooks y skills nativos. | Generado y configurado |
| [`.claude/skills/`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.claude/skills/) | Skills gobernados y externos expuestos como enlaces para Claude. | Generado desde `.github/skills/` |
| [`.claude/hooks/`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.claude/hooks/) | Recordatorios de sesión y nudges no bloqueantes. | Configuración del adapter |
| [`adapters/templates/claude.md.j2`](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/adapters/templates/claude.md.j2) | Plantilla que renderiza instrucciones compartidas para Claude Code. | Adapter |

`CLAUDE.md` es el punto de entrada humano y operativo. `.claude/` contiene la forma nativa que Claude Code usa para comandos, hooks y discovery de skills.

---

## El Claude Toolbelt (Cinturón de Herramientas)

El **Claude Toolbelt** es la capa de ejecución práctica que permite a Claude obtener respuestas a preguntas rutinarias del entorno o del repositorio antes de recurrir a preguntar al desarrollador.

### 1. Servidores MCP Integrados
El archivo `.mcp.json` en la raíz define herramientas de contexto estructurado:
- `context7`: Permite consultar documentación actualizada de librerías, APIs de dependencias y notas de migración.
- `git`: Proporciona una interfaz estructurada para inspeccionar el estado de archivos, diferencias (diffs) y el historial.

### 2. CLIs Recomendadas
Claude tiene acceso a herramientas de terminal para resolver tareas directamente:
- **Gestión de Entorno**: `uv` y `make`.
- **Integraciones de Repositorio**: `git` y `gh` (GitHub CLI).
- **Procesamiento de Datos**: `curl` y `jq`.
- **Herramientas de Diagnóstico**: `opencode` y `claude`.

### 3. Regla de Selección de Herramientas (Tool Choice Rule)
Se instruye a Claude a utilizar la herramienta más ligera disponible que pueda conseguir el dato requerido:
1. Usar targets de `make` y comandos locales del proyecto para operaciones repetibles.
2. Usar **MCP** cuando el contexto estructurado sea superior a la salida plana del terminal.
3. Usar **CLIs nativas** (`gh`, `docker`, `aws`, `gcloud`, etc.) para interactuar con servicios externos autenticados localmente.
4. **Preguntar al desarrollador** únicamente si la información no está disponible mediante herramientas, requiere una decisión de producto o se necesitan credenciales no configuradas.

### 4. Diagnóstico Automático: `make toolbelt-doctor`
Ejecuta el script `scripts/toolbelt_doctor.py` para validar la disponibilidad de las herramientas principales y opcionales. El doctor comprueba si existen variables de entorno o si los servicios locales se ejecutan en sus puertos por defecto de forma no invasiva:
- **LiteLLM / AI Gateway** (por defecto en puerto `4000/v1`)
- **Langfuse** (por defecto en puerto `3000`)
- **MLflow** (por defecto en puerto `5000`)
- **Ollama** (por defecto en puerto `11434/v1`)
- **LM Studio** (por defecto en puerto `1234/v1`)

---

## Hooks de Sesión y Nudges

Los hooks actúan como recordatorios o gates no bloqueantes en la sesión para guiar el flujo agéntico sin obstaculizar la agilidad del desarrollador.

- **SessionStart (`session_start.sh`)**: Inyecta en el contexto de la conversación el recordatorio del ciclo de trabajo del repositorio (`Ground -> Plan -> Delegate -> Verify -> Compound`) y las rutas de la memoria del proyecto al iniciar la sesión.
- **Stop/Idle (`stop_nudge.sh`)**: Cuando finaliza el turno del agente y existen cambios sin confirmar (`uncommitted changes`) en `src/` o `tests/`, imprime una alerta amable recordando que debe ejecutar las pruebas con `/verify` (`make check`), actualizar la documentación local y registrar aprendizajes en `memory/` antes de cerrar.

---

## Configuración de Skills y Comandos Personalizados

Las herramientas gobernadas (skills) se exponen en `.claude/skills/` y se registran usando frontmatter en sus archivos `SKILL.md` para modificar el comportamiento de Claude:

- **`context: fork`**: Ejecuta la skill en un subagente con un contexto aislado. Esto evita que los outputs verbose de análisis de código o exploraciones largas saturen el contexto de la conversación principal del desarrollador.
- **`allowed-tools`**: Limita de forma estricta las herramientas a las que la skill tiene acceso (ej. restringir a operaciones de solo lectura para evitar ediciones destructivas accidentales).
- **`argument-hint`**: Proporciona descripciones e indicaciones interactivas de los parámetros de la skill cuando se invoca desde la terminal.

## Archivos y carpetas que participan

Los skills y reglas nacen en la capa gobernada: `.github/skills/`, `.github/skills-external/`, `.github/agents/` y `.github/*.md`. El motor [`src/ml_python_base/skills_sync/`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/src/ml_python_base/skills_sync/) proyecta esa intención hacia `.claude/skills/` y hacia las regiones generadas de `CLAUDE.md`.

`make sync-skills` actualiza las proyecciones; `make check-sync` valida que los enlaces, bloques generados y manifests no hayan quedado fuera de sincronía. La herramienta puede tener affordances propios, pero el contenido gobernado sigue viviendo en el mismo lugar que para OpenCode, Codex, Copilot y Antigravity.

## Fuente de verdad vs generado

Edita las reglas compartidas y skills en `.github/` y los templates en `adapters/`. Trata `.claude/skills/` como salida nativa. Si se corrige una instrucción solo dentro de una copia proyectada, el cambio queda frágil y no se propaga al resto del harness.

## Mini flujo de estudio

1. Lee el [inventario](../reference-implementation/ml-python-base/inventory.md) y ubica `CLAUDE.md`, `.claude/`, `.claude/skills/` y `.claude/hooks/`.
2. Revisa [hooks](../reference-implementation/ml-python-base/hooks.md) para entender cómo los nudges ayudan sin bloquear.
3. Lee [skills](../reference-implementation/ml-python-base/skills.md) y compara las fuentes gobernadas con los enlaces en `.claude/skills/`.
4. Cierra con [adapters](../reference-implementation/ml-python-base/adapters.md) y [control de drift](../reference-implementation/ml-python-base/drift-control.md).

## Documentación oficial

- [Claude Code Overview](https://docs.anthropic.com/en/docs/claude-code/overview): visión general de Claude Code como herramienta agéntica para leer, editar y ejecutar código.
- [Claude Code Skills](https://docs.anthropic.com/en/docs/claude-code/skills): guía oficial para crear, administrar y compartir skills en Claude Code.
- [Claude Code Memory](https://docs.anthropic.com/en/docs/claude-code/memory): uso de `CLAUDE.md` como memoria e instrucciones persistentes del proyecto.

## Referencias

- [`ml-python-base` en GitHub](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0)
- [Inventario de artefactos](../reference-implementation/ml-python-base/inventory.md)
- [Hooks](../reference-implementation/ml-python-base/hooks.md)
- [Proyección de adaptadores](../reference-implementation/ml-python-base/adapters.md)
