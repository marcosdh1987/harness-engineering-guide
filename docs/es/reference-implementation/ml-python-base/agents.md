# Agentes autónomos y roles

> [!NOTE]
> **Contenido generado**: Esta página se genera automáticamente a partir del snapshot de la plantilla.
> - **Commit de referencia**: [24cdd59](https://github.com/marcosdh1987/ml-python-base/commit/24cdd59e449e5662ba86234d1fab4b6dcf5f8947) en la rama `main`
> - **Última sincronización**: `2026-08-02T00:37:57.887685Z`
> - **Artefactos de referencia**:
>   - [.github/agents/](https://github.com/marcosdh1987/ml-python-base/blob/24cdd59e449e5662ba86234d1fab4b6dcf5f8947/.github/agents/)
> *Nota: Este es un resumen de estudio e índice. La implementación y gobernanza autoritativas permanecen en el repositorio de origen.*
## Roles de agentes gobernados

La implementación de referencia define personas de agentes especializados bajo `.github/agents/`. El motor de sincronización compila y proyecta estas definiciones en las configuraciones de subagentes objetivo (por ejemplo, subagentes Markdown de Claude Code, archivos de configuración TOML de Codex, etc.).

### Personas de agentes detectadas

| Persona del agente | Ruta de configuración | Enlace de GitHub |
|---|---|---|
| `documenter` | `.github/agents/documenter.md` | [Link](https://github.com/marcosdh1987/ml-python-base/blob/24cdd59e449e5662ba86234d1fab4b6dcf5f8947/.github/agents/documenter.md) |
| `reviewer` | `.github/agents/reviewer.md` | [Link](https://github.com/marcosdh1987/ml-python-base/blob/24cdd59e449e5662ba86234d1fab4b6dcf5f8947/.github/agents/reviewer.md) |
| `orchestrator` | `.github/agents/orchestrator.md` | [Link](https://github.com/marcosdh1987/ml-python-base/blob/24cdd59e449e5662ba86234d1fab4b6dcf5f8947/.github/agents/orchestrator.md) |
| `planner` | `.github/agents/planner.md` | [Link](https://github.com/marcosdh1987/ml-python-base/blob/24cdd59e449e5662ba86234d1fab4b6dcf5f8947/.github/agents/planner.md) |
| `tester` | `.github/agents/tester.md` | [Link](https://github.com/marcosdh1987/ml-python-base/blob/24cdd59e449e5662ba86234d1fab4b6dcf5f8947/.github/agents/tester.md) |
| `implementer` | `.github/agents/implementer.md` | [Link](https://github.com/marcosdh1987/ml-python-base/blob/24cdd59e449e5662ba86234d1fab4b6dcf5f8947/.github/agents/implementer.md) |

### Roles y capacidades de los agentes

Según los metadatos de la plantilla, se asignan los siguientes roles:
- **orchestrator**: Coordina tareas entre subagentes especializados y realiza el seguimiento de checklists de implementación.
- **planner**: Analiza la estructura del repositorio, interpreta requisitos y elabora planes de implementación.
- **documenter**: Gestiona los sitios de documentación generados y garantiza el cumplimiento de los estándares de legibilidad.
- **reviewer**: Realiza revisiones estrictas de calidad de código frente a los límites de arquitectura y dominio.
- **tester**: Genera suites de pruebas unitarias, de integración y E2E basadas en los cambios.
- **implementer**: Se encarga de las modificaciones de código reales y aplica patrones de código limpio.
