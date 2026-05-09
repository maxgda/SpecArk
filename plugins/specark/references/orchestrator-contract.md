# SPDD Orchestrator Contract

This reference defines the shared execution modes, phase-detection rules, review gates, and phase handoff contract for the `spdd-orchestrator` skill.

## Execution Modes

- `manual`: run exactly one phase, emit a phase result block, then stop.
- `semi-auto`: run the workflow sequentially and stop at review gates. This is the default mode.
- `auto`: run the workflow sequentially until completion unless blocked by ambiguity, missing input, or a failed phase.
- `resume`: start from an existing SPDD artifact and continue from the next valid phase. Review behavior follows `semi-auto` unless the user explicitly requests `auto`.
- `plan-only`: infer the workflow and return the exact planned phases without executing them.

## Start Phase Detection

- broad feature, epic, PRD, or idea file: start with `spdd-story` when the requirement appears large, multi-capability, or too broad for direct analysis
- focused requirement or story file: start with `spdd-analysis`
- analysis artifact in `spdd/analysis/`: start with `spdd-reasons-canvas`
- prompt artifact in `spdd/prompt/`: start with `spdd-generate`
- prompt artifact plus requirement/design change request: start with `spdd-prompt-update`
- prompt artifact plus code drift/refactor context: start with `spdd-sync`

## Optional Phase Controls

- `with-story=true|false|auto`
- `with-tests=true|false|auto`
- `stop-after=story|analysis|prompt|generate|tests`

Defaults:

- `with-story=auto`
- `with-tests=auto`
- `semi-auto` review gates after `spdd-story`, `spdd-analysis`, `spdd-reasons-canvas`, and `spdd-prompt-update`

## Standard Phase Result Block

Every SPDD phase skill should end with this exact block format:

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

Rules:

- `output_files` must list the actual artifact or changed files created by the phase.
- Paths must be repository-relative.
- `next_phase` must be the next recommended SPDD phase, `review`, or `complete`.
- `summary` must stay to one line.

## Review Gates

`semi-auto` mode should stop and ask before proceeding after:

- `spdd-story`
- `spdd-analysis`
- `spdd-reasons-canvas`
- `spdd-prompt-update`

Suggested prompt:

```text
Phase completed: <phase-name>
Output file(s): <paths>
Would you like to review this artifact before proceeding to <next-phase>?
```

## Orchestrator Output

The orchestrator should:

- announce the selected execution mode
- identify the detected starting phase
- show each consumed artifact path
- show each produced artifact path
- stop only according to the selected mode or on a blocked phase
