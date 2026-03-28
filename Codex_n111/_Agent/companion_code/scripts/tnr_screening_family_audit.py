#!/usr/bin/env python3
"""
TNR screening family audit
==========================

Generalized audit over all subshell families with at least two elements.

This script does not assume a universal closed-form law for every family.
Instead it provides a reproducible map of:

  - extracted same-shell trajectories for every subshell;
  - closure values at full-fill;
  - block-wise series across periods;
  - nearest match to the small DOT screening vocabulary:
      2/3, 1-γ²/2 = 26/27, 1-γ²/3 = 80/81.

The goal is diagnostic: separate truly locked representative families
from later period-depth drift.

Interpretation note:
  this script is the safeguard against overclaiming.
  If a family drifts, the code shows the drift explicitly instead of
  forcing it back into a prettier but false one-coefficient law.
"""

from __future__ import annotations

import importlib.util
import math
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


GENERATOR_PATH = Path(
    "/Users/abc/Codex_n111/tnr_final_synthesis/publishing/chemistry/periodic_table_generator.py"
)


@dataclass
class FamilyPoint:
    z: int
    symbol: str
    subshell: str
    block: str
    n: int
    pos: int
    cap: int
    delta_s_same: float


@dataclass
class FamilyAudit:
    subshell: str
    block: str
    period: int
    anchor_z: int
    anchor_symbol: str
    closure_z: int
    closure_symbol: str
    s_inner: float
    closure: float
    mean: float
    min_value: float
    max_value: float
    nearest_target_label: str
    nearest_target_value: float
    nearest_target_diff: float


def load_generator():
    spec = importlib.util.spec_from_file_location("periodic_table_generator", GENERATOR_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def z_eff_from_ie(ry: float, ie_exp: float, n: int) -> float:
    return n * math.sqrt(ie_exp / ry)


def collect_families(module) -> dict[str, list[tuple]]:
    families = defaultdict(list)
    for z in range(1, 119):
        shell = module.get_shell_state(z)
        ie = module.IE_EXP[z]
        zeff = z_eff_from_ie(module.Ry, ie, shell.n)
        families[shell.subshell].append((z, module.ELEMENTS[z], shell, zeff))
    return families


def extract_family(module, subshell_name: str) -> tuple[FamilyAudit, list[FamilyPoint]]:
    family = collect_families(module)[subshell_name]
    if len(family) < 2:
        raise ValueError(f"Subshell {subshell_name} does not have enough points")

    z0, symbol0, shell0, zeff0 = family[0]
    s_inner = z0 - zeff0

    points: list[FamilyPoint] = []
    for z, symbol, shell, zeff in family[1:]:
        delta_s_same = (z - s_inner - zeff) / (shell.pos - 1)
        points.append(
            FamilyPoint(
                z=z,
                symbol=symbol,
                subshell=subshell_name,
                block=shell.block,
                n=shell.n,
                pos=shell.pos,
                cap=shell.cap,
                delta_s_same=delta_s_same,
            )
        )

    gamma2 = 2.0 / 27.0
    target_vocab = {
        "2/3": 2.0 / 3.0,
        "26/27 = 1-γ²/2": 1.0 - gamma2 / 2.0,
        "80/81 = 1-γ²/3": 1.0 - gamma2 / 3.0,
    }
    closure = points[-1].delta_s_same
    nearest_label, nearest_value = min(
        target_vocab.items(), key=lambda item: abs(closure - item[1])
    )
    nearest_diff = abs(closure - nearest_value)

    audit = FamilyAudit(
        subshell=subshell_name,
        block=shell0.block,
        period=shell0.n,
        anchor_z=z0,
        anchor_symbol=symbol0,
        closure_z=points[-1].z,
        closure_symbol=points[-1].symbol,
        s_inner=s_inner,
        closure=closure,
        mean=sum(p.delta_s_same for p in points) / len(points),
        min_value=min(p.delta_s_same for p in points),
        max_value=max(p.delta_s_same for p in points),
        nearest_target_label=nearest_label,
        nearest_target_value=nearest_value,
        nearest_target_diff=nearest_diff,
    )
    return audit, points


def main() -> None:
    module = load_generator()
    families = collect_families(module)
    order = ["1s", "2s", "2p", "3s", "3p", "3d", "4s", "4p", "4d", "4f",
             "5s", "5p", "5d", "5f", "6s", "6p", "6d", "7s", "7p"]

    audits: list[FamilyAudit] = []
    trajectories: dict[str, list[FamilyPoint]] = {}

    for subshell_name in order:
        if subshell_name not in families or len(families[subshell_name]) < 2:
            continue
        audit, points = extract_family(module, subshell_name)
        audits.append(audit)
        trajectories[subshell_name] = points

    print("=" * 118)
    print("  TNR SCREENING FAMILY AUDIT")
    print(f"  Dataset: {GENERATOR_PATH}")
    print("  Targets audited against small DOT vocabulary: 2/3, 26/27, 80/81")
    print("=" * 118)

    print("\n  FAMILY CLOSURE MAP")
    print(
        f"  {'Sub':<4} {'Blk':<3} {'Anchor':<12} {'Closure':<12} {'ΔS_closure':>12} "
        f"{'mean':>10} {'min':>10} {'max':>10} {'nearest target':>22} {'diff':>10}"
    )
    print("  " + "-" * 112)
    for audit in audits:
        print(
            f"  {audit.subshell:<4} {audit.block:<3} "
            f"{audit.anchor_symbol + ' (Z=' + str(audit.anchor_z) + ')':<12} "
            f"{audit.closure_symbol + ' (Z=' + str(audit.closure_z) + ')':<12} "
            f"{audit.closure:>12.6f} {audit.mean:>10.6f} {audit.min_value:>10.6f} "
            f"{audit.max_value:>10.6f} {audit.nearest_target_label:>22} {audit.nearest_target_diff:>10.6f}"
        )

    print("\n  BLOCK-WISE CLOSURE SERIES")
    by_block = defaultdict(list)
    for audit in audits:
        by_block[audit.block].append(audit)

    for block in ["s", "p", "d", "f"]:
        series = sorted(by_block[block], key=lambda a: (a.period, a.subshell))
        print(f"\n  Block {block}:")
        for audit in series:
            print(
                f"    {audit.subshell:<3}  period={audit.period}  "
                f"closure={audit.closure:.6f}  nearest={audit.nearest_target_label}  "
                f"diff={audit.nearest_target_diff:.6f}"
            )

    print("\n  REPRESENTATIVE LOCKED FAMILIES")
    for subshell_name in ["1s", "3d", "4f", "5f"]:
        audit = next(a for a in audits if a.subshell == subshell_name)
        print(
            f"    {subshell_name:<3} -> closure={audit.closure:.6f}  "
            f"nearest={audit.nearest_target_label}  diff={audit.nearest_target_diff:.6f}"
        )

    print("\n  DETAIL TRAJECTORIES")
    for subshell_name in ["3d", "4f", "5f", "2p", "3p", "4p", "5p", "6p", "7p"]:
        if subshell_name not in trajectories:
            continue
        print(f"\n  {subshell_name}:")
        for point in trajectories[subshell_name]:
            print(
                f"    {point.symbol:>2}  pos={point.pos:>2}/{point.cap:<2}  "
                f"ΔS_same={point.delta_s_same:.6f}"
            )


if __name__ == "__main__":
    main()
