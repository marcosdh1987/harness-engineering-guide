# Session Hooks & Guardrails

> [!NOTE]
> **Generated content**: This page is automatically generated from the template snapshot.
> - **Reference Commit**: [1fc65a8](https://github.com/marcosdh1987/ml-python-base/commit/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0) on branch `main`
> - **Last Synced**: `2026-06-30T12:49:58.403597Z`
> - **Reference Artifacts**:
>   - [.claude/hooks/](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.claude/hooks/)
> *Note: This is a study summary and index. The authoritative implementation and governance remain in the source repository.*
## Hooks as Quality Guardrails

Hooks are executable scripts triggered automatically at key interaction boundaries. They integrate external validation checks, state diagnostics, and environment compliance checks directly into the agent session loop.

### Discovered Hook Files

| Hook Name | Target Path | Purpose | Link |
|---|---|---|---|
| `stop_nudge.sh` | `.claude/hooks/stop_nudge.sh` | Warns developer of drift or uncommitted changes when the session remains idle | [Link](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.claude/hooks/stop_nudge.sh) |
| `session_start.sh` | `.claude/hooks/session_start.sh` | Runs checks on environment setup, local lock state, and checks for uncommitted drift | [Link](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.claude/hooks/session_start.sh) |

### Configuration Settings and Integrations

If explicit shell hooks are not utilized, the integration points are defined in the tool configuration files:
- **Claude Code**: `.claude/settings.json` controls command execution approvals, system prompt modifiers, and tool paths.
- **OpenCode**: `opencode.json` defines tool permissions, network rules, and workspace directory mappings.
- **Antigravity**: `.agents/rules/GEMINI.md` binds workspace permissions and orchestrates agent execution.
