#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PLUGIN_ROOT = ROOT / "plugins" / "specark"
PLUGIN_JSON = PLUGIN_ROOT / ".codex-plugin" / "plugin.json"
MARKETPLACE_JSON = ROOT / ".agents" / "plugins" / "marketplace.json"
SOURCES_MD = PLUGIN_ROOT / "references" / "source-commands" / "SOURCES.md"
SKILLS_ROOT = PLUGIN_ROOT / "skills"

REQUIRED_SKILLS = [
    "spdd-orchestrator",
    "spdd-plan",
    "spdd-story",
    "spdd-analysis",
    "spdd-reasons-canvas",
    "spdd-generate",
    "spdd-prompt-update",
    "spdd-sync",
    "spdd-api-test",
]

RICH_SKILLS = {"spdd-orchestrator", "spdd-plan"}
CANONICAL_PHASE_SKILLS = set(REQUIRED_SKILLS) - RICH_SKILLS


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text())
    except FileNotFoundError:
        fail(f"missing file: {path}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path}: {exc}")


def ensure_no_placeholder_urls(value: object, path: str = "$") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            ensure_no_placeholder_urls(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            ensure_no_placeholder_urls(child, f"{path}[{index}]")
    elif isinstance(value, str) and "example.invalid" in value:
        fail(f"placeholder URL remains at {path}")


def validate_plugin_json() -> None:
    plugin = load_json(PLUGIN_JSON)
    if not isinstance(plugin, dict):
        fail("plugin.json root must be an object")
    if plugin.get("name") != "specark":
        fail("plugin.json name must be 'specark'")
    if plugin.get("skills") != "./skills/":
        fail("plugin.json skills path must be './skills/'")
    interface = plugin.get("interface")
    if not isinstance(interface, dict):
        fail("plugin.json interface must be an object")
    for key in ["displayName", "shortDescription", "longDescription", "category", "capabilities", "defaultPrompt", "brandColor"]:
        if key not in interface:
            fail(f"plugin.json interface missing '{key}'")
    ensure_no_placeholder_urls(plugin)


def validate_marketplace() -> None:
    marketplace = load_json(MARKETPLACE_JSON)
    if not isinstance(marketplace, dict):
        fail("marketplace.json root must be an object")
    plugins = marketplace.get("plugins")
    if not isinstance(plugins, list) or len(plugins) != 1:
        fail("marketplace.json must contain exactly one plugin entry for this package")
    entry = plugins[0]
    if entry.get("name") != "specark":
        fail("marketplace entry name must be 'specark'")
    source = entry.get("source")
    if source != {"source": "local", "path": "./plugins/specark"}:
        fail("marketplace source must be {'source': 'local', 'path': './plugins/specark'}")
    policy = entry.get("policy")
    if policy != {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}:
        fail("marketplace policy must use AVAILABLE / ON_INSTALL")
    if entry.get("category") != "Engineering":
        fail("marketplace category must be 'Engineering'")


def parse_sources() -> list[tuple[str, int]]:
    text = SOURCES_MD.read_text()
    matches = re.findall(
        r"## (spdd-[^\n]+)\.md\n\n- Source branch: `[^`]+`.*?- Source size \(bytes\): `([^`]+)`",
        text,
        re.S,
    )
    if not matches:
        fail("could not parse canonical source entries from SOURCES.md")
    return [(name, int(size)) for name, size in matches]


def validate_sources() -> None:
    for name, expected_size in parse_sources():
        path = PLUGIN_ROOT / "references" / "source-commands" / f"{name}.md"
        if not path.exists():
            fail(f"missing canonical source file: {path}")
        actual_size = path.stat().st_size
        if actual_size != expected_size:
            fail(f"canonical source size mismatch for {path}: expected {expected_size}, got {actual_size}")


def validate_shared_references() -> None:
    orchestrator_ref = PLUGIN_ROOT / "references" / "orchestrator-contract.md"
    reasons_ref = PLUGIN_ROOT / "references" / "reasons-canvas.md"
    skill_authoring_ref = PLUGIN_ROOT / "references" / "high-quality-skill-authoring.md"
    if not orchestrator_ref.exists():
        fail(f"missing orchestrator contract reference: {orchestrator_ref}")
    if not reasons_ref.exists():
        fail(f"missing reasons reference: {reasons_ref}")
    if not skill_authoring_ref.exists():
        fail(f"missing skill authoring reference: {skill_authoring_ref}")


def validate_skill(skill_name: str) -> None:
    skill_dir = SKILLS_ROOT / skill_name
    skill_md = skill_dir / "SKILL.md"
    openai_yaml = skill_dir / "agents" / "openai.yaml"
    if not skill_md.exists():
        fail(f"missing skill file: {skill_md}")
    if not openai_yaml.exists():
        fail(f"missing agents/openai.yaml: {openai_yaml}")

    text = skill_md.read_text()
    if f"name: {skill_name}" not in text:
        fail(f"frontmatter name missing or incorrect in {skill_md}")
    if len(text.splitlines()) >= 500:
        fail(f"{skill_md} should stay below 500 lines for progressive disclosure")
    canonical_ref = f"`../../references/source-commands/{skill_name}.md`"
    if skill_name in CANONICAL_PHASE_SKILLS and canonical_ref not in text:
        fail(f"canonical reference missing in {skill_md}")
    if f"name: /{skill_name}" in text:
        fail(f"embedded canonical command text should not be duplicated inline in {skill_md}")
    if skill_name == "spdd-orchestrator":
        if "`../../references/orchestrator-contract.md`" not in text:
            fail("orchestrator skill must reference the shared orchestrator contract")
        for phase_skill in REQUIRED_SKILLS:
            if phase_skill == "spdd-orchestrator":
                continue
            if f"`../{phase_skill}/SKILL.md`" not in text:
                fail(f"orchestrator skill must reference ../{phase_skill}/SKILL.md")
    elif skill_name == "spdd-plan":
        required_refs = [
            "`../../references/high-quality-skill-authoring.md`",
            "`../../references/orchestrator-contract.md`",
            "`../spdd-story/SKILL.md`",
            "`../spdd-analysis/SKILL.md`",
        ]
        for required_ref in required_refs:
            if required_ref not in text:
                fail(f"spdd-plan skill must reference {required_ref}")
        if "SPDD_PLAN_RESULT" not in text:
            fail(f"{skill_md} must define the standard planning result block")
    else:
        if "SPDD_PHASE_RESULT" not in text:
            fail(f"{skill_md} must define the standard SPDD phase result block")
        if "`../../references/orchestrator-contract.md`" not in text:
            fail(f"{skill_md} must reference orchestrator-contract.md")

    metadata = openai_yaml.read_text()
    if "allow_implicit_invocation: false" not in metadata:
        fail(f"openai.yaml must disable implicit invocation for {skill_name}")
    if f"${skill_name}" not in metadata:
        fail(f"openai.yaml default prompt must explicitly mention the skill for {skill_name}")
    short_description_match = re.search(r'short_description:\s+"([^"]+)"', metadata)
    if not short_description_match:
        fail(f"openai.yaml short_description missing for {skill_name}")
    short_description = short_description_match.group(1)
    if not 25 <= len(short_description) <= 64:
        fail(f"openai.yaml short_description must be 25-64 chars for {skill_name}")
    if not re.search(r'brand_color:\s+"#[0-9A-Fa-f]{6}"', metadata):
        fail(f"openai.yaml brand_color must be a hex value for {skill_name}")
    if not re.search(r'default_prompt:\s+"[^"]+"', metadata):
        fail(f"openai.yaml default_prompt missing for {skill_name}")


def validate_plan_naming_support() -> None:
    script = (PLUGIN_ROOT / "scripts" / "derive_spdd_filename.py").read_text()
    if '"plan"' not in script:
        fail("derive_spdd_filename.py must support the plan artifact kind")
    if "[Plan]" not in script:
        fail("derive_spdd_filename.py must emit [Plan] filenames for plan artifacts")


def main() -> None:
    validate_plugin_json()
    validate_marketplace()
    validate_sources()
    validate_shared_references()
    for skill_name in REQUIRED_SKILLS:
        validate_skill(skill_name)
    validate_plan_naming_support()
    print("OK: plugin manifest, marketplace, canonical sources, and skills validated")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
