---
name: judgment
description: Agents can use this meta skill to assess whether evidence supports a claim, decision or intended use. Use for completed research, proposed releases, performance reports or disputed conclusions. Return a recommendation tied to evidence, scope and uncertainty.
---
# Judgment: Evidence and Readiness Review

Use this skill to review a conclusion or proposed action against its supporting evidence. It examines source history, completed checks, counterexamples, consequences of error and the limits of a recommendation.

## Meta skill role

Agents use this meta skill to decide what a result supports and whether it is ready for an intended use. A task skill can run tests or extract records; Judgment assesses the evidence, uncertainty and limits of the resulting conclusion.

## When to use

Use when findings are ready for a decision, a conclusion is disputed or a tool is being considered for a particular use. Research, release review, reporting and meeting agents can use it to assess what the available record supports.

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

## Reviewing an explanation

When a significant result or research challenge needs explanation, compare the account with the actual records and artifacts. Check the initial expectation, observations, alternative explanations, decisive test, limits and reproduction steps. Mark unsupported parts as unverified and narrow conclusions to the evidence. See [guided research practice](../../references/research-apprenticeship.md) for the optional explanation review method.

## Example request

Review this proposed release using the test results and known limits. State which uses the evidence supports and which checks remain open.

For analysis of meeting comments, commitments and recurring behaviors, see [meeting notes](../../docs/meeting-notes.md).

## Method contract

This section matches the [shared contract registry](../../contracts/skill-contracts.json). See [evidence and handoff rules](../../references/evidence-handoff-rules.md) when another skill needs the result.

* **Activation:** A claim, interpretation or proposed use needs assessment against evidence and consequences.
* **Routine handling:** Report an already established result directly when a further readiness or evidence decision is unnecessary.
* **Required inputs:** The claim or proposed decision.
* **Helpful context:** Evidence records and source references; Intended use, criteria and consequences; Earlier judgments and counterexamples.
* **Missing inputs:** Assess the supplied claim with explicit evidence gaps. Keep intended use or readiness unresolved when its criteria are missing.
* **Evidence produced:** Checks supporting or challenging the claim; Verification gaps, scope and uncertainty; Basis for the assigned judgment level.
* **Records produced:** A scoped assessment and recommendation; Open checks and evidence references.
* **Recommendations:** Proceed within supported conditions; Limit use, revise or request evidence; Seek further review or stop.
* **Authority:** Judgment assesses support and readiness. The user and host authorize deployment, commitments, access and execution.
* **Stop when:** The evidence supports a scoped recommendation; An explicit gap makes the assessment inconclusive; The agreed review limit is reached.
* **Outcome status:** `resolved`, `provisional`, `inconclusive`, `blocked`, `stopped`.
* **Reopen when:** New evidence or counterexamples; Changed intended use, risks or criteria; A verification method or source is corrected.
* **Possible consumers:** `contribution`, `purpose-planning`, `reliability-by-construction`.
* **Failure handling:** Return an inconclusive or provisional assessment and identify the missing checks. Preserve contradictory evidence and useful supported findings.
