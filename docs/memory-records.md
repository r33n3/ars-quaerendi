# Checkpoints and significant event records

Use these records when continuity or reuse would help the task. The host supplies storage, search, telemetry and execution controls. Reading the methods and supplying records in a chat requires access to the text. Use the schemas when structured records would help the task.

## Shared evidence

The [checkpoint schema](../schemas/research-checkpoint.schema.json) and [event schema](../schemas/salient-memory.schema.json) use evidence identifiers, local references, content hashes, tested scope and uncertainty snapshots. They follow the [evidence rules](../references/evidence-handoff-rules.md). Record version and illustrative or operational status explicitly. Each evidence domain remains attached to its record. Source and revision references resolve to retained files in the package examples.

The [checkpoint example](../examples/context-reset-handoff.json) references the existing conversion investigation evidence unchanged. The [event example](../examples/salient-peer-failure.json) references an invented report through a documentary evidence record. Its reliability remains unverified.

## Checkpoint and recovery

Keep purpose and goal references, unknowns, contradictions, experimental state, pending actions, the next useful step and historical authorization context. Recover these records before continuing. Reconcile pending actions with actual task state and apply current user instructions and host permissions.

Resource snapshots distinguish runtime telemetry from unknown values. Runtime values include a retained source reference and capture time. Metrics carry units in their names, such as `remaining_seconds`. Missing telemetry uses null values. Keep forecasts separately labeled in the task plan.

Recovery status describes reconstruction of the checkpoint. A verified status needs operational evidence of the recovery checks. Check source availability, hash consistency, retained scope, unresolved questions and current state. Task completion and authorization require their own assessment. Mark missing critical state failed or unverified, with the gap preserved.

## Significant events

Record significance rationale, evidence reliability, current relevance and recommended behavioral influence separately. Include recall cues, a lesson, applicability conditions, possible counterexamples, limitations and revision status. Observed or reproduced reliability needs operational source evidence with the appropriate provenance. High significance alone leaves reliability unchanged.

Corrections create a new record with a new identifier and `revision_refs` pointing to earlier records. Keep the earlier files and evidence available. Review the corrected lesson against the current task. Archiving and retention follow the user's instructions and available storage.

## Checking records

Check record structure against the schemas. Confirm evidence identifiers, source references, content hashes, scope, uncertainty and the requirements for reliability or recovery claims. Keep earlier records available when adding a correction.

Record consistency and actual performance require separate evidence. Reconstruction, persistence, suitability of a lesson and effects on agent behavior need observations in the relevant host.
