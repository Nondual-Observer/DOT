# DOT Companion Code

This repository contains the **companion code layer** for the *Distinction Observable Theory (DOT)*.

The code is intended for **numerical reproducibility and diagnostics** of the topological parameters, demonstrating that the structural invariances (such as $\gamma = \sqrt{6}/9$) accurately reproduce empirical observation across multiple scales.

## 1. The Unified Comprehensive Engine (Python)

All previously scattered simulation scrips and legacy trackers have been consolidated into a single monolithic generator:

```bash
python3 scripts/tnr_comprehensive_engine.py
```

### What it calculates:
- **L4 (Constants):** Fine structure constant $\alpha$, Weinberg angle, Strong coupling $\alpha_s$, Rydberg constant.
- **L1 (Particles):** 24 particle masses (from electron to Top quark and Higgs boson) calculated using exact geometric bases (e.g., $136/\gamma^2$, $72/\gamma$).
- **L2 (Nuclei):** 98 stable isotopes matched against AME2020 mass defect data using the DOT-SEMF and Ramanujan $\tau(n)$ spectrum.
- **L3 (Molecules):** 14 fundamental molecular bond energies perfectly derived from the $Ry/3$ base.

You can view the full autonomous execution log without running the code by checking `outputs/engine_full_report.txt`.

## 2. Formal Proofs (Lean 4)

We have begun the process of formally verifying the physical derivations using the **Lean 4 interactive theorem prover**. 

- `formal_proofs/DOT_Sn_Isotopes.lean`
  - A mathematically rigorous, executable proof demonstrating that the 10 stable isotopes of Tin (Sn, Z=50) conform identically to the DOT-SEMF mass formula (derived solely from the pion mass $M_{\pi}$, $\alpha$, and $\gamma$) with $<0.2\%$ error margin.

To execute the proof in Lean 4:
```bash
lean --run formal_proofs/DOT_Sn_Isotopes.lean
```

## License

- **Code:** [Apache License 2.0](../LICENSE)
- **Theory and documentation:** [CC BY-NC-SA 4.0](../LICENSE-THEORY.md)
