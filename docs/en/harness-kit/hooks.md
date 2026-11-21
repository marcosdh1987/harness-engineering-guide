# Hooks

## What it is

A hook is a script your AI tool runs at a fixed moment: when a session starts, before or after a tool call, or when the agent is about to stop. A hook can **remind** (print a message) or **enforce** (block the action until something is fixed).

## Why it pays off

Rules written in prose are advisory: a model can skip them, especially late in a long session. A hook fires every time, whether or not the model remembers the rule.

!!! info "Evidence level: reference implementation"
    A production backend (anonymized) used three kinds of hooks and permissions in Claude Code: a session-start hook that printed the working loop and pointed at `memory/`; a stop hook that, when code had changed, reminded the agent to verify, update the docs, and record what it learned; and permissions that ask before every commit, push, merge, or branch deletion. Its OpenCode setup used a plugin that ran the formatter after edits and `make check` when the session went idle.

!!! info "Evidence level: industry"
    In Claude Code, hooks are configured in `settings.json`. What a `SessionStart` hook prints is added to the context the model sees. A `Stop` hook that exits with code 2 sends the agent back to keep working, with the error output as the reason. The `stop_hook_active` input field is true when the agent is already continuing because of a stop hook, and the documentation says to check it so a hook does not block on a condition that will never resolve. See the [Claude Code hooks documentation](https://code.claude.com/docs/en/hooks).

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

An enforcing hook, `.claude/hooks/stop_gate.sh`: if code changed and the fast check fails, the agent goes back to fix it, once. It reads `stop_hook_active` so it never blocks twice in a row, and it uses the fast `lint` target from [Quality gates](quality-gates.md) so it runs in seconds.

```bash
#!/usr/bin/env bash
set -uo pipefail
input="$(cat)"
# Already continuing because of this hook: let the agent stop, so a failure
# it cannot fix never keeps the session running.
if printf '%s' "$input" | grep -q '"stop_hook_active": *true'; then
  exit 0
fi
# Only gate when source or tests have uncommitted changes.
if [ -z "$(git status --porcelain -- src tests 2>/dev/null)" ]; then
  exit 0
fi
log="$(mktemp)"
# A fast, reliable target; the full gate runs in CI.
if ! make lint >"$log" 2>&1; then
  echo "make lint fails (log: $log). Fix it before finishing." >&2
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
- Every blocking hook checks `stop_hook_active`, or an equivalent, so it can never keep a session running forever.
- Every hook runs in a few seconds.
- Hooks live in project settings under version control, not only on one person's machine.
- Commit, push, merge, and branch deletion ask before running.

## Go deeper

- [Quality gates](quality-gates.md): what the enforcing hook runs.
- [Harness health check](health-check.md): "Hooks can enforce, not only remind".
- [Claude Code in the reference implementation](../tools/claude-code.md)
- [Gated delegation](../patterns/gated-delegation.md)
