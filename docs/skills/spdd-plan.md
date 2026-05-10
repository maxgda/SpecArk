# spdd-plan

`spdd-plan` is an explicit pre-story planning skill for broad initiatives, noisy PRDs, and mixed business context that still needs roadmap slicing before story generation.

## Use it when

- the input spans multiple capabilities, dependency chains, or rollout phases
- you need ordered delivery slices before writing stories
- you want a durable planning artifact under `spdd/plan/`
- you need the skill to decide between planning, redirecting, or reusing an existing repository path

## Do not use it when

- the request is already a coherent implementation story for `spdd-story`
- the requirement is already focused enough for `spdd-analysis`
- the capability already exists and the right move is reuse instead of replanning

## Output shape

This skill should typically produce:

- one planning artifact under `spdd/plan/`
- ordered delivery slices with dependency notes and sequencing rationale
- exactly one recommended next slice for `spdd-story`
- a completion block that reports the consumed inputs, produced plan path, next command shape, and any material validation notes

## Notes

`spdd-plan` is explicitly invoked and optional. It exists before `spdd-story`, but it does not replace `spdd-story` or alter the orchestrator's current automatic start-phase detection.
