# Hooks de sesión y guardrails

> [!NOTE]
> **Contenido generado**: Esta página se genera automáticamente a partir del snapshot de la plantilla.
> - **Commit de referencia**: [587ac29](https://github.com/marcosdh1987/ml-python-base/commit/587ac29d30cb50d5c307f41e942c14d3f0bba298) en la rama `main`
> - **Última sincronización**: `2026-06-24T17:45:44.341172Z`
> - **Artefactos de referencia**:
>   - [.claude/hooks/](https://github.com/marcosdh1987/ml-python-base/blob/587ac29d30cb50d5c307f41e942c14d3f0bba298/.claude/hooks/)
> *Nota: Este es un resumen de estudio e índice. La implementación y gobernanza autoritativas permanecen en el repositorio de origen.*
## Hooks como guardrails de calidad

Los hooks son scripts ejecutables que se activan automáticamente en puntos clave de la interacción. Integran verificaciones de validación externas, diagnósticos de estado y controles de conformidad del entorno directamente en el ciclo de sesión del agente.

### Archivos de hooks detectados

| Nombre del Hook | Ruta de destino | Propósito | Enlace |
|---|---|---|---|
| `stop_nudge.sh` | `.claude/hooks/stop_nudge.sh` | Warns developer of drift or uncommitted changes when the session remains idle | [Link](https://github.com/marcosdh1987/ml-python-base/blob/587ac29d30cb50d5c307f41e942c14d3f0bba298/.claude/hooks/stop_nudge.sh) |
| `session_start.sh` | `.claude/hooks/session_start.sh` | Runs checks on environment setup, local lock state, and checks for uncommitted drift | [Link](https://github.com/marcosdh1987/ml-python-base/blob/587ac29d30cb50d5c307f41e942c14d3f0bba298/.claude/hooks/session_start.sh) |

### Ajustes de configuración e integraciones

Si no se utilizan hooks de shell explícitos, los puntos de integración se definen en los archivos de configuración de las herramientas:
- **Claude Code**: `.claude/settings.json` controla las aprobaciones de ejecución de comandos, modificadores de prompt de sistema y rutas de herramientas.
- **OpenCode**: `opencode.json` define los permisos de herramientas, reglas de red y asignaciones de directorios de espacio de trabajo.
- **Antigravity**: `.agents/rules/GEMINI.md` vincula permisos de espacio de trabajo y orquesta la ejecución de agentes.
