# spdd-sync

`spdd-sync` writes implementation reality back into an existing prompt artifact.

## Use it when

- code changed first
- the prompt is now stale relative to implementation
- a refactor needs to be reflected in the structured prompt

## Output shape

This phase should typically produce:

- an updated prompt under `spdd/prompt/`
- a phase result block recommending completion

## Notes

This is the right path when the implementation diverged first.
