# Changelog

All notable changes to this plugin package are documented in this file.

## 0.3.0 — 2026-05-11 — Session health & UX polish

### Added

- `spdd-session-health` skill: pre-flight context-health check that assesses whether the current conversation is in good shape to execute the next SPDD phase.
- `spdd-orchestrator` pre-flight integration that automatically invokes `spdd-session-health` when multiple input artifacts are detected or a prior phase was completed in the current session.
- Cowork compatibility surfaced in docs — no plugin changes were required.
- SpecArk logo in the docs navbar, favicon, and README.

### Changed

- Home page, installation pages, and palette refreshed and unified for clarity.
- Platform logos resized to small clickable thumbnails on the home and installation pages.

### Fixed

- Docs base path corrected after the repository rename so GitHub Pages assets resolve correctly.
- Stale submodule install instructions corrected in README and release notes.

### Notes

- `spdd-plan` skill (shipped during the 0.2.0 cycle but not documented at the time) is now reflected in the workflow table in `plugins/specark/CLAUDE.md`.

## 0.2.0 — 2026-05-10 — Claude Code support

### Added

- Claude Code platform support: SpecArk now works with both Codex and Claude Code via the standard plugin marketplace mechanism.
- `plugins/specark/.claude-plugin/plugin.json`: Claude Code plugin manifest, mirroring the existing `.codex-plugin/plugin.json` layout.
- `.claude-plugin/marketplace.json`: repo-root marketplace file for `claude plugin marketplace add`.
- `docs/installation-claude-code.md`: step-by-step Claude Code install guide.
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

## 0.1.0 — 2026-05-09 — Initial scaffold

- VitePress-based developer documentation site with GitHub Pages deployment workflow.
- Plugin package renamed from `spdd` to `specark` while keeping all `spdd-*` skill names unchanged.
- `spdd-orchestrator` added as a first-class workflow controller skill.
- Shared orchestration contract added in `plugins/specark/references/orchestrator-contract.md`.
- Standard `SPDD_PHASE_RESULT` handoff block added to all SPDD phase skills for orchestrated execution.
- Hardened the SPDD bundle for GitHub-backed Codex plugin distribution.
- Real repo-root marketplace file at `.agents/plugins/marketplace.json`.
- Skill files reworked into lean progressive-disclosure wrappers around canonical source command files.
- Per-skill `agents/openai.yaml` metadata for explicit, command-like invocation.
- `plugins/specark/scripts/validate_plugin_bundle.py` for deterministic packaging validation.
- Removed placeholder manifest URLs so unpublished metadata is no longer fabricated.
