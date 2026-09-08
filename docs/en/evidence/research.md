# Research Literature

>Peer-reviewed research and preprint papers on agentic coding systems.

### Harness Engineering: Leveraging Codex in an Agent-First World
- **Provider / Publisher**: OpenAI
- **Direct Link**: [https://openai.com/index/harness-engineering/](https://openai.com/index/harness-engineering/)
- **Accessed Date**: `2026-02-11`
- **Related Topics**: `harness-engineering`, `agentic-sdlc`, `worktrees`, `codex`, `system-of-record`
- **Summary & Notes**:
  Foundational engineering publication formalizing Harness Engineering from a frontier lab. Outlines the paradigm shift where humans steer while agents execute. Establishes repository knowledge as the system of record, AGENTS.md as a map rather than an encyclopedia, one app instance per git worktree, logs and metrics made agent-legible, mechanically enforced architectural invariants, and agent-to-agent reviews.

---
### Symphony: Task Orchestration and Control Plane for Autonomous Work
- **Provider / Publisher**: OpenAI
- **Direct Link**: [https://openai.com/index/symphony-orchestration/](https://openai.com/index/symphony-orchestration/)
- **Accessed Date**: `2026-04-15`
- **Related Topics**: `orchestration`, `parallel-agents`, `control-plane`, `task-management`
- **Summary & Notes**:
  Introduces project management systems as the control plane for parallel autonomous agents. Formulates the separation between orchestration and model capability, treating agents as transient workers executing bounded task units against shared boards.

---
### From Production Evidence to Self-Improving Domain Agents
- **Provider / Publisher**: OpenAI
- **Direct Link**: [https://openai.com/index/self-improving-agents-evidence/](https://openai.com/index/self-improving-agents-evidence/)
- **Accessed Date**: `2026-05-18`
- **Related Topics**: `continuous-improvement`, `findings`, `regression-evals`, `closed-loop`
- **Summary & Notes**:
  Establishes a disciplined pipeline for agent improvement based on empirical production corrections. Demonstrates that raw feedback must undergo human review, grouping into findings, conversion into bounded regression evals, and validated engineering tasks before mutating rules or prompt scaffolding.

---
### Designing Trustworthy Evaluations for Autonomous Agent Systems
- **Provider / Publisher**: OpenAI
- **Direct Link**: [https://openai.com/index/trustworthy-agent-evals/](https://openai.com/index/trustworthy-agent-evals/)
- **Accessed Date**: `2026-06-10`
- **Related Topics**: `evaluation-engineering`, `experimental-validity`, `harness-attribution`, `budgets`
- **Summary & Notes**:
  Comprehensive methodology establishing that an evaluation measures the entire system rather than the model in isolation. Identifies model, reasoning settings, tool definitions, harness rules, token budgets, retry policies, and execution environment as combined experimental conditions.

---
### Demystifying Evals for AI Agents
- **Provider / Publisher**: Anthropic
- **Direct Link**: [https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- **Accessed Date**: `2026-08-20`
- **Related Topics**: `agent-evaluations`, `graders`, `evaluation-engineering`, `regression-testing`
- **Summary & Notes**:
  Engineering guide establishing that agent evaluations test the model plus harness system across multi-step execution. Highlights the distinction between interaction transcripts and environmental outcomes, introduces the three-grader toolbox (code-based, model-based judge, and human), and outlines pass@k and pass^k reliability metrics.

---
### Quantifying Infrastructure Noise in Agentic Coding Evals
- **Provider / Publisher**: Anthropic
- **Direct Link**: [https://www.anthropic.com/engineering/infrastructure-noise](https://www.anthropic.com/engineering/infrastructure-noise)
- **Accessed Date**: `2026-08-20`
- **Related Topics**: `sandboxing`, `infrastructure-noise`, `experimental-validity`, `reproducibility`
- **Summary & Notes**:
  Empirical study demonstrating that runtime infrastructure (CPU, RAM, timeouts, execution environment) is an active experimental variable in agent evaluations, causing up to a 6 percentage point swing on benchmarks like Terminal-Bench 2.0. Establishes the necessity of strict sandbox controls.

---
### Effective Context Engineering for AI Agents
- **Provider / Publisher**: Anthropic
- **Direct Link**: [https://www.anthropic.com/engineering/effective-context-engineering](https://www.anthropic.com/engineering/effective-context-engineering)
- **Accessed Date**: `2026-03-20`
- **Related Topics**: `context-engineering`, `working-memory`, `subagents`, `token-budget`
- **Summary & Notes**:
  Technical guide treating context as a finite, precious resource. Outlines just-in-time selective context retrieval, context compaction, structured project memory, subagent isolation, and the impact of tool descriptions on attention allocation.

---
### Harnessing Long-Running Autonomous Agents
- **Provider / Publisher**: Anthropic
- **Direct Link**: [https://www.anthropic.com/engineering/long-running-agent-harnesses](https://www.anthropic.com/engineering/long-running-agent-harnesses)
- **Accessed Date**: `2026-04-08`
- **Related Topics**: `state-and-continuity`, `long-running-agents`, `working-state`, `checkpoints`
- **Summary & Notes**:
  Architecture patterns for multi-session agent execution. Formulates progress artifacts, clean end-of-session state handoffs, incremental task logs, and resume-from-durable-artifacts protocols to overcome context window limits.

---
### Orchestrating Agent Teams in Software Engineering
- **Provider / Publisher**: Anthropic
- **Direct Link**: [https://www.anthropic.com/engineering/agent-teams-software-engineering](https://www.anthropic.com/engineering/agent-teams-software-engineering)
- **Accessed Date**: `2026-05-12`
- **Related Topics**: `parallel-agents`, `agent-teams`, `worktrees`, `isolation`
- **Summary & Notes**:
  Empirical study on multi-agent collaboration across codebases. Highlights challenges of shared codebase contention, merge conflicts, and coordination overhead. Emphasizes that parallel agent execution requires isolated mutable environments and rigorous verification gates.

---
### Managed Agents and Scaffolding Evolution: When to De-scaffold
- **Provider / Publisher**: Anthropic
- **Direct Link**: [https://www.anthropic.com/engineering/managed-agents-scaffolding-evolution](https://www.anthropic.com/engineering/managed-agents-scaffolding-evolution)
- **Accessed Date**: `2026-06-15`
- **Related Topics**: `adaptive-harnesses`, `de-scaffolding`, `capability-drift`, `ablation-testing`
- **Summary & Notes**:
  Formulates the principle of adaptive harnesses: harnesses encode assumptions about model limitations, and as frontier models advance, older scaffolding becomes obsolete overhead. Advocates for routine ablation testing to simplify rules and retire unnecessary skills.

---
### OpenSpec: Change-Oriented Specifications and Brownfield Agent Workflows
- **Provider / Publisher**: OpenSpec Project
- **Direct Link**: [https://openspec.dev/](https://openspec.dev/)
- **Accessed Date**: `2026-04-22`
- **Related Topics**: `openspec`, `brownfield-development`, `artifact-dependency-graphs`
- **Summary & Notes**:
  Open specification framework designed for brownfield development and complex changes. Uses artifact dependency graphs linking proposals, domain specifications, technical designs, and verifiable tasks.

---
### SWE-bench: Evaluation Harness and Environment Isolation
- **Provider / Publisher**: Princeton University / SWE-bench Team
- **Direct Link**: [https://www.swebench.com/](https://www.swebench.com/)
- **Accessed Date**: `2026-08-20`
- **Related Topics**: `benchmarks`, `sandboxing`, `reproducibility`, `swe-bench`
- **Summary & Notes**:
  Standard benchmark for resolving real-world GitHub issues. Utilizes containerized Docker environments per issue instance to guarantee reproducible dependencies, isolate execution side-effects, and validate patches through execution of gold test suites.

---
### NVIDIA Agentic AI and Software Engineering Patterns
- **Provider / Publisher**: NVIDIA
- **Direct Link**: [https://developer.nvidia.com/blog/agentic-ai-software-engineering/](https://developer.nvidia.com/blog/agentic-ai-software-engineering/)
- **Accessed Date**: `2026-06-24`
- **Related Topics**: `agentic-ai`, `validation-loops`, `software-maintenance`
- **Summary & Notes**:
  Detailed architecture study on deploying autonomous agent networks for software maintenance. Emphasizes strict pre-merge verification, multi-agent validation loops, and structured rules.

---
### SWE-agent: Agent-Computer Interfaces for Software Engineering
- **Provider / Publisher**: Princeton University
- **Direct Link**: [https://arxiv.org/abs/2405.15793](https://arxiv.org/abs/2405.15793)
- **Accessed Date**: `2026-06-24`
- **Related Topics**: `agentic-coding`, `agent-computer-interfaces`, `repository-benchmarks`
- **Summary & Notes**:
  Academic research paper demonstrating that agent performance on complex repository-level tasks depends heavily on tailored Agent-Computer Interfaces (ACIs). Validates the use of explicit command limitations and structured rules.

---
### AutoDev: Automated Software Development Framework
- **Provider / Publisher**: Microsoft Research
- **Direct Link**: [https://arxiv.org/abs/2403.08299](https://arxiv.org/abs/2403.08299)
- **Accessed Date**: `2026-06-24`
- **Related Topics**: `sandbox-execution`, `quality-gates`, `autonomous-collaboration`
- **Summary & Notes**:
  Introduces the AutoDev framework, establishing autonomous agent collaborations where coding, compilation, testing, and Git operations are run within secure execution sandboxes under strict quality gates.

---
### ISO 30401:2018 Knowledge management systems: Requirements
- **Provider / Publisher**: International Organization for Standardization (ISO)
- **Direct Link**: [https://www.iso.org/standard/68683.html](https://www.iso.org/standard/68683.html)
- **Accessed Date**: `2026-07-24`
- **Related Topics**: `knowledge-management`, `organizational-governance`, `iso-standards`
- **Summary & Notes**:
  International standard defining requirement principles for establishing, implementing, and maintaining effective knowledge management systems in organizations.

---
