# Hooks

## What it is

A hook is a script your AI tool runs at a fixed moment: when a session starts, before or after a tool call, or when the agent is about to stop. A hook can **remind** (print a message) or **enforce** (block the action until something is fixed).

## Why it pays off

Rules written in prose are advisory: a model can skip them, especially late in a long session. A hook fires every time, whether or not the model remembers the rule.

!!! info "Evidence level: reference implementation"
    A production backend (anonymized) used three kinds of hooks and permissions in Claude Code: a session-start hook that printed the working loop and pointed at `memory/`; a stop hook that, when code had changed, reminded the agent to verify, update the docs, and record what it learned; and permissions that ask before every commit, push, merge, or branch deletion. Its OpenCode setup used a plugin that ran the formatter after edits and `make check` when the session went idle.

!!! info "Evidence level: industry"
    In Claude Code, hooks are configured in `settings.json`. A hook that exits with code 2 blocks the action and its error output is shown to the model, which then has to deal with it; a hook that exits 0 only adds a message. See the [Claude Code hooks documentation](https://docs.anthropic.com/en/docs/claude-code/hooks).

## Template

Project settings for Claude Code, in `.claude/settings.json` (committed, so the whole team gets them):

```json
{
  "permissions": {
    "ask": [
      "Bash(git commit:*)",
      "Bash(git push:*)",
      "Bash(git merge:*)",
      "Bash(git branch -D:*)",
      "Bash(gh pr merge:*)"
    ]
  },
  "hooks": {
    "SessionStart": [
      { "hooks": [{ "type": "command", "command": "bash \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/session_start.sh" }] }
    ],
    "Stop": [
      { "hooks": [{ "type": "command", "command": "bash \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/stop_gate.sh" }] }
    ]
  }
}
```

A reminder at session start, `.claude/hooks/session_start.sh`. Whatever it prints is added to the session context:

```bash
#!/usr/bin/env bash
set -euo pipefail
cat <<'EOF'
Working loop: understand, plan when needed, execute, verify, learn.
Read memory/context.md and memory/learnings.md before starting.
Verify with make check. Record decisions in docs/adr/ and lessons in memory/.
EOF
```

An enforcing hook, `.claude/hooks/stop_gate.sh`: if code changed and the gate fails, the agent cannot stop yet.

```bash
#!/usr/bin/env bash
set -uo pipefail
# Only gate when source or tests changed in this session.
if [ -z "$(git status --porcelain -- src tests 2>/dev/null)" ]; then
  exit 0
fi
if ! make check >/tmp/stop_gate.log 2>&1; then
  echo "make check fails. Fix it (see /tmp/stop_gate.log) before finishing." >&2
  exit 2
fi
exit 0
```

## When to use it and when to skip it

Use reminders at the start and end of a session. Enforce only what must never be skipped and is fast and reliable to check: a failing gate, a secret about to be committed, a destructive git command.

Skip blocking hooks for slow or flaky checks. A hook that blocks for the wrong reason teaches people to turn hooks off.

## What failed in practice

- **Every hook only reminded.** All the hooks in the production backend printed a message and exited 0. That is useful at session start, but at the end of a turn a reminder is shown, not enforced, so "verify before finishing" stayed a suggestion. The Harness Lab's health check flags exactly this pattern.

## How to check it is healthy

- At least one hook can block (exits 2 or returns a blocking decision).
- Every hook runs in a few seconds.
- Hooks live in project settings under version control, not only on one person's machine.
- Commit, push, merge, and branch deletion ask before running.

## Go deeper

- [Quality gates](quality-gates.md): what the enforcing hook runs.
- [Harness health check](health-check.md): "Hooks can enforce, not only remind".
- [Claude Code in the reference implementation](../tools/claude-code.md)
- [Gated delegation](../patterns/gated-delegation.md)
