# Orchestrator Modes

`spdd-orchestrator` is the controller skill for the SPDD workflow. It does not replace the phase skills. It selects the right starting point, invokes the right phase in sequence, and respects review gates.

::: info spdd-plan and the orchestrator
`spdd-plan` is not part of the orchestrator's automatic start-phase detection in this release. Use it explicitly before orchestrating when a roadmap-style planning pass is needed.
:::

## Supported modes

### `manual`

Run exactly one phase, require a valid phase result block, and stop immediately after.

**Use it when** you want a single phase with full control — no continuation, no routing.

### `semi-auto` *(recommended default)*

Run sequentially, stopping at configured review gates. Ask before moving into the next gated phase.

::: tip Default mode
`semi-auto` is the recommended starting point for new users. It runs the workflow forward but pauses at each major artifact transition so you can review before continuing.
:::

### `auto`

Run sequentially until completion, without pausing at normal review gates.

Stops only if: blocked, complete, or explicitly instructed to stop after a specific phase.

**Use it when** you are confident in the artifact chain and want fully unattended forward progress.

### `resume`

Start from an existing artifact, preserving downstream lineage instead of regenerating upstream phases. Behaves like `semi-auto` by default unless `auto` is explicitly requested.

**Use it when** a previous session completed some phases and you need to pick up from where it left off.

### `plan-only`

Infer the phase sequence and return the intended path — execute nothing.

**Use it when** you want to see the proposed phase plan before committing to a run.

## Optional controls

The orchestrator also honors these request-level controls:

| Control | Values | Effect |
|---|---|---|
| `with-story` | `true` / `false` / `auto` | Force or skip the story phase |
| `with-tests` | `true` / `false` / `auto` | Force or skip the api-test phase |
| `stop-after` | `story` / `analysis` / `prompt` / `generate` / `tests` | Stop after a specific phase |

## Review gates in semi-auto

In `semi-auto`, the orchestrator stops and asks before continuing past:

- `spdd-story`
- `spdd-analysis`
- `spdd-reasons-canvas`
- `spdd-prompt-update`

::: tip Why these gates?
These are the major artifact transitions. Stopping here lets you verify that the artifact is correct before the next phase uses it as input. Catching drift at this point is cheaper than fixing it downstream.
:::

These gates are defined by the shared orchestrator contract. See [Orchestrator Contract](/references/orchestrator-contract) for full details.

## Pre-flight health check

Before invoking the first phase, the orchestrator automatically runs `spdd-session-health` when either condition is true:

1. More than one input artifact was passed
2. A completed `SPDD_PHASE_RESULT` already exists in the current conversation

This check runs once — before the first phase only. It does not repeat between phases in the same orchestration loop.

### How the orchestrator responds

| Health result | `manual` / `semi-auto` / `resume` | `auto` |
|---|---|---|
| `ready` | Proceed | Proceed |
| `caution` | Surface flags, ask to confirm | Log warning, proceed |
| `blocked` | Stop — fix the input first | Stop — fix the input first |
| `restart` | Stop — start a new session | Stop — start a new session |

`blocked` and `restart` are hard stops regardless of mode. `caution` is advisory — `auto` logs it and continues.

::: warning Three stories, one orchestrator call
Passing three story files to the orchestrator in a single call triggers the health check. In `semi-auto` the orchestrator will surface the `multi-input` flag and ask which input to start with. In `auto` it will log the warning and process the first input — but each subsequent input should ideally start in a fresh session to avoid context accumulation.
:::

See [spdd-session-health](/skills/spdd-session-health) for the full check logic and verdict reference.
