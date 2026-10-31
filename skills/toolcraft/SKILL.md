---
name: toolcraft
description: Help an agent find, adapt or build a tool for a defined task. Use when available tools leave a practical capability gap, a file format is unfamiliar or repeated manual work needs a helper. Return a tested approach, its limits and useful artifacts.
---
# Toolcraft: Finding and Building Tools

Use this skill to identify a missing capability and choose a practical way to supply it. It covers existing tools, configuration, small scripts, unfamiliar interfaces, limited experiments and checks of actual behavior.

## When to use

Use when a task needs a parser, conversion, extraction, calculation or another capability that available tools only partly support. Begin by checking existing resources and access.

## Available tools

Choose methods that fit the tools and access available in the current session. Work from supplied material when access is limited. State which searches, tests or checks were completed, which remain unverified and what would be needed to complete them.

## Method
Identify whether the task needs a tool, information, configuration changes or authorization. Prefer existing local tools or other authorized resources, then configure, compose, extend or build as needed. Investigate undocumented interfaces via exports, headers, symbols, observed errors, ownership and behavior in each version. Build minimal probes in authorized isolation. Compare baseline and perturbations. Validate real execution, failure modes, resource limits and measurement correctness. Retain the results and any code with a clear reuse case. Remove disposable probes after use.

## Expected result

Return the chosen approach, the reason for choosing it, artifacts created, execution evidence, known limits and remaining checks. Identify which temporary work is worth retaining.

## Shared contract
* D documented; O directly observed; R independently reproduced; H hypothesis; U unknown; X contradicted.
* The person or host agent controls purpose, permissions, tool execution and collaboration.
* Support measurements, search results and execution claims with recorded evidence. Choose the smallest action that answers the next question.
* Report evidence, tested scope, limitations, progress and the reason for continuing or stopping.

See `references/` in the package for extended methods.

## Tools for research practice

For an authorized research challenge, choose a small instrument that can distinguish the competing explanations. Explain why it helps and check it on a known sample. Keep temporary code and artifacts separate from the working project. See [guided research practice](../../references/research-apprenticeship.md) when setting up or supporting an evaluation.

## Example request

Find a way to read this unfamiliar data export. Check existing parsers first, test the approach on the supplied sample and record unsupported parts.
