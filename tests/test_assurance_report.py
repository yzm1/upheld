"""Tests for the schema 0.2 intended-versus-actual assurance report."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import assurance_report


def obligation(plan=True, defense=None, accepted_gaps=None):
    plans = []
    selected = None
    status = "unknown"
    if plan:
        status = "reviewed"
        selected = "P1"
        plans = [{
            "id": "P1",
            "obligation_id": "O1",
            "preference": "preferred",
            "portfolio_logic": "all_required",
            "objective": "Prevent invalid state",
            "constraints_considered": [],
            "members": [{
                "id": "M1",
                "guarded_by": "test",
                "intended_scope": "src/x.py",
                "rationale": "Exercise the public boundary",
                "bypass_paths": [],
                "fault_challenge": "Seed one invalid boundary value",
                "needs_environment": [],
                "residual_uncertainty": [],
            }],
            "tradeoffs": [],
            "residual_uncertainty": [],
        }]
    defenses = [] if defense is None else [defense]
    return {
        "id": "O1",
        "text": "Invalid values are rejected.",
        "subject_scope": "src/x.py",
        "source": "docs/spec.md",
        "origin": "authored",
        "confidence": "verified",
        "why": "Invalid values would corrupt state.",
        "falsifier": "An invalid value is accepted.",
        "reachability": "live",
        "constraints": {"objectives": [], "hard_limits": [], "environment": [], "consequence": "corrupt state"},
        "recommended_assurance": {"status": status, "selected_plan_id": selected, "plans": plans},
        "actual_defenses": defenses,
        "accepted_gaps": accepted_gaps or [],
    }


def register(ob):
    return {
        "schema_version": "0.2",
        "producer": {"name": "test", "mode": "authored", "inputs": [], "source_rev": "abc"},
        "obligations": [ob],
    }


def defense(state="present", mapped=True):
    return {
        "id": "D1",
        "obligation_id": "O1",
        "guarded_by": "test",
        "artifact_locator": "tests/test_x.py",
        "subject_scope": "src/x.py",
        "why_this_kind": "Executable boundary check",
        "needs_environment": [],
        "implementation_state": state,
        "recommendation_member_ids": ["M1"] if mapped else [],
    }


class AssuranceReportTests(unittest.TestCase):
    def build(self, ob, bindings=None, evidence=None):
        return assurance_report.build_report(
            register(ob), "fixture.json", bindings or {}, evidence or {}, "2026-09-09T00:00:00Z"
        )

    def test_missing_plan_is_visible(self):
        report = self.build(obligation(plan=False))
        self.assertEqual(report["obligations"][0]["gaps"][0]["kind"], "no_plan")

    def test_missing_defense_is_visible(self):
        report = self.build(obligation())
        self.assertEqual(report["obligations"][0]["gaps"][0]["kind"], "no_defense")

    def test_partial_defense_is_weaker_than_plan(self):
        report = self.build(obligation(defense=defense("partial")))
        self.assertEqual(report["obligations"][0]["gaps"][0]["kind"], "weaker_than_recommended")

    def test_present_but_unbound_defense_is_unproven(self):
        report = self.build(obligation(defense=defense()))
        self.assertEqual(report["obligations"][0]["gaps"][0]["kind"], "unproven_defense")

    def test_bound_supporting_evidence_closes_member_gap(self):
        record = {"evidence_id": "E1", "defense_id": "D1", "verdict": "supports"}
        report = self.build(obligation(defense=defense()), {"D1": "E1"}, {"E1": record})
        self.assertEqual(report["obligations"][0]["gap_state"], "clean")

    def test_unmapped_present_defense_is_a_review_gap(self):
        report = self.build(obligation(defense=defense(mapped=False)))
        kinds = {gap["kind"] for gap in report["obligations"][0]["gaps"]}
        self.assertIn("no_defense", kinds)
        self.assertIn("divergence_unreviewed", kinds)

    def test_cross_reference_errors_fail(self):
        bad = defense()
        bad["recommendation_member_ids"] = ["MISSING"]
        with self.assertRaises(ValueError):
            self.build(obligation(defense=bad))


if __name__ == "__main__":
    unittest.main()
