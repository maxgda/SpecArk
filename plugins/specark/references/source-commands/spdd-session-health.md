---
name: /spdd-session-health
id: spdd-session-health
category: Development
description: Pre-flight session health check that assesses whether the current Claude Code conversation context is in good shape to execute an upcoming SPDD phase, and whether the input load is appropriate for a single session.
---

Assess the health of the current Claude Code session before committing to an SPDD phase invocation. This check is behavioral — it reasons over visible conversation signals and repository state. It cannot read token counts.

**Input**: The target phase name and zero or more input artifact paths.

Input forms:

```
# Single input, target phase
/spdd-session-health for spdd-analysis on requirements/STORY-001.md

# Multiple inputs
/spdd-session-health for spdd-analysis on requirements/STORY-001.md requirements/STORY-002.md requirements/STORY-003.md

# No explicit inputs (skill will flag if the target phase requires a file)
/spdd-session-health for spdd-analysis

# Invoked by the orchestrator (internal)
/spdd-session-health target=spdd-analysis inputs=[<paths>]
```

**Steps**

1. **Parse invocation**

   a. Extract the target phase name (e.g., `spdd-analysis`).
   b. Extract all input artifact paths. Count them as `N`.
   c. If neither a target phase nor any input paths can be determined, use the **AskUserQuestion tool** to ask:
   > "Which SPDD phase are you preparing to run, and what input files will you pass to it?"

   Note: `N = 0` is valid at this step. A missing required input is caught in Check 5.

2. **Check 1 — Input load**

   - If `N > 1`, flag `multi-input`: each input artifact represents a full phase cycle. Running them back-to-back in a single session inflates context with stale exploration from prior inputs.
   - If `N == 1` or `N == 0`, this check produces no flag.

3. **Check 2 — Prior phase completions in this session**

   - Scan the visible conversation history — specifically messages and tool results that appeared *before* this health check was invoked — for any `SPDD_PHASE_RESULT` blocks containing `status: completed`.
   - Count them as `P`.
   - If `P >= 1`, flag `prior-phase-complete`: the session has already done phase work. The next phase's bounded retrieval will be contaminated by the prior phase's exploration history.

4. **Check 3 — Context spinning**

   - Scan the visible conversation history *prior to* this health check invocation for file read operations. Do not include any reads performed by this skill in Check 5 — those happen after this point and must not be counted.
   - Identify any file path that appears in 2 or more distinct read operations in that prior history.
   - If any such path exists AND no write to `spdd/`, `requirements/`, or any implementation file path occurred between those reads (i.e., the reads are not bracketed by artifact output), flag `context-spinning`: the session is re-reading files without converging on output.
   - Threshold: only flag if the same file was read at least 3 times with no intervening artifact write. Two reads of the same file is normal exploration; three is spinning.

5. **Check 4 — User contradictions**

   - Scan visible user messages for explicit instruction reversals — a direction given and then explicitly retracted or replaced (e.g., "actually don't do X", "ignore what I said about Y", "start over", "forget that").
   - If any such reversal is found, flag `user-redirect`: prior context may be wrong, not just stale.

6. **Check 5 — Input artifact validation**

   Perform this check after Checks 1–4. Reads done here are excluded from Check 3.

   a. **Phase input requirements** — identify whether the target phase requires a file input:

   | Phase | Requires file input | Expected artifact location |
   |---|---|---|
   | `spdd-story` | No (accepts text; file optional) | Any requirement doc, PRD, or idea file |
   | `spdd-plan` | No (accepts text; file optional) | Any roadmap-level doc or idea file |
   | `spdd-analysis` | Yes | `requirements/` |
   | `spdd-reasons-canvas` | Yes | `spdd/analysis/` |
   | `spdd-generate` | Yes | `spdd/prompt/` |
   | `spdd-prompt-update` | Yes | `spdd/prompt/` |
   | `spdd-sync` | Yes | `spdd/prompt/` |
   | `spdd-api-test` | Yes | `spdd/prompt/` or implementation files |

   b. **If the target phase requires a file input and `N == 0`**: flag `missing-input` with reason "no input paths provided for a phase that requires a file."

   c. **For each path in the input list** (when `N >= 1`):
   - Read only the first line of the file using the Read tool to confirm it exists and is readable.
   - If the file is missing or unreadable, flag `missing-input` with the specific path.
   - If the file exists but its location does not match the expected artifact location for the target phase (per the table above), flag `wrong-artifact-type` with the specific path and the expected location.

7. **Determine aggregate verdict**

   Apply these rules in priority order (first match wins):

   - **`restart`**: any of `prior-phase-complete`, `context-spinning`, or `user-redirect` is active. The session context is unreliable regardless of input state. Surface all active flags including any `missing-input` or `wrong-artifact-type` flags as additional context, but the verdict is `restart`.
   - **`blocked`**: `missing-input` or `wrong-artifact-type` is active (and no `restart`-level flag is active). The session is healthy but the inputs are wrong or absent. The user must fix the inputs before proceeding — starting a new session is not the solution.
   - **`caution`**: only `multi-input` is active (no `restart` or `blocked` flags). The session is fresh but the input load is high.
   - **`ready`**: no flags active.

   Compound flag handling:
   - `multi-input` + any `restart` flag → `restart` (restart-level flags take precedence)
   - `multi-input` + `missing-input`/`wrong-artifact-type` → `blocked` (fix the inputs first; the multi-input concern is secondary)
   - `missing-input` + `wrong-artifact-type` → `blocked` (list both flags)

8. **Compose and print the health result block**

   Print this block exactly:

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

   Rules:
   - If no flags are active, omit the `flags:` key and all list items entirely — do not emit an empty `flags:` line.
   - If flags are active, emit `flags:` followed by one `- flag-name: reason` line per active flag.
   - `recommendation` must be a single line.
   - `next_action` mapping:
     - `ready` → `proceed`
     - `caution` with `multi-input` → `split-inputs`
     - `blocked` → `fix-input`
     - `restart` → `new-session`

9. **Print follow-up guidance**

   After the block, print a short human-readable message:

   - `proceed`: "Session is healthy. You can run `/specark:<target_phase>` now."
   - `split-inputs`: "Run one input at a time, starting a new Claude Code session between each.\n\nStart with: `/specark:<target_phase> @<first_input_path>`"
   - `fix-input`: "Fix the input before proceeding:\n<one line per missing-input or wrong-artifact-type flag describing what to correct>"
   - `new-session`: "Start a new Claude Code session before running this phase.\n\nIn the new session: `/specark:<target_phase> @<input_path>`"

   Do not print a follow-up message if this check was invoked internally by the orchestrator (the orchestrator reads the block directly).
