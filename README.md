# Ars Quaerendi Agent Skills v2.4

Nine agent skills for investigating questions, planning work, assessing evidence, improving tools, reviewing performance and understanding negotiations or disagreements. Each skill contains instructions an agent can apply to the material and tools available in the session.

Use them with a meeting note taking agent, a work assistant, a research agent or a coding agent. People can also follow the methods directly. Supply the selected skill files and the task context to the agent. Automatic discovery depends on the host application's support for skills.

## Skill names and selection

The titles describe each skill's role. The identifiers match the folder names and the `name` fields in the skill files. Use an identifier when selecting or referring to a skill.

| Agent skill | Identifier | Choose it for |
|---|---|---|
| [Inquiry: Research and Source Checking](skills/inquiry/SKILL.md) | `inquiry` | Investigating an open question, disputed fact or uncertain explanation. |
| [Purpose Planning: Goals and Work Plans](skills/purpose-planning/SKILL.md) | `purpose-planning` | Choosing goals, setting priorities and planning follow up. |
| [Toolcraft: Finding and Building Tools](skills/toolcraft/SKILL.md) | `toolcraft` | Finding a practical way to supply a missing capability. |
| [Judgment: Evidence and Readiness Review](skills/judgment/SKILL.md) | `judgment` | Assessing a conclusion, proposed action or interpretation. |
| [Discovery: Unexpected Findings and New Leads](skills/discovery/SKILL.md) | `discovery` | Investigating surprising observations and recurring patterns. |
| [Contribution: Useful Results and Lessons](skills/contribution/SKILL.md) | `contribution` | Preserving useful work, lessons, decisions and open questions. |
| [Reliability by Construction: Design, Testing and Recovery](skills/reliability-by-construction/SKILL.md) | `reliability-by-construction` | Preparing a prototype for repeated use or addressing recurring failures. |
| [Performance and Metric Integrity: Measures and Report Checks](skills/performance-metric-integrity/SKILL.md) | `performance-metric-integrity` | Checking reported numbers, trends and proposed improvements. |
| [Institutional Intelligence: Negotiations, Incentives and Claims](skills/institutional-intelligence/SKILL.md) | `institutional-intelligence` | Reviewing offers, promises, competing interests and disputed comments. |

## What each skill produces

### Inquiry

The agent researches a question, traces claims to original sources and considers explanations that could account for the evidence. It groups repeated claims from one source and identifies checks that could change the conclusion.

Expect findings with sources, competing explanations, unresolved questions and a justified next check. For a meeting, this might mean investigating a participant's claim about costs or delivery limits.

### Purpose Planning

The agent connects possible goals to the user's purpose, compares priorities and builds a plan with milestones, dependencies and limits. It revises the plan when evidence changes and identifies decisions that need authorization.

Expect proposed goals, priorities, owners where agreed, missing ownership, review points and stopping conditions. For a meeting, this can turn decisions into proposed follow up while preserving what participants actually agreed.

### Toolcraft

The agent identifies a capability gap, checks existing tools and chooses whether to configure, combine, extend or build a helper. It uses limited experiments to test actual behavior and records the useful artifacts.

Expect a chosen approach, reasons, execution evidence, limits and remaining tests. In a coding session, this might produce a small parser for exported meeting files.

### Judgment

The agent reviews whether the available evidence supports a claim, interpretation or intended use. It examines completed checks, conflicting evidence, consequences and uncertainty.

Expect a recommendation with its supporting evidence, tested scope and missing checks. For a meeting, this can establish whether a comment supports an action assignment or whether an interpretation needs clarification.

### Discovery

The agent investigates unexpected observations and patterns, including possible errors, missing context and coincidence. It develops explanations and simple checks that could distinguish them.

Expect a source linked observation, alternative explanations and a lead worth testing or preserving. Across meetings, this can identify recurring concerns, changes in position or questions that repeatedly remain unresolved.

### Contribution

The agent identifies useful findings, methods, components and lessons from work, including incomplete or cancelled projects. It records the evidence of value and the limits of reuse.

Expect the project outcome and a separate account of verified contributions, attribution and reuse options. In meeting work, this can preserve decisions, supported insights and useful proposals alongside unresolved issues.

### Reliability by Construction

The agent defines expected behavior and operating conditions, identifies relevant failures and checks recovery. It connects design choices with tests of repeated requests, interruptions, partial changes and other conditions that matter to the intended use.

Expect operating limits, failure checks, test results, coverage, remaining risks and readiness for a defined use. A coding agent could apply it before scheduling a helper to run on every meeting export.

### Performance and Metric Integrity

The agent checks how a measure is defined, which records are counted and how the result is calculated. It compares similar groups and periods, examines exclusions and checks related outcomes such as quality and repeated work.

Expect recalculated results, reported differences, source coverage, trend limits and options for improvement. For a meeting, this can check a completion rate against the supplied task records.

### Institutional Intelligence

The agent reviews interests, commitments, claims, promises and outside pressure. It examines evidence, alternative interpretations, dependencies, costs and the authorization needed for proposed responses.

Expect a situation summary, supported observations, disputed claims, response options and follow up questions. A meeting note taking agent can use it to examine who offered what, where participants disagreed and how priorities changed. Interpretations of traits or motives stay tentative and linked to specific comments.

## Meeting note taking agents

Supply the transcript or notes, speaker labels, available timestamps, relevant earlier notes and the questions you want the agent to examine. Choose skills according to those questions.

* Use `institutional-intelligence` for comments, commitments, disagreements, competing interests and communication behaviors.
* Use `discovery` for repeated concerns, changing positions and unexpected patterns.
* Use `judgment` to check whether an interpretation is supported by the record.
* Use `purpose-planning` for proposed actions, priorities and unresolved ownership.
* Use `contribution` to preserve decisions, useful findings and open issues.
* Use `performance-metric-integrity` when participants discuss scores, completion rates or other reported measures.

Ask for speaker attribution, timestamps or note references, exact wording where available, observations, tentative interpretations, commitments and follow up questions. Describe recurring behavior in the context of the available meetings. Keep personal conclusions tied to the examples that support them.

Example request:

> Apply the selected agent skills to these meeting notes. Identify important comments, commitments, disagreements and recurring communication behaviors. Link each finding to a speaker and source location. Separate recorded observations from tentative interpretations and list questions that would clarify uncertain points.

See the [meeting review guide](docs/meeting-notes.md) and [worked example](examples/meeting-review.md).

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

For a host that discovers skill folders, copy the selected folders to its configured skills directory. Preserve access to shared references and check relative paths after copying individual folders. For a note taking agent, provide the skill text through its supported instruction or context mechanism. Automatic transcript delivery and file loading depend on that host's features.

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

Use the scenarios in `tests/acceptance.md` to evaluate behavior against an unmodified agent with matched tools and budgets. Record observed results and overhead.

## Changes in v2.4

Expanded `institutional-intelligence` with guidance on promises, reliability of collaborators, shared sources, switching costs, accountability, adoption and decisions about further investment. Added three evaluation examples and eight negotiation acceptance scenarios. Clarified use in chats, work tasks and coding sessions, with tool availability guidance in every skill. The collection still contains nine skills.

## Changes in v2.3

Added `institutional-intelligence`, detailed guidance and examples. These cover negotiations, incentives, disputed claims, possible risks, economic promises and decisions made under outside pressure. The user and host environment control changes to goals, access and commitments.

## Changes in v2.2

Added `performance-metric-integrity`, a report schema, examples using invented records and guidance in `docs/integration-flow.md`. These cover measure definitions, calculation checks, trends, related outcomes and decisions about improvements.

## Changes in v2.1

Added `reliability-by-construction`, a reliability promotion example and guidance in `references/factory-and-reliability.md`. These cover prototype testing, recovery, deployment readiness and evidence requirements for a defined use.
