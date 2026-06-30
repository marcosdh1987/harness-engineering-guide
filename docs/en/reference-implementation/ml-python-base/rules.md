# Governance & Rules System

> [!NOTE]
> **Generated content**: This page is automatically generated from the template snapshot.
> - **Reference Commit**: [1fc65a8](https://github.com/marcosdh1987/ml-python-base/commit/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0) on branch `main`
> - **Last Synced**: `2026-06-30T12:49:58.403597Z`
> - **Reference Artifacts**:
>   - [.github/architecture.md](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.github/architecture.md)
>   - [.github/standards.md](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.github/standards.md)
>   - [.github/domain-boundaries.md](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.github/domain-boundaries.md)
>   - [.github/automation.md](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.github/automation.md)
>   - [.github/orchestration.md](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/.github/orchestration.md)
> *Note: This is a study summary and index. The authoritative implementation and governance remain in the source repository.*
## Structured Governance

The reference implementation structures governance into five dedicated rule files located under `.github/`. They establish Level 3 (Automation) and Level 4 (Orchestration) quality gates that AI coding tools must conform to.

### 1. Architecture Governance (`.github/architecture.md`)
Defines the architectural layout and module boundaries to prevent design drift.
- **Key Principle**: Enforces Single Responsibility Principle (SRP) and separation of business logic from infrastructure.
- **Preferred Layering**: Enforces a Clean Architecture layout:
  1. **Domain layer**: entities, value objects, core rules (must not depend on infrastructure).
  2. **Application layer**: use cases and orchestration.
  3. **Infrastructure layer**: frameworks, database adapters, external providers, APIs.

### 2. Engineering Standards (`.github/standards.md`)
Details development guidelines, language policies, tool execution pathways, and pre-finalization checklists.
- **Language Policy**: Interaction language follows user language, but all code artifacts (identifiers, docstrings, comments, generated documentation) **must remain in English**.
- **Tool Command Policy**: Prioritizes `Makefile` targets. Never execute `pip install` directly; use `uv` workflows.
- **Validation Checklist**:
  1. Code artifacts are in English.
  2. Relevant quality checks ran (`make check` or targeted tests).
  3. Data flows respect boundaries.
  4. Changes include updating documentation under `docs/`.

### 3. Domain Boundaries (`.github/domain-boundaries.md`)
Defines repository zones and data isolation boundaries to limit model generation scopes.
- **Repository Zones**: `src/` (production code), `tests/` (testing), `notebooks/` (prototyping).
- **Data Zones**: Enforces read-only immutable raw data under `data/raw/` and transform-only features under `data/processed/`.

### 4. Automation Policy (`.github/automation.md`)
Defines Level 3 enforcement so quality is verified programmatically and does not depend on model compliance.
- **CI is Read-Only**: CI only verifies and never mutates the working tree. Targets like `make format` are strictly local.
- **Drift Guard**: `make check` executes `uv sync --locked --exact` to align the environment exactly with the lockfile, preventing undeclared dependency leaks.

### 5. Orchestration Policy (`.github/orchestration.md`)
Establishes Level 4 workflow execution guidelines for complex programming tasks.
- **Plan-First**: Requires drawing an explicit implementation plan before writing code.
- **Diff Review**: Mandates model and developer reviews of Git diffs before finalizing to prune boundary violations.
- **Orchestration Route**: Prioritizes internal skill execution over generic model generation.
