# Autonomous Agents & Roles

> [!NOTE]
> **Generated content**: This page is automatically generated from the template snapshot.
> - **Reference Commit**: [587ac29](https://github.com/marcosdh1987/ml-python-base/commit/587ac29d30cb50d5c307f41e942c14d3f0bba298) on branch `main`
> - **Last Synced**: `2026-06-28T00:52:06.059621Z`
> - **Reference Artifacts**:
>   - [.github/agents/](https://github.com/marcosdh1987/ml-python-base/blob/587ac29d30cb50d5c307f41e942c14d3f0bba298/.github/agents/)
> *Note: This is a study summary and index. The authoritative implementation and governance remain in the source repository.*
## Governed Agent Roles

The reference implementation defines specialized agent personas under `.github/agents/`. The sync engine compiles and projects these definitions into the target subagent configurations (e.g. Claude Code Markdown subagents, Codex TOML config files, etc.).

### Discovered Agent Personas

| Agent Persona | Configuration Path | GitHub Link |
|---|---|---|
| `planner` | `.github/agents/planner.md` | [Link](https://github.com/marcosdh1987/ml-python-base/blob/587ac29d30cb50d5c307f41e942c14d3f0bba298/.github/agents/planner.md) |
| `documenter` | `.github/agents/documenter.md` | [Link](https://github.com/marcosdh1987/ml-python-base/blob/587ac29d30cb50d5c307f41e942c14d3f0bba298/.github/agents/documenter.md) |
| `tester` | `.github/agents/tester.md` | [Link](https://github.com/marcosdh1987/ml-python-base/blob/587ac29d30cb50d5c307f41e942c14d3f0bba298/.github/agents/tester.md) |
| `orchestrator` | `.github/agents/orchestrator.md` | [Link](https://github.com/marcosdh1987/ml-python-base/blob/587ac29d30cb50d5c307f41e942c14d3f0bba298/.github/agents/orchestrator.md) |
| `implementer` | `.github/agents/implementer.md` | [Link](https://github.com/marcosdh1987/ml-python-base/blob/587ac29d30cb50d5c307f41e942c14d3f0bba298/.github/agents/implementer.md) |
| `reviewer` | `.github/agents/reviewer.md` | [Link](https://github.com/marcosdh1987/ml-python-base/blob/587ac29d30cb50d5c307f41e942c14d3f0bba298/.github/agents/reviewer.md) |

### Agent Roles and Capabilities

Based on the metadata, the template maps the following roles:
- **orchestrator**: Coordinates tasks across specialized subagents and tracks implementation checklists.
- **planner**: Analyzes repository structure, parses requirements, and drafts implementation plans.
- **documenter**: Manages the generated documentation sites and ensures compliance with readability standards.
- **reviewer**: Conducts strict code quality reviews against architecture and domain boundaries.
- **tester**: Generates unit, integration, and E2E test suites based on changes.
- **implementer**: Handles actual code modifications and applies clean code patterns.
