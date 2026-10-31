# Meta skills and regular task skills

Ars Quaerendi is a package of agent meta skills. The term describes methods that guide how an agent approaches and evaluates work across tasks. The files use the existing skill format and identifiers.

## What each kind of skill provides

A regular task skill gives an agent a procedure for a defined job, such as extracting fields from a document, producing a chart, exporting notes or executing tests. Its result can be inspected as a completed operation, record or artifact.

A meta skill helps the agent decide which approach to use, what evidence to gather, how to interpret the result and whether further work is justified. Its result may be a plan, an assessment, a reasoned conclusion or a reusable lesson. Meta skills can also lead to concrete artifacts and implementation work.

Both kinds can contain reasoning, use tools and be reused across projects. A skill can combine both roles. Classify it according to its main contribution to the work.

## The methods in this package

| Meta skill | What it guides |
|---|---|
| `inquiry` | How to investigate a question and distinguish competing explanations. |
| `purpose-planning` | How to choose goals and organize work around the user's purpose. |
| `judgment` | What a result supports and whether the evidence is sufficient for an intended use. |
| `discovery` | How to investigate unexpected observations and preserve promising leads. |
| `contribution` | What useful results to retain, how to support their value and where reuse could be tested. |
| `toolcraft` | How to choose, adapt or develop a missing capability and check that it works. |
| `reliability-by-construction` | Which design controls and checks support dependable operation and recovery. |
| `performance-metric-integrity` | How to define, verify and interpret measures of performance. |
| `institutional-intelligence` | How to assess incentives, promises, disputed claims and response options. |

The first five apply broadly to investigation and decision making. The remaining four concentrate the same kind of guidance on tools, reliability, performance measures and interactions with others.

## Examples of using both together

| Work | Regular task skill or tool | What the meta skill adds |
|---|---|---|
| Review a meeting | Capture comments with speaker labels and timestamps. | Institutional Intelligence examines promises and disagreements. Judgment assesses how strongly the record supports an interpretation. |
| Check a completion report | Read task records and calculate the completion rate. | Performance and Metric Integrity checks exclusions, counting rules, comparable periods and the improvement claim. |
| Investigate a code failure | Read code, execute a test and record the result. | Inquiry guides competing explanations and the next useful check. Judgment assesses the conclusion against the completed tests. |
| Prepare recurring automation | Implement a job and run test inputs through it. | Reliability by Construction identifies relevant failures, design controls and recovery checks. |
| Retain useful project work | Save files and update a project record. | Contribution identifies what has demonstrated value, records its limits and proposes a test of reuse. |

## Using the methods in a task

One agent can apply selected meta skills while using task skills to carry out the work. When collaboration is authorized, several agents can contribute different methods or perform separate checks. Record the evidence and limits of each contribution so conclusions remain traceable.

Select methods when they would help answer the current question. They can guide planning, investigation, execution or review. The host supplies available tools, access and execution controls. The user and host retain control of purpose, permissions and commitments.

## How to review the classification

Ask what the skill mainly contributes:

* A procedure for a particular job or tool points toward a regular task skill.
* Guidance about method choice, evidence, interpretation, priorities or transfer points toward a meta skill.
* A combination can be described by both roles, with the main emphasis stated clearly.

Review the actual instructions and expected result alongside the name. The classification describes the role of the skill. Evidence of its practical value comes from observing how agents use it in the intended setting.
