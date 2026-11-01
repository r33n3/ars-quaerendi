# Evidence records and handoffs

Use shared records when findings need to be retained or passed to another skill. Choose an appropriate level of detail for ordinary task responses. The schemas describe record structure, while the agent and host apply the methods and authorization rules.

## Evidence fields

The [evidence record schema](../schemas/evidence-record.schema.json) records:

* `evidence_id`: a stable identifier for this record and its content.
* `claim_id` and `claim`: the specific statement being examined.
* `record_kind`: `illustrative` for an invented example, or `operational` for a record of actual work.
* `provenance`: where the evidence came from, how it was obtained and which artifacts are relevant.
* `relationship`: whether the evidence supports, contradicts, qualifies or is neutral toward the claim, or leaves the relationship undetermined.
* `uncertainty`: limitations and open questions.
* `tested_scope`: population or system, coverage and conditions.
* `legacy_status`: the familiar D, O, R, H, U or X summary for existing consumers.

Keep provenance, relationship, uncertainty and scope separate. An observed measurement may remain valid while contradicting an earlier explanation. The legacy status summarizes a record; use the separate fields for detailed interpretation.

## Source and observation

A supplied report describes documented evidence. Mark it as documentary even when its author reports measurements. Direct observation records the agent's actual inspection or measurement. Independent reproduction records the separate conditions, method and artifacts that establish its independence.

Use `unknown` provenance and an undetermined relationship when the source or relevance is unresolved. Preserve the missing information as an open question. Invented examples remain marked `illustrative` throughout the walkthrough.

## Passing records between skills

The [handoff schema](../schemas/handoff.schema.json) identifies the sending skill, receiving skill, claim and evidence. Include the referenced evidence records with the transfer or keep them accessible to the receiver.

Each evidence identifier has a record reference, content hash, scope snapshot and uncertainty snapshot. The maps in `evidence_refs`, `evidence_hashes`, `scope` and `uncertainty` use the identifiers in `evidence_ids` as their keys. In the bundled examples, references are relative to the handoff file.

Calculate the content hash using SHA256 over the complete evidence record serialized as JSON with sorted keys, compact separators and ASCII escapes. The validator provides the same calculation. This makes changes to provenance, relationship, observations and other fields visible during transfer.

Preserve earlier evidence, including contradictions and qualifications, when adding records. Explain new evidence through `change_basis`. Create a new evidence identifier for changed content, including a corrected interpretation, and retain the earlier record. Distinguish a new interpretation from a new measurement through its provenance and status.

Use a new chain when the claim or actual authorization context changes. Carry the current authority context unchanged through a chain. Keep the parent outcome separate from a useful component or reusable method.

Record the sending method's result in `outcome_status`. Use resolved, provisional, inconclusive, blocked or stopped as defined in the method contracts. This describes the assessment being passed along; record the parent outcome separately.

## Judgment levels

Record the assessment basis whenever a judgment level is supplied. The first assessment comes from Judgment. Later receivers carry that assessment forward. A revised assessment comes from Judgment with a recorded basis, and an increase requires new evidence.

J3 requires records of actual direct verification or independent reproduction. J4 also identifies the qualification record for the defined use. A higher verification level requires a new verification record. Documentary reports and invented walkthroughs retain their stated limits.

The bundled examples use J1 or J2 for conclusions supported within their supplied sources. They leave actual reproduction, payment verification and broader generalization unresolved.

## Compatibility and checks

The earlier `research-state.schema.json` remains available for existing records. New detailed evidence and handoffs use the separate schemas described here.

The optional package validator checks schemas, identifiers, references, content hashes, snapshots, route continuity and structural requirements for judgment levels. It also checks that the Markdown contracts match the JSON registry. These checks establish consistency of the supplied records. Truth of observations, adequacy of experimental methods and behavior under real host conditions require evaluation using the relevant source material and execution records.
