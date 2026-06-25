# Session Hooks & Guardrails

> [!NOTE]
> **Generated content**: This page is automatically generated from the template snapshot.
> - **Reference Commit**: [587ac29](https://github.com/marcosdh1987/ml-python-base/commit/587ac29d30cb50d5c307f41e942c14d3f0bba298) on branch `main`
> - **Last Synced**: `2026-06-25T14:51:49.011688Z`
> - **Reference Artifacts**:
>   - [.claude/hooks/](https://github.com/marcosdh1987/ml-python-base/blob/587ac29d30cb50d5c307f41e942c14d3f0bba298/.claude/hooks/)
> *Note: This is a study summary and index. The authoritative implementation and governance remain in the source repository.*
## Hooks as Quality Guardrails

Hooks are executable scripts triggered automatically at key interaction boundaries. They integrate external validation checks, state diagnostics, and environment compliance checks directly into the agent session loop.

### Discovered Hook Files

| Hook Name | Target Path | Purpose | Link |
|---|---|---|---|
| `stop_nudge.sh` | `.claude/hooks/stop_nudge.sh` | Warns developer of drift or uncommitted changes when the session remains idle | [Link](https://github.com/marcosdh1987/ml-python-base/blob/587ac29d30cb50d5c307f41e942c14d3f0bba298/.claude/hooks/stop_nudge.sh) |
| `session_start.sh` | `.claude/hooks/session_start.sh` | Runs checks on environment setup, local lock state, and checks for uncommitted drift | [Link](https://github.com/marcosdh1987/ml-python-base/blob/587ac29d30cb50d5c307f41e942c14d3f0bba298/.claude/hooks/session_start.sh) |

### Configuration Settings and Integrations

If explicit shell hooks are not utilized, the integration points are defined in the tool configuration files:
- **Claude Code**: `.claude/settings.json` controls command execution approvals, system prompt modifiers, and tool paths.
- **OpenCode**: `opencode.json` defines tool permissions, network rules, and workspace directory mappings.
- **Antigravity**: `.agents/rules/GEMINI.md` binds workspace permissions and orchestrates agent execution.
