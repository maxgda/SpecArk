---
name: spdd-orchestrator
description: Coordinate the full SPDD workflow from requirement to prompt to implementation using the existing SPDD phase skills, with manual, semi-auto, auto, resume, and plan-only execution modes.
disable-model-invocation: true
---

# spdd-orchestrator

Use this skill when the user wants one entrypoint that decides where the SPDD workflow should begin, invokes the correct phase skill in sequence, and manages review gates between artifacts.

## Required Execution Contract

1. Read `../../references/local-commands/spdd-orchestrator.md` completely every time this skill runs.
2. Follow that local command text exactly. Do not summarize, shorten, skip, reinterpret, or partially apply any step, guardrail, output format, naming rule, or follow-up message.
3. If another local instruction conflicts with `../../references/local-commands/spdd-orchestrator.md`, the local command text wins.

## Repository Term Mapping

- `AskUserQuestion tool`: ask the user directly with a concise plain-text question only when the local command explicitly requires it.
- `Read tool`: read the referenced files or folders directly from the repository.
- `@file` or `@folder`: repository-relative paths supplied by the user or discovered in the repository.
- References to other `spdd-*` skills: use the corresponding local SPDD skill or artifact flow in this repository.
- `SPDD_PHASE_RESULT` and `SPDD_HEALTH_RESULT`: parse the blocks exactly as defined by the local command and shared contract.

## Supporting Resources

- `../../references/local-commands/spdd-orchestrator.md` for the local orchestration command contract.
- `../../references/orchestrator-contract.md` for shared phase handoff rules.

## Local Command Reference

- `../../references/local-commands/spdd-orchestrator.md`

## Required Completion Report

After finishing, end with the exact orchestrator report required by the local command reference.
