# Claim-conditioned evidence sufficiency: source-free protocol v1

**Scope:** a reproducible input/output *specification* and algebraic diagnostics, not an independently validated audit method. No source company or human review results are bundled.

## Intended-use gate

1. **Declare the requested question and use.** Is the source explicitly asserting this result, is there separately confirmed managerial use, or is this a researcher-defined diagnostic? Never attribute a researcher query to company management.
2. **Lock the evidence population.** Record source identity, version, observation boundary, unit, operational scope, and evidence role. Hash identity alone does not establish authenticity or interpretive meaning.
3. **Admit evidence.** A human reviewer checks whether the semantics match the question. If source scopes cannot be aligned, record `ADMISSION_HOLD` and an explanation. Do not force a contradiction merely because two reported counts differ.
4. **Separate the logical result and explanation.** For admitted, jointly interpreted records, determine an identified source answer, a genuine same-scope conflict, alternative admissible outcomes, or missing *required* observation. Save the value if identified (including `false`), bounds and a witness if only bounded, and the missing-evidence reason separately.
5. **Audit decisions, not inputs alone.** For a specified decision rule and admissible uncertainty set, test whether one action is weakly preferred for all admitted interpretations. Stable decisions may be possible with non-unique parameter values.
6. **Specify what would resolve uncertainty.** Name the precise additional record, issuer/authority, effective date, service scope, and what it could and could not certify. Do not say `minimum` without a formal cost/cardinality/minimality rule.
7. **Report limits.** Source counting, an algebraic witness, and human interpretive reproducibility are distinct. A real reviewer study and a genuine owner-authored evidence-repair are both pending.

## Explicit outcome levels

- **L0**: Original source identity and admission check (requires authorized source access).
- **L1**: An executable mathematical certificate on admitted or synthetic inputs (this public capsule).
- **L2**: Independent human claim interpretation (not done in this case).
- **L3**: Dated authorized evidence repair and rerun (not done in this case).
- **L4**: External multi-organization transport or observed operational effect (not done).

## Decision-stability examples

Under ordinal scores *if* treated as numeric, componentwise dominance is equivalent to weak preference under every nonnegative normalized weight vector. This fact does not imply the company used any weighted sum. Positive-weight alternative winners show that zeros are not required to exhibit scorecard ambiguity. See `tests/test_decision_sufficiency.py`.

Under a disjoint additive **illustration** with `r_j>=0`, and a known aggregate `Y_g` for each group, the bounds of a linear target with coefficients `c_j` are exactly `sum_g Y_g*min_{j in g}(c_j)` and `sum_g Y_g*max_{j in g}(c_j)`. This formalizes why a whole group's total can be identified despite individual package-level shares remaining unresolved. It cannot reveal actually realized revenue, an approved distribution rule, or a causal delay effect.

## Reproducible example

`python -m unittest discover -s tests -v` from repository root runs the source-free tests. A separate original-company-workbook gate is not redistributable.
