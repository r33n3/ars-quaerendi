---
name: reliability-by-construction
description: Improve correctness, repeatability, robustness and recovery when preparing tools or agents for reuse or deployment.
---
# Reliability by Construction

## Invoke when
A prototype is being promoted; repeated failures indicate a design weakness; a distributed task needs dependable recovery; a tool's side effects matter.

## Method
1. Define **operating envelope** (version, inputs, environment, permissions, resources, dependencies) and intended consequence of failure.
2. Separate **correctness**, **repeatability**, **robustness**, and **resilience**. Record the evidence for each property, including tests beyond the expected successful case.
3. State critical invariants. Use structural controls such as atomic writes, bounded interfaces, least authority and idempotency to prevent identified failures.
4. Identify credible failure modes using actual architecture, traces, incidents and threat model; rank by consequence, exposure and detectability. Keep the review focused on failures supported by the design or evidence.
5. Choose evidence appropriate to the stage and cost: deterministic tests, property tests, fault injection, model checking when justified, or independent reproduction.
6. Test recovery and containment: crashes, timeouts, malformed inputs, resource exhaustion, partial responses, restart, duplicate delivery, and peer partitions **as applicable**.
7. Distinguish observed reliability from statistical guarantees. Record sample sizes, coverage and uncertainty in failure-rate estimates.
8. If a test fails, determine whether the instrument, implementation, assumption or architecture failed. Prefer eliminating the failure class over repeated patches where economical.
9. Recommend readiness for the tested version, environment and intended use. The user and host environment control permissions.
10. Capture partial achievements and unexpected observations. Apply `contribution` and `discovery` when useful for those records.

## Stage-aware evidence
- Explore: isolated experiments and observation with limits appropriate to the experiment.
- Prototype: deterministic functional and regression checks.
- Pilot: realistic variations, bounded permissions and recovery exercises.
- Production: defined SLOs, monitoring, rollback, incident response and environment-specific qualification.
- High consequence: stronger independent evidence and explicit external approval.

## Output
Operating envelope, invariants, failure-mode table, test evidence/coverage, unresolved risks, stage-specific readiness and next smallest reliability improvement.

For extended promotion guidance, see [factory-and-reliability.md](../../references/factory-and-reliability.md) in the full package. Keep this reference available if installing the skill separately.
