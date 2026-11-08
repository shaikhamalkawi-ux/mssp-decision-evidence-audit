"""Transparent source-free tests; no real company independent validation."""
import unittest
from src.decision_sufficiency import (grouped_linear_target_bounds,
    linear_target_identified, robust_weak_score_preference, linear_decision_status)

class TestTargetBounds(unittest.TestCase):
    def test_exact_vertex_enumeration_independent_check(self):
        # Two synthetic groups of sizes 2 and 3: enumerate their six simplex vertices.
        coeff1=[3,-2];coeff2=[1,4,0];y1,y2=2,5
        values=[y1*c1+y2*c2 for c1 in coeff1 for c2 in coeff2]
        self.assertEqual(grouped_linear_target_bounds([coeff1,coeff2],[y1,y2]),
                         (min(values),max(values)))
    def test_nonidentified_service_in_two_service_group(self):
        self.assertEqual(grouped_linear_target_bounds([[1,0]],[1]),(0.0,1.0))
    def test_identified_whole_group(self):
        self.assertEqual(grouped_linear_target_bounds([[1,1]],[1]),(1.0,1.0))
        self.assertTrue(linear_target_identified([[1,1]],[1]))
    def test_three_groups_sum_linear(self):
        self.assertEqual(grouped_linear_target_bounds([[1,0],[2,2],[0,5]],[2,3,4]),(6,28))
    def test_nonnegative_one_service_group(self):
        self.assertTrue(linear_target_identified([[3]],[2]))
    def test_zero_total_is_identified(self):
        self.assertTrue(linear_target_identified([[1,0]],[0]))
    def test_pairwise_utility_difference_robust(self):
        self.assertEqual(linear_decision_status(*grouped_linear_target_bounds([[.4,.1]], [2])),'a_weakly_robust')
    def test_pairwise_difference_crosses_zero(self):
        self.assertEqual(linear_decision_status(*grouped_linear_target_bounds([[-1,1]], [2])),'decision_unresolved')
    def test_exact_tie(self):
        self.assertEqual(linear_decision_status(0,0),'exact_tie')
    def test_invalid_group(self):
        with self.assertRaises(ValueError): grouped_linear_target_bounds([[]],[1])
    def test_invalid_total(self):
        with self.assertRaises(ValueError): grouped_linear_target_bounds([[1]],[-1])
    def test_invalid_coeff(self):
        with self.assertRaises(ValueError): grouped_linear_target_bounds([[float('nan')]], [1])
    def test_invalid_interval(self):
        with self.assertRaises(ValueError): linear_decision_status(3,2)
    def test_firewall_weakly_dominates_two(self):
        fw=[5,4,5,4,5]; iam=[5,4,4,4,5];grc=[4,3,4,3,5]
        self.assertTrue(robust_weak_score_preference(fw,iam))
        self.assertTrue(robust_weak_score_preference(fw,grc))
    def test_firewall_does_not_dominate_others(self):
        fw=[5,4,5,4,5]; dspm=[4,4,3,5,4];human=[3,5,3,4,4]
        self.assertFalse(robust_weak_score_preference(fw,dspm))
        self.assertFalse(robust_weak_score_preference(fw,human))
    def test_positive_weight_witnesses(self):
        vals={
          'Firewall':[5,4,5,4,5],
          'DSPM':[4,4,3,5,4],
          'Human':[3,5,3,4,4],
          'IAM':[5,4,4,4,5],
          'GRC':[4,3,4,3,5]}
        for w,leader,fwvalue,leadervalue in [
           ([.1,.2,.1,.5,.1],'DSPM',4.3,4.4),
           ([.1,.6,.05,.1,.15],'Human',4.3,4.45)]:
           scored={k:sum(a*b for a,b in zip(w,v)) for k,v in vals.items()}
           self.assertEqual(max(scored,key=scored.get),leader)
           self.assertAlmostEqual(scored['Firewall'],fwvalue)
           self.assertAlmostEqual(scored[leader],leadervalue)

if __name__=='__main__': unittest.main()
