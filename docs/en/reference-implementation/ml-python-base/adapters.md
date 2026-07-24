# Tool Adapters Projection

> [!NOTE]
> **Generated content**: This page is automatically generated from the template snapshot.
> - **Reference Commit**: [a1f62c2](https://github.com/marcosdh1987/ml-python-base/commit/a1f62c29d9814d59f5e19a911913a0a43d46157b) on branch `main`
> - **Last Synced**: `2026-07-24T20:30:15.716502Z`
> - **Reference Artifacts**:
>   - [adapters/](https://github.com/marcosdh1987/ml-python-base/blob/a1f62c29d9814d59f5e19a911913a0a43d46157b/adapters/)
>   - [CLAUDE.md](https://github.com/marcosdh1987/ml-python-base/blob/a1f62c29d9814d59f5e19a911913a0a43d46157b/CLAUDE.md)
>   - [OPENCODE.md](https://github.com/marcosdh1987/ml-python-base/blob/a1f62c29d9814d59f5e19a911913a0a43d46157b/OPENCODE.md)
>   - [AGENTS.md](https://github.com/marcosdh1987/ml-python-base/blob/a1f62c29d9814d59f5e19a911913a0a43d46157b/AGENTS.md)
>   - [.github/copilot-instructions.md](https://github.com/marcosdh1987/ml-python-base/blob/a1f62c29d9814d59f5e19a911913a0a43d46157b/.github/copilot-instructions.md)
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
| `registry.toml` | `adapters/registry.toml` | Multiple | [Link](https://github.com/marcosdh1987/ml-python-base/blob/a1f62c29d9814d59f5e19a911913a0a43d46157b/adapters/registry.toml) |
| `template: claude.md.j2` | `adapters/templates/claude.md.j2` | Claude Code | [Link](https://github.com/marcosdh1987/ml-python-base/blob/a1f62c29d9814d59f5e19a911913a0a43d46157b/adapters/templates/claude.md.j2) |
| `template: opencode.md.j2` | `adapters/templates/opencode.md.j2` | OpenCode | [Link](https://github.com/marcosdh1987/ml-python-base/blob/a1f62c29d9814d59f5e19a911913a0a43d46157b/adapters/templates/opencode.md.j2) |
| `template: _skills_block.j2` | `adapters/templates/_skills_block.j2` | Multiple | [Link](https://github.com/marcosdh1987/ml-python-base/blob/a1f62c29d9814d59f5e19a911913a0a43d46157b/adapters/templates/_skills_block.j2) |
| `template: agents.md.j2` | `adapters/templates/agents.md.j2` | Codex | [Link](https://github.com/marcosdh1987/ml-python-base/blob/a1f62c29d9814d59f5e19a911913a0a43d46157b/adapters/templates/agents.md.j2) |
| `template: gemini.md.j2` | `adapters/templates/gemini.md.j2` | Antigravity | [Link](https://github.com/marcosdh1987/ml-python-base/blob/a1f62c29d9814d59f5e19a911913a0a43d46157b/adapters/templates/gemini.md.j2) |
| `template: copilot.md.j2` | `adapters/templates/copilot.md.j2` | GitHub Copilot | [Link](https://github.com/marcosdh1987/ml-python-base/blob/a1f62c29d9814d59f5e19a911913a0a43d46157b/adapters/templates/copilot.md.j2) |
