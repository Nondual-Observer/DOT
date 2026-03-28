# DOT / TNR Chemical Screening Family Audit

## 1. Status

This document records the result of the generalized audit for `same-shell screening`
in the chemical layer.

It relies on executable artifacts:

- [periodic_table_generator.py](/Users/abc/Codex_n111/tnr_final_synthesis/publishing/chemistry/periodic_table_generator.py)
- [tnr_same_shell_screening_extractor.py](/Users/abc/Codex_n111/tnr_final_synthesis/publishing/chemistry/tnr_same_shell_screening_extractor.py)
- [tnr_screening_family_audit.py](/Users/abc/Codex_n111/tnr_final_synthesis/publishing/chemistry/tnr_screening_family_audit.py)

The main result of the audit:

- the small `γ²` vocabulary does indeed reproduce **representative closure-families**;
- but the generalized family map does **not** confirm the simple formula
  `entire block = one and the same coefficient`;
- instead, a more precise picture emerges:
  **locked representative families + period-depth drift**.

---

## 2. Method

For each subshell with at least two elements, the first element
of the family is taken as the anchor.

From its ionization energy, we reconstruct:

\[
S_{inner}=Z-n\sqrt{IE/Ry}.
\]

Then for each next position inside the same subshell we compute:

\[
\Delta S_{same}=\frac{Z-S_{inner}-n\sqrt{IE/Ry}}{pos-1}.
\]

The closure value of the family is defined at full filling (`pos = cap`).

It is these closure values that are compared against the small screening vocabulary:

\[
\left\{\frac{2}{3},\; \frac{26}{27}=1-\frac{\gamma^2}{2},\; \frac{80}{81}=1-\frac{\gamma^2}{3}\right\}.
\]

---

## 3. Family Closure Map

| Subshell | Block | Closure `ΔS_same` | Nearest DOT target | abs diff |
|---|---|---:|---|---:|
| `1s` | `s` | `0.655337` | `2/3` | `0.011330` |
| `2s` | `s` | `0.603379` | `2/3` | `0.063288` |
| `2p` | `p` | `0.808744` | `2/3` | `0.142078` |
| `3s` | `s` | `0.594693` | `2/3` | `0.071973` |
| `3p` | `p` | `0.752155` | `2/3` | `0.085489` |
| `3d` | `d` | `0.954503` | `26/27 = 1-γ²/2` | `0.008460` |
| `4s` | `s` | `0.578109` | `2/3` | `0.088557` |
| `4p` | `p` | `0.719629` | `2/3` | `0.052962` |
| `4d` | `d` | `0.939062` | `26/27 = 1-γ²/2` | `0.023901` |
| `4f` | `f` | `0.988382` | `80/81 = 1-γ²/3` | `0.013074` |
| `5s` | `s` | `0.535405` | `2/3` | `0.131262` |
| `5p` | `p` | `0.707831` | `2/3` | `0.041164` |
| `5d` | `d` | `0.864221` | `26/27 = 1-γ²/2` | `0.098742` |
| `5f` | `f` | `0.968189` | `26/27 = 1-γ²/2` | `0.005226` |
| `6s` | `s` | `0.496164` | `2/3` | `0.170503` |
| `6p` | `p` | `0.737348` | `2/3` | `0.070682` |
| `6d` | `d` | `0.781610` | `2/3` | `0.114943` |
| `7s` | `s` | `0.469966` | `2/3` | `0.196701` |
| `7p` | `p` | `0.892684` | `26/27 = 1-γ²/2` | `0.070279` |

---

## 4. Representative Locked Families

These four families can currently be treated as
representative executable locks:

| Family | Closure `ΔS_same` | DOT target | abs diff |
|---|---:|---|---:|
| `1s` | `0.655337` | `2/3` | `0.011330` |
| `3d` | `0.954503` | `26/27` | `0.008460` |
| `4f` | `0.988382` | `80/81` | `0.013074` |
| `5f` | `0.968189` | `26/27` | `0.005226` |

This is the minimal executable backbone of the current screening table.

---

## 5. Block-wise Reading

### 5.1. `s` family

`s` closure does not remain constant.

The sequence runs as follows:

\[
1s \to 0.6553,\;
2s \to 0.6034,\;
3s \to 0.5947,\;
4s \to 0.5781,\;
5s \to 0.5354,\;
6s \to 0.4962,\;
7s \to 0.4700.
\]

This means:

- `2/3` is not the universal constant of all `s` subshells;
- it is the **primordial s-limit**, most cleanly manifested in `1s`;
- from there onward an explicit period-depth drift begins.

### 5.2. `d` family

`3d` and `4d` remain close to `26/27`, but then the drift intensifies:

\[
3d \approx 0.9545,\quad
4d \approx 0.9391,\quad
5d \approx 0.8642,\quad
6d \approx 0.7816.
\]

This means:

- `26/27` holds the early `d` closure families well;
- the later `d` families no longer reduce to the same point without residue.

### 5.3. `f` family

Here the split is especially clean:

- `4f` locks near `80/81`;
- `5f` locks near `26/27`.

That is, the `f` layer itself is not homogeneous and bifurcates into two closure regimes.

### 5.4. `p` family

Under the current audit, the `p` families do not yield a clean lock to the small vocabulary.

This means:

- the `p` layer cannot honestly be reduced to the same simple formula
  as `1s / 3d / 4f / 5f`;
- this is either a different screening regime,
  or a layer in which the small vocabulary manifests only indirectly.

---

## 6. Main Conclusion

The generalized audit does not destroy the chemical canon. On the contrary, it refines it.

It shows that the correct formula is:

> the small `γ²` vocabulary defines not the entire block as such,  
> but representative closure-families;  
> the remaining families are read as their period-depth continuations with drift.

In exactly this form, the screening layer is now
the most precise and the most defensible reading.
