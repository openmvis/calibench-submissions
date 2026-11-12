#!/usr/bin/env python3
"""Publish result.json(s) to the calibench-vi/results dataset.

Usage: HF_TOKEN=... python scripts/publish.py [result.json ...]
Needs a fine-grained Hugging Face token with write access to calibench-vi/results only.
Records are stored per tool and batch: <tool.name>/<batch>/<file>.json
(batch = record "batch" field, else its timestamp date) — so each leaderboard
generation traces to a batch and the same tool is comparable across batches.
"""
import json
import os
import pathlib
import sys

from huggingface_hub import HfApi

REPO = "calibench-vi/results"


def main(files):
    token = os.environ.get("HF_TOKEN")
    if not token:
        sys.exit("HF_TOKEN not set (add it as a GitHub Actions secret)")
    api = HfApi(token=token)
    files = files or ["result.json"]
    for f in files:
        name = pathlib.Path(f).name
        try:
            r = json.load(open(f))
            tool = r.get("tool", {}).get("name") or "unsorted"
            batch = r.get("batch") or str(r.get("timestamp", ""))[:10] or "unbatched"
        except Exception:
            tool, batch = "unsorted", "unbatched"
        dest = f"{tool}/{batch}/{name}"
        api.upload_file(path_or_fileobj=f, path_in_repo=dest,
                        repo_id=REPO, repo_type="dataset",
                        commit_message=f"add leaderboard result {dest}")
        print(f"  published {dest} -> {REPO}")


if __name__ == "__main__":
    main(sys.argv[1:])
