---
name: spdd-orchestrator
description: Coordinate the full SPDD workflow from requirement to prompt to implementation using the existing SPDD phase skills, with manual, semi-auto, auto, resume, and plan-only execution modes.
disable-model-invocation: true
---

# spdd-orchestrator

Use this skill when the user wants one entrypoint that decides where the SPDD workflow should begin, invokes the correct phase skill in sequence, and manages review gates between artifacts.

This skill is an orchestration layer only. It must not replace the individual SPDD phase skills or invent a parallel workflow. The phase skills and their output artifacts remain the source of truth.

## Primary Responsibility

The orchestrator is responsible for workflow control, not phase execution logic.

It should:

- decide the execution mode
- detect the correct starting phase from the user input and available artifacts
- invoke one SPDD phase at a time
- pass the right artifact path into the next phase
- honor review gates and stop conditions
- report progress clearly after each phase

It must not:

- perform a phase by approximation when a dedicated SPDD phase skill already exists
- silently skip a required review gate for the active mode
- fabricate artifact paths, phase results, or completion states
- treat conversational summaries as equivalent to repository artifacts when a phase requires a file-backed input

## Required Startup Reads

Before orchestrating, read these files:

- `../../references/orchestrator-contract.md`
- `../spdd-plan/SKILL.md`
- `../spdd-story/SKILL.md`
- `../spdd-analysis/SKILL.md`
- `../spdd-reasons-canvas/SKILL.md`
- `../spdd-generate/SKILL.md`
- `../spdd-prompt-update/SKILL.md`
- `../spdd-sync/SKILL.md`
- `../spdd-api-test/SKILL.md`

Read all of them at the start when you need to coordinate the full flow. If the workflow is clearly resuming from a later artifact, it is still acceptable to focus operational attention on only the relevant downstream phase skills after the initial read.

## Shared Contracts And References

These files define the orchestration behavior and should be treated as normative support material:

- `../../references/orchestrator-contract.md`
- `../../references/source-commands/SOURCES.md` for provenance only

If a rule in this skill conflicts with `../../references/orchestrator-contract.md`, the contract file wins.

## Operating Model

Think in terms of phases, artifacts, and gates.

- A phase consumes a user requirement or an existing SPDD artifact.
- A phase produces one or more repository artifacts and an `SPDD_PHASE_RESULT` block.
- The orchestrator reads that result block and decides whether to stop, ask, or continue.

The orchestrator should always preserve explicit artifact lineage:

- what input artifact or requirement was consumed
- what output artifact was produced
- which phase produced it
- which phase is next

Do not allow the flow to become ambiguous. If multiple candidate inputs exist and the correct one is not obvious, stop and ask instead of guessing.
If the user supplied an explicit `@file` or repository path, validate that it exists, is readable, and matches the artifact type implied by the selected starting phase before invoking any downstream skill. If not, stop and ask the user nicely to provide the correct file or say whether to proceed with current context.

## Execution Modes

Support these modes exactly as defined in `../../references/orchestrator-contract.md`:

- `manual`
- `semi-auto`
- `auto`
- `resume`
- `plan-only`

Default to `semi-auto` when the user does not specify a mode.

### Mode Semantics

`manual`

- Run exactly one phase.
- Require that phase to finish with a valid `SPDD_PHASE_RESULT` block.
- Report the produced artifact and recommended next phase.
- Stop immediately after that phase, even if continuation is obvious.

`semi-auto`

- Run sequentially.
- Stop at every configured review gate.
- Ask the user whether to continue before invoking the next gated phase.
- Also stop when blocked, when the requested `stop-after` phase is reached, or when the workflow completes.

`auto`

- Run sequentially until completion.
- Do not pause at review gates.
- Stop only when blocked, when the requested `stop-after` phase is reached, or when the workflow completes.

`resume`

- Start from an existing artifact or a clearly implied downstream state.
- Use `semi-auto` review behavior by default.
- Upgrade to `auto` only if the user explicitly asks for it.

`plan-only`

- Do not execute any phase skill.
- Infer the likely phase path, review gates, and stopping points.
- Return the exact intended sequence and stop.

## Start Phase Detection

Infer the starting phase from the supplied input, repository state, and the rules in `../../references/orchestrator-contract.md`.

Use these rules:

- optional explicit pre-story planning: use `spdd-plan` only when the user explicitly asks for roadmap slicing before story generation
- broad idea, epic, PRD, or multi-capability feature: start with `spdd-story` when the requirement is too broad for direct technical analysis
- focused requirement or existing story: start with `spdd-analysis`
- analysis artifact in `spdd/analysis/`: start with `spdd-reasons-canvas`
- prompt artifact in `spdd/prompt/`: start with `spdd-generate`
- prompt artifact plus requirement or design change request: start with `spdd-prompt-update`
- prompt artifact plus code drift, refactor, or implementation divergence: start with `spdd-sync`

### Start Phase Heuristics

Use `spdd-story` when one or more of these are true:

- the input covers multiple user journeys or subsystems
- acceptance criteria are missing or too high level
- the requirement would likely create multiple implementation tracks
- the user is asking for decomposition before solutioning

Use `spdd-analysis` when one or more of these are true:

- the requirement already describes one coherent change
- the repository likely needs architectural analysis before prompting
- there is already a story artifact or story-like requirement

Use downstream resume modes only when the artifact type is explicit enough that phase selection is not speculative.

## Optional Controls

Honor these optional controls when the user provides them:

- `with-story=true|false|auto`
- `with-tests=true|false|auto`
- `stop-after=story|analysis|prompt|generate|tests`

Defaults:

- `with-story=auto`
- `with-tests=auto`

Interpret them as follows:

- `with-story=false`: do not route through `spdd-story` unless the user’s input is unusably broad and progress would otherwise be invalid
- `with-story=true`: prefer `spdd-story` even if direct analysis might be possible
- `with-tests=false`: end after `spdd-generate` unless another explicit downstream phase is requested
- `with-tests=true`: include `spdd-api-test` when generation or changed behavior justifies verification assets
- `stop-after=<phase>`: stop immediately after the corresponding phase completes and report the next recommended phase without executing it

If a control conflicts with a hard requirement of the actual workflow, surface that conflict explicitly instead of silently overriding it.

## Required Orchestration Loop

Follow this loop strictly:

1. Determine the execution mode.
2. Resolve any optional controls.
3. Detect the starting phase.
4. If the mode is `plan-only`, return the phase plan and stop.
5. Invoke exactly one phase skill.
6. Require a valid `SPDD_PHASE_RESULT` block from that phase.
7. Parse `status`, `artifact_type`, `output_files`, `next_phase`, `review_recommended`, and `summary`.
8. Validate that the reported outputs make sense for the phase that just ran.
9. Record the consumed and produced artifact paths.
10. Decide whether to stop, ask, or continue based on mode, review gates, `stop-after`, and `next_phase`.
11. If continuing, pass the most relevant produced artifact path into the next phase.
12. Repeat until completion or blockage.

Never collapse multiple phases into one undocumented jump. Every transition should be explainable from the previous phase result.

## Phase Invocation Rules

When invoking a phase skill:

- pass the most specific available artifact path, not a loose verbal summary, when a file exists
- preserve repository-relative paths when reporting or handing off artifacts
- respect the phase skill’s own execution contract and canonical reference requirements
- do not rewrite or reinterpret the downstream skill’s required completion block

If a phase skill returns an incomplete or malformed `SPDD_PHASE_RESULT`, treat that phase as blocked until the result is corrected. Do not continue based on inference alone.

## Phase Result Validation

Every executed phase must end with the standard block defined in `../../references/orchestrator-contract.md`.

Validate at minimum:

- `phase` matches the skill that was just executed
- `status` is either `completed` or `blocked`
- `output_files` is present and contains repository-relative paths when files were created or changed
- `next_phase` is plausible for the artifact type and workflow position
- `summary` is a single line

Also validate phase-specific expectations:

- `spdd-story` should normally produce files under `requirements/`
- `spdd-analysis` should normally produce files under `spdd/analysis/`
- `spdd-reasons-canvas`, `spdd-prompt-update`, and `spdd-sync` should normally produce files under `spdd/prompt/`
- `spdd-generate` should report changed implementation files
- `spdd-api-test` should report changed verification assets

If a result is structurally valid but semantically suspicious, stop and surface the issue instead of chaining forward.

## Review Gates

In `semi-auto`, stop and ask at the review gates defined in `../../references/orchestrator-contract.md`.

That means stopping after:

- `spdd-story`
- `spdd-analysis`
- `spdd-reasons-canvas`
- `spdd-prompt-update`

Use this exact review prompt shape:

```text
Phase completed: <phase-name>
Output file(s): <paths>
Would you like to review this artifact before proceeding to <next-phase>?
```

In `manual`, the phase boundary itself is already the stop point, so no extra review-gate logic is needed beyond the normal stop.

In `auto`, do not stop at review gates unless the phase is blocked.

## Stop Conditions

Stop immediately when any of these conditions is true:

- the active mode requires a stop after the current phase
- the current phase returned `status: blocked`
- the current phase hit a `semi-auto` review gate
- the requested `stop-after` phase has been reached
- the workflow reported `next_phase: complete`
- the correct next input artifact is ambiguous
- a user-supplied file path is missing, unreadable, or clearly the wrong artifact type for the selected phase, unless the user explicitly says to proceed with current context
- user clarification is required by a downstream phase contract

When stopping, clearly state whether the stop was expected, user-controlled, or due to blockage.

## Resume Behavior

Use `resume` when the user provides an existing SPDD artifact and wants to continue from the next sensible step.

Resume should:

- infer the artifact type from the supplied file path and context
- identify the next valid phase from that artifact type
- preserve the existing artifact chain rather than regenerating earlier phases
- use `semi-auto` review gates unless the user explicitly requests `auto`

Do not restart from `spdd-story` or `spdd-analysis` during resume unless the user explicitly asks to back up and redo the workflow.

## Planning Behavior

For `plan-only`, return a concrete workflow plan without executing phase skills.

The plan should include:

- selected execution mode
- detected starting phase
- expected phase sequence
- expected review gates
- any optional controls affecting the path
- the likely terminal phase

Do not claim that artifacts were produced in `plan-only` mode.

## Output Contract

The orchestrator itself should always report:

- selected execution mode
- detected starting phase
- each consumed artifact path
- each produced artifact path
- current next phase or completion state

When the workflow ends, provide a concise completion summary and the final artifact path or changed file set.

## Recommended Progress Reporting Shape

Use a compact structure like this during orchestration:

```text
SPDD orchestration status
mode: <mode>
starting_phase: <phase>
consumed:
- <path>
produced:
- <path>
next_phase: <phase|complete>
```

This is not a replacement for the phase skill’s own `SPDD_PHASE_RESULT` block. It is the orchestrator’s progress report.

## Failure Handling

Treat the workflow as blocked instead of improvising when:

- the start phase cannot be determined reliably
- required input artifacts are missing
- multiple candidate artifacts exist and no clear winner is available
- a phase result block is missing or malformed
- a downstream phase would require assumptions that the user has not approved

When blocked, explain:

- what phase the workflow was trying to run
- what specific ambiguity or missing artifact caused the block
- what exact user input or file path would unblock the flow

## Quality Bar

A good orchestration run is:

- deterministic about why each phase was chosen
- explicit about every artifact handoff
- strict about mode semantics
- conservative about ambiguous continuation
- faithful to the phase skill contracts

A bad orchestration run:

- jumps ahead without a validated phase result
- treats summaries as artifacts
- ignores review gates
- resumes from the wrong downstream phase
- hides uncertainty behind confident prose
