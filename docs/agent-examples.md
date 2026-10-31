# Examples of agents using the skills

Each example describes a role an existing agent can perform. Supply the relevant skill files and task material. Select the methods needed for the question. Execution depends on the host's tools, access and permissions. These examples describe intended use; record actual results when evaluating an agent.

## Research agent

Material: a question, conflicting reports, source links or supplied documents.

Use `inquiry` to trace claims and consider explanations. Use `judgment` when the evidence is ready for a conclusion.

Expected result: findings with original sources, assumptions, counterevidence, open questions and a justified next check.

Example request:

> Investigate why these two reports reach different conclusions. Trace the evidence, compare assumptions and explain what further check would resolve the disagreement.

## Coding and debugging agent

Material: relevant code, errors, sample inputs, expected behavior and available test commands.

Use `inquiry` to investigate the cause, `toolcraft` for a missing diagnostic helper and `reliability-by-construction` for repeated use and recovery.

Expected result: an explanation supported by records or tests, a proposed or executed fix, test results and remaining limits. Distinguish code inspection from execution.

Example request:

> Investigate this intermittent import failure. Reproduce it when the available tools permit, compare possible causes and check the fix against partial input and interruption.

## Project planning agent

Material: goals, milestones, constraints, current commitments and a changed dependency.

Use `purpose-planning` to compare priorities and revise the plan. Use `judgment` for assumptions that materially affect the decision.

Expected result: a revised plan with reasons, dependencies, agreed owners, missing decisions and review points.

Example request:

> Our supplier is two weeks late. Compare ways to preserve the most valuable milestones, show the tradeoffs and identify changes that need authorization.

## Operations and automation agent

Material: execution records, incident times, expected behavior, configuration and recovery procedures.

Use `discovery` to examine patterns and `reliability-by-construction` to assess relevant failures and recovery.

Expected result: source linked patterns, competing explanations, completed checks and improvements within existing authorization.

Example request:

> Review this job that occasionally runs twice. Trace the duplicate requests, assess their effects and propose checks for safe retries and recovery.

## Reporting agent

Material: a report, measure definitions, source records, reporting periods and comparison groups.

Use `performance-metric-integrity` to recalculate results and examine exclusions. Use `judgment` to assess the improvement claim.

Expected result: reported and recalculated figures, differences, counting rules, missing records and limits on comparisons.

Example request:

> Check whether the claimed completion improvement holds when we use consistent definitions and comparable tasks. Show the arithmetic and any missing evidence.

## Supplier review agent

Material: the offer, requirements, existing terms, alternatives and authorization limits.

Use `institutional-intelligence` to assess terms, incentives, promises and dependencies. Use `inquiry` for claims that need research.

Expected result: verified terms, conditional promises, costs, risks, alternatives and questions for negotiation. Commitments stay within existing authorization.

Example request:

> Compare these supplier offers. Identify what each has demonstrated, what depends on future promises and which terms we should clarify before deciding.

## Knowledge and learning agent

Material: completed work, experiment records, useful artifacts or an authorized practice challenge.

Use `contribution` to retain useful methods and their limits. For requested investigative practice, use `inquiry` and `judgment` with [guided research practice](../references/research-apprenticeship.md).

Expected result: a reusable explanation with evidence and reproduction steps, or an evaluation record that distinguishes guesses, tests, feedback and demonstrated transfer.

Example request:

> Turn this investigation into a reusable method. Explain the decisive test, its limits and a new task where we could test whether the method transfers.

## Meeting note taking agent

Material: notes or a transcript, speaker labels, source locations and relevant earlier records.

Use `institutional-intelligence` for comments and commitments, `discovery` for recurring concerns and `judgment` to assess interpretations.

Expected result: speaker linked observations, commitments, tentative interpretations, alternative explanations and follow up questions.

Example request:

> Identify the commitments, disputed claims and recurring concerns in these notes. Cite speakers and source locations, and identify interpretations that need clarification.

See the [meeting review guide](meeting-notes.md) for details and a worked example.
