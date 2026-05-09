#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from datetime import datetime


def slugify(text: str) -> str:
    lowered = text.lower()
    lowered = re.sub(r"[^a-z0-9]+", "-", lowered)
    lowered = re.sub(r"-{2,}", "-", lowered).strip("-")
    tokens = [token for token in lowered.split("-") if token]
    return "-".join(tokens[:10]) or "untitled"


def derive_filename(args: argparse.Namespace) -> str:
    timestamp = args.timestamp or datetime.now().strftime("%Y%m%d%H%M")
    slug = slugify(args.text)

    if args.kind == "analysis":
        return f"{args.jira}-{timestamp}-[Analysis]-{slug}.md"
    if args.kind == "prompt":
        scope = f"-{args.scope}" if args.scope else ""
        action = args.action or "Feat"
        return f"{args.jira}-{timestamp}-[{action}]{scope}-{slug}.md"
    if args.kind == "test":
        scope = f"-{args.scope}" if args.scope else ""
        return f"{args.jira}-{timestamp}-[Test]{scope}-{slug}.md"
    if args.kind == "story":
        module = args.module or "001"
        sequence = args.sequence or "001"
        return f"STORY-{module}-{sequence}-{slug}.md"
    raise ValueError(f"Unsupported kind: {args.kind}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Derive SPDD artifact filenames.")
    parser.add_argument("kind", choices=["analysis", "prompt", "story", "test"])
    parser.add_argument("--text", required=True, help="Business text used to derive the description slug.")
    parser.add_argument("--jira", default="GGQPA-XXX")
    parser.add_argument("--timestamp")
    parser.add_argument("--action")
    parser.add_argument("--scope")
    parser.add_argument("--module")
    parser.add_argument("--sequence")
    args = parser.parse_args()
    print(derive_filename(args))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
