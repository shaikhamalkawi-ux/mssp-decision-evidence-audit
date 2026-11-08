"""Small transparent decision-evidence routines for a research casebook.

This is NOT an assurance certification, a security control evaluator, or a
trained ranking algorithm. No confidential source workbook is distributed.
"""
from __future__ import annotations

from collections.abc import Mapping, Sequence
from math import isfinite, isclose

IDENTIFIED = "IDENTIFIED_SOURCE_FACT"
CONFLICT = "SOURCE_CONFLICT"
NOT_IDENTIFIED = "NOT_IDENTIFIED"
OUTCOME_ABSENT = "OUTCOME_EVIDENCE_ABSENT"


def classify_joint_assertions(records: Sequence[Mapping[str, object]]) -> str:
    """Compare facts already ADMITTED to the SAME claim definition and scope.

    Cross-version, cross-time, or cross-unit records are an input error. This
    routine does not decide whether two external texts truly share a meaning;
    that source-semantic decision belongs to the documented evidence review.
    """
    if not records:
        raise ValueError("nonempty jointly asserted source records required")
    required = ("claim_definition", "claim_unit", "source_version", "observation_time", "value")
    if any(any(key not in r for key in required) for r in records):
        raise ValueError("every record requires explicit claim definition, unit, version, time, value")
    scopes = {tuple(repr(r[k]) for k in required[:-1]) for r in records}
    if len(scopes) != 1:
        raise ValueError("records do not have the same admitted scope")
    values = {repr(r["value"]) for r in records}
    return IDENTIFIED if len(values) == 1 else CONFLICT


def classify_admissible_alternatives(values: Sequence[object]) -> str:
    """Report uniqueness within a pre-admitted nonempty interpretation set.

    Empty set is explicitly inconsistent, not vacuously identified.
    This method cannot construct an admissible set or judge source semantics.
    """
    if not values:
        return CONFLICT
    return IDENTIFIED if len({repr(v) for v in values}) == 1 else NOT_IDENTIFIED


def operational_outcome_state(*, required_outcome_records_present: bool) -> str:
    """Classify absence only; actual sufficiency needs a separate evidence gate."""
    if not isinstance(required_outcome_records_present, bool):
        raise ValueError("outcome presence must be a boolean")
    if required_outcome_records_present:
        raise ValueError("present records require a domain-specific verification rule")
    return OUTCOME_ABSENT


def strict_component_status(statuses: Sequence[str], allowed: frozenset[str]) -> bool:
    """A declared component-wise predicate, not operational readiness."""
    if not statuses:
        raise ValueError("unknown component list must not pass vacuously")
    if any(not isinstance(x, str) or not x.strip() for x in statuses):
        raise ValueError("missing component status requires explicit evidence decision")
    return all(x in allowed for x in statuses)


def weighted_score_winners(scores: Mapping[str, Sequence[float]], weights: Sequence[float], *, tol: float = 1e-10) -> tuple[str, ...]:
    """Diagnostic, NOT source-authorized MCDA or an elicitation of weights."""
    if not scores or not weights:
        raise ValueError("score matrix and weights required")
    if any(not isfinite(float(w)) or float(w) < 0 for w in weights):
        raise ValueError("weights must be finite and nonnegative")
    if not isclose(sum(weights), 1., rel_tol=tol, abs_tol=tol):
        raise ValueError("weights must sum to one")
    totals = {}
    for label, row in scores.items():
        if len(row) != len(weights) or any(not isfinite(float(x)) for x in row):
            raise ValueError("every score vector must be finite and match the criteria count")
        totals[label] = sum(w * x for w, x in zip(weights, row))
    maximum = max(totals.values())
    return tuple(sorted(label for label, value in totals.items() if isclose(value, maximum, abs_tol=tol, rel_tol=tol)))


def additive_group_nullity(group_sizes: Sequence[int]) -> int:
    """n - g under one independent total constraint per disjoint nonempty group."""
    if not group_sizes or any(type(n) is not int or n < 1 for n in group_sizes):
        raise ValueError("group sizes must be positive integers")
    return sum(group_sizes) - len(group_sizes)


def distinct_allocations_same_total(a: Sequence[float], b: Sequence[float], *, tol: float = 1e-10) -> bool:
    if not a or len(a) != len(b):
        raise ValueError("same-size nonempty allocations required")
    if any(not isfinite(float(x)) or x < 0 for x in (*a, *b)):
        raise ValueError("allocation values must be finite and nonnegative")
    return (any(not isclose(x, y, abs_tol=tol, rel_tol=tol) for x, y in zip(a, b))
            and isclose(sum(a), sum(b), abs_tol=tol, rel_tol=tol))
