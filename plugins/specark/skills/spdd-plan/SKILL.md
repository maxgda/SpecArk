---
name: spdd-plan
description: Turn broad or noisy product direction into a reviewable SPDD planning artifact with ordered delivery slices before story generation begins.
disable-model-invocation: true
---

# spdd-plan

Use this skill only when the user explicitly invokes planning for broad product direction before `spdd-story` or `spdd-analysis`.

## Scope And Non-Goals

This skill owns pre-story planning, routing, and artifact creation.

It should:

- consolidate mixed business inputs into one planning context
- inspect the repository just enough to justify planning, redirect, or reuse
- write one roadmap artifact under `spdd/plan/` when planning is warranted
- recommend exactly one next slice and hand it off to `spdd-story`

It must not:

- generate stories directly
- perform technical analysis, REASONS prompt generation, or implementation
- change orchestrator start-phase detection in this release
- invent a plan when redirecting or blocking is the correct result

## Required Startup Reads

Read these files before making routing or artifact decisions:

- `../../references/high-quality-skill-authoring.md`
- `../../references/orchestrator-contract.md`
- `../spdd-story/SKILL.md`
- `../spdd-analysis/SKILL.md`

If any required startup read is missing or unreadable, stop and report a blocked outcome.

## Execution Contract

Treat this skill as a repository-native controller, not as a thin wrapper around a canonical command.

You must:

- keep the prompt outcome-first and organized into short labeled sections
- prefer Markdown headings and lists over XML-style wrappers unless multiple embedded documents require stronger separation
- issue a short user-visible preamble before repository searches or other multi-step tool work
- keep repository lookup bounded to enough evidence for a trustworthy decision
- keep all reported and generated paths repository-relative

## Repository Term Mapping

- user-provided `@file` references or repository paths are authoritative inputs
- free text, pasted notes, and attached file content must be consolidated into the same planning context
- `spdd-story` is the next-phase handoff target for a successful plan
- `spdd-analysis` is the redirect target when the input is already focused and technically analyzable
- `spdd/plan/` is the only valid output folder for planning artifacts

## Prompt Sections

Keep the planning prompt contract short and explicitly labeled:

1. Role
2. Collaboration Style
3. Goal
4. Decision Rules
5. Tool Rules
6. Output Contract
7. Stop Rules

## Workflow

1. Announce the next heavy step before repository search, file discovery, or broad inspection.
2. Read the required startup references.
3. Consolidate all supplied inputs into one cleaned planning context.
4. Record consumed sources and any clearly unrelated material removed from scope.
5. Collect repository evidence only from the minimum surfaces needed to justify planning, redirect, or reuse.
6. Retry once with a narrower query if repository evidence is empty or obviously partial.
7. Stop searching once additional evidence is unlikely to change the decision.
8. Decide whether the run should `plan`, `redirect`, `reuse`, or `block`.
9. Write exactly one plan artifact under `spdd/plan/` only when the decision is `plan`.
10. Validate that the artifact contains ordered slices, dependency notes, sequencing rationale, repository-relative paths, validation notes, and exactly one recommended next slice.
11. Report the final completion block that matches the artifact or redirect state.

## Decision Rules

Mark the run as `plan` only when the input clearly spans multiple capabilities, dependency chains, or phased rollout concerns.

Redirect instead of planning when any of these are true:

- the input is already a coherent implementation story suitable for `spdd-story`
- the requirement is already focused enough for `spdd-analysis`
- repository evidence shows the capability already exists and reuse is the better path

Block instead of planning when any of these are true:

- the context is still too incomplete to create trustworthy slices
- required startup references are missing
- conflicting repository evidence prevents a reliable recommendation

When planning is justified, the artifact must include:

- a short summary of the planning decision
- ordered delivery slices with stable slice identifiers
- dependency notes for each slice
- sequencing rationale for the proposed order
- requirements-to-slice mapping
- repository surfaces consulted
- validation checks and open questions
- exactly one recommended next slice for `spdd-story`

## Retrieval Budget

Repository lookup must stay bounded:

- start with the explicitly referenced files and the required startup reads
- inspect the adjacent skill, docs, and helper-script surfaces most likely to overlap with the request
- retry with one narrower search when the first lookup is empty or clearly partial
- stop once you can explain the decision with enough evidence

Do not run broad speculative scans across unrelated repository areas.

## Artifact And File Conventions

- derive planning filenames with `../../scripts/derive_spdd_filename.py` using `kind=plan`
- store planning artifacts only under `spdd/plan/`
- keep all paths repository-relative in the artifact and completion report
- prefer concise slugs based on the requirement, not long conversational fragments

## Validation Rules

Before reporting success, verify all of the following:

- the decision to plan, redirect, reuse, or block is explicitly justified
- any produced plan artifact exists under `spdd/plan/`
- delivery slices are ordered and reviewable
- dependency notes and sequencing rationale are present
- repository-relative paths are used consistently
- exactly one recommended next slice is named for `spdd-story`
- material open questions are surfaced when they affect readiness

## Stop Conditions And Failure Handling

Stop immediately when:

- required startup references cannot be read
- a user-supplied file path is missing, unreadable, or clearly the wrong artifact type for planning, unless the user explicitly says to proceed with current context
- the input is too incomplete for trustworthy slice planning
- the request is already better served by `spdd-story` or `spdd-analysis`
- repository evidence shows reuse is the correct path

Blocked and redirected outcomes must stay concise, actionable, and explicit about why no planning artifact was written.

## Output Expectations

Successful runs must provide:

- the consumed input path or source set
- the produced `spdd/plan/` artifact path
- the recommended next slice identifier
- the exact next command shape for `spdd-story`
- validation notes and any material open questions

End with this exact block format:

```text
SPDD_PLAN_RESULT
status: completed|redirected|blocked
consumed_inputs:
- <repo-relative-path-or-source>
produced_plan: <repo-relative-path|none>
recommended_next_slice: <slice-id|none>
next_command: Use $spdd-story on <artifact-path or source> for slice <slice-id>.
summary: <single-line summary>
END_SPDD_PLAN_RESULT
```
