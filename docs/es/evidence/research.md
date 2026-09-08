# Literatura de investigación

>Investigaciones revisadas por pares y preprints sobre sistemas de codificación agentic.

### Harness Engineering: Leveraging Codex in an Agent-First World
- **Proveedor / Editorial**: OpenAI
- **Enlace directo**: [https://openai.com/index/harness-engineering/](https://openai.com/index/harness-engineering/)
- **Fecha de acceso**: `2026-02-11`
- **Temas relacionados**: `harness-engineering`, `agentic-sdlc`, `worktrees`, `codex`, `system-of-record`
- **Resumen y notas**:
  Foundational engineering publication formalizing Harness Engineering from a frontier lab. Outlines the paradigm shift where humans steer while agents execute. Establishes repository knowledge as the system of record, AGENTS.md as a map rather than an encyclopedia, one app instance per git worktree, logs and metrics made agent-legible, mechanically enforced architectural invariants, and agent-to-agent reviews.

---
### Symphony: Task Orchestration and Control Plane for Autonomous Work
- **Proveedor / Editorial**: OpenAI
- **Enlace directo**: [https://openai.com/index/symphony-orchestration/](https://openai.com/index/symphony-orchestration/)
- **Fecha de acceso**: `2026-04-15`
- **Temas relacionados**: `orchestration`, `parallel-agents`, `control-plane`, `task-management`
- **Resumen y notas**:
  Introduces project management systems as the control plane for parallel autonomous agents. Formulates the separation between orchestration and model capability, treating agents as transient workers executing bounded task units against shared boards.

---
### From Production Evidence to Self-Improving Domain Agents
- **Proveedor / Editorial**: OpenAI
- **Enlace directo**: [https://openai.com/index/self-improving-agents-evidence/](https://openai.com/index/self-improving-agents-evidence/)
- **Fecha de acceso**: `2026-05-18`
- **Temas relacionados**: `continuous-improvement`, `findings`, `regression-evals`, `closed-loop`
- **Resumen y notas**:
  Establishes a disciplined pipeline for agent improvement based on empirical production corrections. Demonstrates that raw feedback must undergo human review, grouping into findings, conversion into bounded regression evals, and validated engineering tasks before mutating rules or prompt scaffolding.

---
### Designing Trustworthy Evaluations for Autonomous Agent Systems
- **Proveedor / Editorial**: OpenAI
- **Enlace directo**: [https://openai.com/index/trustworthy-agent-evals/](https://openai.com/index/trustworthy-agent-evals/)
- **Fecha de acceso**: `2026-06-10`
- **Temas relacionados**: `evaluation-engineering`, `experimental-validity`, `harness-attribution`, `budgets`
- **Resumen y notas**:
  Comprehensive methodology establishing that an evaluation measures the entire system rather than the model in isolation. Identifies model, reasoning settings, tool definitions, harness rules, token budgets, retry policies, and execution environment as combined experimental conditions.

---
### Demystifying Evals for AI Agents
- **Proveedor / Editorial**: Anthropic
- **Enlace directo**: [https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- **Fecha de acceso**: `2026-08-20`
- **Temas relacionados**: `agent-evaluations`, `graders`, `evaluation-engineering`, `regression-testing`
- **Resumen y notas**:
  Engineering guide establishing that agent evaluations test the model plus harness system across multi-step execution. Highlights the distinction between interaction transcripts and environmental outcomes, introduces the three-grader toolbox (code-based, model-based judge, and human), and outlines pass@k and pass^k reliability metrics.

---
### Quantifying Infrastructure Noise in Agentic Coding Evals
- **Proveedor / Editorial**: Anthropic
- **Enlace directo**: [https://www.anthropic.com/engineering/infrastructure-noise](https://www.anthropic.com/engineering/infrastructure-noise)
- **Fecha de acceso**: `2026-08-20`
- **Temas relacionados**: `sandboxing`, `infrastructure-noise`, `experimental-validity`, `reproducibility`
- **Resumen y notas**:
  Empirical study demonstrating that runtime infrastructure (CPU, RAM, timeouts, execution environment) is an active experimental variable in agent evaluations, causing up to a 6 percentage point swing on benchmarks like Terminal-Bench 2.0. Establishes the necessity of strict sandbox controls.

---
### Effective Context Engineering for AI Agents
- **Proveedor / Editorial**: Anthropic
- **Enlace directo**: [https://www.anthropic.com/engineering/effective-context-engineering](https://www.anthropic.com/engineering/effective-context-engineering)
- **Fecha de acceso**: `2026-03-20`
- **Temas relacionados**: `context-engineering`, `working-memory`, `subagents`, `token-budget`
- **Resumen y notas**:
  Technical guide treating context as a finite, precious resource. Outlines just-in-time selective context retrieval, context compaction, structured project memory, subagent isolation, and the impact of tool descriptions on attention allocation.

---
### Harnessing Long-Running Autonomous Agents
- **Proveedor / Editorial**: Anthropic
- **Enlace directo**: [https://www.anthropic.com/engineering/long-running-agent-harnesses](https://www.anthropic.com/engineering/long-running-agent-harnesses)
- **Fecha de acceso**: `2026-04-08`
- **Temas relacionados**: `state-and-continuity`, `long-running-agents`, `working-state`, `checkpoints`
- **Resumen y notas**:
  Architecture patterns for multi-session agent execution. Formulates progress artifacts, clean end-of-session state handoffs, incremental task logs, and resume-from-durable-artifacts protocols to overcome context window limits.

---
### Orchestrating Agent Teams in Software Engineering
- **Proveedor / Editorial**: Anthropic
- **Enlace directo**: [https://www.anthropic.com/engineering/agent-teams-software-engineering](https://www.anthropic.com/engineering/agent-teams-software-engineering)
- **Fecha de acceso**: `2026-05-12`
- **Temas relacionados**: `parallel-agents`, `agent-teams`, `worktrees`, `isolation`
- **Resumen y notas**:
  Empirical study on multi-agent collaboration across codebases. Highlights challenges of shared codebase contention, merge conflicts, and coordination overhead. Emphasizes that parallel agent execution requires isolated mutable environments and rigorous verification gates.

---
### Managed Agents and Scaffolding Evolution: When to De-scaffold
- **Proveedor / Editorial**: Anthropic
- **Enlace directo**: [https://www.anthropic.com/engineering/managed-agents-scaffolding-evolution](https://www.anthropic.com/engineering/managed-agents-scaffolding-evolution)
- **Fecha de acceso**: `2026-06-15`
- **Temas relacionados**: `adaptive-harnesses`, `de-scaffolding`, `capability-drift`, `ablation-testing`
- **Resumen y notas**:
  Formulates the principle of adaptive harnesses: harnesses encode assumptions about model limitations, and as frontier models advance, older scaffolding becomes obsolete overhead. Advocates for routine ablation testing to simplify rules and retire unnecessary skills.

---
### OpenSpec: Change-Oriented Specifications and Brownfield Agent Workflows
- **Proveedor / Editorial**: OpenSpec Project
- **Enlace directo**: [https://openspec.dev/](https://openspec.dev/)
- **Fecha de acceso**: `2026-04-22`
- **Temas relacionados**: `openspec`, `brownfield-development`, `artifact-dependency-graphs`
- **Resumen y notas**:
  Open specification framework designed for brownfield development and complex changes. Uses artifact dependency graphs linking proposals, domain specifications, technical designs, and verifiable tasks.

---
### SWE-bench: Evaluation Harness and Environment Isolation
- **Proveedor / Editorial**: Princeton University / SWE-bench Team
- **Enlace directo**: [https://www.swebench.com/](https://www.swebench.com/)
- **Fecha de acceso**: `2026-08-20`
- **Temas relacionados**: `benchmarks`, `sandboxing`, `reproducibility`, `swe-bench`
- **Resumen y notas**:
  Standard benchmark for resolving real-world GitHub issues. Utilizes containerized Docker environments per issue instance to guarantee reproducible dependencies, isolate execution side-effects, and validate patches through execution of gold test suites.

---
### NVIDIA Agentic AI and Software Engineering Patterns
- **Proveedor / Editorial**: NVIDIA
- **Enlace directo**: [https://developer.nvidia.com/blog/agentic-ai-software-engineering/](https://developer.nvidia.com/blog/agentic-ai-software-engineering/)
- **Fecha de acceso**: `2026-06-24`
- **Temas relacionados**: `agentic-ai`, `validation-loops`, `software-maintenance`
- **Resumen y notas**:
  Detailed architecture study on deploying autonomous agent networks for software maintenance. Emphasizes strict pre-merge verification, multi-agent validation loops, and structured rules.

---
### SWE-agent: Agent-Computer Interfaces for Software Engineering
- **Proveedor / Editorial**: Princeton University
- **Enlace directo**: [https://arxiv.org/abs/2405.15793](https://arxiv.org/abs/2405.15793)
- **Fecha de acceso**: `2026-06-24`
- **Temas relacionados**: `agentic-coding`, `agent-computer-interfaces`, `repository-benchmarks`
- **Resumen y notas**:
  Academic research paper demonstrating that agent performance on complex repository-level tasks depends heavily on tailored Agent-Computer Interfaces (ACIs). Validates the use of explicit command limitations and structured rules.

---
### AutoDev: Automated Software Development Framework
- **Proveedor / Editorial**: Microsoft Research
- **Enlace directo**: [https://arxiv.org/abs/2403.08299](https://arxiv.org/abs/2403.08299)
- **Fecha de acceso**: `2026-06-24`
- **Temas relacionados**: `sandbox-execution`, `quality-gates`, `autonomous-collaboration`
- **Resumen y notas**:
  Introduces the AutoDev framework, establishing autonomous agent collaborations where coding, compilation, testing, and Git operations are run within secure execution sandboxes under strict quality gates.

---
### ISO 30401:2018 Knowledge management systems: Requirements
- **Proveedor / Editorial**: International Organization for Standardization (ISO)
- **Enlace directo**: [https://www.iso.org/standard/68683.html](https://www.iso.org/standard/68683.html)
- **Fecha de acceso**: `2026-07-24`
- **Temas relacionados**: `knowledge-management`, `organizational-governance`, `iso-standards`
- **Resumen y notas**:
  International standard defining requirement principles for establishing, implementing, and maintaining effective knowledge management systems in organizations.

---
