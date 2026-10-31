# Factory progression and assurance without gridlock

This is a **method and integration contract**, not a new agent factory or central coordinator.

## Purpose
Preserve experimental freedom while engineering repeatable, resilient capabilities for specific intended uses. Qualify **capability × version × environment × permissions**, not an agent as universally trustworthy.

## Flow
1. **Discover / Explore:** Inquiry, Discovery, Purpose & Planning; record hypotheses, prototypes and useful failures. No production-grade burden.
2. **Prototype / Build:** Toolcraft; establish one working case, controlled baselines, regression tests and explicit limits.
3. **Harden / Pilot:** Reliability by Construction; select credible failure classes, design invariants, exercise recovery and realistic variation.
4. **Review / Qualify:** Judgment checks evidence sufficiency and returns a scoped readiness recommendation. The user and host environment make authorization and promotion decisions.
5. **Catalog / Deploy:** If deployment is intended, record artifact identity, provenance, permitted capabilities, version, environment, rollback and monitoring in the chosen project or deployment system. A research success need not be cataloged.
6. **Observe / Improve:** Runtime results, incidents, anomalies and partial successes return to Inquiry, Discovery, Contribution, Toolcraft or Planning as warranted.

These are promotion checkpoints, **not mandatory steps for every task**. A read-only disposable probe can finish at prototype; a high-consequence actuator needs stronger gates.

## Optional agent collaboration
People can apply this method directly, and agents can use it within their existing host environment. If agent-to-agent (A2A) collaboration is available, each participant retains its own authorization boundaries. Peers may offer capabilities and evidence, but no peer automatically inherits another's permissions or verification. Capability reuse is scoped and authorized. No peer network, central registry, coordinator, or approval service is required.

## Sample reliability contract
```yaml
capability: a2a_task_execution
stage: pilot
scope:
  environment: trusted_p2p_mesh
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

## Anti-gridlock rules
- A proof-of-concept may be useful while unqualified for deployment.
- Evidence standard rises with consequences, not the number of judges.
- Deterministic controls precede semantic review; one targeted challenge and bounded revision by default.
- A failing qualification should return the **specific missing evidence or restriction**, not an infinite rejection loop.
- Prefer architectural restrictions that remove failure classes.
- Never mistake absence of observed failures for proof of safety.
