# High-Quality SpecArk Skill Authoring Guide

Use this guide when creating or revising skills under `plugins/specark/skills/`.

The goal is not just to make a skill longer. The goal is to make it operationally complete, easy for an agent to follow under pressure, and explicit about how the skill should behave inside this repository.

Good long-form skills reduce ambiguity, preserve workflow discipline, and make future maintenance cheaper. Bad long-form skills are just verbose wrappers with weak instructions repeated many times. This guide is meant to help produce the first kind and avoid the second.

## What “High Quality” Means Here

A high-quality SpecArk skill should do four things well:

- explain exactly when the skill should and should not be used
- define the workflow in a way that is executable, not merely descriptive
- identify the repository files, references, and artifacts that control the work
- constrain ambiguity so two different agents would make roughly the same decisions

The best test is this:

If an agent opens only the skill and the referenced files it names, can it perform the task with high confidence and low interpretation drift?

If the answer is no, the skill is probably still under-specified.

## Target Shape Of A Strong Skill

For non-trivial skills, the `SKILL.md` should usually include most of these sections:

1. purpose and trigger conditions
2. scope and non-goals
3. required startup reads
4. execution contract
5. repository term mapping
6. workflow or operating loop
7. decision rules and heuristics
8. artifact and file conventions
9. validation or completion contract
10. stop conditions and failure handling
11. output/reporting expectations

Not every skill needs every section. But if the task involves orchestration, artifact handoffs, review gates, downstream dependencies, or file conventions, omitting these sections usually lowers quality.

## What To Optimize For

When writing a SpecArk skill, optimize for:

- predictability: the skill leads to stable behavior
- traceability: the skill makes inputs, outputs, and decisions visible
- local correctness: repository paths, filenames, and artifact types are precise
- guarded autonomy: the agent can act independently, but only inside well-defined bounds
- useful verbosity: explanation exists to remove ambiguity, not to inflate word count

## What To Avoid

Do not mistake repetition for quality.

Avoid these common failure modes:

- vague instructions such as “handle this appropriately” or “use best judgment” without decision criteria
- references to “the workflow” without naming the exact file or contract that defines it
- long descriptions of intent without an actual execution sequence
- mixing hard requirements with optional advice without labeling which is which
- hidden assumptions about filenames, folders, or artifact types
- telling the agent to be careful without stating what to validate
- summarizing another canonical command when the skill should instead instruct the agent to read it directly

## Writing Style Rules

Use direct operational language.

- prefer “Read `path/file.md` before doing X” over abstract guidance
- prefer “Stop if A, B, or C is true” over soft warnings
- prefer “Validate these fields” over “make sure the output looks right”

For long skills, structure matters more than prose elegance.

- use section headings that describe operational intent
- keep bullets concrete and mutually distinct
- separate mandatory rules from heuristics
- separate normal flow from blocked flow
- separate phase logic from reporting logic

If a section does not change agent behavior, question whether it belongs in the skill.

## A Strong Skill Should Define These Explicitly

### 1. Trigger Conditions

State when the skill should be used and when it should not be used.

Good:

- “Use this skill when the user wants to continue an SPDD workflow from an existing prompt artifact.”
- “Do not use this skill to create a new story from a broad feature request.”

Weak:

- “Use this skill for prompt work.”

### 2. Scope And Non-Goals

Explain what the skill owns versus what related skills own.

This matters especially in plugin ecosystems where multiple skills are adjacent. A good skill tells the agent where its boundary is.

For example:

- “This skill coordinates phases but does not replace the phase skills.”
- “This skill updates a prompt artifact but does not implement code.”

### 3. Required Startup Reads

Name the exact files the agent must read before acting.

If those files are authoritative, say so. If there is a precedence rule, say so explicitly.

Example:

- `../../references/orchestrator-contract.md` defines review gates and start-phase detection
- if that contract conflicts with this wrapper, the contract wins

### 4. Execution Contract

Tell the agent how strictly to follow the workflow.

Useful patterns:

- read the canonical command file every time
- do not summarize or reinterpret canonical text
- do not skip validation or reporting blocks
- do not continue from malformed outputs

This is where you convert the skill from “guidance” into “operating procedure”.

### 5. Repository Term Mapping

If the original source workflow came from another environment, map its terms into this repository clearly.

Examples:

- what “Read” means locally
- what `@file` and `@folder` correspond to
- what “save” means in repo terms
- what command aliases map to which local skills

This avoids tool-context drift and is especially important when porting workflows from other assistants.

### 6. Workflow Or Operating Loop

For anything multi-step, provide an ordered loop.

Example pattern:

1. determine mode
2. detect starting artifact
3. run one phase
4. require a result block
5. validate the block
6. decide whether to stop or continue

This section is one of the biggest differences between a high-quality skill and a merely descriptive one.

### 7. Decision Rules And Heuristics

Where judgment is needed, specify the basis for judgment.

For example:

- when to route to `spdd-story` versus `spdd-analysis`
- when to stop and ask the user instead of continuing
- when a resume request should preserve lineage versus restart

Do not leave important branch decisions at “use best judgment” if the branch can be described concretely.

### 8. Artifact And File Conventions

If a workflow produces files, define:

- expected folders
- naming conventions
- whether paths must be repository-relative
- which artifact types feed which downstream phases

This prevents silent breakage in orchestrated flows.

### 9. Validation And Completion

Specify what a successful phase or skill run must produce.

Examples:

- a required result block
- expected fields inside that block
- expected folder or file type by phase
- required summary or next-phase field

If the skill consumes outputs from another skill, this section is mandatory.

### 10. Stop Conditions And Failure Handling

A mature skill tells the agent when not to continue.

Typical stop conditions:

- ambiguous starting input
- missing artifact path
- malformed downstream result block
- conflicting user controls
- missing required review approval

Also specify what the agent should report when blocked.

### 11. Output Expectations

Define how the agent should report status back to the user.

This is especially useful for controller skills. The user should be able to tell:

- what happened
- what file was consumed
- what file was produced
- what happens next

## When To Be Verbose

Add explanation when the extra text helps with:

- decision quality
- workflow correctness
- artifact handoff reliability
- safety around ambiguity
- interoperability between related skills

Do not add explanation just because the skill feels too short.

Useful verbosity explains:

- why a rule exists
- how to interpret a control
- what should happen when a rule and a user request conflict
- how to distinguish nearby cases that route differently

Low-value verbosity repeats:

- that the agent should be careful
- that the user wants quality
- that the workflow matters
- that artifacts are important, without saying how

## Suggested Skill Skeleton

Use this as a starting structure for substantial SpecArk skills:

```md
---
name: example-skill
description: Clear trigger-oriented description of what the skill does and when to use it.
---

# example-skill

Short definition of the skill and its operational purpose.

## Scope

- what this skill does
- what this skill does not do

## Required Startup Reads

- `path/to/reference.md`
- `path/to/related/SKILL.md`

## Execution Contract

1. read the canonical reference every time
2. follow it exactly
3. when conflicts exist, the canonical reference wins

## Repository Term Mapping

- source term -> local meaning

## Workflow

1. determine starting state
2. resolve controls
3. execute the required operation
4. validate outputs
5. report status

## Decision Rules

- routing rule A
- routing rule B

## Validation

- expected output field A
- expected output file path B

## Stop Conditions

- ambiguity A
- missing artifact B

## Output Contract

- required reporting fields
```

## How To Decide Between A Thin Wrapper And A Rich Skill

A thin wrapper is enough when:

- the canonical source command already contains nearly all behavior
- the local skill only needs a small amount of repository term mapping
- there are few branch decisions
- the workflow is phase-local and not cross-cutting

A rich skill is warranted when:

- it coordinates multiple other skills
- it decides routing between several possible workflows
- it manages review gates or stop conditions
- it passes artifacts between phases
- it needs to interpret user controls that change flow behavior

The orchestrator class of skill should almost always be rich, because orchestration quality depends on explicit decision-making rules.

## Review Checklist For Future Skill Edits

Before considering a skill “high quality”, check:

- does the description clearly trigger on the right requests?
- does the body explain when not to use the skill?
- are authoritative references named explicitly?
- is there an ordered operating procedure?
- are decisions and branches explained concretely?
- are artifact paths and output expectations defined?
- does the skill say when to stop instead of guessing?
- would another agent produce similar behavior after reading it?

If several answers are no, the skill likely needs structural improvement, not just more text.

## SpecArk-Specific Recommendation

Within this plugin, prefer this pattern:

- thin, contract-focused wrappers for atomic SPDD phase skills
- richer, more explicit instructions for cross-phase controller skills
- repository references for reusable standards that multiple skills may share

That keeps the phase skills stable and small while letting controller skills carry the extra operational detail where it actually matters.
