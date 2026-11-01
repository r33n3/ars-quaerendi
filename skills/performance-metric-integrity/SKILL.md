---
name: performance-metric-integrity
description: Agents can use this meta skill to define performance measures and check reports against source records. Use for dashboards, progress reviews, changed counting rules or improvement proposals. Return recalculated results, trend limits, related outcomes and options for improvement.
---
# Performance and Metric Integrity: Measures and Report Checks

Use this skill to examine how a measure is defined, calculated and interpreted. It checks inclusion rules, exclusions, missing records, comparable groups, source history and whether related outcomes support the reported improvement.

## Meta skill role

Agents use this focused meta skill to decide how a measure should be defined, checked and interpreted. Task skills can query records or calculate a rate. Performance and Metric Integrity examines the counting rules, comparison and evidence behind the reported result.

## When to use

Use when defining success measures, reviewing dashboards or meeting reports, comparing performance over time or investigating conflicting numbers. Also use it to compare the expected benefits, costs and risks of a proposed improvement.

## Available tools

Choose methods that fit the tools and access available in the current session. Work from supplied material when access is limited. State which searches, tests or checks were completed, which remain unverified and what would be needed to complete them.

## Method

1. State the intended outcome, the people or tasks covered and the decision the measure will support. Check how the measure reflects the actual outcome.
2. Define what is counted, what is included or excluded, the units, source records, reporting period, owner and definition version. State how missing, cancelled and repeated records are handled and how soon results are reported. Preserve earlier definitions and corrections.
3. Obtain authorized source records. Prefer records with a history of changes or a way to detect changes. Recalculate the result and record counts, exclusions, missing records, differences and source history. Investigate possible causes of any difference.
4. Check related outcomes such as coverage, user confirmed usefulness, reopened work, severity, cost, reliability, permission violations and quality. Record favorable and unfavorable evidence.
5. Test how changes in exclusions, reporting periods, task difficulty, definitions, delayed records and repeated achievements affect the score. Check whether the score could rise while the intended outcome worsens.
6. Compare similar tasks, versions, hardware and reporting periods. Record sample sizes, uncertainty and the baseline. Explain the limits of conclusions drawn from a small sample.
7. Compare the likely benefits, costs, risks, confidence and alternatives for each proposed improvement. Include the cost of delaying other work and how easily changes could be reversed. Use a small experiment when the evidence is weak.
8. Plan a comparison before and after the change, or use a control group when appropriate. Define when to stop or restore the earlier version. Track related outcomes for signs of harm.
9. Report what improved, what worsened, what was learned, remaining uncertainty and verified achievements. Support recognition of progress with source records and independent checks.
10. Identify any independent audit or professional review needed for formal financial, regulatory or other consequential reports.

## Evidence and permissions

* Support claims with recorded evidence and state what was independently checked.
* Preserve source records, earlier definitions and scoring rules. Obtain authorization for changes.
* Investigate differences through evidence. Consider errors, missing data, changed definitions and manipulation as possible explanations.
* Share records and summaries within the permissions set by the user and host environment.

## Output

Report the measure and its definition, source coverage, recalculated result, reported result, differences, related outcomes, trend limits and options for improvement. Recommend an experiment, continued observation, revision or a stop, with the supporting evidence.

For detailed guidance, see [measurement checks](../../references/metric-integrity-and-reconciliation.md) and [reliability guidance](../../references/factory-and-reliability.md) in the full package. Keep these references available when installing the skill separately.

## Example request

Check the reported improvement against the source records. Explain the counting rules, exclusions and differences between comparable periods.

## Method contract

This section matches the [shared contract registry](../../contracts/skill-contracts.json). See [evidence and handoff rules](../../references/evidence-handoff-rules.md) when another skill needs the result.

* **Activation:** A material measure, trend, reported achievement or proposed improvement needs verification.
* **Routine handling:** Provide a straightforward calculation directly when its definition and source records are already clear.
* **Required inputs:** The measure, report or outcome being assessed.
* **Helpful context:** Definitions and counting rules; Source records, periods and comparable groups; Earlier versions, exclusions and intended decision.
* **Missing inputs:** State the missing definition or records. Explain which parts can be assessed and which calculations or comparisons remain unresolved.
* **Evidence produced:** Recalculated counts and results; Definition changes, exclusions and source gaps; Related outcomes and limits on comparisons.
* **Records produced:** A reconciled or explicitly unresolved report; Options for improvement and further verification.
* **Recommendations:** Use a verified measure within its scope; Correct a report or collect missing records; Test an improvement or defer a decision.
* **Authority:** Source records and scoring policies remain under existing authorization. Recommendations identify corrections and uncertainty; formal commitments and publication follow user and host controls.
* **Stop when:** The reported result is reconciled; A specific source or definition gap remains documented; The agreed review limit is reached.
* **Outcome status:** `resolved`, `provisional`, `inconclusive`, `blocked`, `stopped`.
* **Reopen when:** New source records or corrected counts; Changed definitions, periods or task mix; Evidence about the effects of an improvement.
* **Possible consumers:** `judgment`, `purpose-planning`, `institutional-intelligence`.
* **Failure handling:** Return the calculation evidence, discrepancies, possible causes and remaining uncertainty and keep possible motives tentative.

## Optional comparison of variants

Agents can use [method comparison](../../references/adaptive-variation-selection.md) to compare useful outcomes, total resource cost, regressions and correlated failures under comparable conditions. Assess recovery and cumulative improvement through distinct measures. Preserve coverage limits, baseline results and uncertain findings.
