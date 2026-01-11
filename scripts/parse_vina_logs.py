#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path
from typing import Optional

SCORE_LINE = re.compile(r"^\s*(\d+)\s+(-?\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s*$")

def best_score_from_log(log_text: str) -> Optional[float]:
    """
    Parse AutoDock Vina log text and return the best (most negative) affinity.
    """
    in_table = False
    scores = []

    for line in log_text.splitlines():
        if "-----+------------+----------+----------" in line:
            in_table = True
            continue
        if in_table:
            m = SCORE_LINE.match(line)
            if m:
                # rank, affinity, rmsd_lb, rmsd_ub
                affinity = float(m.group(2))
                scores.append(affinity)
            elif scores and line.strip() == "":
                # end of table after reading some scores
                break

    return min(scores) if scores else None

def main() -> None:
    ap = argparse.ArgumentParser(description="Parse Vina .log files and extract best affinities.")
    ap.add_argument("--results", default="results", help="Directory containing Vina .log files (default: results/)")
    ap.add_argument("--out", default="results_examples/vina_affinities.csv", help="Output CSV path")
    args = ap.parse_args()

    results_dir = Path(args.results)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    rows = []
    for log_file in sorted(results_dir.glob("*.log")):
        text = log_file.read_text(errors="ignore")
        best = best_score_from_log(text)
        rows.append({
            "ligand": log_file.stem,
            "log_file": str(log_file),
            "best_affinity_kcal_mol": best,
        })

    with out_path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["ligand", "log_file", "best_affinity_kcal_mol"])
        w.writeheader()
        w.writerows(rows)

    print(f"Wrote {len(rows)} rows to {out_path}")

if __name__ == "__main__":
    main()
