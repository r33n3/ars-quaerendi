# Ars Quaerendi Agent Meta Skills v3.0

Nine agent meta skills for investigating questions, planning work, assessing evidence, improving tools and preserving useful results. Agents can apply them across research, coding, operations, reporting, supplier review, learning and meetings. People can also follow the methods directly.

A meta skill guides how an agent chooses a method, evaluates evidence or reaches a decision. A regular task skill supplies a procedure for a particular job, such as extracting document fields, executing a test or exporting meeting notes. Agents can use both together. Some skills combine these roles. See [meta skills and task skills](docs/meta-skills.md).

## Choose a skill

Agents can use each skill for the work below. The identifiers match the skill folders and their `name` fields.

| Meta skill | Identifier | Use and expected result |
|---|---|---|
| [Inquiry: Research and Source Checking](skills/inquiry/SKILL.md) | `inquiry` | Investigate an open question, trace original sources and compare explanations. Return source linked findings, uncertainty and a useful next check. |
| [Purpose Planning: Goals and Work Plans](skills/purpose-planning/SKILL.md) | `purpose-planning` | Connect goals to the user's purpose, assess opportunities and plan work. Return justified proposals, alternatives, resource limits and stopping conditions. |
| [Toolcraft: Finding and Building Tools](skills/toolcraft/SKILL.md) | `toolcraft` | Address a missing capability through existing tools or a limited helper. Return the chosen approach, execution evidence, limits and remaining checks. |
| [Judgment: Evidence and Readiness Review](skills/judgment/SKILL.md) | `judgment` | Assess whether evidence supports a claim, decision or intended use. Return a scoped recommendation, supporting evidence and unresolved checks. |
| [Discovery: Unexpected Findings and New Leads](skills/discovery/SKILL.md) | `discovery` | Investigate surprising observations and recurring patterns. Return alternative explanations, source linked leads and ways to test them. |
| [Contribution: Useful Results and Lessons](skills/contribution/SKILL.md) | `contribution` | Preserve useful findings, methods and lessons from completed or partial work. Return evidence of value, attribution, reuse conditions and the parent outcome separately. |
| [Reliability by Construction: Design, Testing and Recovery](skills/reliability-by-construction/SKILL.md) | `reliability-by-construction` | Prepare a prototype for repeated use or examine recurring failures. Return operating limits, recovery checks, results and readiness for a defined use. |
| [Performance and Metric Integrity: Measures and Report Checks](skills/performance-metric-integrity/SKILL.md) | `performance-metric-integrity` | Check reported measures and proposed improvements. Return definitions, recalculated results, coverage, related outcomes and interpretation limits. |
| [Institutional Intelligence: Negotiations, Incentives and Claims](skills/institutional-intelligence/SKILL.md) | `institutional-intelligence` | Examine offers, promises, commitments and disputed comments. Return supported observations, alternative interpretations, response options and follow up questions. |

## Use with an agent or in a chat

1. State the purpose, task, relevant context and result you need.
2. Supply the selected `SKILL.md` files and any references needed for that task.
3. Let the agent use available task skills and tools within existing permissions.
4. Ask for supporting evidence, completed checks, uncertainty and a justified next step.

One agent can apply several methods. When collaboration is authorized, several agents can contribute separate investigations or checks and exchange findings with their limits intact. The user and host control purpose, tools, execution, resources and commitments.

For hosts that discover skill folders, use the host's configured skills location. Keep shared references available and preserve relative paths when copying files. In a chat, attach or paste the selected instructions and relevant source material. The optional [AGENTS.md](AGENTS.md) provides repository integration guidance.

## Examples

| Context | What agents can use the skills to do | Useful skills |
|---|---|---|
| Research | Compare conflicting reports and identify a check that could settle the disagreement. | `inquiry`, `judgment` |
| Coding | Investigate an intermittent import failure and assess the fix and recovery behavior. | `inquiry`, `toolcraft`, `reliability-by-construction` |
| Planning | Compare opportunities or revise work after a dependency changes. | `purpose-planning`, `judgment` |
| Operations | Examine a recurring job that sometimes runs twice. | `discovery`, `reliability-by-construction` |
| Reporting | Check a claimed improvement against underlying records. | `performance-metric-integrity`, `judgment` |
| Supplier review | Compare an offer with promises about future price or capacity. | `institutional-intelligence`, `inquiry` |
| Learning | Preserve useful methods and assess their applicability to another task. | `contribution`, `inquiry` |
| Meeting notes | Identify commitments, disputed comments and recurring concerns. | `institutional-intelligence`, `discovery`, `judgment` |

See [example tasks and requests](docs/agent-examples.md) and [how the skills fit together](docs/integration-flow.md). The [meeting guide](docs/meeting-notes.md) and [worked review](examples/meeting-review.md) show how to link interpretations to speaker comments while preserving uncertainty about traits or motives.

## Contracts and records

Each skill declares activation, inputs, outputs, recommendations, authority, stopping conditions, consumers and failure handling. Its Method contract section matches the [contract registry](contracts/skill-contracts.json). See [field definitions](docs/method-contracts.md).

Shared [schemas](schemas/evidence-record.schema.json) describe evidence and related records. Preserve source identity, provenance, content hashes, tested scope, contradictions and uncertainty when passing findings between skills. See the [handoff rules](references/evidence-handoff-rules.md) and [complete worked examples](examples/complete-handoffs/README.md).

Use D for documented, O for directly observed, R for independently reproduced, H for hypothesis, U for unknown and X for contradicted. Judgment levels run from J0 exploratory, through J1 plausible and J2 supported, to J3 verified within tested scope and J4 qualified for a defined use. Keep supporting evidence and limits with each assessment.

## Optional methods

Select these methods when they help answer the current question:

* [Model formation](references/scientific-model-formation.md), [experimental environments](references/experimental-environment-synthesis.md) and [evidence boundaries](references/epistemic-boundaries.md) help compare explanations and design useful tests.
* [Resource and continuity review](references/resource-homeostasis.md), [evidence recall](references/associative-evidence-recall.md) and [knowledge consolidation](references/memory-consolidation-reinvestment.md) help preserve useful work across tasks and interruptions. See [memory records](docs/memory-records.md).
* [Significant event records](references/significance-weighted-memory.md) keep importance separate from reliability, relevance and recommended responses.
* [Method comparison](references/adaptive-variation-selection.md) and [diversity and recovery](references/evolutionary-diversity-and-recovery.md) help test alternatives and assess changed conditions. The [adaptation example](examples/adaptive-peer-recovery.json) keeps unperformed variants explicitly proposed.
* [Reasoning lenses and narrative summaries](references/archetypal-reasoning.md) are experimental methods requiring a user request or an approved evaluation that includes them. Their benefit remains unmeasured.

The package supplies instructions, references, contracts, record schemas and examples. The host supplies storage, search, telemetry and execution capabilities. Applying the skills requires access to the relevant text and task material.
