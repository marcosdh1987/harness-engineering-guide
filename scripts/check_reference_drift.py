#!/usr/bin/env python3
"""scripts/check_reference_drift.py

Detects drift between docs/reference-data/ml-python-base-snapshot.json
and the active reference implementation (local path or remote git).

Usage:
    python scripts/check_reference_drift.py [--strict]
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path


def load_dotenv() -> None:
    env_path = Path(".env")
    if env_path.exists():
        with open(env_path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    k, v = line.split("=", 1)
                    k = k.strip()
                    v = v.strip().strip("\"'")
                    if k and k not in os.environ:
                        os.environ[k] = v


def get_current_reference_commit(
    repo_url: str, local_path: str | None
) -> tuple[str | None, str]:
    """Return (commit_sha, source_description)."""
    if local_path and os.path.exists(local_path):
        try:
            res = subprocess.run(
                ["git", "-C", local_path, "rev-parse", "HEAD"],
                capture_output=True,
                text=True,
                check=True,
            )
            return res.stdout.strip(), f"local path '{local_path}'"
        except subprocess.SubprocessError:
            pass

    # Remote fallback
    try:
        res = subprocess.run(
            ["git", "ls-remote", repo_url, "HEAD"],
            capture_output=True,
            text=True,
            check=True,
            timeout=10,
        )
        parts = res.stdout.strip().split()
        if parts:
            return parts[0], f"remote '{repo_url}'"
    except (subprocess.SubprocessError, OSError):
        pass

    return None, "unavailable"


def check_drift(snapshot_file: Path, strict: bool = False) -> int:
    if not snapshot_file.exists():
        print(f"❌ Snapshot file not found at {snapshot_file}")
        return 1 if strict else 0

    with open(snapshot_file, encoding="utf-8") as f:
        data = json.load(f)

    snapshot_sha = data.get("commit_sha", "").strip()
    repo_url = data.get("repo_url", "").strip()
    last_sync = data.get("last_sync", "unknown")

    load_dotenv()
    local_path = os.environ.get("REF_REPO_PATH")

    current_sha, source = get_current_reference_commit(repo_url, local_path)

    if not current_sha:
        print(
            f"⚠️ Could not resolve reference commit from {source}. Skipping drift check."
        )
        return 0

    if snapshot_sha == current_sha:
        print(f"✅ Reference snapshot is up to date with {source}.")
        print(f"   Commit SHA: {snapshot_sha} (synced: {last_sync})")
        return 0

    print("⚠️  REFERENCE DRIFT DETECTED!")
    print(f"   Source checked: {source}")
    print(f"   Snapshot Commit SHA: {snapshot_sha}")
    print(f"   Current Target SHA:  {current_sha}")
    print("\nRemediation:")
    print("   Run `make sync-reference` to update the snapshot and generated docs.")
    return 1 if strict else 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check for reference template snapshot drift."
    )
    parser.add_argument(
        "--snapshot",
        type=Path,
        default=Path("docs/reference-data/ml-python-base-snapshot.json"),
        help="Path to snapshot JSON file.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with code 1 if drift is detected.",
    )
    args = parser.parse_args()
    return check_drift(args.snapshot, strict=args.strict)


if __name__ == "__main__":
    sys.exit(main())
