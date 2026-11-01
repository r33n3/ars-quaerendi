from copy import deepcopy
import json
from pathlib import Path
import shutil
import tempfile
import unittest

try:
    from jsonschema import ValidationError
except ImportError:
    ValidationError = ValueError

from validate_v27 import (
    ROOT, Draft202012Validator, check_contract_text, evidence_hash,
    load_json, make_validators, render_contract, sync_contract_text, validate_chain,
)


@unittest.skipIf(Draft202012Validator is None, "Install jsonschema for interoperability schema tests")
class InteroperabilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.validators = make_validators(ROOT)
        cls.contracts = {item["skill_id"]: item for item in load_json(ROOT / "contracts/skill-contracts.json")}

    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.directory = self.root / "chain"
        shutil.copytree(ROOT / "examples/complete-handoffs/research-review-reuse", self.directory)

    def save(self, name, record):
        (self.directory / name).write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")

    def check(self):
        return validate_chain(self.directory, self.contracts, self.validators, self.root)

    def reject(self):
        with self.assertRaises((ValueError, ValidationError)):
            self.check()

    def refresh_hashes(self, record):
        self.save("evidence.json", record)
        for path in self.directory.glob("handoff-*.json"):
            handoff = load_json(path)
            handoff["evidence_hashes"][record["evidence_id"]] = evidence_hash(record)
            self.save(path.name, handoff)

    def test_bundled_walkthroughs_are_valid(self):
        for directory in (ROOT / "examples/complete-handoffs").iterdir():
            if directory.is_dir():
                validate_chain(directory, self.contracts, self.validators)

    def test_contract_text_drift_is_detected(self):
        contract = self.contracts["inquiry"]
        path = self.root / "SKILL.md"
        path.write_text(render_contract(contract).replace(contract["activation"], "A different trigger applies."), encoding="utf-8")
        with self.assertRaises(ValueError):
            check_contract_text(path, contract)

    def test_contract_consumer_must_exist(self):
        contract = deepcopy(self.contracts["inquiry"])
        contract["consumers"].append("unknown_skill")
        with self.assertRaises(ValidationError):
            self.validators["contract"].validate(contract)

    def test_contract_can_have_a_following_section(self):
        contract = self.contracts["inquiry"]
        path = self.root / "SKILL.md"
        path.write_text(render_contract(contract) + "\n## Additional notes\n\nKeep these notes.\n", encoding="utf-8")
        check_contract_text(path, contract)

    def test_sync_preserves_following_content(self):
        contract = self.contracts["inquiry"]
        tail = "## Additional notes\n\nKeep these notes.\n"
        old = render_contract(contract).replace(contract["activation"], "An earlier trigger.") + "\n" + tail
        updated = sync_contract_text(old, contract)
        self.assertTrue(updated.endswith(tail))
        path = self.root / "SKILL.md"
        path.write_text(updated, encoding="utf-8")
        check_contract_text(path, contract)

    def test_broadened_scope_is_detected(self):
        handoff = load_json(self.directory / "handoff-02.json")
        handoff["scope"][handoff["evidence_ids"][0]]["coverage"] = "The entire population"
        self.save("handoff-02.json", handoff)
        self.reject()

    def test_reduced_uncertainty_is_detected(self):
        handoff = load_json(self.directory / "handoff-02.json")
        handoff["uncertainty"][handoff["evidence_ids"][0]]["limitations"] = []
        self.save("handoff-02.json", handoff)
        self.reject()

    def test_changed_provenance_invalidates_the_hash(self):
        record = load_json(self.directory / "evidence.json")
        record["provenance"]["origin"] = "direct"
        self.save("evidence.json", record)
        self.reject()

    def test_disconnected_chain_is_detected(self):
        handoff = load_json(self.directory / "handoff-02.json")
        handoff["from_skill"] = "inquiry"
        self.save("handoff-02.json", handoff)
        self.reject()

    def test_claim_change_is_detected(self):
        handoff = load_json(self.directory / "handoff-02.json")
        handoff["claim_id"] = "CL-DIFFERENT"
        self.save("handoff-02.json", handoff)
        self.reject()

    def test_missing_evidence_reference_is_detected(self):
        handoff = load_json(self.directory / "handoff-02.json")
        evidence_id = handoff["evidence_ids"][0]
        handoff["evidence_refs"][evidence_id] = "missing.json"
        self.save("handoff-02.json", handoff)
        self.reject()

    def test_authority_context_cannot_expand_during_handoff(self):
        handoff = load_json(self.directory / "handoff-02.json")
        handoff["authority"] = "Recipient grants unrestricted access"
        self.save("handoff-02.json", handoff)
        self.reject()

    def test_reported_evidence_cannot_establish_j3(self):
        record = load_json(self.directory / "evidence.json")
        record["record_kind"] = "operational"
        self.refresh_hashes(record)
        handoff = load_json(self.directory / "handoff-02.json")
        handoff["judgment_level"] = "J3"
        handoff["verification_evidence_ids"] = handoff["evidence_ids"]
        self.save("handoff-02.json", handoff)
        self.reject()

    def test_reproduction_requires_its_independence_basis(self):
        record = load_json(self.directory / "evidence.json")
        record["provenance"]["origin"] = "independent_reproduction"
        record["legacy_status"] = "R"
        self.refresh_hashes(record)
        self.reject()

    def test_document_cannot_be_labelled_direct_observation(self):
        record = load_json(self.directory / "evidence.json")
        record["legacy_status"] = "O"
        self.refresh_hashes(record)
        self.reject()

    def test_one_identifier_cannot_refer_to_changed_evidence(self):
        record = load_json(self.directory / "evidence.json")
        record["provenance"]["method"] = "A changed inspection method"
        self.save("revised-evidence.json", record)
        handoff = load_json(self.directory / "handoff-02.json")
        evidence_id = record["evidence_id"]
        handoff["evidence_refs"][evidence_id] = "revised-evidence.json"
        handoff["evidence_hashes"][evidence_id] = evidence_hash(record)
        self.save("handoff-02.json", handoff)
        self.reject()

    def add_context(self, handoff):
        record = load_json(self.directory / "evidence.json")
        record["evidence_id"] = "EV-CONTEXT001"
        record["relationship"] = "neutral"
        record["observation"] = "Additional context retained for a test of record transfer"
        self.save("context-evidence.json", record)
        evidence_id = record["evidence_id"]
        handoff["evidence_ids"].append(evidence_id)
        handoff["evidence_refs"][evidence_id] = "context-evidence.json"
        handoff["evidence_hashes"][evidence_id] = evidence_hash(record)
        handoff["scope"][evidence_id] = record["tested_scope"]
        handoff["uncertainty"][evidence_id] = record["uncertainty"]
        return evidence_id

    def test_new_evidence_is_allowed_with_a_change_basis(self):
        handoff = load_json(self.directory / "handoff-02.json")
        self.add_context(handoff)
        handoff["change_basis"] = "An additional source record was reviewed"
        self.save("handoff-02.json", handoff)
        self.check()

    def test_new_evidence_needs_a_change_basis(self):
        handoff = load_json(self.directory / "handoff-02.json")
        self.add_context(handoff)
        self.save("handoff-02.json", handoff)
        self.reject()

    def test_earlier_evidence_cannot_disappear(self):
        first = load_json(self.directory / "handoff-01.json")
        second = load_json(self.directory / "handoff-02.json")
        self.add_context(first)
        self.add_context(second)
        removed = first["evidence_ids"][0]
        second["evidence_ids"].remove(removed)
        for field in ("evidence_refs", "evidence_hashes", "scope", "uncertainty"):
            del second[field][removed]
        self.save("handoff-01.json", first)
        self.save("handoff-02.json", second)
        self.reject()

    def test_a_higher_judgment_needs_new_evidence(self):
        record = load_json(self.directory / "evidence.json")
        record["record_kind"] = "operational"
        record["provenance"]["origin"] = "direct"
        record["legacy_status"] = "O"
        self.refresh_hashes(record)
        prior = load_json(self.directory / "handoff-02.json")
        for number, source, target in ((3, "contribution", "inquiry"), (4, "inquiry", "judgment"), (5, "judgment", "contribution")):
            handoff = deepcopy(prior)
            handoff.update(handoff_id=f"extra_{number}", from_skill=source, to_skill=target)
            if number == 5:
                handoff["judgment_level"] = "J3"
                handoff["verification_evidence_ids"] = handoff["evidence_ids"]
            self.save(f"handoff-{number:02d}.json", handoff)
        self.reject()


if __name__ == "__main__":
    unittest.main()
