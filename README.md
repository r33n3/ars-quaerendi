# Ars Quaerendi Agent Meta Skills v3.0

A package of nine agent meta skills for investigating questions, planning work, assessing evidence, improving tools, reviewing performance and understanding negotiations or disagreements. An agent or several agents can use each skill to carry out a defined part of a task using the material and tools available in the session.

Apply them to research, coding, project planning, operations, reporting, supplier review, learning and meeting notes. One agent can use several skills during a task. When collaboration is authorized, several agents can use selected skills for different parts of the work. People can also follow the methods directly. Supply the skill files and task context through the host, whose features determine automatic discovery.

## Meta skills and regular task skills

A **meta skill** guides how an agent approaches work. It helps the agent choose a method, examine evidence, handle uncertainty, assess results or carry learning into another task.

A **regular task skill** describes how to perform a particular operation or produce a defined result. Examples include extracting fields from a document, calculating a report, running a test suite or exporting meeting notes.

| Aspect | Meta skill | Regular task skill |
|---|---|---|
| Main purpose | Guide the choice of methods, checks and conclusions. | Perform a defined operation or produce an artifact. |
| Typical result | A reasoned plan, assessment, interpretation or reusable lesson. | Extracted data, a completed calculation, a file or test results. |
| Reuse | Applies the method across different tasks and settings. | Applies a procedure to a particular task or tool. |
| Example | Judgment assesses whether completed tests support a release. | A test execution skill runs the specified tests and records their results. |

An agent can use both together. For example, a task skill captures meeting comments, while Institutional Intelligence examines commitments and competing claims. A data calculation skill produces a completion rate, while Performance and Metric Integrity checks its definition and interpretation.

The categories describe a skill's main role. Both kinds can be reused across projects. Some skills combine both kinds of work, and both can produce concrete artifacts. Toolcraft, for example, guides a capability decision and may also build a helper. Here, meta skill is a descriptive category within the existing skill format. Select each method according to the task and available evidence.

Inquiry, Purpose Planning, Judgment, Discovery and Contribution provide general meta skills. Toolcraft, Reliability by Construction, Performance and Metric Integrity, and Institutional Intelligence focus those methods on particular areas of work.

See [how meta skills work with task skills](docs/meta-skills.md) for examples and a guide to reviewing the distinction.

## Method contracts and evidence handoffs

Each of the nine meta skills declares when it is useful, its minimum inputs and helpful context, evidence and records it produces, recommendations it can make, authority boundaries, stopping conditions, possible consumers and failure handling. The contract also records outcome states and reasons to reopen an assessment.

The [contract registry](contracts/skill-contracts.json) is the source for matching sections in each skill file. See [method contracts](docs/method-contracts.md) for the field definitions and update process.

Shared evidence records separate provenance, the relationship to a claim, uncertainty and tested scope. Handoffs carry stable identifiers, record references, content hashes and scope and uncertainty snapshots. Agents preserve earlier findings and limits when another skill uses the result.

See the [complete handoff walkthroughs](examples/complete-handoffs/README.md) for research and reuse, offer review and planning, investigation of an unexpected pattern, and a proposed experiment. The walkthroughs use invented source records and leave their verification limits explicit. The [handoff rules](references/evidence-handoff-rules.md) describe the checks and judgment requirements.

## Optional models, experiments and evidence boundaries

Agents can use Inquiry to form competing explanatory models, Toolcraft to design discriminating tests and Judgment to assess where the evidence applies. These methods help with unfamiliar software behavior, scientific questions and other tasks where several explanations remain possible. Select them when they help answer the current question.

See [model formation](references/scientific-model-formation.md), [experimental environments](references/experimental-environment-synthesis.md) and [evidence boundaries](references/epistemic-boundaries.md). The [conversion example](examples/frontier-model-handoff.md) keeps a proposed test separate from its documentary input evidence and unresolved causal claim.

[Reasoning lenses and narrative summaries](references/archetypal-reasoning.md) are experimental options requiring a user request or an approved evaluation that includes them. Their benefit remains unmeasured. The labels describe reasoning and presentation functions. One agent can use them within the current task and permissions. The [method index](contracts/v28-method-extensions.json) maps these optional methods to the existing skills and references.

The package still contains nine meta skills. These additions provide methods and record conventions. The user and host supply execution, tools and authorization.

## Optional recall and continuity methods

Agents can use [resource and continuity review](references/resource-homeostasis.md) to prepare for interruptions, [evidence recall](references/associative-evidence-recall.md) to reconstruct earlier findings, and [knowledge consolidation](references/memory-consolidation-reinvestment.md) to retain useful methods. [Significant event records](references/significance-weighted-memory.md) preserve consequential lessons with their evidence and limits. Significance, reliability, relevance and recommended responses remain separate.

These methods use the storage, search and telemetry available in the host. People can also supply retained records in a chat. A checkpoint records historical context; resumed work follows current instructions, permissions and actual task state. The package still contains nine meta skills. See the [method mapping](contracts/v29-method-extensions.json) and [memory record guide](docs/memory-records.md).

## Optional adaptation and recovery methods

Agents can use [method comparison](references/adaptive-variation-selection.md) when changed conditions or repeated failures justify a limited test of alternatives. Record the baseline, predictions, acceptance criteria, resource limit, results and rejected approaches. [Diversity and recovery](references/evolutionary-diversity-and-recovery.md) helps assess shared dependencies and distinguish restored service from better outcomes.

The [adaptation example](examples/adaptive-peer-recovery.json) keeps both variants proposed and the selection inconclusive. Its source is explicitly invented. The [record schema](schemas/adaptation-record.schema.json) and validator check candidate identity, evidence references, hashes, scope, execution prerequisites and selection consistency. Actual measurement validity and benefits remain questions for the method and host evaluation.

These additions remain optional methods within the existing nine meta skills. See the [method mapping](contracts/v30-method-extensions.json). The user and host control purpose, execution, deployment and resource limits.

## Skill names and selection

The titles describe each skill's role. The identifiers match the folder names and the `name` fields in the skill files. Use an identifier when selecting or referring to a skill.

| Meta skill | Identifier | Choose it for |
|---|---|---|
| [Inquiry: Research and Source Checking](skills/inquiry/SKILL.md) | `inquiry` | Investigating an open question, disputed fact or uncertain explanation. |
| [Purpose Planning: Goals and Work Plans](skills/purpose-planning/SKILL.md) | `purpose-planning` | Assessing opportunities, justifying goals, planning work and reviewing further investment. |
| [Toolcraft: Finding and Building Tools](skills/toolcraft/SKILL.md) | `toolcraft` | Finding a practical way to supply a missing capability. |
| [Judgment: Evidence and Readiness Review](skills/judgment/SKILL.md) | `judgment` | Assessing a conclusion, proposed action or interpretation. |
| [Discovery: Unexpected Findings and New Leads](skills/discovery/SKILL.md) | `discovery` | Investigating surprising observations and recurring patterns. |
| [Contribution: Useful Results and Lessons](skills/contribution/SKILL.md) | `contribution` | Preserving useful work, lessons, decisions and open questions. |
| [Reliability by Construction: Design, Testing and Recovery](skills/reliability-by-construction/SKILL.md) | `reliability-by-construction` | Preparing a prototype for repeated use or addressing recurring failures. |
| [Performance and Metric Integrity: Measures and Report Checks](skills/performance-metric-integrity/SKILL.md) | `performance-metric-integrity` | Checking reported numbers, trends and proposed improvements. |
| [Institutional Intelligence: Negotiations, Incentives and Claims](skills/institutional-intelligence/SKILL.md) | `institutional-intelligence` | Reviewing offers, promises, competing interests and disputed comments. |

## What each skill produces

### Inquiry

Agents can use `inquiry` to research a question, trace claims to original sources and consider explanations that fit the evidence. The method groups repeated claims from one source and identifies checks that could change the conclusion.

Expect findings with sources, competing explanations, unresolved questions and a justified next check. For example, agents can compare conflicting research reports or investigate an unfamiliar code failure.

### Purpose Planning

Agents can use `purpose-planning` to connect goals to the user's purpose, compare priorities and build a plan with milestones, dependencies and limits. The method supports revising plans as evidence changes and identifying decisions that need authorization.

It also compares new opportunities with continuing current goals, identifies what is blocking progress and assesses whether a capability improvement is justified. See the [goal review examples](examples/purpose-to-action.md) for a proposed investigation and a decision to continue existing work.

Expect proposed goals, priorities, owners where agreed, missing ownership, review points and stopping conditions. For example, agents can replan after a delay or organize a broad request into achievable work.

### Toolcraft

Agents can use `toolcraft` to identify a capability gap, check existing tools and choose whether to configure, combine, extend or build a helper. The method uses limited experiments to test behavior and records useful artifacts.

Expect a chosen approach, reasons, execution evidence, limits and remaining tests. For example, agents can produce a small parser for an unfamiliar data export or a helper for repeated calculations.

### Judgment

Agents can use `judgment` to assess whether available evidence supports a claim, interpretation or intended use. The method examines completed checks, conflicting evidence, consequences and uncertainty.

Expect a recommendation with its supporting evidence, tested scope and missing checks. For example, agents can assess whether completed release tests support the proposed use and identify remaining checks.

### Discovery

Agents can use `discovery` to investigate unexpected observations and patterns, including possible errors, missing context and coincidence. The method develops explanations and simple checks that could distinguish them.

Expect a source linked observation, alternative explanations and a lead worth testing or preserving. For example, agents can find a pattern in timeout records or preserve an unexpected experimental result.

### Contribution

Agents can use `contribution` to identify useful findings, methods, components and lessons from work, including incomplete or cancelled projects. The method records evidence of value and limits on reuse.

Expect the project outcome and a separate account of verified contributions, attribution and reuse options. For example, agents can retain a verified method from a cancelled project and record whether another task successfully reused it.

### Reliability by Construction

Agents can use `reliability-by-construction` to define expected behavior and operating conditions, identify relevant failures and check recovery. The method connects design choices with tests of repeated requests, interruptions, partial changes and other conditions that matter to the intended use.

Expect operating limits, failure checks, test results, coverage, remaining risks and readiness for a defined use. For example, agents can assess repeated requests, failed writes and recovery after an interruption.

### Performance and Metric Integrity

Agents can use `performance-metric-integrity` to check how a measure is defined, which records are counted and how the result is calculated. The method compares similar groups and periods, examines exclusions and checks related outcomes such as quality and repeated work.

Expect recalculated results, reported differences, source coverage, trend limits and options for improvement. For example, agents can check a completion rate against task records or compare quality before and after a change.

### Institutional Intelligence

Agents can use `institutional-intelligence` to review interests, commitments, claims, promises and outside pressure. The method examines evidence, alternative interpretations, dependencies, costs and the authorization needed for proposed responses.

Expect a situation summary, supported observations, disputed claims, response options and follow up questions. For example, agents can check supplier promises and alternatives or examine meeting commitments and disagreements. Keep tentative interpretations linked to specific evidence.

## Examples of what agents can use the skills to do

These examples describe work that one or more agents can carry out with the skills. Supply the selected skill files and task material. Choose methods that fit the question, access and authorization available. For shared work, record the sources, completed checks and open questions for each part.

| Context | What agents can use the skills to do | Useful skills | Expected result |
|---|---|---|---|
| Research | Investigate conflicting claims in supplied reports. | `inquiry`, `judgment` | Findings linked to sources, competing explanations and missing evidence. |
| Coding and debugging | Investigate an intermittent file import failure. | `inquiry`, `toolcraft`, `reliability-by-construction` | A tested explanation or clearly stated uncertainty, a useful fix and recovery checks. |
| Project planning | Replan work after a dependency slips. | `purpose-planning`, `judgment` | Priorities, milestones, dependencies and decisions needing authorization. |
| Operations and automation | Review a recurring job that sometimes runs twice. | `discovery`, `reliability-by-construction` | Evidence of the pattern, relevant failure checks and a recovery plan. |
| Reporting | Check a claimed improvement against the underlying records. | `performance-metric-integrity`, `judgment` | Recalculated measures, counting rules, differences and limits on the conclusion. |
| Supplier review | Compare an offer with promises about future price or capacity. | `institutional-intelligence`, `inquiry` | Verified terms, uncertain claims, alternatives and questions for negotiation. |
| Knowledge and learning | Preserve methods from completed work or run authorized research practice. | `contribution`, `inquiry`, `judgment` | Reusable lessons or a practice record with evidence and limits. |
| Meeting notes | Identify comments, commitments and recurring concerns in supplied notes. | `institutional-intelligence`, `discovery`, `judgment` | Speaker linked findings, tentative interpretations and follow up questions. |

See [example tasks and requests](docs/agent-examples.md).

For the meeting example, supply speaker labels, timestamps or note references and relevant earlier records. Link observations to comments and keep interpretations of traits or motives tentative. See the [meeting review guide](docs/meeting-notes.md) and [worked example](examples/meeting-review.md).

## Chats, work and coding sessions

* In a chat, attach or paste the selected `SKILL.md` and any references needed for the task. State the question and ask the assistant to apply the method.
* For work tasks, supply the relevant reports, notes or project context. Ask the agent for the decisions or findings you need.
* In a coding session, make the selected files available to the agent alongside the code, records and tests relevant to the task.
* For personal use, follow the instructions directly and keep your own notes and evidence.

Choose the skills that fit the work. The person or host agent controls goals, execution, permissions and collaboration. Each skill explains how to work with limited tool access and report checks that remain unverified.

## Setup and use

1. Choose a skill from the table and read its instructions.
2. Give the agent the skill file, task context and the result you want.
3. Include relevant references when the task calls for detailed methods.
4. Ask the agent to state its evidence, assumptions, completed checks and open questions.
5. Keep findings and decisions with the source material so they can be reviewed later.

For a host that discovers skill folders, copy the selected folders to its configured skills directory. Preserve access to shared references and check relative paths after copying individual folders. Provide the skill text through the host's supported instruction or context mechanism. Automatic delivery of records and file loading depend on that host's features.

The optional `AGENTS.md` file describes skill selection for hosts that use repository instructions. Merge it with existing instructions as appropriate. See [how the skills fit together](docs/integration-flow.md) for examples of combining methods.

## Evidence and judgment

Evidence labels:

* D: documented in a source.
* O: directly observed.
* R: independently reproduced.
* H: hypothesis.
* U: unknown.
* X: contradicted.

Judgment levels:

* J0: exploratory.
* J1: plausible.
* J2: supported.
* J3: verified within the tested scope.
* J4: qualified for a defined use.

Record the scope and supporting evidence with each assessment. Authorization remains with the user and host environment.

## Validation

The Python validator is an optional check for people maintaining the package. The `jsonschema` library enables full schema checks. Reading and applying the skill instructions uses the text itself.

Run `python3 tests/validate.py` to check package structure, JSON syntax and schema compliance when the `jsonschema` library is available.

Run `python3 tests/test_goal_proposals.py` for the goal record checks. These cover proposed goals, unchanged goals, evidence references, resource limits and authorization fields.

Run `python3 tests/validate_v27.py` to check contract synchronization, shared evidence schemas and bundled handoff records. Run `python3 tests/test_interoperability.py` for altered records, missing evidence, scope changes and unsupported verification upgrades. Full schema validation uses the optional `jsonschema` library.

Run `python3 tests/test_experimental_methods.py` for evidence domains and optional method checks. The scenarios in `tests/v28-experimental-scenarios.md` cover host behavior for the new methods.

Run `python3 tests/validate_v29.py` for the memory examples and `python3 tests/test_memory_records.py` for altered checkpoints, missing sources and unsupported reliability claims. The scenarios in `tests/v29-memory-scenarios.md` describe host behavior to evaluate.

Run `python3 tests/validate_v30.py` for adaptation records and `python3 tests/test_adaptation_records.py` for valid comparisons and invalid selections. The scenarios in `tests/v30-evolution-scenarios.md` describe host behavior to evaluate.

Use the scenarios in `tests/acceptance.md` to evaluate behavior against an unmodified agent with matched tools and budgets. Record observed results and overhead.

## Changes in v3.0

Added bounded comparison of alternative methods and guidance on diversity, recovery and cumulative improvement. Added an adaptation record, a proposed recovery example and checks for unsupported selections, missing evidence and inconsistent records. Preserved the reviewed contracts, evidence domains, memory methods, examples and earlier tests. The package still contains nine meta skills.

## Changes in v2.9

Added optional resource review, evidence recall, knowledge consolidation and significant event records within the existing skills. Added checkpoint and memory schemas, linked illustrative examples and validation of source references, hashes, scope and reliability requirements. Current authorization and execution state are reviewed on resumption. Earlier evidence records remain unchanged.

## Changes in v2.8

Added optional model formation, experiment design, evidence boundary review and requested reasoning lenses or narrative summaries. Added a fourth illustrative walkthrough that keeps a proposed experiment separate from observed evidence. Evidence and handoff schema version 1.1 records the evidence domain and intended decision domain. Existing version 1.0 records remain readable; verification requires an explicit domain. Added checks for domain transfer and optional method references.

## Changes in v2.7

Added contracts for all nine meta skills, a shared evidence schema and a handoff schema. Added three complete illustrative walkthroughs with seven handoffs. The checks now compare contract text with the JSON registry and verify references, hashes, scope, uncertainty, consumers, authority context and judgment requirements. The earlier research record schema remains available for existing records.

## Changes in v2.6

Expanded `purpose-planning` to assess opportunities, justify goals, investigate capability gaps and review further investment. Added a goal proposal schema, examples of proposing a goal and continuing existing work, and acceptance scenarios. Proposals preserve the user's purpose, current authorization and resource limits. The collection still contains nine meta skills.

## Changes in v2.5

Added optional research challenges, explanation review and guided investigative practice to the existing skills. Added a generic file comparison challenge with separate evaluator notes, plus task examples for one or more agents. The collection still contains nine skills. Practice results and learning effectiveness require observation and evaluation in the chosen host.

## Changes in v2.4

Expanded `institutional-intelligence` with guidance on promises, reliability of collaborators, shared sources, switching costs, accountability, adoption and decisions about further investment. Added three evaluation examples and eight negotiation acceptance scenarios. Clarified use in chats, work tasks and coding sessions, with tool availability guidance in every skill. The collection still contains nine skills.

## Changes in v2.3

Added `institutional-intelligence`, detailed guidance and examples. These cover negotiations, incentives, disputed claims, possible risks, economic promises and decisions made under outside pressure. The user and host environment control changes to goals, access and commitments.

## Changes in v2.2

Added `performance-metric-integrity`, a report schema, examples using invented records and guidance in `docs/integration-flow.md`. These cover measure definitions, calculation checks, trends, related outcomes and decisions about improvements.

## Changes in v2.1

Added `reliability-by-construction`, a reliability promotion example and guidance in `references/factory-and-reliability.md`. These cover prototype testing, recovery, deployment readiness and evidence requirements for a defined use.
