"""Check bundled contracts and handoff records. Optional schema checks use jsonschema."""

import argparse
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

try:
    from jsonschema import Draft202012Validator
except ImportError:
    Draft202012Validator = None


ROOT = Path(__file__).resolve().parents[1]


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def evidence_hash(record):
    content = json.dumps(record, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def render_contract(contract):
    def joined(items):
        if not items:
            return "Additional context is optional."
        return "; ".join(item.rstrip(".") for item in items) + "."

    rows = [
        ("Activation", contract["activation"]),
        ("Routine handling", contract["non_activation"]),
        ("Required inputs", joined(contract["inputs"]["required"])),
        ("Helpful context", joined(contract["inputs"]["helpful"])),
        ("Missing inputs", contract["inputs"]["missing_behavior"]),
        ("Evidence produced", joined(contract["outputs"]["evidence"])),
        ("Records produced", joined(contract["outputs"]["records"])),
        ("Recommendations", joined(contract["recommendations"])),
        ("Authority", contract["authority"]),
        ("Stop when", joined(contract["stopping"])),
        ("Outcome status", ", ".join(f"`{item}`" for item in contract["outcome_statuses"]) + "."),
        ("Reopen when", joined(contract["revision_triggers"])),
        ("Possible consumers", ", ".join(f"`{item}`" for item in contract["consumers"]) + "."),
        ("Failure handling", contract["failure_behavior"]),
    ]
    if contract.get("optional_methods"):
        rows.append(("Optional methods", ", ".join(f"`{item}`" for item in contract["optional_methods"]) + "."))
    heading = "## Method contract\n\n"
    reference = (
        "This section matches the [shared contract registry](../../contracts/skill-contracts.json). "
        "See [evidence and handoff rules](../../references/evidence-handoff-rules.md) "
        "when another skill needs the result.\n"
    )
    return heading + reference + "\n" + "\n".join(f"* **{label}:** {value}" for label, value in rows) + "\n"


def check_contract_text(path, contract):
    text = path.read_text(encoding="utf-8")
    marker = "## Method contract\n"
    require(text.count(marker) == 1, f"Expected one method contract in {path}")
    actual = re.search(r"^## Method contract\n.*?(?=^## |\Z)", text, re.M | re.S).group().strip()
    require(actual == render_contract(contract).strip(), f"Contract text differs from registry: {path}")


def sync_contract_text(text, contract):
    pattern = r"^## (?:v2\.7 )?Method [Cc]ontract\n.*?(?=^## |\Z)"
    matches = list(re.finditer(pattern, text, re.M | re.S))
    require(len(matches) <= 1, "Multiple method contract sections need manual review")
    if not matches:
        return text.rstrip() + "\n\n" + render_contract(contract)
    match = matches[0]
    suffix = text[match.end():]
    separator = "\n" if suffix else ""
    return text[:match.start()] + render_contract(contract) + separator + suffix


def local_reference(base, reference, root):
    require(not urlsplit(reference).scheme, f"Expected a local reference: {reference}")
    path = (base / reference).resolve()
    require(path.is_relative_to(root.resolve()), f"Reference leaves the package: {reference}")
    require(path.is_file(), f"Missing reference: {path}")
    return path


def make_validators(root):
    paths = {
        "contract": "contracts/skill-contract.schema.json",
        "evidence": "schemas/evidence-record.schema.json",
        "handoff": "schemas/handoff.schema.json",
    }
    schemas = {key: load_json(root / path) for key, path in paths.items()}
    if Draft202012Validator is None:
        return {}
    validators = {}
    for key, schema in schemas.items():
        Draft202012Validator.check_schema(schema)
        validators[key] = Draft202012Validator(schema)
    return validators


def validate_method_extensions(root, contracts):
    combined = {skill: [] for skill in contracts}
    all_ids = []
    for version, filename in (("2.8", "v28-method-extensions.json"), ("2.9", "v29-method-extensions.json")):
        index = load_json(root / "contracts" / filename)
        require(set(index) == {"version", "optional_methods", "method_references", "experimental_opt_in_methods", "global_invariants"}, "Unexpected optional method index fields")
        require(index["version"] == version, "Unknown optional method index version")
        methods = index["optional_methods"]
        require(isinstance(methods, dict) and set(methods) <= set(contracts), "Unknown optional method owner")
        identifiers = []
        for skill, owned in methods.items():
            require(isinstance(owned, list) and bool(owned) and all(isinstance(item, str) and item.strip() for item in owned), "Invalid optional method identifiers")
            combined[skill].extend(owned)
            identifiers.extend(owned)
        require(set(index["method_references"]) == set(identifiers), "Optional method references differ from identifiers")
        for reference in index["method_references"].values():
            local_reference(root, reference, root)
        opt_in = index["experimental_opt_in_methods"]
        require(isinstance(opt_in, list) and len(opt_in) == len(set(opt_in)), "Invalid experimental selection list")
        expected = {"optional-archetypal-lenses", "evidence-linked-narrative-representation"} if version == "2.8" else set()
        require(set(opt_in) == expected, "Experimental selection differs from declared method requirements")
        require(set(opt_in) <= set(identifiers), "Unknown experimental method")
        invariants = index["global_invariants"]
        require(isinstance(invariants, list) and bool(invariants) and all(isinstance(item, str) and item.strip() for item in invariants), "Missing method invariants")
        all_ids.extend(identifiers)
    require(len(all_ids) == len(set(all_ids)), "Optional method identifier reused")
    for skill, contract in contracts.items():
        require(contract.get("optional_methods", []) == combined[skill], "Optional methods differ from the contract registry")


def validate_chain(directory, contracts, validators, root=ROOT, registry=None):
    registry = {} if registry is None else registry
    files = sorted(directory.glob("handoff-*.json"))
    require(len(files) >= 2, f"Expected at least two handoffs in {directory}")
    previous = None
    previous_level = None
    handoff_ids = set()
    for path in files:
        handoff = load_json(path)
        if validators:
            validators["handoff"].validate(handoff)
        for reference in handoff.get("related_artifacts", []):
            local_reference(path.parent, reference, root)
        require(handoff["handoff_id"] not in handoff_ids, "Duplicate handoff identifier")
        handoff_ids.add(handoff["handoff_id"])
        source = handoff["from_skill"]
        target = handoff["to_skill"]
        require(source in contracts and target in contracts, "Unknown skill in handoff")
        require(target in contracts[source]["consumers"], "Destination is outside the source contract's consumers")
        ids = handoff["evidence_ids"]
        require(len(ids) == len(set(ids)), "Duplicate evidence identifier")
        expected_ids = set(ids)
        for field in ("evidence_refs", "evidence_hashes", "scope", "uncertainty"):
            require(set(handoff[field]) == expected_ids, f"Evidence keys differ in {field}")
        records = {}
        for evidence_id in ids:
            record_path = local_reference(path.parent, handoff["evidence_refs"][evidence_id], root)
            record = load_json(record_path)
            if validators:
                validators["evidence"].validate(record)
            require(record["evidence_id"] == evidence_id, "Referenced evidence identifier differs")
            require(record["claim_id"] == handoff["claim_id"], "Claim identifier differs from evidence")
            fingerprint = evidence_hash(record)
            require(handoff["evidence_hashes"][evidence_id] == fingerprint, "Evidence content hash differs")
            require(registry.get(evidence_id, fingerprint) == fingerprint, "Evidence identifier was reused for changed content")
            registry[evidence_id] = fingerprint
            require(handoff["scope"][evidence_id] == record["tested_scope"], "Tested scope differs from evidence")
            require(handoff["uncertainty"][evidence_id] == record["uncertainty"], "Uncertainty differs from evidence")
            source_ref = record["provenance"]["source"]
            if urlsplit(source_ref).scheme not in ("https", "http") and record["provenance"]["origin"] != "unknown":
                local_reference(record_path.parent, source_ref, root)
            records[evidence_id] = record
        new_ids = expected_ids
        if previous:
            require(previous["to_skill"] == source, "Handoff chain is disconnected")
            require(previous["claim_id"] == handoff["claim_id"], "Claim changed within the chain")
            require(previous["authority"] == handoff["authority"], "Authority context changed within the chain")
            require(previous.get("decision_domain") == handoff.get("decision_domain"), "Decision domain changed within the chain")
            previous_ids = set(previous["evidence_ids"])
            require(previous_ids <= expected_ids, "Earlier evidence was removed from the handoff")
            new_ids = expected_ids - previous_ids
            if new_ids:
                require(bool(handoff.get("change_basis", "").strip()), "Added evidence needs a recorded change basis")
        level = handoff.get("judgment_level")
        if previous_level:
            require(level is not None, "Earlier judgment level was omitted")
        if level and level != previous_level:
            require(source == "judgment", "A new assessment must come from Judgment")
            if previous_level and int(level[1:]) > int(previous_level[1:]):
                require(bool(new_ids), "Judgment level increased without new evidence")
        if level in ("J3", "J4"):
            verification_ids = handoff.get("verification_evidence_ids", [])
            require(bool(verification_ids), "Verification needs supporting evidence records")
            if previous_level and int(level[1:]) > int(previous_level[1:]):
                require(bool(set(verification_ids) & new_ids), "Verification increased without a new verification record")
            for evidence_id in verification_ids:
                require(evidence_id in records, "Verification evidence is outside this handoff")
                record = records[evidence_id]
                require(record["record_kind"] == "operational", "Illustrative records cannot establish actual verification")
                require(record["provenance"]["origin"] in ("direct", "independent_reproduction"), "Reported material cannot establish direct verification")
                domain = record["tested_scope"].get("domain")
                require(domain in ("real_world", "software", "simulation"), "Verification requires an explicit observed domain")
                require(domain == handoff.get("decision_domain"), "Verification evidence is outside the decision domain")
        if level == "J4":
            local_reference(path.parent, handoff["qualification_ref"], root)
        previous_level = level
        previous = handoff
    return len(files), handoff_ids


def validate_package(root=ROOT, sync_contracts=False):
    validators = make_validators(root)
    items = load_json(root / "contracts/skill-contracts.json")
    contracts = {item["skill_id"]: item for item in items}
    names = {path.parent.name for path in (root / "skills").glob("*/SKILL.md")}
    require(len(items) == len(contracts) == len(names) == 9, "Expected nine unique skill contracts")
    require(set(contracts) == names, "Contract registry differs from installed skill identifiers")
    for contract in items:
        if validators:
            validators["contract"].validate(contract)
        require(set(contract["consumers"]) <= names, "Unknown contract consumer")
        render_contract(contract)
    validate_method_extensions(root, contracts)
    for contract in items:
        path = root / "skills" / contract["skill_id"] / "SKILL.md"
        if sync_contracts:
            text = path.read_text(encoding="utf-8")
            path.write_text(sync_contract_text(text, contract), encoding="utf-8", newline="\n")
        check_contract_text(path, contract)
    registry = {}
    seen_handoffs = set()
    count = 0
    directories = sorted(path for path in (root / "examples/complete-handoffs").iterdir() if path.is_dir())
    expected = {"research-review-reuse", "offer-review-planning", "pattern-investigation-review-reuse", "model-experiment-review-reuse"}
    require(expected <= {path.name for path in directories}, "Missing bundled handoff walkthrough")
    for directory in directories:
        size, identifiers = validate_chain(directory, contracts, validators, root, registry)
        require(not seen_handoffs.intersection(identifiers), "Handoff identifier reused across walkthroughs")
        seen_handoffs.update(identifiers)
        count += size
    if not validators:
        print("JSON schema checks skipped: install jsonschema for full validation")
    print(f"Contracts and handoff structure: {len(contracts)} skills, {len(directories)} walkthroughs, {count} handoffs passed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sync-contracts", action="store_true", help="Update skill contract sections from the JSON registry")
    arguments = parser.parse_args()
    validate_package(sync_contracts=arguments.sync_contracts)
