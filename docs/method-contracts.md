# Method contracts

Each meta skill declares a method contract describing when it is useful, what it needs, what it can return and where its authority ends. One or more agents can use the contracts to select methods and exchange findings within the user's task.

## Contract source

The [JSON registry](../contracts/skill-contracts.json) contains the nine contracts. The [contract schema](../contracts/skill-contract.schema.json) describes their structure. Each skill has a matching Method contract section generated from that registry.

The contracts are reference material. The host continues to provide discovery, tools, execution controls and authorization. Select the methods relevant to the current question.

## Fields

| Field | Meaning |
|---|---|
| `activation` | The situation that makes the method useful. |
| `non_activation` | How routine work can proceed when a separate method review adds little value. |
| `inputs.required` | The minimum question or material needed to frame the method. |
| `inputs.helpful` | Additional context that can improve the result. |
| `inputs.missing_behavior` | What can be assessed and what remains unresolved when information is missing. |
| `outputs.evidence` | Observations, checks, sources and uncertainty the method records. |
| `outputs.records` | Plans, assessments, proposals or other records it returns. |
| `recommendations` | Decisions or next actions the method can recommend. |
| `authority` | The user and host controls that apply to actions and commitments. |
| `stopping` | Conditions for ending the method and preserving partial work. |
| `consumers` | Skills that can use its output when another question needs a method. |
| `failure_behavior` | How the method reports gaps, failed checks and useful partial results. |
| `outcome_statuses` | The state of this method's result. |
| `optional_methods` | Optional method identifiers mapped to shared references in the method index. |
| `revision_triggers` | Changes that justify reopening the assessment. |

The contract version identifies this field structure. Skill identifiers retain their existing names.

## Outcome status

* `resolved`: the method's question is answered within its stated scope.
* `provisional`: the result depends on explicit assumptions or conditions.
* `inconclusive`: available evidence leaves the question unsettled.
* `blocked`: a required prerequisite or authorization prevents further progress.
* `stopped`: the review ends because of an agreed limit, instruction or value decision.

Record the reason, limitations and open checks with the status. This status describes the method result. Keep the parent goal's outcome and actual execution state separately. A completed review may recommend continuing existing goals or stopping a proposed action.

## Handoffs

Use the [evidence and handoff rules](../references/evidence-handoff-rules.md) when another skill needs the result. Preserve claim identity, provenance, contradictions, uncertainty and tested scope. Include evidence references and the actual authorization context.

The [walkthroughs](../examples/complete-handoffs/README.md) show four complete routes: research and reuse, offer review and planning, investigation of an unexpected pattern, and a proposed discriminating experiment. Each uses invented source material and retains its limits at every step.

## Updating contracts

Edit the JSON registry, then run `python3 tests/validate_v27.py --sync-contracts` to update the matching skill sections. Run `python3 tests/validate_v27.py` for a check that leaves files unchanged. These optional maintenance commands use Python; full schema validation uses `jsonschema`.

Run `python3 tests/test_interoperability.py` for cases that deliberately change records, remove evidence, broaden scope or attempt unsupported verification upgrades. The checks support package maintenance. Host behavior evaluation uses the scenarios in `tests/handoff-invariants.md`.

## Optional method index

The [model and experiment index](../contracts/v28-method-extensions.json) and [memory method index](../contracts/v29-method-extensions.json) map identifiers to owning skills and references. The validator compares these identifiers with the contract registry and checks local references. Experimental lenses and narrative summaries require a user request or an approved evaluation that includes them. The agent and host apply selection and permission rules during use.
