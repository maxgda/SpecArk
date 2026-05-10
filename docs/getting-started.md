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

What good looks like:

- the plugin is available in Codex
- you can reference `spdd-*` skills in a request
- you are ready to give the workflow a real input artifact

## Step 2: Pick the right first command

Most first-time users should start with the orchestrator:

```text
Use the spdd-orchestrator skill on @idea-of-the-enhancement.md in semi-auto mode.
```

Use a manual phase only when you already have the matching artifact:

- Broad idea: start with `spdd-story`
- Existing story or focused requirement: start with `spdd-analysis`
- Existing analysis artifact in `spdd/analysis/`: start with `spdd-reasons-canvas`
- Existing prompt artifact in `spdd/prompt/`: start with `spdd-generate`

What good looks like:

- you are not forcing a broad idea into `spdd-generate`
- your command matches the artifact you actually have
- the workflow starts from the smallest valid phase instead of repeating context

## Step 3: Watch the artifact handoff

SpecArk works best when each phase creates a file that becomes the next phase's input.

Typical output locations:

- `spdd/plan/`
- `requirements/`
- `spdd/analysis/`
- `spdd/prompt/`
- `spdd/tests/`

Typical progression:

```text
idea.md
-> requirements/STORY-001.md
-> spdd/analysis/ANALYSIS-001.md
-> spdd/prompt/PROMPT-001.md
-> implementation files
-> spdd/tests/<verification assets>
```

What good looks like:

- each step leaves behind a repository file
- the next command points at that file instead of pasting the same context again
- you can inspect the artifact before moving forward

## Step 4: Know when to choose orchestrator vs manual flow

Choose the orchestrator when:

- the requirement is broad
- you want review gates between phases
- you are still learning the workflow

Choose manual phase entry when:

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

- Starting with `spdd-generate` before a prompt exists in `spdd/prompt/`
- Re-pasting the full requirement into every phase instead of passing the produced artifact
- Treating README, getting started, and workflow reference pages as interchangeable
- Mixing maintainer-only local plugin work with the first-time adopter path

## Read next

1. [First Feature Tutorial](/first-feature)
2. [Workflow Overview](/workflow/)
3. [Phase Handoffs](/workflow/phase-handoffs)
4. [Skill Index](/skills/)
