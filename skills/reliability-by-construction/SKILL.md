---
name: reliability-by-construction
description: Improve correctness, repeatability, robustness and recovery when preparing tools or agents for reuse or deployment.
---
# Reliability by Construction

## Invoke when
A prototype is being promoted; repeated failures indicate a design weakness; a distributed task needs dependable recovery; a tool's side effects matter.

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

For extended promotion guidance, see [factory-and-reliability.md](../../references/factory-and-reliability.md) in the full package. Keep this reference available if installing the skill separately.
