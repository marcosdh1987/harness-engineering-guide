# Adopting the Harness in an Existing Project

Most real engagements do not start from a fresh template. The typical case is an
**existing project** — one repository, or a few services that share a domain —
that already has code, history, and habits. This page describes how to adopt the
harness there safely, how the project's context grows into a **project brain**,
and when (and only when) that brain should be extracted into a shared repository.

The rule that governs everything here comes from
[From Project to Organization](project-to-organization.md): **do not skip
levels.** Adopt at the smallest scope that solves the observable problem.

## The progression

```text
Level 0 — Existing repo, no harness
    AI use is ad-hoc; context is re-explained every session.

Level 1 — Retrofit
    The repo adopts the governance layer from the template
    (rules, skills, adapters, gates) via selective sync. Code untouched.

Level 2 — Project brain (inside the repo)
    The project's context accumulates in the containers the template
    already provides: memory/, docs/adr/, .github/domain-boundaries.md,
    and domain docs. No new repository is created.

Level 3 — Shared brain (only at 2+ repos)
    The moment a second repo of the same project/client starts duplicating
    context, the common part is extracted to a context repository
    (see The Company Brain Template) and both repos point at it.
```

Most engagements live their whole life at Levels 1–2. That is success, not an
intermediate state.

## What "project brain" means

A project brain is not a product or a new repository. It is the **in-repo
context layer** that `ml-python-base` already ships containers for:

| Container | What accumulates there |
|---|---|
| `memory/context.md` | Where the project is right now — updated at session start/end |
| `memory/learnings.md`, `memory/patterns.md` | Durable lessons and recurring solutions |
| `docs/adr/` | Decisions and their rationale — the durable "why" |
| `.github/domain-boundaries.md` | The project's domain rules and boundaries |
| `docs/` (glossary, runbooks as needed) | Vocabulary and procedures, added when they earn their place |

The brain grows by use, not by ceremony: the first working session fills
`context.md`; the first non-obvious decision produces an ADR; a term that needed
explaining twice enters a glossary; a procedure explained twice becomes a
runbook. Nothing is written "just in case".

## Two safe adoption paths

### Path A — Retrofit in place

For a repo that will keep evolving where it is. The selective governance sync
brings rules, skills, agents and adapters from a tagged template release
**without touching code, data, or the project's Makefile**:

```bash
make template-remote-setup                 # once
make template-sync PREVIEW=1 REF=vX.Y.Z    # read-only diff — always look first
make template-sync REF=vX.Y.Z              # adopt
```

Safety properties that make this low-friction:

- **Read-only first.** The preview shows every file the sync would write before
  anything is written.
- **Additive by default.** Governance files land next to the project; existing
  CI and scripts are not modified. Gates are adopted incrementally — start with
  the read-only ones (`lint`, `test`) and only then make them required.
- **Reversible.** Everything arrives in one commit range; reverting the adoption
  is a `git revert`, not a migration back.

### Path B — Strangler expansion (new repo beside the legacy)

For projects where retrofitting the legacy repo is not worth the friction (very
old toolchains, frozen CI, hostile build systems) — or where new work can be
cleanly separated. Instead of migrating the legacy repo, **start the next
module/service as a fresh repo from the template** (`make init`) and let it
coexist:

```text
legacy-repo/          minimal retrofit: adapters + read-only gates only
new-service/          full harness from day 1 (make init)
```

- The legacy repo gets the *minimum*: instruction adapters (`CLAUDE.md`,
  `AGENTS.md`) and read-only checks, so AI assistance is governed there too —
  but nobody rewrites its build.
- New work happens in the new repo with the full working loop.
- Migration proceeds module by module, **pulled by real tasks** ("this feature
  touches module X → X moves"), never as a big-bang rewrite.

This is the classic strangler-fig pattern applied to harness adoption: full
migration friction is avoided because full migration is never scheduled.

!!! warning "The moment Path B creates two repos, watch for context duplication"
    The legacy repo and the new repo share a domain. The day you copy the
    glossary or a business rule from one to the other is the day the shared
    brain earns its existence — see below.

## When to extract a shared brain

The trigger is concrete and observable: **a second repo starts duplicating the
first repo's context.** Not before. The extraction itself is cheap — it is
moving Markdown files, not migrating code:

1. Instantiate the context template
   ([company-brain-template](company-brain-template.md)) at the scope of the
   engagement — the "organization" can simply be *this client's platform*.
2. Move (not copy) the shared parts: glossary, domain rules, cross-repo
   decisions, shared conventions. Project-specific ADRs and memory stay in each
   repo.
3. Point both repos' adapters at the shared brain (the ready-to-paste snippet is
   in the template's `examples/`).

Anti-pattern, stated plainly: **creating a company/shared brain on day one of a
single-repo engagement is overkill.** It adds a second repository to maintain
before any duplication exists. The in-repo project brain is the right tool until
the second repo appears.

## Measuring the adoption

Adoption without a baseline cannot demonstrate value. Minimum viable
measurement, in order of effort:

1. Route AI usage through a gateway from day one — cost and adoption per
   developer become data, not anecdote.
2. Record the "before": gate status, time-to-onboard, where sessions lose time
   re-explaining context.
3. Re-measure after 4–6 weeks; the delta is the engagement's evidence.

## Checklist

- [ ] Preview run and reviewed before any sync (`PREVIEW=1`)
- [ ] Gates adopted read-only first; nothing existing was weakened or replaced
- [ ] `memory/context.md` filled in the first working session
- [ ] First ADR recorded when the first non-obvious decision appeared
- [ ] No shared brain created while the engagement has a single repo
- [ ] On the second repo: duplication watched, extraction done when it appears
