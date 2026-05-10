# Phase Handoffs

The orchestrator and the phase skills are connected by a standard machine-readable result block. Every phase must emit one of these at the end of its run.

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
| `summary` | single line only |

## Common phase outputs

| Phase | Expected output location |
|---|---|
| `spdd-story` | `requirements/` |
| `spdd-analysis` | `spdd/analysis/` |
| `spdd-reasons-canvas` | `spdd/prompt/` |
| `spdd-prompt-update` | `spdd/prompt/` |
| `spdd-sync` | `spdd/prompt/` |
| `spdd-generate` | implementation files (project-specific) |
| `spdd-api-test` | `spdd/tests/` |

## Failure rule

::: warning Malformed handoffs
If a phase returns a malformed or suspicious handoff block, the orchestrator treats the workflow as blocked instead of guessing. Do not manually patch the block or continue — diagnose why the phase produced a bad result first.
:::
