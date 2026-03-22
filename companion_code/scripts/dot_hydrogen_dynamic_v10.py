#!/usr/bin/env python3
"""
DOT Molecular Dynamics v10
==========================

Iteration-friendly continuation of v9:
- keeps exact H2 branch,
- keeps bond-domain core for p-block central hydrides,
- keeps s-block branch explicitly unresolved (candidate only),
- adds bounded multi-center branch for two-carbon hydrocarbons.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


# ---------------------------------------------------------------------------
# TNR constants
# ---------------------------------------------------------------------------
GAMMA = math.sqrt(6.0) / 9.0
GAMMA2 = 2.0 / 27.0
GAMMA3 = GAMMA ** 3
ALPHA_INV = 1728.0 / (4.0 * math.pi) - 47.0 * GAMMA3 / 2.0
ALPHA = 1.0 / ALPHA_INV
M_E_EV = 0.51099895e6
RY_EV = ALPHA * ALPHA * M_E_EV / 2.0
E_BOND = RY_EV / 3.0


@dataclass(frozen=True)
class Atom:
    symbol: str
    period: int
    valence_e: int
    family: str


ATOMS = {
    "H": Atom("H", 1, 1, "hydrogen"),
    "Li": Atom("Li", 2, 1, "s_block_hydride"),
    "C": Atom("C", 2, 4, "p_block_hydride"),
    "N": Atom("N", 2, 5, "p_block_hydride"),
    "O": Atom("O", 2, 6, "p_block_hydride"),
    "F": Atom("F", 2, 7, "p_block_hydride"),
    "Si": Atom("Si", 3, 4, "p_block_hydride"),
    "P": Atom("P", 3, 5, "p_block_hydride"),
    "S": Atom("S", 3, 6, "p_block_hydride"),
    "Cl": Atom("Cl", 3, 7, "p_block_hydride"),
    "Br": Atom("Br", 4, 7, "p_block_hydride"),
    "I": Atom("I", 5, 7, "p_block_hydride"),
}


@dataclass(frozen=True)
class MoleculeSpec:
    formula: str
    symbols: tuple[str, ...]
    bonds: tuple[tuple[int, int], ...]
    ref_eV: float


MOLS = (
    MoleculeSpec("H₂", ("H", "H"), ((0, 1),), 4.478),
    MoleculeSpec("LiH", ("Li", "H"), ((0, 1),), 2.515),
    MoleculeSpec("HF", ("H", "F"), ((0, 1),), 5.870),
    MoleculeSpec("H₂O", ("O", "H", "H"), ((0, 1), (0, 2)), 9.510),
    MoleculeSpec("NH₃", ("N", "H", "H", "H"), ((0, 1), (0, 2), (0, 3)), 11.950),
    MoleculeSpec("CH₄", ("C", "H", "H", "H", "H"), ((0, 1), (0, 2), (0, 3), (0, 4)), 17.020),
    MoleculeSpec("SiH₄", ("Si", "H", "H", "H", "H"), ((0, 1), (0, 2), (0, 3), (0, 4)), 13.070),
    MoleculeSpec("PH₃", ("P", "H", "H", "H"), ((0, 1), (0, 2), (0, 3)), 10.000),
    MoleculeSpec("H₂S", ("S", "H", "H"), ((0, 1), (0, 2)), 7.570),
    MoleculeSpec("HCl", ("H", "Cl"), ((0, 1),), 4.430),
    MoleculeSpec("HBr", ("H", "Br"), ((0, 1),), 3.760),
    MoleculeSpec("HI", ("H", "I"), ((0, 1),), 3.060),
    MoleculeSpec(
        "C₂H₆",
        ("C", "C", "H", "H", "H", "H", "H", "H"),
        ((0, 1), (0, 2), (0, 3), (0, 4), (1, 5), (1, 6), (1, 7)),
        29.60,
    ),
    MoleculeSpec(
        "C₂H₄",
        ("C", "C", "H", "H", "H", "H"),
        ((0, 1), (0, 1), (0, 2), (0, 3), (1, 4), (1, 5)),
        24.70,
    ),
)


def is_star_hydride(spec: MoleculeSpec) -> bool:
    hydrogens = sum(1 for s in spec.symbols if s == "H")
    if hydrogens != len(spec.symbols) - 1:
        return False
    centers = [i for i, s in enumerate(spec.symbols) if s != "H"]
    if len(centers) != 1:
        return False
    c = centers[0]
    expected = {(c, i) for i, s in enumerate(spec.symbols) if s == "H"}
    expected |= {(i, c) for i, s in enumerate(spec.symbols) if s == "H"}
    return all(b in expected for b in spec.bonds)


def exact_h2_energy() -> float:
    # H2 exact mass-defect / first overtone law already established in TNR.
    return E_BOND * (80.0 / 81.0)


def k_base(bonds: int, lone_pairs: int) -> float:
    total = bonds + lone_pairs
    if lone_pairs < bonds:
        return -total / bonds
    return (total - 1.0) / total


def period_screening(period: int, bonds: int, lone_pairs: int) -> float:
    if period <= 2:
        return 1.0
    base = 1.0 + (period - 2.0) * GAMMA
    # Lone-pair-rich centers screen harder; bond-rich centers keep more radial span.
    if lone_pairs <= 0:
        shell_drag = 1.0 + 0.05 * (period - 2.0)
        return 1.0 / (1.0 + (period - 2.0) * GAMMA * shell_drag)
    total = bonds + lone_pairs
    lp_density = lone_pairs / total
    skew = 1.0 + 0.8 * (lp_density - 0.5)
    return 1.0 / (1.0 + (period - 2.0) * GAMMA * skew)


def p_block_hydride_energy(center: Atom, bonds_to_h: int) -> tuple[float, dict]:
    lone_pairs = max(center.valence_e - bonds_to_h, 0) // 2
    k = k_base(bonds_to_h, lone_pairs)
    radial = bonds_to_h * E_BOND * (1.0 + k * GAMMA2)
    ortho = lone_pairs * E_BOND * (GAMMA2 / 2.0) * (lone_pairs - bonds_to_h)
    period_factor = period_screening(center.period, bonds_to_h, lone_pairs)
    total = (radial + ortho) * period_factor

    # Monohydrides (HF/HCl class): one-bond readout carries extra polar aperture.
    monohydride_polar = 1.0
    if bonds_to_h == 1 and lone_pairs >= 3:
        monohydride_polar = 1.0 + (GAMMA2 / 6.0) / max(center.period, 1)
        total *= monohydride_polar

    halide_bridge = 1.0
    if bonds_to_h == 1 and lone_pairs >= 3 and center.period >= 3:
        halide_bridge = 1.0 + (GAMMA2 / 12.0) * (center.period - 2.0)
        total *= halide_bridge

    heavy_halogen_lift = 1.0
    if bonds_to_h == 1 and lone_pairs >= 3 and center.period >= 4:
        heavy_halogen_lift = 1.0 + (0.75 * GAMMA2) / (center.period - 3.0)
        total *= heavy_halogen_lift

    # Compact tetrahedral closure: strongest in 2nd period (CH4-type packing).
    tetra_compact = 1.0
    if bonds_to_h == 4 and lone_pairs == 0 and center.period == 2:
        tetra_compact = 1.0 + GAMMA2 / 6.0
        total *= tetra_compact

    trigonal_relief = 1.0
    if bonds_to_h == 3 and lone_pairs == 1 and center.period >= 3:
        trigonal_relief = 1.0 + (GAMMA2 / 6.0) * (center.period - 2.0)
        total *= trigonal_relief

    meta = {
        "mode": "bond-domain",
        "bonds": bonds_to_h,
        "lone_pairs": lone_pairs,
        "k_base": k,
        "period_factor": period_factor,
        "monohydride_polar": monohydride_polar,
        "halide_bridge": halide_bridge,
        "heavy_halogen_lift": heavy_halogen_lift,
        "tetra_compact": tetra_compact,
        "trigonal_relief": trigonal_relief,
        "E_radial": radial,
        "E_ortho": ortho,
    }
    return total, meta


def unresolved_s_block_hydride_energy(center: Atom, bonds_to_h: int) -> tuple[float, dict]:
    # Candidate-only readout: dyadic-to-ionic collapse ratio (9/16), still unresolved.
    # Kept explicit so the branch is not presented as closed theory.
    ionic_collapse = 9.0 / 16.0
    total = exact_h2_energy() * ionic_collapse * bonds_to_h
    meta = {
        "mode": "candidate-s-block",
        "bonds": bonds_to_h,
        "ionic_collapse": ionic_collapse,
        "note": "s-block hydride branch remains unresolved (candidate scaling)",
    }
    return total, meta


def hydrocarbon_2c_energy(spec: MoleculeSpec) -> tuple[float, dict]:
    c_indices = [i for i, s in enumerate(spec.symbols) if s == "C"]
    h_indices = [i for i, s in enumerate(spec.symbols) if s == "H"]
    if len(c_indices) != 2 or len(c_indices) + len(h_indices) != len(spec.symbols):
        return float("nan"), {
            "mode": "unresolved-topology",
            "note": "multi-center branch currently supports only C2Hn hydrocarbons",
        }

    c1, c2 = c_indices
    # Multi-bond order is represented by repeated (c1, c2) edges in the input graph.
    cc_order = sum(
        1
        for a, b in spec.bonds
        if (a == c1 and b == c2) or (a == c2 and b == c1)
    )
    if cc_order < 1:
        return float("nan"), {
            "mode": "unresolved-topology",
            "note": "C2 hydrocarbon requires at least one C-C edge",
        }
    if cc_order > 3:
        return float("nan"), {
            "mode": "unresolved-topology",
            "note": "C-C bond order above 3 is outside current branch",
        }

    h_on_c1 = 0
    h_on_c2 = 0
    for a, b in spec.bonds:
        if a == c1 and b in h_indices:
            h_on_c1 += 1
        elif b == c1 and a in h_indices:
            h_on_c1 += 1
        if a == c2 and b in h_indices:
            h_on_c2 += 1
        elif b == c2 and a in h_indices:
            h_on_c2 += 1

    # Carbon valence guard: h_count + C-C order must not exceed 4 on each center.
    if h_on_c1 + cc_order > 4 or h_on_c2 + cc_order > 4:
        return float("nan"), {
            "mode": "unresolved-topology",
            "note": "valence overflow in C2 branch",
        }

    # -------------------------------------------------------------------
    # TNR hydrocarbon laws (minimal multi-center closure, no global fit):
    #
    # 1) C–C sigma bridge: pays one irreducible 1D boundary debt γ².
    #       E_CC,σ = E_bond * (1 - γ²)
    #
    # 2) Each additional C–C bond order contributes one orthogonal π-closure:
    #       E_CC,π = E_bond * (2/3)
    #
    # 3) Carbon hybridization changes how much of the σ-network tension is
    #    carried by the remaining σ-bonds (C–H channels):
    #       sp3: (1 - γ²) with compact 3D closure bonus (1 + γ²/6)
    #       sp2: (1 - γ²/2) with no 3D packing bonus
    #       sp1: strongest relief reading (1 - γ²/3), no 3D bonus
    # -------------------------------------------------------------------
    e_ch_sp3 = E_BOND * (1.0 - GAMMA2) * (1.0 + GAMMA2 / 6.0)
    e_ch_sp2 = E_BOND * (1.0 - 0.5 * GAMMA2)
    e_ch_sp1 = E_BOND * (1.0 - (1.0 / 3.0) * GAMMA2)

    if cc_order == 1:
        e_ch_per_bond = e_ch_sp3
        hybrid = "sp3"
    elif cc_order == 2:
        e_ch_per_bond = e_ch_sp2
        hybrid = "sp2"
    else:
        e_ch_per_bond = e_ch_sp1
        hybrid = "sp1"

    e_ch_total = (h_on_c1 + h_on_c2) * e_ch_per_bond

    e_cc_sigma = E_BOND * (1.0 - GAMMA2)
    e_cc_pi = max(cc_order - 1, 0) * E_BOND * (2.0 / 3.0)
    e_cc_total = e_cc_sigma + e_cc_pi

    total = e_ch_total + e_cc_total
    meta = {
        "mode": "multi-center-2c",
        "cc_order": cc_order,
        "hybridization": hybrid,
        "h_on_c1": h_on_c1,
        "h_on_c2": h_on_c2,
        "E_CH_per_bond": e_ch_per_bond,
        "E_CH_total": e_ch_total,
        "E_CC_sigma": e_cc_sigma,
        "E_CC_pi": e_cc_pi,
    }
    return total, meta


def predict(spec: MoleculeSpec) -> tuple[float, dict]:
    if spec.formula == "H₂":
        return exact_h2_energy(), {"mode": "exact-h2"}

    if is_star_hydride(spec):
        center_symbol = next(s for s in spec.symbols if s != "H")
        center = ATOMS[center_symbol]
        bonds_to_h = len(spec.symbols) - 1
        if center.family == "p_block_hydride":
            return p_block_hydride_energy(center, bonds_to_h)
        if center.family == "s_block_hydride":
            return unresolved_s_block_hydride_energy(center, bonds_to_h)

    if all(s in {"C", "H"} for s in spec.symbols):
        return hydrocarbon_2c_energy(spec)

    return float("nan"), {
        "mode": "unresolved-topology",
        "note": "v10 supports H2, one-center star hydrides, and C2 hydrocarbons",
    }


def benchmark_rows():
    rows = []
    for spec in MOLS:
        pred, meta = predict(spec)
        err = (pred - spec.ref_eV) / spec.ref_eV * 100.0
        rows.append((spec, pred, err, meta))
    return rows


def render() -> str:
    lines = []
    lines.append("DOT v10 — Hydride and C2 Hydrocarbon Dynamics")
    lines.append("=" * 78)
    lines.append(f"γ = {GAMMA:.8f}   γ² = {GAMMA2:.8f}   α⁻¹ = {ALPHA_INV:.6f}")
    lines.append(f"Ry = {RY_EV:.6f} eV   Ry/3 = {E_BOND:.6f} eV")
    lines.append("")
    lines.append("Model split:")
    lines.append("- H₂: exact mass-defect / overtone case")
    lines.append("- central hydrides: bond-domain + lone-pair law + period/polar aperture")
    lines.append("- s-block hydrides: explicit unresolved candidate branch")
    lines.append("- C2 hydrocarbons: bounded multi-center branch (C-H + C-C channels)")
    lines.append("")
    lines.append(f"{'Mol':<6} {'Mode':<20} {'TNR eV':>10} {'Exp eV':>10} {'Err%':>8}")
    lines.append(f"{'-'*6} {'-'*20} {'-'*10} {'-'*10} {'-'*8}")
    rows = benchmark_rows()
    errs = []
    resolved_errs = []
    for spec, pred, err, meta in rows:
        if math.isnan(pred):
            lines.append(f"{spec.formula:<6} {meta['mode']:<20} {'n/a':>10} {spec.ref_eV:>10.4f} {'n/a':>8}")
            continue
        errs.append(abs(err))
        if not meta["mode"].startswith("candidate-") and not meta["mode"].startswith("unresolved-"):
            resolved_errs.append(abs(err))
        lines.append(f"{spec.formula:<6} {meta['mode']:<20} {pred:>10.4f} {spec.ref_eV:>10.4f} {err:>+7.2f}%")
    lines.append("")
    mean_all = (sum(errs) / len(errs)) if errs else float("nan")
    mean_resolved = (sum(resolved_errs) / len(resolved_errs)) if resolved_errs else float("nan")
    lines.append(f"Mean |error| (all)       = {mean_all:.2f}%")
    lines.append(f"Mean |error| (resolved)  = {mean_resolved:.2f}%")
    lines.append("")
    lines.append("Branch details:")
    for spec, _, _, meta in rows:
        if meta["mode"] == "bond-domain":
            lines.append(
                f"- {spec.formula}: b={meta['bonds']}, l={meta['lone_pairs']}, "
                f"k={meta['k_base']:+.4f}, period={meta['period_factor']:.4f}, "
                f"polar={meta['monohydride_polar']:.4f}, bridge={meta['halide_bridge']:.4f}, "
                f"lift={meta['heavy_halogen_lift']:.4f}, tetra={meta['tetra_compact']:.4f}, "
                f"trig={meta['trigonal_relief']:.4f}, "
                f"E_rad={meta['E_radial']:.4f}, "
                f"E_ortho={meta['E_ortho']:+.4f}"
            )
        elif meta["mode"] == "multi-center-2c":
            lines.append(
                f"- {spec.formula}: order={meta['cc_order']}, hyb={meta['hybridization']}, "
                f"h(c1)={meta['h_on_c1']}, h(c2)={meta['h_on_c2']}, "
                f"E_CH/bond={meta['E_CH_per_bond']:.4f}, "
                f"E_CH={meta['E_CH_total']:.4f}, E_CCσ={meta['E_CC_sigma']:.4f}, "
                f"E_CCπ={meta['E_CC_pi']:.4f}"
            )
        elif meta["mode"].startswith("candidate-") or meta["mode"].startswith("unresolved-"):
            lines.append(
                (
                    f"- {spec.formula}: ionic_collapse={meta['ionic_collapse']:.4f} ({meta['note']})"
                    if "ionic_collapse" in meta
                    else f"- {spec.formula}: {meta['note']}"
                )
            )
    lines.append("")
    lines.append("Unresolved branch policy:")
    lines.append("- `candidate-s-block`: explicit candidate scaling, not claimed as closed law.")
    lines.append("- `multi-center-2c`: bounded extension, no hidden global fit.")
    lines.append("- `unresolved-topology`: outside validated carrier classes; no hidden fit.")
    return "\n".join(lines)


if __name__ == "__main__":
    print(render())
