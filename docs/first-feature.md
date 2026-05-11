# First Feature Tutorial

This tutorial walks through a first feature from install to release handoff using SpecArk's artifact-driven workflow. The goal is not to teach every edge case. The goal is to get you through one complete path with confidence.

## What you will end up with

::: info Outcome
By the end of this tutorial you will have:

- the plugin installed
- a real input artifact in your repository
- one or more SPDD handoff artifacts created in sequence
- generated implementation changes
- a clean release handoff with sensible git checkpoints
:::

## The full path at a glance

```
Step 1: Install
Step 2: Create a starting artifact (idea.md or feature-brief.md)
Step 3: Run the orchestrator or jump to the matching phase
Step 4: Review each phase result block before continuing
Step 5: Generate the implementation
Step 6: Add a git checkpoint
Step 7: Review and hand off
```

## Step 1: Install the plugin

::: code-group

```bash [Codex]
codex plugin marketplace add maxgda/spec-ark
codex plugin marketplace upgrade
```

```bash [Claude Code]
claude plugin marketplace add maxgda/spec-ark
claude plugin install specark
```

:::

::: tip After install
- The `spdd-*` skills are available in your session.
- You are ready to start from a real repository artifact.
:::

## Step 2: Create a lightweight starting artifact

Create one file that describes the feature you want to ship. Keep it narrow enough that one implementation pass can finish it.

Examples:

- `idea.md` for a broad enhancement
- `requirements/feature-brief.md` for a focused requirement
- an existing story file if one already exists

::: tip Good signal
- You have one clear artifact to hand to the first phase.
- The request is small enough to review phase by phase.
:::

## Step 3: Start from the smallest valid phase

::: code-group

```text [Codex — broad start]
Use the spdd-orchestrator skill on @idea.md in semi-auto mode.
```

```text [Claude Code — broad start]
/specark:spdd-orchestrator @idea.md semi-auto
```

:::

If you already have a more specific artifact, jump in manually:

::: code-group

```text [Codex]
Use the spdd-analysis skill on @requirements/feature-brief.md.
Use the spdd-reasons-canvas skill on @spdd/analysis/ANALYSIS-001.md.
Use the spdd-generate skill on @spdd/prompt/PROMPT-001.md.
```

```text [Claude Code]
/specark:spdd-analysis @requirements/feature-brief.md
/specark:spdd-reasons-canvas @spdd/analysis/ANALYSIS-001.md
/specark:spdd-generate @spdd/prompt/PROMPT-001.md
```

:::

::: tip Good signal
- The next artifact appears in the repository.
- The request stays narrow and phase-specific.
:::

## Step 4: Review each handoff before moving on

The normal sequence is:

```
spdd-story → spdd-analysis → spdd-reasons-canvas → spdd-generate
```

After each phase, look for the `SPDD_PHASE_RESULT` block and the new file path it reports.

Check:

- the phase is what you expected
- the output file exists where the result block says it does
- the summary matches the feature you are trying to ship

::: tip Good signal
- You catch requirement drift early.
- You preserve traceability from idea to implementation.
:::

## Step 5: Generate the implementation

Once you have a prompt artifact under `spdd/prompt/`, run:

::: code-group

```text [Codex]
Use the spdd-generate skill on @spdd/prompt/PROMPT-001.md.
```

```text [Claude Code]
/specark:spdd-generate @spdd/prompt/PROMPT-001.md
```

:::

::: tip Good signal
- Implementation files change in the repository.
- The generated code reflects the operations defined in the prompt.
- You can now review code and run verification.
:::

## Step 6: Add a release-ready checkpoint

```bash
git switch -c feature/first-feature
```

::: info Worktrees (optional)
If you want to compare two alternative prompt or implementation paths, a worktree is useful. It keeps the main branch clean while you explore A/B variants in parallel.
:::

::: tip Good signal
- You can recover cleanly if one variant goes wrong.
- Design and implementation checkpoints stay easy to review.
:::

## Step 7: Finish the handoff

Once the generated code and any required verification look correct:

- review the changed files
- run the relevant tests or validation commands for the consuming project
- prepare the normal repository handoff, such as a commit or pull request

::: warning Prompt-first rule
If there is a mistake in the implementation, check whether it came from the prompt first. Fix the prompt and then regenerate the affected code instead of patching the output directly. Patching generated code without updating the prompt creates drift.
:::

::: tip Done
- The feature is ready for normal team review.
- The prompt and implementation stay in sync.
:::

## Common pitfalls

::: warning Avoid these
- Jumping into `spdd-generate` with only an idea or analysis file — you need a prompt artifact first.
- Editing generated code for prompt-contract mistakes without updating the prompt first.
- Treating worktrees as mandatory instead of optional.
:::

## Read next

1. [Workflow Overview](/workflow/)
2. [Phase Handoffs](/workflow/phase-handoffs)
3. [Release Notes](/release-notes)
