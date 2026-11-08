# Manuscript repository-link insertion — verification gate

**Current state:** The public GitHub repository exists at https://github.com/shaikhamalkawi-ux/mssp-decision-evidence-audit.
The manuscript link must be updated **only after** the uploaded commit has been
read back and the source-free tests have been checked at that commit.

Once a real publicly accessible repository is confirmed, replace the current
MDPI `\\dataavailability{...}` statement with a version-locked paragraph:

> A source-free reproducibility capsule containing de-identified derived inputs,
> a claim-decision casebook, deterministic validation scripts, and regression
> tests is publicly available at [VERIFIED_REPO_URL], commit [VERIFIED_COMMIT].
> The original confidential company XLSX/PDF records, original-source hashes
> and owner-side source-reconstruction materials are not publicly distributed.
> Accordingly, the repository reproduces the selected derived numerical and
> logical witnesses, but cannot provide full raw-source-to-manuscript replication
> or validate operational service deployment. Requests for restricted source
> materials require the data owner's separate approval.

Do not populate `[VERIFIED_REPO_URL]` from a planned repository name alone, and
do not invent a DOI. Check the release license before offering unrestricted reuse.
