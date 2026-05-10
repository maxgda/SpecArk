# Release Notes

This page tracks release-facing changes at a higher level than the raw changelog.

## 0.2.0 — Claude Code support

### Added

- **Claude Code platform support**: SpecArk now works with both Codex and Claude Code. Install via git submodule or direct clone and reference `plugins/specark/CLAUDE.md` from your project's `CLAUDE.md`.
- `plugins/specark/CLAUDE.md`: new Claude Code plugin entry point listing all nine skills, invocation syntax, and supporting references.
- `docs/installation-claude-code.md`: step-by-step install guide for Claude Code (submodule, clone, and skills-only options).
- Codex and Claude Code SVG logos in `docs/public/` for use in documentation.
- GitHub quick-link action button on the docs home page.
- Platform compatibility badges (Codex · Claude Code) on the docs home page.
- VitePress code-group tabs on Getting Started and First Feature Tutorial for side-by-side Codex / Claude Code syntax.

### Changed

- `docs/index.md`: tagline and "What this site covers" section updated to reflect dual-platform support. Removed Codex-only framing.
- `docs/installation.md`: restructured into Codex and Claude Code sections with platform logos.
- `docs/getting-started.md`: Step 1 install block now shows both platforms in a code-group tab.
- `docs/first-feature.md`: install and branch steps now show Codex and Claude Code alternatives.
- `docs/.vitepress/config.mjs`: added `installation-claude-code` to the Overview sidebar section.
- `plugins/specark/skills/spdd-analysis/SKILL.md` and `spdd-story/SKILL.md`: removed "Codex skill" wording from `description` frontmatter fields so descriptions are platform-neutral.

### Notes

- The Codex install path (`codex plugin marketplace add`) is unchanged.
- `agents/openai.yaml` files are unchanged — Claude Code does not consume them.
- `validate_plugin_bundle.py` now checks for `plugins/specark/CLAUDE.md` as part of the bundle validation.

---

## 0.1.x — Initial documentation refresh

The documentation refresh in this cycle focused on:

- separating user-facing usage guidance from maintainer-only notes
- making the `README` a cleaner front door for installation, workflow execution, token savings, and test generation
- improving VitePress navigation so release preparation material is easier to find

---

## Release checklist

Before publishing a new version:

1. Run `python3 plugins/specark/scripts/validate_plugin_bundle.py`.
2. Run `npm run docs:build`.
3. Review `CHANGELOG.md` and add the final versioned entry.
4. Verify `plugins/specark/.codex-plugin/plugin.json` has correct publisher and release metadata.
5. Verify `plugins/specark/CLAUDE.md` is present and lists all skills.
6. Restart Codex and verify the plugin is discoverable from `.agents/plugins/marketplace.json`.
7. Test Claude Code installation using one of the three install options in `docs/installation-claude-code.md`.
8. Tag the release after validation is clean.

## Suggested release summary format

Use a short structure for each release:

### Added

- new skills, scripts, references, or docs sections

### Changed

- workflow behavior, prompts, docs structure, or packaging metadata

### Fixed

- validator issues, broken docs links, packaging mistakes, or routing problems

### Notes

- anything maintainers or adopters should watch during upgrade

## Relationship to changelog

Use `CHANGELOG.md` as the versioned source of truth.

Use this page for:

- release preparation guidance
- summary expectations
- consistent notes structure across releases
