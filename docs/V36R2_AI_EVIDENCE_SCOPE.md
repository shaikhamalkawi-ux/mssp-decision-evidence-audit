# MEMRAN V36R2 — Public source-free replay subset

**Date:** 22 November 2026  
**Research status:** author review; not journal-submitted.  
**Current article:** *What Can a Managed Security Service Roadmap Establish? Evidence Sufficiency and Partial Identification for Portfolio Governance*, by Muhammad Emran and Ghassan Malkawi.

This is a **limited public source-free research capsule**, not the full V36R2 controlled replay archive and not a replacement for the previously locked V18 code/schema baseline.

## Reproduce one exact mathematical check
```bash
python -m pip install numpy scipy
python public_replay/v36r2/verify_linear_claim_class.py \
  --groups public_replay/v36r2/DERIVED_GROUP_SIZES_FOR_LINEAR_CLAIM_TEST.csv
```
Expected: `PASS 109 linear claims; max endpoint LP error 0.0` on a compatible NumPy/SciPy environment. This uses synthetic/normalized totals (each positive group total set to 1) and **does not replay private company financial amounts**. The code and group-size CSV match the author-review source subset.

For disjoint groups with strictly positive totals `Y_g` and nonnegative allocations `r_i`, the exact range of a linear claim `c^T r` is
- lower bound: sum over groups of `Y_g min_(i in group g) c_i`;
- upper bound: sum over groups of `Y_g max_(i in group g) c_i`.

A linear claim is uniquely identified exactly when `c` is constant within each positive group. This follows from elementary linear algebra/linear programming; it is **not a novel general theorem**, a verified company allocation, or a service performance finding. For this normalized derived topology: 12 groups, 57 coordinates, rank 12, nullity 45. The 109 deterministic claim tests include 12 group totals, 57 individual coordinates, 20 group-linear combinations and 20 mixed targets.

## Documentary and AI diagnostics: precise boundaries

Two different experiments must not be pooled:
1. **42 author-coded documentary questions:** each comparator implementation returned 10 supported and 32 unresolved; exact paired parity. These are documentary status checks, not an independently labelled accuracy test.
2. **32 documentary questions / 8 public-notice sources:** five frozen AI-authored outputs agree literally on 21/32 questions (Q1 8/8, Q2 2/8, Q3 3/8, Q4 8/8). Disagreements are concentrated in supplier choice/award, contract-conclusion stage, and same-scope date interpretation. Agreement is **not accuracy**; the AI-produced source audit is not independent ground truth. Separate arm runs for four providers are retained in a controlled project archive, not combined post hoc with this frozen five-output diagnostic.

The constructed 16,200-scenario result is a simulation, not observed service delivery, workforce savings, or commercial benefit.

## Underlying material and data governance

The original Muhammad Emran industrial dossier includes paired Excel/PDF planning material from **Draft 2** and **Draft 3**, plus service-consolidation material. The three 'years' are **prospective Year 1–3 plan columns**, **not** three independently observed yearly statements. Later source versions revise scope, making direct inter-draft growth comparisons invalid.

**Selected original Excel/PDF planning files are now publicly released** at [`source_material/`](../source_material/README.md), with a [source-object SHA-256 register](../source_material/SOURCE_SHA256SUMS.txt). This release follows user-reported rights-holder authorization. The files retain their company financial planning assumptions and confidentiality legends. Original entire-archive contents, other company records, restricted operational details, controlled rerun code and unverified declarations are not part of this public release. No general open-data reuse license is asserted.

**Do not describe this GitHub update as a new validation, a new industrial result, or a full reproducibility release.** Permanent DOI archiving on Zenodo should be considered only for a rights-cleared, frozen release package.
