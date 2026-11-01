---
name: inquiry
description: Agents can use this meta skill to investigate unfamiliar questions, find original sources and test competing explanations. Use for research, unclear technical behavior, disputed facts or authorized research practice. Return findings, supporting evidence and open questions.
---
# Inquiry: Research and Source Checking

Use this skill to build an explanation from available evidence. It covers search terms, original sources, repeated claims from one source, alternative explanations and small tests that could change the conclusion.

## Meta skill role

Agents use this meta skill to guide how they investigate a question and select evidence. A task skill can retrieve documents or run an experiment; Inquiry helps choose the check and interpret what it establishes.

## When to use

Use when a question needs investigation, sources disagree or an explanation is uncertain. Research agents can compare claims, coding agents can investigate behavior and work assistants can check factual statements.

## Available tools

Choose methods that fit the tools and access available in the current session. Work from supplied material when access is limited. State which searches, tests or checks were completed, which remain unverified and what would be needed to complete them.

## Method
Choose the research depth according to the question and its consequences. Build a terminology list with unique terms, synonyms, historical names, translations and exclusions. Search primary sources, archives and citation chains; group sources that repeat the same original claim. Try alternative interpretations and label conjectures explicitly. Form competing hypotheses when useful. Validate measurements: construct, controls, confounders, sensitivity and discrimination. Design a small experiment that could disprove the explanation. Preserve evidence and dead ends; stop when adequately answered.

## Expected result

Return the question, sources examined, findings, competing explanations and remaining uncertainty. Explain which next check would be useful or why the available evidence is sufficient.

## Shared contract
* D documented; O directly observed; R independently reproduced; H hypothesis; U unknown; X contradicted.
* The person or host agent controls purpose, permissions, tool execution and collaboration.
* Support measurements, search results and execution claims with recorded evidence. Choose the smallest action that answers the next question.
* Report evidence, tested scope, limitations, progress and the reason for continuing or stopping.

See `references/` in the package for extended methods.

## Optional research practice

When the user requests investigative practice or evaluation, use [guided research practice](../../references/research-apprenticeship.md). Select a challenge with clear limits and keep the evaluator's preparation and answers separate from the investigator's context. Record explanations, instrument choices, distinguishing tests, failed attempts and evidence. Assess the method and the result separately.

## Example request

Investigate the conflicting explanations in these reports. Trace the original sources, list the assumptions and identify a check that could resolve the disagreement.

## Method contract

This section matches the [shared contract registry](../../contracts/skill-contracts.json). See [evidence and handoff rules](../../references/evidence-handoff-rules.md) when another skill needs the result.

* **Activation:** A question, disputed claim or unexplained behavior needs investigation.
* **Routine handling:** Answer a simple lookup directly when the available evidence settles the question.
* **Required inputs:** A question or observation to investigate.
* **Helpful context:** Sources and earlier findings; Constraints and intended use; Available tools and resource limits.
* **Missing inputs:** Clarify a missing question. Use supplied sources when access is limited and identify which conclusions remain open.
* **Evidence produced:** Source linked findings and competing explanations; Completed checks and their scope; Conflicting evidence and open questions.
* **Records produced:** Claim linked evidence records; An investigation summary and proposed checks.
* **Recommendations:** Accept a conclusion within stated limits; Run a useful next check; Narrow or defer the investigation.
* **Authority:** Research, tool use and sharing follow existing user authorization. Changes to purpose, access or commitments remain with the user and host.
* **Stop when:** The question is answered within the agreed scope; A required source or authorization is unavailable; The agreed budget ends.
* **Outcome status:** `resolved`, `provisional`, `inconclusive`, `blocked`, `stopped`.
* **Reopen when:** New sources or counterexamples; Changed scope or intended use.
* **Possible consumers:** `judgment`, `discovery`, `toolcraft`, `contribution`.
* **Failure handling:** Preserve useful partial findings and return an inconclusive or blocked result with the missing evidence and next useful check.
* **Optional methods:** `scientific-model-formation`, `epistemic-boundary-exploration`, `associative-evidence-recall`.

## Optional model formation

Agents can use [model formation](../../references/scientific-model-formation.md) when surprising observations or competing mechanisms require discriminating predictions. Record operational definitions, alternatives, falsifiers and a useful next test. Use [evidence boundaries](../../references/epistemic-boundaries.md) to preserve the observed domain and proposed transfer. Return an underdetermined result when available observations leave the models unresolved.

## Optional evidence recall

Agents can use [evidence recall](../../references/associative-evidence-recall.md) to reconstruct earlier conclusions and compare their applicability with the current task. Preserve source records, contradictions, scope and uncertainty. Search by mechanism and constraints as well as familiar terms. Mark missing sources unreconstructable and keep verification unresolved.
