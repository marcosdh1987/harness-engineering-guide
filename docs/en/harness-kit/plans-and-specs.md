# Plans and specs

## What it is

A spec (a design) says what you will build and why. A plan says how, step by step: the files each step touches and how each step is verified. The order is fixed: the design is approved, then the plan is written, then execution follows the plan without reopening the design.

## Why it pays off

Separating decisions from execution lets an agent run a long task without drifting, lets a person review the design once instead of every diff, and makes the work resumable when a session ends halfway through. When the plan carries the decisions, execution can run on a cheaper model or be split across agents.

!!! info "Evidence level: reference implementation"
    A production backend (anonymized) kept about 27 plans in `docs/plans/` over two months. Its planning skill (`plan_and_execute_feature`, also in `ml-python-base`) has an `execute_only` mode: given an approved plan, it skips the planning phases and goes straight to execution, so the design is not reopened.

## Template

A spec, in `docs/specs/YYYY-MM-DD-<topic>-design.md`:

```markdown
# Design: <topic>

## Intent
Why this exists and who it is for.

## Goals, non-goals, anti-goals
What it must do, what it will not do, and what would make it a failure even if it works.

## Constraints
Rules, dependencies, deadlines, privacy.

## Approaches considered
Two or three options, what each trades off, which one was chosen and why.

## Decided design
The parts that are settled.

## Left to the builder
What the person or agent implementing it may decide.
```

A plan, in `docs/plans/YYYY-MM-DD-<topic>.md`:

```markdown
# Plan: <topic>

Spec: docs/specs/YYYY-MM-DD-<topic>-design.md

## Task 1: <deliverable>
Files: <files to create or change>
- [ ] Write the failing test (or the check that proves it).
- [ ] Make the change.
- [ ] Run <command>. Expected: <output>.
- [ ] Commit.

## Task 2: ...
```

## When to use it and when to skip it

Use both for new or ambiguous work, for changes across modules, and for anything risky or hard to reverse.

Skip them for small and clear tasks: a typo needs neither. A bounded task gets a short plan in the session itself, not a file. The routing table in `AGENTS.md` makes that choice for you.

## What failed in practice

- **The design gate was named more than it was used.** In the production backend, the brainstorming skill (which blocks code until a design is approved) was referenced in every instruction file, yet only 7 design specs were written in the same period that produced over 100 decision records and about 27 plans. Most work went through the cheaper path, which was fine; the mistake would be to believe the gate protected work it never saw.
- **Plans that reopen the design mid-way** turn execution into a new design session, without the review the first one had.

!!! tip "Evidence level: guide recommendation"
    Keep the design gate for new or ambiguous work only, and let the routing table send everything else down the cheap path. Count designs written, not mentions of the gate.

## How to check it is healthy

- Every non-trivial change that merged can point to a plan, or to a reason it did not need one.
- Every plan step says how it is verified.
- Every spec records the approaches it considered.
- No plan changed the design without a new approval.

## Go deeper

- [Spec-driven agentic work](../patterns/spec-driven-agentic-work.md)
- [Gated delegation](../patterns/gated-delegation.md)
- [The working loop](../patterns/working-loop.md)
- [Decision records](decision-records.md)
