# Changelog

All notable changes to this plugin package should be documented in this file.

## Unreleased

- Renamed the plugin package from `spdd` to `specark` while keeping all `spdd-*` skill names unchanged.
- Added `spdd-orchestrator` as a first-class workflow controller skill.
- Added the shared orchestration contract in `plugins/specark/references/orchestrator-contract.md`.
- Added a standard `SPDD_PHASE_RESULT` handoff block to all SPDD phase skills for orchestrated execution.
- Hardened the SPDD bundle for GitHub-backed Codex plugin distribution.
- Added a real repo-root marketplace file at `.agents/plugins/marketplace.json`.
- Reworked skill files into lean progressive-disclosure wrappers around canonical source command files.
- Added per-skill `agents/openai.yaml` metadata for explicit, command-like invocation.
- Added `plugins/specark/scripts/validate_plugin_bundle.py` for deterministic packaging validation.
- Removed placeholder manifest URLs so unpublished metadata is no longer fabricated.
