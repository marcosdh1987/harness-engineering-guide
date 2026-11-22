# Session Hooks & Guardrails

> [!NOTE]
> **Generated content**: This page is automatically generated from the template snapshot.
> - **Reference Commit**: [68ed781](https://github.com/marcosdh1987/ml-python-base/commit/68ed7816a2e312d6ec65167b30e3e24dc6d8c5f8) on branch `main`
> - **Last Synced**: `2026-11-22T05:11:00.364951Z`
> - **Reference Artifacts**:
>   - [.claude/hooks/](https://github.com/marcosdh1987/ml-python-base/blob/68ed7816a2e312d6ec65167b30e3e24dc6d8c5f8/.claude/hooks/)
> *Note: This is a study summary and index. The authoritative implementation and governance remain in the source repository.*
## Hooks as Quality Guardrails

Hooks are executable scripts triggered automatically at key interaction boundaries. They integrate external validation checks, state diagnostics, and environment compliance checks directly into the agent session loop.

### Discovered Hook Files

| Hook Name | Target Path | Purpose | Link |
|---|---|---|---|
| `session_start.sh` | `.claude/hooks/session_start.sh` | Runs checks on environment setup, local lock state, and checks for uncommitted drift | [Link](https://github.com/marcosdh1987/ml-python-base/blob/68ed7816a2e312d6ec65167b30e3e24dc6d8c5f8/.claude/hooks/session_start.sh) |
| `stop_nudge.sh` | `.claude/hooks/stop_nudge.sh` | Warns developer of drift or uncommitted changes when the session remains idle | [Link](https://github.com/marcosdh1987/ml-python-base/blob/68ed7816a2e312d6ec65167b30e3e24dc6d8c5f8/.claude/hooks/stop_nudge.sh) |

### Configuration Settings and Integrations

If explicit shell hooks are not utilized, the integration points are defined in the tool configuration files:
- **Claude Code**: `.claude/settings.json` controls command execution approvals, system prompt modifiers, and tool paths.
- **OpenCode**: `opencode.json` defines tool permissions, network rules, and workspace directory mappings.
- **Antigravity**: `.agents/rules/GEMINI.md` binds workspace permissions and orchestrates agent execution.
