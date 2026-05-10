# Getting Started

SpecArk is a Codex plugin bundle for Structured Prompt-Driven Development. This page is the fastest path to a first successful run if you are using the plugin for the first time.

## Before you start

You are in the right place if you want:

- a repeatable path from idea or requirement to implementation
- file-backed artifacts between phases
- an explicit skill surface instead of vague prompting
- a clear handoff from one phase to the next

If you only need installation details or local docs commands, jump to [Installation](/installation).

## Step 1: Install with the two-command startup

```bash
codex plugin marketplace add <owner>/<repo>
codex plugin marketplace upgrade
```

::: tip After install
- The plugin is available in Codex.
- You can reference `spdd-*` skills in a request.
- You are ready to give the workflow a real input artifact.
:::

## Step 2: Pick the right first command

Most first-time users should start with the orchestrator:

```text
Use the spdd-orchestrator skill on @idea-of-the-enhancement.md in semi-auto mode.
```

Use a manual phase only when you already have the matching artifact:

| Your artifact | Start phase |
|---|---|
| Broad idea or noisy PRD | `spdd-plan` → `spdd-story` |
| Broad requirement | `spdd-story` |
| Focused story or requirement | `spdd-analysis` |
| Analysis artifact in `spdd/analysis/` | `spdd-reasons-canvas` |
| Prompt artifact in `spdd/prompt/` | `spdd-generate` |

::: tip Good signal
- You are not forcing a broad idea into `spdd-generate`.
- Your command matches the artifact you actually have.
- The workflow starts from the smallest valid phase instead of repeating context.
:::

## Step 3: Watch the artifact handoff

SpecArk works best when each phase creates a file that becomes the next phase's input.

```
idea.md
  └─ requirements/STORY-001.md       ← spdd-story
       └─ spdd/analysis/ANALYSIS.md  ← spdd-analysis
            └─ spdd/prompt/PROMPT.md ← spdd-reasons-canvas
                 └─ implementation   ← spdd-generate
                      └─ spdd/tests/ ← spdd-api-test (optional)
```

::: tip Good signal
- Each step leaves behind a repository file.
- The next command points at that file instead of pasting the same context again.
- You can inspect the artifact before moving forward.
:::

## Step 4: Know when to choose orchestrator vs manual flow

**Choose the orchestrator when:**

- the requirement is broad
- you want review gates between phases
- you are still learning the workflow

**Choose manual phase entry when:**

- you already have the correct artifact for the next phase
- you want a narrow, single-purpose request
- you are resuming work after a previous phase already completed

## Step 5: Continue into your first feature

Once installation and the first artifact flow make sense, use the full end-to-end walkthrough:

- [First Feature Tutorial](/first-feature)

That tutorial covers:

- install through first implementation
- expected output after each step
- lightweight git guidance on branches, commits, and worktrees
- how to hand the feature off for release-ready review

## Common mistakes

::: warning Avoid these
- Starting with `spdd-generate` before a prompt exists in `spdd/prompt/`.
- Re-pasting the full requirement into every phase instead of passing the produced artifact.
- Treating README, getting started, and workflow reference pages as interchangeable.
- Mixing maintainer-only local plugin work with the first-time adopter path.
:::

## Read next

1. [First Feature Tutorial](/first-feature)
2. [Workflow Overview](/workflow/)
3. [Phase Handoffs](/workflow/phase-handoffs)
4. [Skill Index](/skills/)
