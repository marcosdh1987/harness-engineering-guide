# Agentes autónomos y roles

> [!NOTE]
> **Contenido generado**: Esta página se genera automáticamente a partir del snapshot de la plantilla.
> - **Commit de referencia**: [a1f62c2](https://github.com/marcosdh1987/ml-python-base/commit/a1f62c29d9814d59f5e19a911913a0a43d46157b) en la rama `main`
> - **Última sincronización**: `2026-07-24T20:30:15.716502Z`
> - **Artefactos de referencia**:
>   - [.github/agents/](https://github.com/marcosdh1987/ml-python-base/blob/a1f62c29d9814d59f5e19a911913a0a43d46157b/.github/agents/)
> *Nota: Este es un resumen de estudio e índice. La implementación y gobernanza autoritativas permanecen en el repositorio de origen.*
## Roles de agentes gobernados

La implementación de referencia define personas de agentes especializados bajo `.github/agents/`. El motor de sincronización compila y proyecta estas definiciones en las configuraciones de subagentes objetivo (por ejemplo, subagentes Markdown de Claude Code, archivos de configuración TOML de Codex, etc.).

### Personas de agentes detectadas

| Persona del agente | Ruta de configuración | Enlace de GitHub |
|---|---|---|
| `orchestrator` | `.github/agents/orchestrator.md` | [Link](https://github.com/marcosdh1987/ml-python-base/blob/a1f62c29d9814d59f5e19a911913a0a43d46157b/.github/agents/orchestrator.md) |
| `reviewer` | `.github/agents/reviewer.md` | [Link](https://github.com/marcosdh1987/ml-python-base/blob/a1f62c29d9814d59f5e19a911913a0a43d46157b/.github/agents/reviewer.md) |
| `documenter` | `.github/agents/documenter.md` | [Link](https://github.com/marcosdh1987/ml-python-base/blob/a1f62c29d9814d59f5e19a911913a0a43d46157b/.github/agents/documenter.md) |
| `tester` | `.github/agents/tester.md` | [Link](https://github.com/marcosdh1987/ml-python-base/blob/a1f62c29d9814d59f5e19a911913a0a43d46157b/.github/agents/tester.md) |
| `planner` | `.github/agents/planner.md` | [Link](https://github.com/marcosdh1987/ml-python-base/blob/a1f62c29d9814d59f5e19a911913a0a43d46157b/.github/agents/planner.md) |
| `implementer` | `.github/agents/implementer.md` | [Link](https://github.com/marcosdh1987/ml-python-base/blob/a1f62c29d9814d59f5e19a911913a0a43d46157b/.github/agents/implementer.md) |

### Roles y capacidades de los agentes

Según los metadatos de la plantilla, se asignan los siguientes roles:
- **orchestrator**: Coordina tareas entre subagentes especializados y realiza el seguimiento de checklists de implementación.
- **planner**: Analiza la estructura del repositorio, interpreta requisitos y elabora planes de implementación.
- **documenter**: Gestiona los sitios de documentación generados y garantiza el cumplimiento de los estándares de legibilidad.
- **reviewer**: Realiza revisiones estrictas de calidad de código frente a los límites de arquitectura y dominio.
- **tester**: Genera suites de pruebas unitarias, de integración y E2E basadas en los cambios.
- **implementer**: Se encarga de las modificaciones de código reales y aplica patrones de código limpio.
