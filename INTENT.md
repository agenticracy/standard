# Agenticracy Standard — Forward Intent

This file declares the public commitments and conditional roadmap for the Agenticracy Standard ecosystem. It is structured so that compliance can be verified by anyone, at any time, against the live state of the listed services.

## Author and ownership

- **Originator:** Vladut-Mihai Iorga
- **ORCID:** https://orcid.org/0000-0001-8705-1326
- **Legal entity (commercial implementer):** psylligent ltd (UK Companies House: 13093346)
- **Future legal entity (foundation / governance):** agenticracy.org (UK charity, registration in progress)
- **Trademarks (UK IPO active):** UK00004369189 (agenticracy), UK00004377660 (slopometry x4), UK00004377674 (workability.ai x2). XQ + Meta-Cognitive Quotient: intended filing.

## Public versus private (binding statement)

The Agenticracy Standard is published as a **partially open standard**. The semantic layer (constructs S, P, O, R, D, G; schema; calibration class definitions) is open under CC BY-NC-ND 4.0. The synthesis layer (private coefficients, tax weights, decay parameters, verdict thresholds, projection formula) is reserved and operated by the author or licensees.

Reverse-engineering, statistical inference, model-distillation, or any other technical method aimed at recovering the private synthesis layer from public outputs is **prohibited** under the licence and would constitute a breach.

## Forward commitments (with triggers)

### Tier 1 — Active or imminent

| Commitment | Status |
|---|---|
| ORCID anchor (0000-0001-8705-1326) | active |
| Zenodo deposit + DOI | imminent (within 7 days of this commit) |
| OpenAIRE auto-harvest | imminent (within 24-72h after Zenodo) |
| Software Heritage mirror of public repositories | continuous (automatic) |
| Public schema reference implementation | published in this repository |

### Tier 2 — 90 days

| Commitment | Trigger | Notes |
|---|---|---|
| FAIRsharing standard listing | post-Zenodo DOI | Reusability anchor |
| Public licensure pathway documented | n/a | For commercial implementers via psylligent ltd / workability.ai |
| Sample audit-record dataset (Paper 1) | post-Paper-1 publication | First 132-entity panel, end-of-audit-year basis |

### Tier 3 — 6-12 months (conditional)

| Commitment | Trigger | Conditionality |
|---|---|---|
| W3C Community Group "Agenticracy Standard CG" | community interest signal (≥3 independent implementers) | If signal reached |
| OAI-PMH 2.0 endpoint at `oai.congruence.wiki` | funding event sufficient to operate the endpoint | Conditional on operational substrate |
| Paper 2 (prospective 99-day cohort) pre-registration | post-PhD enrolment | Late 2026 / early 2027 |

### Tier 4 — 12-24 months (aspirational, conditional)

| Commitment | Trigger | Conditionality |
|---|---|---|
| re3data + OpenDOAR listing | OAI-PMH endpoint live | Sequential |
| OpenAIRE service catalogue submission | TRL-9 operational corpus + sustained funding | Conditional on Tier 3 + funding |
| ISO standard submission | n/a | Aspirational; only after independent replication |

## Honesty clauses

1. None of the Tier 3 / Tier 4 commitments are guaranteed; they are conditional on funding, community signal, and successful pre-PhD publication.
2. Private synthesis coefficients are not a substitute for verifiability — public schema + public prompts allow any party to audit *any* entity and report results. Only the offline G-scoring requires the private layer.
3. The author commits to not claim outcomes beyond what the published evidence supports. Specifically: Paper 1 establishes calibration and discrimination, *not* prospective collapse-ETA prediction. The latter requires Paper 2.

## Verification

Every assertion in this file is anchored by a SHA-256 hash of the artifact in question, recorded in `outputs/artifacts/PRE_REGISTRATION_MANIFEST_v2.json` of the companion experiment repository. Discrepancies between this file and on-the-ground reality should be reported as issues against this repository.

---

*Last updated: 2026-04-28. Living document; changes are version-controlled in git history.*
