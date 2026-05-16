---
name: spdd-discovery
description: Interview early, unclear, or noisy product context and write a Discovery Brief before planning, story splitting, or analysis begins.
disable-model-invocation: true
---

# spdd-discovery

Use this skill only when the user explicitly invokes a Discovery Interview for rough ideas, noisy notes, pasted context, or referenced files that need to become a Discovery Brief before `spdd-plan`, `spdd-story`, or `spdd-analysis`.

## Required Execution Contract

1. Read `../../references/local-commands/spdd-discovery.md` completely every time this skill runs.
2. Follow that local command text exactly. Do not summarize, shorten, skip, reinterpret, or partially apply any step, guardrail, output format, naming rule, or follow-up message.
3. If another local instruction conflicts with `../../references/local-commands/spdd-discovery.md`, the local command text wins.

## Repository Term Mapping

- `AskUserQuestion tool`: ask the user directly with one concise plain-text question only when the local command explicitly requires it.
- `Read tool`: read the referenced files or folders directly from the repository.
- `@file` or `@folder`: repository-relative paths supplied by the user or discovered in the repository.
- `Save` or `write file`: create or update files in this repository at the required paths.
- References to other `spdd-*` skills: use the corresponding local SPDD skill or artifact flow in this repository.

## Supporting Resources

- `../../references/local-commands/spdd-discovery.md` for the local Discovery Interview command contract.
- `../../scripts/derive_spdd_filename.py` when the local command needs Discovery Brief filenames.

## Local Command Reference

- `../../references/local-commands/spdd-discovery.md`

## Required Completion Report

After finishing, end with the exact `SPDD_DISCOVERY_RESULT` block required by the local command reference.
