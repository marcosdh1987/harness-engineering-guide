# CLAUDE.md

## Repository Overview

`harness-engineering-guide` is a bilingual (English and Spanish) MkDocs documentation repository defining the principles, patterns, reference implementations, and evaluation engineering of Harness Engineering in AI-assisted software development.

## Quality Gates and Commands

Always use the following commands to validate work:

- `make check`: Full quality gate (lint, prose style, reference drift, tests, strict docs build).
- `make check-style`: Check prose punctuation style across markdown files.
- `make check-drift`: Detect drift between reference snapshot and `ml-python-base`.
- `make test`: Run unit tests for scripts and tools via pytest.
- `make lint`: Read-only lint and format check using Ruff.
- `make fix`: Auto-format and auto-fix Python scripts using Ruff.
- `make docs-build`: Build documentation in strict mode (`mkdocs build --strict`).
- `make docs-serve`: Start local MkDocs preview server.
- `make sync-reference`: Synchronize template snapshot and generated reference pages.

## Editorial Prose Policy (Mandatory)

When writing human-facing prose in this repository:

1. **No double ASCII hyphens (`--`)**: do not use consecutive hyphens as punctuation in text.
2. **No Unicode em dashes (`—`)**: do not use em dashes to set off clauses.
3. **No Unicode en dashes (`–`)**: do not use en dashes as a stylistic dash.
4. **Use standard alternatives**: commas, periods, colons, semicolons, parentheses, or ordinary single hyphens for compound words.
5. **Technical syntax preserved**: double hyphens, em dashes, or en dashes are allowed ONLY inside fenced code blocks, inline code, command line flags (e.g. `--strict`), URLs, frontmatter, Markdown table rows, and Mermaid blocks.

See `docs/contributing/writing-style.md` for complete guidelines.

## Content & Architectural Guidelines

- **5-Layer Ecosystem**:
  1. Method: `harness-engineering-guide`
  2. Knowledge: `company-brain-template`
  3. Governance: `ml-python-base`
  4. Runtime: `ml-langchain-agent`
  5. Evaluation: `sdlc-ml-python-harness-lab`
- **Context Architecture**: Systems of Record → Company Brain → Engineering Harness.
- **Bilingual Parity**: Every content change must exist in both English (`docs/en/`) and Spanish (`docs/es/`).
- **Assertion Rigor**: Explicitly distinguish Industry Evidence (cited with primary source), Guide Recommendation, and Reference Implementation.
