# Harness Engineering Guide

**The Engineering Discipline for Building, Evaluating, and Continuously Improving the Agentic SDLC.**

[Harness Engineering Guide](https://marcosdh1987.github.io/harness-engineering-guide/) is a public, vendor-neutral methodology and reference guide for engineering organizations transitioning from individual, ad-hoc AI assistance to a systematic, measurable, and continuously improving agentic software development lifecycle.

---

```mermaid
flowchart LR
    A["Standardize<br/>(Rules, Skills, Adapters, Gates)"] --> B["Measure<br/>(Sandboxes, Attribution, Audits)"]
    B --> C["Improve<br/>(Proposals, Fixes, Regressions)"]
    C --> A
```

---

## The Core Question

> **How does an engineering organization transition from individual developers using AI coding tools to systematically managing, measuring, and improving an agentic development system?**

As AI coding assistants evolve from single-turn autocompletion into multi-turn autonomous agents (executing shell commands, editing repositories, running test suites, and calling external tools), prompt engineering alone becomes insufficient. 

Organizations face recurring challenges:
- **Silent Regressions and Drift**: Agents generate code that passes superficial checks but violates architectural boundaries, security policies, or database migration rules.
- **Perception-Driven Evaluation**: Teams judge agents by individual anecdotal feelings rather than reproducible, quantitative evidence.
- **Ephemeral Learning**: Lessons from agent mistakes remain lost in chat transcripts instead of compounding into organizational capabilities.

**Harness Engineering** solves this by treating the system around the model (the rules, context, skills, tools, execution environments, quality gates, observability, and evaluations) as an engineered, version-controlled software system.

---

## The Guiding Methodology: Standardize → Measure → Improve

The framework is structured around three foundational pillars:

```mermaid
flowchart TB
    subgraph S["1. STANDARDIZE"]
        direction TB
        S1["Engineering Rules & Constraints"]
        S2["Reusable Governed Skills"]
        S3["Agent & Subagent Roles"]
        S4["Tool Adapters (Claude, Codex, OpenCode)"]
        S5["Drift Control & Quality Gates"]
    end

    subgraph M["2. MEASURE"]
        direction TB
        M1["Isolated Container Sandboxes"]
        M2["Objective Pass/Fail Verification"]
        M3["Structured Attribution (Used vs Available)"]
        M4["Telemetry (Tokens, Cost, Steps, Time)"]
        M5["LLM Behavioral Audits"]
    end

    subgraph I["3. IMPROVE"]
        direction TB
        I1["Failure → Evaluation Case"]
        I2["Controlled A/B Experiments"]
        I3["Harness & Skill Refinement"]
        I4["Gate-Verified Release"]
        I5["Permanent Regression Suites"]
    end

    S --> M --> I --> S
```

1. **Standardize**: Define and version how agents are expected to work, including architectural boundaries, approved tools, reusable skills, and validation gates.
2. **Measure**: Replace subjective perception with reproducible evaluation cases executed inside controlled sandbox environments. Capture exact attribution, token costs, step traces, and behavioral audits.
3. **Improve**: Close the feedback loop. Transform agent failures into reproducible evaluation cases, test improvements under controlled conditions, and retain them as permanent regression tests.

---

## Where to Start

<div class="grid cards" markdown>

-   :material-presentation: **[Agentic SDLC for Teams](start-here/agentic-sdlc-for-teams.md)**

    ---

    A 10-minute executive and technical briefing. Covers the core problem, the Maturity Model, the database migration case study, and implementation roadmaps.

-   :material-school: **[What is Harness Engineering?](start-here/what-is-harness-engineering.md)**

    ---

    Explore the complete Harness Stack: context engineering, rules architecture, governed skills, quality gates, and tool adapters.

-   :material-chart-line: **[Agentic SDLC Maturity Model](adoption/maturity-model.md)**

    ---

    Assess your organization across 6 levels (from Level 0: Ad-hoc AI to Level 5: Continuously Improving Agentic SDLC).

-   :material-flask: **[Controlled Environments & Sandboxing](evaluation/controlled-environments-sandboxing.md)**

    ---

    Understand why evaluating agents requires isolated execution environments for reproducibility, safety, and experimental validity, backed by industry research.

</div>

---

## The Five-Layer Ecosystem

This guide connects five modular layers of agentic engineering into a closed continuous improvement loop:

```mermaid
flowchart TD
    GUIDE["<b>1. METHOD</b><br/>harness-engineering-guide<br/><i>Principles · Patterns · Evidence · Adoption</i>"]
    BRAIN["<b>2. KNOWLEDGE</b><br/>company-brain-template<br/><i>Evidence · Decisions · Context · Requirements</i>"]
    HARNESS["<b>3. GOVERNANCE</b><br/>ml-python-base<br/><i>Rules · Skills · Adapters · Quality Gates</i>"]
    RUNTIME["<b>4. RUNTIME</b><br/>ml-langchain-agent<br/><i>Clean Architecture · LangGraph · Persistent APIs</i>"]
    LAB["<b>5. EVALUATION</b><br/>sdlc-ml-python-harness-lab<br/><i>Experiments · Sandboxes · Attribution · Scoring</i>"]

    GUIDE --> BRAIN --> HARNESS --> RUNTIME --> LAB
    LAB -->|"Empirical Learnings"| HARNESS
    LAB -->|"Empirical Learnings"| BRAIN
    LAB -->|"Validation Evidence"| GUIDE
```

1. **Methodology**: [`harness-engineering-guide`](https://github.com/marcosdh1987/harness-engineering-guide), providing the conceptual foundations, operational surfaces, and patterns.
2. **Knowledge Plane**: [`company-brain-template`](https://github.com/marcosdh1987/company-brain-template), providing the persistent, agent-readable organizational memory and evidence promotion pipeline.
3. **Engineering Governance**: [`ml-python-base`](https://github.com/marcosdh1987/ml-python-base), providing the governed coding harness with centralized rules, skills, and multi-tool adapters.
4. **Agent Product Runtime**: [`ml-langchain-agent`](https://github.com/marcosdh1987/ml-langchain-agent), providing the application template for shipping production agent services with LangGraph.
5. **Evaluation Platform**: [`sdlc-ml-python-harness-lab`](https://github.com/xmartlabs/sdlc-ml-python-harness-lab), providing the containerized benchmarking, attribution, and regression platform.

---

## Claim Levels & Academic Rigor

To maintain scientific integrity and engineering clarity, this documentation strictly differentiates three levels of claims:

1. **Industry Evidence**: Publicly documented research, empirical findings, and architecture papers from frontier labs and standard benchmarks (such as Anthropic, OpenAI, SWE-bench, Princeton, and Microsoft Research).
2. **Guide Recommendation**: Our proposed methodologies, maturity models, and architectural patterns for engineering organizations.
3. **Reference Implementation**: Specific design decisions implemented in our reference repositories (`ml-python-base`, `ml-langchain-agent`, `company-brain-template`, and `sdlc-ml-python-harness-lab`).
