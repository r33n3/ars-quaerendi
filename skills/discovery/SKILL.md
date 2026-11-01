---
name: discovery
description: Agents can use this meta skill to examine unexpected observations, recurring patterns and promising leads. Use for surprising test results, unusual records, operational incidents or patterns across discussions. Return observations, possible explanations and checks that could distinguish them.
---
# Discovery: Unexpected Findings and New Leads

Use this skill to investigate something that differs from expectations or suggests a useful new question. It checks measurement errors, missing context, coincidence and alternative explanations before developing a lead.

## Meta skill role

Agents use this meta skill to examine surprises and choose what to investigate next. Task skills can collect logs, calculate values or organize notes. Discovery helps explain an unexpected pattern and identify a useful follow up check.

## When to use

Use when an observation is surprising, a pattern appears across records or an unrelated finding could be useful. Operations agents can review incidents, research agents can examine experimental results and meeting agents can compare recurring concerns.

## Available tools

Choose methods that fit the tools and access available in the current session. Work from supplied material when access is limited. State which searches, tests or checks were completed, which remain unverified and what would be needed to complete them.

## Method
Record expected versus observed results, raw evidence, environment and provenance. Separate anomaly from interpretation. Test for instrument errors, confounders, coverage and coincidence. Change representation where helpful: bytes, hex, entropy, parsed structure, visualization, numerical patterns or execution traces. Develop alternative hypotheses and simple tests that distinguish the explanations. Record leads outside the current task for later investigation. Check prior work before claiming novelty and ask the user before changing the goal.

## Expected result

Return the observation with source references, possible explanations, available checks, open questions and any lead worth preserving. Describe the amount of evidence behind a claimed pattern.

## Shared contract
* D documented; O directly observed; R independently reproduced; H hypothesis; U unknown; X contradicted.
* The person or host agent controls purpose, permissions, tool execution and collaboration.
* Support measurements, search results and execution claims with recorded evidence. Choose the smallest action that answers the next question.
* Report evidence, tested scope, limitations, progress and the reason for continuing or stopping.

See `references/` in the package for extended methods.

## Example request

Review these failure records for recurring conditions around the timeouts. Link each pattern to records and propose checks that distinguish possible causes.

For analysis of meeting comments, commitments and recurring behaviors, see [meeting notes](../../docs/meeting-notes.md).

## Method contract

This section matches the [shared contract registry](../../contracts/skill-contracts.json). See [evidence and handoff rules](../../references/evidence-handoff-rules.md) when another skill needs the result.

* **Activation:** An unexpected observation, recurring pattern or promising lead needs explanation.
* **Routine handling:** Record an ordinary observation directly when it raises no useful new question.
* **Required inputs:** The observation and its available source.
* **Helpful context:** The prior expectation; Comparable records and context; Measurement controls and resource limits.
* **Missing inputs:** Record what was supplied and which expectation or context is missing. Keep possible patterns tentative.
* **Evidence produced:** Source linked anomalies and supporting examples; Alternative explanations and instrument checks; Contradictions, limitations and open tests.
* **Records produced:** A lead with its evidence and scope; A proposed distinguishing check or reason to archive the lead.
* **Recommendations:** Investigate, explain, dismiss or retain a lead; Propose a further check within existing scope.
* **Authority:** Leads and interpretations remain tied to evidence. The user controls goal changes and sharing; novelty claims require appropriate prior work checks.
* **Stop when:** The observation is explained or dismissed; The lead is retained with clear uncertainty; Further checks require unavailable evidence, access or budget.
* **Outcome status:** `resolved`, `provisional`, `inconclusive`, `blocked`, `stopped`.
* **Reopen when:** New comparable observations; Corrected instruments or context; Results of the proposed distinguishing check.
* **Possible consumers:** `inquiry`, `judgment`, `contribution`.
* **Failure handling:** Preserve the observation, alternative explanations and missing checks and keep conclusions limited to supporting evidence.
* **Optional methods:** `optional-archetypal-lenses`.

## Optional reasoning lenses

When the user requests them or an approved evaluation includes them, agents can use [reasoning lenses](../../references/archetypal-reasoning.md) to generate candidate perspectives and falsifiers. Preserve the user's purpose, evidence requirements and stopping rules. One agent can apply the functions sequentially. Creating separate agents follows the user's and host's actual authorization. Treat the labels' benefit as unmeasured until evaluated.
