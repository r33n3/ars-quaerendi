# Preparing tools for reliable use

Use this guidance when a prototype needs to support repeatable tasks or deployment.

## Purpose
Match reliability work to the intended use. Record the capability, version, environment and permissions covered by each assessment.

## Flow
1. **Discover / Explore:** Inquiry, Discovery, Purpose & Planning; record hypotheses, prototypes and useful failures. Use controls appropriate to the experiment.
2. **Prototype / Build:** Toolcraft; establish one working case, controlled baselines, regression tests and explicit limits.
3. **Harden / Pilot:** Reliability by Construction; select credible failure classes, design invariants, exercise recovery and realistic variation.
4. **Review / Qualify:** Judgment checks evidence sufficiency and returns a scoped readiness recommendation. The user and host environment make authorization and promotion decisions.
5. **Catalog / Deploy:** If deployment is intended, record artifact identity, provenance, permitted capabilities, version, environment, rollback and monitoring in the chosen project or deployment system. Catalog results when they have an intended reuse or deployment.
6. **Observe / Improve:** Runtime results, incidents, anomalies and partial successes return to Inquiry, Discovery, Contribution, Toolcraft or Planning as warranted.

Choose checkpoints according to the task and its consequences. A disposable probe that only reads data can finish at prototype. A system that controls consequential actions needs stronger qualification evidence.

## Optional agent collaboration
People can apply this method directly, and agents can use it within their existing host environment. For collaboration between agents, verify each participant's identity, permissions and supporting evidence. Authorize capability reuse for a defined scope.

## Sample reliability contract
```yaml
capability: shared_task_execution
stage: pilot
scope:
  environment: authenticated_collaborators
  permissions: delegated_read_only
invariants:
  - duplicate_delivery_does_not_duplicate_side_effects
  - peer_cannot_expand_requester_authority
  - task_state_survives_owner_restart
tests:
  - duplicate_request
  - network_partition
  - peer_restart
  - invalid_result
observed_coverage: not_yet_measured
readiness: inconclusive
```

## Review guidance
* Record prototype results and deployment readiness separately.
* Set evidence requirements according to the consequences of failure.
* Begin with repeatable checks. Review disputed interpretations through a focused challenge and a set number of revision attempts.
* When qualification fails, identify the missing evidence, required control or scope restriction.
* Prefer architectural restrictions that remove failure classes.
* Report sample sizes, coverage and remaining uncertainty when assessing reliability.
