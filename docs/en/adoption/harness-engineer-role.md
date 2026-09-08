# The Harness Engineer / AI Champion Role

As engineering organizations adopt AI coding tools, a sharp divide quickly appears: individual developers report speedups on isolated tasks, yet team delivery throughput and software quality remain flat. Individual AI proficiency does not automatically create organizational leverage.

The **Harness Engineer** (or **AI Champion**) is the organizational role or capability responsible for turning personal AI productivity into reliable, team-wide engineering throughput.

---

## 1. Role Definition: Responsibility over Job Title

Depending on organizational maturity and team size, this function may manifest as:

- **A Team Responsibility**: distributed among senior engineers within an existing feature squad.
- **A Dedicated Staff Role**: a staff engineer leading developer productivity and agentic workflows.
- **A Platform Team Capability**: an internal developer platform (IDP) team providing shared governance, devcontainers, and evaluation infrastructure.

The title matters far less than the mandate: **designing, maintaining, and simplifying the system around the model.**

---

## 2. Contrasting the Profiles

Understanding this role requires separating individual tool proficiency from systems engineering:

| Dimension | AI-Proficient Developer | Harness Engineer / AI Champion |
|---|---|---|
| **Primary Focus** | Completing their own assigned ticket faster | Designing the system that makes the whole team reliable |
| **Tool Usage** | Crafting effective one-off chat prompts | Encoding constraints into reusable rules, skills, and gates |
| **Context Strategy** | Pasting snippets into the context window | Structuring repository layout and Company Brain registers |
| **Verification** | Eyeballing output or running local checks | Building automated evaluation suites and regression tests |
| **Lifecycle View** | Individual coding sessions | Continuous improvement loop: Measure → Learn → Improve |
| **Maintenance** | Adopting every new prompt trick | Pruning obsolete rules and retiring redundant scaffolding |

---

## 3. Core Responsibilities

The Harness Engineer operates across the **Five Operational Surfaces**:

### 1. Direction & Instructions
- Governs shared repository rules (`.github/standards.md`, `AGENTS.md`, `CLAUDE.md`).
- Curates the catalog of operational skills, ensuring each skill has clear triggers and verification steps.
- Establishes spec-driven guidelines that prevent agents from writing ungrounded code.

### 2. Context Architecture
- Structures the repository map so agents can navigate large codebases efficiently.
- Integrates project memory (`memory/`, ADRs) with the broader Company Brain.
- Designs selective retrieval mechanisms to protect model context windows from saturation.

### 3. Environment & Agent Legibility
- Ensures local and CI environments are reproducible (lockfiles, containers, makefiles).
- Optimizes internal developer tools to emit machine-readable output (structured JSON, exit codes).
- Provisions isolated sandboxes and git worktree setups for parallel agent execution.

### 4. Validation & Evaluation
- Builds internal evaluation suites and regression cases derived from production bugs.
- Operates the evaluation platform to measure the impact of harness changes before rolling them out.
- Enforces multi-tier quality gates (`make check`) that block regressions before merge.

### 5. Adaptive Maintenance & De-scaffolding
- Audits skill and rule usage via attribution logs.
- Identifies scaffolding that has become obsolete due to frontier model advancements.
- Simplifies the harness to reduce token overhead and maintenance burden.

---

## 4. Enabling Team Adoption

A successful Harness Engineer does not act as an isolated gatekeeper. Their primary goal is education and capability transfer:

1. **Pairing and Mentoring**: teaching engineers how to steer agents effectively using the working loop.
2. **Standardizing Best Practices**: turning hard-won debugging lessons into repository rules or regression evals.
3. **Removing Scaffolding Friction**: ensuring that using the harness is faster and more dependable than working without it.
