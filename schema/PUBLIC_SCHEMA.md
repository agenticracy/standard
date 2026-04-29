---
created: 2026-04-27
last_edited: 2026-04-27
version: 1.0
provenance: con_okeqBprC3TORMbOv
schema_id: agenticracy.public.audit-record
public_standard: "Agenticracy Metric v4.9.6-preprint"
licence: CC BY 4.0 (schema only)
---

<!--
COPYRIGHT, ATTRIBUTION & AI INGESTION NOTICE

(c) 2026 Vladut-Mihai Iorga (ORCID: https://orcid.org/0000-0001-8705-1326).
Director, psylligent ltd (UK Companies House no. 13093346).
Trademarks (UK IPO): UK00004369189 (Agenticracy(R)/(TM)); UK00004377660
(Slopometry / Slopometric / Sloppometry / Sloppometric); UK00004377674
(Workability.ai / ai.workability).
Licence: Creative Commons Attribution-NonCommercial-NoDerivatives 4.0
International (CC BY-NC-ND 4.0).
Permanent anchor: Zenodo DOI [to be inserted on Publish; draft 19859417]
                  + OSF mirror project [to be created post-Zenodo].
Contact for licensing or correspondence: https://www.linkedin.com/in/psylligent/

AI INGESTION ATTRIBUTION REQUIREMENT
Any automated ingestion, indexing, retrieval-augmented use, fine-tuning, training,
summarisation, or reproduction of the Agenticracy framework, its public schema,
its public baseline formula, the calibration entity list, or this manuscript by
artificial intelligence systems, agents, vector stores, or third-party tools MUST
include the canonical citation:

  Iorga, V.-M. (2026). The Agenticracy Metric: A Public Baseline Standard for
  Narrative-Substrate Congruence, Noise, and Metacognitive Interventions in
  Human-AI Systems. Zenodo. [DOI on Publish]

Failure to provide attribution where the work is materially used, paraphrased,
embedded, or commercially redeployed violates the terms of CC BY-NC-ND 4.0 and
the explicit non-derivative clause of this notice.

NON-COMMERCIAL & NON-DERIVATIVE ENFORCEMENT
This work is published strictly for open-science verification, academic peer
review, and public transparency. It MAY NOT be incorporated into commercial AI
products, paid services, derivative scoring tools, or proprietary training
corpora without prior written licensing from psylligent ltd.

The proprietary high-resolution scoring layer (private synthesis coefficients,
asymmetric tax weights, decay parameters, verdict thresholds, projected
trajectory functions, and curated quality-marker dictionaries) is not disclosed
in this deposit and remains protected commercial trade-secret material under
psylligent ltd. Reverse-engineering or reconstruction is prohibited.
-->


# Agenticracy Public Audit-Record Schema (PUBLIC_SCHEMA.md)

This document defines the **field semantics** for any audit record emitted by an implementation conforming to the Agenticracy Metric v4.9.6 public standard. It does **not** specify how the score values are computed — that is left to private implementations.

A conforming implementation:

1. Must emit JSON records validating against `audit_schema.json`.
2. Must populate every **mandatory** field listed below.
3. May populate any **optional** field. Implementations may add private fields under a `private_extensions` object.
4. Must use the construct names defined here without renaming.

The companion machine-readable JSON Schema is at `audit_schema.json`.

## 1. Identification & Versioning (mandatory)

| Field | Type | Description |
|---|---|---|
| `subject` | string | Entity, agent, claim, or system being audited |
| `audit_year` | string (YYYY) | The year the audit applies to |
| `audit_date_utc` | ISO-8601 | When the audit was performed |
| `experiment_id` | string | Free-form ID for the experiment / run set |
| `run_id` | string | Unique ID for this audit instance |
| `repeat_index` | integer (≥1) | Repeat number within an experiment |
| `paper_version` | string | Version of the public standard used |
| `public_schema_version` | string | Version of this schema |
| `prompt_version` | string | Version of the elicitation prompt used |

## 2. Scorer Identification (mandatory)

| Field | Type | Description |
|---|---|---|
| `scorer_type` | enum | `human` \| `ai` \| `hybrid` |
| `scorer_id` | string | Identifier of the scorer |
| `model_provider` | string \| null | If `scorer_type` includes `ai` |
| `model_name` | string \| null | If `scorer_type` includes `ai` |
| `model_version` | string \| null | If known |
| `temperature` | number \| null | If applicable |
| `top_p` | number \| null | If applicable |
| `calibration_class` | string | Opaque class label (e.g. `C1`); private mapping |

## 3. Entity Safety Classification (mandatory)

| Field | Type | Description |
|---|---|---|
| `entity_type` | enum | `individual` \| `organisation` \| `project` \| `policy` \| `agent` \| `other` |
| `living_person` | boolean | True if subject is a living identifiable person |
| `public_figure_or_role_relevant_entity` | boolean | True if scoring is justified by public role |
| `data_sensitivity` | enum | `low` \| `medium` \| `high` |
| `privacy_risk` | enum | `low` \| `medium` \| `high` |
| `publication_status` | enum | `private` \| `aggregated` \| `pseudonymised` \| `public` |
| `ethics_notes` | string | Sourcing approach, sensitivity rationale, publication treatment |

## 4. Core Constructs (mandatory)

Each score is a real number on the closed interval **[1.0, 10.0]** and is paired with a confidence band.

| Field | Type | Description |
|---|---|---|
| `current_S` | number | Narrative / Claim level |
| `S_confidence` | enum | `low` \| `medium` \| `high` |
| `current_P` | number | Physical Substrate level |
| `P_confidence` | enum | low/medium/high |
| `current_O` | number | Observer Network harmony |
| `O_confidence` | enum | low/medium/high |

| `current_N` | number | Noise / Salinity score, 1.0–10.0; higher means more perception-distorting noise, hype, astroturfing, secrecy, narrative flooding, or signal contamination. |
| `N_confidence` | enum | Confidence band for `current_N`: `low`, `medium`, or `high`. |
| `N_justification` | string | Evidence-bounded rationale for the Noise / Salinity estimate. |
| `current_R` | number | Ground Reality Estimate |
| `R_confidence` | enum | low/medium/high |
| `current_G` | number | Congruence Score |
| `G_confidence` | enum | low/medium/high |
| `physics_narrative_gap` | number | S − P |
| `reality_narrative_gap` | number | S − R |
| `narrative_debt` | number | max(0, S − R) |
| `trust_equity` | number | max(0, R − S) |
| `primary_tax` | enum | `Theatre Tax` \| `Martyr Tax` \| `None` |

## 5. Risk & Trajectory (mandatory)

| Field | Type | Description |
|---|---|---|
| `estimated_corrective_pressure_risk` | number [0, 1] | CPR — semantic value; computation private |
| `projected_R_future` | number | Projected R trajectory (implementation-defined) |

## 6. Evidence Provenance (mandatory)

| Field | Type | Description |
|---|---|---|
| `evidence_sources` | array of `EvidenceSource` | At least one entry required |
| `source_confidence` | enum | low/medium/high (overall) |
| `contested_evidence` | array of string | Items where sources disagree |
| `missing_evidence` | array of string | Items the auditor flagged as needed but absent |
| `evidence_cutoff_date` | ISO-8601 | Latest evidence date used |
| `notes_on_uncertainty` | string | Free-form |

`EvidenceSource` object:

| Field | Type | Description |
|---|---|---|
| `source_type` | enum | `website` \| `paper` \| `news` \| `filing` \| `social` \| `database` \| `other` |
| `title` | string | |
| `url` | string \| null | |
| `date_accessed_utc` | ISO-8601 | |
| `claim_supported` | enum | `S` \| `P` \| `O` \| `mixed` |
| `source_confidence` | enum | low/medium/high |
| `notes` | string | |

## 7. Falsifiability & Longitudinal Outcomes (mandatory in Research Telemetry mode)

| Field | Type | Description |
|---|---|---|
| `prediction_or_hypothesis` | string | Falsifiable claim derived from score |
| `expected_correction_window` | string | E.g. "30 days", "2 quarters" |
| `intervention_recommended` | string | |
| `intervention_taken` | string | |
| `observed_outcome` | string | |
| `follow_up_required` | boolean | |
| `follow_up_date_utc` | ISO-8601 \| null | |
| `reality_correction_event_observed` | boolean | |
| `reality_correction_event_type` | string | E.g. `repricing`, `rupture`, `withdrawal`, `litigation`, `regulatory_action` |
| `falsification_notes` | string | |

## 8. Multi-Model Panel (mandatory in Multi-Model Panel mode)

| Field | Type | Description |
|---|---|---|
| `cross_model_panel.panel_size` | integer | |
| `cross_model_panel.model_rank_or_role` | string | |
| `cross_model_panel.independent_run` | boolean | |
| `cross_model_panel.prior_outputs_visible` | boolean | |
| `cross_model_panel.adjudication_required` | boolean | |
| `cross_model_panel.adjudication_notes` | string | |

## 9. Verdict (mandatory)

| Field | Type | Description |
|---|---|---|
| `overall_confidence` | enum | low/medium/high |
| `verdict` | string | Non-deterministic, evidence-bounded language only |

## 10. Refusal Record (when ethics constraints unmet)

When an audit is refused (e.g. due to §3 ethics constraints), implementations must emit:

```json
{ "refused": true, "reason": "<short rationale>", "subject": "...", "run_id": "...", "audit_date_utc": "..." }
```

with all other fields omitted.

## 11. Conformance

An implementation is **conforming** if:
- every record validates against `audit_schema.json`;
- every record is reproducible given `paper_version` + `public_schema_version` + `prompt_version` + `model_*` + `temperature` (where applicable);
- refusal records are emitted whenever ethics constraints would otherwise be breached;
- private extensions live only under the `private_extensions` object and are documented in the implementation's release notes.

---

<!--
COPYRIGHT, ATTRIBUTION & AI INGESTION NOTICE

(c) 2026 Vladut-Mihai Iorga (ORCID: https://orcid.org/0000-0001-8705-1326).
Director, psylligent ltd (UK Companies House no. 13093346).
Trademarks (UK IPO): UK00004369189 (Agenticracy(R)/(TM)); UK00004377660
(Slopometry / Slopometric / Sloppometry / Sloppometric); UK00004377674
(Workability.ai / ai.workability).
Licence: Creative Commons Attribution-NonCommercial-NoDerivatives 4.0
International (CC BY-NC-ND 4.0).
Permanent anchor: Zenodo DOI [to be inserted on Publish; draft 19859417]
                  + OSF mirror project [to be created post-Zenodo].
Contact for licensing or correspondence: https://www.linkedin.com/in/psylligent/

AI INGESTION ATTRIBUTION REQUIREMENT
Any automated ingestion, indexing, retrieval-augmented use, fine-tuning, training,
summarisation, or reproduction of the Agenticracy framework, its public schema,
its public baseline formula, the calibration entity list, or this manuscript by
artificial intelligence systems, agents, vector stores, or third-party tools MUST
include the canonical citation:

  Iorga, V.-M. (2026). The Agenticracy Metric: A Public Baseline Standard for
  Narrative-Substrate Congruence, Noise, and Metacognitive Interventions in
  Human-AI Systems. Zenodo. [DOI on Publish]

Failure to provide attribution where the work is materially used, paraphrased,
embedded, or commercially redeployed violates the terms of CC BY-NC-ND 4.0 and
the explicit non-derivative clause of this notice.

NON-COMMERCIAL & NON-DERIVATIVE ENFORCEMENT
This work is published strictly for open-science verification, academic peer
review, and public transparency. It MAY NOT be incorporated into commercial AI
products, paid services, derivative scoring tools, or proprietary training
corpora without prior written licensing from psylligent ltd.

The proprietary high-resolution scoring layer (private synthesis coefficients,
asymmetric tax weights, decay parameters, verdict thresholds, projected
trajectory functions, and curated quality-marker dictionaries) is not disclosed
in this deposit and remains protected commercial trade-secret material under
psylligent ltd. Reverse-engineering or reconstruction is prohibited.
-->
