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
new_session_recommended: yes|no
summary: <single-line summary>
END_SPDD_PHASE_RESULT
```

Rules:

- `output_files` must list the actual artifact or changed files created by the phase.
- Paths must be repository-relative.
- `next_phase` must be the next recommended SPDD phase, `review`, or `complete`.
- `summary` must stay to one line.
- `new_session_recommended` must be `yes` when `status: completed` and a durable artifact was written. It must be `no` when `status: blocked` or the phase is mid-execution.

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

## Pre-Flight Health Check

Before invoking the **first** phase of an orchestration run, the orchestrator must run `spdd-session-health` when either of these conditions is true:

1. More than one input artifact was passed by the user
2. A `SPDD_PHASE_RESULT` with `status: completed` already exists in the current conversation

Run this check exactly once — before the first phase only. Do not re-run it between subsequent phases in the same orchestration loop.

The health check produces this block:

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

Orchestrator behavior based on health result and active mode:

| `status` | `next_action` | `manual` / `semi-auto` / `resume` | `auto` |
|---|---|---|---|
| `ready` | `proceed` | Continue | Continue |
| `caution` | `split-inputs` | Surface flags, ask which input to start with | Log warning, proceed with first input |
| `caution` | `proceed` | Surface flags, ask to confirm | Log warning, proceed |
| `blocked` | `fix-input` | Stop, print fix-input guidance | Stop, print fix-input guidance |
| `restart` | `new-session` | Stop, print new-session command | Stop, print new-session command |

`blocked` and `restart` are hard stops in all modes. `caution` is advisory — `auto` mode logs it and continues.

When stopping on `blocked`, print:

```text
Session health check requires input correction before continuing.
<one line per flag describing what to fix>
Once corrected, run: /specark:<target_phase> @<corrected_input_path>
```

When stopping on `restart`, print:

```text
Session health check blocked continuation.
Reason: <recommendation from SPDD_HEALTH_RESULT>
Start a new Claude Code session and run: /specark:<target_phase> @<first_input_path>
```

## Session Boundaries

The SPDD workflow is artifact-driven. All canonical state lives in the repository as Markdown files. The Claude Code conversation context is a separate layer that accumulates noise over time.

**One completed phase = one session boundary** — in `manual` and `semi-auto` modes.

In `manual` and `semi-auto`: after any `SPDD_PHASE_RESULT` block with `status: completed` and `new_session_recommended: yes`, the orchestrator must print:

```text
Session boundary reached. Start a new Claude Code session to continue.
Next phase: /specark:<next_phase> @<output_artifact_path>
```

In `auto`: do not stop on `new_session_recommended: yes`. The orchestrator chains phases within the same session by design. `auto` mode accepts the context accumulation tradeoff in exchange for uninterrupted execution.

### When to start a new session

| Signal | Action |
|---|---|
| `SPDD_PHASE_RESULT` with `status: completed` | Start a new session before the next phase |
| Switching JIRA IDs or features | Start a new session |
| More than one phase completed in the same session | Start a new session |
| User explicitly redirects mid-phase | Start a new session |

### When to stay in the current session

| Signal | Action |
|---|---|
| No `SPDD_PHASE_RESULT` yet (mid-phase) | Stay — the session IS the work state |
| User gave clarifications not captured in any artifact | Stay — starting fresh loses those |
| Active debugging with error history needed | Stay — error context is the signal |
| Open questions from the phase result unresolved | Stay — resolve before closing |

### Detecting messy context

The orchestrator cannot read token counts directly. These behavioral signals indicate the context has become unreliable:

- Multiple contradictory instructions from the user in the same session
- The same file read more than twice without producing an artifact
- A decision was made and then reversed
- A long tool-call chain that produced no artifact output

When these signals appear, the orchestrator should surface them and recommend starting a new session even if no `SPDD_PHASE_RESULT` has been emitted yet.

## Orchestrator Output

The orchestrator should:

- announce the selected execution mode
- identify the detected starting phase
- show each consumed artifact path
- show each produced artifact path
- stop only according to the selected mode or on a blocked phase
