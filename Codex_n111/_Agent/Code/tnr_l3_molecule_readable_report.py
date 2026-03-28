#!/usr/bin/env python3
"""
Readable L3 molecule report
===========================

Human-facing and AI-facing report for the canonical molecular layer.

Design principles:
  1. Show the bare bond carrier first.
  2. Show the local topology-corrected state second.
  3. Show the environment multiplier explicitly.
  4. Show the final value and the final precision last.

This keeps the molecular layer readable as a staged construction rather than
an opaque one-line energy formula.

Usage:
  python3 tnr_l3_molecule_readable_report.py
  python3 tnr_l3_molecule_readable_report.py --name "H₂O"
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from tnr_comprehensive_engine import (  # noqa: E402
    MOLECULES,
    build_l3_molecule_breakdown,
)


def all_breakdowns():
    return [build_l3_molecule_breakdown(entry) for entry in MOLECULES]


def print_catalog(rows):
    print("=" * 176)
    print("  TNR L3 MOLECULE READABLE REPORT")
    print("  Columns: bare carrier -> local topology correction -> environment multiplier -> final bond energy")
    print("=" * 176)
    print(
        f"  {'Mol':<8} {'Family':<15} {'Role/mode':<26} "
        f"{'Bare eV':>10} {'Bare err%':>10} "
        f"{'Local eV':>10} {'Local err%':>11} "
        f"{'Env ×':>10} {'Env ΔeV':>10} "
        f"{'Final eV':>10} {'Final err%':>11}"
    )
    print("  " + "-" * 170)
    for row in rows:
        print(
            f"  {row['name']:<8} {row['topology_family']:<15} "
            f"{row['topology_role'] + '/' + row['pair_mode']:<26} "
            f"{row['bare_ev']:>10.4f} {row['bare_error_pct']:>+9.3f}% "
            f"{row['local_ev']:>10.4f} {row['local_error_pct']:>+10.3f}% "
            f"{row['env_multiplier']:>10.6f} {row['env_delta_ev']:>+10.4f} "
            f"{row['final_ev']:>10.4f} {row['final_error_pct']:>+10.3f}%"
        )


def print_single(row):
    print("=" * 104)
    print(f"  {row['name']}")
    print("=" * 104)
    print(f"  Topology family     : {row['topology_family']}")
    print(f"  Role / mode         : {row['topology_role']} / {row['pair_mode']}")
    print(f"  Bare formula        : {row['bare_formula']}")
    print(f"  Local formula       : {row['local_formula']}")
    print(f"  Experimental value  : {row['exp_ev']:.6f} eV")
    print(f"  Bare value          : {row['bare_ev']:.6f} eV   ({row['bare_error_pct']:+.6f}%)")
    print(f"  Local value         : {row['local_ev']:.6f} eV   ({row['local_error_pct']:+.6f}%)")
    print(f"  Local delta         : {row['local_delta_ev']:+.6f} eV")
    print(f"  Environment ×       : {row['env_multiplier']:.9f}")
    print(f"  Environment delta   : {row['env_delta_ev']:+.6f} eV")
    print(f"  Final value         : {row['final_ev']:.6f} eV   ({row['final_error_pct']:+.6f}%)")
    print(f"  Period              : {row['period']}   shell depth={row['period_shell_depth']}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="Inspect a single molecule by exact display name")
    args = parser.parse_args()

    rows = all_breakdowns()
    if args.name:
        for row in rows:
            if row["name"] == args.name:
                print_single(row)
                return
        raise SystemExit(f"Molecule not found: {args.name}")

    print_catalog(rows)


if __name__ == "__main__":
    main()
