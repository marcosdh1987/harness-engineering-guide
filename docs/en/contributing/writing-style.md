# Writing Style Guide

This document establishes the canonical editorial and punctuation standards for `harness-engineering-guide`. All documentation, guides, reference implementations, and agent-generated text in this repository must comply with these guidelines.

## Punctuation and Prose Standards

To maintain human, natural, credible, and precise documentation, this repository enforces a strict punctuation rule across English and Spanish prose.

### Prohibited Punctuation in Prose

Do not use the following punctuation marks in visible prose:

1. **Double ASCII hyphens (`--`)**: do not use consecutive hyphens as an informal dash.
2. **Unicode em dashes (`—`)**: do not use em dashes to set off clauses or thoughts.
3. **Unicode en dashes (`–`)**: do not use en dashes as a stylistic dash.

### Permitted Alternatives

Instead of dash punctuation, use conventional grammatical structures:

- **Commas**: for non-restrictive clauses, parenthetical phrases, and natural pauses.
- **Parentheses**: to enclose clarifications, acronyms, or secondary context.
- **Colons**: to introduce explanations, lists, definitions, or amplifications.
- **Semicolons**: to link closely related independent clauses.
- **Periods**: to split compound thoughts into concise, direct sentences.
- **Single ASCII hyphens (`-`)**: for standard compound words (for example: `high-signal context`, `well-tested units`).

#### Examples

| Avoid | Preferred |
|---|---|
| `The harness -- not the model -- determines the workflow.` | The harness, not the model, determines the workflow. |
| `The model — even a frontier model — needs feedback.` | Even a frontier model needs feedback. |
| `Extremos — escribir el ticket, revisar el PR.` | Extremos: escribir el ticket y revisar el PR. |
| `Tres repositorios — guía, template y lab.` | Tres componentes: guía, template y lab. |

### Technical Exceptions

The prohibited sequences remain permitted only when syntactically required by technical formats:

- Fenced code blocks (such as shell sessions, Python, or YAML).
- Inline code identifiers and command flags (such as `--strict` or `--locked`).
- Markdown frontmatter delimiters (`---`).
- Markdown table structural rows (`|---|---|`).
- Markdown horizontal rules (`---`).
- URLs and hyperlink targets.
- Markdown attribute lists (such as `{.md-button--primary}`).
- Mermaid diagram syntax.

## Automated Verification

Compliance is checked mechanically by `scripts/check_prose_style.py`. Run the check locally with:

```bash
make check-style
```

This check runs automatically on every pull request and is part of `make check`.
