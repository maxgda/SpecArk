---
name: spdd-discovery
description: Interview early, unclear, or noisy product context and write a Discovery Brief before planning, story splitting, or analysis begins.
disable-model-invocation: true
---

# spdd-discovery

Use this skill only when the user explicitly invokes a Discovery Interview for rough ideas, noisy notes, pasted context, or referenced files that need to become a Discovery Brief before `spdd-plan`, `spdd-story`, or `spdd-analysis`.

## Scope And Non-Goals

This skill owns early discovery intake, interview flow, and Discovery Brief creation.

It should:

- consolidate discovery input from free text, pasted notes, and referenced files
- validate source references before using them
- ask one focused question at a time when high-impact context is missing
- write exactly one Discovery Brief under `spdd/discovery/` when ready
- recommend exactly one next phase from `spdd-plan`, `spdd-story`, or `spdd-analysis`

It must not:

- generate stories, technical analysis artifacts, REASONS Canvas prompts, implementation code, or tests
- update source requirements, prompts, or implementation files
- perform Context Review Interview behavior
- invoke downstream skills automatically
- change orchestrator routing or start-phase detection

## Required Startup Reads

Read these files before making interview, routing, or artifact decisions:

- `../../references/high-quality-skill-authoring.md`
- `../../references/orchestrator-contract.md`
- `../spdd-plan/SKILL.md`
- `../spdd-story/SKILL.md`
- `../spdd-analysis/SKILL.md`

If any required startup read is missing or unreadable, stop and report a blocked outcome.

## Execution Contract

Treat this skill as a repository-native local command wrapper, not as a wrapper around an upstream source command.

You must:

- keep the interview focused on product clarity and downstream routing
- issue a short user-visible preamble before repository searches or file reads
- read every referenced file completely before relying on it
- keep all reported and generated paths repository-relative
- derive Discovery Brief filenames with `../../scripts/derive_spdd_filename.py`
- block when required startup reads are missing

## Repository Term Mapping

- `spdd/discovery/` is the only valid output folder for Discovery Briefs
- a Discovery Brief is a durable Markdown handoff artifact for unclear early context
- referenced paths are user-provided `@file`, `@folder`, or repository-relative paths
- free-text context includes rough ideas, pasted notes, meeting fragments, and inline requirements
- interview answers are user-confirmed context and must be kept distinct from model inferences
- valid downstream phases are exactly `spdd-plan`, `spdd-story`, and `spdd-analysis`

## Interview Loop

1. Read the required startup references.
2. Validate and read supplied source references completely.
3. Consolidate free-text context, pasted notes, referenced files, and interview answers.
4. Check readiness criteria.
5. If one high-impact criterion is missing, ask exactly one focused question.
6. If a missing file, wrong artifact, contradiction, user pause, or unresolved routing ambiguity prevents progress, block.
7. If ready, write exactly one Discovery Brief and report the result block.

Never present a multi-question checklist. Ask the next single question that most improves problem framing, user value, scope boundaries, or downstream routing.

## Readiness Criteria

Write a Discovery Brief only when the context establishes:

- the problem or opportunity
- the beneficiaries or stakeholders
- the desired outcome
- what is in scope
- what is out of scope
- exactly one recommended next phase
- acceptable remaining uncertainty that can safely be carried into the next phase

## Source Handling

Every referenced file must be validated and read completely before use. If a referenced file is missing or unreadable, ask for one replacement path or block if the run cannot continue.

Clarify before writing when sources conflict on scope, users, artifact location, or downstream routing. Do not silently choose between contradictory sources.

## Artifact Conventions

- use `../../scripts/derive_spdd_filename.py` with `kind=discovery`
- store the artifact under `spdd/discovery/`
- use repository-relative paths in the artifact and result block
- use a concise slug based on the topic, not the full conversation

Completed Discovery Briefs must include these exact sections:

1. Source Context
2. Interview Summary
3. Problem Frame
4. Target Users And Stakeholders
5. Desired Outcomes
6. Scope In
7. Scope Out
8. Workflow And User Journey
9. Domain Concepts And Terms
10. Constraints And Policies
11. Data, Integrations, And Repository Touchpoints
12. Risks And Assumptions
13. Open Questions
14. Recommended Next Phase
15. Evidence Log

## Validation Rules

Before reporting success, verify all of the following:

- exactly one Discovery Brief exists under `spdd/discovery/`
- every required section is present
- user-confirmed answers and model inferences are distinguishable
- every source path is repository-relative
- the recommended next phase is exactly one of `spdd-plan`, `spdd-story`, or `spdd-analysis`
- no story, analysis, prompt, implementation, or test artifact was produced

## Stop Conditions And Failure Handling

Stop immediately when:

- a required startup read is missing or unreadable
- a referenced file is missing, unreadable, or the wrong artifact type and no replacement is available
- source context is contradictory on scope, users, artifact location, or routing
- the user pauses or declines to provide discovery context
- exactly one downstream phase cannot be recommended
- high-impact context remains insufficient after the interview has tried to gather it

With no input, ask exactly one starter question for a rough idea, pasted notes, or file reference. Do not block immediately unless the user cannot or will not provide any discovery context.

## Output Expectations

Successful runs must provide:

- consumed source context
- produced `spdd/discovery/` artifact path
- recommended next phase
- validation notes and material open questions

Blocked runs must use `output_files: none` and `recommended_next_phase: none`.

End with this exact block format:

```text
SPDD_DISCOVERY_RESULT
status: completed|blocked
artifact_type: discovery
output_files:
- <repo-relative-path|none>
recommended_next_phase: spdd-plan|spdd-story|spdd-analysis|none
review_recommended: yes|no
summary: <single-line summary>
END_SPDD_DISCOVERY_RESULT
```
