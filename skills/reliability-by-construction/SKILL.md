---
name: reliability-by-construction
description: Engineer repeatability, correctness, robustness, and resilience before promoting experimental tools or agents into consequential or reusable use.
---
# Reliability by Construction

## Invoke when
A prototype is being promoted; repeated failures indicate a design weakness; a distributed task needs dependable recovery; a tool's side effects matter.

## Method
1. Define **operating envelope** (version, inputs, environment, permissions, resources, dependencies) and intended consequence of failure.
2. Separate **correctness**, **repeatability**, **robustness**, and **resilience**. Passing a happy-path test proves none of the others.
3. State critical invariants. Prefer structural prevention (atomic writes, bounded interfaces, least authority, idempotency) over retrying or judging every conceivable failure.
4. Identify credible failure modes using actual architecture, traces, incidents and threat model; rank by consequence, exposure and detectability. Do not invent endless hypotheticals.
5. Choose the least expensive proof suitable to the stage: deterministic tests, property tests, fault injection, model checking when justified, or independent reproduction.
6. Test recovery and containment: crashes, timeouts, malformed inputs, resource exhaustion, partial responses, restart, duplicate delivery, and peer partitions **as applicable**.
7. Distinguish observed reliability from statistical guarantees. Zero failures in a small sample is not proof of zero failure probability. Record sample sizes and coverage.
8. If a test fails, determine whether the instrument, implementation, assumption or architecture failed. Prefer eliminating the failure class over repeated patches where economical.
9. Return a **scoped readiness recommendation**; do not grant permissions or certify universal trust.
10. Capture partial achievements and unexpected observations. If available and useful, apply `contribution` and `discovery` for those records; neither skill is required.

## Stage-aware evidence
- Explore: isolated experiments and observation; do not require production reliability.
- Prototype: deterministic functional and regression checks.
- Pilot: realistic variations, bounded permissions and recovery exercises.
- Production: defined SLOs, monitoring, rollback, incident response and environment-specific qualification.
- High consequence: stronger independent evidence and explicit external approval.

## Output
Operating envelope, invariants, failure-mode table, test evidence/coverage, unresolved risks, stage-specific readiness and next smallest reliability improvement.

For extended promotion guidance, see [factory-and-reliability.md](../../references/factory-and-reliability.md) in the full package. Keep this reference available if installing the skill separately.
