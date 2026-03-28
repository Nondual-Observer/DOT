# Appendix
## Chemical Realization: Data, Mapping, Error Metrics

**Main text:** [DOT_tnr_chemical_realization_canon_en.md](/Users/abc/Codex_n111/_Agent/en/Theory_Science/en/DOT_tnr_chemical_realization_canon_en.md)  
**Function of this appendix:** to provide the computational and tabular support for those chemical-layer claims that already have an executable artifact, and separately to show what still remains only a strong reading rather than a closed derivation.

---

## 1. Current Status of the Appendix

At the current stage of this appendix, the corpus already contains **two different classes of support**, and they should not be mixed.

### 1.1. What is already confirmed by executable artifacts

Only those layers for which a separate script or registry-layer has been found should be treated as confirmed:

- full `TOPO_MAP` for `Z = 1..118`;
- anchor `E_BOND = Ry/3`;
- global and block-wise error metrics for first ionization energies;
- node usage and prime cross-reference;
- split of strong and weak periodic exceptions;
- exact match for `strong canonical transfer` and `weak residual transfer`.

### 1.2. What still remains a pending layer

No separate standalone extraction script for `ΔS_same` was found in the current registry search.

This means:

- the screening table from the main chemical canon may be retained as a strong working table;
- but it cannot yet be presented as the same kind of executable layer as `TOPO_MAP` or the global metrics from `periodic_table_generator.py`.

One more point matters here: in the screening table of the main canon there had been an internal inconsistency in the `5f` row; the expression `1 - γ²/2` and the stated error correspond to `26/27`, not to `53/54`. This has already been corrected in the main text.

---

## 2. Data Sources and Artifacts

### 2.1. Main executable registry

At present, the chemical canon has one main numerical source:

- `/Users/abc/Codex_n111/tnr_final_synthesis/publishing/chemistry/periodic_table_generator.py`

It is this script that defines:

- `E_BOND = Ry / 3`;
- the full `TOPO_MAP`;
- the reference IE set for `1..118`;
- global / block / period statistics;
- node usage;
- prime cross-reference.

### 2.2. Solver-side scaffolds

Additional verifiable artifacts:

- `/Users/abc/Codex_n111/tnr_final_synthesis/scripts/tnr_periodic_canonical_transfer.py`
- `/Users/abc/Codex_n111/tnr_final_synthesis/scripts/tnr_periodic_residual_transfer.py`
- `/Users/abc/Codex_n111/tnr_final_synthesis/scripts/tnr_periodic_exception_split.py`

They do not build the full chemical registry, but they do close an important solver-layer:

- `strong canonical transfer` — `7/7`;
- `weak residual transfer` — `4/4`;
- split of strong and weak exceptions.

### 2.3. Molecular anchor-layer

For the bridge-layer of chemistry, this artifact is separately important:

- `/Users/abc/Codex_n8n/docs/prefin/companion_code/scripts/tnr_molecular_engine_v2.py`

It confirms that `E_BOND` already works as a universal anchor on the molecular layer and that ionic fraction-laws such as `13/10`, `12/11`, `15/16`, `23/24` have their own executable status.

### 2.4. What should not be mixed in here

Scripts such as:

- `/Users/abc/Codex_n111/tnr_final_synthesis/scripts/tnr_lattice_atom_solver.py`
- `/Users/abc/Codex_n111/tnr_final_synthesis/scripts/tnr_atomic_test_all.py`

are **different atomic models**. They are useful in their own right, but they should not be used as though they were the same registry-layer as `periodic_table_generator.py`.

---

## 3. TOPO_MAP

### 3.1. Anchor

The main anchor of the chemical registry:

\[
E_{bond} = \frac{Ry}{3}
\]

In the current executable generator:

- `Ry = 13.59844 eV`
- `E_BOND = 4.532813333... eV`

### 3.2. Small alphabet of coarse nodes

The current generator uses only **10 numerators**:

\[
\{3, 9, 11, 13, 15, 16, 23, 38, 55, 67\}.
\]

This no longer looks like accidental fitting. It is a genuinely small coarse-node vocabulary.

| Node `N` | Node name | Factorization | Occurrences | Structural type |
|---:|---|---|---:|---|
| `3` | Triad (γ-base) | `3` | `4` | prime-node |
| `9` | Oxygen Bridge | `3²` | `2` | power-node |
| `11` | Boron Bridge | `11` | `8` | prime-node |
| `13` | Lithium Edge | `13` | `5` | prime-node |
| `15` | Carbon Dual | `3·5` | `6` | bridge-composite |
| `16` | Nitrogen Core | `2⁴` | `13` | power-node |
| `23` | Halogen Edge | `23` | `15` | prime-node |
| `38` | Closed Shell | `2·19` | `16` | bridge-composite |
| `55` | Deep Boundary | `5·11` | `11` | bridge-composite |
| `67` | Li-carrier (67/56) | `67` | `38` | prime-node |

### 3.3. On the provenance of pairs `(N, D)`

The current generator stores an already completed registry map:

```python
TOPO_MAP = { Z: (N, D), ... }
```

But it does not yet store the provenance field for each pair explicitly:

- `derived`
- `selected`
- `bridge-derived`
- `open`

Therefore, at the current version of this appendix, the following can be honestly claimed:

- the full executable registry exists;
- its numerical properties are computed;
- but row-wise provenance has not yet been separated into its own artifact.

### 3.4. Where the full catalog currently lives

The full 118-row catalog `Z -> (N, D)` currently exists in three related forms:

- executable source of truth:
  - `/Users/abc/Codex_n111/tnr_final_synthesis/publishing/chemistry/periodic_table_generator.py`
- mirrored registry export:
  - [DOT_tnr_chemical_realization_topo_map_118_en.md](/Users/abc/Codex_n111/_Agent/en/Theory_Science/en/DOT_tnr_chemical_realization_topo_map_118_en.md)
- mirrored Russian registry export:
  - [DOT_tnr_chemical_realization_topo_map_118_ru.md](/Users/abc/Codex_n111/_Agent/en/Theory_Science/DOT_tnr_chemical_realization_topo_map_118_ru.md)

This distinction is principled:

- the script remains the **source of truth** for the entire registry;
- the markdown export is needed as a readable documentary slice;
- the appendix itself does not duplicate all 118 rows, but aggregates their main computable properties:
  - vocabulary;
  - global metrics;
  - block / period metrics;
  - outliers;
  - noble-gas closure line;
  - prime occurrence table.

---

## 4. Error Metrics

### 4.1. Formulae

\[
IE_{DOT}(Z)=\frac{N}{D}E_{bond}
\]

\[
\varepsilon_{abs}(Z)=\frac{|IE_{DOT}(Z)-IE_{exp}(Z)|}{IE_{exp}(Z)}\cdot 100\%
\]

\[
\varepsilon_{signed}(Z)=\frac{IE_{DOT}(Z)-IE_{exp}(Z)}{IE_{exp}(Z)}\cdot 100\%
\]

### 4.2. Global metrics

Below are the **current executable values** from `periodic_table_generator.py`:

| Metric | Value |
|---|---:|
| Mean absolute error (MAE) | `0.312799%` |
| Median absolute error | `0.210848%` |
| Max absolute error | `1.204134%` |
| Mean signed error | `-0.064762%` |
| RMS signed error | `0.425539%` |
| Elements `< 1%` | `114 / 118` |
| Elements `< 0.5%` | `93 / 118` |
| Elements `< 0.1%` | `34 / 118` |

### 4.3. Block-wise metrics

| Block | Count | MAE | Mean signed error | Worst case | Worst abs err |
|---|---:|---:|---:|---|---:|
| `s` | `14` | `0.272440%` | `-0.094955%` | `Be (Z=4)` | `0.959899%` |
| `p` | `36` | `0.348294%` | `-0.082439%` | `Ts (Z=117)` | `1.131699%` |
| `d` | `40` | `0.344194%` | `-0.073637%` | `Rg (Z=111)` | `1.204134%` |
| `f` | `28` | `0.242491%` | `-0.014259%` | `Cf (Z=98)` | `0.717159%` |

### 4.4. Period-wise metrics

| Period | Count | MAE | Mean signed error | Worst case | Worst abs err |
|---:|---:|---:|---:|---|---:|
| `1` | `2` | `0.041682%` | `+0.041682%` | `He` | `0.080128%` |
| `2` | `8` | `0.268883%` | `-0.232254%` | `Be` | `0.959899%` |
| `3` | `8` | `0.343974%` | `-0.156493%` | `Mg` | `0.700205%` |
| `4` | `18` | `0.476990%` | `-0.221831%` | `Kr` | `1.069550%` |
| `5` | `18` | `0.263049%` | `-0.078978%` | `Cd` | `0.685917%` |
| `6` | `32` | `0.201437%` | `-0.084334%` | `At` | `0.906754%` |
| `7` | `32` | `0.379917%` | `+0.109312%` | `Rg` | `1.204134%` |

### 4.5. Worst outliers

| Rank | Z | Element | Subshell | `N/D` | abs err % | signed err % |
|---:|---:|---|---|---|---:|---:|
| `1` | `111` | `Rg` | `6d` | `67/29` | `1.204134%` | `-1.204134%` |
| `2` | `107` | `Bh` | `6d` | `67/39` | `1.131699%` | `+1.131699%` |
| `3` | `117` | `Ts` | `7p` | `67/39` | `1.131699%` | `+1.131699%` |
| `4` | `36` | `Kr` | `4p` | `55/18` | `1.069550%` | `-1.069550%` |
| `5` | `4` | `Be` | `2s` | `55/27` | `0.959899%` | `-0.959899%` |
| `6` | `26` | `Fe` | `3d` | `38/22` | `0.918693%` | `-0.918693%` |
| `7` | `85` | `At` | `6p` | `55/27` | `0.906754%` | `-0.906754%` |
| `8` | `30` | `Zn` | `3d` | `23/11` | `0.891001%` | `+0.891001%` |
| `9` | `32` | `Ge` | `4p` | `38/22` | `0.881063%` | `-0.881063%` |
| `10` | `29` | `Cu` | `3d` | `67/39` | `0.791365%` | `+0.791365%` |
| `11` | `116` | `Lv` | `7p` | `67/43` | `0.752577%` | `+0.752577%` |
| `12` | `31` | `Ga` | `4p` | `67/51` | `0.735582%` | `-0.735582%` |

---

## 5. Screening Layer

### 5.1. Current honest status

At present, the repo contains **three different support levels** for the screening layer:

- `/Users/abc/Codex_n8n/docs/prefin/companion_code/scripts/tnr_comprehensive_engine.py`
  explicitly encodes the continuous `γ²` screening law for L4 and prints the target line
  `f -> 80/81`, `d -> 1-γ²/2`, `s -> 2/3`;
- `/Users/abc/Codex_n8n/docs/prefin/companion_code/scripts/tnr_same_shell_screening_extractor.py`
  performs a standalone reverse extraction of representative `ΔS_same` directly from the
  same IE dataset for the closure families `1s`, `3d`, `4f`, `5f`;
- the main chemical canon already contains a compiled comparison table for `ΔS_same`.

Therefore, at this version of the appendix, screening should be fixed in separated form:

- the representative same-shell table `1s / 3d / 4f / 5f` as an **executable extraction layer**;
- the continuous `γ²` law over the entire chemistry layer as a **strong law-readout**,
  because its reverse block-wide extraction has not yet been separated into a generalized artifact.

### 5.2. Current working table of screening targets

| Block / family | `ΔS_same (exp)` | DOT target | DOT expression | abs diff | Status |
|---|---:|---:|---|---:|---|
| `4f` (lanthanides, full-fill) | `0.9884` | `80/81` | `1 - γ²/3` | `0.0007` | extracted |
| `5f` (actinides, full-fill) | `0.9682` | `26/27` | `1 - γ²/2` | `0.0052` | extracted |
| `3d` (metals, full-fill) | `0.9545` | `26/27` | `1 - γ²/2` | `0.0085` | extracted |
| `1s` (primordial s-limit) | `0.6553` | `2/3` | `2/3` | `0.0113` | extracted |

### 5.3. Generalized family audit

The separate audit script:

- `/Users/abc/Codex_n8n/docs/prefin/companion_code/scripts/tnr_screening_family_audit.py`

does not merely reproduce the representative families, but also computes closure values
for all available `s / p / d / f` subshells.

The main conclusion of that generalized audit:

- **not** the entire block is held by the same coefficient;
- what is held are precisely the **representative locked families**;
- later periods show **period-depth drift** relative to the small screening vocabulary.

At the current executable level, this reads as follows:

- `s` family:
  - `1s -> 0.6553 ~ 2/3`
  - then closure drifts monotonically downward (`2s -> 0.6034`, `7s -> 0.4700`)
  - therefore `2/3` is the **primordial s-limit**, not a universal constant of all `s` families;
- `d` family:
  - `3d` and `4d` remain close to `26/27`,
  - `5d` and especially `6d` drift noticeably away;
- `f` family:
  - `4f` locks near `80/81`,
  - `5f` locks near `26/27`;
- `p` family:
  - under the current audit it shows no clean lock to the small vocabulary
    `2/3`, `26/27`, `80/81`.

Therefore the generalized audit strengthens the canon not with the formula
"every block = one coefficient," but with the more precise law:

> the small `γ²` vocabulary defines representative closure-nodes,  
> and the later families are read as their period-depth continuations with drift.

---

## 6. Macro-Primes

### 6.1. What the generator actually shows

The executable generator yields not only the three numbers `{19, 23, 67}`, but a broader chemistry-only set:

\[
\{19, 23, 29, 31, 41, 43, 47, 59, 67\}.
\]

The set shared with the particle layer:

\[
\{2, 3, 5, 7, 11, 13, 17\}.
\]

### 6.2. Occurrence table

| Prime | In numerators `N` | In denominators `D` | Total occurrences | Current role reading |
|---:|---:|---:|---:|---|
| `19` | `16` | `2` | `18` | closure-linked macro-prime through node `38 = 2·19` |
| `23` | `15` | `0` | `15` | boundary / halogen edge node |
| `67` | `38` | `0` | `38` | dominant macro-carrier node |

### 6.2.a. Full prime occurrence cross-reference

| Prime | In `N` | In `D` | Total |
|---:|---:|---:|---:|
| `2` | `29` | `60` | `89` |
| `3` | `12` | `33` | `45` |
| `5` | `17` | `24` | `41` |
| `7` | `0` | `15` | `15` |
| `11` | `19` | `10` | `29` |
| `13` | `5` | `11` | `16` |
| `17` | `0` | `12` | `12` |
| `19` | `16` | `2` | `18` |
| `23` | `15` | `0` | `15` |
| `29` | `0` | `5` | `5` |
| `31` | `0` | `1` | `1` |
| `41` | `0` | `1` | `1` |
| `43` | `0` | `2` | `2` |
| `47` | `0` | `1` | `1` |
| `59` | `0` | `1` | `1` |
| `67` | `38` | `0` | `38` |

### 6.3. Noble-gas line and its limit

| Element | `N/D` | Note |
|---|---|---|
| `He` | `38/7` | direct node `38` |
| `Ne` | `38/8` | direct node `38` |
| `Ar` | `38/11` | direct node `38` |
| `Kr` | `55/18` | closure line continues, but no longer via `38` |
| `Xe` | `67/25` | closure line continues, but via `67` |
| `Rn` | `38/16` | return to `38` |

---

## 7. Solver-Side Verified Layers

### 7.1. Strong canonical transfer

The script:

- `/Users/abc/Codex_n111/tnr_final_synthesis/scripts/tnr_periodic_canonical_transfer.py`

yields the exact result:

- `7 / 7` exact matches

for the cases:

- `Cr`
- `Cu`
- `Mo`
- `Pd`
- `Ag`
- `Au`
- `Gd`

### 7.2. Weak residual transfer

The script:

- `/Users/abc/Codex_n111/tnr_final_synthesis/scripts/tnr_periodic_residual_transfer.py`

yields:

- `4 / 4` exact matches

for:

- `Nb`
- `Ru`
- `Rh`
- `Pt`

### 7.3. Exception split

The script:

- `/Users/abc/Codex_n111/tnr_final_synthesis/scripts/tnr_periodic_exception_split.py`

separates:

- strong half/full-transfer exceptions;
- weak residual-transfer exceptions.

---

## 8. Claim Status Map

| Claim | Current status | Why |
|---|---|---|
| `E_BOND = Ry/3` as chemical anchor | `[D]` artifact-level | explicitly fixed in the generator and the molecular engine |
| Full `TOPO_MAP` for `1..118` exists | `[D]` artifact-level | the full registry map is present in `periodic_table_generator.py` |
| Mean error `~0.31%` | `[D]` artifact-level | current executable value `0.312799%` |
| Small numerator vocabulary of size `10` | `[D]` artifact-level | read directly from the generator |
| Shared prime alphabet with the particle layer | `[G1]` strong structural reading | the cross-reference is computable, but the interpretation is still structural |
| Macro-primes `{19,23,67}` are privileged | `[G1]` | the generator strongly supports them, but the chemistry-only set is broader |
| Canonical transfer group (`7/7`) | `[D]` artifact-level | separate exact-match script |
| Residual transfer group (`4/4`) | `[D]` artifact-level | separate exact-match script |
| Representative `ΔS_same` extraction (`1s/3d/4f/5f`) | `[D]` artifact-level | standalone extractor reproduces the screening-table values from the same IE dataset |
| Generalized family screening audit | `[D]` artifact-level | all subshell closure trajectories are reproducibly computed and show where lock vs drift occurs |
| Screening law around `γ²` | `[G1]` strong law-readout | the continuous law is encoded in `tnr_comprehensive_engine.py`; generalized block-wide reverse extraction remains a higher-layer task |
| Every pair `(N,D)` already has row-wise provenance | `[G2]` open | the current registry stores the final map, not provenance annotations |

---

## 9. Reproducibility Block

### 9.1. Environment

- `Python 3.9.13`

### 9.2. Artifacts

| Artifact | File / script | Role |
|---|---|---|
| Full chemical registry | `/Users/abc/Codex_n111/tnr_final_synthesis/publishing/chemistry/periodic_table_generator.py` | `TOPO_MAP`, `IE_exp`, metrics, node usage, prime cross-reference |
| Continuous L4 screening law | `/Users/abc/Codex_n8n/docs/prefin/companion_code/scripts/tnr_comprehensive_engine.py` | encodes `γ²` screening targets for `f/d/s` blocks |
| Same-shell screening extractor | `/Users/abc/Codex_n8n/docs/prefin/companion_code/scripts/tnr_same_shell_screening_extractor.py` | reverse-extracts representative `ΔS_same` values from the same IE dataset |
| Family screening audit | `/Users/abc/Codex_n8n/docs/prefin/companion_code/scripts/tnr_screening_family_audit.py` | computes closure trajectories for all `s/p/d/f` subshell families |
| Strong canonical transfer | `/Users/abc/Codex_n111/tnr_final_synthesis/scripts/tnr_periodic_canonical_transfer.py` | verifies `7/7` strong exceptions |
| Weak residual transfer | `/Users/abc/Codex_n111/tnr_final_synthesis/scripts/tnr_periodic_residual_transfer.py` | verifies `4/4` weak exceptions |
| Exception split | `/Users/abc/Codex_n111/tnr_final_synthesis/scripts/tnr_periodic_exception_split.py` | separates strong vs weak branch |
| Molecular bridge anchor | `/Users/abc/Codex_n8n/docs/prefin/companion_code/scripts/tnr_molecular_engine_v2.py` | confirms `E_BOND` and ionic rational family |
| Separate atomic model | `/Users/abc/Codex_n111/tnr_final_synthesis/scripts/tnr_lattice_atom_solver.py` | independent atomic/Slater experiment, not the same registry |
| Hydrogen-like testbed | `/Users/abc/Codex_n111/tnr_final_synthesis/scripts/tnr_atomic_test_all.py` | separate single-electron testbed |
