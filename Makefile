# Detect if uv is available to run commands in the managed virtual environment
UV := $(shell command -v uv 2> /dev/null)

ifdef UV
  PYTHON = uv run python
  RUFF = uv run ruff
else
  PYTHON = python
  RUFF = ruff
endif

docs-serve:
	$(PYTHON) -m mkdocs serve

docs-build:
	$(PYTHON) -m mkdocs build --strict

sync-reference:
	$(PYTHON) scripts/sync_reference_template.py

# Auto-format and auto-fix the repo's Python (the sync script). Run this often.
fix:
	$(RUFF) check --fix scripts
	$(RUFF) format scripts

# Format only (no lint fixes).
format:
	$(RUFF) format scripts
	$(RUFF) check --select I --fix scripts

# Read-only lint (no writes) — what CI-style checks should use.
lint:
	$(RUFF) check scripts
	$(RUFF) format --check scripts

# Read-only quality gate: lint + strict docs build.
check: lint docs-build

.PHONY: docs-serve docs-build sync-reference fix format lint check

