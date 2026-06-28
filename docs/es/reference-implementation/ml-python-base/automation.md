# Flujos de automatización del Makefile

> [!NOTE]
> **Contenido generado**: Esta página se genera automáticamente a partir del snapshot de la plantilla.
> - **Commit de referencia**: [587ac29](https://github.com/marcosdh1987/ml-python-base/commit/587ac29d30cb50d5c307f41e942c14d3f0bba298) en la rama `main`
> - **Última sincronización**: `2026-06-28T00:52:06.059621Z`
> - **Artefactos de referencia**:
>   - [Makefile](https://github.com/marcosdh1987/ml-python-base/blob/587ac29d30cb50d5c307f41e942c14d3f0bba298/Makefile)
> *Nota: Este es un resumen de estudio e índice. La implementación y gobernanza autoritativas permanecen en el repositorio de origen.*
## Matriz de automatización de comandos

El repositorio de plantilla centraliza todos los comandos de desarrollo local y quality gates en un único `Makefile` utilizando `uv` para la gestión del entorno.

### Targets clave del Makefile

| Comando Target | Naturaleza de ejecución | Propósito principal / Acciones |
|---|---|---|
| `make install` | Local-Modificador | Instala `uv`, fija la versión de Python y construye el `.venv` local exactamente de acuerdo con `uv.lock`. |
| `make format` | Local-Modificador | Ejecuta automáticamente el formateo de Ruff y la ordenación de imports en `src/`, `tests/` y `scripts/`. |
| `make fix` | Local-Modificador | Aplica correcciones automáticas seguras del linter y formateo. |
| `make check` | Seguro para CI (Lectura) | **Gate de calidad de CI**: Sincroniza el `.venv` con `uv sync --locked --exact`, verifica el formato/lint de Ruff, ejecuta controles de seguridad (Bandit), realiza la comprobación de tipos de Mypy y ejecuta pruebas con cobertura. |
| `make sync-skills` | Local-Modificador | Activa el motor de sincronización centralizado para enlazar skills, proyectar agentes y reescribir las regiones de skills generadas. |
| `make check-sync` | Seguro para CI (Lectura) | **Gate de drift de CI**: Valida que ningún adaptador local, enlace de skill nativo o manifiesto se haya desviado de las fuentes gobernadas. |
| `make ci` | Seguro para CI (Lectura) | Ejecuta el pipeline completo de CI: `make check` seguido de `make check-sync`. |

### Flujos de trabajo locales modificadores vs seguros para CI (solo lectura)

- Los targets **Seguros para CI (solo lectura)** nunca modifican archivos en el directorio de trabajo (excepto la sincronización del entorno dentro de `.venv`). Verifican el estado y fallan rápidamente si fallan los controles.
- Los targets **Locales modificadores** escriben cambios, formateos o refactorizaciones en el disco. Solo deben ser ejecutados por desarrolladores de forma local.
