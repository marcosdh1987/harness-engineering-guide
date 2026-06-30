# Hooks de sesión y guardrails

> [!NOTE]
> **Contenido generado**: Esta página se genera automáticamente a partir del snapshot de la plantilla.
> - **Commit de referencia**: [1fc65a8](https://github.com/marcosdh1987/ml-python-base/commit/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0) en la rama `main`
> - **Última sincronización**: `2026-06-30T12:49:58.403597Z`
> - **Artefactos de referencia**:
>   - [.claude/hooks/](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.claude/hooks/)
> *Nota: Este es un resumen de estudio e índice. La implementación y gobernanza autoritativas permanecen en el repositorio de origen.*
## Hooks como guardrails de calidad

Los hooks son scripts ejecutables que se activan automáticamente en puntos clave de la interacción. Integran verificaciones de validación externas, diagnósticos de estado y controles de conformidad del entorno directamente en el ciclo de sesión del agente.

### Archivos de hooks detectados

| Nombre del Hook | Ruta de destino | Propósito | Enlace |
|---|---|---|---|
| `stop_nudge.sh` | `.claude/hooks/stop_nudge.sh` | Advierte al desarrollador sobre drift o cambios sin confirmar cuando la sesion queda inactiva | [Link](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.claude/hooks/stop_nudge.sh) |
| `session_start.sh` | `.claude/hooks/session_start.sh` | Realiza comprobaciones de configuracion del entorno, estado de bloqueo local y drift sin confirmar | [Link](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.claude/hooks/session_start.sh) |

### Ajustes de configuración e integraciones

Si no se utilizan hooks de shell explícitos, los puntos de integración se definen en los archivos de configuración de las herramientas:
- **Claude Code**: `.claude/settings.json` controla las aprobaciones de ejecución de comandos, modificadores de prompt de sistema y rutas de herramientas.
- **OpenCode**: `opencode.json` define los permisos de herramientas, reglas de red y asignaciones de directorios de espacio de trabajo.
- **Antigravity**: `.agents/rules/GEMINI.md` vincula permisos de espacio de trabajo y orquesta la ejecución de agentes.
