# Appendix
## Chemical Realization: Data, Mapping, Error Metrics

**Основной текст:** [DOT_tnr_chemical_realization_canon_ru.md](/Users/abc/Codex_n8n/docs/prefin/ru/DOT_tnr_chemical_realization_canon_ru.md)  
**Функция приложения:** дать вычислительную и табличную опору для тех claim'ов chemical-layer, которые уже имеют executable artifact, и отдельно показать, что ещё остаётся только сильным reading, а не закрытым выводом.

---

## 1. Текущий статус приложения

На момент этой версии приложения в корпусе уже есть **два разных класса опоры**, и их нельзя смешивать.

### 1.1. Что уже подтверждается executable-артефактами

Подтверждаемыми считаются только те слои, для которых найден отдельный скрипт или registry-слой:

- полный `TOPO_MAP` на `Z = 1..118`;
- anchor `E_BOND = Ry/3`;
- глобальные и block-wise метрики ошибки для first ionization energies;
- node-usage и prime cross-reference;
- split сильных и слабых periodic exceptions;
- exact match для `strong canonical transfer` и `weak residual transfer`.

### 1.2. Что пока остаётся pending-layer

Отдельного standalone extraction-script для `ΔS_same` в текущем registry-поиске найдено не было.

Это значит:

- screening-table из основного chemical canon можно держать как сильную рабочую таблицу;
- но её нельзя пока выдавать за такой же executable-layer, как `TOPO_MAP` или global metrics из `periodic_table_generator.py`.

Отдельно важно: в screening-table основного canon была внутренняя несогласованность в строке `5f`; выражение `1 - γ²/2` и указанная ошибка соответствуют `26/27`, а не `53/54`. В основном тексте это уже исправлено.

---

## 2. Источники данных и артефакты

### 2.1. Главный executable registry

Основной численный источник chemical canon сейчас один:

- `/Users/abc/Codex_n111/tnr_final_synthesis/publishing/chemistry/periodic_table_generator.py`

Именно он задаёт:

- `E_BOND = Ry / 3`;
- полный `TOPO_MAP`;
- reference IE-set для `1..118`;
- global / block / period statistics;
- node-usage;
- prime cross-reference.

### 2.2. Solver-side scaffolds

Дополнительные проверяемые артефакты:

- `/Users/abc/Codex_n111/tnr_final_synthesis/scripts/tnr_periodic_canonical_transfer.py`
- `/Users/abc/Codex_n111/tnr_final_synthesis/scripts/tnr_periodic_residual_transfer.py`
- `/Users/abc/Codex_n111/tnr_final_synthesis/scripts/tnr_periodic_exception_split.py`

Они не строят весь chemical registry, но закрывают важный solver-layer:

- `strong canonical transfer` — `7/7`;
- `weak residual transfer` — `4/4`;
- split сильных и слабых исключений.

### 2.3. Молекулярный anchor-layer

Для bridge-layer chemistry отдельно важен:

- `/Users/abc/Codex_n8n/docs/prefin/companion_code/scripts/tnr_molecular_engine_v2.py`

Он подтверждает, что `E_BOND` уже работает как универсальный anchor на molecular-layer и что ионные fraction-laws типа `13/10`, `12/11`, `15/16`, `23/24` имеют собственный executable status.

### 2.4. Что сюда не смешивается

Скрипты типа:

- `/Users/abc/Codex_n111/tnr_final_synthesis/scripts/tnr_lattice_atom_solver.py`
- `/Users/abc/Codex_n111/tnr_final_synthesis/scripts/tnr_atomic_test_all.py`

являются **другими атомными моделями**. Они полезны сами по себе, но не должны использоваться как будто это и есть тот же registry-layer, что и `periodic_table_generator.py`.

---

## 3. TOPO_MAP

### 3.1. Anchor

Главный anchor chemical registry:

\[
E_{bond} = \frac{Ry}{3}
\]

В текущем executable generator:

- `Ry = 13.59844 eV`
- `E_BOND = 4.532813333... eV`

### 3.2. Малый алфавит coarse nodes

Текущий generator использует всего **10 числителей**:

\[
\{3, 9, 11, 13, 15, 16, 23, 38, 55, 67\}.
\]

Это уже не похоже на случайный fit. Это реально малый coarse-node vocabulary.

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

### 3.3. О provenance pairs `(N, D)`

Текущий generator хранит уже готовую registry-map:

```python
TOPO_MAP = { Z: (N, D), ... }
```

Но он не хранит в явном виде поле происхождения каждой пары:

- `derived`
- `selected`
- `bridge-derived`
- `open`

Следовательно, на этой версии приложения честно можно утверждать только следующее:

- full executable registry существует;
- его численные свойства считаются;
- но row-wise provenance ещё не вынесен в отдельный artifact.

### 3.4. Где сейчас лежит полный каталог

Полный `118`-строчный каталог `Z -> (N, D)` сейчас существует в трёх связанных формах:

- executable source of truth:
  - `/Users/abc/Codex_n111/tnr_final_synthesis/publishing/chemistry/periodic_table_generator.py`
- mirrored registry export (working copy):
  - [DOT_tnr_chemical_realization_topo_map_118_ru.md](/Users/abc/Codex_n8n/docs/prefin/ru/DOT_tnr_chemical_realization_topo_map_118_ru.md)
- mirrored registry export (publishing copy):
  - [DOT_tnr_chemical_realization_topo_map_118_ru.md](/Users/abc/Codex_n111/tnr_final_synthesis/publishing/DOT_tnr_chemical_realization_topo_map_118_ru.md)

Это различие принципиально:

- script остаётся **source of truth** для всего registry;
- markdown-export нужен как читаемый документальный срез;
- сам appendix не дублирует все `118` строк, а агрегирует их главные вычислимые свойства:
  - vocabulary;
  - global metrics;
  - block / period metrics;
  - outliers;
  - noble-gas closure-line;
  - prime occurrence table.

---

## 4. Error Metrics

### 4.1. Формулы

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

Ниже — **текущие executable values** из `periodic_table_generator.py`:

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

### 5.1. Текущий честный статус

В текущем repo есть **три разных уровня опоры** для screening-layer:

- `/Users/abc/Codex_n8n/docs/prefin/companion_code/scripts/tnr_comprehensive_engine.py`
  явно кодирует непрерывный `γ²`-screening law для L4 и печатает target-line
  `f -> 80/81`, `d -> 1-γ²/2`, `s -> 2/3`;
- `/Users/abc/Codex_n8n/docs/prefin/companion_code/scripts/tnr_same_shell_screening_extractor.py`
  делает standalone reverse-extraction representative `ΔS_same` directly from the
  same IE dataset for closure families `1s`, `3d`, `4f`, `5f`;
- основной chemical canon содержит уже собранную comparison-table по `ΔS_same`.

Следовательно, на этой версии приложения screening нужно фиксировать раздельно:

- representative same-shell table `1s / 3d / 4f / 5f` — как **executable extraction layer**;
- continuous `γ²`-law over the whole chemistry layer — как **strong law-readout**,
  потому что его обратное block-wide извлечение ещё не вынесено в отдельный generalized artifact.

### 5.2. Текущая рабочая таблица screening-targets

| Block / family | `ΔS_same (exp)` | DOT target | DOT expression | abs diff | Status |
|---|---:|---:|---|---:|---|
| `4f` (лантаноиды, full-fill) | `0.9884` | `80/81` | `1 - γ²/3` | `0.0007` | extracted |
| `5f` (актиноиды, full-fill) | `0.9682` | `26/27` | `1 - γ²/2` | `0.0052` | extracted |
| `3d` (металлы, full-fill) | `0.9545` | `26/27` | `1 - γ²/2` | `0.0085` | extracted |
| `1s` (primordial s-limit) | `0.6553` | `2/3` | `2/3` | `0.0113` | extracted |

### 5.3. Generalized family audit

Отдельный audit-script:

- `/Users/abc/Codex_n8n/docs/prefin/companion_code/scripts/tnr_screening_family_audit.py`

не только воспроизводит representative families, но и считает closure-values
для всех доступных `s / p / d / f`-подоболочек.

Главный вывод этого generalized audit:

- **не** весь block удерживается одним и тем же коэффициентом;
- удерживаются именно **representative locked families**;
- более поздние периоды показывают **period-depth drift** относительно малого screening vocabulary.

На текущем executable уровне это читается так:

- `s`-семейство:
  - `1s -> 0.6553 ~ 2/3`
  - дальше closure монотонно уходит вниз (`2s -> 0.6034`, `7s -> 0.4700`)
  - значит `2/3` — это **primordial s-limit**, а не универсальная константа всех `s`-семейств;
- `d`-семейство:
  - `3d` и `4d` остаются близки к `26/27`,
  - `5d` и особенно `6d` заметно уходят в drift;
- `f`-семейство:
  - `4f` lockится около `80/81`,
  - `5f` lockится около `26/27`;
- `p`-семейство:
  - на текущем audit не показывает clean lock к малому vocabulary
    `2/3`, `26/27`, `80/81`.

Следовательно, generalized audit усиливает канон не формулой
“каждый блок = один коэффициент”, а более точным законом:

> малый `γ²`-vocabulary задаёт representative closure-nodes,  
> а дальнейшие семейства читаются как их period-depth continuations с drift.

---

## 6. Macro-Primes

### 6.1. Что generator реально показывает

Executable generator даёт не только три числа `{19, 23, 67}`, а более широкий chemistry-only set:

\[
\{19, 23, 29, 31, 41, 43, 47, 59, 67\}.
\]

Shared set with particle-layer:

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

### 6.3. Noble gas line and its limit

| Element | `N/D` | Note |
|---|---|---|
| `He` | `38/7` | direct node `38` |
| `Ne` | `38/8` | direct node `38` |
| `Ar` | `38/11` | direct node `38` |
| `Kr` | `55/18` | closure-line continues, but no longer via `38` |
| `Xe` | `67/25` | closure-line continues, but via `67` |
| `Rn` | `38/16` | return to `38` |

---

## 7. Solver-Side Verified Layers

### 7.1. Strong canonical transfer

Скрипт:

- `/Users/abc/Codex_n111/tnr_final_synthesis/scripts/tnr_periodic_canonical_transfer.py`

даёт точный результат:

- `7 / 7` exact matches

для cases:

- `Cr`
- `Cu`
- `Mo`
- `Pd`
- `Ag`
- `Au`
- `Gd`

### 7.2. Weak residual transfer

Скрипт:

- `/Users/abc/Codex_n111/tnr_final_synthesis/scripts/tnr_periodic_residual_transfer.py`

даёт:

- `4 / 4` exact matches

для:

- `Nb`
- `Ru`
- `Rh`
- `Pt`

### 7.3. Exception split

Скрипт:

- `/Users/abc/Codex_n111/tnr_final_synthesis/scripts/tnr_periodic_exception_split.py`

разводит:

- strong half/full-transfer exceptions;
- weak residual-transfer exceptions.

---

## 8. Claim Status Map

| Claim | Current status | Why |
|---|---|---|
| `E_BOND = Ry/3` as chemical anchor | `[D]` artifact-level | явно зафиксирован в generator и molecular engine |
| Full `TOPO_MAP` for `1..118` exists | `[D]` artifact-level | полная registry-map есть в `periodic_table_generator.py` |
| Mean error `~0.31%` | `[D]` artifact-level | current executable value `0.312799%` |
| Small numerator vocabulary of size `10` | `[D]` artifact-level | читается напрямую из generator |
| Shared prime alphabet with particle layer | `[Г1]` strong structural reading | cross-reference вычислим, но интерпретация still structural |
| Macro-primes `{19,23,67}` are privileged | `[Г1]` | generator supports them strongly, но chemistry-only set шире |
| Canonical transfer group (`7/7`) | `[D]` artifact-level | отдельный exact-match script |
| Residual transfer group (`4/4`) | `[D]` artifact-level | отдельный exact-match script |
| Representative `ΔS_same` extraction (`1s/3d/4f/5f`) | `[D]` artifact-level | standalone extractor reproduces the screening table values from the same IE dataset |
| Generalized family screening audit | `[D]` artifact-level | all subshell closure trajectories are reproducibly computed and show where lock vs drift occurs |
| Screening law around `γ²` | `[Г1]` strong law-readout | continuous law is encoded in `tnr_comprehensive_engine.py`; generalized block-wide reverse extraction remains a higher-layer task |
| Every pair `(N,D)` already has row-wise provenance | `[Г2]` open | current registry stores final map, not provenance annotations |

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
| Separate atomic model | `/Users/abc/Codex_n111/tnr_final_synthesis/scripts/tnr_lattice_atom_solver.py` | independent atomic/slater experiment, not the same registry |
| Hydrogen-like testbed | `/Users/abc/Codex_n111/tnr_final_synthesis/scripts/tnr_atomic_test_all.py` | separate single-electron testbed |
