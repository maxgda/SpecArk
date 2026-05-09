# spdd-reasons-canvas

`spdd-reasons-canvas` transforms analysis into a structured prompt artifact for generation.

## Use it when

- analysis is complete enough to produce an implementation-ready prompt
- the next step should be code generation rather than more exploration

## Output shape

This phase should typically produce:

- a prompt artifact under `spdd/prompt/`
- a phase result block recommending `spdd-generate`

## Notes

This skill relies on the shared REASONS Canvas terminology and conventions stored in the plugin references.
