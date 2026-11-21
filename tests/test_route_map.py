"""Guards the route map data embedded in each language's landing page.

The map is drawn by docs/javascripts/route-map.js from a JSON block in the page,
and every link it shows is read from Markdown fallback anchors, so the strict
MkDocs build validates them. These tests keep both languages aligned and make
sure the fallback carries every route and box.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

NODE_IDS = {"guide", "template", "brain", "work", "observatory", "lab"}
ROUTE_IDS = ["dev", "lead", "docs", "champion"]
LANDINGS = {"en": "docs/en/index.md", "es": "docs/es/index.md"}

DATA_BLOCK = re.compile(
    r'<script type="application/json" id="route-map-data">\s*(.*?)\s*</script>',
    re.DOTALL,
)


def load_data(path: str) -> dict:
    text = Path(path).read_text(encoding="utf-8")
    match = DATA_BLOCK.search(text)
    assert match, f"{path}: no route-map-data block"
    return json.loads(match.group(1))


def test_each_landing_declares_all_nodes_and_routes_in_order():
    for lang, path in LANDINGS.items():
        data = load_data(path)
        assert set(data["nodes"]) == NODE_IDS, lang
        assert [r["id"] for r in data["routes"]] == ROUTE_IDS, lang


def test_languages_have_the_same_step_structure():
    en, es = (load_data(p) for p in LANDINGS.values())

    def shape(d: dict) -> list[list[str]]:
        return [[s["node"] for s in r["steps"]] for r in d["routes"]]

    assert (
        shape(en)
        == shape(es)
        == [
            ["guide", "template", "work", "lab"],
            ["guide", "brain", "work", "observatory"],
            ["guide", "brain", "work"],
            ["observatory", "lab", "template", "guide"],
        ]
    )


def test_every_route_and_node_has_a_fallback_anchor():
    for path in LANDINGS.values():
        text = Path(path).read_text(encoding="utf-8")
        for rid in ROUTE_IDS:
            assert f'data-route="{rid}"' in text, (path, rid)
        for nid in NODE_IDS:
            assert f'data-node="{nid}"' in text, (path, nid)


def test_data_blocks_have_no_forbidden_dashes_or_urls():
    for path in LANDINGS.values():
        raw = json.dumps(load_data(path), ensure_ascii=False)
        assert "--" not in raw and "—" not in raw and "–" not in raw
        assert "http" not in raw and "](" not in raw
