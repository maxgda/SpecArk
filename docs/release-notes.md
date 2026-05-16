# Release Notes

This page tracks release-facing changes at a higher level than the raw changelog.

## 0.3.3 — Discovery Interview UX patch

### Changed

- **Stronger interview behavior**: `spdd-discovery` now treats the user's initial prompt as a starting hypothesis and asks focused questions before writing a Discovery Brief.
- **`generate now` handoff**: users can explicitly say `generate now` when the context is good enough to write the brief.
- **REASONS-informed checklist**: discovery now uses a concise coverage checklist for Requirements, Entities, Approach, Structure, Operations, Norms, and Safeguards to guide the next question.
- **Adaptive questioning**: after each relevant answer, the skill re-evaluates the best next question from the current context instead of following a fixed script.
- **Prompt sync**: the discovery SPDD prompt now matches the implemented local command wrapper and interview behavior.

### Notes

- This patch does not add automatic orchestrator discovery routing or `with-discovery` controls.

---

## 0.3.2 — Discovery Interview and local command wrappers

### Added

- **`spdd-discovery` skill**: manual Discovery Interview skill for rough ideas, noisy notes, pasted context, or referenced files that need a durable Discovery Brief before planning, story splitting, or technical analysis.
- **Discovery Brief artifacts**: completed discovery runs write one handoff-ready Markdown artifact under `spdd/discovery/` and recommend exactly one next phase from `spdd-plan`, `spdd-story`, or `spdd-analysis`.
- **`references/local-commands/` command contracts**: SpecArk-authored command text now lives outside slim `SKILL.md` wrappers for local workflow skills such as `spdd-orchestrator`, `spdd-discovery`, and `spdd-plan`.

### Changed

- `spdd-orchestrator` and `spdd-plan` now use thin wrappers that delegate behavior to local command files, keeping callable skill files smaller while preserving the same workflow contracts.
- Bundle validation now checks discovery skill files, docs visibility, Discovery Brief naming support, and local command wrapper conventions.
- Public docs now place discovery before planning and story creation, while noting that discovery is manually invoked until separate orchestrator discovery support lands.

### Notes

- `spdd-discovery` does not generate stories, analysis, prompts, code, or tests. It preserves early product context and hands that context to the next SPDD phase.
- Automatic orchestrator routing into discovery remains a separate follow-up.

---

## 0.3.1 — Documentation sync skill

### Added

- **`spdd-doc-sync` skill**: standalone maintenance skill that keeps human-facing in-repo documentation aligned after any workflow, skill, or behavior change. Accepts a free-form change description and uses an explicit routing table to determine which documentation surfaces to update — and which to leave untouched.
- **Affected-vs-untouched report**: every invocation produces a structured report listing which documentation files were updated with reasons, and which were deliberately skipped with reasons. Supports auditable, traceable doc changes.
- **`docs/skills/spdd-doc-sync.md`**: dedicated documentation page explaining when and how to use the skill and how it differs from `spdd-sync`.
- **Maintenance skills section** added to `docs/skills/index.md`.

### Notes

- `spdd-doc-sync` is a terminal maintenance step — it always emits `next_phase: complete` and does not chain into `spdd-generate`.
- `spdd-doc-sync` and `spdd-sync` are complementary: run `spdd-sync` to keep the structured prompt accurate, then `spdd-doc-sync` to propagate those changes into the human-facing docs.
- The skill enforces a hard boundary: it never reads or writes files under `spdd/prompt/` (that path is owned by `spdd-sync`).

---

## 0.3.0 — Session health & UX polish

### Added

- **`spdd-session-health` skill**: pre-flight context-health check that assesses whether the current conversation is in good shape to execute the next SPDD phase.
- **Orchestrator pre-flight integration**: `spdd-orchestrator` automatically invokes `spdd-session-health` when multiple input artifacts are detected or a prior phase was completed in the current session.
- **Cowork compatibility** surfaced in docs — no plugin changes required.
- **SpecArk logo** in the docs navbar, favicon, and README.

### Changed

- Home page, installation pages, and palette refreshed and unified for clarity.
- Platform logos resized to small clickable thumbnails on the home and installation pages.

### Fixed

- Docs base path corrected after the repository rename so GitHub Pages assets resolve correctly.
- Stale submodule install instructions corrected in README and release notes.

### Notes

- `spdd-plan` skill (added during the 0.2.0 cycle but not documented at the time) is now in the workflow table — see `plugins/specark/CLAUDE.md`.

---

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
4. Review `docs/release-notes.md` and move any unreleased release summary into the final versioned section.
5. Verify `plugins/specark/.codex-plugin/plugin.json` and `plugins/specark/.claude-plugin/plugin.json` have correct version and metadata.
6. Restart Codex and verify the plugin is discoverable from `.agents/plugins/marketplace.json`.
7. Test Claude Code installation: `claude plugin marketplace add maxgda/spec-ark && claude plugin install specark`.
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
