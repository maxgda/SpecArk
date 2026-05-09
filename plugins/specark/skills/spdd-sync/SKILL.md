---
name: spdd-sync
description: Sync implementation changes back to the structured SPDD prompt file following the canonical repository command text integrated into this project.
---

# spdd-sync

Use this skill only to sync implementation reality back into an existing SPDD prompt after code changes or refactors.

## Required Execution Contract

1. Read `../../references/source-commands/spdd-sync.md` completely every time this skill runs.
2. Follow that canonical command text exactly. Do not summarize, shorten, skip, reinterpret, or partially apply any step, guardrail, output format, naming rule, or follow-up message.
3. If the canonical command text conflicts with this wrapper, the canonical command text wins.

## Cursor Term Mapping

- `AskUserQuestion tool`: ask the user directly with a concise plain-text question only when the canonical command explicitly requires it.
- `Read tool`: read the referenced files or folders directly from the repository.
- `@file` or `@folder`: repository-relative paths supplied by the user or discovered in the repository.
- `Save` or `write file`: create or update files in this repository at the required paths.
- References to other `/spdd-*` commands: use the corresponding local SPDD skill or the artifact flow in this repository.

## Supporting Resources

- `../../references/source-commands/SOURCES.md` for provenance only.
- `../../references/orchestrator-contract.md` for the shared phase result block used by `spdd-orchestrator`.
- `../../scripts/parse_reasons_sections.py` when the canonical workflow needs REASONS section parsing.

## Canonical Reference

- `../../references/source-commands/spdd-sync.md`

## Required Completion Report

After finishing, end with this exact block format:

```text
SPDD_PHASE_RESULT
phase: spdd-sync
status: completed|blocked
artifact_type: prompt
output_files:
- spdd/prompt/<file-name>.md
next_phase: complete
review_recommended: yes
summary: <single-line summary>
END_SPDD_PHASE_RESULT
```
