# Literatura de investigación

>Investigaciones revisadas por pares y preprints sobre sistemas de codificación agentic.

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
### ISO 30401:2018 Knowledge management systems — Requirements
- **Proveedor / Editorial**: International Organization for Standardization (ISO)
- **Enlace directo**: [https://www.iso.org/standard/68683.html](https://www.iso.org/standard/68683.html)
- **Fecha de acceso**: `2026-07-24`
- **Temas relacionados**: `knowledge-management`, `organizational-governance`, `iso-standards`
- **Resumen y notas**:
  International standard defining requirement principles for establishing, implementing, and maintaining effective knowledge management systems in organizations.

---
