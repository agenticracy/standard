---
created: 2026-04-28
last_edited: 2026-04-28
version: 1.0
provenance: con_okeqBprC3TORMbOv
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


# Agenticracy Public Baseline Engine v1.0

## Purpose

This document defines the reproducible public scoring engine used for the Agenticracy Metric v4.9.6-preprint validation dataset.

The public baseline engine is deliberately simple, transparent, and hand-calculable. It is designed for:

- peer-review reproducibility
- inter-rater comparison
- JSON-LD interoperability
- open scientific criticism
- baseline validation of the Agenticracy semantic constructs

It is not the high-resolution private/commercial implementation.

## Public Inputs

All public baseline scores are computed from four elicited variables on a 1.0–10.0 scale:

| Symbol | Construct | Valence |
|---|---|---|
| `S` | Narrative strength / claim intensity | higher = stronger/louder claim |
| `P` | Physical / operational / financial substrate | higher = stronger substrate |
| `O` | Observer validation / stakeholder regard | higher = stronger independent validation |
| `N` | Noise / salinity / signal contamination | higher = more contamination, hype, opacity, or distortion |

## Public Formula

```text
R_public = (P + O) / 2
D_public = max(0, S - R_public)
G_public = clamp(1.0, 10.0, R_public - 0.5 * D_public - 0.25 * N)
```

Where:

```text
clamp(1.0, 10.0, x) = min(10.0, max(1.0, x))
```

## Interpretation

- `R_public` estimates the publicly grounded reality surface from substrate and observer validation.
- `D_public` estimates Narrative Debt: the positive gap between narrative strength and grounded reality.
- `G_public` estimates public baseline congruence after applying transparent penalties for Narrative Debt and Noise/Salinity.

## Boundary to Private Implementations

Private or commercial implementations may compute higher-resolution scores, including but not limited to:

- nonlinear salinity effects
- ratio-damped or exponential decay
- observer-drag transforms
- temporal decay and trajectory models
- CPR / estimated corrective-pressure risk
- ETA-to-correction estimates
- proprietary verdict bands

These are not required to reproduce the public validation dataset and are not part of the public baseline engine.

Public records should disclose `engine_type`. For this paper and validation package, public records use:

```json
{ "engine_type": "public_baseline" }
```

## Publication Rule

Any public table, Zenodo/OSF dataset, JSON-LD example, or academic replication material must label public scores as `R_public`, `D_public`, and `G_public`.

Private scores must not be published as public baseline scores.

## v2.7 Addendum — Symmetric Public Model + Cost-Quality

The public Agenticracy model is symmetric. It identifies five public state classes:

| state_class | meaning |
|---|---|
| extractive_extreme | S substantially exceeds P; over-broadcasting without substrate |
| congruent_center | S, P, O within a narrow band; low N |
| pathological_humility | P substantially exceeds S; real substrate hoarded; under-broadcasting |
| noise_dominant | high N drowns signal even when S/P aligned |
| ambiguous_mixed | contested or oscillating evidence |

And six public action classes: `reduce_S`, `increase_P`, `increase_S`, `reduce_N`, `maintain`, `mixed`.

**Cost-quality block** (publicly published with every audit record):

| field | meaning |
|---|---|
| input_tokens, output_tokens, reasoning_tokens, total_tokens | token counts |
| latency_seconds | wall-clock latency |
| cost_usd | provider cost |
| reasoning_text_chars | length of exposed reasoning trace |
| condition_id | C1 / C2 / C3 |

Cost-quality enables a defensible public claim:
*"The Agenticracy metacognitive condition (C3) imposes a measurable compute premium
of X% over baseline freeform (C1) and Y% over neutral structured (C2), and produces
a measurable quality delta of ΔS, ΔP, ΔO, ΔN, ΔG_public, plus reduced sycophancy/halo
markers and improved classification F1 against ground-truth labels."*

The compute-vs-quality trade-off is a public, replicable, reportable metric. The
proprietary `quality_private` and the proprietary classification engine remain
trade-secret.

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
