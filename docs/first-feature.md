# First Feature Tutorial

This tutorial walks through a first feature from install to release handoff using SpecArk's artifact-driven workflow. The goal is not to teach every edge case. The goal is to get you through one complete path with confidence.

## Outcome

By the end of this tutorial you should have:

- the plugin installed
- a real input artifact in your repository
- one or more SPDD handoff artifacts created in sequence
- generated implementation changes
- a clean release handoff with sensible git checkpoints

## Step 1: Install the plugin

```bash
codex plugin marketplace add <owner>/<repo>
codex plugin marketplace upgrade
```

Expected outcome:

- Codex can access the `spdd-*` skills
- you are ready to start from a real repository artifact

## Step 2: Create a lightweight starting artifact

Create one file that describes the feature you want to ship. Keep it narrow enough that one implementation pass can finish it.

Examples:

- `idea.md` for a broad enhancement
- `requirements/feature-brief.md` for a focused requirement
- an existing story file if one already exists

Expected outcome:

- you have one clear artifact to hand to the first phase
- the request is small enough to review phase by phase

## Step 3: Start from the smallest valid phase

If you are starting broad, use the orchestrator:

```text
Use the spdd-orchestrator skill on @idea.md in semi-auto mode.
```

If you already have a more specific artifact, jump in manually:

```text
Use the spdd-analysis skill on @requirements/feature-brief.md.
Use the spdd-reasons-canvas skill on @spdd/analysis/ANALYSIS-001.md.
Use the spdd-generate skill on @spdd/prompt/PROMPT-001.md.
```

Expected outcome:

- the next artifact appears in the repository
- the request stays narrow and phase-specific

## Step 4: Review each handoff before moving on

The normal sequence is:

```text
spdd-story -> spdd-analysis -> spdd-reasons-canvas -> spdd-generate
```

After each phase, look for the `SPDD_PHASE_RESULT` block and the new file path it reports.

Check:

- the phase is what you expected
- the output file exists where the result block says it does
- the summary matches the feature you are trying to ship

Expected outcome:

- you catch requirement drift early
- you preserve traceability from idea to implementation

## Step 5: Generate the implementation

Once you have a prompt artifact under `spdd/prompt/`, run:

```text
Use the spdd-generate skill on @spdd/prompt/PROMPT-001.md.
```

Expected outcome:

- implementation files change in the repository
- the generated code reflects the operations defined in the prompt
- you can now review code and run verification

## Step 6: Add a release-ready checkpoint

Use lightweight git discipline so the first feature feels safe:

- create a branch before major implementation work
- commit after a clean prompt artifact is ready if you want a stable design checkpoint
- commit again after implementation and verification pass

Example:

```bash
git switch -c codex/first-feature
```

If you want to compare two alternative prompt or implementation paths, a worktree is useful. It keeps the main branch clean while you explore A/B variants in parallel.

Expected outcome:

- you can recover cleanly if one variant goes wrong
- design and implementation checkpoints stay easy to review

## Step 7: Finish the handoff

Once the generated code and any required verification look correct:

- review the changed files
- run the relevant tests or validation commands for the consuming project
- prepare the normal repository handoff, such as a commit or pull request

If the issue is in the implementation contract itself, fix the prompt first and then regenerate the affected code instead of patching blindly.

Expected outcome:

- the feature is ready for normal team review
- the prompt and implementation stay in sync

## Common pitfalls

- jumping into `spdd-generate` with only an idea or analysis file
- editing generated code for prompt-contract mistakes without updating the prompt
- treating worktrees as mandatory instead of optional
- overexplaining git steps until the tutorial stops being about shipping the feature

## Read next

1. [Workflow Overview](/workflow/)
2. [Phase Handoffs](/workflow/phase-handoffs)
3. [Release Notes](/release-notes)
