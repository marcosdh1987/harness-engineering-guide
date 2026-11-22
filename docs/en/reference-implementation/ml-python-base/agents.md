# Autonomous Agents & Roles

> [!NOTE]
> **Generated content**: This page is automatically generated from the template snapshot.
> - **Reference Commit**: [68ed781](https://github.com/marcosdh1987/ml-python-base/commit/68ed7816a2e312d6ec65167b30e3e24dc6d8c5f8) on branch `main`
> - **Last Synced**: `2026-11-22T05:11:00.364951Z`
> - **Reference Artifacts**:
>   - [.github/agents/](https://github.com/marcosdh1987/ml-python-base/blob/68ed7816a2e312d6ec65167b30e3e24dc6d8c5f8/.github/agents/)
> *Note: This is a study summary and index. The authoritative implementation and governance remain in the source repository.*
## Governed Agent Roles

The reference implementation defines specialized agent personas under `.github/agents/`. The sync engine compiles and projects these definitions into the target subagent configurations (e.g. Claude Code Markdown subagents, Codex TOML config files, etc.).

### Discovered Agent Personas

| Agent Persona | Configuration Path | GitHub Link |
|---|---|---|
| `documenter` | `.github/agents/documenter.md` | [Link](https://github.com/marcosdh1987/ml-python-base/blob/68ed7816a2e312d6ec65167b30e3e24dc6d8c5f8/.github/agents/documenter.md) |
| `planner` | `.github/agents/planner.md` | [Link](https://github.com/marcosdh1987/ml-python-base/blob/68ed7816a2e312d6ec65167b30e3e24dc6d8c5f8/.github/agents/planner.md) |
| `tester` | `.github/agents/tester.md` | [Link](https://github.com/marcosdh1987/ml-python-base/blob/68ed7816a2e312d6ec65167b30e3e24dc6d8c5f8/.github/agents/tester.md) |
| `orchestrator` | `.github/agents/orchestrator.md` | [Link](https://github.com/marcosdh1987/ml-python-base/blob/68ed7816a2e312d6ec65167b30e3e24dc6d8c5f8/.github/agents/orchestrator.md) |
| `reviewer` | `.github/agents/reviewer.md` | [Link](https://github.com/marcosdh1987/ml-python-base/blob/68ed7816a2e312d6ec65167b30e3e24dc6d8c5f8/.github/agents/reviewer.md) |
| `implementer` | `.github/agents/implementer.md` | [Link](https://github.com/marcosdh1987/ml-python-base/blob/68ed7816a2e312d6ec65167b30e3e24dc6d8c5f8/.github/agents/implementer.md) |

### Agent Roles and Capabilities

Based on the metadata, the template maps the following roles:
- **orchestrator**: Coordinates tasks across specialized subagents and tracks implementation checklists.
- **planner**: Analyzes repository structure, parses requirements, and drafts implementation plans.
- **documenter**: Manages the generated documentation sites and ensures compliance with readability standards.
- **reviewer**: Conducts strict code quality reviews against architecture and domain boundaries.
- **tester**: Generates unit, integration, and E2E test suites based on changes.
- **implementer**: Handles actual code modifications and applies clean code patterns.
