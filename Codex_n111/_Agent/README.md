# Distinction Observable Theory (DOT)

> **Languages:** [English](README.md) | [Русский](ru/README_RU.md)

[![DOI](https://zenodo.org/badge/1188736747.svg)](https://doi.org/10.5281/zenodo.19236868)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/Theory-CC%20BY--NC--SA%204.0-blue.svg)](LICENSE-THEORY.md)
[![License: Apache-2.0](https://img.shields.io/badge/Code-Apache--2.0-yellow.svg)](LICENSE)

> *"The unmanifest [Prakriti] is endowed with the three gunas… The gunas, by their nature, are pleasure [Sattva], pain [Rajas], and indifference [Tamas]. Their purpose is to illuminate, to activate, and to restrict. They suppress each other, support each other, produce each other, and act together, like a lamp [where oil, wick, and flame act in concert].*
>
> *…Purusha [pure consciousness] is merely a witness to what occurs. It is endowed with absolute isolation, complete indifference, the capacity to contemplate, and absolute non-action.*
>
> *…For the sake of Purusha's contemplation of Prakriti, and for its ultimate liberation, their union occurs. It is like the union of the lame and the blind. From this union, creation arises."*
> — *Sankhya Karika, 11–21*

---

## What this repository is

This repository is not just a folder of theory texts and not just a folder of
scripts. It is DOT assembled as a single system.

It contains three connected layers:

- **theory** — the Russian and English text corpus;
- **machine** — the architectural map of how the theory works as a structured
  system;
- **code** — the companion computational layer that carries the same framework
  through constants, particles, nuclei, molecular projections, and chemistry.

The point of the repository is simple: to show that one and the same structural
framework can be read as theory, as machine architecture, and as reproducible
code.

## What DOT is, in plain language

**Distinction Observable Theory** starts from a question that comes before ready-
made objects: *what makes distinction possible at all?*

Ordinarily we speak as if a thing exists first and only then gets seen,
measured, or described. DOT proposes a different order. First there must be:

- a boundary;
- a ban on coincidence;
- polarity;
- transition;
- closure;
- and only then an object as a stable readout.

That is why DOT is not simply “another physical model.” It is an attempt to
describe a framework in which:

- structure;
- act;
- observation

do not reduce to one another.

In its current canonical form, the lower layer of the machine is read as the
ladder:

```text
0 -> 1 -> 2 -> 6 -> 12 -> 8
```

where:

- `0` is the vacuum fixed-point;
- `1` is unary identity;
- `2` is the first polarity;
- `6` is the triadic boundary;
- `12` is the transitional edge-network;
- `8` is the first closure.

These are not “magic numbers.” They are support nodes of the machine’s lower
grammar.

## The code layer

In this repository the theory does not hang separately from the code. There is
a full computational layer that shows DOT working not only as a descriptive
language, but as a **generative calculation scheme**.

There are two distinct working forms here:

- **Python companion-code** — the main numerical engine;
- **Lean 4** — the formal proof layer for selected results.

### Python companion-code

The main code lives in:

- [companion_code/](companion_code/)

The central engine is:

```bash
cd companion_code
python3 scripts/tnr_comprehensive_engine.py
```

This is not a black-box fit and not a neural net tuned to a table of values.
The principle is different: one and the same set of topological and geometric
invariants is carried through several floors and produces numerical readouts at
different physical scales.

At the moment the engine assembles:

- **L0** — fundamental constants and base readouts;
- **L1** — particle masses;
- **L2** — the nuclear layer;
- **L3** — molecular and chemical projections;
- **L4** — fundamental control readouts.

In practical terms, the code shows that:

- particle masses are not produced as a free fit, but from fixed geometric bases
  and carriers;
- the nuclear layer is built from the same framework rather than from a separate
  unrelated theory;
- the molecular and chemical layers appear as later projections of the same
  grammar;
- one and the same machine passes through different scales without changing its
  basic alphabet.

Current headline results:

- **L1**: 24 particle masses with errors on the order of `< 0.001%`;
- **L2**: 98 nuclear isotopes with errors on the order of `< 0.001%`;
- **L3**: 14 molecular bond energies with mean error around `0.32%`;
- **L4**: fundamental readouts with zero free parameters.

So the code layer is not present merely as an illustration. It is there to show
that one structural law can actually pass computationally through constants,
particles, nuclei, and chemistry.

For the code architecture and design principles, the right document is:

- [companion_code/README_code.md](companion_code/README_code.md)

### Lean 4

The Lean layer does not replace the Python engine. It serves a different role:
to check selected DOT results in a formal, executable proof setting rather than
only as numerical agreement.

If you want the fastest direct entry into the particle layer in Lean, there is
now one dedicated entry-point file:

- [docs/prefin/24_part_Lean!/ParticlePrototype.lean](docs/prefin/24_part_Lean!/ParticlePrototype.lean)

It does not claim to formalize “all of DOT in Lean.” It shows one concrete,
readable slice that matters immediately to an outside reader:

- the bare particle formula;
- the bare mass produced by that carrier;
- the current final `L1` package value;
- the error against the current reference dataset;
- and the reference value with uncertainty.

So this is the minimal visual entry where you can already see that:

- the system is not a black box;
- the bare layer and the final layer are explicitly separated;
- and the current numerical precision is visible directly in the output.

Key files:

- [companion_code/formal_proofs/DOT_Sn_Isotopes.lean](companion_code/formal_proofs/DOT_Sn_Isotopes.lean)
- [companion_code/formal_proofs/DOT_Particle_Spectrum.lean](companion_code/formal_proofs/DOT_Particle_Spectrum.lean)

So:

- Python shows the broad numerical passage of the machine across multiple
  layers;
- Lean shows that selected nodes of the same machine can already be translated
  into strict proof form.

## Where to start reading

If you are new to DOT, there is only one correct first entry point:

- [en/Theory_Core/DOT_foundations_and_machine_en.md](en/Theory_Core/DOT_foundations_and_machine_en.md)

This is the main starting text. It gives:

- the basic logic of distinction;
- the role of the octahedral machine;
- the separation of `structure / act / observation`;
- and the general framework without which later documents can look like strong
  but floating claims.

After that, the sensible order is:

1. [en/Machine/DOT_machine_architecture_overview_en.md](en/Machine/DOT_machine_architecture_overview_en.md)
2. [en/Theory_Science/en/DOT_physical_realization_en.md](en/Theory_Science/en/DOT_physical_realization_en.md)

That is:

- first the foundations;
- then the machine map;
- then the physical realization.

## How the text corpus is organized

The repository is divided into three main theory sections:

- `en/Theory_Core/`
- `en/Machine/`
- `en/Theory_Science/`

This matters because the documents inside them do not all have the same status.

### 1. Theory Core

This is the lower and middle theoretical backbone of DOT.

Key texts:

- [en/Theory_Core/DOT_foundations_and_machine_en.md](en/Theory_Core/DOT_foundations_and_machine_en.md)  
  the main foundational entry point;
- [en/Theory_Core/DOT_tnr_pure_structural_core_en.md](en/Theory_Core/DOT_tnr_pure_structural_core_en.md)  
  the cleaner early structural core;
- [en/Theory_Core/DOT_tnr_foundations_architectural_full_en.md](en/Theory_Core/DOT_tnr_foundations_architectural_full_en.md)  
  the full architectural unfolding;
- [en/Theory_Core/DOT_tnr_foundations_formal_appendix_en.md](en/Theory_Core/DOT_tnr_foundations_formal_appendix_en.md)  
  the formal supporting appendix.

If you want only one foundational text, start with:

- [en/Theory_Core/DOT_foundations_and_machine_en.md](en/Theory_Core/DOT_foundations_and_machine_en.md)

### 2. Machine

This section is about how the theory assembles into a machine.

Key texts:

- [en/Machine/DOT_machine_architecture_overview_en.md](en/Machine/DOT_machine_architecture_overview_en.md)
- [en/Machine/DOT_terminology_and_layer_map_en.md](en/Machine/DOT_terminology_and_layer_map_en.md)
- [en/Machine/DOT_octahedral_proof_calculus_en.md](en/Machine/DOT_octahedral_proof_calculus_en.md)
- [en/Machine/DOT_code_availability_en.md](en/Machine/DOT_code_availability_en.md)

This section is best read after the main foundational entry, once the lower
grammar of distinction is already clear.

## The scientific section

`en/Theory_Science/` is not one single document and not one single “physics
section.” It is the layer where DOT begins to project into mathematical,
physical, chemical, and later research corridors.

The simple distinction to keep in mind is this:

- some of these texts are **main volumes**;
- some are **strong companion documents**;
- some are **draft / research corridors**, important but not to be read as fully
  closed canon.

### Mathematical and operator entry

If you want the number-theory and operator layer first, the clean order is:

- [en/Theory_Science/en/DOT_mathematical_framework_en.md](en/Theory_Science/en/DOT_mathematical_framework_en.md)
- [en/Theory_Science/en/DOT_tnr_mathematical_operator_line_en.md](en/Theory_Science/en/DOT_tnr_mathematical_operator_line_en.md)

The first gives the larger mathematical framework.
The second gives a more compact line of operator nodes and transitions.

### Physical realization

The main physical volume is:

- [en/Theory_Science/en/DOT_physical_realization_en.md](en/Theory_Science/en/DOT_physical_realization_en.md)

This is the main science-level text if your interest is how the theoretical
machine projects into particles, nuclei, and matter-readouts.

### Late companion / research documents

These texts matter, but they are not the first entry point:

- [en/Theory_Science/en/DOT_tnr_multiplicative_additive_resonance_en.md](en/Theory_Science/en/DOT_tnr_multiplicative_additive_resonance_en.md)  
  a companion document on number resonance, prime roles, and the relation
  between additive and multiplicative readings;
- [en/Theory_Science/en/DOT_tnr_processual_boundary_draft_en.md](en/Theory_Science/en/DOT_tnr_processual_boundary_draft_en.md)  
  a draft on processual boundary, closure, tail, `2×2` logic, and the gravity
  corridor.

These are best read only after the foundations and the main physical layer.

### Chemical sub-corpus

Chemistry in DOT is already a distinct sub-corpus inside the scientific layer.

If you want to enter it, the best order is:

1. [en/Theory_Science/en/DOT_tnr_chemical_realization_canon_en.md](en/Theory_Science/en/DOT_tnr_chemical_realization_canon_en.md)
2. [en/Theory_Science/en/DOT_tnr_chemical_realization_appendix_en.md](en/Theory_Science/en/DOT_tnr_chemical_realization_appendix_en.md)
3. [en/Theory_Science/en/DOT_tnr_chemical_realization_topo_map_118_en.md](en/Theory_Science/en/DOT_tnr_chemical_realization_topo_map_118_en.md)
4. [en/Theory_Science/en/DOT_tnr_chemical_screening_family_audit_en.md](en/Theory_Science/en/DOT_tnr_chemical_screening_family_audit_en.md)
5. [en/Theory_Science/en/DOT_tnr_chemical_realization_canon_stabilization_map_en.md](en/Theory_Science/en/DOT_tnr_chemical_realization_canon_stabilization_map_en.md)

The important caution here is simple: the chemical canon is already strong as a
late-stage synthesis, but the appendix and audit layer are needed so that a
strong correspondence is not mistaken for a fully closed strict derivation.

## How the repository is currently structured

The current `_Agent/` structure looks like this:

```text
_Agent/
├── README.md
├── LICENSE
├── LICENSE-THEORY.md
├── ru/
│   ├── README_RU.md
│   ├── Theory_Core/
│   ├── Theory_Science/
│   └── Machine/
├── en/
│   ├── Theory_Core/
│   ├── Machine/
│   └── Theory_Science/
│       └── en/
├── companion_code/
│   ├── README.md
│   ├── README_code.md
│   ├── requirements.txt
│   ├── docs/
│   ├── scripts/
│   ├── formal_proofs/
│   ├── notes/
│   └── outputs/
└── Code/
    ├── tnr_comprehensive_engine.py
    ├── tnr_molecular_engine_v2.py
    ├── ...
```

Do not confuse the roles:

- `ru/` is the current Russian corpus;
- `en/` is the English corpus;
- `companion_code/` is the repo-ready code layer;
- `Code/` is the flat source snapshot of the current scripts.

The center of the code side is:

- [companion_code/README.md](companion_code/README.md)

## How to run the code

For the basic run you need Python 3 and `numpy`.

Minimal entry:

```bash
cd companion_code
pip install -r requirements.txt
python3 scripts/tnr_comprehensive_engine.py
```

That run assembles several layers at once:

- constants;
- particles;
- nuclei;
- the molecular layer;
- diagnostic readouts.

If you do not want the full aggregate run, useful entry points are:

```bash
python3 scripts/tnr_molecular_engine_v2.py
python3 scripts/tnr_l1_particle_readable_report.py
python3 scripts/tnr_l3_molecule_readable_report.py
python3 scripts/tnr_l4_element_readable_report.py
python3 scripts/tnr_same_shell_screening_extractor.py
python3 scripts/tnr_l4_same_shell_screening_extractor.py
python3 scripts/tnr_screening_family_audit.py
python3 scripts/tnr_l4_screening_family_audit.py
```

Lean is not required for ordinary Python runs. It is only needed for the formal
proof layer.

## What is already saved in outputs

`companion_code/outputs/` already contains not only aggregate reports but also
separate readable artifacts:

- [companion_code/outputs/engine_full_report.txt](companion_code/outputs/engine_full_report.txt)
- [companion_code/outputs/readable_reports/l1_particle_readable_report.txt](companion_code/outputs/readable_reports/l1_particle_readable_report.txt)
- [companion_code/outputs/readable_reports/l4_element_readable_report.txt](companion_code/outputs/readable_reports/l4_element_readable_report.txt)
- [companion_code/outputs/readable_reports/l4_element_example_U92.txt](companion_code/outputs/readable_reports/l4_element_example_U92.txt)
- [companion_code/outputs/readable_reports/README.md](companion_code/outputs/readable_reports/README.md)

So the code layer already provides not only machine outputs but also human-
readable entry points into the particle and chemical layers.

## Formal proofs

The Lean files live in:

- [companion_code/formal_proofs/](companion_code/formal_proofs/)

Key files:

- [companion_code/formal_proofs/DOT_Sn_Isotopes.lean](companion_code/formal_proofs/DOT_Sn_Isotopes.lean)
- [companion_code/formal_proofs/DOT_Particle_Spectrum.lean](companion_code/formal_proofs/DOT_Particle_Spectrum.lean)

Minimal run:

```bash
cd companion_code
lean --run formal_proofs/DOT_Sn_Isotopes.lean
```

## Main publication backbone

If you want the shortest publication backbone, read:

| # | Text | Focus |
|:-:|:-----|:------|
| **I** | [Foundations and Machine](en/Theory_Core/DOT_foundations_and_machine_en.md) | foundations, octahedral machine, basic carrier |
| **II** | [Mathematical Framework](en/Theory_Science/en/DOT_mathematical_framework_en.md) | numbers, spectral layer, modular and operator readings |
| **III** | [Physical Realization](en/Theory_Science/en/DOT_physical_realization_en.md) | particles, nuclei, chemistry layer, physical readouts |

Additional support texts:

| | Text | Focus |
|:-:|:-----|:------|
| **IV** | [Machine Architecture Overview](en/Machine/DOT_machine_architecture_overview_en.md) | full machine layer map |
| **V** | [Terminology and Layer Map](en/Machine/DOT_terminology_and_layer_map_en.md) | terminology and structural layer chart |
| **VI** | [Code Availability Statement](en/Machine/DOT_code_availability_en.md) | reproducibility and code layer |
| **VII** | [Formal Verification (Lean 4)](companion_code/formal_proofs/DOT_Sn_Isotopes.lean) | executable mathematical verification |

## Fundamental invariants

What follows is not “proof of the whole theory,” but the minimum set of support
constants that currently function as machine invariants in the corpus:

| Symbol | Value | Origin |
|:-------|:------|:-------|
| `γ = √6/9` | `0.27216553` | anisotropy of the Observer on carrier `K(2,2,2)` |
| `γ² = 2/27` | `0.07407407` | basic spectral / metric ratio |
| `α⁻¹` | `137.035999084…` | precision chiral structural law |
| `sin²θ_W = 2/9` | `0.22222` | lower electroweak readout |
| `Koide K₄ = 2/3` | `0.66667` | frozen lepton mass readout |
| `432 = j(i)/4` | `16 × 27` | universal modular pivot |

## Citation

```bibtex
@software{zhuk_2026_dot,
  author    = {Zhuk, Igor M.},
  title     = {Distinction Observable Theory (DOT): Foundations,
               Mathematical Framework, and Physical Realization},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.19236868},
  url       = {https://github.com/nondual-observer/distinction-observable-theory}
}
```

## Support the research

This project is being developed as **independent open research** without
institutional funding.

Donations are voluntary.

| Currency | Network | Address |
|----------|---------|---------|
| Bitcoin | BTC | `bc1qlaxsrum7fxpml57nsrtkjfkkxl5v3xtj4d0uxe` |
| USDT | TRC20 | `TM8U2EqVaT3tjvG6NyuKTqY4F5qc2A69Sy` |
| Ethereum | ETH | `0x4fFc68f0d55d19Fa5EBd5f6570a41E100aFe4a98` |

## License

**Code:** [Apache License 2.0](LICENSE)  
**Theory & Documentation:** [CC BY-NC-SA 4.0](LICENSE-THEORY.md)

---

*© 2026 Igor M. Zhuk. All rights reserved under the respective licenses.*
