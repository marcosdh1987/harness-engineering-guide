# Research Literature

>Peer-reviewed research and preprint papers on agentic coding systems.

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
### ISO 30401:2018 Knowledge management systems — Requirements
- **Provider / Publisher**: International Organization for Standardization (ISO)
- **Direct Link**: [https://www.iso.org/standard/68683.html](https://www.iso.org/standard/68683.html)
- **Accessed Date**: `2026-07-24`
- **Related Topics**: `knowledge-management`, `organizational-governance`, `iso-standards`
- **Summary & Notes**:
  International standard defining requirement principles for establishing, implementing, and maintaining effective knowledge management systems in organizations.

---
