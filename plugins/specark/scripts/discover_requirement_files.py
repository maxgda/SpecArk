#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from dataclasses import asdict, dataclass
from pathlib import Path


EXCLUDED_DIRS = {
    ".git",
    ".hg",
    ".svn",
    "node_modules",
    "vendor",
    "dist",
    "build",
    "target",
    ".next",
    ".turbo",
}

EXCLUDED_PATH_PARTS = {
    "spdd/analysis",
    "spdd/prompt",
    "plugins/specark",
}

HIGH_SIGNAL_PARTS = (
    "requirements",
    "stories",
    "tickets",
    "specs",
    "prd",
    "brief",
    "feature",
    "epic",
    "acceptance",
    "billing",
    "story",
)

LOW_SIGNAL_NAMES = {
    "readme.md",
    "changelog.md",
    "contributing.md",
    "agents.md",
}


@dataclass
class Candidate:
    path: str
    score: int
    reasons: list[str]


def should_skip(path: Path) -> bool:
    text = path.as_posix().lower()
    if any(part in text for part in EXCLUDED_PATH_PARTS):
        return True
    return any(part in EXCLUDED_DIRS for part in path.parts)


def score_file(path: Path) -> Candidate:
    lowered = path.as_posix().lower()
    name = path.name.lower()
    score = 0
    reasons: list[str] = []

    if name in LOW_SIGNAL_NAMES:
        score -= 10
        reasons.append("low-signal-name")

    for token in HIGH_SIGNAL_PARTS:
        if token in lowered:
            score += 5
            reasons.append(f"matched:{token}")

    if path.parent.name.lower() == "requirements":
        score += 10
        reasons.append("in-requirements-dir")

    if "spdd/context" in lowered:
        score += 3
        reasons.append("project-context")

    return Candidate(path=str(path), score=score, reasons=reasons)


def discover(root: Path) -> list[Candidate]:
    candidates: list[Candidate] = []
    for current_root, dirs, files in os.walk(root):
        dirs[:] = [entry for entry in dirs if entry not in EXCLUDED_DIRS]
        current_path = Path(current_root)
        for filename in files:
            if not filename.lower().endswith(".md"):
                continue
            file_path = current_path / filename
            if should_skip(file_path.relative_to(root)):
                continue
            candidates.append(score_file(file_path.relative_to(root)))
    ranked = [item for item in candidates if item.score > 0]
    ranked.sort(key=lambda item: (-item.score, item.path))
    return ranked


def main() -> int:
    parser = argparse.ArgumentParser(description="Rank likely requirement markdown files.")
    parser.add_argument("--root", default=".", help="Repository root to scan.")
    parser.add_argument("--limit", type=int, default=20, help="Maximum number of candidates to print.")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of plain text.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    candidates = discover(root)[: args.limit]

    if args.json:
        print(json.dumps([asdict(item) for item in candidates], indent=2))
        return 0

    for item in candidates:
        reasons = ", ".join(item.reasons) if item.reasons else "no-strong-signal"
        print(f"{item.score:>3}  {item.path}  [{reasons}]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
