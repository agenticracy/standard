# Agenticracy™ Public Standard

**A public baseline schema and metacognitive evaluation protocol for reality-grounded AI outputs.**

Agenticracy™ provides a reproducible public standard for evaluating narrative-substrate congruence in organisations, claims, systems, and human-AI workflows. It is designed to test whether structured metacognitive prompting reduces sycophancy, halo effects, and narrative over-accommodation in large language model outputs.

> Public standard: open for research, replication, and voluntary adoption.  
> Proprietary layer: AgenticracyXQ™ and high-resolution private scoring remain reserved for authorised commercial use via Workability.ai / psylligent ltd.

## Key empirical result

Paper 1 evaluated **132 entities × 10 model providers × 3 prompt conditions = 3,960 cells**. The public Agenticracy schema produced strong archetype separation in the merged calibration dataset:

| Group | Intended archetype | Hit rate |
|---|---|---:|
| A | Extractive / collapsed systems | 96.1% |
| B | Regenerative / substrate-anchored systems | 84.3% |
| C | Ambiguous / contested systems | Panel disagreement expected |
| D | Pathological humility / halo-disguised dysfunction | 77.7% |

The dataset includes cost-quality telemetry, structured outputs, public derived scores, and model reasoning where providers exposed it.

## Public constructs

| Symbol | Construct | Meaning |
|---|---|---|
| `S` | Narrative signal | Strength, prominence, ambition, or public projection |
| `P` | Physical substrate | Verifiable operational, financial, institutional, or technical evidence |
| `O` | Observer validation | Independent stakeholder, expert, peer, regulatory, or community regard |
| `N` | Noise / slop | Perception-distorting hype, secrecy, astroturfing, contradiction, or low signal-to-noise |

## Public baseline formula

```text
R_public = (P + O) / 2
D_public = max(0, S - R_public)
G_public = clamp(1.0, 10.0, R_public - 0.5 * D_public - 0.25 * max(0, N - 5.0))
```

This public baseline exists for reproducibility. It is **not** the proprietary AgenticracyXQ™ engine.

## Repository structure

```text
schema/      Public JSON Schema and human-readable field definitions
prompts/     C1/C2/C3 public experimental prompts
engine/      Public baseline engine and formula notes
examples/    Public example audit record
paper/       Paper 1 preprint manuscript
```

## Public vs reserved

Public and reproducible:

- construct definitions (`S/P/O/N`)
- public schema
- public baseline formula
- state/action classes
- prompts C1/C2/C3
- public example records
- public telemetry conventions

Reserved / not disclosed:

- AgenticracyXQ™ high-resolution scoring
- private synthesis constants
- private corrective-pressure computations
- private trajectory / ETA computations
- proprietary quality-marker dictionaries
- commercial audit, certification, or managed implementation services

## Citation

Use `CITATION.cff` or cite the forthcoming Zenodo DOI once issued.

## Contact

- LinkedIn: https://www.linkedin.com/in/psylligent/
- GitHub: https://github.com/psylligent
- OpenCollective: https://opencollective.com/agenticracy
