from copy import deepcopy
import json
from pathlib import Path
import unittest

try:
    import jsonschema
except ImportError:
    jsonschema = None


ROOT = Path(__file__).resolve().parents[1]


@unittest.skipIf(jsonschema is None, "Install jsonschema to validate goal records")
class GoalProposalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        schema = json.loads((ROOT / "schemas/goal-proposal.schema.json").read_text(encoding="utf-8"))
        jsonschema.Draft202012Validator.check_schema(schema)
        cls.validator = jsonschema.Draft202012Validator(schema)
        cls.proposal = json.loads((ROOT / "examples/purpose-to-action-goal.json").read_text(encoding="utf-8"))
        cls.no_goal = json.loads((ROOT / "examples/purpose-to-action-no-goal.json").read_text(encoding="utf-8"))

    def test_hypothetical_proposal_with_unknown_authorization(self):
        self.validator.validate(self.proposal)

    def test_keep_existing_goals_with_null_goal_fields(self):
        self.validator.validate(self.no_goal)

    def test_existing_authorization_requires_its_basis(self):
        record = deepcopy(self.proposal)
        record["authorization_status"] = "within_existing_scope"
        with self.assertRaises(jsonschema.ValidationError):
            self.validator.validate(record)
        record["authorization_basis"] = "Invented user instruction permits this local review for 30 minutes"
        self.validator.validate(record)

    def test_observation_needs_an_evidence_reference(self):
        record = deepcopy(self.proposal)
        record["evidence_status"] = "O"
        record["evidence_refs"] = []
        with self.assertRaises(jsonschema.ValidationError):
            self.validator.validate(record)

    def test_unknown_evidence_can_have_an_empty_reference_list(self):
        record = deepcopy(self.proposal)
        record["evidence_status"] = "U"
        record["evidence_refs"] = []
        self.validator.validate(record)

    def test_new_proposal_needs_a_resource_limit(self):
        record = deepcopy(self.proposal)
        del record["resource_limit"]
        with self.assertRaises(jsonschema.ValidationError):
            self.validator.validate(record)

    def test_new_proposal_needs_a_nonempty_goal(self):
        record = deepcopy(self.proposal)
        record["goal"] = ""
        with self.assertRaises(jsonschema.ValidationError):
            self.validator.validate(record)

    def test_current_goals_decision_cannot_add_a_new_goal(self):
        record = deepcopy(self.no_goal)
        record["goal"] = "Build a new helper"
        with self.assertRaises(jsonschema.ValidationError):
            self.validator.validate(record)

    def test_current_goals_decision_cannot_add_development(self):
        record = deepcopy(self.no_goal)
        record["proposed_improvement"] = "Train a model"
        with self.assertRaises(jsonschema.ValidationError):
            self.validator.validate(record)

    def test_prohibited_goal_requires_rejection_or_unchanged_goals(self):
        record = deepcopy(self.proposal)
        record["authorization_status"] = "prohibited"
        with self.assertRaises(jsonschema.ValidationError):
            self.validator.validate(record)
        record["decision"] = "reject"
        self.validator.validate(record)

    def test_development_needs_a_gap_and_a_proposed_change(self):
        record = deepcopy(self.proposal)
        record["goal_type"] = "developmental"
        self.validator.validate(record)
        record["capability_gap"] = None
        with self.assertRaises(jsonschema.ValidationError):
            self.validator.validate(record)


if __name__ == "__main__":
    unittest.main()
