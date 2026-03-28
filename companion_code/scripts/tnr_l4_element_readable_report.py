#!/usr/bin/env python3
"""
Readable L4 element report
==========================

Human-facing and AI-facing report for the chemical layer.

Two modes:
  1. Catalog mode (default): all 118 elements in a compact readable table.
  2. Inspect mode (--z): one selected element with expanded context.

The report shows not only IE accuracy, but also the family-level screening
context: subshell closure, nearest screening target, and whether the family
looks like a representative lock or a drifting continuation.

Theory note:
  the chemical layer should stay readable as a staged construction:
    canonical registry -> bare shell state -> screening context -> residual drift.
  This prevents a good result from looking like opaque coefficient fitting.
"""

from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path
import sys


SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from tnr_l4_screening_family_audit import extract_family  # noqa: E402


GENERATOR_PATH = Path(
    "/Users/abc/Codex_n111/tnr_final_synthesis/publishing/chemistry/periodic_table_generator.py"
)


def load_generator():
    spec = importlib.util.spec_from_file_location("periodic_table_generator", GENERATOR_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def family_status(audit):
    if audit.subshell in {"1s", "3d", "4f", "5f"}:
        return "representative lock"
    return "period-depth drift"


def element_row(module, z: int):
    ss = module.get_shell_state(z)
    n_val, d_val = module.TOPO_MAP[z]
    ie_dot = (n_val / d_val) * module.E_BOND
    ie_exp = module.IE_EXP[z]
    err_pct = abs(ie_dot - ie_exp) / ie_exp * 100.0
    audit, _points = extract_family(module, ss.subshell)
    return {
        "z": z,
        "symbol": module.ELEMENTS[z],
        "subshell": ss.subshell,
        "period": ss.period,
        "block": ss.block,
        "pos": ss.pos,
        "cap": ss.cap,
        "N": n_val,
        "D": d_val,
        "N_fact": module.factorize(n_val),
        "D_fact": module.factorize(d_val),
        "node_name": module.NODE_NAMES.get(n_val, "unlabeled"),
        "ie_dot": ie_dot,
        "ie_exp": ie_exp,
        "err_pct": err_pct,
        "family_closure": audit.closure,
        "family_target": audit.nearest_target_label,
        "family_target_diff": audit.nearest_target_diff,
        "family_status": family_status(audit),
        "anchor_symbol": audit.anchor_symbol,
        "anchor_z": audit.anchor_z,
        "closure_symbol": audit.closure_symbol,
        "closure_z": audit.closure_z,
    }


def print_catalog(rows):
    print("=" * 176)
    print("  TNR L4 ELEMENT READABLE REPORT")
    print("  Columns: registry fraction, node meaning, IE prediction, and family-level screening context")
    print("=" * 176)
    print(
        f"  {'Z':<4} {'El':<3} {'Sub':<4} {'Pos':<6} {'N/D':<8} {'Node':<22} "
        f"{'IE_DOT':>10} {'IE_exp':>10} {'Err%':>8} {'Fam closure':>12} {'Nearest':>20} {'Status':>22}"
    )
    print("  " + "-" * 170)
    for row in rows:
        print(
            f"  {row['z']:<4} {row['symbol']:<3} {row['subshell']:<4} {str(row['pos']) + '/' + str(row['cap']):<6} "
            f"{str(row['N']) + '/' + str(row['D']):<8} {row['node_name']:<22} "
            f"{row['ie_dot']:>10.4f} {row['ie_exp']:>10.4f} {row['err_pct']:>7.3f}% "
            f"{row['family_closure']:>12.6f} {row['family_target']:>20} {row['family_status']:>22}"
        )


def print_single(row):
    print("=" * 104)
    print(f"  {row['symbol']}  (Z={row['z']})")
    print("=" * 104)
    print(f"  Subshell            : {row['subshell']}   pos={row['pos']}/{row['cap']}   block={row['block']}   period={row['period']}")
    print(f"  Registry fraction   : {row['N']}/{row['D']} = ({row['N_fact']}) / ({row['D_fact']})")
    print(f"  Numerator node      : {row['node_name']}")
    print(f"  IE_DOT              : {row['ie_dot']:.6f} eV")
    print(f"  IE_exp              : {row['ie_exp']:.6f} eV")
    print(f"  Abs error           : {row['err_pct']:.6f}%")
    print(f"  Family anchor       : {row['anchor_symbol']} (Z={row['anchor_z']})")
    print(f"  Family closure      : {row['closure_symbol']} (Z={row['closure_z']})")
    print(f"  Family ΔS_closure   : {row['family_closure']:.6f}")
    print(f"  Nearest target      : {row['family_target']}   (diff {row['family_target_diff']:.6f})")
    print(f"  Family status       : {row['family_status']}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--z", type=int, help="Inspect a single element by atomic number")
    args = parser.parse_args()

    module = load_generator()
    if args.z is not None:
        if args.z < 1 or args.z > 118:
            raise SystemExit("--z must be in 1..118")
        print_single(element_row(module, args.z))
        return

    rows = [element_row(module, z) for z in range(1, 119)]
    print_catalog(rows)


if __name__ == "__main__":
    main()
