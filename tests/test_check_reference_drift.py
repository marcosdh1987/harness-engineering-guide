"""tests/test_check_reference_drift.py

Unit tests for scripts/check_reference_drift.py.
"""

import json
from pathlib import Path
from unittest.mock import patch

from scripts.check_reference_drift import check_drift


def test_missing_snapshot(tmp_path: Path):
    missing = tmp_path / "nonexistent.json"
    assert check_drift(missing, strict=False) == 0
    assert check_drift(missing, strict=True) == 1


def test_matching_commit(tmp_path: Path):
    snapshot = tmp_path / "snapshot.json"
    snapshot.write_text(
        json.dumps(
            {
                "repo_url": "https://example.com/repo",
                "commit_sha": "abc1234",
                "last_sync": "2026-09-01T00:00:00Z",
            }
        ),
        encoding="utf-8",
    )

    with patch(
        "scripts.check_reference_drift.get_current_reference_commit",
        return_value=("abc1234", "mock"),
    ):
        assert check_drift(snapshot, strict=True) == 0


def test_drifted_commit(tmp_path: Path):
    snapshot = tmp_path / "snapshot.json"
    snapshot.write_text(
        json.dumps(
            {
                "repo_url": "https://example.com/repo",
                "commit_sha": "abc1234",
                "last_sync": "2026-09-01T00:00:00Z",
            }
        ),
        encoding="utf-8",
    )

    with patch(
        "scripts.check_reference_drift.get_current_reference_commit",
        return_value=("def5678", "mock"),
    ):
        assert check_drift(snapshot, strict=False) == 0
        assert check_drift(snapshot, strict=True) == 1
