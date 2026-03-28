#!/usr/bin/env python3
"""
Readable L1 particle report
===========================

Human-facing and AI-facing report for the particle layer.

Design principles:
  1. Show the bare carrier first.
  2. Show the shifted value (after δ₀ + Ω) separately.
  3. Show the residual tail explicitly as a small correction.
  4. Show the final value and the final precision.

This makes it obvious that the long formula is not arbitrary fitting:
the tail acts on a much larger carrier and usually changes less than a
small fraction of the total mass.

Theory note:
  the particle layer is read in four stages:
    bare carrier -> shifted carrier -> residual tail -> final value.
  This script exists to keep those stages visible instead of collapsing
  them into one opaque closed formula.

Why this report exists:
  a giant closed formula looks like fitting;
  a staged report shows the opposite:
    bare carrier -> shifted carrier -> residual tail -> final value.

Usage:
  python3 tnr_l1_particle_readable_report.py
  python3 tnr_l1_particle_readable_report.py --name "Pion (π⁰)"
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from tnr_comprehensive_engine import (  # noqa: E402
    L1_PARTICLE_SPECS,
    build_l1_particle_breakdown,
)


def all_breakdowns():
    return [build_l1_particle_breakdown(spec) for spec in L1_PARTICLE_SPECS]


def print_catalog(rows):
    print("=" * 152)
    print("  TNR L1 PARTICLE READABLE REPORT")
    print("  Columns: bare carrier -> shifted state -> tail delta -> final observed value")
    print("=" * 152)
    print(
        f"  {'Particle':<18} {'Cat':<13} {'Bare formula':<18} "
        f"{'Bare MeV':>12} {'Bare err%':>11} "
        f"{'Shifted MeV':>13} {'Shift err%':>12} "
        f"{'Tail ×':>10} {'Tail ΔMeV':>12} "
        f"{'Final MeV':>12} {'Final err%':>11}"
    )
    print("  " + "-" * 146)
    for row in rows:
        print(
            f"  {row['name']:<18} {row['category']:<13} {row['bare_formula']:<18} "
            f"{row['bare_mev']:>12.6f} {row['bare_error_pct']:>+10.4f}% "
            f"{row['shifted_mev']:>13.6f} {row['shifted_error_pct']:>+11.4f}% "
            f"{row['tail_multiplier']:>10.8f} {row['tail_delta_mev']:>+12.6f} "
            f"{row['final_mev']:>12.6f} {row['final_error_pct']:>+10.4f}%"
        )


def print_single(row):
    print("=" * 96)
    print(f"  {row['name']}")
    print("=" * 96)
    print(f"  Category           : {row['category']}")
    print(f"  Canonical source   : {row['source']}")
    print(f"  Bare formula       : {row['bare_formula']}")
    print(f"  PDG value          : {row['pdg_mev']:.9f} MeV")
    print(f"  Bare value         : {row['bare_mev']:.9f} MeV   ({row['bare_error_pct']:+.6f}%)")
    print(f"  Shifted value      : {row['shifted_mev']:.9f} MeV   ({row['shifted_error_pct']:+.6f}%)")
    print(f"  Tail multiplier    : {row['tail_multiplier']:.12f}")
    print(f"  Tail delta         : {row['tail_delta_mev']:+.9f} MeV")
    print(f"  Final value        : {row['final_mev']:.9f} MeV   ({row['final_error_pct']:+.6f}%)")
    print(f"  Has residual tail  : {'yes' if row['has_tail'] else 'no'}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="Inspect a single particle by exact display name")
    args = parser.parse_args()

    rows = all_breakdowns()
    if args.name:
        for row in rows:
            if row["name"] == args.name:
                print_single(row)
                return
        raise SystemExit(f"Particle not found: {args.name}")

    print_catalog(rows)


if __name__ == "__main__":
    main()
