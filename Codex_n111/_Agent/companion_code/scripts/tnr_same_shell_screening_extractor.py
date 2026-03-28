#!/usr/bin/env python3
"""
TNR same-shell screening extractor
=================================

Standalone reverse-extraction of representative same-shell screening values
from the same IE dataset used by the chemical registry.

Method
------
For each subshell family:

1. Take the first element of the family (`pos = 1`) as the anchor.
2. Recover its inner-core screening:

       S_inner = Z - n * sqrt(IE / Ry)

3. For every later position inside the same subshell, recover:

       ΔS_same = (Z - S_inner - n * sqrt(IE / Ry)) / (pos - 1)

The full-fill value (`pos = cap`) is the representative screening constant
for the completed subshell family.

This reproduces the canonical targets used in the chemical screening table:

  1s  -> ~ 2/3
  3d  -> ~ 26/27
  4f  -> ~ 80/81
  5f  -> ~ 26/27

Interpretation note:
  this script is intentionally narrow. It proves that the representative
  closure families can be reverse-extracted from the same IE dataset.
  It does not claim that every block is exhausted by one universal constant.
"""

from __future__ import annotations

import importlib.util
import math
from dataclasses import dataclass
from pathlib import Path


GENERATOR_PATH = Path(
    "/Users/abc/Codex_n111/tnr_final_synthesis/publishing/chemistry/periodic_table_generator.py"
)


@dataclass
class ScreeningPoint:
    z: int
    symbol: str
    subshell: str
    pos: int
    cap: int
    delta_s_same: float


def load_generator():
    spec = importlib.util.spec_from_file_location("periodic_table_generator", GENERATOR_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def z_eff_from_ie(ry: float, ie_exp: float, n: int) -> float:
    return n * math.sqrt(ie_exp / ry)


def extract_subshell_points(module, subshell_name: str) -> tuple[float, list[ScreeningPoint]]:
    family = []
    for z in range(1, 119):
        shell = module.get_shell_state(z)
        if shell.subshell != subshell_name:
            continue
        family.append((z, shell, module.IE_EXP[z], module.ELEMENTS[z]))

    if len(family) < 2:
        raise ValueError(f"Subshell {subshell_name} does not have enough points for extraction")

    z0, shell0, ie0, _symbol0 = family[0]
    s_inner = z0 - z_eff_from_ie(module.Ry, ie0, shell0.n)

    points = []
    for z, shell, ie, symbol in family[1:]:
        zeff = z_eff_from_ie(module.Ry, ie, shell.n)
        delta_s_same = (z - s_inner - zeff) / (shell.pos - 1)
        points.append(
            ScreeningPoint(
                z=z,
                symbol=symbol,
                subshell=subshell_name,
                pos=shell.pos,
                cap=shell.cap,
                delta_s_same=delta_s_same,
            )
        )

    return s_inner, points


def main() -> None:
    module = load_generator()

    representative_targets = {
        "1s": ("2/3", 2.0 / 3.0, "primordial s-limit"),
        "3d": ("26/27", 26.0 / 27.0, "d-metal full-fill"),
        "4f": ("80/81", 80.0 / 81.0, "lanthanoid full-fill"),
        "5f": ("26/27", 26.0 / 27.0, "actinoid full-fill"),
    }

    print("=" * 98)
    print("  TNR SAME-SHELL SCREENING EXTRACTOR")
    print(f"  Dataset: {GENERATOR_PATH}")
    print(f"  Ry = {module.Ry:.5f} eV")
    print("=" * 98)

    print("\n  FULL-FILL REPRESENTATIVE EXTRACTION")
    print(
        f"  {'Sub':<4} {'Anchor':<12} {'Closure':<12} {'ΔS_same(exp)':>14} "
        f"{'DOT target':>12} {'abs diff':>10}  Status"
    )
    print("  " + "-" * 84)

    for subshell_name, (target_label, target_value, status) in representative_targets.items():
        family = []
        for z in range(1, 119):
            shell = module.get_shell_state(z)
            if shell.subshell != subshell_name:
                continue
            family.append((z, shell, module.IE_EXP[z], module.ELEMENTS[z]))

        z0, _shell0, _ie0, symbol0 = family[0]
        _s_inner, points = extract_subshell_points(module, subshell_name)
        closure = points[-1]
        diff = abs(closure.delta_s_same - target_value)
        print(
            f"  {subshell_name:<4} {symbol0 + ' (Z=' + str(z0) + ')':<12} "
            f"{closure.symbol + ' (Z=' + str(closure.z) + ')':<12} "
            f"{closure.delta_s_same:>14.6f} {target_label:>12} {diff:>10.6f}  {status}"
        )

    print("\n  SUBSHELL FAMILY TRAJECTORIES")
    print(f"  {'Sub':<4} {'Anchor':<12} {'S_inner':>12} {'min ΔS':>12} {'max ΔS':>12} {'closure':>12}")
    print("  " + "-" * 72)

    for subshell_name in ["1s", "2s", "3s", "4s", "5s", "6s", "7s", "3d", "4f", "5f"]:
        family = []
        for z in range(1, 119):
            shell = module.get_shell_state(z)
            if shell.subshell != subshell_name:
                continue
            family.append((z, shell, module.IE_EXP[z], module.ELEMENTS[z]))

        if len(family) < 2:
            continue

        z0, shell0, ie0, symbol0 = family[0]
        s_inner, points = extract_subshell_points(module, subshell_name)
        min_delta = min(p.delta_s_same for p in points)
        max_delta = max(p.delta_s_same for p in points)
        closure = points[-1].delta_s_same
        print(
            f"  {subshell_name:<4} {symbol0 + ' (Z=' + str(z0) + ')':<12} "
            f"{s_inner:>12.6f} {min_delta:>12.6f} {max_delta:>12.6f} {closure:>12.6f}"
        )

    print("\n  DETAIL: 3d / 4f / 5f / 1s")
    for subshell_name in ["1s", "3d", "4f", "5f"]:
        family = []
        for z in range(1, 119):
            shell = module.get_shell_state(z)
            if shell.subshell != subshell_name:
                continue
            family.append((z, shell, module.IE_EXP[z], module.ELEMENTS[z]))
        z0, shell0, ie0, symbol0 = family[0]
        s_inner, points = extract_subshell_points(module, subshell_name)
        print(f"\n  {subshell_name}: anchor = {symbol0} (Z={z0}), S_inner = {s_inner:.6f}")
        for point in points:
            print(
                f"    {point.symbol:>2}  pos={point.pos:>2}/{point.cap:<2}  "
                f"ΔS_same={point.delta_s_same:.6f}"
            )


if __name__ == "__main__":
    main()
