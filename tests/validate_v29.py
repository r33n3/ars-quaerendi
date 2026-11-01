"""Check memory examples and their evidence. Schema validation uses optional jsonschema."""

from urllib.parse import urlsplit

from validate_v27 import (
    ROOT, Draft202012Validator, evidence_hash, load_json, local_reference,
    require, validate_method_extensions,
)


def memory_validators(root=ROOT):
    schemas = {
        "checkpoint": load_json(root / "schemas/research-checkpoint.schema.json"),
        "memory": load_json(root / "schemas/salient-memory.schema.json"),
        "evidence": load_json(root / "schemas/evidence-record.schema.json"),
    }
    if Draft202012Validator is None:
        return {}
    for schema in schemas.values():
        Draft202012Validator.check_schema(schema)
    return {name: Draft202012Validator(schema) for name, schema in schemas.items()}


def validate_record(path, kind, validators, root=ROOT, registry=None):
    record = load_json(path)
    require(kind in ("checkpoint", "memory"), "Unknown memory record kind")
    if validators:
        validators[kind].validate(record)
    ids = record["evidence_ids"]
    require(bool(ids) and len(ids) == len(set(ids)), "Evidence identifiers must be present and unique")
    for field in ("evidence_refs", "evidence_hashes", "tested_scope", "uncertainty"):
        require(set(record[field]) == set(ids), f"Evidence keys differ in {field}")
    registry = {} if registry is None else registry
    evidence = {}
    for identifier in ids:
        source_path = local_reference(path.parent, record["evidence_refs"][identifier], root)
        source = load_json(source_path)
        if validators:
            validators["evidence"].validate(source)
        require(source["evidence_id"] == identifier, "Evidence identifier differs from reference")
        require(record["record_kind"] == "illustrative" or source["record_kind"] == "operational", "Operational memory requires operational evidence")
        fingerprint = evidence_hash(source)
        require(record["evidence_hashes"][identifier] == fingerprint, "Evidence content hash differs")
        require(registry.get(identifier, fingerprint) == fingerprint, "Evidence identifier reused for changed content")
        registry[identifier] = fingerprint
        require(record["tested_scope"][identifier] == source["tested_scope"], "Tested scope differs from evidence")
        require(record["uncertainty"][identifier] == source["uncertainty"], "Uncertainty differs from evidence")
        reference = source["provenance"]["source"]
        if urlsplit(reference).scheme not in ("http", "https") and source["provenance"]["origin"] != "unknown":
            local_reference(source_path.parent, reference, root)
        evidence[identifier] = source
    for reference in record.get("revision_refs", []):
        prior_path = local_reference(path.parent, reference, root)
        prior = load_json(prior_path)
        if validators:
            validators["memory"].validate(prior)
        require(prior["event_id"] != record["event_id"], "A revision requires a new event identifier")
    if kind == "checkpoint":
        for field in ("purpose_ref", "goal_ref"):
            local_reference(path.parent, record[field], root)
        snapshot = record["resource_snapshot"]
        if snapshot["source"] == "unknown":
            require(all(value is None for value in snapshot["metrics"].values()), "Unknown telemetry must retain unknown values")
        else:
            require(snapshot["source"] == "runtime", "Unknown telemetry source")
            local_reference(path.parent, snapshot["source_ref"], root)
        recovery_ids = record.get("recovery_evidence_ids", [])
        if record["recovery_status"] == "verified":
            require(bool(recovery_ids) and record["record_kind"] == "operational", "Verified recovery requires operational evidence")
        for identifier in recovery_ids:
            require(identifier in evidence, "Recovery evidence is outside the checkpoint")
            check_observation(evidence[identifier])
    elif record["reliability"] in ("observed", "reproduced"):
        require(record["record_kind"] == "operational", "Observed reliability requires an operational record")
        for source in evidence.values():
            check_observation(source)
            if record["reliability"] == "reproduced":
                require(source["provenance"]["origin"] == "independent_reproduction", "Reproduced reliability needs independent reproduction")
    return record


def check_observation(source):
    require(source["record_kind"] == "operational", "Illustrative evidence leaves actual verification unresolved")
    require(source["provenance"]["origin"] in ("direct", "independent_reproduction"), "Documentary evidence leaves direct observation unresolved")
    require(source["tested_scope"].get("domain") in ("software", "simulation", "real_world"), "Observation requires an explicit tested domain")


def validate_package(root=ROOT):
    validators = memory_validators(root)
    registry = {}
    for filename, kind in (("context-reset-handoff.json", "checkpoint"), ("salient-peer-failure.json", "memory")):
        validate_record(root / "examples" / filename, kind, validators, root, registry)
    contracts = {item["skill_id"]: item for item in load_json(root / "contracts/skill-contracts.json")}
    validate_method_extensions(root, contracts)
    if not validators:
        print("JSON schema checks skipped: install jsonschema for full validation")
    print("Memory records, evidence references and method mappings: passed")


if __name__ == "__main__":
    validate_package()
