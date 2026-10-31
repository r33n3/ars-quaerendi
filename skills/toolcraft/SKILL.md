---
name: toolcraft
description: Find, adapt or build a tool for a specific task
---
# Toolcraft

## When to use
Find, adapt or build a tool for a specific task. Use existing tools directly for routine tasks.

## Method
Identify whether the task needs a tool, information, configuration changes or authorization. Prefer existing local tools or other authorized resources, then configure, compose, extend or build as needed. Investigate undocumented interfaces via exports, headers, symbols, observed errors, ownership and behavior in each version. Build minimal probes in authorized isolation. Compare baseline and perturbations. Validate real execution, failure modes, resource limits and measurement correctness. Retain the results and any code with a clear reuse case. Remove disposable probes after use.

## Shared contract
* D documented; O directly observed; R independently reproduced; H hypothesis; U unknown; X contradicted.
* The person or host agent controls purpose, permissions, tool execution and collaboration.
* Support measurements, search results and execution claims with recorded evidence. Choose the smallest action that answers the next question.
* Report evidence, tested scope, limitations, progress and the reason for continuing or stopping.

See `references/` in the package for extended methods.
