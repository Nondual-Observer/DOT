#!/usr/bin/env python3
"""
Reusable boundary-math engine for DOT.

This module consolidates the working prototype scripts into one importable layer:
  carrier -> projector -> split -> response -> pairing -> gluing -> involution

The goal is not to replace the exploratory scripts, but to provide a stable
functional core that later analyses can import instead of copying logic.
"""

from __future__ import annotations

import cmath
from statistics import mean
from typing import Dict, Iterable, List, Sequence, Tuple


MAX_N_DEFAULT = 200

MODULI = {
    5: {"annihilated": 4, "name": "isospin", "pairs": [(1, 4), (2, 3)]},
    7: {"annihilated": 5, "name": "spinor", "pairs": [(1, 6), (2, 5), (3, 4)]},
    11: {
        "annihilated": 6,
        "name": "string",
        "pairs": [(1, 10), (2, 9), (3, 8), (4, 7), (5, 6)],
    },
}


# ── Carriers ────────────────────────────────────────────────────

def partition_coeffs(n_max: int = MAX_N_DEFAULT) -> list[int]:
    p = [0] * (n_max + 1)
    p[0] = 1
    for k in range(1, n_max + 1):
        for n in range(k, n_max + 1):
            p[n] += p[n - k]
    return p


def euler_cut_coeffs(n_max: int = MAX_N_DEFAULT) -> list[int]:
    c = [0] * (n_max + 1)
    c[0] = 1
    for k in range(1, n_max + 1):
        for n in range(n_max, k - 1, -1):
            c[n] -= c[n - k]
    return c


def phi_coeffs(n_max: int = MAX_N_DEFAULT) -> list[int]:
    c = [0] * (n_max + 1)
    c[0] = 1
    n = 1
    while n * n <= n_max:
        c[n * n] += 2
        n += 1
    return c


def psi_coeffs(n_max: int = MAX_N_DEFAULT) -> list[int]:
    c = [0] * (n_max + 1)
    n = 0
    while True:
        t = n * (n + 1) // 2
        if t > n_max:
            break
        c[t] += 1
        n += 1
    return c


def fab_coeffs(
    n_max: int = MAX_N_DEFAULT,
    a_exp: float = 1.0,
    b_exp: float = 1.0,
) -> list[float]:
    c = [0.0] * (n_max + 1)
    for n in range(-n_max, n_max + 1):
        t_a = n * (n + 1) // 2
        t_b = n * (n - 1) // 2
        exp = int(a_exp * t_a + b_exp * t_b)
        if 0 <= exp <= n_max:
            c[exp] += 1.0
    return c


def sigma1(n_max: int = MAX_N_DEFAULT) -> list[int]:
    out = [0] * (n_max + 1)
    for d in range(1, n_max + 1):
        for n in range(d, n_max + 1, d):
            out[n] += d
    return out


def e2_response(n_max: int = MAX_N_DEFAULT) -> list[int]:
    sig1 = sigma1(n_max)
    return [0] + [-24 * sig1[n] for n in range(1, n_max + 1)]


# ── Projector / Split ───────────────────────────────────────────

def residue_project(coeffs: Sequence[complex], p: int, r: int) -> list[complex]:
    omega = cmath.exp(2j * cmath.pi / p)
    out = [0j] * len(coeffs)
    for n, a_n in enumerate(coeffs):
        phase_sum = sum(omega ** ((n - r) * m) for m in range(p))
        out[n] = complex(a_n) * phase_sum / p
    return out


def split_channels(coeffs: Sequence[complex], p: int) -> dict[int, list[complex]]:
    return {r: residue_project(coeffs, p, r) for r in range(p)}


def classify_channels(channels: dict[int, list[complex]], ann: int) -> dict[str, list[int]]:
    result = {"annihilated": [], "surviving": [], "backbone": []}
    for r in channels:
        if r == ann:
            result["annihilated"].append(r)
        elif r == 0:
            result["backbone"].append(r)
        else:
            result["surviving"].append(r)
    return result


def residue_loads(coeffs: Sequence[complex], p: int) -> dict[int, float]:
    all_abs = [abs(coeffs[n]) for n in range(1, len(coeffs)) if abs(coeffs[n]) > 1e-12]
    global_abs = mean(all_abs) if all_abs else 1.0
    st = {}
    for r in range(p):
        bucket = [abs(coeffs[n]) for n in range(1, len(coeffs)) if n % p == r]
        st[r] = mean(bucket) / global_abs if bucket and global_abs else 0.0
    return st


def reconstruction_error(coeffs: Sequence[complex], p: int) -> float:
    pieces = [residue_project(coeffs, p, r) for r in range(p)]
    max_err = 0.0
    for n, a_n in enumerate(coeffs):
        total = sum(piece[n].real for piece in pieces)
        max_err = max(max_err, abs(total - complex(a_n).real))
    return max_err


# ── Involution ──────────────────────────────────────────────────

def seed_shift(coeffs: Sequence[complex], k: int) -> list[complex]:
    """Integer seed shift: q^k * f(q).

    This is the discrete analogue of the q^α seed/casimir shift used in eta/theta
    formulas. Fractional α (e.g. 1/24) requires a different basis (Q = q^(1/24))
    and is intentionally not mixed into the integer-index coefficient arrays.
    """
    if k < 0:
        raise ValueError("seed_shift expects k >= 0")
    out = [0j] * len(coeffs)
    for n, a_n in enumerate(coeffs):
        j = n + k
        if j < len(out):
            out[j] = complex(a_n)
    return out


def seed_trim_leading_zeros(coeffs: Sequence[complex]) -> list[complex]:
    """Trim leading exact zeros from the series (seed alignment helper)."""
    i = 0
    while i < len(coeffs) and abs(coeffs[i]) < 1e-15:
        i += 1
    return [complex(x) for x in coeffs[i:]] if i else [complex(x) for x in coeffs]


def seed_normalize_l1(coeffs: Sequence[complex], start: int = 1) -> list[complex]:
    """Normalize by L1 mass of coefficients (useful as seed/baseline)."""
    total = sum(abs(coeffs[n]) for n in range(start, len(coeffs)))
    if total <= 0:
        return [complex(x) for x in coeffs]
    return [complex(x) / total for x in coeffs]


def sign_flip_coeffs(coeffs: Sequence[complex]) -> list[complex]:
    return [complex(a_n) * ((-1) ** n) for n, a_n in enumerate(coeffs)]


def involution_alignment(original: Sequence[complex], flipped: Sequence[complex]) -> dict[str, float]:
    # normalized dot / parity-aware alignment
    num = 0.0
    den_a = 0.0
    den_b = 0.0
    alt_num = 0.0
    for n in range(1, min(len(original), len(flipped))):
        a = complex(original[n]).real
        b = complex(flipped[n]).real
        num += a * b
        den_a += a * a
        den_b += b * b
        alt_num += ((-1) ** n) * a * b
    corr = num / ((den_a * den_b) ** 0.5) if den_a > 0 and den_b > 0 else 0.0
    alt_corr = alt_num / ((den_a * den_b) ** 0.5) if den_a > 0 and den_b > 0 else 0.0
    return {"corr": corr, "alternating_corr": alt_corr}


# ── Response / Pairing / Gluing ────────────────────────────────

def channel_response(channel: Sequence[complex], response: Sequence[float]) -> float:
    num = 0.0
    den = 0.0
    for n in range(1, min(len(channel), len(response))):
        mag = abs(channel[n])
        den += mag
        num += mag * abs(response[n])
    return num / den if den > 0 else 0.0


def pair_channels(
    channels: dict[int, Sequence[complex]],
    pairs: Sequence[Tuple[int, int]],
) -> dict[tuple[int, int], list[complex]]:
    composites = {}
    for a, b in pairs:
        composites[(a, b)] = [channels[a][n] + channels[b][n] for n in range(len(channels[a]))]
    return composites


def pair_stats(
    loads: dict[int, float],
    pairs: Sequence[Tuple[int, int]],
    ann: int | None = None,
) -> list[dict[str, float | tuple[int, int] | bool]]:
    out = []
    for a, b in pairs:
        joint = loads[a] + loads[b]
        out.append(
            {
                "pair": (a, b),
                "joint": joint,
                "balance_a": loads[a] / joint if joint > 1e-12 else 0.0,
                "balance_b": loads[b] / joint if joint > 1e-12 else 0.0,
                "broken": ann in (a, b) if ann is not None else False,
            }
        )
    return out


def dirichlet_partial(coeffs: Sequence[complex], s: float) -> complex:
    total = 0j
    for n in range(1, len(coeffs)):
        if abs(coeffs[n]) > 1e-15:
            total += coeffs[n] / (n ** s)
    return total


# ── Pipeline helpers ────────────────────────────────────────────

def carrier_catalog(n_max: int = MAX_N_DEFAULT) -> dict[str, list[complex]]:
    return {
        "P(q)": [complex(x) for x in partition_coeffs(n_max)],
        "f(-q)": [complex(x) for x in euler_cut_coeffs(n_max)],
        "phi(q)": [complex(x) for x in phi_coeffs(n_max)],
        "psi(q)": [complex(x) for x in psi_coeffs(n_max)],
        "f(q,q)": [complex(x) for x in fab_coeffs(n_max, 1.0, 1.0)],
        "f(q,q^2)": [complex(x) for x in fab_coeffs(n_max, 1.0, 2.0)],
    }


def pipeline_summary(
    coeffs: Sequence[complex],
    p: int,
    response: Sequence[float] | None = None,
) -> dict[str, object]:
    meta = MODULI[p]
    ann = meta["annihilated"]
    pairs = meta["pairs"]
    response = response if response is not None else e2_response(len(coeffs) - 1)

    channels = split_channels(coeffs, p)
    classes = classify_channels(channels, ann)
    loads = residue_loads(coeffs, p)
    pair_info = pair_stats(loads, pairs, ann)
    ch_resp = {r: channel_response(channels[r], response) for r in range(p)}
    Lvals = {r: dirichlet_partial(channels[r], 7.0) for r in range(p)}
    return {
        "p": p,
        "meta": meta,
        "reconstruction_error": reconstruction_error(coeffs, p),
        "classes": classes,
        "loads": loads,
        "responses": ch_resp,
        "pairs": pair_info,
        "dirichlet_abs": {r: abs(v) for r, v in Lvals.items()},
    }


__all__ = [
    "MAX_N_DEFAULT",
    "MODULI",
    "partition_coeffs",
    "euler_cut_coeffs",
    "phi_coeffs",
    "psi_coeffs",
    "fab_coeffs",
    "sigma1",
    "e2_response",
    "residue_project",
    "split_channels",
    "classify_channels",
    "residue_loads",
    "reconstruction_error",
    "seed_shift",
    "seed_trim_leading_zeros",
    "seed_normalize_l1",
    "sign_flip_coeffs",
    "involution_alignment",
    "channel_response",
    "pair_channels",
    "pair_stats",
    "dirichlet_partial",
    "carrier_catalog",
    "pipeline_summary",
]
