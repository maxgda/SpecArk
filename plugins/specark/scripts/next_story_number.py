#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


STORY_PATTERN = re.compile(r"STORY-(\d{3})-(\d{3})", re.IGNORECASE)


def main() -> int:
    parser = argparse.ArgumentParser(description="Find the next story module or sequence number.")
    parser.add_argument("--root", default="requirements", help="Directory containing story files.")
    parser.add_argument("--module", help="Existing module number; if supplied, compute the next sequence within that module.")
    args = parser.parse_args()

    root = Path(args.root)
    modules: dict[str, list[int]] = {}

    if root.exists():
        for path in root.glob("*.md"):
            match = STORY_PATTERN.search(path.name)
            if not match:
                continue
            module, sequence = match.groups()
            modules.setdefault(module, []).append(int(sequence))

    if args.module:
        next_sequence = max(modules.get(args.module, [0])) + 1
        payload = {"module": args.module, "next_sequence": f"{next_sequence:03d}"}
    else:
        next_module = max((int(value) for value in modules), default=0) + 1
        payload = {"next_module": f"{next_module:03d}", "next_sequence": "001"}

    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
