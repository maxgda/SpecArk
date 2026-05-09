# Release Notes

This page tracks release-facing changes at a higher level than the raw changelog.

## Current release direction

The current documentation refresh focused on:

- separating user-facing usage guidance from maintainer-only notes
- making the `README` a cleaner front door for installation, workflow execution, token savings, and test generation
- improving VitePress navigation so release preparation material is easier to find

## Release checklist

Before publishing a new version:

1. Run `python3 plugins/specark/scripts/validate_plugin_bundle.py`.
2. Run `npm run docs:build`.
3. Review `CHANGELOG.md` and add the final versioned entry.
4. Verify `plugins/specark/.codex-plugin/plugin.json` has correct publisher and release metadata.
5. Restart Codex and verify the plugin is discoverable from `.agents/plugins/marketplace.json`.
6. Tag the release after validation is clean.

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
