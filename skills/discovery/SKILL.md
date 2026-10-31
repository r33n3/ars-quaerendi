---
name: discovery
description: Help an agent examine unexpected observations, recurring patterns and promising leads. Use for surprising test results, unusual records, operational incidents or patterns across discussions. Return observations, possible explanations and checks that could distinguish them.
---
# Discovery: Unexpected Findings and New Leads

Use this skill to investigate something that differs from expectations or suggests a useful new question. It checks measurement errors, missing context, coincidence and alternative explanations before developing a lead.

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
