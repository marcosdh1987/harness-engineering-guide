# Detect if uv is available to run commands in the managed virtual environment
UV := $(shell command -v uv 2> /dev/null)

ifdef UV
  PYTHON = uv run python
else
  PYTHON = python
endif

docs-serve:
	$(PYTHON) -m mkdocs serve

docs-build:
	$(PYTHON) -m mkdocs build --strict

sync-reference:
	$(PYTHON) scripts/sync_reference_template.py

