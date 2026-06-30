# Claude Code in the Engineering Harness

## Role in a Development Workflow

Claude Code integrates into the workflow as an interactive terminal tool capable of running diagnostics, exploring code incrementally, and applying refactoring. Unlike tools that depend purely on one-off prompting, Claude Code operates as a semi-autonomous agent guided by a durable operating layer (the Harness).

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
