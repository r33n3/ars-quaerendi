# Ars Quaerendi Unified v2.3

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

Run `python3 tests/validate.py` to check package structure, JSON syntax and schema compliance when the `jsonschema` library is available.

Use the scenarios in `tests/acceptance.md` to evaluate behavior against an unmodified agent with matched tools and budgets. Record observed results and overhead.

## Changes in v2.3

Added `institutional-intelligence`, detailed guidance and examples. These cover negotiations, incentives, disputed claims, possible risks, economic promises and decisions made under outside pressure. The user and host environment control changes to goals, access and commitments.

## Changes in v2.2

Added `performance-metric-integrity`, a report schema, examples using invented records and guidance in `docs/integration-flow.md`. These cover measure definitions, calculation checks, trends, related outcomes and decisions about improvements.

## Changes in v2.1

Added `reliability-by-construction`, a reliability promotion example and guidance in `references/factory-and-reliability.md`. These cover prototype testing, recovery, deployment readiness and evidence requirements for a defined use.
