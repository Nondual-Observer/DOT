# Distinction Observable Theory (DOT)

> **Languages:** [English](README.md) | [Русский](ru/README_RU.md)

[![DOI](https://zenodo.org/badge/1188736747.svg)](https://doi.org/10.5281/zenodo.19210790)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/Theory-CC%20BY--NC--SA%204.0-blue.svg)](LICENSE-THEORY.md)
[![License: Apache-2.0](https://img.shields.io/badge/Code-Apache--2.0-yellow.svg)](LICENSE)

> *"The unmanifest [Prakriti] is endowed with the three gunas… The gunas, by their nature, are pleasure [Sattva], pain [Rajas], and indifference [Tamas]. Their purpose is to illuminate, to activate, and to restrict. They suppress each other, support each other, produce each other, and act together, like a lamp [where oil, wick, and flame act in concert].*
>
> *…Purusha [pure consciousness] is merely a witness to what occurs. It is endowed with absolute isolation, complete indifference, the capacity to contemplate, and absolute non-action.*
>
> *…For the sake of Purusha's contemplation of Prakriti, and for its ultimate liberation, their union occurs. It is like the union of the lame and the blind. From this union, creation arises."*
> — *Sankhya Karika, 11–21*

---

## What this repository contains

This repository does not contain only companion numerical code. It contains an **assembled TNR/DOT package** in three forms:

- **theory corpus** — texts that fix the machine’s architectural basis;
- **reference engine** — an executable generative chain connecting constants, particles, nuclei, and molecular projections;
- **verification layer** — reproducible audits showing that the same grammar works across different floors of the machine.

In other words, this repository is meant neither only for reading theory nor only for running calculations. It shows how the same structural framework can be written as ontology, as computational architecture, and as executable code.

## What DOT is

**Distinction Observable Theory (DOT)** describes a machine in which primary reality is not made of ready-made objects, but of **distinctions, boundaries, and acts of closure**. In this picture, an object is not the starting point of theory; it appears later as a stabilized readout of a deeper structural grammar. DOT therefore begins not with finished “particles” or “bodies”, but with a lower grammar of prohibition, identity, polarity, boundary, transition, and closure.

In its current canonical form, the lower floor of the machine is read as the ladder

```text
0 -> 1 -> 2 -> 6 -> 12 -> 8
```

where `0` is the vacuum fixed-point, `1` is unary identity, `2` is the first polarity, `6` is the full triadic boundary, `12` is the transitional edge-network, and `8` is the first closure. At this same floor, action-types are already separated: addition builds horizons, subtraction reads deficits, multiplication assembles structure, division performs oriented readout, and exponentiation seals and amplifies closure.

From this follows a central DOT thesis: **structure, act, and observation do not reduce to one another**. Structure holds symmetry. Act is asymmetric by definition, because it delineates, orients, normalizes, and leaves a remainder. Observation holds distinction as an invariant and is therefore not just another act. This separation forms the machine’s basic operational block:

```text
carrier + act + readout
```

The first strong carrier architecture on which this grammar becomes a reproducible machine is the octahedron `K(2,2,2)`. It is not “the first object of the whole world”, but it is the first stable carrier on which distinction, addressing, seams, and readout assemble into a working topological grammar. From here arise the visible/shadow packets `24 / 48` and `23 / 47`, the shell corridor `94 / 95 / 96`, the higher horizons `120`, `136`, `200`, `252`, `432`, `1728`, and their machine-readable structural dictionary.

## Universality of DOT

DOT does not claim to be only a narrow physical model. It proposes a more general grammar of distinction that can be read simultaneously in several registers.

At the lower level it appears as structural arithmetic: prohibition, identity, polarity, boundary, transition, closure. At the next level the same framework appears as carrier topology: seams, cycles, axes, shells, visible and shadow components. Above that it becomes an operational machine: unresolved tails generate pressure, pressure triggers act, act leaves traces and remainder, readout fixes a new state. In the reference engine the same grammar is already realized as a generative chain for constants, particles, nuclei, and molecular projections.

This is what constitutes the universality of DOT: the same grammar persists when one moves from mathematics to machine architecture and from there to physically readable structure.

Several consequences follow from this:
- the object is secondary to distinction and boundary;
- act is asymmetric by definition;
- observation preserves distinction and is not reducible to act;
- visible and shadow are assembled as a single packet;
- higher horizons are derived from lower-floor grammar rather than introduced from outside.

## What is already implemented

At the current stage, the repository contains not merely a set of local formulas but an entire reference chain of the machine.

1. **Structural layer**
   - the lower floor is assembled;
   - `structure / act / observation` are separated;
   - visible/shadow packets are assembled;
   - the canonical structural dictionary is frozen.

2. **Reference engine**
   - the generative chain `L0 -> L1 -> L2 -> L3` is implemented, plus `L4` as a layer of fundamental readouts;
   - geometric constants feed the particle layer, then the nuclear layer, and then molecular projections.

3. **Verification layer**
   - reproducible structural audits are present;
   - numerical checks exist for particle, nuclear, and chemistry layers;
   - a machine-readable package exists for canonical nodes and frontier bands.

4. **Publication layer**
   - theory is presented as a connected corpus of texts;
   - machine architecture is separated from the open frontier;
   - code and theory can already be read as one connected package.

This is an important boundary. In this repository, DOT is no longer just a hypothesis and no longer just a collection of numerical coincidences. It is an assembled architecture of distinction with a reference realization and a verifiable numerical layer.

## What the code does

The code in this repository serves three purposes:

- to reproduce the numerical consequences of the theory;
- to show that the same grammar truly executes as a generative chain;
- to connect the theoretical corpus to concrete computable objects.

In practice, this means that the reference engine and related modules:
- compute fundamental readouts and constants;
- assemble particle masses and their tail layer;
- build the nuclear layer;
- compute molecular projections and bond energies;
- allow one to check how structural grammar passes into an executable physical scheme.

### Quick Start

```bash
cd companion_code
pip install -r requirements.txt    # only numpy

# Run the full 4-level generative chain:
python3 scripts/tnr_comprehensive_engine.py
```

### What the engine computes

| Level | What it computes | Key metric |
|:------|:-----------------|:-----------|
| **L0** | Geometric constants: γ = √6/9, precision α, Rydberg | α⁻¹ error: **0.0000068σ** |
| **L1** | 24 particle masses from topological addresses + Ramanujan carriers | All **< 0.001%** error |
| **L2** | 98 nuclear isotope masses via DOT-SEMF | All **< 0.001%** error |
| **L3** | 14 molecular bond energies (H₂, H₂O, CH₄, NH₃, HF…) | Mean error: **0.32%** |
| **L4** | Fundamental readouts: α⁻¹, sin²θ_W, Koide, α_s(M_Z) | **Zero free parameters** |

### Formal Proofs (Lean 4)

We have begun mathematically verifying the physical derivations using the **Lean 4 interactive theorem prover**. 
- `formal_proofs/DOT_Sn_Isotopes.lean` provides an executable, mathematically rigorous proof that the DOT-SEMF nuclear formula applied to Tin (Sn) isotopes accurately reproduces AME2020 mass defects using the Ramanujan spectrum.

### Repository Structure

```
companion_code/
├── formal_proofs/
│   └── DOT_Sn_Isotopes.lean          # ★ Lean 4 mathematical verification
├── scripts/
│   └── tnr_comprehensive_engine.py   # ★ Full 4-level generative engine
├── outputs/                          # Saved output snapshots
├── requirements.txt                  # numpy>=1.26
└── README_code.md                    # Code-specific documentation
```


---

## Theory Overview

**Distinction Observable Theory (DOT)** does not describe a set of isolated physical formulas. It describes a **machine of distinction** in which primary reality is not made of ready-made objects, but of boundaries, prohibitions, polarities, transitions, and acts of closure. In this picture, the object is not the beginning of theory; it appears later as a stabilized readout of a deeper structural grammar.

In its present canonical form, the lower layer of the machine is read as the ladder

```text
0 -> 1 -> 2 -> 6 -> 12 -> 8
```

where `0` gives the vacuum fixed-point, `1` gives unary identity, `2` the first polarity, `6` the triadic boundary, `12` the transitional edge-network, and `8` the first closure. At this same level, action-types are already separated: addition builds horizons, subtraction reads deficits, multiplication assembles structure, division performs oriented readout, and exponentiation seals and amplifies closure.

From this follows the basic DOT distinction: **structure, act, and observation do not reduce to one another**. Structure holds symmetry. Act is asymmetric by definition, because it delineates, orients, normalizes, and leaves a remainder. Observation preserves distinction as an invariant and therefore is not merely another act. This separation forms the machine’s core operational block:

```text
carrier + act + readout
```

The first strong carrier architecture on which this grammar becomes reproducible is the octahedron `K(2,2,2)`. It is not “the first object of the whole world”, but it is the first stable carrier on which distinction, addressing, seams, and readout assemble into a working topology grammar. From this arise the visible/shadow packets `24 / 48` and `23 / 47`, the shell corridor `94 / 95 / 96`, the higher horizons `120`, `136`, `200`, `252`, `432`, `1728`, and the machine-readable structural dictionary that organizes them.

The universality of DOT lies in the fact that one and the same grammar operates across several registers. At the lowest level it appears as structural arithmetic. At the next level it appears as carrier topology. Above that it becomes an operational machine of states, traces, and closures. In the reference engine the same grammar is already realized as a generative chain for constants, particles, nuclei, and molecular projections. DOT in this repository is therefore presented not only as theory and not only as code, but as a connected package: texts, canonical package, reference engine, and reproducible audits.

### Lower grammar of the machine

The lower grammar of DOT is not given by a list of objects, but by a handful of hard laws.

### 1. Prohibition of self-readout

The machine begins with the restriction `0/0`. As long as distinction has not yet arisen, vacuum cannot be read as a relation to itself. This prohibition generates the entire lower ladder of distinction: identity, polarity, boundary, transition, and closure grow out of it.

### 2. Asymmetry of act

In DOT, actions are not interchangeable arithmetic operations. They are separated by role:

- `+` builds horizon;
- `-` reads gap and deficit;
- `*` assembles structure;
- `/` performs readout and normalization;
- `^` gives closure and amplification.

Act in DOT is therefore asymmetric by definition. Symmetry belongs to structure, not to act.

### 3. Separation of structure / act / observation

DOT strictly distinguishes carrier, transition, and readout. Structure holds symmetry. Act initiates deformation and routing and leaves transition traces. Observation preserves distinction as a stable invariant. An important consequence follows: observation may be present without a new act, and distinction is not identical to transition.

### 4. Visible / shadow grammar

When the lower floor is assembled into a carrier, the machine yields two linked branches: visible and complement/shadow. Their basic packets are `24 / 48` and `23 / 47`. From them are built shell layers, corridors, and higher bands. The visible branch governs assembly and closure. The shadow branch governs witness, remainder, and complement readout. These branches do not exist independently: the machine state is read only through their linkage.

### 5. Higher horizons as a consequence of the lower floor

Higher machine nodes are not inserted from outside. They are assembled from already discovered lower-floor invariants and shell grammar. This is especially clear in visible assembly:

- `120 = 24*5`
- `136 = 24*6 - 8`
- `200 = 24*8 + 8`
- `252 = 24*10 + 12`
- `432 = 24*18`

Higher horizons are thus not “magical numbers”; they are consequences of lower-floor grammar, visible shell assembly, and act-level seams `±8`, `+12`, `+24`.

### 6. Realized generative chain

In code, this architecture is already realized as a reference chain:

- `L0` — geometric and coupling constants;
- `L1` — particle layer;
- `L2` — nuclear layer;
- `L3` — molecular projections;
- `L4` — fundamental readouts.

The repository therefore records more than a collection of theoretical claims. It shows that one and the same grammar can be written as ontology, as structural dictionary, and as executable engine.

---

## Publications

The theory is presented in three volumes, published on Zenodo:

| # | Title | DOI | Focus |
|:-:|:------|:----|:------|
| **I** | [Foundations and the Octahedral Machine](en/DOT_foundations_and_machine_en.md) | [10.5281/zenodo.19210790](https://doi.org/10.5281/zenodo.19210790) | K(2,2,2), boundary operator ∂²=0, D/F/C triad, 6 statuses, ⊙ operation, Observer |
| **II** | [Mathematical Framework, Number Theory, and Spectral Geometry](en/DOT_mathematical_framework_en.md) | [10.5281/zenodo.19210790](https://doi.org/10.5281/zenodo.19210790) | Ramanujan τ, ζ(s) spectral interpretation, Hecke operators, modular carriers |
| **III** | [Physical Realization and the Structure of Matter](en/DOT_physical_realization_en.md) | [10.5281/zenodo.19210790](https://doi.org/10.5281/zenodo.19210790) | 26 particle masses, cosmological fractions, molecular chemistry, gravity as status diffusion |

**Supplementary:**
| | Title | Focus |
|:-:|:------|:------|
| **IV** | [Octahedral Proof Calculus](en/DOT_octahedral_proof_calculus_en.md) | Formal verification framework: axioms, lemmas, and derivation chains (DOI: [10.5281/zenodo.19210790](https://doi.org/10.5281/zenodo.19210790)) |
| **V** | [Code Availability Statement](en/DOT_code_availability_en.md) | Reproducibility guide for the companion code |
| **VI** | [Machine Architecture Overview](en/DOT_machine_architecture_overview_en.md) | Full architectural layer map of the DOT machine |
| **VII** | [Terminology and Layer Map](en/DOT_terminology_and_layer_map_en.md) | Reference terminology dictionary and structural layer chart |
| **VIII** | [Formal Verification (Lean 4)](companion_code/formal_proofs/DOT_Sn_Isotopes.lean) | Executable mathematical proof of the DOT-SEMF nuclear formula |

---

## Fundamental Constants of DOT

Below are the basic invariants and readouts that in the current codebase and theory texts play the role of the machine’s support constants. For the README, what matters is not only their numerical value, but the fact that they are already read as elements of one architecture grammar: lower-floor geometry, shell assembly, chiral corrections, and modular pivots.

| Symbol | Value | Origin |
|:-------|:------|:-------|
| γ = √6/9 | 0.27216553 | Observer anisotropy on the carrier layer `K(2,2,2)` |
| γ² = 2/27 | 0.07407407 | Basic spectral / metric ratio |
| α⁻¹ | 137.035999084… | Precision chiral structural law over nodes `432`, `47`, `72`, `136`, `252` |
| sin²θ_W = 2/9 | 0.22222 | Basic electroweak readout of the lower layer |
| Koide K₄ = 2/3 | 0.66667 | Frozen lepton mass readout |
| 432 = j(i)/4 | 16 × 27 | Universal modular pivot of the machine |

---

## Citation

```bibtex
@software{zhuk_2026_dot,
  author    = {Zhuk, Igor M.},
  title     = {Distinction Observable Theory (DOT): Foundations, 
               Mathematical Framework, and Physical Realization},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.19210790},
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

**Code:** [Apache License 2.0](LICENSE) — Open-use software license with explicit patent terms.  
**Theory & Documentation:** [CC BY-NC-SA 4.0](LICENSE-THEORY.md) — Non-commercial use with attribution and share-alike.

---

*© 2026 Igor M. Zhuk. All rights reserved under the respective licenses.*
