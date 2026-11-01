---
name: contribution
description: Agents can use this meta skill to identify useful results, lessons and reusable work from a task or project. Use for project reviews, incomplete efforts, knowledge records or transfer of a method. Return verified contributions, their source, limits and possible reuse alongside the project outcome.
---
# Contribution: Useful Results and Lessons

Use this skill to preserve work that has demonstrated value. It covers findings, methods, components, failed hypotheses, lessons and unexpected useful results, with evidence of what each result supports.

## Meta skill role

Agents use this meta skill to identify what should be retained from completed or partial work and why it may be useful elsewhere. Task skills can save an artifact or update a record. Contribution guides the evidence, attribution, limits and proposed reuse recorded with it.

## When to use

Use when work ends, a project changes direction or a method could help another task. Research, coding, knowledge and work assistants can preserve verified components, findings, decisions and open questions.

## Available tools

Choose methods that fit the tools and access available in the current session. Work from supplied material when access is limited. State which searches, tests or checks were completed, which remain unverified and what would be needed to complete them.

## Method
Record the project outcome separately from partial progress. Identify verified methods, tools, experiments, insights, negative results and unexpected useful results. Assess each contribution for evidence, scope, limits, privacy and reuse. Report what worked, what was learned and what remains. Distinguish progress, achievement, actual adoption and project success. Recommend discard, note, useful for this task or reusable. Support each contribution with evidence of its value or use. Share with collaborators when authorized.

## Expected result

Return the project outcome and a separate record of useful contributions, source attribution, supporting evidence, limits and reuse options. Distinguish proposed value from demonstrated value.

## Shared contract
* D documented; O directly observed; R independently reproduced; H hypothesis; U unknown; X contradicted.
* The person or host agent controls purpose, permissions, tool execution and collaboration.
* Support measurements, search results and execution claims with recorded evidence. Choose the smallest action that answers the next question.
* Report evidence, tested scope, limitations, progress and the reason for continuing or stopping.

See `references/` in the package for extended methods.

## Transferring a useful method

When a method is worth reusing, record what it explains, when it applies, counterexamples, instruments, reproduction steps and possible uses. Keep a proposed analogy separate from a tested transfer. Record whether another task actually used the method successfully. See [guided research practice](../../references/research-apprenticeship.md) for an optional explanation and transfer review.

## Example request

Preserve useful methods and tested components from this cancelled experiment. Record their evidence, limits and possible uses in future work.

## Method contract

This section matches the [shared contract registry](../../contracts/skill-contracts.json). See [evidence and handoff rules](../../references/evidence-handoff-rules.md) when another skill needs the result.

* **Activation:** Completed, failed, stalled or redirected work contains results that may be useful to retain.
* **Routine handling:** Keep the normal task record when a separate reuse or contribution review would add little value.
* **Required inputs:** The work or outcome to review.
* **Helpful context:** Evidence and artifact references; Parent goal status and restrictions; Potential uses and actual reuse records.
* **Missing inputs:** Record candidate contributions as unverified when supporting evidence or artifacts are missing. Preserve any confirmed value.
* **Evidence produced:** Support for each useful finding, method or component; Attribution, limitations and evidence of reuse; Unresolved parts of the parent outcome.
* **Records produced:** A contribution record separate from the parent outcome; Retention and reuse recommendations with restrictions.
* **Recommendations:** Discard, retain as a note, keep for the task or propose wider reuse; Test a possible transfer before claiming successful reuse.
* **Authority:** Retention, publication, sharing and catalog changes follow existing user authorization. A useful component retains its own tested scope.
* **Stop when:** Each candidate contribution has a documented disposition; Evidence is insufficient to establish a candidate value; The agreed review scope is complete.
* **Outcome status:** `resolved`, `provisional`, `inconclusive`, `blocked`, `stopped`.
* **Reopen when:** New evidence of usefulness or limitations; Actual reuse succeeds or fails; Privacy, ownership or retention conditions change.
* **Possible consumers:** `purpose-planning`, `toolcraft`, `inquiry`.
* **Failure handling:** Return supported contributions, uncertain candidates and missing records while keeping the parent outcome accurate.
* **Optional methods:** `evidence-linked-narrative-representation`.

## Optional narrative summaries

When the user requests a narrative or an approved evaluation includes it, agents can use [narrative summaries](../../references/archetypal-reasoning.md) to explain retained results. Keep the structured records available and link factual statements to evidence identifiers. Preserve uncertainty, scope, failed checks and the parent outcome. Record hypothetical events as hypothetical. Assess reuse and improvement through observed evidence.
