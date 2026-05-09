---
name: spdd-orchestrator
description: Coordinate the full SPDD workflow from requirement to prompt to implementation using the existing SPDD phase skills, with manual, semi-auto, auto, resume, and plan-only execution modes.
---

# spdd-orchestrator

Use this skill when the user wants a single entrypoint that coordinates the SPDD workflow across the existing phase skills instead of invoking each phase manually.

## Core Role

The orchestrator is a controller, not a replacement for the phase skills.

- It decides where to start.
- It runs one SPDD phase at a time.
- It passes artifact file paths from one phase to the next.
- It enforces review gates depending on the selected execution mode.

The artifact files remain the source of truth.

## Required References

Read these files before orchestrating:

- `../../references/orchestrator-contract.md`
- `../spdd-story/SKILL.md`
- `../spdd-analysis/SKILL.md`
- `../spdd-reasons-canvas/SKILL.md`
- `../spdd-generate/SKILL.md`
- `../spdd-prompt-update/SKILL.md`
- `../spdd-sync/SKILL.md`
- `../spdd-api-test/SKILL.md`

Only load the phase skills that are relevant for the chosen path.

## Execution Modes

Support these modes exactly as defined in `../../references/orchestrator-contract.md`:

- `manual`
- `semi-auto`
- `auto`
- `resume`
- `plan-only`

Default to `semi-auto` when the user does not specify a mode.

## Start Phase Detection

Infer the starting phase from the supplied input and the rules in `../../references/orchestrator-contract.md`.

Examples:

- broad idea or PRD -> `spdd-story` when needed, otherwise `spdd-analysis`
- story or focused requirement -> `spdd-analysis`
- analysis artifact -> `spdd-reasons-canvas`
- prompt artifact -> `spdd-generate`
- prompt artifact plus requirement/design change -> `spdd-prompt-update`
- prompt artifact plus code drift/refactor -> `spdd-sync`

## Orchestration Rules

1. Determine the execution mode.
2. Determine the starting phase.
3. If mode is `plan-only`, return the exact phase plan and stop.
4. Otherwise, run one phase at a time by following the corresponding phase skill contract.
5. After each phase, require the standard `SPDD_PHASE_RESULT` block.
6. Extract `output_files`, `next_phase`, and `review_recommended` from that block.
7. Use the output artifact path from the completed phase as the input to the next phase.
8. In `manual` mode, stop after one completed phase.
9. In `semi-auto` mode, stop at configured review gates and ask before proceeding.
10. In `auto` mode, continue until completion unless blocked.
11. In `resume` mode, continue from the detected artifact type using `semi-auto` review behavior unless the user explicitly requests `auto`.

## Optional Controls

Honor these optional controls when the user provides them:

- `with-story=true|false|auto`
- `with-tests=true|false|auto`
- `stop-after=story|analysis|prompt|generate|tests`

Defaults:

- `with-story=auto`
- `with-tests=auto`

## Review Behavior

In `semi-auto`, stop and ask at the review gates defined in `../../references/orchestrator-contract.md`.

Use this exact review prompt shape:

```text
Phase completed: <phase-name>
Output file(s): <paths>
Would you like to review this artifact before proceeding to <next-phase>?
```

In `auto`, do not stop at review gates unless the phase is blocked.

## Output Contract

The orchestrator itself should report:

- execution mode
- detected starting phase
- each consumed artifact path
- each produced artifact path
- the current next phase or completion state

When the workflow ends, provide a concise completion summary and the final artifact path(s).
