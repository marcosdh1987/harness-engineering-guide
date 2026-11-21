"""Keeps the English and Spanish navigation trees mirrored.

mkdocs.yml uses a `!!python/name:` tag for the Mermaid fence formatter, so the
file is loaded with a SafeLoader subclass that turns unknown tags into None.
"""

from __future__ import annotations

from pathlib import Path

import yaml


class _LenientLoader(yaml.SafeLoader):
    pass


def _ignore_unknown(loader, tag_suffix, node):
    return None


_LenientLoader.add_multi_constructor("tag:yaml.org,2002:python/", _ignore_unknown)


def load_nav() -> dict[str, list]:
    config = yaml.load(Path("mkdocs.yml").read_text(encoding="utf-8"), _LenientLoader)
    sections = {}
    for entry in config["nav"]:
        if isinstance(entry, dict):
            for title, value in entry.items():
                sections[title] = value
    return sections


def shape(items: list, depth: int = 0) -> list[tuple[int, bool]]:
    out: list[tuple[int, bool]] = []
    for item in items:
        for value in item.values():
            is_group = isinstance(value, list)
            out.append((depth, is_group))
            if is_group:
                out.extend(shape(value, depth + 1))
    return out


def pages(items: list) -> list[str]:
    out: list[str] = []
    for item in items:
        for value in item.values():
            if isinstance(value, list):
                out.extend(pages(value))
            else:
                out.append(value)
    return out


def test_english_and_spanish_trees_have_the_same_shape():
    nav = load_nav()
    assert shape(nav["English"]) == shape(nav["Español"])


def test_every_nav_page_exists():
    nav = load_nav()
    for lang in ("English", "Español"):
        for page in pages(nav[lang]):
            assert Path("docs", page).is_file(), page


def test_routes_and_the_complete_harness_come_first():
    nav = load_nav()
    en_titles = [next(iter(item)) for item in nav["English"]][:3]
    es_titles = [next(iter(item)) for item in nav["Español"]][:3]
    assert en_titles == ["Overview", "Routes", "The complete harness"]
    assert es_titles == ["Visión general", "Rutas", "El harness completo"]
