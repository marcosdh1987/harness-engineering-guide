"""tests/test_check_prose_style.py

Unit tests for scripts/check_prose_style.py.
"""

from scripts.check_prose_style import check_file_content


def test_valid_prose_passes():
    content = """# Valid Heading

This is a clean sentence with normal punctuation: commas, colons, and semicolons; everything is fine.
We also support standard single-hyphen words like high-signal context and well-tested units.
"""
    violations = check_file_content(content)
    assert len(violations) == 0


def test_invalid_em_dash_detected():
    content = """This sentence uses an em dash — which is forbidden in prose."""
    violations = check_file_content(content)
    assert len(violations) == 1
    assert violations[0].matched_text == "—"
    assert "no-em-dash" in violations[0].rule


def test_invalid_en_dash_detected():
    content = """This sentence uses an en dash – which is forbidden in prose."""
    violations = check_file_content(content)
    assert len(violations) == 1
    assert violations[0].matched_text == "–"
    assert "no-en-dash" in violations[0].rule


def test_invalid_double_hyphen_detected():
    content = """The harness -- not the model -- determines the workflow."""
    violations = check_file_content(content)
    assert len(violations) == 2
    assert violations[0].matched_text == "--"
    assert "no-double-hyphen" in violations[0].rule


def test_fenced_code_blocks_ignored():
    content = """Here is code:

```bash
uv run python -m mkdocs build --strict
git log --oneline -n 5
```

```mermaid
flowchart LR
    A --> B
    C --- D
```

And back to valid prose.
"""
    violations = check_file_content(content)
    assert len(violations) == 0


def test_inline_code_ignored():
    content = """Run `make check --strict` and inspect `--locked` flags in `pyproject.toml`."""
    violations = check_file_content(content)
    assert len(violations) == 0


def test_frontmatter_ignored():
    content = """---
title: My Document
tags: [harness, engineering]
custom_flag: --ignore-legacy
---

# Title

Clean prose goes here.
"""
    violations = check_file_content(content)
    assert len(violations) == 0


def test_markdown_tables_and_rules_ignored():
    content = """| Header 1 | Header 2 |
|---|---|
| Cell 1 | Cell 2 |

---

More clean prose.
"""
    violations = check_file_content(content)
    assert len(violations) == 0


def test_urls_with_hyphens_ignored_in_links():
    content = """Check the [OpenAI Codex guide](https://platform.openai.com/docs/guides/code--execution) for details."""
    violations = check_file_content(content)
    assert len(violations) == 0


def test_attribute_lists_ignored():
    content = """- [English](en/index.md){ .md-button .md-button--primary }"""
    violations = check_file_content(content)
    assert len(violations) == 0


def test_multiline_html_comments_ignored():
    content = """<!--
This is an HTML comment with -- double hyphens and — em dashes.
-->
This is clean prose.
"""
    violations = check_file_content(content)
    assert len(violations) == 0
