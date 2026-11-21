# Quality gates

## What it is

A quality gate is one command that answers "is this change acceptable?" with pass or fail: for example `make check`. People run it, agents run it before saying they are done, hooks can run it, and CI runs the same command on every change.

## Why it pays off

An agent's "all tests pass" is only as good as the command behind it. One gate, used by everyone and everything, turns verification from a claim into evidence, and it lets you add a rule once (a lint, a test that enforces architecture) and have every tool respect it.

!!! info "Evidence level: reference implementation"
    A production backend (anonymized) bundled its gate in `make check`: secret scan, prose check, formatter check, lint, security lint, type check, and tests with coverage. A broader `make ci` added two checks worth copying: a test that parses imports and fails when a module crosses an architecture layer, and a check that fails when source or tests change without a documentation change. `ml-python-base` v2.2.0 fixed a gate that used to auto-format the code and then report success even when a test failed.

## Template

A minimal gate in a `Makefile`, read-only by design:

```make
install:
	uv sync

# Fast checks: format and lint. Hooks can run this in seconds.
lint:
	uv run ruff format --check src tests
	uv run ruff check src tests

# The gate never writes. It fails when anything fails.
check: lint
	uv run mypy src
	uv run pytest

# Fixes are a separate, explicit step.
fix:
	uv run ruff check --fix src tests
	uv run ruff format src tests
```

Use the equivalent for your stack (`npm run check`, `./gradlew check`). Then make CI run exactly the same target:

```yaml
# .github/workflows/ci.yml
name: ci
on: [push, pull_request]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v6
      - run: make install
      - run: make check
```

Two extras that pay off once the basics are in place:

- **An architecture test:** a unit test that reads the imports of each module and fails if, say, the domain layer imports the infrastructure layer. The rule stops depending on review.
- **Docs follow code:** a CI check that fails when files under `src/` or `tests/` change and nothing under `docs/` does. It keeps the context the agents read from going stale.

## When to use it and when to skip it

Every repository that agents touch needs a gate, even a small one. Grow it as you find failures: a mistake an agent made twice is a candidate for a check.

Do not put slow, flaky, or network-dependent steps in the gate agents run on every change; keep those in a separate CI job.

## What failed in practice

- **A gate that could not fail.** The template's earlier `make test` ran the formatter and the auto-fixer first, then ended with a fallback that printed "No tests found to run", so a failing suite exited 0. Every "tests pass" built on it was unverified. Release 2.2.0 made it run the tests only and propagate the failure.
- **A gate that rewrites the tree** hides lint failures and leaves diffs nobody can explain, because the code being checked changes while it is checked.

## How to check it is healthy

- Break a test on purpose: the gate must exit with an error.
- Run the gate twice on a clean tree: `git status` stays clean.
- CI runs the same target, on every pull request.
- The gate finishes fast enough that people run it before every commit.

## Go deeper

- [Harness health check](health-check.md): "Verification can fail", "Verification does not rewrite the tree", "CI runs the same gate the agent runs".
- [Hooks](hooks.md): blocking the end of a turn on a failing gate.
- [Validate a change](../labs/validate-a-change.md)
- [ml-python-base automation reference](../reference-implementation/ml-python-base/automation.md)
