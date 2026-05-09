#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


SECTION_PATTERN = re.compile(r"^##\s+(Requirements|Entities|Approach|Structure|Operations|Norms|Safeguards)\s*$", re.MULTILINE)


def parse_sections(text: str) -> dict[str, str]:
    matches = list(SECTION_PATTERN.finditer(text))
    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        name = match.group(1)
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections[name] = text[start:end].strip()
    return sections


def main() -> int:
    parser = argparse.ArgumentParser(description="Parse REASONS sections from a prompt file.")
    parser.add_argument("path", help="Markdown file to parse.")
    args = parser.parse_args()

    content = Path(args.path).read_text(encoding="utf-8")
    print(json.dumps(parse_sections(content), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
