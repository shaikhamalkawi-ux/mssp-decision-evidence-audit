"""Deterministic specification tests, NOT independent company validation."""
import json
import unittest
from pathlib import Path
from src.evidence_protocol import (
    IDENTIFIED, CONFLICT, NOT_IDENTIFIED, OUTCOME_ABSENT,
    classify_joint_assertions, classify_admissible_alternatives,
    operational_outcome_state, strict_component_status,
    weighted_score_winners, additive_group_nullity, distinct_allocations_same_total,
)
ROOT = Path(__file__).resolve().parents[1]
D = json.loads((ROOT / 'evidence/anonymized_derived_evidence.json').read_text())
W = json.loads((ROOT / 'evidence/package_label_witness_v8.json').read_text())


def record(value, **changes):
    return {"claim_definition": "same declared capability universe",
            "claim_unit": "detailed row count", "source_version": "Draft-3",
            "observation_time": "planning", "value": value, **changes}


class TestProtocol(unittest.TestCase):
    def test_identified_joint(self): self.assertEqual(classify_joint_assertions([record(51), record(51)]), IDENTIFIED)
    def test_conflicting_joint(self): self.assertEqual(classify_joint_assertions([record(49), record(51)]), CONFLICT)
    def test_cross_version_rejected(self):
        with self.assertRaises(ValueError): classify_joint_assertions([record(49), record(51, source_version='Draft-2')])
    def test_cross_unit_rejected(self):
        with self.assertRaises(ValueError): classify_joint_assertions([record(49), record(51, claim_unit='packages')])
    def test_cross_time_rejected(self):
        with self.assertRaises(ValueError): classify_joint_assertions([record(49), record(51, observation_time='later')])
    def test_cross_definition_rejected(self):
        with self.assertRaises(ValueError): classify_joint_assertions([record(49), record(51, claim_definition='other scope')])
    def test_missing_joint_rejected(self):
        with self.assertRaises(ValueError): classify_joint_assertions([])
    def test_untyped_rejected(self):
        with self.assertRaises(ValueError): classify_joint_assertions([{'value':49}, {'value':51}])
    def test_alternative_nonunique(self): self.assertEqual(classify_admissible_alternatives([49, 51]), NOT_IDENTIFIED)
    def test_alternative_unique(self): self.assertEqual(classify_admissible_alternatives([51, 51]), IDENTIFIED)
    def test_empty_alternatives_not_vacuous(self): self.assertEqual(classify_admissible_alternatives([]), CONFLICT)
    def test_missing_outcome(self): self.assertEqual(operational_outcome_state(required_outcome_records_present=False), OUTCOME_ABSENT)
    def test_present_outcome_not_certified(self):
        with self.assertRaises(ValueError): operational_outcome_state(required_outcome_records_present=True)
    def test_component_profiles(self):
        allowed=frozenset({'Provided','Provided / Expandable'})
        self.assertEqual([strict_component_status(c['component_statuses'], allowed) for c in W['cases']], [False,True])
    def test_missing_component_not_pass(self):
        with self.assertRaises(ValueError): strict_component_status([], frozenset({'Provided'}))
    def test_missing_status_not_pass(self):
        with self.assertRaises(ValueError): strict_component_status(['Provided',''], frozenset({'Provided'}))
    def test_equal_weights(self): self.assertEqual(weighted_score_winners(D['scorecards']['vectors'], [.2]*5), ('Managed Firewall Services',))
    def test_soc_only(self): self.assertEqual(weighted_score_winners(D['scorecards']['vectors'], [0,0,0,1,0]), ('DSPM / Data Privacy',))
    def test_demand_only(self): self.assertEqual(weighted_score_winners(D['scorecards']['vectors'], [0,1,0,0,0]), ('Managed Human Risk and AI Awareness',))
    def test_invalid_weights(self):
        with self.assertRaises(ValueError): weighted_score_winners(D['scorecards']['vectors'], [.2,.2,.2,.2,.3])
    def test_score_ties_retained(self): self.assertEqual(weighted_score_winners({'a':[1,1],'b':[1,1]}, [.5,.5]), ('a','b'))
    def test_financial_free_dimensions(self):
        # Illustrative disjoint 12-group partition with 57 service-year cells.
        # Group membership is NOT inferred from the proprietary source.
        illustrative = [4,4,4] + [5,5,5,5] + [5,5,5,5,5]
        self.assertEqual(len(illustrative), 12)
        self.assertEqual(sum(illustrative), 57)
        self.assertEqual(additive_group_nullity(illustrative), 45)
    def test_nonunique_allocations(self): self.assertTrue(distinct_allocations_same_total([.5,.5],[.75,.25]))
    def test_unique_allocations_not_counterexample(self): self.assertFalse(distinct_allocations_same_total([.5,.5],[.5,.5]))
    def test_different_totals_not_counterexample(self): self.assertFalse(distinct_allocations_same_total([.5,.5],[.5,.4]))
    def test_nonfinite_values_rejected(self):
        with self.assertRaises(ValueError): distinct_allocations_same_total([float('nan'),1],[.5,.5])

if __name__=='__main__': unittest.main()
