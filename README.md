# MSSP decision-evidence audit — reproducibility and source records

> **Editorial disclosure correction (23 November 2026):** Current author-review manuscript is **V36R3P2** (22-page article + 33-page supplement). Section 3.1 explicitly distinguishes the nine [public original planning Excel/PDF files](source_material/README.md), which include **financial planning scenario amounts**, from the remaining controlled company archive. Supplementary Table D2 identifies earlier AI checks as **not rerun in the documented execution record**. This is a two-sentence editorial correction only; no scientific data, results, public source files or software code changed. The public `manuscript/` snapshot remains the old V20 edition; the current article is available only in the author-review package.


> **Editorial update (23 November 2026):** The current *author-review* manuscript is **V36R3P1**. This production cleanup reconciles the public availability of nine source documents in the article and Appendix A–M, improves Appendix L's 11-group comparison table, and removes internal version labels. It does not revise the scientific results or public source files. The full revised article and supplementary material are maintained in the author-controlled review package, not at `manuscript/` in this public repository.


> **Current research state (23 November 2026):** MEMRAN **V36R3**, author review only, not journal-submitted. The public repository now contains [nine exact-source Excel/PDF planning files](source_material/README.md), [their SHA-256 manifest](source_material/SOURCE_SHA256SUMS.txt), [the V36R2 AI/documentary scope note](docs/V36R2_AI_EVIDENCE_SCOPE.md), and a [normalized mathematical replay](public_replay/v36r2/verify_linear_claim_class.py). The publication of selected original documents follows the project user's report of rights-holder consent. The *full updated V36R3 article* (literature and result-input provenance synchronized) and *other restricted controlled records* remain in the author's Drive workspace; the manuscript snapshot in this repository is an older **V20** edition, not the current paper.

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
- `evidence/`: selected de-identified, normalized and source-derived values required by historical scripts.
- `source_material/`: nine newly released original planning Excel/PDF documents from Draft 2, Draft 3 and consolidation, with their SHA-256 hashes and publication-context notes.
- `manuscript/`: an **unpublished author-review PDF**. It is not an MDPI
  proof and its pagination can change at final production.
- `docs/REPRODUCIBILITY_SCOPE.md`: exact scope and exclusions of each check.

## Evidence and reporting limits

Nine original Excel/PDF planning objects from Draft 2, Draft 3 and the 25-service consolidation are **now publicly available** in [`source_material/`](source_material/README.md), with matching source-object SHA-256 values. They contain company-branded projections, not realized financial statements. The **rest of the original corporate ZIP**, confidential audit logs, restricted original source paths, controlled owner-side replay scripts and other archival files remain outside this repository.

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

The originating data owner and first author, Muhammad Emran, confirmed consent to the prior de-identified capsule. The project user subsequently confirmed approval to release the **nine selected original planning files**, with exact content preserved and access now provided under `source_material/`. This does not constitute a blanket publication or reuse license for other company materials. Muhammad Emran conducted the industrial planning investigation, data collection and source validation; Ghassan Malkawi developed the analytic methodology and wrote the manuscript. Funding and competing-interest declarations still require truthful author statements before journal submission.

## MEMRAN V36R3 editorial and source-governance addendum (23 November 2026)

The current author-review paper focuses on the original industrial planning records and documentary/AI results. This public update adds a **mathematical replay subset and the selected primary Excel/PDF sources**, not the full current author-review PDF or entire original corporate ZIP:

- `docs/V36R2_AI_EVIDENCE_SCOPE.md` explains the exact permitted claims, source versions, denominator separation, and reproduction limits.
- `public_replay/v36r2/verify_linear_claim_class.py` and the paired derived CSV check 109 linear target bounds using normalized, non-proprietary totals (requires NumPy and SciPy).
- The five-output source-bounded AI diagnostic reports 21/32 literal agreement; this is **not a gold-standard accuracy score**. The 42-question documentary comparator and the 16,200 constructed cases are separate experiments.
- The original material describes prospective **Year 1–3 planning** within Draft 2/Draft 3 Excel/PDF pairs, **not** separate observed yearly performance statements.

**Release boundary:** the nine listed originals are public and remain byte-identical to the source archive. They contain Year 1–3 *planning*, not three realized yearly accounts. Other company records, personal event photographs, duplicate academic submissions and private archive paths have not been released. The V36R3 author-review PDF has been synchronized with the source-access disclosure and remains under controlled editorial review. A separately DOI-archived Zenodo release may be appropriate after the repository and licensing metadata are frozen.

### V36R3 research-comparison and reproducibility crosswalk (23 November 2026)

The updated author-review paper shortens its main closest-predecessor table from 19 to **8** rows, and organizes **11** complementary literature groups in Supplementary Appendix L; no previously cited comparison was dropped. It explicitly links component status, priority rules, financial identifiability and operational launch evidence in one claim-conditioned audit. See [the editorial scientific-scope note](docs/V36R3_LITERATURE_AND_REPRODUCIBILITY_SCOPE.md) and the [18-result source-to-input/execution-status ledger](docs/V36R3_RESULT_INPUT_REPLAY_LEDGER.csv). All 14 original figures and the substantive results are preserved. The mathematical 109-target normalized LP diagnostic was run in this revision; prior original-source and AI/synthetic experiments were **not** rerun. The public manuscript PDF under `manuscript/` remains the older V20 snapshot; full V36R3 manuscript and Supplementary Material are in author review, not a new GitHub publication or journal submission.
