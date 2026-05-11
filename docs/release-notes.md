# Release Notes

This page tracks release-facing changes at a higher level than the raw changelog.

## 0.2.0 — Claude Code support

### Added

- **Claude Code platform support**: SpecArk now works with both Codex and Claude Code via the standard plugin marketplace mechanism.
- `plugins/specark/.claude-plugin/plugin.json`: Claude Code plugin manifest, mirroring the existing `.codex-plugin/plugin.json` layout.
- `.claude-plugin/marketplace.json`: repo-root marketplace file for `claude plugin marketplace add`.
- `docs/installation-claude-code.md`: step-by-step Claude Code install guide (`claude plugin marketplace add maxgda/spec-ark` + `claude plugin install specark`).
- Real Anthropic and OpenAI inline SVG logo marks on the docs home page and installation pages.
- GitHub quick-link action button on the docs home page.
- VitePress code-group tabs on Getting Started and First Feature Tutorial for side-by-side Codex / Claude Code syntax.

### Changed

- All 9 `SKILL.md` files: added `disable-model-invocation: true` to frontmatter and removed platform-specific "Codex skill" wording from descriptions.
- `docs/index.md`: platform compatibility badges with real logo marks; GitHub action button; Codex-only framing removed.
- `docs/installation.md`: restructured into Codex and Claude Code sections with inline SVG platform icons.
- `docs/getting-started.md`, `docs/first-feature.md`: `/specark:skill-name` invocation syntax shown for Claude Code.
- `docs/.vitepress/config.mjs`: added Installation — Claude Code to the Overview sidebar.
- `plugins/specark/CLAUDE.md`: simplified to a reference overview; install entry-point role moved to `.claude-plugin/plugin.json`.
- `README.md`: Claude Code startup section updated to `claude plugin marketplace add` / `claude plugin install`.
- `validate_plugin_bundle.py`: checks both `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`, plus `disable-model-invocation: true` in every skill.

### Notes

- The Codex install path (`codex plugin marketplace add`) is unchanged.
- `agents/openai.yaml` files are unchanged — Claude Code does not consume them.

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
4. Verify `plugins/specark/.codex-plugin/plugin.json` and `plugins/specark/.claude-plugin/plugin.json` have correct version and metadata.
5. Restart Codex and verify the plugin is discoverable from `.agents/plugins/marketplace.json`.
6. Test Claude Code installation: `claude plugin marketplace add maxgda/spec-ark && claude plugin install specark`.
7. Tag the release after validation is clean.

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
