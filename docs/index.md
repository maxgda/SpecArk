---
layout: home

hero:
  name: "SpecArk"
  text: "Structured Prompt-Driven Development"
  tagline: "A Git-distributed Codex plugin that turns SPDD into an explicit, artifact-driven workflow — from idea to implementation."
  actions:
    - theme: brand
      text: Get Started →
      link: /getting-started
    - theme: alt
      text: First Feature Tutorial
      link: /first-feature
    - theme: alt
      text: Workflow Reference
      link: /workflow/

features:
  - icon: 📄
    title: Start with one artifact
    details: Use a real repository file as the input, then hand artifacts from one phase to the next instead of re-pasting the same context.
  - icon: 🎛️
    title: Explicit workflow control
    details: Use the orchestrator for guided routing or invoke a single spdd-* phase directly when you already have the right artifact.
  - icon: 💡
    title: Low-token delivery
    details: Narrow requests and file-backed handoffs keep prompts smaller, reviews clearer, and iteration cheaper.
  - icon: 🚀
    title: First-user to ship path
    details: Move from install to a first successful feature with guided onboarding, a tutorial path, and clear phase handoffs.
  - icon: 🔁
    title: Clean recovery paths
    details: Use spdd-prompt-update or spdd-sync to correct drift after requirement changes or implementation refactors — no guesswork.
  - icon: 🔍
    title: Full traceability
    details: Every phase leaves a reviewable artifact. Go from idea to code with a clear audit trail in your repository.
---

## Start here if you are new

SpecArk is built for teams and repositories that want a disciplined SPDD workflow instead of loose prompt chains. If you are evaluating the plugin for the first time, start with:

1. [Getting Started](/getting-started)
2. [First Feature Tutorial](/first-feature)
3. [Workflow Overview](/workflow/)

## The workflow at a glance

```
idea.md
  └─ spdd-plan (optional: when input is roadmap-sized)
       └─ spdd-story → requirements/STORY-001.md
            └─ spdd-analysis → spdd/analysis/ANALYSIS-001.md
                 └─ spdd-reasons-canvas → spdd/prompt/PROMPT-001.md
                      └─ spdd-generate → implementation files
                           └─ spdd-api-test → spdd/tests/ (optional)
```

Each phase produces a repository file. The next phase reads that file directly — no context re-pasting.

## What this site covers

Use this documentation when you need to:

- install the plugin into Codex from a Git-backed marketplace
- choose the right SPDD phase for the artifact you already have
- understand how handoff artifacts move from story to analysis to prompt to implementation
- keep token usage low while still preserving reviewable workflow checkpoints
- maintain or extend the plugin after the first-user path is already clear

## Read next

- Start with [Getting Started](/getting-started).
- Continue with the [First Feature Tutorial](/first-feature).
- Review the [Workflow Overview](/workflow/).
- Browse the [Skill Index](/skills/).
- Use [Maintainer Notes](/maintainer-notes) only when you are extending the plugin itself.
