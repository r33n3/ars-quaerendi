# Examples of what agents can do with the skills

These examples show agents using the package's meta skills alongside regular task skills and tools. The meta skills guide choices, evidence checks and interpretation. Task skills perform work such as reading files, calculating values or producing artifacts. See [the distinction](meta-skills.md) for details.

An agent or several agents can use the skills for the tasks below. Supply the selected skill files and task material. Select the methods needed for the question. When collaboration is authorized, divide work according to available access and record the evidence and limits of each part. Execution depends on the host's tools, access and permissions. Record actual results when evaluating these intended uses.

## Research

Material: a question, conflicting reports, source links or supplied documents.

Agents can use `inquiry` to trace claims and consider explanations. They can use `judgment` when the evidence is ready for a conclusion.

Expected result: findings with original sources, assumptions, counterevidence, open questions and a justified next check.

Example request:

> Investigate why these two reports reach different conclusions. Trace the evidence, compare assumptions and explain what further check would resolve the disagreement.

## Coding and debugging

Material: relevant code, errors, sample inputs, expected behavior and available test commands.

Agents can use `inquiry` to investigate the cause, `toolcraft` for a missing diagnostic helper and `reliability-by-construction` for repeated use and recovery.

Expected result: an explanation supported by records or tests, a proposed or executed fix, test results and remaining limits. Distinguish code inspection from execution.

Example request:

> Investigate this intermittent import failure. Reproduce it when the available tools permit, compare possible causes and check the fix against partial input and interruption.

## Project planning

Material: goals, milestones, constraints, current commitments and a changed dependency.

Agents can use `purpose-planning` to compare priorities and revise the plan. They can use `judgment` for assumptions that materially affect the decision.

Expected result: a revised plan with reasons, dependencies, agreed owners, missing decisions and review points.

Example request:

> Our supplier is two weeks late. Compare ways to preserve the most valuable milestones, show the tradeoffs and identify changes that need authorization.

## Operations and automation

Material: execution records, incident times, expected behavior, configuration and recovery procedures.

Agents can use `discovery` to examine patterns and `reliability-by-construction` to assess relevant failures and recovery.

Expected result: source linked patterns, competing explanations, completed checks and improvements within existing authorization.

Example request:

> Review this job that occasionally runs twice. Trace the duplicate requests, assess their effects and propose checks for safe retries and recovery.

## Reporting

Material: a report, measure definitions, source records, reporting periods and comparison groups.

Agents can use `performance-metric-integrity` to recalculate results and examine exclusions. They can use `judgment` to assess the improvement claim.

Expected result: reported and recalculated figures, differences, counting rules, missing records and limits on comparisons.

Example request:

> Check whether the claimed completion improvement holds when we use consistent definitions and comparable tasks. Show the arithmetic and any missing evidence.

## Supplier review

Material: the offer, requirements, existing terms, alternatives and authorization limits.

Agents can use `institutional-intelligence` to assess terms, incentives, promises and dependencies. They can use `inquiry` for claims that need research.

Expected result: verified terms, conditional promises, costs, risks, alternatives and questions for negotiation. Commitments stay within existing authorization.

Example request:

> Compare these supplier offers. Identify what each has demonstrated, what depends on future promises and which terms we should clarify before deciding.

## Knowledge and learning

Material: completed work, experiment records, useful artifacts or an authorized practice challenge.

Agents can use `contribution` to retain useful methods and their limits. For requested investigative practice, agents can use `inquiry` and `judgment` with [guided research practice](../references/research-apprenticeship.md).

Expected result: a reusable explanation with evidence and reproduction steps, or an evaluation record that distinguishes guesses, tests, feedback and demonstrated transfer.

Example request:

> Turn this investigation into a reusable method. Explain the decisive test, its limits and a new task where we could test whether the method transfers.

## Meeting notes

Material: notes or a transcript, speaker labels, source locations and relevant earlier records.

Agents can use `institutional-intelligence` for comments and commitments, `discovery` for recurring concerns and `judgment` to assess interpretations.

Expected result: speaker linked observations, commitments, tentative interpretations, alternative explanations and follow up questions.

Example request:

> Identify the commitments, disputed claims and recurring concerns in these notes. Cite speakers and source locations, and identify interpretations that need clarification.

See the [meeting review guide](meeting-notes.md) for details and a worked example.
