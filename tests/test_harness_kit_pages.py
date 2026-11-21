"""Keeps the practice pages of "The complete harness" on one shared template.

Every practice page answers the same questions in the same order, in both
languages, and carries at least one labeled evidence box.
"""

from __future__ import annotations

from pathlib import Path

EN_DIR = Path("docs/en/harness-kit")
ES_DIR = Path("docs/es/harness-completo")

EN_H2 = [
    "What it is",
    "Why it pays off",
    "Template",
    "When to use it and when to skip it",
    "What failed in practice",
    "How to check it is healthy",
    "Go deeper",
]
ES_H2 = [
    "Qué es",
    "Por qué rinde",
    "Plantilla",
    "Cuándo usarlo y cuándo no",
    "Qué falló en la práctica",
    "Cómo saber si está sano",
    "Para profundizar",
]

# EN file -> ES file. Extended as practice pages are added.
KIT_PAGES = {
    "few-skills.md": "pocas-skills.md",
}


def h2s(path: Path) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    return [line[3:].strip() for line in lines if line.startswith("## ")]


def test_practice_pages_follow_the_template_in_both_languages():
    for en, es in KIT_PAGES.items():
        assert h2s(EN_DIR / en) == EN_H2, en
        assert h2s(ES_DIR / es) == ES_H2, es


def test_every_kit_page_has_an_evidence_box():
    for en, es in KIT_PAGES.items():
        assert '"Evidence level:' in (EN_DIR / en).read_text(encoding="utf-8"), en
        assert '"Nivel de evidencia:' in (ES_DIR / es).read_text(encoding="utf-8"), es


def test_kit_index_shows_the_starter_tree_and_routing_table():
    for path in (EN_DIR / "index.md", ES_DIR / "index.md"):
        text = path.read_text(encoding="utf-8")
        for needle in (
            "AGENTS.md",
            "memory/",
            "docs/adr/",
            "docs/plans/",
            "make check",
            "LEVEL=minimal",
        ):
            assert needle in text, (str(path), needle)
