---
name: inquiry
description: Agents can use this skill to investigate unfamiliar questions, find original sources and test competing explanations. Use for research, unclear technical behavior, disputed facts or authorized research practice. Return findings, supporting evidence and open questions.
---
# Inquiry: Research and Source Checking

Use this skill to build an explanation from available evidence. It covers search terms, original sources, repeated claims from one source, alternative explanations and small tests that could change the conclusion.

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
