# Claude Code in the Engineering Harness

## Role in a Development Workflow

Claude Code integrates into the workflow as an interactive terminal tool capable of running diagnostics, exploring code incrementally, and applying refactoring. Unlike tools that depend purely on one-off prompting, Claude Code operates as a semi-autonomous agent guided by a durable operating layer: the harness.

In [`ml-python-base`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0), Claude Code is the most complete example of a tool with persistent instructions, commands, hooks, and native skills. This page is a study guide for how a highly autonomous tool can follow shared rules without hand-copying them.

## What Claude Code Reads

| Artifact | What it provides | Source |
|---|---|---|
| [`CLAUDE.md`](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/CLAUDE.md) | Integration profile, command policies, toolbelt, and working loop. | Rendered source of truth for Claude Code |
| [`.claude/`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.claude/) | Workspace settings, commands, hooks, and native skills. | Generated and configured |
| [`.claude/skills/`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.claude/skills/) | Governed and external skills exposed as links for Claude. | Generated from `.github/skills/` |
| [`.claude/hooks/`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.claude/hooks/) | Session reminders and non-blocking nudges. | Adapter configuration |
| [`adapters/templates/claude.md.j2`](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/adapters/templates/claude.md.j2) | Template that renders shared instructions for Claude Code. | Adapter |

`CLAUDE.md` is the human and operational entry point. `.claude/` contains the native shape Claude Code uses for commands, hooks, and skill discovery.

---

## The Claude Toolbelt

The **Claude Toolbelt** is the practical execution layer that allows Claude to obtain answers to routine environment or repository questions before asking the developer.

### 1. Integrated MCP Servers
The `.mcp.json` file in the project root defines structured context tools:
- `context7`: Allows querying up-to-date documentation for libraries, dependency APIs, and migration notes.
- `git`: Provides a structured interface to inspect file state, diffs, and history.

### 2. Recommended CLIs
Claude has access to terminal tools to resolve tasks directly:
- **Environment Management**: `uv` and `make`.
- **Repository Integrations**: `git` and `gh` (GitHub CLI).
- **Data Processing**: `curl` and `jq`.
- **Diagnostic Tools**: `opencode` and `claude`.

### 3. Tool Choice Rule
Claude is instructed to use the lightest tool available that can retrieve the required data:
1. Use `make` targets and local project commands for repeatable operations.
2. Use **MCP** when structured context is superior to flat terminal shell output.
3. Use **native CLIs** (`gh`, `docker`, `aws`, `gcloud`, etc.) to interact with locally authenticated external services.
4. **Ask the developer** only if the information cannot be retrieved via tools, requires a product decision, or needs unconfigured credentials.

### 4. Automatic Diagnostics: `make toolbelt-doctor`
Runs the `scripts/toolbelt_doctor.py` script to validate the availability of core and optional tools. The doctor check probes environment variables or checks if local services are running on their default ports non-invasively:
- **LiteLLM / AI Gateway** (default port `4000/v1`)
- **Langfuse** (default port `3000`)
- **MLflow** (default port `5000`)
- **Ollama** (default port `11434/v1`)
- **LM Studio** (default port `1234/v1`)

---

## Session Hooks and Nudges

Hooks act as non-blocking reminders or gates in the session to guide the agentic workflow without hindering developer agility.

- **SessionStart (`session_start.sh`)**: Injects a reminder of the repository's working loop (`Ground -> Plan -> Delegate -> Verify -> Compound`) and project memory paths into the conversation context at session startup.
- **Stop/Idle (`stop_nudge.sh`)**: When the agent's turn ends and there are uncommitted changes under `src/` or `tests/`, it prints a gentle reminder to verify changes with `/verify` (`make check`), update local documentation, and record learnings in `memory/` before closing.

---

## Custom Commands and Skills Configuration

Governed skills are exposed in `.claude/skills/` and registered using YAML frontmatter in their `SKILL.md` files to customize Claude's behavior:

- **`context: fork`**: Executes the skill in a subagent with an isolated context. This prevents verbose code analysis or long exploration outputs from cluttering the developer's main conversation context.
- **`allowed-tools`**: Restricts the tools the skill can access (e.g., limiting to read-only operations to prevent accidental destructive edits).
- **`argument-hint`**: Provides descriptions and interactive prompts for skill parameters when invoked from the terminal.

## Files and Folders Involved

Skills and rules originate in the governed layer: `.github/skills/`, `.github/skills-external/`, `.github/agents/`, and `.github/*.md`. The [`src/ml_python_base/skills_sync/`](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/src/ml_python_base/skills_sync/) engine projects that intent into `.claude/skills/` and into generated regions of `CLAUDE.md`.

`make sync-skills` updates projections; `make check-sync` validates that links, generated blocks, and manifests are still synchronized. The tool can have its own affordances, while governed content remains in the same place used by OpenCode, Codex, Copilot, and Antigravity.

## Source of Truth vs Generated

Edit shared rules and skills in `.github/`, and templates in `adapters/`. Treat `.claude/skills/` as native output. If an instruction is fixed only in a projected copy, the change is fragile and will not propagate to the rest of the harness.

## Mini Study Flow

1. Read the [inventory](../reference-implementation/ml-python-base/inventory.md) and locate `CLAUDE.md`, `.claude/`, `.claude/skills/`, and `.claude/hooks/`.
2. Review [hooks](../reference-implementation/ml-python-base/hooks.md) to understand how nudges help without blocking.
3. Read [skills](../reference-implementation/ml-python-base/skills.md) and compare governed sources with links in `.claude/skills/`.
4. Finish with [adapters](../reference-implementation/ml-python-base/adapters.md) and [drift control](../reference-implementation/ml-python-base/drift-control.md).

## Official Documentation

- [Claude Code Overview](https://docs.anthropic.com/en/docs/claude-code/overview): overview of Claude Code as an agentic tool that reads, edits, and runs code.
- [Claude Code Skills](https://docs.anthropic.com/en/docs/claude-code/skills): official guide for creating, managing, and sharing skills in Claude Code.
- [Claude Code Memory](https://docs.anthropic.com/en/docs/claude-code/memory): using `CLAUDE.md` as project memory and persistent instructions.

## References

- [`ml-python-base` on GitHub](https://github.com/marcosdh1987/ml-python-base/tree/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0)
- [Artifact inventory](../reference-implementation/ml-python-base/inventory.md)
- [Hooks](../reference-implementation/ml-python-base/hooks.md)
- [Adapter projection](../reference-implementation/ml-python-base/adapters.md)
