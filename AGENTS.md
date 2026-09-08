# AGENTS.md

## Repository Purpose

This repository hosts the canonical Harness Engineering Guide. It contains bilingual technical documentation, architecture patterns, evaluation methodology, and reference implementation mappings.

## Canonical Commands

- `make check`: Complete quality gate (lint, prose style, reference drift, tests, strict docs build).
- `make check-style`: Check prose punctuation style across markdown files.
- `make check-drift`: Check reference template snapshot drift.
- `make test`: Execute pytest suite in `tests/`.
- `make docs-build`: Strict MkDocs build.
- `make sync-reference`: Synchronize `ml-python-base` snapshot and evidence pages.

## Editorial Prose Rule

When writing human-facing prose in this repository, do not use double ASCII hyphens (`--`), Unicode em dashes (`—`), or Unicode en dashes (`–`) as punctuation. Use commas, periods, colons, semicolons, parentheses, or ordinary single hyphens instead. Preserve these characters only when required by code, commands, URLs, Markdown structure, or technical syntax.

Refer to `docs/contributing/writing-style.md` for details.

## Bilingual Parity

All documentation pages in `docs/en/` must have a corresponding, semantically aligned page in `docs/es/`. Navigation changes must be mirrored symmetrically in `mkdocs.yml`.
