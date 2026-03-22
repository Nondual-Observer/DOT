# Distinction Observable Theory: Code Availability

**Status:** editorial reproducibility note  
**Date:** March 22, 2026  
**Purpose:** to state which companion scripts exist for checking the numerical results of DOT and what status they have relative to the main manuscript.

---

This manuscript bundle is accompanied by a code layer. Its purpose is **numerical reproducibility**, not the replacement of formal derivation blocks.

The code currently covers three task classes:

1. **Verification of microphysical tables**
   - bare-address calculations;
   - tail evaluations;
   - particle and constant audit tables.

2. **Verification of selected macroscopic calculations**
   - arithmetic shell factors;
   - gravity-bridge numerics;
   - horizon-fraction checks.

3. **Exploratory DOT chemistry**
   - atomic and hydride readout models;
   - bond-domain / lone-pair / aperture logic;
   - a bounded multi-center branch for $C_2H_n$ hydrocarbons (explicit $C\!-\!C$ $\sigma/\pi$ split and a hybridization readout driven only by the octahedral invariants $2/3$ and $\gamma^2$);
   - reproducibility checks for a limited molecular class.

It is important to distinguish:

- the **main manuscript** — formal derivations whose status is explicitly marked as `[D] / [G1] / [G2]`;
- the **companion code** — tools for reproducing numerical consequences and exploratory models.

Accordingly:

- numerical agreement in code does **not** replace strict proof;
- but it is an important element of **reproducibility**;
- and it allows separate testing of the stability of DOT readouts on new inputs.

For a publishable version, the manuscript should be accompanied by:

- either a public repository with a frozen tag/snapshot;
- or an archival snapshot (for example, via Zenodo);
- or a project page with a fixed public script version.

The code should not be embedded into the main articles as long listings. It is sufficient to provide:

- a short link to the code archive;
- a note on which scripts reproduce which tables/chapters;
- and a clear separation between formal derivation and numerical verification.

In the current corpus, the companion scripts should be understood exactly in this sense:  
**as a reproducibility, validation, and extension layer, but not as an independent source of axioms.**

---

*Companion code note for the DOT draft manuscript*  
*March 22, 2026*

## Numerical Snapshot (Chemistry, Draft)

This is a **verification** snapshot for the hydride and bounded multi-center chemistry branches. This is **draft**-level: the model does not claim universality across chemistry; once multi-center phase-selection logic is closed, accuracy may plausibly improve further.

**Script:** `scripts/tnr_hydrogen_dynamic_v10.py`  
**Internal constants used by the model:**

- $\gamma = \sqrt{6}/9 \approx 0.27216553$, $\gamma^2 = 2/27 \approx 0.07407407$
- $\alpha^{-1} \approx 137.036101$
- $Ry \approx 13.605673$ eV, $E_{\text{bond}} = Ry/3 \approx 4.535224$ eV

The script also prints an **internal decomposition** for each case (for example, $E_{\text{radial}}$, $E_{\text{ortho}}$, period/aperture factors for hydrides; and $E_{CH}$ and $E_{CC,\sigma/\pi}$ for $C_2H_n$), so one can validate not only final energies but also the model’s “internal channels”.

**Accuracy (current benchmark set):**

- Mean $|\%|$ error (resolved) $\approx 0.34\%$.
- $H_2$ (exact branch) $\approx 0.03\%$.
- Multi-center $C_2H_n$ (bounded branch): $C_2H_6 \approx 0.36\%$, $C_2H_4 \approx 0.03\%$.
- `candidate-s-block` (e.g. LiH) is explicitly marked as **not closed** and is not counted as “resolved”.

| Molecule | Mode | DOT (eV) | Ref (eV) | Err% |
|---|---|---:|---:|---:|
| $H_2$ | exact-h2 | 4.4792 | 4.4780 | +0.03 |
| LiH | candidate-s-block | 2.5196 | 2.5150 | +0.18 |
| HF | bond-domain | 5.8308 | 5.8700 | -0.67 |
| $H_2O$ | bond-domain | 9.5744 | 9.5100 | +0.68 |
| $NH_3$ | bond-domain | 11.9260 | 11.9500 | -0.20 |
| $CH_4$ | bond-domain | 17.0045 | 17.0200 | -0.09 |
| $SiH_4$ | bond-domain | 13.0638 | 13.0700 | -0.05 |
| $PH_3$ | bond-domain | 9.9145 | 10.0000 | -0.86 |
| $H_2S$ | bond-domain | 7.5260 | 7.5700 | -0.58 |
| HCl | bond-domain | 4.4134 | 4.4300 | -0.38 |
| HBr | bond-domain | 3.7573 | 3.7600 | -0.07 |
| HI | bond-domain | 3.0717 | 3.0600 | +0.38 |
| $C_2H_6$ | multi-center-2c | 29.7060 | 29.6000 | +0.36 |
| $C_2H_4$ | multi-center-2c | 24.6918 | 24.7000 | -0.03 |

## Single Entrypoint (Companion Dashboard)

To avoid scattering many scripts across the text, the companion code includes a **single entrypoint** that orchestrates the checks:

- `scripts/dot_companion_verify.py --chem` (exploratory chemistry, v10)
- `scripts/dot_companion_verify.py --full` (legacy unified verification dashboard)
- `scripts/dot_companion_verify.py --tails` (legacy tail calculator)
- `scripts/dot_companion_verify.py --vacuum64` (legacy 64-state engine)
- `scripts/dot_companion_verify.py --all` (runs the full set in order)
- `scripts/dot_companion_verify.py --hydrogen-dyn` (legacy hydrogen dynamics: state evolution with excited/ground populations, entropy, channel-load diagnostics)

Note: the `legacy:*` branches are kept as a snapshot/dashboard (they mix exact identities, baseline predictions, and candidate layers). They are useful for reproducibility and diagnostics, but they do not replace `[D]/[G1]/[G2]` status claims in the main corpus.
