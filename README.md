# MSSP decision-evidence audit — research reproducibility capsule

Public repository: https://github.com/shaikhamalkawi-ux/mssp-decision-evidence-audit

Supporting material for the author manuscript:

**Auditing Evidence Sufficiency for MSSP Portfolio Decisions: A Reproducible Protocol and Industrial Case**

Authors: **Muhammad Emran** and **Ghassan Malkawi**. The linked author-review manuscript (V19) is being prepared
for *Systems* (MDPI) and is **not yet published or assigned a journal DOI**.

This repository is intended to support examination of the claims in a prospective
industrial managed security service provider (MSSP) planning case. It does not
contain an IDS, intrusion detector or a new portfolio-optimization algorithm.

## Quick start

Requires Python 3.10 or newer; standard library only.

```bash
python3 run_checks.py
```

Runs 42 deterministic source-free unit tests, 14 checks on limited anonymized derived evidence, 18 casebook checks, and a worked claim-gate demo; none is an independent company observation.

## Contents

- `src/evidence_protocol.py`: small role-typed consistency, uniqueness, score,
  aggregation, and additive-model functions, with guarded inputs.
- `tests/test_evidence_protocol.py`: edge cases including empty interpretation
  sets, mutually inconsistent same-scope assertions, scope mismatch, missing
  outcome records, weight-dependent rank changes, and nonunique allocations.
- `code/`: version-frozen deterministic case scripts corresponding to the
  current author manuscript.
- `evidence/`: selected de-identified, normalized and source-derived values
  required by those scripts. No source-by-source proprietary workbook dump.
- `manuscript/`: an **unpublished author-review PDF**. It is not an MDPI
  proof and its pagination can change at final production.
- `docs/REPRODUCIBILITY_SCOPE.md`: exact scope and exclusions of each check.

## Evidence and reporting limits

Original corporate Excel/PDF files, exact source paths, unmasked monetary totals,
internal data-owner audit logs, and proprietary replay scripts are **not** in
this repository. The original corporate archive's precise byte fingerprints
are not made public. These omissions are intentional.

An earlier *owner-side* script reported 72 selected original-spreadsheet checks
passing. That script and original records are kept in a separate controlled
record and **cannot** be independently rerun from this public capsule. The
casebook checks are deterministic checks of released source-derived inputs; they
are not external validation, implementation tests, or statistical replicates.

The 51-to-25 mapping is source membership, not evidence of delivered services.
The source-authored "Provided" label is not a readiness certificate. A listed
launch year is not evidence of achieved launch; missing operational records
are not proof of implementation failure. The scorecard witnesses use explicitly
chosen diagnostic weights, not elicited or company-approved priorities.

## Publication and citation

The manuscript PDF is an author-review copy; neither journal acceptance nor a
DOI is implied. The V18 manuscript Data Availability Statement points to the immutable source-free code and schema
snapshot commit `14be6c6affa0ca163299f325067f7d2b9b42e78e`. The current document file may be updated
without changing that source-code snapshot.

`CITATION.cff` identifies the software material, but final
journal metadata, license, author declarations and rights-clearance remain to
be confirmed. Repository visibility is not evidence that restricted original
company data can be redistributed.

## V18 decision-sufficiency extension (source-free)

The research extension adds `src/decision_sufficiency.py`, exact linear target bounds over explicitly declared nonnegative disjoint aggregation groups, robust pairwise score comparisons, and deterministic unit tests. `docs/PORTABLE_CLAIM_PROTOCOL_V1.md` and `schemas/claim_evidence_record_v1.schema.json` specify claim origin, intended use, admission holds and separate finding/value/reason fields. The public `evidence/claim_origin_intended_use_v18.csv` only recodes already reported, de-identified source IDs; it contains no company originals or new monetary amounts.

Human blind application and a genuine dated owner-authorized evidence repair have **not been executed** (see the files with `NOT_EXECUTED` in their titles). Run `python3 run_checks.py` for the expanded source-free suite. The journal submission and release permissions still require author/data-owner review; no license, archive DOI or independent field validation is implied.

**Scope correction:** the historical V8 casebook records a conditional same-scope 49-versus-51 counterexample. The source helper calls 49 `services` and enumeration yields 51 detailed `capabilities`; the V18 claim-origin gate holds cross-term equivalence until an authorized data dictionary reconciles the units. The software demonstration must not be mistaken for a verified same-meaning company contradiction.

## V19 literature-grounded manuscript revision (8 November 2026)

V19 preserves the documented 51-to-25 mapping and all V18 mathematical and case results. Five published references (Hybertson 2018, Liesiö et al. 2007, Greco et al. 2008, Punkka & Salo 2014, and Diemert et al. 2025) clarify scientific precedent for evidence-based systems engineering, robust portfolio preference, conditionality of ordinal numeric scores and human assurance evaluation. The manuscript now contains 36 cited references, with citations in first-appearance order. No new company observations, human study, or observed evidence repair have been added.

The manuscript has been updated at `manuscript/main.tex` and `manuscript/MSSP_Decision_Evidence_MDPI_Author_Review.pdf`. `PUBLIC_SHA256SUMS.txt` now lists exact SHA-256 fingerprints for 33 fixed source-free and manuscript objects (mutable overview metadata excluded). The cited fixed code/schema snapshot remains `14be6c6affa0ca163299f325067f7d2b9b42e78e`.

The coauthor reports that the original material creator agrees to disclosure of de-identified results. A separate author-controlled written scope/roles confirmation is maintained off GitHub; corporate original XLSX/PDF, raw financial amounts and restricted source paths are still excluded. Both authors must finalize CRediT, funding, competing-interest and publication statements before journal submission.
