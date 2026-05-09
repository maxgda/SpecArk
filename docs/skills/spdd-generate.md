# spdd-generate

`spdd-generate` implements code from a structured SPDD prompt artifact.

## Use it when

- a valid prompt artifact already exists
- implementation work should now follow the prompt rather than free-form design discussion

## Output shape

This phase should typically produce:

- changed implementation files
- a phase result block recommending either `spdd-api-test` or completion

## Notes

Generation should stay artifact-driven. The prompt file should remain the main source of intent.
