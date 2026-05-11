# spdd-session-health

`spdd-session-health` assesses whether the current Claude Code session is in good shape before committing to an SPDD phase invocation.

## Quick start

::: code-group

```text [Codex]
Use the spdd-session-health skill for spdd-analysis on @requirements/STORY-001.md.
```

```text [Claude Code]
/specark:spdd-session-health for spdd-analysis on requirements/STORY-001.md
```

:::

## Use it when

- you want to verify the session before running a heavy phase like `spdd-analysis` or `spdd-reasons-canvas`
- you are about to pass multiple input files to the orchestrator
- the session has been running a while and you are unsure whether prior context will interfere
- the orchestrator invokes it automatically as a pre-flight check (see below)

## What it checks

The skill cannot read token counts. Instead it reasons over visible conversation signals and repository state:

| Check | Flag raised | Meaning |
|---|---|---|
| More than one input file passed | `multi-input` | Each input is a full phase cycle — batching them inflates context |
| A completed `SPDD_PHASE_RESULT` already in this session | `prior-phase-complete` | Prior exploration contaminates the next phase's bounded retrieval |
| Same file read 3+ times with no artifact write between reads | `context-spinning` | Session is looping without converging on output |
| User reversed an instruction explicitly | `user-redirect` | Prior context may be wrong, not just stale |
| Required input file missing or wrong type for the target phase | `missing-input` / `wrong-artifact-type` | Cannot proceed without a corrected input |

## Output

The skill produces a `SPDD_HEALTH_RESULT` block:

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

`flags:` and its list items are omitted when no flags are active.

### Verdict levels

| Status | Meaning | Action |
|---|---|---|
| `ready` | No flags — session is clean | Proceed |
| `caution` | Only `multi-input` — session is fresh but input load is high | Split inputs across sessions |
| `blocked` | Input is missing or wrong type — session itself is healthy | Fix the input, then proceed |
| `restart` | Context is unreliable (`prior-phase-complete`, `context-spinning`, or `user-redirect`) | Start a new session |

## Automatic invocation by the orchestrator

The orchestrator runs `spdd-session-health` automatically — once, before the first phase — when:

1. More than one input artifact was passed, or
2. A completed `SPDD_PHASE_RESULT` already exists in the conversation

It does not re-run the check between subsequent phases in the same orchestration loop.

### Orchestrator behavior by mode

| Result | `manual` / `semi-auto` / `resume` | `auto` |
|---|---|---|
| `ready` | Proceed | Proceed |
| `caution` | Surface flags, ask to confirm | Log warning, proceed |
| `blocked` | Stop, print fix-input guidance | Stop, print fix-input guidance |
| `restart` | Stop, print new-session command | Stop, print new-session command |

`blocked` and `restart` are hard stops in all modes. `caution` is advisory — `auto` logs and continues.

## Where it fits

`spdd-session-health` is a pre-flight utility, not a phase. It produces no repository artifact and does not advance the workflow. Run it before any phase when you are uncertain about session quality.

::: tip One completed phase = one session boundary
After any SPDD phase completes and writes its artifact, the artifact is the canonical handoff. The next phase works best in a fresh session that reads the artifact rather than inheriting the prior session's exploration history.
:::
