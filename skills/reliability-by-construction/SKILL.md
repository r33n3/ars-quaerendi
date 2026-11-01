---
name: reliability-by-construction
description: Agents can use this meta skill to prepare tools or systems for repeated use by improving correctness, testing and recovery. Use when a prototype is being reused, failures recur or side effects matter. Return operating limits, failure checks, test evidence and readiness for a defined use.
---
# Reliability by Construction: Design, Testing and Recovery

Use this skill to make expected behavior and recovery dependable within a defined setting. It connects design choices, permissions, repeatable tests, relevant failure conditions, monitoring and restoration of earlier versions.

## Meta skill role

Agents use this focused meta skill to choose design controls and evidence needed for dependable use. Task skills can implement a control or execute a test. Reliability by Construction connects those actions to expected behavior, relevant failures and recovery.

## When to use

Use when a prototype is moving toward repeated use or deployment, a failure exposes a design weakness or a task can leave partial changes. Choose the depth of review according to the consequences of failure.

## Available tools

Choose methods that fit the tools and access available in the current session. Work from supplied material when access is limited. State which searches, tests or checks were completed, which remain unverified and what would be needed to complete them.

## Method
1. Define the version, inputs, environment, permissions, resources and dependencies being tested. Describe the consequences of failure.
2. Separate **correctness**, **repeatability**, **robustness**, and **resilience**. Record the evidence for each property, including tests beyond the expected successful case.
3. State the conditions that must remain true. Prevent failures through design. For example, make file changes complete in one operation, restrict access to what the task needs and ensure that repeated requests have the same effect as one request.
4. Identify possible failures using the design, execution records and past incidents. Rank them by their consequences, likelihood and ease of detection.
5. Choose evidence appropriate to the stage and cost: repeatable tests, property tests, fault injection, model checking when justified, or independent reproduction.
6. Test how the system limits damage and recovers from relevant failures. These may include crashes, timeouts, invalid inputs, exhausted resources, partial responses, restarts, repeated requests and lost connections.
7. Distinguish observed reliability from statistical guarantees. Record sample sizes, coverage and uncertainty in estimates of how often failures occur.
8. If a test fails, determine whether the instrument, implementation, assumption or architecture failed. Prefer eliminating the failure class over repeated patches where economical.
9. Recommend readiness for the tested version, environment and intended use. The user and host environment control permissions.
10. Capture partial achievements and unexpected observations. Apply `contribution` and `discovery` when useful for those records.

## Evidence for each stage
* Explore: isolated experiments and observation with limits appropriate to the experiment.
* Prototype: repeatable checks of expected behavior and previously working features.
* Pilot: realistic variations, bounded permissions and recovery exercises.
* Production: defined service level objectives, monitoring, rollback, incident response and checks for the intended environment.
* High consequence: stronger independent evidence and explicit external approval.

## Output
Report the operating conditions, required behavior, possible failures, test results, coverage and remaining risks. State whether the system is ready for the intended use and identify the next useful improvement.

For extended promotion guidance, see [factory and reliability guidance](../../references/factory-and-reliability.md) in the full package. Keep this reference available if installing the skill separately.

## Example request

Review this recurring import job before wider use. Check repeated requests, missing files, partial writes and recovery after interruption.

## Method contract

This section matches the [shared contract registry](../../contracts/skill-contracts.json). See [evidence and handoff rules](../../references/evidence-handoff-rules.md) when another skill needs the result.

* **Activation:** A prototype is moving toward repeated use or a relevant failure exposes a design or recovery weakness.
* **Routine handling:** Use ordinary prototype checks when a limited experiment has no justified need for a broader readiness review.
* **Required inputs:** The intended behavior or use; The artifact or system under review.
* **Helpful context:** Operating conditions and permissions; Required properties, failure records and test material; Consequences, resource limits and recovery needs.
* **Missing inputs:** Describe the required behavior and proposed checks. Keep readiness provisional when system details or execution evidence are missing.
* **Evidence produced:** Results of relevant functional and failure checks; Recovery and containment observations; Sample sizes, coverage and unresolved risks.
* **Records produced:** A readiness recommendation for a defined use; Design controls, evidence gaps and next improvements.
* **Recommendations:** Proceed within tested limits; Revise a control, run a targeted check or limit use; Defer qualification or stop the review.
* **Authority:** Readiness applies to the stated version, setting and use. The user and host control deployment and changes to authority.
* **Stop when:** Evidence is sufficient for the intended stage; A specific gap prevents qualification; Required access or the agreed testing budget is exhausted.
* **Outcome status:** `resolved`, `provisional`, `inconclusive`, `blocked`, `stopped`.
* **Reopen when:** Changed version, setting or permissions; New failures or corrected tests; A broader or more consequential intended use.
* **Possible consumers:** `judgment`, `toolcraft`, `performance-metric-integrity`.
* **Failure handling:** Report the specific missing control or evidence, preserve prototype results and identify a useful revision or restriction.
