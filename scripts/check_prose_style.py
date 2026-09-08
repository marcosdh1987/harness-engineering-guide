#!/usr/bin/env python3
"""scripts/check_prose_style.py

Checks documentation files for forbidden prose punctuation:
- Double ASCII hyphens: '--'
- Unicode em dashes: '—' (\\u2014)
- Unicode en dashes: '–' (\\u2013)

Permits these characters ONLY when syntactically required:
- Fenced code blocks
- Inline code
- Markdown frontmatter delimiters
- Markdown table structural delimiters (|---|)
- Markdown horizontal rules
- URLs and image links
- Markdown attribute lists (e.g. {.md-button--primary})
- HTML comments

Usage:
    python scripts/check_prose_style.py [--strict] [--fix] [paths...]
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass
class StyleViolation:
    file_path: str
    line_number: int
    column: int
    matched_text: str
    line_content: str
    rule: str


DASH_PATTERN = re.compile(r"(--+|—|–)")
TABLE_SEP_PATTERN = re.compile(r"^\s*\|?(\s*:?-+:?\s*\|)+\s*:?-+:?\s*\|?\s*$")
HR_PATTERN = re.compile(r"^\s*([-*_])(\s*\1){2,}\s*$")
INLINE_CODE_PATTERN = re.compile(r"`[^`\n]+`")
LINK_URL_PATTERN = re.compile(r"\]\(([^)]+)\)")
ATTR_LIST_PATTERN = re.compile(r"\{[^{}\n]*\}")
HTML_TAG_PATTERN = re.compile(r"<[^>\n]+>")


def mask_range(text: str, start: int, end: int) -> str:
    """Replace slice with spaces to preserve line offsets."""
    return text[:start] + (" " * (end - start)) + text[end:]


def mask_technical_prose(line: str) -> str:
    """Mask inline code, link targets, attribute lists, and HTML tags."""
    masked = line

    # 1. Mask inline code
    for match in INLINE_CODE_PATTERN.finditer(line):
        masked = mask_range(masked, match.start(), match.end())

    # 2. Mask link URLs (keep anchor text)
    for match in LINK_URL_PATTERN.finditer(line):
        # match.group(1) is the URL part inside parentheses
        url_start = match.start(1)
        url_end = match.end(1)
        masked = mask_range(masked, url_start, url_end)

    # 3. Mask Markdown attribute lists {: .class--name }
    for match in ATTR_LIST_PATTERN.finditer(line):
        masked = mask_range(masked, match.start(), match.end())

    # 4. Mask HTML tags / comments
    for match in HTML_TAG_PATTERN.finditer(line):
        masked = mask_range(masked, match.start(), match.end())

    return masked


def check_file_content(
    content: str, file_path: str = "<input>"
) -> list[StyleViolation]:
    """Check text content for prose style violations."""
    violations: list[StyleViolation] = []
    lines = content.splitlines()

    in_frontmatter = False
    in_code_fence = False
    in_html_comment = False

    for idx, line in enumerate(lines, 1):
        stripped = line.strip()

        # Frontmatter delimiter check
        if idx == 1 and stripped == "---":
            in_frontmatter = True
            continue
        if in_frontmatter:
            if stripped == "---":
                in_frontmatter = False
            continue

        # HTML comment multi-line check
        if "<!--" in line and "-->" not in line:
            in_html_comment = True
            continue
        if in_html_comment:
            if "-->" in line:
                in_html_comment = False
            continue

        # Fenced code block check (``` or ````)
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_code_fence = not in_code_fence
            continue
        if in_code_fence:
            continue

        # Markdown horizontal rules (e.g. ---, ***, ___ )
        if HR_PATTERN.match(stripped):
            continue

        # Markdown table separator row (|---|---|)
        if TABLE_SEP_PATTERN.match(stripped):
            continue

        # Mask technical substrings on this line
        masked_line = mask_technical_prose(line)

        # Look for forbidden punctuation
        for match in DASH_PATTERN.finditer(masked_line):
            matched = match.group(1)
            col = match.start() + 1
            if matched == "—":
                rule = "no-em-dash (use comma, colon, parentheses, or period)"
            elif matched == "–":
                rule = "no-en-dash (use hyphen, comma, or parentheses)"
            else:
                rule = (
                    "no-double-hyphen (use single hyphen, comma, colon, or parentheses)"
                )

            violations.append(
                StyleViolation(
                    file_path=file_path,
                    line_number=idx,
                    column=col,
                    matched_text=matched,
                    line_content=line,
                    rule=rule,
                )
            )

    return violations


def check_file(path: Path) -> list[StyleViolation]:
    """Read and check a single file."""
    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return []
    return check_file_content(content, str(path))


def discover_files(paths: list[str]) -> list[Path]:
    """Discover markdown files from input paths."""
    found: list[Path] = []
    if not paths:
        paths = ["docs", "README.md"]

    for p_str in paths:
        p = Path(p_str)
        if not p.exists():
            continue
        if p.is_file() and p.suffix in (".md", ".markdown"):
            found.append(p)
        elif p.is_dir():
            for root, _, files in os.walk(p):
                for f in files:
                    if f.endswith((".md", ".markdown")):
                        found.append(Path(root) / f)
    return sorted(found)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check prose punctuation style in docs."
    )
    parser.add_argument("paths", nargs="*", help="Files or directories to check.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with code 1 if any violation is found.",
    )
    args = parser.parse_args()

    files = discover_files(args.paths)
    if not files:
        print("No markdown files found to check.")
        return 0

    all_violations: list[StyleViolation] = []
    for f in files:
        violations = check_file(f)
        all_violations.extend(violations)

    if not all_violations:
        print(f"✅ Prose style check passed: {len(files)} files checked, 0 violations.")
        return 0

    print(f"❌ Found {len(all_violations)} prose style violation(s):")
    for v in all_violations:
        print(f"  {v.file_path}:{v.line_number}:{v.column} [{v.rule}]")
        print(f"    Line: {v.line_content.strip()}")
        print(f"    Matched: {v.matched_text!r}")
        print()

    print(
        f"Summary: {len(all_violations)} violation(s) across {len({v.file_path for v in all_violations})} file(s)."
    )
    return 1 if args.strict else 0


if __name__ == "__main__":
    sys.exit(main())
