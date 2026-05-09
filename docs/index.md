---
layout: home

hero:
  name: "SpecArk"
  text: "Structured Prompt-Driven Development for Codex"
  tagline: "A Git-distributed Codex plugin that turns SPDD into an explicit, file-driven workflow for story creation, analysis, prompt generation, implementation, sync, and API verification."
  actions:
    - theme: brand
      text: Get Started
      link: /getting-started
    - theme: alt
      text: Browse Skills
      link: /skills/
    - theme: alt
      text: Understand the Workflow
      link: /workflow/

features:
  - title: Explicit workflow control
    details: Use one orchestrator to route across story, analysis, prompt, generation, sync, and API-test phases without losing file-backed handoffs.
  - title: Lean phase skills
    details: Each SPDD phase skill stays narrow and contract-focused while canonical source commands remain preserved under plugin references.
  - title: Artifact-driven delivery
    details: Requirements, analyses, prompts, and test assets move forward as repository files instead of repeated pasted context.
  - title: Lower token waste
    details: Narrow inputs, phase-by-phase handoffs, and prompt maintenance flows reduce repeated context and keep requests cheaper.
---

## What this site covers

This documentation explains how the SpecArk plugin is structured, how each `spdd-*` skill fits into the SPDD lifecycle, and how to install, operate, and extend the plugin safely.

Use this site when you need to:

- install the plugin into Codex from a Git-backed marketplace
- run the docs site locally during plugin development
- understand which skill to invoke for a given stage of delivery
- keep token usage under control while moving phase to phase
- use the orchestrator without drifting from the defined workflow
- maintain or expand the plugin itself

## Core model

SpecArk packages Structured Prompt-Driven Development into a Codex plugin with explicit invocation semantics. The skills are not meant to behave like vague assistants. They behave more like disciplined commands with clear input artifacts, output artifacts, and handoff contracts.

The workflow is organized around these concepts:

- large ideas can be split into implementation-sized stories
- focused requirements can be analyzed into strategic context
- strategic context can be turned into a REASONS Canvas prompt
- prompts can drive implementation and downstream verification assets
- changes can flow back into prompts when requirements or code drift

## Read next

- Start with [Getting Started](/getting-started).
- Review [Limitations](/limitations) before broadening the workflow.
- Check [Next Steps](/next-steps) for release polish tasks.
- Use [Release Notes](/release-notes) for release preparation and summary structure.
- Use [Maintainer Notes](/maintainer-notes) when extending the plugin.
- Review the [Workflow Overview](/workflow/).
- Browse the [Skill Index](/skills/).
