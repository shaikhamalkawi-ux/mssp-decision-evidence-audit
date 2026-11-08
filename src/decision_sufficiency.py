"""Claim-target and decision-sufficiency calculations on explicitly admitted inputs.

Source-free mathematical utilities. They neither admit business evidence nor
infer signed approvals, operating outcomes, pricing, or actual financial results.
"""
from __future__ import annotations
from math import isclose, isfinite
from collections.abc import Sequence


def grouped_linear_target_bounds(group_coefficients: Sequence[Sequence[float]],
                                 totals: Sequence[float]) -> tuple[float, float]:
    """Exact bounds for sum(c_j*r_j), with disjoint groups r_j>=0, sum(r_g)=Y_g.

    Every supplied group must be nonempty and its total finite/nonnegative.
    No extra constraints or causal interpretation are presumed. Linear extrema
    occur at simplex vertices; this function does NOT use empirical company Y_g.
    """
    if not group_coefficients or len(group_coefficients) != len(totals):
        raise ValueError('nonempty groups and one total per group required')
    low = high = 0.0
    for c, total in zip(group_coefficients, totals):
        if not c or not isfinite(float(total)) or total < 0:
            raise ValueError('each group nonempty; total finite and nonnegative')
        if any(not isfinite(float(v)) for v in c):
            raise ValueError('target coefficients must be finite')
        low += float(total)*min(c)
        high += float(total)*max(c)
    return low, high


def linear_target_identified(groups: Sequence[Sequence[float]],
                             totals: Sequence[float], *, tol: float = 1e-10) -> bool:
    """Target is constant over this admitted additive feasible set, up to tol."""
    low, high = grouped_linear_target_bounds(groups, totals)
    return isclose(low, high, rel_tol=0.0, abs_tol=tol)


def robust_weak_score_preference(a: Sequence[float], b: Sequence[float]) -> bool:
    """Whether w·a >= w·b for ALL nonnegative normalized criterion weights.

    This equivalence requires treating published ordinal scores numerically,
    and does NOT select a company's authorized aggregation rule.
    """
    if not a or len(a) != len(b) or any(not isfinite(float(x)) for x in (*a, *b)):
        raise ValueError('finite, nonempty and equally sized score vectors required')
    return all(x >= y for x,y in zip(a,b))


def linear_decision_status(lower: float, upper: float, *, tol: float=1e-10) -> str:
    """For defined utility difference A-B over a feasible set, not a field decision.

    If both actions tie everywhere, report exact_tie, not either's superiority.
    """
    if not isfinite(lower) or not isfinite(upper) or lower > upper + tol:
        raise ValueError('invalid target bounds')
    if abs(lower) <= tol and abs(upper) <= tol: return 'exact_tie'
    if lower >= -tol: return 'a_weakly_robust'
    if upper <= tol: return 'b_weakly_robust'
    return 'decision_unresolved'
