#!/usr/bin/env python3
"""scripts/curate_prose_dashes.py

Carefully transforms forbidden dashes in prose into clean commas, colons,
parentheses, semicolons, or single hyphens without altering code or technical syntax.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from scripts.check_prose_style import check_file, discover_files


def curate_line(line: str) -> str:
    # 1. Protect inline code snippets
    code_snippets: list[str] = []

    def save_code(m: re.Match[str]) -> str:
        idx = len(code_snippets)
        code_snippets.append(m.group(0))
        return f"__INLINE_CODE_{idx}__"

    protected = re.sub(r"`[^`\n]+`", save_code, line)

    # 2. Protect link URLs
    link_urls: list[str] = []

    def save_url(m: re.Match[str]) -> str:
        idx = len(link_urls)
        link_urls.append(m.group(1))
        return f"](__LINK_URL_{idx}__)"

    protected = re.sub(r"\]\(([^)]+)\)", save_url, protected)

    # 3. Protect HTML tags
    html_tags: list[str] = []

    def save_html(m: re.Match[str]) -> str:
        idx = len(html_tags)
        html_tags.append(m.group(0))
        return f"__HTML_TAG_{idx}__"

    protected = re.sub(r"<[^>\n]+>", save_html, protected)

    # 4. Protect Markdown attribute lists {: .class }
    attr_lists: list[str] = []

    def save_attr(m: re.Match[str]) -> str:
        idx = len(attr_lists)
        attr_lists.append(m.group(0))
        return f"__ATTR_LIST_{idx}__"

    protected = re.sub(r"\{[^{}\n]*\}", save_attr, protected)

    # Transform prose punctuation
    # Item definition: **Item** — description -> **Item**: description
    protected = re.sub(r"\*\* — ", "**: ", protected)
    protected = re.sub(r"\] — ", "]: ", protected)

    # Paired em dashes: word — inner — word -> word (inner) word or word, inner, word
    # E.g. "texto —explicación— texto" or "word — explanation — word"
    def repl_paired_dash(m: re.Match[str]) -> str:
        inner = m.group(1).strip()
        return f" ({inner}) "

    protected = re.sub(r"\s*—\s*([^—\n]+?)\s*—\s*", repl_paired_dash, protected)
    protected = re.sub(r"\s*--\s*([^-\n]+?)\s*--\s*", repl_paired_dash, protected)

    # Any remaining spaced em-dashes: " — " -> ", " or ": " depending on context
    protected = re.sub(r" — ", ", ", protected)

    # Any remaining unspaced em-dash: "—" -> ", "
    protected = re.sub(r"—", ", ", protected)

    # Any en-dash between digits (ranges): 1–5 -> 1-5
    protected = re.sub(r"(\d+)–(\d+)", r"\1-\2", protected)
    # Remaining en-dashes
    protected = re.sub(r"\s*–\s*", ", ", protected)
    protected = re.sub(r"–", "-", protected)

    # Any remaining double hyphens in prose: " -- " -> ", "
    protected = re.sub(r" -- ", ", ", protected)

    # Restore protected elements
    for idx, attr in enumerate(attr_lists):
        protected = protected.replace(f"__ATTR_LIST_{idx}__", attr)
    for idx, tag in enumerate(html_tags):
        protected = protected.replace(f"__HTML_TAG_{idx}__", tag)
    for idx, url in enumerate(link_urls):
        protected = protected.replace(f"__LINK_URL_{idx}__", url)
    for idx, code in enumerate(code_snippets):
        protected = protected.replace(f"__INLINE_CODE_{idx}__", code)

    return protected


def curate_file(path: Path) -> int:
    content = path.read_text(encoding="utf-8")
    lines = content.splitlines(keepends=True)
    out_lines: list[str] = []

    in_frontmatter = False
    in_code_fence = False
    in_html_comment = False
    changes = 0

    for idx, line in enumerate(lines, 1):
        stripped = line.strip()

        if idx == 1 and stripped == "---":
            in_frontmatter = True
            out_lines.append(line)
            continue
        if in_frontmatter:
            if stripped == "---":
                in_frontmatter = False
            out_lines.append(line)
            continue

        if "<!--" in line and "-->" not in line:
            in_html_comment = True
            out_lines.append(line)
            continue
        if in_html_comment:
            if "-->" in line:
                in_html_comment = False
            out_lines.append(line)
            continue

        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_code_fence = not in_code_fence
            out_lines.append(line)
            continue
        if in_code_fence:
            out_lines.append(line)
            continue

        # Skip markdown horizontal rule
        if re.match(r"^\s*([-*_])(\s*\1){2,}\s*$", stripped):
            out_lines.append(line)
            continue

        # Skip markdown table separator row
        if re.match(r"^\s*\|?(\s*:?-+:?\s*\|)+\s*:?-+:?\s*\|?\s*$", stripped):
            out_lines.append(line)
            continue

        new_line = curate_line(line)
        if new_line != line:
            changes += 1
        out_lines.append(new_line)

    if changes > 0:
        path.write_text("".join(out_lines), encoding="utf-8")

    return changes


def main() -> int:
    files = discover_files(["docs", "README.md"])
    total_curated = 0
    files_changed = 0

    for f in files:
        if check_file(f):
            count = curate_file(f)
            if count > 0:
                files_changed += 1
                total_curated += count

    print(f"Curated {total_curated} line(s) across {files_changed} file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
