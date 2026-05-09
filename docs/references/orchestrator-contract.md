# Orchestrator Contract

This page documents the shared orchestration contract used by `spdd-orchestrator`.

## Execution modes

- `manual`: run one phase and stop
- `semi-auto`: run sequentially and stop at review gates
- `auto`: run sequentially until complete unless blocked
- `resume`: continue from an existing artifact
- `plan-only`: infer the workflow without execution

## Start phase detection

- broad feature, epic, PRD, or idea file: start with `spdd-story` when the scope is too broad for direct analysis
- focused requirement or story file: start with `spdd-analysis`
- analysis artifact in `spdd/analysis/`: start with `spdd-reasons-canvas`
- prompt artifact in `spdd/prompt/`: start with `spdd-generate`
- prompt artifact plus requirement or design change request: start with `spdd-prompt-update`
- prompt artifact plus code drift or refactor context: start with `spdd-sync`

## Optional controls

- `with-story=true|false|auto`
- `with-tests=true|false|auto`
- `stop-after=story|analysis|prompt|generate|tests`

## Review gates

In `semi-auto`, the orchestrator should stop after:

- `spdd-story`
- `spdd-analysis`
- `spdd-reasons-canvas`
- `spdd-prompt-update`

## Handoff contract

Every phase should end with the standard `SPDD_PHASE_RESULT` block described in [Phase Handoffs](/workflow/phase-handoffs).

For the authoritative repository source, see `plugins/specark/references/orchestrator-contract.md`.
