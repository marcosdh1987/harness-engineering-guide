# Gated Delegation: a Ticket-to-PR Pipeline

This pattern describes the most autonomous shape a harness can safely take: an
agent receives a ticket and produces a pull request ready for human review, with
humans only at the two ends — writing the ticket, reviewing the PR. It has been
proven internally on a real production codebase; this page documents the pattern
in tool-agnostic terms and how to implement it on top of the reference template.

## The one idea

Most agent setups let the model report its own success. This pattern forbids it
structurally, by splitting the pipeline into two layers with a hard line between
them:

- **Judgement belongs to the model.** Reading the ticket, writing a spec,
  proposing a design, editing code — everything that requires interpretation.
- **Certification belongs to code.** Whether gates passed, whether the bug was
  reproduced and stopped, what the final verdict is — everything a reviewer will
  trust must be derived by deterministic scripts the model can *invoke* but can
  never *author the output of*.

```text
judgement (model)                      certification (deterministic code)
  reads a ticket                         did every required gate pass?
  writes a spec          ── invokes ──▶  would the gates notice a break?
  proposes a plan                        did the bug exist, then stop existing?
  edits code                             one single derivation of the verdict
                                                      │
                                          verdict + artifacts → human review
```

Everything else in the pattern is a consequence of that line.

## The pipeline and its diets

Each phase runs with a deliberately **restricted context** — a "diet". The diets
are the mechanism, not ceremony:

| Phase | Diet | Why |
|---|---|---|
| **Spec** | Ticket only — the repository is *not* loaded | A spec written with the code open starts describing what the code already does |
| **Design** | Repository open; may not change requirements | Design decisions need the code; requirements were fixed upstream |
| **Adversarial review** | Fresh context; documents only, no code | A reviewer who reads the code starts agreeing with it. Reviewing with the spec's own inputs lets it judge instead of taking anyone's word |
| **Plan** | Spec + design, approved | Tasks, files, order |
| **Implement** | One task, one commit | Small batches keep verification meaningful |
| **Verify** | Deterministic only | Gates run by script, per task |
| **Classify** | Deterministic only | One derivation of the verdict; a run that fails a cap is `partial`, never `success` |

An adversarial "no-go" returns the work to a person. It does not loop forever.

## What "verified" is allowed to mean

Four independent questions, four mechanisms — and a run that cannot answer one
says so instead of answering a different question:

| Question | Mechanism | Honest failure mode |
|---|---|---|
| Did the project's own checks pass? | A gate runner executes the gates **the project declares** | Absence, error, and "not recognized" are all failures — never "n/a" |
| Would those checks notice a break? | A **mutation check**: revert the non-test diff and re-run the gates | A gate that still passes is decorative — reported as such |
| Did the described bug exist, and stop? | A frozen reproduction, run at the pinned base commit and again at HEAD | A repro that passes at the pin proved nothing — marked invalid |
| What is the verdict? | One single classification script | Any cap fires → `partial`, never `success` |

The mutation check is the one teams underestimate: green gates prove the gates
*ran*, not that they can *detect* anything. Breaking the code on purpose and
requiring the gates to notice is what makes a green run mean something.

## Standing rules

Four rules, each typically earned by a shipped bug:

1. **Nothing from the repository self-certifies.** Everything trusted derives
   from a base commit pinned *before* any model touched the tree, stored outside
   the repository.
2. **Absence is not a pass.** A missing artifact, a service that never came up,
   a check that failed to load — each gets a loud state of its own.
3. **Buckets must not flatter.** No taxonomy where environment breakage lands in
   a success-enabling bin.
4. **Claims must match mechanisms.** "Deterministic" is reserved for code. A
   comment promising a bound the code does not enforce is worse than silence.

## Implementing on `ml-python-base`

The template already provides most of the raw material; the pattern is a way of
arranging it:

| Pattern element | Template counterpart |
|---|---|
| Phases as governed procedures | One skill per phase in `.github/skills/` (spec, design, adversarial, plan, implement) — same format as the existing skills |
| Phase diets | Subagents with restricted context (`.claude/agents/`, one per phase; fresh context for the adversarial reviewer) — the existing `planner`/`reviewer`/`implementer` roles are the starting point |
| Certification layer | `make` gates plus small deterministic scripts under `scripts/` — bash/`jq`-level tooling, versioned and tested like any code. The model calls `make verify`; it never writes the report |
| Per-project declaration | A config file in the target project declaring *which* gates exist and how to run them — only the project knows what verifying it means; the pipeline only knows verification must be provable |
| Run artifacts | A per-run directory (spec, plan, per-task diffs and gate logs, classification) — provenance a reviewer and the lab can audit |
| The wall | Branch protection on the default branch, plus dry-run as the default for any mutating operation. A command-level guard is a seatbelt, not containment |

What the template does **not** give you and this pattern adds: the phase
ordering with its diets, the mutation check, the red→green evidence flow, and
the single-derivation classifier. Each is small, deterministic code — the kind
of thing the working loop's *Verify* step already argues for, taken to its
logical end.

## Where it fits

- **Adoption order:** this is an end-state, not an entry point. A team should be
  comfortable with the assisted working loop (Ground → Plan → Delegate → Verify
  → Compound) before delegating whole tickets.
- **Measurement:** a benchmarking lab can run the pipeline as one more condition
  (pipeline vs. assisted session, same tickets) and compare pass rate, cost,
  and intervention count — the pattern's artifacts are designed to be audited.
- **Context:** the spec phase reads the ticket *and the project's conventions* —
  ticketing rules, definition of ready, domain glossary — which is exactly what
  the project brain (and, at multi-repo scope, a shared brain) provides. See
  [Adopting the Harness in an Existing Project](../getting-started/adopt-existing-project.md).
