# Phase Handoffs

The orchestrator and the phase skills are connected by a standard machine-readable result block.

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

## Validation expectations

At minimum, a valid phase handoff should ensure:

- `phase` matches the phase that just ran
- `status` is `completed` or `blocked`
- `output_files` are repository-relative and real for created or changed artifacts
- `next_phase` is plausible for the current position in the workflow
- `summary` stays on one line

## Common phase outputs

- `spdd-story` should usually create files under `requirements/`
- `spdd-analysis` should usually create files under `spdd/analysis/`
- `spdd-reasons-canvas`, `spdd-prompt-update`, and `spdd-sync` should usually create files under `spdd/prompt/`
- `spdd-generate` should usually report changed implementation files
- `spdd-api-test` should usually report changed verification assets

## Failure rule

If a phase returns a malformed or suspicious handoff block, the orchestrator should treat the workflow as blocked instead of guessing.
