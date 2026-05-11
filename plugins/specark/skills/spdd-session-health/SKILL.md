---
name: spdd-session-health
description: Pre-flight session health check that assesses whether the current conversation context is in good shape to execute an upcoming SPDD phase, and whether the input load is appropriate for a single session.
disable-model-invocation: true
---

# spdd-session-health

Use this skill before running any SPDD phase when you want to verify the session is healthy enough to produce reliable output. Also invoked automatically by `spdd-orchestrator` when multiple input artifacts are detected or a prior phase was completed in the current session.

This skill does not produce a repository artifact. It produces a `SPDD_HEALTH_RESULT` block that the user or orchestrator reads to decide whether to proceed, split inputs, or start a new session.

## Required Execution Contract

1. Read `../../references/source-commands/spdd-session-health.md` completely every time this skill runs.
2. Follow that canonical command text exactly. Do not summarize, shorten, skip, reinterpret, or partially apply any step, check, or output format.
3. If the canonical command text conflicts with this wrapper, the canonical command text wins.

## Cursor Term Mapping

- `AskUserQuestion tool`: ask the user directly with a concise plain-text question only when the canonical command explicitly requires it.
- `Read tool`: read the referenced files or folders directly from the repository.
- `@file`: repository-relative paths supplied by the user or the orchestrator.
- Conversation history: the full visible sequence of user messages and tool call results in the current session.

## Supporting Resources

- `../../references/orchestrator-contract.md` for the health result block schema and session boundary rules.

## Canonical Reference

- `../../references/source-commands/spdd-session-health.md`

## Required Completion Block

After finishing, end with this exact block format:

```text
SPDD_HEALTH_RESULT
target_phase: <phase-name>
status: ready|caution|blocked|restart
inputs_assessed: <N>
flags:
- <flag-name>: <one-line reason>
recommendation: <single-line recommendation>
next_action: proceed|split-inputs|fix-input|new-session
END_SPDD_HEALTH_RESULT
```

`flags:` and its list items are omitted entirely when no flags are active — do not emit an empty `flags:` line.
