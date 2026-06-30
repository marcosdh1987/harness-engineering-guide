# Autonomous Agents & Roles

> [!NOTE]
> **Generated content**: This page is automatically generated from the template snapshot.
> - **Reference Commit**: [1fc65a8](https://github.com/marcosdh1987/ml-python-base/commit/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0) on branch `main`
> - **Last Synced**: `2026-06-30T12:49:58.403597Z`
> - **Reference Artifacts**:
>   - [.github/agents/](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.github/agents/)
> *Note: This is a study summary and index. The authoritative implementation and governance remain in the source repository.*
## Governed Agent Roles

The reference implementation defines specialized agent personas under `.github/agents/`. The sync engine compiles and projects these definitions into the target subagent configurations (e.g. Claude Code Markdown subagents, Codex TOML config files, etc.).

### Discovered Agent Personas

| Agent Persona | Configuration Path | GitHub Link |
|---|---|---|
| `orchestrator` | `.github/agents/orchestrator.md` | [Link](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.github/agents/orchestrator.md) |
| `reviewer` | `.github/agents/reviewer.md` | [Link](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.github/agents/reviewer.md) |
| `documenter` | `.github/agents/documenter.md` | [Link](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.github/agents/documenter.md) |
| `tester` | `.github/agents/tester.md` | [Link](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.github/agents/tester.md) |
| `planner` | `.github/agents/planner.md` | [Link](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.github/agents/planner.md) |
| `implementer` | `.github/agents/implementer.md` | [Link](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.github/agents/implementer.md) |

### Agent Roles and Capabilities

Based on the metadata, the template maps the following roles:
- **orchestrator**: Coordinates tasks across specialized subagents and tracks implementation checklists.
- **planner**: Analyzes repository structure, parses requirements, and drafts implementation plans.
- **documenter**: Manages the generated documentation sites and ensures compliance with readability standards.
- **reviewer**: Conducts strict code quality reviews against architecture and domain boundaries.
- **tester**: Generates unit, integration, and E2E test suites based on changes.
- **implementer**: Handles actual code modifications and applies clean code patterns.
