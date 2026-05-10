# Orchestrator Modes

`spdd-orchestrator` is the controller skill for the SPDD workflow. It does not replace the phase skills. It selects the right starting point, invokes the right phase in sequence, and respects review gates.

`spdd-plan` is not part of the orchestrator's automatic start-phase detection in this release. Use it explicitly before orchestrating when a roadmap-style planning pass is needed.

## Supported modes

### `manual`

- run exactly one phase
- require a valid phase result block
- stop immediately after that phase

### `semi-auto`

- run sequentially
- stop at configured review gates
- ask before moving into the next gated phase

This is the default mode.

### `auto`

- run sequentially until completion
- do not pause at normal review gates
- stop only if blocked, complete, or explicitly instructed to stop after a phase

### `resume`

- start from an existing artifact
- preserve downstream lineage instead of regenerating upstream phases
- behave like `semi-auto` by default unless the user explicitly requests `auto`

### `plan-only`

- infer the sequence
- return the intended phase path
- execute nothing

## Optional controls

The orchestrator also honors:

- `with-story=true|false|auto`
- `with-tests=true|false|auto`
- `stop-after=story|analysis|prompt|generate|tests`

## Review behavior

In `semi-auto`, the orchestrator should stop after:

- `spdd-story`
- `spdd-analysis`
- `spdd-reasons-canvas`
- `spdd-prompt-update`

These gates are defined by the shared orchestrator contract and are meant to keep major artifact transitions reviewable.
