# Proyección de adaptadores de herramientas

> [!NOTE]
> **Contenido generado**: Esta página se genera automáticamente a partir del snapshot de la plantilla.
> - **Commit de referencia**: [1fc65a8](https://github.com/marcosdh1987/ml-python-base/commit/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0) en la rama `main`
> - **Última sincronización**: `2026-06-30T13:26:01.964630Z`
> - **Artefactos de referencia**:
>   - [adapters/](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/adapters/)
>   - [CLAUDE.md](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/CLAUDE.md)
>   - [OPENCODE.md](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/OPENCODE.md)
>   - [AGENTS.md](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/AGENTS.md)
>   - [.github/copilot-instructions.md](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.github/copilot-instructions.md)
> *Nota: Este es un resumen de estudio e índice. La implementación y gobernanza autoritativas permanecen en el repositorio de origen.*
## Composición de adaptadores

Un **Adapter** actúa como la capa de unión entre las reglas centrales gobernadas y los formatos de configuración específicos de cada herramienta.
Cada adaptador se compone de dos regiones distintas:
1. **Gobernanza escrita a mano**: Explica la estructura del proyecto, las reglas y las políticas generales.
2. **Región de skills gestionada por máquina**: Escrita dinámicamente por el motor de sincronización entre dos comentarios markdown únicos:
   ```markdown
   <!-- BEGIN GENERATED SKILLS (managed by skills_sync; do not edit) -->
   ...
   <!-- END GENERATED SKILLS -->
   ```

### Configuraciones de adaptadores detectadas

| Nombre del adaptador / plantilla | Ruta | Herramienta de destino | Enlace |
|---|---|---|---|
| `registry.toml` | `adapters/registry.toml` | Multiple | [Link](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/adapters/registry.toml) |
| `template: claude.md.j2` | `adapters/templates/claude.md.j2` | Claude Code | [Link](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/adapters/templates/claude.md.j2) |
| `template: opencode.md.j2` | `adapters/templates/opencode.md.j2` | OpenCode | [Link](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/adapters/templates/opencode.md.j2) |
| `template: _skills_block.j2` | `adapters/templates/_skills_block.j2` | Multiple | [Link](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/adapters/templates/_skills_block.j2) |
| `template: agents.md.j2` | `adapters/templates/agents.md.j2` | Codex | [Link](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/adapters/templates/agents.md.j2) |
| `template: gemini.md.j2` | `adapters/templates/gemini.md.j2` | Antigravity | [Link](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/adapters/templates/gemini.md.j2) |
| `template: copilot.md.j2` | `adapters/templates/copilot.md.j2` | GitHub Copilot | [Link](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/adapters/templates/copilot.md.j2) |
