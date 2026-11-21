# Harness health check

Eight checks that tell you whether a repository's harness can actually do its job. You can run all of them by reading your repository; the Harness Lab can also run them for you, deterministically, with no model.

!!! info "Evidence level: reference implementation"
    These are the checks of the Harness Lab's `make harness-check`, the same ones its repository audit embeds. They are decided by code, not by a model, so the result is the same every time.

## The checklist

| # | Check | How to check by reading | Why it matters |
| --- | --- | --- | --- |
| 1 | **Verification can fail** | Find the command agents are told to verify with. Break a test on purpose: does it exit with an error? | If a failing test still exits 0, every "tests pass" an agent reports is unverified. |
| 2 | **Verification does not rewrite the tree** | Read that target: does it format or auto-fix while it "tests"? | A target that rewrites code changes what it is checking, hides lint failures, and leaves unexplained diffs. |
| 3 | **Hooks can enforce, not only remind** | Look at your hooks: can at least one block (exit code 2 or a blocking decision)? | Prose rules are advisory. A hook that prints a reminder and exits 0 is shown, not acted on. |
| 4 | **Always-loaded instructions stay a map** | Count the lines of `AGENTS.md`, `CLAUDE.md`, or your tool's rules file. Budget: about 200 lines or 2,500 tokens. | Every session pays for that file before it reads the task. A short map that points to docs and skills does the same job. |
| 5 | **Skills are discoverable** | Open each `SKILL.md`: does it have a `name` and a one-line `description` that says when to use it? | An agent decides whether to load a skill from its name and description alone. Without a description it is never chosen. |
| 6 | **MCP servers are pinned** | Read `.mcp.json`: does any server use `@latest` or no version? | An unpinned server runs whatever was published last, with the agent's permissions. Pinning makes an upgrade a reviewed change. |
| 7 | **CI runs the same gate the agent runs** | Open `.github/workflows/`: does a workflow run the same target on every change? | Local verification only counts if CI enforces it; otherwise skipped checks reach main. |
| 8 | **The harness version is declared** | Is there a `.template-version` or `.harness-version.yaml` file? | Without it, nobody can tell which harness a result came from, or whether an upgrade changed anything. |

## Run it automatically

Clone the Harness Lab once and point it at any local repository:

```bash
git clone https://github.com/marcosdh1987/ai-agentic-harness-lab
cd ai-agentic-harness-lab
make harness-check REPO=../your-project
```

It needs `git`, `uv`, and `make`. It needs no Docker, no model, and no network once installed, and each run takes about 30 seconds. It reads the committed tree (add `REF=<branch>` for another ref), prints one line per check with a fix for each failure, and exits 1 when a check fails, so it can gate a CI job too.

## After the checklist

A green checklist means the harness can work, not that it helps. To know whether a skill, a rule, or a model change actually improves results, compare two configurations on the same case in the [Harness Lab](../reference-implementation/ai-agentic-harness-lab/index.md).

## Go deeper

- [Quality gates](quality-gates.md): checks 1, 2, and 7.
- [Hooks](hooks.md): check 3.
- [Start with few skills](few-skills.md): checks 4 and 5.
- [The starter kit](index.md): a harness that passes most checks from day one.
