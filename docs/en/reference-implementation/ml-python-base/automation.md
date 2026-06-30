# Makefile Automation Workflows

> [!NOTE]
> **Generated content**: This page is automatically generated from the template snapshot.
> - **Reference Commit**: [1fc65a8](https://github.com/marcosdh1987/ml-python-base/commit/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0) on branch `main`
> - **Last Synced**: `2026-06-30T12:49:58.403597Z`
> - **Reference Artifacts**:
>   - [Makefile](https://github.com/marcosdh1987/ml-python-base/blob/1fc65a8b6cef84e9aa40ed333a8a78475cbb22a0/Makefile)
> *Note: This is a study summary and index. The authoritative implementation and governance remain in the source repository.*
## Command Automation Matrix

The template repository centralizes all local development commands and quality gates in a single `Makefile` utilizing `uv` for environment management.

### Key Makefile Targets

| Target Command | Execution Nature | Core Purpose / Actions |
|---|---|---|
| `make install` | Local-Mutating | Installs `uv`, pins Python version, and builds the local `.venv` exactly according to `uv.lock`. |
| `make format` | Local-Mutating | Automatically runs Ruff formatting and import sorting across `src/`, `tests/`, and `scripts/`. |
| `make fix` | Local-Mutating | Applies safe linter autofixes and formatting. |
| `make toolbelt-doctor` | Local-Safe (Read-Only) | Checks for installed CLIs and probes configured local service endpoints. |
| `make check` | CI-Safe (Read-Only) | **CI Quality Gate**: Lock-syncs `.venv` with `uv sync --locked --exact`, checks Ruff formatting/linting, executes security checks (Bandit), runs Mypy type-checking, and executes tests with coverage. |
| `make sync-skills` | Local-Mutating | Triggers the centralized sync engine to link skills, project agents, and rewrite generated adapter skill regions. |
| `make check-sync` | CI-Safe (Read-Only) | **CI Drift Gate**: Validates that no local adapter files, native skill links, or manifests have drifted from the governed sources. |
| `make ci` | CI-Safe (Read-Only) | Runs the complete CI pipeline: `make check` followed by `make check-sync`. |

### Local-Mutating vs CI-Safe (Read-Only) Workflows

- **CI-Safe (Read-Only)** targets never modify files in the working directory (besides environment sync inside `.venv`). They assert state and fail fast if checks fail.
- **Local-Mutating** targets write changes, formats, or refactors back to the disk. These should only be run by developers locally.
