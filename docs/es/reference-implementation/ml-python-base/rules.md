# Sistema de reglas y gobernanza

> [!NOTE]
> **Contenido generado**: Esta página se genera automáticamente a partir del snapshot de la plantilla.
> - **Commit de referencia**: [1fc65a8](https://github.com/marcosdh1987/ml-python-base/commit/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0) en la rama `main`
> - **Última sincronización**: `2026-06-30T13:26:01.964630Z`
> - **Artefactos de referencia**:
>   - [.github/architecture.md](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.github/architecture.md)
>   - [.github/standards.md](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.github/standards.md)
>   - [.github/domain-boundaries.md](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.github/domain-boundaries.md)
>   - [.github/automation.md](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.github/automation.md)
>   - [.github/orchestration.md](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.github/orchestration.md)
> *Nota: Este es un resumen de estudio e índice. La implementación y gobernanza autoritativas permanecen en el repositorio de origen.*
## Gobernanza estructurada

La implementación de referencia estructura la gobernanza en cinco archivos de reglas dedicados ubicados en `.github/`. Estos establecen los quality gates de Nivel 3 (Automatización) y Nivel 4 (Orquestación) que las herramientas de codificación de IA deben cumplir.

### 1. Gobernanza de arquitectura (`.github/architecture.md`)
Define el esquema arquitectónico y los límites de los módulos para evitar desviaciones en el diseño.
- **Principio clave**: Aplica el Principio de Responsabilidad Única (SRP) y separa la lógica de negocio de la infraestructura.
- **Capas preferidas**: Impone un esquema de Arquitectura Limpia (Clean Architecture):
  1. **Domain layer**: entidades, objetos de valor y reglas principales (no debe depender de la infraestructura).
  2. **Application layer**: casos de uso y orquestación.
  3. **Infrastructure layer**: frameworks, adaptadores de base de datos, proveedores externos, APIs.

### 2. Estándares de ingeniería (`.github/standards.md`)
Detalla pautas de desarrollo, políticas de idioma, rutas de ejecución de herramientas y checklists previas a la finalización.
- **Política de idioma**: El idioma de interacción se adapta al usuario, pero todos los artefactos de código (identificadores, docstrings, comentarios, documentación técnica generada) **deben permanecer en inglés**.
- **Política de comandos de herramientas**: Prioriza los targets del `Makefile`. Nunca ejecute `pip install` directamente; use los flujos de `uv`.
- **Checklist de validación**:
  1. Los artefactos de código están en inglés.
  2. Se ejecutaron los controles de calidad correspondientes (`make check` o pruebas específicas).
  3. Los flujos de datos respetan los límites de zona.
  4. Los cambios en la implementación incluyen la actualización de la documentación en `docs/`.

### 3. Límites de dominio (`.github/domain-boundaries.md`)
Define las zonas del repositorio y los límites de aislamiento de datos para restringir el alcance de generación de los modelos.
- **Zonas del repositorio**: `src/` (código de producción), `tests/` (pruebas), `notebooks/` (prototipos).
- **Zonas de datos**: Impone datos de origen inmutables de solo lectura en `data/raw/` y transformaciones solo en `data/processed/`.

### 4. Política de automatización (`.github/automation.md`)
Define el cumplimiento de Nivel 3 para que la calidad se verifique mediante programación y no dependa del comportamiento del modelo.
- **La CI es de solo lectura**: La CI solo verifica y nunca modifica el árbol de trabajo. Comandos como `make format` son estrictamente locales.
- **Guardia de drift**: `make check` ejecuta `uv sync --locked --exact` para alinear el entorno exactamente con el archivo de bloqueo, evitando fugas de dependencias no declaradas.

### 5. Política de orquestación (`.github/orchestration.md`)
Establece pautas de ejecución de flujos de trabajo de Nivel 4 para tareas de programación complejas.
- **Planificar primero**: Requiere elaborar un plan de implementación explícito antes de escribir código.
- **Revisión de diffs**: Exige revisiones del diff de Git por parte del modelo y del desarrollador antes de finalizar para eliminar violaciones de límites.
- **Ruta de orquestación**: Prioriza la ejecución de skills internos sobre la generación genérica por parte de los modelos.
