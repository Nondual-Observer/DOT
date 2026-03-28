# DOT / TNR Chemical Screening Family Audit

## 1. Статус

Этот документ фиксирует результат generalized audit для `same-shell screening`
в chemical layer.

Он опирается на executable artifacts:

- [periodic_table_generator.py](/Users/abc/Codex_n111/tnr_final_synthesis/publishing/chemistry/periodic_table_generator.py)
- [tnr_same_shell_screening_extractor.py](/Users/abc/Codex_n111/tnr_final_synthesis/publishing/chemistry/tnr_same_shell_screening_extractor.py)
- [tnr_screening_family_audit.py](/Users/abc/Codex_n111/tnr_final_synthesis/publishing/chemistry/tnr_screening_family_audit.py)

Главный результат аудита:

- малый `γ²`-vocabulary действительно воспроизводит **representative closure-families**;
- но generalized family map **не** подтверждает простую формулу
  `весь block = один и тот же коэффициент`;
- вместо этого возникает более точная картина:
  **locked representative families + period-depth drift**.

---

## 2. Метод

Для каждой подоболочки с как минимум двумя элементами берётся первый элемент
семейства как anchor.

Из его энергии ионизации восстанавливается:

\[
S_{inner}=Z-n\sqrt{IE/Ry}.
\]

Далее для каждого следующего положения внутри той же подоболочки вычисляется:

\[
\Delta S_{same}=\frac{Z-S_{inner}-n\sqrt{IE/Ry}}{pos-1}.
\]

Closure-value семейства определяется на полной заполненности (`pos = cap`).

Именно эти closure-values и сравниваются с малым screening-vocabulary:

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

Именно эти четыре семейства сейчас можно считать
representative executable locks:

| Family | Closure `ΔS_same` | DOT target | abs diff |
|---|---:|---|---:|
| `1s` | `0.655337` | `2/3` | `0.011330` |
| `3d` | `0.954503` | `26/27` | `0.008460` |
| `4f` | `0.988382` | `80/81` | `0.013074` |
| `5f` | `0.968189` | `26/27` | `0.005226` |

Это и есть минимальный executable backbone текущей screening-table.

---

## 5. Block-wise Reading

### 5.1. `s`-семейство

`s`-closure не остаётся константным.

Серия идёт так:

\[
1s \to 0.6553,\;
2s \to 0.6034,\;
3s \to 0.5947,\;
4s \to 0.5781,\;
5s \to 0.5354,\;
6s \to 0.4962,\;
7s \to 0.4700.
\]

Значит:

- `2/3` — это не универсальная константа всех `s`-подоболочек;
- это **primordial s-limit**, наиболее чисто проявленный в `1s`;
- дальше начинается выраженный period-depth drift.

### 5.2. `d`-семейство

`3d` и `4d` остаются близки к `26/27`, но затем drift усиливается:

\[
3d \approx 0.9545,\quad
4d \approx 0.9391,\quad
5d \approx 0.8642,\quad
6d \approx 0.7816.
\]

Значит:

- `26/27` хорошо держит ранние `d`-closure families;
- поздние `d`-семейства уже не сводятся к той же точке без остатка.

### 5.3. `f`-семейство

Здесь split особенно чистый:

- `4f` lockится около `80/81`;
- `5f` lockится около `26/27`.

То есть `f`-слой сам не однороден и bifurcates на два closure-regime.

### 5.4. `p`-семейство

На текущем audit `p`-семейства не дают clean lock к малому vocabulary.

Значит:

- `p`-layer нельзя честно свести к той же простой формуле,
  что `1s / 3d / 4f / 5f`;
- это либо другой режим экранирования,
  либо слой, где малый vocabulary проявляется уже косвенно.

---

## 6. Главный Вывод

Generalized audit не разрушает chemical canon. Наоборот, он его очищает.

Он показывает, что правильная формула такова:

> малый `γ²`-vocabulary задаёт не весь block целиком,  
> а representative closure-families;  
> остальные семейства читаются как их period-depth continuations с drift.

Именно в таком виде screening-layer сейчас является
самым точным и самым защищаемым чтением.
