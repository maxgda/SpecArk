---
name: spdd-api-test
description: Generate API test assets from SPDD stories, prompts, and implemented behavior using the canonical repository command text integrated into this project.
---

# spdd-api-test

Use this skill only to generate or update API-oriented verification artifacts from an SPDD story, prompt, or implemented behavior.

## Required Execution Contract

1. Read `../../references/source-commands/spdd-api-test.md` completely every time this skill runs.
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

## Canonical Reference

- `../../references/source-commands/spdd-api-test.md`

## Required Completion Report

After finishing, end with this exact block format:

```text
SPDD_PHASE_RESULT
phase: spdd-api-test
status: completed|blocked
artifact_type: api-test
output_files:
- <changed-file>
next_phase: complete
review_recommended: no
summary: <single-line summary>
END_SPDD_PHASE_RESULT
```
