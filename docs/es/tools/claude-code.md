# Claude Code en el Harness de Ingeniería

## Rol en un Workflow de Desarrollo

Claude Code se integra en el flujo de trabajo como una herramienta interactiva en terminal capaz de ejecutar diagnósticos, explorar código de manera incremental y aplicar refactorizaciones. A diferencia de las herramientas que dependen puramente de prompts, Claude Code opera como un agente semi-autónomo guiado por un sistema operativo duradero (el Harness).

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
