"""Check adaptation records and evidence. Full schema checks use optional jsonschema."""

from urllib.parse import urlsplit

from validate_v27 import (
    ROOT, Draft202012Validator, evidence_hash, load_json, local_reference,
    require, validate_method_extensions,
)
from validate_v29 import check_observation


def adaptation_validators(root=ROOT):
    schemas = {
        "adaptation": load_json(root / "schemas/adaptation-record.schema.json"),
        "evidence": load_json(root / "schemas/evidence-record.schema.json"),
    }
    if Draft202012Validator is None:
        return {}
    for schema in schemas.values():
        Draft202012Validator.check_schema(schema)
    return {name: Draft202012Validator(schema) for name, schema in schemas.items()}


def validate_record(path, validators, root=ROOT):
    record = load_json(path)
    if validators:
        validators["adaptation"].validate(record)
    local_reference(path.parent, record["purpose_ref"], root)
    ids = record["evidence_ids"]
    require(len(ids) == len(set(ids)), "Duplicate evidence identifier")
    for field in ("evidence_refs", "evidence_hashes", "tested_scope", "uncertainty"):
        require(set(record[field]) == set(ids), f"Evidence keys differ in {field}")
    evidence = {}
    for identifier in ids:
        source_path = local_reference(path.parent, record["evidence_refs"][identifier], root)
        source = load_json(source_path)
        if validators:
            validators["evidence"].validate(source)
        require(source["evidence_id"] == identifier, "Referenced evidence identifier differs")
        require(source["claim_id"] == record["claim_id"], "Claim differs from referenced evidence")
        require(record["record_kind"] == "illustrative" or source["record_kind"] == "operational", "Operational records require operational evidence")
        require(record["evidence_hashes"][identifier] == evidence_hash(source), "Evidence content hash differs")
        require(record["tested_scope"][identifier] == source["tested_scope"], "Tested scope differs from evidence")
        require(record["uncertainty"][identifier] == source["uncertainty"], "Uncertainty differs from evidence")
        reference = source["provenance"]["source"]
        if urlsplit(reference).scheme not in ("http", "https") and source["provenance"]["origin"] != "unknown":
            local_reference(source_path.parent, reference, root)
        evidence[identifier] = source

    def check_ids(references, observed=False):
        require(len(references) == len(set(references)), "Duplicate evidence reference")
        require(set(references) <= set(evidence), "Evidence reference is outside the record")
        if observed:
            require(bool(references), "Observed results require evidence")
            require(record["record_kind"] == "operational", "Illustrative records leave actual execution unverified")
            for identifier in references:
                source = evidence[identifier]
                check_observation(source)
                require(source["tested_scope"]["domain"] == record["decision_domain"], "Observed evidence is outside the decision domain")

    baseline = record["baseline"]
    check_ids(baseline["evidence_ids"], baseline["status"] == "tested")
    delta = record["environment_delta"]
    check_ids(delta["evidence_ids"], delta["status"] == "observed")
    variants = record["variants"]
    names = [item["id"] for item in variants]
    require(len(names) == len(set(names)), "Duplicate variant identifier")
    require(all(isinstance(name, str) and name.strip() for name in names), "Variant identifiers must be meaningful")
    for variant in variants:
        check_ids(variant["evidence_ids"])
        comparison = variant.get("comparison")
        if variant["status"] in ("tested", "retained"):
            require(isinstance(comparison, dict), "Tested variants require comparison evidence")
        if comparison is not None:
            require(variant["status"] != "proposed", "Proposed variants retain unperformed status")
            require(baseline["status"] == "tested", "Comparison requires a tested baseline")
            baseline_ids = comparison["baseline_evidence_ids"]
            variant_ids = comparison["variant_evidence_ids"]
            require(set(baseline_ids) <= set(baseline["evidence_ids"]), "Comparison baseline evidence differs from the baseline")
            require(set(variant_ids) <= set(variant["evidence_ids"]), "Comparison evidence differs from the variant")
            require(bool(set(variant_ids) - set(baseline_ids)), "A variant requires new comparison evidence")
            check_ids(baseline_ids, observed=True)
            check_ids(variant_ids, observed=True)
    selection = record["selection"]
    require(set(selection["retained_alternative_ids"]) <= set(names), "Unknown retained alternative")
    selected = selection["selected_variant_id"]
    if selection["decision"] == "variant":
        require(selected in names, "Selected variant identifier is unknown")
        variant = next(item for item in variants if item["id"] == selected)
        require(variant["status"] in ("tested", "retained"), "Selection requires a tested candidate")
        comparison = variant["comparison"]
        require(comparison["criteria_met"] is True, "Selection requires recorded acceptance of the criteria")
        require(comparison["outcome"] != "inconclusive", "An unresolved comparison leaves selection inconclusive")
    else:
        require(selected is None, "Only a variant decision selects a candidate")
    return record


def validate_package(root=ROOT):
    validators = adaptation_validators(root)
    validate_record(root / "examples/adaptive-peer-recovery.json", validators, root)
    contracts = {item["skill_id"]: item for item in load_json(root / "contracts/skill-contracts.json")}
    require(len(contracts) == len(list((root / "skills").glob("*/SKILL.md"))) == 9, "Expected nine skills")
    validate_method_extensions(root, contracts)
    if not validators:
        print("JSON schema checks skipped: install jsonschema for full validation")
    print("Adaptation example, evidence references and method mappings: passed")


if __name__ == "__main__":
    validate_package()
