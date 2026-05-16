# Phase Handoffs

The orchestrator and the phase skills are connected by a standard machine-readable result block. Every phase must emit one of these at the end of its run.

`spdd-discovery` is a manual pre-workflow intake skill and uses its own `SPDD_DISCOVERY_RESULT` block until separate orchestrator discovery support lands.

## Required result block

```text
SPDD_PHASE_RESULT
phase: <phase-name>
status: completed|blocked
artifact_type: story|analysis|prompt|code|api-test
output_files:
- <repo-relative-path>
next_phase: <phase-name|complete|review>
review_recommended: yes|no
new_session_recommended: yes|no
summary: <single-line summary>
END_SPDD_PHASE_RESULT
```

## Why this exists

This block keeps orchestration deterministic.

It lets the controller:

- validate which phase just ran
- capture which file paths were produced
- determine the next recommended phase
- decide whether to stop, ask, or continue

::: tip Reading the result block
After any phase runs, look for the `SPDD_PHASE_RESULT` block in the response. The `output_files` list tells you exactly which repository files were created or changed. The `next_phase` field tells you where the workflow recommends going next.
:::

## Validation expectations

At minimum, a valid phase handoff should ensure:

| Field | Requirement |
|---|---|
| `phase` | matches the phase that just ran |
| `status` | `completed` or `blocked` |
| `output_files` | repository-relative, real paths for created or changed artifacts |
| `next_phase` | plausible for the current position in the workflow |
| `new_session_recommended` | `yes` when `status: completed` and a durable artifact was written |
| `summary` | single line only |

## Common phase outputs

| Phase | Expected output location |
|---|---|
| `spdd-discovery` | `spdd/discovery/` |
| `spdd-story` | `requirements/` |
| `spdd-analysis` | `spdd/analysis/` |
| `spdd-reasons-canvas` | `spdd/prompt/` |
| `spdd-prompt-update` | `spdd/prompt/` |
| `spdd-sync` | `spdd/prompt/` |
| `spdd-generate` | implementation files (project-specific) |
| `spdd-api-test` | `spdd/tests/` |

## Session boundaries

`new_session_recommended: yes` signals that the phase wrote a durable artifact and the next phase should start in a fresh session. The artifact is the canonical handoff — the next phase reads the file, not the conversation history.

In `manual` and `semi-auto` modes the orchestrator stops after a completed phase and prints:

```text
Session boundary reached. Start a new Claude Code session to continue.
Next phase: /specark:<next_phase> @<output_artifact_path>
```

In `auto` mode the orchestrator chains phases within the same session by design and does not stop on `new_session_recommended: yes`.

## Pre-flight health result block

`spdd-session-health` produces a separate block that is not a phase handoff. It appears before any phase runs and is consumed by the orchestrator or the user directly.

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

`flags:` and its list items are omitted entirely when no flags are active.

See [spdd-session-health](/skills/spdd-session-health) for the full verdict logic and orchestrator behavior table.

## Discovery result block

Discovery produces a standalone handoff block rather than the standard phase block:

```text
SPDD_DISCOVERY_RESULT
status: completed|blocked
artifact_type: discovery
output_files:
- <repo-relative-path|none>
recommended_next_phase: spdd-plan|spdd-story|spdd-analysis|none
review_recommended: yes|no
summary: <single-line summary>
END_SPDD_DISCOVERY_RESULT
```

Completed discovery writes a Discovery Brief under `spdd/discovery/` and recommends exactly one next phase. Blocked discovery writes no file and reports `recommended_next_phase: none`.

## Failure rule

::: warning Malformed handoffs
If a phase returns a malformed or suspicious handoff block, the orchestrator treats the workflow as blocked instead of guessing. Do not manually patch the block or continue — diagnose why the phase produced a bad result first.
:::
