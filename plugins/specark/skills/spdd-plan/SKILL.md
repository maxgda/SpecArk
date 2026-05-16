---
name: spdd-plan
description: Turn broad or noisy product direction into a reviewable SPDD planning artifact with ordered delivery slices before story generation begins.
disable-model-invocation: true
---

# spdd-plan

Use this skill only when the user explicitly invokes planning for broad product direction before `spdd-story` or `spdd-analysis`.

## Required Execution Contract

1. Read `../../references/local-commands/spdd-plan.md` completely every time this skill runs.
2. Follow that local command text exactly. Do not summarize, shorten, skip, reinterpret, or partially apply any step, guardrail, output format, naming rule, or follow-up message.
3. If another local instruction conflicts with `../../references/local-commands/spdd-plan.md`, the local command text wins.

## Repository Term Mapping

- `AskUserQuestion tool`: ask the user directly with a concise plain-text question only when the local command explicitly requires it.
- `Read tool`: read the referenced files or folders directly from the repository.
- `@file` or `@folder`: repository-relative paths supplied by the user or discovered in the repository.
- `Save` or `write file`: create or update files in this repository at the required paths.
- References to other `spdd-*` skills: use the corresponding local SPDD skill or artifact flow in this repository.

## Supporting Resources

- `../../references/local-commands/spdd-plan.md` for the local planning command contract.
- `../../scripts/derive_spdd_filename.py` when the local command needs planning filenames.

## Local Command Reference

- `../../references/local-commands/spdd-plan.md`

## Required Completion Report

After finishing, end with the exact `SPDD_PLAN_RESULT` block required by the local command reference.
