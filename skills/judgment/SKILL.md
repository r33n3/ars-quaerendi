---
name: judgment
description: Help an agent assess whether evidence supports a claim, decision or intended use. Use for completed research, proposed releases, disputed conclusions or interpretations of meeting comments. Return a recommendation tied to evidence, scope and uncertainty.
---
# Judgment: Evidence and Readiness Review

Use this skill to review a conclusion or proposed action against its supporting evidence. It examines source history, completed checks, counterexamples, consequences of error and the limits of a recommendation.

## When to use

Use when findings are ready for a decision, a conclusion is disputed or a tool is being considered for a particular use. In meeting analysis, use it to check whether notes support an interpretation of a comment or recurring behavior.

## Available tools

Choose methods that fit the tools and access available in the current session. Work from supplied material when access is limited. State which searches, tests or checks were completed, which remain unverified and what would be needed to complete them.

## Method
Identify claim, intended use, risk and reversibility. Select J0 exploratory, J1 plausible, J2 supported, J3 verified in tested scope, J4 qualified for specified deployment. Run repeatable tests and checks of source history first. When interpretation needs review, start with one focused challenge and set a limit on revision attempts. Use concrete counterexamples to test conclusions. Mark missing evidence as inconclusive. Recommend proceeding, limiting use, revising, requesting evidence, seeking review or stopping. State which uses the recommendation covers. The user and host environment control authorization.

## Expected result

Return the claim and intended use, supporting and conflicting evidence, completed checks, missing evidence and a recommendation. State the conditions and limits that apply.

## Shared contract
* D documented; O directly observed; R independently reproduced; H hypothesis; U unknown; X contradicted.
* The person or host agent controls purpose, permissions, tool execution and collaboration.
* Support measurements, search results and execution claims with recorded evidence. Choose the smallest action that answers the next question.
* Report evidence, tested scope, limitations, progress and the reason for continuing or stopping.

See `references/` in the package for extended methods.

## Example request

Review whether these notes support the conclusion that a participant agreed to own the work. Cite the relevant comments and identify ambiguity.

For analysis of meeting comments, commitments and recurring behaviors, see [meeting notes](../../docs/meeting-notes.md).
