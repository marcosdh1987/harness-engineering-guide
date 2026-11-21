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
    "project-memory.md": "memoria-del-proyecto.md",
    "decision-records.md": "registros-de-decision.md",
    "plans-and-specs.md": "planes-y-specs.md",
    "commands.md": "comandos.md",
    "hooks.md": "hooks.md",
    "quality-gates.md": "gates-de-calidad.md",
}

# The eight deterministic checks of the Harness Lab's `make harness-check`.
HEALTH_CHECKS_EN = [
    "Verification can fail",
    "Verification does not rewrite the tree",
    "Hooks can enforce, not only remind",
    "Always-loaded instructions stay a map",
    "Skills are discoverable",
    "MCP servers are pinned",
    "CI runs the same gate the agent runs",
    "The harness version is declared",
]
HEALTH_CHECKS_ES = [
    "La verificación puede fallar",
    "La verificación no reescribe el árbol",
    "Los hooks pueden hacer cumplir, no solo recordar",
    "Las instrucciones que se cargan siempre siguen siendo un mapa",
    "Las skills se pueden descubrir",
    "Los servidores MCP están fijados",
    "CI corre el mismo gate que corre el agente",
    "La versión del harness está declarada",
]


def h2s(path: Path) -> list[str]:
    """Second-level headings outside fenced code blocks."""
    headings: list[str] = []
    in_fence = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        elif not in_fence and line.startswith("## "):
            headings.append(line[3:].strip())
    return headings


def test_practice_pages_follow_the_template_in_both_languages():
    for en, es in KIT_PAGES.items():
        assert h2s(EN_DIR / en) == EN_H2, en
        assert h2s(ES_DIR / es) == ES_H2, es


def test_every_kit_page_has_an_evidence_box():
    for en, es in KIT_PAGES.items():
        assert '"Evidence level:' in (EN_DIR / en).read_text(encoding="utf-8"), en
        assert '"Nivel de evidencia:' in (ES_DIR / es).read_text(encoding="utf-8"), es


def test_health_check_lists_the_eight_checks():
    en = (EN_DIR / "health-check.md").read_text(encoding="utf-8")
    es = (ES_DIR / "chequeo-de-salud.md").read_text(encoding="utf-8")
    for name in HEALTH_CHECKS_EN:
        assert name in en, name
    for name in HEALTH_CHECKS_ES:
        assert name in es, name
    for text in (en, es):
        assert "make harness-check" in text
        assert "github.com/marcosdh1987/ai-agentic-harness-lab" in text


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
