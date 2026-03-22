#!/usr/bin/env python3
"""
DOT Companion Verification Dashboard
=====================================

Single entrypoint for the Distinction Observable Theory (DOT)
companion code layer:
- particle/macro verification dashboard (legacy snapshot),
- full tail calculator (legacy snapshot),
- 64-state vacuum engine (legacy snapshot),
- exploratory chemistry (current v10).

This wrapper intentionally does not rewrite the underlying logic.
It simply orchestrates the scripts and provides a stable CLI.

Note: The legacy scripts mix exact identities, baseline predictions, and
candidate layers. Treat their output as a reproducibility dashboard,
not a single closed proof.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
LEGACY = ROOT / "companion_legacy"

SCRIPT_FULL = LEGACY / "dot_full_verification.py"
SCRIPT_TAILS = LEGACY / "dot_all_particles_tail_calculator.py"
SCRIPT_64 = LEGACY / "dot_64state_engine.py"
SCRIPT_CHEM_V10 = ROOT / "dot_hydrogen_dynamic_v10.py"
SCRIPT_HYDROGEN_DYN = LEGACY / "dot_hydrogen_dynamic_v5_1.py"


def _run(script: Path) -> int:
    if not script.exists():
        print(f"[dot_companion_verify] missing script: {script}", file=sys.stderr)
        return 2
    env = dict(os.environ)
    # Ensure stable UTF-8 output in terminals/logs.
    env.setdefault("PYTHONUTF8", "1")
    p = subprocess.run([sys.executable, str(script)], env=env)
    return int(p.returncode)


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(
        prog="dot_companion_verify.py",
        description="DOT companion verification dashboard (runs selected scripts).",
    )
    ap.add_argument(
        "--full",
        action="store_true",
        help="Run the legacy unified verification dashboard.",
    )
    ap.add_argument(
        "--tails",
        action="store_true",
        help="Run the legacy all-particles tail calculator.",
    )
    ap.add_argument(
        "--vacuum64",
        action="store_true",
        help="Run the legacy 64-state engine for K(2,2,2).",
    )
    ap.add_argument(
        "--chem",
        action="store_true",
        help="Run the current exploratory chemistry model (v10).",
    )
    ap.add_argument(
        "--hydrogen-dyn",
        action="store_true",
        help="Run the legacy hydrogen dynamics model (state evolution / excitation).",
    )
    ap.add_argument(
        "--all",
        action="store_true",
        help="Run --full --tails --vacuum64 --chem --hydrogen-dyn in order.",
    )

    args = ap.parse_args(argv)
    if not (args.full or args.tails or args.vacuum64 or args.chem or args.hydrogen_dyn or args.all):
        ap.print_help(sys.stdout)
        return 0

    steps: list[tuple[str, Path]] = []
    if args.all or args.full:
        steps.append(("legacy: full verification", SCRIPT_FULL))
    if args.all or args.tails:
        steps.append(("legacy: tail calculator", SCRIPT_TAILS))
    if args.all or args.vacuum64:
        steps.append(("legacy: 64-state engine", SCRIPT_64))
    if args.all or args.chem:
        steps.append(("current: chemistry v10", SCRIPT_CHEM_V10))
    if args.all or args.hydrogen_dyn:
        steps.append(("legacy: hydrogen dynamics v5.1", SCRIPT_HYDROGEN_DYN))

    for label, script in steps:
        print("\n" + "=" * 88)
        print(f"[dot_companion_verify] RUN {label}")
        print(f"[dot_companion_verify] {script}")
        print("=" * 88)
        rc = _run(script)
        if rc != 0:
            print(f"[dot_companion_verify] step failed: {label} (rc={rc})", file=sys.stderr)
            return rc

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
