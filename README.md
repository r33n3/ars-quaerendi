# Ars Quaerendi Unified v2.4

Nine reusable skills for research, planning, tools, reliability, performance measures and negotiations. People can follow the instructions directly or use them with a compatible AI agent. Each skill can be used independently.

| Skill | Purpose |
|---|---|
| inquiry | Research unfamiliar questions and test explanations. |
| `purpose-planning` | Choose goals and plan work within the user's stated purpose. |
| toolcraft | Find, adapt or build a tool for a specific task. |
| judgment | Assess whether evidence supports an intended use. |
| discovery | Investigate unexpected observations and promising leads. |
| contribution | Preserve useful results, including work from incomplete projects. |
| `reliability-by-construction` | Improve correctness, repeatability, robustness and recovery. |
| `performance-metric-integrity` | Check performance reports and evaluate proposed improvements. |
| `institutional-intelligence` | Assess incentives, negotiate terms and investigate disputed claims. |

## Use

Choose the skill that fits the task. Combine skills when the work calls for several methods. The person or host agent controls goals, execution, permissions and collaboration.

Record the project outcome, verified milestones, findings and reusable contributions separately. Keep unexpected leads available for later investigation. Share material with collaborators when authorized.

## Chats, work and coding sessions

* In a chat, attach or paste the selected `SKILL.md` and any references needed for the task. State the question and ask the assistant to apply the method.
* For work tasks, use the methods to research questions, review reports, plan projects, compare proposals or prepare negotiations.
* In a coding session, make the selected files available to the agent. Use them to investigate behavior, assess evidence, improve tools or check reliability.
* For personal use, follow the instructions directly and keep your own notes and evidence.

An agent can apply the methods when the host supplies the text as context. Automatic discovery, file access and tool use depend on the host. Searches, tests and external actions require the relevant tools, access and permissions. State what was actually checked and what remains uncertain.

## Install

For manual use, read `skills/<name>/SKILL.md` and consult `references/` as needed.

For an agent host, copy the skill folders to its configured skills directory. Keep the full package available for shared references. Check reference paths when installing individual skills. Merge the optional `AGENTS.md` guidance with your existing instructions. Remove older installed versions when replacing a skill.

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
