# Detect if uv is available to run commands in the managed virtual environment
UV := $(shell command -v uv 2> /dev/null)

ifdef UV
  PYTHON = uv run python
  RUFF = uv run ruff
  PYTEST = uv run pytest
else
  PYTHON = python
  RUFF = ruff
  PYTEST = pytest
endif

docs-serve:
	$(PYTHON) -m mkdocs serve

docs-build:
	$(PYTHON) -m mkdocs build --strict

sync-reference:
	$(PYTHON) scripts/sync_reference_template.py

check-style:
	$(PYTHON) scripts/check_prose_style.py --strict docs README.md

check-drift:
	$(PYTHON) scripts/check_reference_drift.py

test:
	$(PYTEST) tests

# Auto-format and auto-fix the repo's Python code. Run this often.
fix:
	$(RUFF) check --fix scripts tests
	$(RUFF) format scripts tests

# Format only (no lint fixes).
format:
	$(RUFF) format scripts tests
	$(RUFF) check --select I --fix scripts tests

# Read-only lint (no writes) for CI and quality gates.
lint:
	$(RUFF) check scripts tests
	$(RUFF) format --check scripts tests

# Read-only quality gate: lint + prose style + reference drift + tests + strict docs build.
check: lint check-style check-drift test docs-build

.PHONY: docs-serve docs-build sync-reference check-style check-drift test fix format lint check

