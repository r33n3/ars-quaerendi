# Ars Quaerendi Agent Skills v2.5

Nine agent skills for investigating questions, planning work, assessing evidence, improving tools, reviewing performance and understanding negotiations or disagreements. Each skill contains instructions an agent can apply to the material and tools available in the session.

Use them with research, coding, project planning, operations, reporting, supplier review, learning and meeting note taking agents. People can also follow the methods directly. Supply the selected skill files and the task context to the agent. Automatic discovery depends on the host application's support for skills.

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

Expect findings with sources, competing explanations, unresolved questions and a justified next check. A research agent might compare conflicting reports, while a coding agent might investigate an unfamiliar failure.

### Purpose Planning

The agent connects possible goals to the user's purpose, compares priorities and builds a plan with milestones, dependencies and limits. It revises the plan when evidence changes and identifies decisions that need authorization.

Expect proposed goals, priorities, owners where agreed, missing ownership, review points and stopping conditions. A project agent can use it to replan after a delay or organize a broad request into achievable work.

### Toolcraft

The agent identifies a capability gap, checks existing tools and chooses whether to configure, combine, extend or build a helper. It uses limited experiments to test actual behavior and records the useful artifacts.

Expect a chosen approach, reasons, execution evidence, limits and remaining tests. A coding agent might produce a small parser for an unfamiliar data export or a helper for repeated calculations.

### Judgment

The agent reviews whether the available evidence supports a claim, interpretation or intended use. It examines completed checks, conflicting evidence, consequences and uncertainty.

Expect a recommendation with its supporting evidence, tested scope and missing checks. A release review agent can assess whether completed tests support the proposed use and identify remaining checks.

### Discovery

The agent investigates unexpected observations and patterns, including possible errors, missing context and coincidence. It develops explanations and simple checks that could distinguish them.

Expect a source linked observation, alternative explanations and a lead worth testing or preserving. An operations agent might find a pattern in timeout records, while a research agent might preserve an unexpected experimental result.

### Contribution

The agent identifies useful findings, methods, components and lessons from work, including incomplete or cancelled projects. It records the evidence of value and the limits of reuse.

Expect the project outcome and a separate account of verified contributions, attribution and reuse options. A knowledge agent can retain a verified method from a cancelled project and record whether another task successfully reused it.

### Reliability by Construction

The agent defines expected behavior and operating conditions, identifies relevant failures and checks recovery. It connects design choices with tests of repeated requests, interruptions, partial changes and other conditions that matter to the intended use.

Expect operating limits, failure checks, test results, coverage, remaining risks and readiness for a defined use. An automation agent can apply it to repeated requests, failed writes and recovery after an interruption.

### Performance and Metric Integrity

The agent checks how a measure is defined, which records are counted and how the result is calculated. It compares similar groups and periods, examines exclusions and checks related outcomes such as quality and repeated work.

Expect recalculated results, reported differences, source coverage, trend limits and options for improvement. A reporting agent can check a completion rate against task records or compare quality before and after a change.

### Institutional Intelligence

The agent reviews interests, commitments, claims, promises and outside pressure. It examines evidence, alternative interpretations, dependencies, costs and the authorization needed for proposed responses.

Expect a situation summary, supported observations, disputed claims, response options and follow up questions. A supplier review agent can check promised terms and alternatives. A meeting agent can examine commitments and disagreements, with tentative interpretations linked to specific comments.

## Example agents that can use the skills

These are examples of agent roles. Give an existing agent the selected skill files and the task material. Choose the methods that fit the question, access and authorization available.

| Agent role | Example task | Skills it might use | Expected result |
|---|---|---|---|
| Research agent | Investigate conflicting claims in supplied reports. | `inquiry`, `judgment` | Findings linked to sources, competing explanations and missing evidence. |
| Coding and debugging agent | Investigate an intermittent file import failure. | `inquiry`, `toolcraft`, `reliability-by-construction` | A tested explanation or clearly stated uncertainty, a useful fix and recovery checks. |
| Project planning agent | Replan work after a dependency slips. | `purpose-planning`, `judgment` | Priorities, milestones, dependencies and decisions needing authorization. |
| Operations and automation agent | Review a recurring job that sometimes runs twice. | `discovery`, `reliability-by-construction` | Evidence of the pattern, relevant failure checks and a recovery plan. |
| Reporting agent | Check a claimed improvement against the underlying records. | `performance-metric-integrity`, `judgment` | Recalculated measures, counting rules, differences and limits on the conclusion. |
| Supplier review agent | Compare an offer with promises about future price or capacity. | `institutional-intelligence`, `inquiry` | Verified terms, uncertain claims, alternatives and questions for negotiation. |
| Knowledge and learning agent | Preserve methods from completed work or run authorized research practice. | `contribution`, `inquiry`, `judgment` | Reusable lessons or a practice record with evidence and limits. |
| Meeting note taking agent | Identify comments, commitments and recurring concerns in supplied notes. | `institutional-intelligence`, `discovery`, `judgment` | Speaker linked findings, tentative interpretations and follow up questions. |

See [example tasks and requests for each agent](docs/agent-examples.md).

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

Use the scenarios in `tests/acceptance.md` to evaluate behavior against an unmodified agent with matched tools and budgets. Record observed results and overhead.

## Changes in v2.5

Added optional research challenges, explanation review and guided investigative practice to the existing skills. Added a generic file comparison challenge with separate evaluator notes, plus examples for several agent roles. The collection still contains nine skills. Practice results and learning effectiveness require observation and evaluation in the chosen host.

## Changes in v2.4

Expanded `institutional-intelligence` with guidance on promises, reliability of collaborators, shared sources, switching costs, accountability, adoption and decisions about further investment. Added three evaluation examples and eight negotiation acceptance scenarios. Clarified use in chats, work tasks and coding sessions, with tool availability guidance in every skill. The collection still contains nine skills.

## Changes in v2.3

Added `institutional-intelligence`, detailed guidance and examples. These cover negotiations, incentives, disputed claims, possible risks, economic promises and decisions made under outside pressure. The user and host environment control changes to goals, access and commitments.

## Changes in v2.2

Added `performance-metric-integrity`, a report schema, examples using invented records and guidance in `docs/integration-flow.md`. These cover measure definitions, calculation checks, trends, related outcomes and decisions about improvements.

## Changes in v2.1

Added `reliability-by-construction`, a reliability promotion example and guidance in `references/factory-and-reliability.md`. These cover prototype testing, recovery, deployment readiness and evidence requirements for a defined use.
