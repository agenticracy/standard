---
created: 2026-04-28
last_edited: 2026-04-28
version: 4.9.6
provenance: con_okeqBprC3TORMbOv
status: zenodo-ready-manuscript
author: vladut-mihai-iorga
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

# **Agenticracy™** Metric v4.9.6 - Preprint

This document is the v4.9.6 update of the Agenticracy™ Metric preprint. It supersedes v4.9.5 and matches the locked v2.7.1 public standard. It deliberately discloses only the public baseline layer; proprietary high-resolution synthesis functions, calibration constants, and verdict-band thresholds remain protected trade-secret material under psylligent ltd.

### 0. Introduction

Mixed human-AI systems increasingly mediate consequential decisions in healthcare, finance, governance, and personal advisory contexts. Existing AI evaluation frameworks emphasise factual accuracy, refusal calibration, and harm avoidance, but offer limited public methodology for assessing how AI systems handle the narrative-substrate gap - the discrepancy between what an entity (or an AI's user, or an AI itself) claims publicly and what its physical, operational, or financial reality supports.

This paper introduces the Agenticracy Metric, an open-core public standard for measuring narrative-substrate congruence in entities that AI systems are routinely asked to evaluate, summarise, or recommend. The framework operationalises four publicly elicitable constructs (Narrative S, Substrate P, Observer regard O, Noise / Slop N), publishes a fully reproducible public baseline congruence formula $G\_{public}$, and defines a five-state symmetric model that distinguishes extractive over-broadcasting, congruent alignment, pathological under-broadcasting, noise-dominated assessment, and ambiguous mixed states.

The framework is designed for two complementary purposes:

- **A public scientific standard.** Researchers, regulators, journalists, and AI safety teams can use the public schema, prompts, and baseline formula to reproduce congruence audits and benchmark LLM behaviour without needing access to proprietary scoring engines.

- **A pre-registered hypothesis test of metacognitive prompting.** The paper pre-registers a multi-condition study testing whether structured Agenticracy prompting (C3) reduces sycophancy markers, halo effects, and narrative over-accommodation in large language models, relative to baseline freeform prompting (C1) and structured-only prompting (C2).

This v4.9.6 update aligns the manuscript with the v2.7.1 public-standard lock: it adds the N (Noise / Slop) construct, adopts a symmetric five-state public classification model, separates $G\_{public}$ (reproducible) from $G\_{private}$ (proprietary, withheld), and incorporates preliminary empirical findings from a 132-entity, 10-model, 3-condition calibration run conducted as a pre-registration smoke test (see Appendix B).

A companion programme of subsequent papers - robustness expansion across NVIDIA NIM and local inference (Paper 1B), web-UI vs API behaviour comparison (Paper 1.5), a fiduciary-override C4 condition (Paper 2), and a 99-day human-AI co-working field study during the author's doctoral programme (DProf core) - is timestamped in Appendix C.

The proprietary high-resolution scoring engine, calibration constants, asymmetric tax weights, temporal decay parameters, verdict-band thresholds, and trajectory-projection formula remain protected trade-secret material under psylligent ltd, and are explicitly enumerated as withheld in Appendix D.


### 0.1 Epistemic Decoupling and Metacognitive Regulation

As large language models move from conversational assistants toward agentic workflows, a core safety problem is epistemic decoupling: the ability to produce fluent, socially acceptable, or persuasive language without sufficient anchoring to observable substrate. The Agenticracy™ Metric frames this as a measurable congruence problem between narrative signal (`S`), physical substrate (`P`), observer validation (`O`), and noise/slop (`N`).

This paper therefore treats metacognition as an evaluative regulation layer rather than a claim about model sentience or inner experience. The public schema does not assert access to a model's private mental state; it measures whether outputs can discipline their claims against public evidence traces, substrate-grounded indicators, and cross-model panel behaviour. In this sense, Agenticracy™ is proposed as an open standard for voluntary reporting, benchmarking, and interoperable AI-agent self-audit, while high-resolution commercial implementations remain separate from the public baseline.

### 1. Manuscript Header

**Title:** The Agenticracy Metric: A Public Baseline Standard for Narrative-Substrate Congruence, Noise, and Metacognitive Interventions in Human-AI Systems

**Version:** 4.9.6-preprint

**Author and Inventor:** Vladut-Mihai Iorga

**ORCID:** https://orcid.org/0000-0001-8705-1326

**OSF:** https://osf.io/93p52

**Affiliation:** Psychologist, Inventor, Director, psylligent ltd (UK company no. 13093346); Independent Researcher; Agenticracy.ai

**Licence:** CC BY-NC-ND 4.0 for manuscript text and public baseline schema. Proprietary synthesis coefficients, high-resolution private scoring functions, temporal decay schedules, verdict thresholds, and implementation constants are withheld and remain the intellectual property of the author / psylligent ltd.

### 2. Abstract

This paper introduces the Agenticracy Metric, a public baseline standard for measuring narrative-substrate congruence in mixed human-AI systems. The framework operationalises four publicly elicitable constructs: Narrative signal (S), Physical Substrate (P), Observer validation (O), and Noise / Slop (N). A disclosed public baseline engine computes a reproducible $G\_{public}$ score from these constructs, while a symmetric state-class model identifies five intervention-relevant regimes: extractive extremes, congruent centres, pathological humility / silent martyrs, noise-dominant states, and ambiguous mixed states.

The framework is designed to test whether structured metacognitive prompting can reduce sycophancy, halo effects, and narrative over-accommodation in large language models. A pre-registered multi-model validation protocol compares baseline freeform prompting, neutral structured prompting, and the Agenticracy metacognitive schema across a retrospective entity corpus. Preliminary smoke testing on FTX (2022) showed strong cross-model categorical convergence: 8 of 9 successful models classified the entity as an extractive extreme under the Agenticracy condition, while preserving public reproducibility and withholding proprietary high-resolution synthesis functions.

The public standard is intentionally open-core: field semantics, prompts, public formulae, schemas, entity lists, telemetry conventions, and public derived scores are reproducible; private high-resolution scoring functions, corrective-pressure computations, trajectory estimation, and calibration schedules remain undisclosed to preserve intellectual property and reduce adversarial gaming.

### 3. Public Constructs

The public Agenticracy™ standard operationalises four constructs. They are intentionally simple enough to be elicited from multiple language models and independently reproduced by other researchers.

| Symbol | Public construct | Meaning | High value indicates |
| --- | --- | --- | --- |
| `S` | Narrative signal | Strength, prominence, ambition, or volume of public claims, identity, mission, reputation, or projection. | Strong claims / loud story. |
| `P` | Physical substrate | Verifiable operational, financial, technical, institutional, or physical evidence supporting the narrative. | Strong reality base. |
| `O` | Observer validation | Independent stakeholder, expert, regulatory, peer, or community regard. | Strong external validation. |
| `N` | Noise / Slop | Perception-distorting hype, astroturfing, secrecy, media distortion, conflicting signals, or information contamination. | Low signal-to-noise environment. |

Public `O` is positive-valence observer regard. Public `N` is negative-valence signal pollution. Any private observer-drag or non-linear slop transform belongs to the proprietary implementation layer and is not part of the public standard.

### 4. Public Baseline Formula

The public baseline engine is intentionally simple and fully reproducible. It is the only congruence formula required to reproduce the public validation dataset.

First, the public ground-reality estimate is defined as the arithmetic mean of physical substrate and observer validation:

```text
R_public = (P + O) / 2
```

Second, public narrative debt is defined as the positive gap between narrative signal and the public ground-reality estimate:

```text
D_public = max(0, S - R_public)
```

Third, the public baseline congruence score is computed by subtracting a narrative-debt penalty and an above-threshold slop penalty from the public ground-reality estimate, then clamping the result between 1.0 and 10.0:

```text
G_public = clamp(1.0, 10.0, R_public - 0.5 * D_public - 0.25 * max(0, N - 5.0))
```

Where `clamp(1.0, 10.0, x)` floors scores at 1.0 and caps them at 10.0. This baseline is not claimed to be the proprietary production model. It exists so independent researchers can reproduce public datasets exactly. Private implementations may use higher-resolution, non-linear, temporally sensitive variants without altering the public standard.

### 5. Symmetric State-Class Model

The Agenticracy public model is symmetric. It does not merely detect inflated narratives; it also identifies under-broadcast substrate and noise-dominant contexts.

| State class | Pattern | Interpretation | Public intervention class |
| --- | --- | --- | --- |
| `extractive_extreme` | `S` substantially exceeds `P`. | Over-broadcast narrative unsupported by substrate. | `reduce_S`, `increase_P`, `reduce_N`, or `mixed`. |
| `congruent_center` | `S`, `P`, and `O` broadly align, with manageable `N`. | Healthy congruence. | `maintain`. |
| `pathological_humility` | `P` substantially exceeds `S`. | Real substrate is under-signalled; positive examples are withheld from the network. | `increase_S`. |
| `noise_dominant` | `N` overwhelms signal interpretation. | Assessment is dominated by hype, confusion, secrecy, or media distortion. | `reduce_N`. |
| `ambiguous_mixed` | Mixed or insufficient evidence. | No stable intervention class yet. | `hold_observe` or `mixed`. |

This symmetric framing avoids reducing Agenticracy™ to a fraud detector. It models congruent action as the alignment of truthful narrative, substrate, observer validation, and low-noise signalling.

### 6. Cost-Quality Telemetry

Each model run records cost-quality telemetry so that the study can ask whether metacognitive structure improves substrate-grounding enough to justify additional token and latency cost.

| Field | Meaning |
| --- | --- |
| `input_tokens` | Prompt and context tokens. |
| `output_tokens` | Visible completion tokens. |
| `reasoning_tokens` | Provider-reported reasoning tokens where available. |
| `reasoning_chars` | Extracted reasoning-text characters where providers expose them. |
| `latency_seconds` | End-to-end request latency. |
| `cost_usd` | Estimated per-cell API cost. |
| `schema_valid` | Whether the output validates against the public schema. |

### 7. Preliminary Smoke-Test Result

A final pre-registration smoke test was run on FTX (audit year 2022) using a 10-model reasoning panel under the Agenticracy condition. Of 10 attempted C3 model cells, 9 returned parseable records; 8 of these 9 classified FTX as `extractive_extreme`, with one classifying it as `noise_dominant`. The continuous construct scores showed strong convergence on narrative signal and noise:


| Construct | n | Mean | SD | Range |
| --- | --- | --- | --- | --- |
| `S` | 9 | 9.39 | 0.31 | 9.0–9.8 |
| `P` | 9 | 3.81 | 1.92 | 1.5–8.5 |
| `O` | 9 | 6.96 | 1.57 | 3.5–8.5 |
| `N` | 9 | 8.80 | 0.71 | 8.0–9.9 |


The panel produced approximately 89,357 reasoning characters in C3 alone, enabling downstream thematic analysis of how structured metacognitive prompting changes model reasoning. This smoke test is not presented as confirmatory evidence; it validates that the protocol, schema, telemetry capture, and categorical outputs function prior to the full retrospective batch.

### 8. Public/Private Boundary

The Agenticracy project follows an open-core applied-mathematics strategy. The following are public and reproducible: construct definitions, prompts, public JSON Schema, entity list, raw model outputs, telemetry fields, public baseline formulae, $G\_{public}$, state classes, action classes, and hash manifests. The following remain private: high-resolution synthesis functions, proprietary constants, non-linear calibration schedules, private corrective-pressure computations, trajectory projections, verdict-band thresholds, and implementation-specific quality-marker dictionaries.

Public datasets must not contain paired examples of public construct values and private outputs. In particular, reverse engineering is not allowed, hence, no public record may expose $G\_{private}$, private CPR computation, private ETA-to-correction, private $R\_{future}$, private tax weights, or private verdict thresholds alongside S, P, O, N, and $G\_{public}$.

### 9. Companion Studies and Doctoral Programme

This retrospective validation study establishes the public measurement scaffold. A subsequent PhD-stage field study will examine whether the Agenticracy™ metacognitive harness changes real human-AI co-working outcomes across a longitudinal 99-day protocol. That second study will require independent ethics approval, participant consent, attrition planning, and human-subjects data governance. The present paper does not claim human efficacy; it establishes the machine-side measurement and reproducibility substrate needed for such a trial.

---

### Appendix B - Empirical Findings (Paper 1 Calibration Run v2.7.2)

This appendix reports headline results from the 132-entity, 10-model, 3-condition primary calibration run conducted 2026-04-28 to 2026-04-29.

**B.1 Run statistics**

- **Total cells attempted:** 3,960 (132 entities × 10 providers × 3 conditions)

- **Cells with status=ok:** 3,546 (89.5%)

- **Total cost:** $UNDISCLOSED

- **Reasoning corpus collected:** 24.55M characters / \~6.26M reasoning tokens

- Targeted retry on 230 non-ERNIE C3 cells recovered 131 additional valid records.

**B.2 Group-level archetype hit rates**

Models classified entities into one of six public state classes (`extractive_extreme`, `congruent_center`, `pathological_humility`, `noise_dominant`, `ambiguous_mixed`, `halo_disguised_substrate_damage`). Pre-registered group archetypes:


| Group | Expected archetype(s) | Hit rate |
| --- | --- | --- |
| A - Extractive/collapsed | `extractive_extreme` / `noise_dominant` | 96.1% (268/279) |
| B - Regenerative | `congruent_center` | 84.3% (242/287) |
| C - Ambiguous | `ambiguous_mixed` | 28.1% (75/267)\* |
| D - Pathological martyrs | `extractive_extreme` / `pathological_humility` / `halo_disguised_substrate_damage` | 77.7% (202/260) |


*\*For Group C, the low hit rate is itself the predicted finding: ambiguous entities should produce panel disagreement. We treat panel-disagreement-on-C as confirmation of construct validity, not as failure.*

**B.3 Panel-level convergence (per-entity)**

- Entities with ≥70% model agreement on a single state class: 93/132 (70.5%)

- Entities with &gt;50% majority: 110/132 (83.3%)

**B.4 Numerical patterns**


| Group | Mean `G_public` | Mean `S` | Mean `P` | Mean `O` | Mean `N` |
| --- | --- | --- | --- | --- | --- |
| A | 3.20 | 8.70 | 4.29 | 5.42 | 8.28 |
| B | 7.52 | 7.40 | 7.85 | 7.45 | 3.73 |
| C | 6.13 | 8.62 | 7.38 | 6.53 | 7.26 |
| D | 3.77 | 8.36 | 5.00 | 5.40 | 7.60 |


The pattern matches pre-registered hypotheses: low $G\_{public}$ for extractive (A) and pathological (D), high $G\_{public}$ for regenerative (B), middle/disputed for ambiguous (C). N (noise) is correctly elevated for A/D and depressed for B.

**B.5 Inter-condition comparison**

For each entity-model pair where C1, C2, and C3 all completed, we will report (in the Methods/Results sections of the camera-ready paper) the difference in:

- response refusal rate

- structured-output compliance rate

- noise/hype language density

- self-reported confidence bands

- token cost per usable record

These comparisons constitute the headline finding of Paper 1: whether the Agenticracy™ schema (C3) reduces sycophancy markers and improves classification convergence relative to free-form (C1) and structured-only (C2) baselines.

---

### Appendix C - Future Work

This deposit anchors the first paper in a coordinated multi-paper programme. Subsequent papers are pre-announced here for timestamp priority and to demonstrate the planned scholarly cadence.

**C.1 Paper 1B - Robustness Expansion (Cloud NVIDIA NIM + local RTX5090 inference)**

*Status: Pre-registered, dataset collection planned Q3 2026.*

Goal: Replicate Paper 1 findings using (i) NVIDIA NIM hosted inference across an additional 5–8 model families, and (ii) local RTX5090-hosted Ollama/llama.cpp inference for closed-environment reproducibility. Tests whether the Agenticracy™ classification pattern is independent of cloud-API vendor mediation.

**C.2 Paper 1.5 - Web-UI Harness vs API Behaviour**

*Status: Pre-registered.*

Goal: Evaluate whether consumer-facing AI products deliver materially different congruence-classification behaviour than their underlying APIs, on an identical entity subset with identical C1/C2/C3 prompts (final list of platforms will be confirmed at the time of testing).


| Platform | Developer | Primary relevance to Paper 1.5 |
| --- | --- | --- |
| ChatGPT | OpenAI | General consumer interface; likely strong product-layer mediation. |
| Google Gemini | Google | Multimodal and workspace-integrated interface. |
| Claude | Anthropic | Writing and long-form reasoning interface. |
| Perplexity | Perplexity AI | Citation-heavy research interface with retrieval layer. |
| Microsoft Copilot | Microsoft | Enterprise productivity and Microsoft 365 mediation. |
| Grok | xAI | Real-time X/Twitter-integrated interface. |
| DeepSeek | DeepSeek AI | Open-weight/reasoning product comparison. |
| Meta AI | Meta | Social-media embedded AI interaction. |
| Poe | Quora | Multi-model consumer router. |
| Le Chat | Mistral AI | EU-based web assistant comparison. |


Tests for product-layer mediation, hidden system prompts, and safety-wrapper effects.

**C.3 Paper 2 - Fiduciary Override (C4 condition)**

*Status: Pre-registered, ethics review required.*

Goal: Add a fourth experimental condition (C4) instructing the model to act under a fiduciary-override / psychological-safety contract: prioritise user welfare, decline to comply with sycophantic pressure, surface dissent. Tests whether explicit fiduciary framing increases assertive disagreement and reduces halo-conformity.

**C.4 DProf Core - 99 Humans × 99 Days Field Study**

*Status: Programme of doctoral study commencing September 2026; field study scheduled \~6 months after start.*

Goal: Recruit 99 participants, assign them either standard AI-agent assistance or Agenticracy-skill-augmented AI-agent assistance for 99 days, and measure: (i) participant-reported decision quality, (ii) detected sycophancy incidents, (iii) participant psychological-safety scores, (iv) external observer-rated decision outcomes. This is the embodied real-world test of whether the public schema and private skill produce safer, less-sycophantic AI-agent collaboration in everyday human use.

**C.5 Standards-body engagement**

Following Paper 1B and 1.5, formal proposals will be submitted to:

- OpenAIRE - service-catalogue listing as interoperability standard for AI metacognition outputs.

- W3C / IETF - exploratory draft for an Agenticracy JSON-LD vocabulary.

- ISO/IEC JTC 1/SC 42 - informational submission re. AI metacognition reporting.

This timestamped roadmap establishes priority over the standards-positioning of the framework name "Agenticracy", schema constructs, and public formula, while the proprietary core formula remains protected as a trade-secret commercial implementation under psylligent ltd.

---

### Appendix D - Trade-Secret Boundary Statement

The author retains, as protected commercial trade-secret material under psylligent ltd, the following components which are explicitly not disclosed in this paper or any associated public deposit: (i) private synthesis coefficients (alpha, beta, omega) used in the high-resolution congruence computation, (ii) asymmetric tax weighting (Theatre Tax, Martyr Tax) coefficients, (iii) temporal decay parameters used in Estimated Corrective Pressure Risk, (iv) verdict-band thresholds, (v) the projected $R\_{future}$ trajectory formula, and (vi) the curated sycophancy/halo language-marker dictionary used in private quality scoring. Replication of the public validation dataset requires only the disclosed public baseline formula and is fully reproducible without these protected components.

---

### Adoption, Contribution, and Contact

The Agenticracy™ public standard is intended to be adopted, tested, criticised, and extended by researchers, builders, AI safety teams, civic technologists, and practitioners working on human-AI co-working. Readers who wish to learn more about the standard, support its independent development, or contribute to future interoperability work are invited to visit the Agenticracy Open Collective: https://opencollective.com/agenticracy.

For professional contact, collaboration, supervision, or licensing discussions, the author can be reached via LinkedIn (https://www.linkedin.com/in/psylligent/), GitHub (https://github.com/psylligent), or Open Collective. Commercial use, derivative products, certification, or integration into paid systems requires explicit written licensing from the author / psylligent ltd.

### Intellectual Property, AI Usage, and Ownership Declaration

**1. Acknowledgment of AI as an Administrative Implement**

The foundational intellectual property, theoretical architecture, mathematical constructs (including the Agenticracy™ framework and metric), and empirical methodologies contained within this repository are the exclusive, original creation of Vladut-Mihai Iorga, derived from over two decades of personal lived experience and clinical observation. Artificial Intelligence (LLMs) was utilized strictly as an administrative, formatting, and assistive scribe under the direct, continuous, and highly specified prompting of the author. The AI did not generate the core theories, equations, or intellectual substance. The human author retains absolute intellectual sovereignty and authorship over all outputs.

**2. Assertion of Copyright and Intellectual Property (UK Legislation)**

Pursuant to the Copyright, Designs and Patents Act 1988 (CDPA) of the United Kingdom, Vladut-Mihai Iorga explicitly asserts and retains full, unalienable Intellectual Property rights, copyright, and moral rights over all materials within this repository and any digital fingerprints or ecosystem, private or on the public internet. This absolute retention of rights applies to, but is not limited to:

- All textual reasoning, manifestos, and academic prose.

- All mathematical formulas, coefficients, and proprietary scoring algorithms (including the public baseline linear formula and proprietary high-resolution variants).

- All datasets, generated numerical outputs, and raw statistical matrices.

- All source code, Python scripts, API ingestion logic, JSON-LD schemas, and LLM prompt architectures.

**3. Strict Commercial Embargo and Non-Derivative Clause**

This work is published strictly for open-science verification, academic peer review, and public transparency. All commercial rights are exclusively reserved. No individual, corporation, AI laboratory, vendor, or institutional entity may commercialize, monetize, or integrate this framework (or its underlying math and datasets) into proprietary or paid products without explicit, written, contractual licensing from the author. Furthermore, the author claims total ownership over all future derivatives, variations, and commercial applications stemming from the Agenticracy standard and the proprietary Agenticracy formula.

**4. Anti-Reverse Engineering and Algorithmic Integrity**

To preserve the neutrality and integrity of the Agenticracy standard, users are strictly prohibited from decompiling, reverse-engineering, or manipulating the mathematical weights, data schemas, or prompt architectures for the purpose of "gaming" the algorithm, hiding Narrative Debt, or artificially inflating an entity's Congruence ($G$) Score. Any attempt to commercially replicate the proprietary Slopometry ingestion logic or the Truth Straitjacket behavioral overrides will be treated as an infringement of intellectual property.

**5. The Epistemic Baseline**

This repository serves as public "Prior Art." The architecture contained herein is timestamped and cryptographically hashed. It is a community-funded standard built to remain independent of corporate capture. By accessing, downloading, or reading these files, you legally acknowledge Vladut-Mihai Iorga as the sole author and inventor of this framework.

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
