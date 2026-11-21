# Decision records (ADRs)

## What it is

An Architecture Decision Record (ADR) is one page about one decision that is hard to reverse: the context that forced a choice, the choice, its consequences, and the alternatives you rejected. The code shows what the system does; the record says why.

## Why it pays off

Decision records stop teams from re-arguing settled questions, make reviews faster, and give agents the rationale they need to extend a system the way it was meant to grow. An agent that reads "we store dates in UTC and convert them only at the edges, because..." will not add local times in the next change.

!!! info "Evidence level: reference implementation"
    A production backend (anonymized) wrote over 100 decision records in about two months (roughly 1,000 commits). Many recorded behavior decisions (how a step behaves, which component owns a value), not only architecture. Each title was the decision written as a sentence, so the index read as a list of the rules in force.

## Template

Copy the record itself from [the starter kit](index.md). Put these rules in `docs/adr/README.md`:

```markdown
# Decision records

Write one when a decision is hard to reverse, or when someone (a person or an
agent) would otherwise have to reverse-engineer it.

1. Copy 0000-template.md to NNNN-short-title.md (next number, four digits).
2. The title is the decision as a sentence: "Store dates in UTC, convert at the edges".
3. Fill in Context, Decision, Consequences, Alternatives. One page is plenty.
4. Status starts as Proposed. It becomes Accepted in the same pull request
   that implements it.
5. Accepted records are not edited. A new decision supersedes the old one, and
   the old one says "Superseded by ADR-XXXX".
6. Add the record to the index at the end of this file.
```

A `/adr` command can scaffold a new record from the template, add it to the index, and ask you for anything it had to assume. See [Commands](commands.md) for the other shortcuts.

## When to use it and when to skip it

Write one when you choose a framework, a datastore, or an external service; when you define or change a boundary between modules; when you accept a non-obvious trade-off; when you set a convention everyone must follow; or when an agent would otherwise have to guess why a behavior exists.

Skip it for routine changes that are easy to reverse. A typo does not need a decision record; put small lessons in [project memory](project-memory.md) or the commit message.

## What failed in practice

- **Status drift.** In the production backend, more than half of the records were still "Proposed" after their work had shipped. Readers, and agents, could not tell which decisions were in force.
- **Editing history.** Changing an accepted record hides how the system got where it is. Superseding keeps both the old reason and the new one.

!!! tip "Evidence level: guide recommendation"
    Make accepting the record part of merging: the pull request that implements a decision flips its status to Accepted, and the reviewer checks that line like any other.

## How to check it is healthy

- Every record appears in the index.
- No record is "Proposed" when its change has already merged.
- Every superseded record names its replacement.
- Each record still fits on one page.

## Go deeper

- [Project memory](project-memory.md): for lessons that are not decisions.
- [Plans and specs](plans-and-specs.md): where a decision often starts.
- [State and continuity](../concepts/state-and-continuity.md): how decisions fit into project memory and organizational knowledge.
