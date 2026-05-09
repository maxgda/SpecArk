# spdd-prompt-update

`spdd-prompt-update` updates an existing prompt artifact after requirements, design assumptions, or architecture constraints have changed.

## Use it when

- the prompt still exists but the problem definition changed
- you want to preserve the existing prompt structure instead of regenerating from scratch

## Output shape

This phase should typically produce:

- an updated prompt under `spdd/prompt/`
- a phase result block recommending `spdd-generate`

## Notes

This is the right path when business intent changed first.
