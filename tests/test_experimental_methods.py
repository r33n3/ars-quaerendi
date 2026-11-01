"""Structural checks using synthetic records, with no actual experiment claims."""

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
    ROOT, Draft202012Validator, evidence_hash, load_json, make_validators,
    validate_chain, validate_method_extensions,
)


@unittest.skipIf(Draft202012Validator is None, "Install jsonschema for experimental method schema tests")
class ExperimentalMethodTests(unittest.TestCase):
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

    def save(self, path, data):
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    def check(self):
        validate_chain(self.directory, self.contracts, self.validators, self.root)

    def reject(self):
        with self.assertRaises((ValueError, ValidationError)):
            self.check()

    def set_domain(self, evidence_domain, decision_domain=None, verification=False):
        record = load_json(self.directory / "evidence.json")
        record["schema_version"] = "1.1"
        record["tested_scope"]["domain"] = evidence_domain
        if verification:
            record["record_kind"] = "operational"
            record["provenance"]["origin"] = "direct"
            record["legacy_status"] = "O"
        self.save(self.directory / "evidence.json", record)
        for path in self.directory.glob("handoff-*.json"):
            handoff = load_json(path)
            handoff["schema_version"] = "1.1"
            handoff["decision_domain"] = decision_domain or evidence_domain
            handoff["scope"][record["evidence_id"]] = record["tested_scope"]
            handoff["evidence_hashes"][record["evidence_id"]] = evidence_hash(record)
            if verification and handoff["from_skill"] == "judgment":
                handoff["judgment_level"] = "J3"
                handoff["verification_evidence_ids"] = handoff["evidence_ids"]
            self.save(path, handoff)

    def test_legacy_walkthrough_remains_readable(self):
        self.check()

    def test_new_walkthrough_keeps_proposed_plan_separate(self):
        directory = ROOT / "examples/complete-handoffs/model-experiment-review-reuse"
        validate_chain(directory, self.contracts, self.validators)
        for path in directory.glob("handoff-*.json"):
            handoff = load_json(path)
            self.assertEqual(handoff["evidence_ids"], ["E-101"])
            self.assertIn("experiment-plan.md", handoff["related_artifacts"])
            self.assertNotIn("verification_evidence_ids", handoff)

    def test_verification_can_remain_within_observed_domains(self):
        for domain in ("software", "simulation", "real_world"):
            with self.subTest(domain=domain):
                self.set_domain(domain, verification=True)
                self.check()

    def test_simulation_cannot_verify_another_domain(self):
        for domain in ("real_world", "software"):
            with self.subTest(domain=domain):
                self.set_domain("simulation", domain, verification=True)
                self.reject()

    def test_conceptual_and_unknown_domains_leave_verification_unresolved(self):
        for domain in ("conceptual", "unknown"):
            with self.subTest(domain=domain):
                self.set_domain(domain, verification=True)
                self.reject()

    def test_new_evidence_schema_requires_a_domain(self):
        record = load_json(self.directory / "evidence.json")
        record["schema_version"] = "1.1"
        with self.assertRaises(ValidationError):
            self.validators["evidence"].validate(record)

    def test_new_handoff_schema_requires_decision_domain(self):
        self.set_domain("software")
        handoff = load_json(self.directory / "handoff-02.json")
        del handoff["decision_domain"]
        self.save(self.directory / "handoff-02.json", handoff)
        self.reject()

    def test_domain_survives_scope_snapshot(self):
        self.set_domain("software")
        handoff = load_json(self.directory / "handoff-02.json")
        handoff["scope"][handoff["evidence_ids"][0]]["domain"] = "real_world"
        self.save(self.directory / "handoff-02.json", handoff)
        self.reject()

    def test_decision_domain_survives_chain(self):
        self.set_domain("simulation")
        handoff = load_json(self.directory / "handoff-02.json")
        handoff["decision_domain"] = "real_world"
        self.save(self.directory / "handoff-02.json", handoff)
        self.reject()

    def test_legacy_missing_domain_cannot_establish_verification(self):
        self.set_domain("software", verification=True)
        record = load_json(self.directory / "evidence.json")
        record["schema_version"] = "1.0"
        del record["tested_scope"]["domain"]
        self.save(self.directory / "evidence.json", record)
        for path in self.directory.glob("handoff-*.json"):
            handoff = load_json(path)
            handoff["schema_version"] = "1.0"
            del handoff["decision_domain"]
            handoff["scope"][record["evidence_id"]] = record["tested_scope"]
            handoff["evidence_hashes"][record["evidence_id"]] = evidence_hash(record)
            self.save(path, handoff)
        self.reject()

    def test_illustration_retains_verification_limit_even_with_a_domain(self):
        self.set_domain("simulation", verification=True)
        record = load_json(self.directory / "evidence.json")
        record["record_kind"] = "illustrative"
        self.save(self.directory / "evidence.json", record)
        for path in self.directory.glob("handoff-*.json"):
            handoff = load_json(path)
            handoff["evidence_hashes"][record["evidence_id"]] = evidence_hash(record)
            self.save(path, handoff)
        self.reject()

    def test_missing_plan_reference_is_detected(self):
        handoff = load_json(self.directory / "handoff-01.json")
        handoff["related_artifacts"] = ["missing-plan.md"]
        self.save(self.directory / "handoff-01.json", handoff)
        self.reject()

    def test_method_index_matches_contracts(self):
        validate_method_extensions(ROOT, self.contracts)

    def test_method_ownership_drift_is_detected(self):
        contracts = deepcopy(self.contracts)
        contracts["discovery"]["optional_methods"] = []
        with self.assertRaises(ValueError):
            validate_method_extensions(ROOT, contracts)

    def test_missing_reference_and_experimental_selection_are_detected(self):
        for folder in ("contracts", "references"):
            shutil.copytree(ROOT / folder, self.root / folder)
        path = self.root / "contracts/v28-method-extensions.json"
        original = load_json(path)
        for field, value in (("method_references", {**original["method_references"], "scientific-model-formation": "missing.md"}), ("experimental_opt_in_methods", [])):
            with self.subTest(field=field):
                changed = deepcopy(original)
                changed[field] = value
                self.save(path, changed)
                with self.assertRaises(ValueError):
                    validate_method_extensions(self.root, self.contracts)


if __name__ == "__main__":
    unittest.main()
