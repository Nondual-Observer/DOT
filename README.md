# Distinction Observable Theory (DOT)

> **Languages:** [English](README.md) | [Русский](README_RU.md)

[![DOI](https://zenodo.org/badge/1188736747.svg)](https://doi.org/10.5281/zenodo.19162312)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/Theory-CC%20BY--NC--SA%204.0-blue.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![License: MIT](https://img.shields.io/badge/Code-MIT-yellow.svg)](LICENSE)

> *"The unmanifest [Prakriti] is endowed with the three gunas… The gunas, by their nature, are pleasure [Sattva], pain [Rajas], and indifference [Tamas]. Their purpose is to illuminate, to activate, and to restrict. They suppress each other, support each other, produce each other, and act together, like a lamp [where oil, wick, and flame act in concert].*
>
> *…Purusha [pure consciousness] is merely a witness to what occurs. It is endowed with absolute isolation, complete indifference, the capacity to contemplate, and absolute non-action.*
>
> *…For the sake of Purusha's contemplation of Prakriti, and for its ultimate liberation, their union occurs. It is like the union of the lame and the blind. From this union, creation arises."*
> — *Sankhya Karika, 11–21*

---

## What this code does

This repository contains **executable numerical verification** of Distinction Observable Theory (DOT) — a set of Python scripts that reproduce all predictions of the theory **with zero free parameters**.

All constants are derived from the geometry of a single object — the **Octahedron K(2,2,2)** (6 vertices, 12 edges, 8 faces).

### Quick Start

```bash
cd ../companion_code
pip install -r requirements.txt    # only numpy

# Run everything:
python3 scripts/dot_companion_verify.py --all

# Or run individual modules:
python3 scripts/dot_companion_verify.py --full        # 21 observables dashboard
python3 scripts/dot_companion_verify.py --vacuum64    # 64-state vacuum engine
python3 scripts/dot_companion_verify.py --chem        # Molecular bond energies
python3 scripts/dot_companion_verify.py --tails       # Mellin tail calculator
python3 scripts/dot_companion_verify.py --hydrogen-dyn  # 48-dim Cayley graph dynamics
```

### What each module verifies

| Module | What it verifies | Key metric |
|:-------|:-----------------|:-----------|
| `--full` | 21 observables: 9 particle masses, 4 couplings, 4 cosmological fractions, g-2, fine structure, Bethe log | Mean error: **0.0002%** |
| `--vacuum64` | 64 vacuum states of K(2,2,2), spectral projections → quark charges | All 1/3, 2/3, 1/4 — **exact** |
| `--chem` | 14 molecules (H₂, H₂O, CH₄, NH₃, HF, C₂H₂, C₂H₄, C₂H₆, etc.) | Mean error: **0.32%** |
| `--tails` | Complete mass atlas of 26 particles with Mellin corrections | Per-particle δ₀ + Ω breakdown |
| `--hydrogen-dyn` | 2p→1s decay dynamics on 48-dim Cayley graph | P(1s) → 98.7%, norm = 1.000 |

### Repository Structure

```
companion_code/
├── scripts/
│   ├── dot_companion_verify.py       # CLI entry point
│   ├── dot_hydrogen_dynamic_v10.py   # Chemistry model (current)
│   └── companion_legacy/
│       ├── dot_full_verification.py          # 21-observable dashboard
│       ├── dot_all_particles_tail_calculator.py  # Mellin tail atlas
│       ├── dot_64state_engine.py             # 64-state vacuum engine
│       ├── dot_hydrogen_dynamic_v5_1.py      # Cayley graph dynamics
│       └── dot_boundary_engine.py            # Reusable boundary math core
├── outputs/                          # Saved output snapshots
├── requirements.txt                  # numpy>=1.26
└── README_code.md                    # Code-specific documentation
```

---

## Theory Overview

**Distinction Observable Theory (DOT)** proposes that the entire architecture of fundamental physics
can be derived from the combinatorial and spectral properties of one graph:
the **complete tripartite graph K(2,2,2)** — the 1-skeleton of the regular octahedron.

From this single structure, with **no free parameters**, DOT derives:

- **The fine structure constant**: α⁻¹ = 432/π − 47γ³/2 ≈ 137.036 (error < 0.001%)
- **Particle masses**: 26 particles from a single formula M = C/γᵏ · mₑ · exp(δ₀ + Ω)
- **Cosmological fractions**: Ωb = 4/81, Ωc = 21/81, ΩΛ = 56/81 (exact closure Σ = 1)
- **Quark charges**: 1/3, 2/3 computed as spectral projections of K(2,2,2)
- **The Weinberg angle**: sin²θ_W = 2/9 = 3γ²
- **Molecular bond energies**: H₂, CH₄, H₂O, HF, … with 0.3% mean accuracy

where γ = √6/9 is the **observer anisotropy** — the unique geometric invariant of the octahedron.

---

## Three Principles: Architecture of the Operator

The entire theory is built upon **three interconnected principles**, each arising from the previous one:

### 1. The Closure Law: ∂² = 0

Nothing in nature exists by itself. Every tension must find its absolute compensation — all waves and asymmetries must sum to zero.

This is the **Principle of Closure** (∂² = 0): the boundary of a boundary is zero. No structure can exist unless it closes upon itself.

### 2. The Face Paradox: three does not divide by two

The minimal volumetric structure compatible with ∂² = 0 is the **Octahedron** (3 axes × 2 poles = 6 vertices). But each face of the octahedron is a **triangle** (3 edges), while the basic logic of information is **binary** (yes/no, 0/1 — 2 states).

A fundamental paradox arises: a wall of 3 edges tries to fit symmetrically into the logic of 2. This is impossible without a remainder. **Three does not divide by two.**

This tiny "burr" — a topological mismatch — never disappears. It is the source of all physics: from it arises the observer anisotropy γ = √6/9.

### 3. The Law of Impenetrability: the magic of coprime numbers

To "spread out" this mismatch, the vacuum is forced to build protective layers around it — horizons nested like Russian dolls. Each layer consists of an **Inner Body** (e.g. the number 80) and an **Outer Background** (the number 81).

But why don't these layers collapse back into zero? Because two adjacent integers are always **coprime**: 80 and 81 share no common prime divisor. Their internal frequencies are absolutely orthogonal.

The Body pulses on its frequencies (twos, fives), and the Background on its own (threes). Sound from the Body strikes the Background wall and is **reflected back 100%**, unable to dissolve. The wall is impenetrable.

> **Result:** ∂² = 0 produces the octahedron → the 3-vs-2 incompatibility produces γ → coprimality locks the structure into stable horizons. From these three layers, **everything** grows: particle masses, cosmological fractions, quark charges.

---

## Publications

The theory is presented in three volumes, published on Zenodo:

| # | Title | DOI | Focus |
|:-:|:------|:----|:------|
| **I** | [Foundations and the Octahedral Machine](en/DOT_foundations_and_machine_en.md) | [10.5281/zenodo.19162312](https://doi.org/10.5281/zenodo.19162312) | K(2,2,2), boundary operator ∂²=0, D/F/C triad, 6 statuses, ⊙ operation, Observer |
| **II** | [Mathematical Framework, Number Theory, and Spectral Geometry](en/DOT_mathematical_framework_en.md) | [10.5281/zenodo.19162523](https://doi.org/10.5281/zenodo.19162523) | Ramanujan τ, ζ(s) spectral interpretation, Hecke operators, modular carriers |
| **III** | [Physical Realization and the Structure of Matter](en/DOT_physical_realization_en.md) | [10.5281/zenodo.19162523](https://doi.org/10.5281/zenodo.19162523) | 26 particle masses, cosmological fractions, molecular chemistry, gravity as status diffusion |

**Supplementary:**
| | Title | Focus |
|:-:|:------|:------|
| **IV** | [Octahedral Proof Calculus](en/DOT_octahedral_proof_calculus_en.md) | Formal verification framework: axioms, lemmas, and derivation chains (DOI: [10.5281/zenodo.19162523](https://doi.org/10.5281/zenodo.19162523)) |
| **V** | [Code Availability Statement](en/DOT_code_availability_en.md) | Reproducibility guide for the companion code |

---

## Fundamental Constants of DOT

| Symbol | Value | Origin |
|:-------|:------|:-------|
| γ = √6/9 | 0.27216553 | Observer anisotropy of K(2,2,2) |
| γ² = 2/27 | 0.07407407 | Spectral gap ratio |
| α⁻¹ = 432/π − 47γ³/2 | 137.03600 | Fine structure constant |
| sin²θ_W = 2/9 | 0.22222 | Weinberg angle (bare) |
| Koide K₄ = 2/3 | 0.66667 | Lepton mass relation |
| 432 = j(i)/4 | 16 × 27 | Ramanujan pixel (Dirac ⊗ Higgs) |

---

## Citation

```bibtex
@software{zhuk_2026_dot,
  author    = {Zhuk, Igor M.},
  title     = {Distinction Observable Theory (DOT): Foundations, 
               Mathematical Framework, and Physical Realization},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.19162312},
  url       = {https://github.com/nondual-observer/distinction-observable-theory}
}
```

---

## Support the Research

This project is developed as **independent open research** with no institutional funding.

**Donations are voluntary.**

| Currency | Network | Address |
|----------|---------|---------|
| Bitcoin | BTC | `bc1qlaxsrum7fxpml57nsrtkjfkkxl5v3xtj4d0uxe` |
| USDT | TRC20 | `TM8U2EqVaT3tjvG6NyuKTqY4F5qc2A69Sy` |
| Ethereum | ETH | `0x4fFc68f0d55d19Fa5EBd5f6570a41E100aFe4a98` |

---

## License

**Code:** [MIT License](LICENSE) — Free to use, modify, and distribute.  
**Theory & Documentation:** [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) — Non-commercial use with attribution and share-alike.

---

*© 2026 Igor M. Zhuk. All rights reserved under the respective licenses.*
