"""Exercise record structure with synthetic fixtures, without claims of host execution."""

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
from validate_v29 import memory_validators, validate_record


@unittest.skipIf(Draft202012Validator is None, "Install jsonschema for memory schema tests")
class MemoryRecordTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.validators = memory_validators()

    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        shutil.copytree(ROOT / "examples", self.root / "examples")
        self.path = self.root / "examples/salient-peer-failure.json"
        self.checkpoint = self.root / "examples/context-reset-handoff.json"

    def save(self, path, record):
        path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")

    def check(self, path=None, kind="memory"):
        return validate_record(path or self.path, kind, self.validators, self.root)

    def reject(self, path=None, kind="memory"):
        with self.assertRaises((ValueError, ValidationError)):
            self.check(path, kind)

    def operational(self, path):
        record = load_json(path)
        record["record_kind"] = "operational"
        for identifier, reference in record["evidence_refs"].items():
            source_path = path.parent / reference
            source = load_json(source_path)
            source["record_kind"] = "operational"
            source["provenance"]["origin"] = "direct"
            source["observation"] = "Synthetic direct observation for testing record validation."
            source["legacy_status"] = "O"
            self.save(source_path, source)
            record["evidence_hashes"][identifier] = evidence_hash(source)
        self.save(path, record)
        return record

    def test_bundled_records_are_valid(self):
        self.check()
        self.check(self.checkpoint, "checkpoint")

    def test_empty_evidence_is_rejected(self):
        record = load_json(self.path)
        record["evidence_ids"] = []
        self.save(self.path, record)
        self.reject()

    def test_missing_evidence_file_is_rejected(self):
        record = load_json(self.path)
        record["evidence_refs"][record["evidence_ids"][0]] = "missing.json"
        self.save(self.path, record)
        self.reject()

    def test_missing_original_source_is_rejected(self):
        (self.path.parent / "memory-sources/peer-interruption.md").unlink()
        self.reject()

    def test_evidence_changes_invalidate_the_hash(self):
        record = load_json(self.path)
        source_path = self.path.parent / next(iter(record["evidence_refs"].values()))
        source = load_json(source_path)
        source["observation"] = "A different observation"
        self.save(source_path, source)
        self.reject()

    def test_scope_expansion_is_rejected(self):
        record = load_json(self.path)
        record["tested_scope"][record["evidence_ids"][0]]["coverage"] = "All remote tasks"
        self.save(self.path, record)
        self.reject()

    def test_reduced_uncertainty_is_rejected(self):
        record = load_json(self.path)
        record["uncertainty"][record["evidence_ids"][0]]["limitations"] = []
        self.save(self.path, record)
        self.reject()

    def test_high_significance_leaves_observation_unverified(self):
        record = load_json(self.path)
        record["salience"]["level"] = "critical"
        self.save(self.path, record)
        self.assertEqual(self.check()["reliability"], "unverified")
        record["reliability"] = "observed"
        self.save(self.path, record)
        self.reject()

    def test_documentary_source_cannot_establish_observed_reliability(self):
        record = self.operational(self.path)
        record["reliability"] = "observed"
        source_path = self.path.parent / next(iter(record["evidence_refs"].values()))
        source = load_json(source_path)
        source["provenance"]["origin"] = "document"
        source["legacy_status"] = "D"
        self.save(source_path, source)
        record["evidence_hashes"][source["evidence_id"]] = evidence_hash(source)
        self.save(self.path, record)
        self.reject()

    def test_observed_reliability_accepts_synthetic_operational_evidence(self):
        record = self.operational(self.path)
        record["reliability"] = "observed"
        self.save(self.path, record)
        self.check()

    def test_reproduced_reliability_requires_independent_reproduction(self):
        record = self.operational(self.path)
        record["reliability"] = "reproduced"
        self.save(self.path, record)
        self.reject()

    def test_verified_recovery_requires_evidence_ids(self):
        record = load_json(self.checkpoint)
        record["recovery_status"] = "verified"
        self.save(self.checkpoint, record)
        self.reject(self.checkpoint, "checkpoint")

    def test_illustrative_recovery_cannot_be_verified(self):
        record = load_json(self.checkpoint)
        record["recovery_status"] = "verified"
        record["recovery_evidence_ids"] = record["evidence_ids"]
        self.save(self.checkpoint, record)
        self.reject(self.checkpoint, "checkpoint")

    def test_recovery_accepts_synthetic_operational_evidence(self):
        record = self.operational(self.checkpoint)
        record["recovery_status"] = "verified"
        record["recovery_evidence_ids"] = record["evidence_ids"]
        self.save(self.checkpoint, record)
        self.check(self.checkpoint, "checkpoint")

    def test_missing_goal_reference_is_rejected(self):
        record = load_json(self.checkpoint)
        record["goal_ref"] = "missing-goal.md"
        self.save(self.checkpoint, record)
        self.reject(self.checkpoint, "checkpoint")

    def test_unknown_telemetry_requires_unknown_values(self):
        record = load_json(self.checkpoint)
        record["resource_snapshot"]["metrics"]["remaining_tokens"] = 4000
        self.save(self.checkpoint, record)
        self.reject(self.checkpoint, "checkpoint")

    def test_runtime_telemetry_requires_a_retained_source(self):
        record = load_json(self.checkpoint)
        record["resource_snapshot"] = {"source": "runtime", "metrics": {"remaining_seconds": 60}, "captured_at": "Example capture time", "source_ref": "missing-telemetry.json"}
        self.save(self.checkpoint, record)
        self.reject(self.checkpoint, "checkpoint")

    def test_checkpoint_requires_pending_actions_and_authority_context(self):
        original = load_json(self.checkpoint)
        for field in ("pending_actions", "authority_context", "contradictions"):
            with self.subTest(field=field):
                record = deepcopy(original)
                del record[field]
                self.save(self.checkpoint, record)
                self.reject(self.checkpoint, "checkpoint")

    def test_revision_requires_a_new_identifier(self):
        record = load_json(self.path)
        record["revision_refs"] = [self.path.name]
        self.save(self.path, record)
        self.reject()

    def test_new_revision_retains_the_earlier_record(self):
        original = self.path.read_bytes()
        record = load_json(self.path)
        record["event_id"] = "EV-PEER-002"
        record["revision_refs"] = [self.path.name]
        record["revision_status"] = "under_review"
        revision_path = self.path.with_name("revised-event.json")
        self.save(revision_path, record)
        self.check(revision_path)
        self.assertEqual(self.path.read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
