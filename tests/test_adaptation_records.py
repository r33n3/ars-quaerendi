"""Check adaptation invariants with synthetic fixtures, without host execution claims."""

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

from validate_v27 import ROOT, Draft202012Validator, evidence_hash, load_json
from validate_v30 import adaptation_validators, validate_record


@unittest.skipIf(Draft202012Validator is None, "Install jsonschema for adaptation schema tests")
class AdaptationRecordTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.validators = adaptation_validators()

    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        shutil.copytree(ROOT / "examples", self.root / "examples")
        self.path = self.root / "examples/adaptive-peer-recovery.json"

    def save(self, path, record):
        path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")

    def check(self):
        return validate_record(self.path, self.validators, self.root)

    def reject(self):
        with self.assertRaises((ValueError, ValidationError)):
            self.check()

    def comparison_fixture(self, outcome="improvement"):
        record = load_json(self.path)
        record["record_kind"] = "operational"
        record["decision_domain"] = "simulation"
        record["environment_delta"]["status"] = "hypothesis"
        record["environment_delta"]["evidence_ids"] = []
        for field in ("evidence_ids", "evidence_refs", "evidence_hashes", "tested_scope", "uncertainty"):
            record[field] = [] if field == "evidence_ids" else {}
        template = load_json(self.path.parent / "memory-sources/peer-interruption-evidence.json")
        for identifier in ("E-BASELINE", "E-VARIANT"):
            evidence = deepcopy(template)
            evidence.update(record_kind="operational", evidence_id=identifier, legacy_status="O")
            evidence["observation"] = "Synthetic comparison observation for validating record structure."
            evidence["provenance"]["origin"] = "direct"
            evidence["tested_scope"]["domain"] = "simulation"
            relative = f"memory-sources/{identifier}.json"
            self.save(self.path.parent / relative, evidence)
            record["evidence_ids"].append(identifier)
            record["evidence_refs"][identifier] = relative
            record["evidence_hashes"][identifier] = evidence_hash(evidence)
            record["tested_scope"][identifier] = evidence["tested_scope"]
            record["uncertainty"][identifier] = evidence["uncertainty"]
        record["baseline"].update(status="tested", evidence_ids=["E-BASELINE"])
        variant = record["variants"][0]
        variant.update(status="tested", evidence_ids=["E-VARIANT"])
        variant["comparison"] = {
            "baseline_evidence_ids": ["E-BASELINE"],
            "variant_evidence_ids": ["E-VARIANT"],
            "conditions": ["Synthetic shared test conditions"],
            "criteria_met": True,
            "outcome": outcome,
            "summary": "Synthetic scoped comparison for testing validation.",
            "regressions": [],
        }
        record["selection"].update(decision="variant", selected_variant_id=variant["id"])
        self.save(self.path, record)
        return record

    def revise_source(self, record, identifier, change):
        path = self.path.parent / record["evidence_refs"][identifier]
        source = load_json(path)
        change(source)
        self.save(path, source)
        record["evidence_hashes"][identifier] = evidence_hash(source)
        self.save(self.path, record)

    def test_proposed_example_remains_inconclusive(self):
        record = self.check()
        self.assertEqual(record["selection"]["decision"], "inconclusive")
        self.assertTrue(all(item["status"] == "proposed" for item in record["variants"]))

    def test_synthetic_comparison_can_recommend_a_tested_variant(self):
        self.comparison_fixture()
        self.check()

    def test_recovery_result_preserves_its_distinct_outcome(self):
        self.comparison_fixture("recovery")
        record = self.check()
        self.assertEqual(record["variants"][0]["comparison"]["outcome"], "recovery")

    def test_selected_variant_must_exist(self):
        record = self.comparison_fixture()
        record["selection"]["selected_variant_id"] = "V-MISSING"
        self.save(self.path, record)
        self.reject()

    def test_selected_variant_requires_an_identifier(self):
        record = self.comparison_fixture()
        del record["selection"]["selected_variant_id"]
        self.save(self.path, record)
        self.reject()

    def test_proposed_variant_cannot_be_selected(self):
        record = load_json(self.path)
        record["selection"].update(decision="variant", selected_variant_id="V1")
        self.save(self.path, record)
        self.reject()

    def test_tested_variant_requires_comparison(self):
        record = load_json(self.path)
        record["variants"][0]["status"] = "tested"
        self.save(self.path, record)
        self.reject()

    def test_proposed_variant_keeps_its_unperformed_state(self):
        record = self.comparison_fixture()
        record["variants"][0]["status"] = "proposed"
        self.save(self.path, record)
        self.reject()

    def test_selection_requires_recorded_criteria_acceptance(self):
        record = self.comparison_fixture()
        record["variants"][0]["comparison"]["criteria_met"] = False
        self.save(self.path, record)
        self.reject()

    def test_inconclusive_comparison_leaves_selection_unresolved(self):
        self.comparison_fixture("inconclusive")
        self.reject()

    def test_duplicate_variant_identifiers_are_rejected(self):
        record = load_json(self.path)
        record["variants"][1]["id"] = record["variants"][0]["id"]
        self.save(self.path, record)
        self.reject()

    def test_blank_identifiers_and_empty_baseline_are_rejected(self):
        original = load_json(self.path)
        for field, value in (("adaptation_id", " "), ("purpose_ref", ""), ("baseline", {})):
            with self.subTest(field=field):
                record = deepcopy(original)
                record[field] = value
                self.save(self.path, record)
                self.reject()

    def test_missing_evidence_reference_is_rejected(self):
        record = load_json(self.path)
        identifier = record["evidence_ids"][0]
        record["evidence_refs"][identifier] = "missing.json"
        self.save(self.path, record)
        self.reject()

    def test_missing_original_source_is_rejected(self):
        (self.path.parent / "memory-sources/peer-interruption.md").unlink()
        self.reject()

    def test_missing_purpose_reference_is_rejected(self):
        record = load_json(self.path)
        record["purpose_ref"] = "missing-purpose.md"
        self.save(self.path, record)
        self.reject()

    def test_reference_outside_package_is_rejected(self):
        record = load_json(self.path)
        record["purpose_ref"] = "../../outside.md"
        self.save(self.path, record)
        self.reject()

    def test_evidence_hash_changes_are_rejected(self):
        record = load_json(self.path)
        path = self.path.parent / next(iter(record["evidence_refs"].values()))
        source = load_json(path)
        source["observation"] = "Changed content"
        self.save(path, source)
        self.reject()

    def test_scope_and_uncertainty_snapshots_remain_unchanged(self):
        original = load_json(self.path)
        identifier = original["evidence_ids"][0]
        for field, key, value in (("tested_scope", "coverage", "All tasks"), ("uncertainty", "limitations", [])):
            with self.subTest(field=field):
                record = deepcopy(original)
                record[field][identifier][key] = value
                self.save(self.path, record)
                self.reject()

    def test_documentary_evidence_cannot_establish_tested_results(self):
        record = self.comparison_fixture()
        def change(source):
            source["provenance"]["origin"] = "document"
            source["legacy_status"] = "D"
        self.revise_source(record, "E-VARIANT", change)
        self.reject()

    def test_illustrative_record_cannot_establish_tested_results(self):
        record = self.comparison_fixture()
        record["record_kind"] = "illustrative"
        self.save(self.path, record)
        self.reject()

    def test_simulation_results_keep_their_domain(self):
        record = self.comparison_fixture()
        record["decision_domain"] = "real_world"
        self.save(self.path, record)
        self.reject()

    def test_variant_requires_new_evidence(self):
        record = self.comparison_fixture()
        variant = record["variants"][0]
        variant["evidence_ids"] = ["E-BASELINE"]
        variant["comparison"]["variant_evidence_ids"] = ["E-BASELINE"]
        self.save(self.path, record)
        self.reject()

    def test_comparison_must_reference_its_baseline_and_candidate(self):
        record = self.comparison_fixture()
        record["variants"][0]["comparison"]["variant_evidence_ids"] = ["E-BASELINE"]
        self.save(self.path, record)
        self.reject()

    def test_unknown_retained_alternative_is_rejected(self):
        record = load_json(self.path)
        record["selection"]["retained_alternative_ids"].append("V-MISSING")
        self.save(self.path, record)
        self.reject()

    def test_unrelated_claim_evidence_is_rejected(self):
        record = self.comparison_fixture()
        self.revise_source(record, "E-VARIANT", lambda source: source.update(claim_id="OTHER-CLAIM"))
        self.reject()

    def test_hold_decision_leaves_selected_identifier_empty(self):
        record = self.comparison_fixture()
        record["selection"]["decision"] = "hold"
        self.save(self.path, record)
        self.reject()


if __name__ == "__main__":
    unittest.main()
