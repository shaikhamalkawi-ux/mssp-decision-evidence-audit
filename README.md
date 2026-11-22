# MSSP decision-evidence audit — research reproducibility capsule

> **Current research state (22 November 2026):** MEMRAN **V36R2**, author-review only, not submitted to *Systems*. The complete new manuscript, Supplementary Material and restricted reproducibility materials remain under controlled author review. This public GitHub repository still contains an **older V20 author-review manuscript snapshot**; it is **not** a full V36R2 release. The newest **public, source-free subset** contains the [V36R2 evidence and AI-diagnostic scope](docs/V36R2_AI_EVIDENCE_SCOPE.md), [normalized mathematical test](public_replay/v36r2/verify_linear_claim_class.py) and [derived group sizes](public_replay/v36r2/DERIVED_GROUP_SIZES_FOR_LINEAR_CLAIM_TEST.csv). Original company Excel/PDF sources and unredacted yearly planning records are **not public**; no Zenodo deposit has been made.\n\nPublic repository: https://github.com/shaikhamalkawi-ux/mssp-decision-evidence-audit

Supporting material for the author manuscript:

**Auditing Evidence Sufficiency for MSSP Portfolio Decisions: A Reproducible Protocol and Industrial Case**

Authors: **Muhammad Emran** and **Ghassan Malkawi**. The archived public author-review manuscript (V20) is being prepared
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

Operational-impact evaluation and verified owner-authorized evidence repair are **not established** by these deterministic checks. Run `python3 run_checks.py` for the existing source-free suite. The journal submission and release permissions still require author/data-owner review; no license, archive DOI or independent field validation is implied.

**Scope correction:** the historical V8 casebook records a conditional same-scope 49-versus-51 counterexample. The source helper calls 49 `services` and enumeration yields 51 detailed `capabilities`; the V18 claim-origin gate holds cross-term equivalence until an authorized data dictionary reconciles the units. The software demonstration must not be mistaken for a verified same-meaning company contradiction.

## V19 literature-grounded manuscript revision (8 November 2026)

V19 preserves the documented 51-to-25 mapping and all V18 mathematical and case results. Five published references (Hybertson 2018, Liesiö et al. 2007, Greco et al. 2008, Punkka & Salo 2014, and Diemert et al. 2025) clarify scientific precedent for evidence-based systems engineering, robust portfolio preference, conditionality of ordinal numeric scores and human assurance evaluation. The manuscript now contains 36 cited references, with citations in first-appearance order. No new company observations, human study, or observed evidence repair have been added.

The manuscript has been updated at `manuscript/main.tex` and `manuscript/MSSP_Decision_Evidence_MDPI_Author_Review.pdf`. `PUBLIC_SHA256SUMS.txt` now lists exact SHA-256 fingerprints for 33 fixed source-free and manuscript objects (mutable overview metadata excluded). The cited fixed code/schema snapshot remains `14be6c6affa0ca163299f325067f7d2b9b42e78e`.

The originating data owner and first author, Muhammad Emran, has confirmed consent to publication of the de-identified findings and public source-free capsule. His contributions include the original practical investigation, source-data collection and audit/validation; Ghassan Malkawi developed the analytical methodology and wrote the manuscript. This consent does not grant general access to confidential company originals; corporate original XLSX/PDF, raw financial amounts and restricted source paths are still excluded. The specified CRediT role division and consent have been updated in V20. Funding and competing-interest declarations still require truthful author statements before journal submission.

## Current MEMRAN V36R2 source-free addendum (22 November 2026)

The current author-review paper focuses on the original industrial planning records and documentary/AI results. The **public repository adds only a controlled mathematical reproduction subset**, not the full current author-review PDF or original corporate archive:

- `docs/V36R2_AI_EVIDENCE_SCOPE.md` explains the exact permitted claims, source versions, denominator separation, and reproduction limits.
- `public_replay/v36r2/verify_linear_claim_class.py` and the paired derived CSV check 109 linear target bounds using normalized, non-proprietary totals (requires NumPy and SciPy).
- The five-output source-bounded AI diagnostic reports 21/32 literal agreement; this is **not a gold-standard accuracy score**. The 42-question documentary comparator and the 16,200 constructed cases are separate experiments.
- The original material describes prospective **Year 1–3 planning** within Draft 2/Draft 3 Excel/PDF pairs, **not** separate observed yearly performance statements.

**Release boundary:** no original yearly company workbooks, original reports, restricted financial figures, corporate identities or sensitive source filenames are being uploaded. The current author-review PDF contains declarations requiring verification and remains in the controlled workspace. A DOI-archived Zenodo release is appropriate only after the public files, source rights and final statements are approved and frozen.
