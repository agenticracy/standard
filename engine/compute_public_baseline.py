#!/usr/bin/env python3
"""Compute reproducible Agenticracy public baseline scores.

Formula:
  R_public = (P + O) / 2
  D_public = max(0, S - R_public)
  G_public = clamp(1.0, 10.0, R_public - 0.5 * D_public - 0.25 * N)

This script intentionally does not compute G_private, CPR, ETA-to-correction, or any
protected nonlinear commercial score.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


def clamp(lo: float, hi: float, x: float) -> float:
    return min(hi, max(lo, x))


def compute_public_baseline(S: float, P: float, O: float, N: float) -> dict[str, float | str | bool]:
    R_public = (P + O) / 2.0
    D_public = max(0.0, S - R_public)
    G_public = clamp(1.0, 10.0, R_public - 0.5 * D_public - 0.25 * N)
    return {
        "engine_type": "public_baseline",
        "R_public": round(R_public, 3),
        "D_public": round(D_public, 3),
        "G_public": round(G_public, 3),
        "private_scores_withheld": True,
    }


def extract_scores(record: dict[str, Any]) -> tuple[float, float, float, float] | None:
    parsed = record.get("parsed_output") or record
    scores = parsed.get("scores") or {}
    try:
        return float(scores["S"]), float(scores["P"]), float(scores["O"]), float(scores["N"])
    except Exception:
        return None


def enrich_record(path: Path) -> dict[str, Any] | None:
    record = json.loads(path.read_text())
    vals = extract_scores(record)
    if vals is None:
        return None
    S, P, O, N = vals
    baseline = compute_public_baseline(S, P, O, N)
    parsed = record.get("parsed_output")
    if isinstance(parsed, dict):
        parsed.update(baseline)
        record["parsed_output"] = parsed
    record["public_baseline"] = baseline
    return record


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input-dir", required=True)
    ap.add_argument("--output-dir", required=True)
    args = ap.parse_args()

    inp = Path(args.input_dir)
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    rows = []
    for path in sorted(inp.glob("*.json")):
        enriched = enrich_record(path)
        if not enriched:
            continue
        out_path = out / path.name
        out_path.write_text(json.dumps(enriched, indent=2, default=str))
        b = enriched["public_baseline"]
        rows.append({
            "cell_id": enriched.get("cell_id"),
            "provider": enriched.get("provider"),
            "condition_id": enriched.get("condition_id"),
            "R_public": b["R_public"],
            "D_public": b["D_public"],
            "G_public": b["G_public"],
            "engine_type": b["engine_type"],
            "private_scores_withheld": b["private_scores_withheld"],
        })
    with (out / "public_baseline_summary.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else [])
        if rows:
            writer.writeheader(); writer.writerows(rows)
    print(json.dumps({"records_enriched": len(rows), "output_dir": str(out)}, indent=2))


if __name__ == "__main__":
    main()
