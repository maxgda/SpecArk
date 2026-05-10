---
name: spdd-story
description: Decompose high-level feature requirements into INVEST-compliant, business-focused stories with clear scope boundaries and testable acceptance criteria, following the canonical repository command text via the integrated reference file.
disable-model-invocation: true
---

# spdd-story

Use this skill only to create SPDD story artifacts from a feature, epic, PRD, or requirement document before technical analysis begins.

## Required Execution Contract

1. Read `../../references/source-commands/spdd-story.md` completely every time this skill runs.
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
- `../../scripts/next_story_number.py` when the canonical workflow needs the next story number.
- `../../scripts/derive_spdd_filename.py` when the canonical workflow needs SPDD-compliant filenames.

## Canonical Reference

- `../../references/source-commands/spdd-story.md`

## Required Completion Report

After finishing, end with this exact block format:

```text
SPDD_PHASE_RESULT
phase: spdd-story
status: completed|blocked
artifact_type: story
output_files:
- requirements/<file-name>.md
next_phase: spdd-analysis
review_recommended: yes
summary: <single-line summary>
END_SPDD_PHASE_RESULT
```
