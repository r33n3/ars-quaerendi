# Agent integration

This package provides meta skills that guide methods, evidence assessment and decisions across tasks. Apply them alongside the task skills and tools needed to perform the work. See `docs/meta-skills.md` for the distinction and examples.

Select skills according to the task:

* Research or uncertainty: `inquiry`.
* Goal formation and planning: `purpose-planning`.
* Missing tool capability: `toolcraft`.
* Evidence assessment: `judgment`.
* Unexpected observations: `discovery`.
* Reusable results: `contribution`.
* Prototype promotion or recurring failures: `reliability-by-construction`.
* Performance measures, progress reports and improvement proposals: `performance-metric-integrity`.
* Negotiations, disputed claims, competing incentives and pressure to change goals: `institutional-intelligence`.

Handle routine tasks directly with available tools. Record project outcomes and partial progress separately. The user and host environment control authorization, execution, deployment and collaboration.

For prototype promotion, consult `references/factory-and-reliability.md`.

For examples of how the skills fit together, consult `docs/integration-flow.md`.

For consequential negotiations, promises, disputed claims or decisions about continued investment, consult `references/institutional-resilience-advanced.md` when those methods would help. Assess behavior through evidence and preserve the user's control of commitments and goals.

For examples of research, coding, planning, operations, reporting, supplier review, learning and meeting agents, consult `docs/agent-examples.md`.

When the user requests investigative practice or evaluation, consult `references/research-apprenticeship.md`. Choose a limited challenge, keep evaluator answers separate and record evidence of the method and result. Explanation review can help transfer significant findings to another task.

Use `purpose-planning` for justified goal proposals, capability gaps, further investment review and comparison with the user's purpose. Include continuing the current goals as an option. Proactive reviews follow existing user instructions, schedules and resource limits. See `references/purpose-to-action.md`.

Use `contracts/skill-contracts.json` to review activation, inputs, outputs, recommendations, authority, stopping and consumers. Each skill has a matching Method contract section. Preserve evidence references, provenance, contradictions, uncertainty and scope when passing results to another skill. See `references/evidence-handoff-rules.md`.

Use the optional model formation and experiment design references when competing explanations need a discriminating test. Preserve evidence domains, proposed transfer, uncertainty and actual execution status. Use reasoning lenses, narrative summaries and exploratory unusual assumptions when requested by the user or included in an approved evaluation. Keep unfamiliar agents' motives as hypotheses supported by behavioral evidence. The optional method index is `contracts/v28-method-extensions.json`.

For long tasks or likely interruptions, use `references/resource-homeostasis.md`. Preserve source evidence, scope, contradictions and pending actions in checkpoints. Use current instructions and permissions when resuming. Consult `references/associative-evidence-recall.md` to reconstruct earlier claims. Use the consolidation and significant event references when durable lessons would help. Mark unavailable telemetry, sources or storage explicitly unresolved. See `contracts/v29-method-extensions.json` for the method mapping.
