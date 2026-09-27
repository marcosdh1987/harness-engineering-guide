# Tool Adapters Projection

> [!NOTE]
> **Generated content**: This page is automatically generated from the template snapshot.
> - **Reference Commit**: [a13a7ba](https://github.com/marcosdh1987/ml-python-base/commit/a13a7ba3a107d6810ee15f05851acd873cfdf316) on branch `main`
> - **Last Synced**: `2026-09-27T03:46:08.533808Z`
> - **Reference Artifacts**:
>   - [adapters/](https://github.com/marcosdh1987/ml-python-base/blob/a13a7ba3a107d6810ee15f05851acd873cfdf316/adapters/)
>   - [CLAUDE.md](https://github.com/marcosdh1987/ml-python-base/blob/a13a7ba3a107d6810ee15f05851acd873cfdf316/CLAUDE.md)
>   - [OPENCODE.md](https://github.com/marcosdh1987/ml-python-base/blob/a13a7ba3a107d6810ee15f05851acd873cfdf316/OPENCODE.md)
>   - [AGENTS.md](https://github.com/marcosdh1987/ml-python-base/blob/a13a7ba3a107d6810ee15f05851acd873cfdf316/AGENTS.md)
>   - [.github/copilot-instructions.md](https://github.com/marcosdh1987/ml-python-base/blob/a13a7ba3a107d6810ee15f05851acd873cfdf316/.github/copilot-instructions.md)
> *Note: This is a study summary and index. The authoritative implementation and governance remain in the source repository.*
## Adapters Composition

An **Adapter** acts as the glue layer between governed central rules and the tool-specific configuration formats.
Each adapter is composed of two distinct regions:
1. **Hand-written Governance Prose**: Explains project structure, rules, and general policies.
2. **Machine-Managed Skills Region**: Written dynamically by the synchronization engine between two unique markdown comments:
   ```markdown
   <!-- BEGIN GENERATED SKILLS (managed by skills_sync; do not edit) -->
   ...
   <!-- END GENERATED SKILLS -->
   ```

### Discovered Adapter Configurations

| Adapter / Template Name | Path | Target Tool | Link |
|---|---|---|---|
| `registry.toml` | `adapters/registry.toml` | Multiple | [Link](https://github.com/marcosdh1987/ml-python-base/blob/a13a7ba3a107d6810ee15f05851acd873cfdf316/adapters/registry.toml) |
| `template: agents.md.j2` | `adapters/templates/agents.md.j2` | Codex | [Link](https://github.com/marcosdh1987/ml-python-base/blob/a13a7ba3a107d6810ee15f05851acd873cfdf316/adapters/templates/agents.md.j2) |
| `template: skills_catalog.md.j2` | `adapters/templates/skills_catalog.md.j2` | Multiple | [Link](https://github.com/marcosdh1987/ml-python-base/blob/a13a7ba3a107d6810ee15f05851acd873cfdf316/adapters/templates/skills_catalog.md.j2) |
| `template: _skills_block.j2` | `adapters/templates/_skills_block.j2` | Multiple | [Link](https://github.com/marcosdh1987/ml-python-base/blob/a13a7ba3a107d6810ee15f05851acd873cfdf316/adapters/templates/_skills_block.j2) |
| `template: gemini.md.j2` | `adapters/templates/gemini.md.j2` | Antigravity | [Link](https://github.com/marcosdh1987/ml-python-base/blob/a13a7ba3a107d6810ee15f05851acd873cfdf316/adapters/templates/gemini.md.j2) |
| `template: claude.md.j2` | `adapters/templates/claude.md.j2` | Claude Code | [Link](https://github.com/marcosdh1987/ml-python-base/blob/a13a7ba3a107d6810ee15f05851acd873cfdf316/adapters/templates/claude.md.j2) |
| `template: copilot.md.j2` | `adapters/templates/copilot.md.j2` | GitHub Copilot | [Link](https://github.com/marcosdh1987/ml-python-base/blob/a13a7ba3a107d6810ee15f05851acd873cfdf316/adapters/templates/copilot.md.j2) |
| `template: opencode.md.j2` | `adapters/templates/opencode.md.j2` | OpenCode | [Link](https://github.com/marcosdh1987/ml-python-base/blob/a13a7ba3a107d6810ee15f05851acd873cfdf316/adapters/templates/opencode.md.j2) |
