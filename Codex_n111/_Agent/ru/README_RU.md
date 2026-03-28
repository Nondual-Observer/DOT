# Теория Наблюдаемых Различий (ТНР / DOT)

> **Языки:** [English](../README.md) | [Русский](README_RU.md)

[![DOI](https://zenodo.org/badge/1188736747.svg)](https://doi.org/10.5281/zenodo.19272459)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/Theory-CC%20BY--NC--SA%204.0-blue.svg)](../LICENSE-THEORY.md)
[![License: Apache-2.0](https://img.shields.io/badge/Code-Apache--2.0-yellow.svg)](../LICENSE)

> *«Непроявленное [Пракрити] наделено тремя гунами… Гуны по своей природе — радость [Саттва], страдание [Раджас] и безразличие [Тамас]. Их назначение — освещать, приводить в движение и ограничивать. Они подавляют друг друга, опираются друг на друга, порождают друг друга и действуют совместно, подобно светильнику [где масло, фитиль и пламя действуют вместе].*
>
> *…Пуруша [чистое сознание] — лишь свидетель происходящего. Он наделён абсолютной изоляцией, совершенной невозмутимостью, способностью созерцать и абсолютным недеянием.*
>
> *…Ради созерцания Пурушей Пракрити и ради его окончательного освобождения происходит их соединение. Оно подобно союзу хромого и слепого. Из этого союза возникает творение.»*
> — *Санкхья Карика, 11–21*

---

## Что это за репозиторий

Это репозиторий ТНР как **собранной системы**, а не как набора разрозненных
текстов или скриптов.

Здесь есть три связанных слоя:

- **теория** — русский и английский корпус текстов;
- **машина** — архитектурная карта того, как теория устроена как рабочая
  структура;
- **код** — companion-layer, который проводит тот же каркас через константы,
  частицы, ядра, молекулярные и химические readout-ы.

Идея репозитория простая: показать, что один и тот же structural каркас можно
читать как теорию, как архитектуру машины и как воспроизводимый код.

## Что такое ТНР простыми словами

**Теория Наблюдаемых Различий** начинается не с готовых объектов, а с более
раннего вопроса: *что вообще делает различение возможным*.

В обычном языке мы говорим так, будто сначала существует вещь, а потом мы её
видим, измеряем и описываем. ТНР предлагает другой порядок. Сначала должны
появиться:

- граница;
- запрет совпадения;
- полярность;
- переход;
- замыкание;
- и только потом объект как устойчивый readout.

Поэтому ТНР — это не просто “ещё одна физическая модель”. Это попытка описать
каркас, в котором:

- структура;
- действие;
- наблюдение

не сводятся друг к другу.

В текущем каноническом виде нижний слой машины читается как лестница:

```text
0 -> 1 -> 2 -> 6 -> 12 -> 8
```

где:

- `0` — vacuum fixed-point;
- `1` — unary identity;
- `2` — первая полярность;
- `6` — триадная граница;
- `12` — переходная рёберная сеть;
- `8` — первое замыкание.

Это не “магические числа”, а опорные узлы нижней grammar машины.

## Кодовая часть

В этом репозитории теория не висит отдельно от кода. Здесь есть полноценный
вычислительный слой, который показывает, что ТНР работает не только как язык
описания, но и как **генеративная схема расчёта**.

Здесь есть две разные рабочие формы:

- **Python companion-code** — основной численный движок;
- **Lean 4** — слой формальной проверки отдельных выводов.

### Python companion-code

Основной код лежит в:

- [`../companion_code/`](../companion_code/)

Главный движок:

```bash
cd ../companion_code
python3 scripts/tnr_comprehensive_engine.py
```

Это не black-box fit и не нейросеть, подогнанная под таблицу данных. Принцип
другой: один и тот же набор топологических и геометрических инвариантов
проходит через несколько этажей и даёт численные readout-ы разных физических
слоёв.

В текущем виде движок собирает:

- **L0** — фундаментальные константы и базовые readout-ы;
- **L1** — массы частиц;
- **L2** — ядерный слой;
- **L3** — молекулярные и химические проекции;
- **L4** — фундаментальные контрольные readout-ы.

Если совсем коротко, то код показывает следующее:

- массы частиц вычисляются не как свободный fit, а из фиксированных
  геометрических баз и носителей;
- ядерный слой строится через тот же каркас, а не через отдельную “другую”
  теорию;
- молекулярный и химический слой читаются как более поздняя проекция той же
  grammar;
- одна и та же машина проходит через разные масштабы без смены базового
  алфавита.

Ключевые текущие результаты:

- **L1**: 24 массы частиц с ошибками порядка `< 0.001%`;
- **L2**: 98 ядерных изотопов с ошибками порядка `< 0.001%`;
- **L3**: 14 молекулярных энергий связей со средней ошибкой около `0.32%`;
- **L4**: фундаментальные readout-ы без свободных параметров.

То есть кодовый слой здесь нужен не “для иллюстрации”, а для демонстрации того,
что один структурный закон действительно способен вычислительно проходить через
константы, частицы, ядра и chemistry-layer.

Если нужна не только команда запуска, а само описание принципа работы кодового
слоя, правильный документ здесь:

- [`../companion_code/README_code.md`](../companion_code/README_code.md)

### Lean 4

Lean-слой не заменяет Python-движок. Он нужен для другой задачи: формально и
исполняемо проверять отдельные выводы ТНР, когда уже нужно не численное
совпадение, а строгое пошаговое доказательство.

Если нужен самый быстрый вход именно в particle-layer на Lean, то сейчас есть
два отдельных entry-point файла:

- английский bait/prototype:
  [`../docs/prefin/24_part_Lean!/ParticlePrototype.lean`](../docs/prefin/24_part_Lean!/ParticlePrototype.lean)
- локальный русский вариант:
  [`../docs/prefin/24_part_Lean!/ParticlePrototype_ru.lean`](../docs/prefin/24_part_Lean!/ParticlePrototype_ru.lean)

Они показывают не “всю теорию в Lean”, а одну конкретную вещь, которая для
внешнего человека считывается сразу:

- bare-формулу частицы;
- bare-массу;
- финальное значение текущего пакета `L1`;
- ошибку относительно текущего reference-набора;
- и сам reference с uncertainty.

То есть это минимальный наглядный вход, где уже видно, что:

- система не black box;
- bare-layer и final-layer разведены;
- и точность сравнения с текущими данными лежит прямо в выводе.

Ключевые файлы лежат здесь:

- [`../companion_code/formal_proofs/DOT_Sn_Isotopes.lean`](../companion_code/formal_proofs/DOT_Sn_Isotopes.lean)
- [`../companion_code/formal_proofs/DOT_Particle_Spectrum.lean`](../companion_code/formal_proofs/DOT_Particle_Spectrum.lean)

То есть:

- Python показывает широкий численный проход машины через несколько слоёв;
- Lean фиксирует, что отдельные узлы этой машины уже можно переводить в строгий
  proof-режим.

## С чего начинать чтение

Если человек вообще не знаком с ТНР, правильный первый вход только один:

- [`Theory_Core/DOT_foundations_and_machine_ru.md`](Theory_Core/DOT_foundations_and_machine_ru.md)

Это главный стартовый текст. Он даёт:

- базовую логику различения;
- роль октаэдральной машины;
- разведение `structure / act / observation`;
- и общий каркас, без которого поздние документы будут читаться как набор
  сильных, но висящих в воздухе утверждений.

После него разумный порядок такой:

1. [`Machine/DOT_machine_architecture_overview_ru.md`](Machine/DOT_machine_architecture_overview_ru.md)
2. [`Theory_Science/DOT_physical_realization_ru.md`](Theory_Science/DOT_physical_realization_ru.md)

То есть:

- сначала foundations;
- потом карта машины;
- потом уже физическая реализация.

## Как устроен корпус текстов

Русская ветка делится на три больших раздела:

- `Theory_Core/`
- `Machine/`
- `Theory_Science/`

Это полезно понимать заранее, потому что документы внутри них имеют разный
статус.

### 1. Theory Core

Это нижний и средний теоретический каркас ТНР.

Ключевые тексты:

- [`Theory_Core/DOT_foundations_and_machine_ru.md`](Theory_Core/DOT_foundations_and_machine_ru.md)  
  главный вход в foundations;
- [`Theory_Core/DOT_tnr_pure_structural_core_ru.md`](Theory_Core/DOT_tnr_pure_structural_core_ru.md)  
  более чистое ядро ранней structural logic;
- [`Theory_Core/DOT_tnr_foundations_architectural_full_ru.md`](Theory_Core/DOT_tnr_foundations_architectural_full_ru.md)  
  полная архитектурная развёртка;
- [`Theory_Core/DOT_tnr_foundations_formal_appendix_ru.md`](Theory_Core/DOT_tnr_foundations_formal_appendix_ru.md)  
  формальный supporting appendix;
- [`Theory_Core/DOT_liminal_canon_ru.md`](Theory_Core/DOT_liminal_canon_ru.md)  
  пограничный канон и переходные узлы.

Если нужен только один foundational text, начинать надо с:

- [`Theory_Core/DOT_foundations_and_machine_ru.md`](Theory_Core/DOT_foundations_and_machine_ru.md)

### 2. Machine

Это раздел о том, как теория собирается как машина.

Ключевые тексты:

- [`Machine/DOT_machine_architecture_overview_ru.md`](Machine/DOT_machine_architecture_overview_ru.md)
- [`Machine/DOT_terminologiya_i_sloevaya_karta_ru.md`](Machine/DOT_terminologiya_i_sloevaya_karta_ru.md)
- [`Machine/DOT_octahedral_proof_calculus_ru.md`](Machine/DOT_octahedral_proof_calculus_ru.md)
- [`Machine/DOT_code_availability_ru.md`](Machine/DOT_code_availability_ru.md)

Этот раздел лучше читать уже после основного foundational входа, когда нижняя
grammar различения уже схвачена.

## Научный раздел

`Theory_Science/` — это не один документ и не один “раздел физики”. Это слой,
где ТНР начинает проецироваться в математические, физические, химические и
поздние исследовательские коридоры.

Важно держать в голове простое различие:

- часть этих текстов имеет характер **основных томов**;
- часть — **сильных companion-документов**;
- часть — **draft / research corridor**, которые важны, но не должны
  читаться как уже окончательно закрытый канон.

### Математический и операторный вход

Если нужен вход в number-theory и operator-layer ТНР, идти лучше так:

- [`Theory_Science/DOT_mathematical_framework_ru.md`](Theory_Science/DOT_mathematical_framework_ru.md)
- [`Theory_Science/DOT_tnr_mathematical_operator_line_ru.md`](Theory_Science/DOT_tnr_mathematical_operator_line_ru.md)

Первый текст даёт большой математический каркас.
Второй — более компактную линию операторных узлов и переходов.

### Физическая реализация

Основной физический том:

- [`Theory_Science/DOT_physical_realization_ru.md`](Theory_Science/DOT_physical_realization_ru.md)

Это главный science-level text, если интересует, как теоретическая машина
проецируется в слой частиц, ядер и matter-readouts.

### Поздние companion / research-документы

Эти тексты важны, но они уже не самый первый вход:

- [`Theory_Science/DOT_tnr_multiplicative_additive_resonance_ru.md`](Theory_Science/DOT_tnr_multiplicative_additive_resonance_ru.md)  
  companion-документ о числовых резонансах, prime-ролях и соотношениях
  аддитивного и мультипликативного чтения;
- [`Theory_Science/DOT_tnr_processual_boundary_draft_ru.md`](Theory_Science/DOT_tnr_processual_boundary_draft_ru.md)  
  draft о processual boundary, closure, tail, `2×2`-логике и гравитационном
  коридоре.

Их лучше читать только после foundations и основного physical layer.

### Химический подкорпус

Химия в ТНР — это уже отдельный подкорпус внутри scientific layer.

Если идти в него, то порядок лучше такой:

1. [`Theory_Science/DOT_tnr_chemical_realization_canon_ru.md`](Theory_Science/DOT_tnr_chemical_realization_canon_ru.md)
2. [`Theory_Science/DOT_tnr_chemical_realization_appendix_ru.md`](Theory_Science/DOT_tnr_chemical_realization_appendix_ru.md)
3. [`Theory_Science/DOT_tnr_chemical_realization_topo_map_118_ru.md`](Theory_Science/DOT_tnr_chemical_realization_topo_map_118_ru.md)
4. [`Theory_Science/DOT_tnr_chemical_screening_family_audit_ru.md`](Theory_Science/DOT_tnr_chemical_screening_family_audit_ru.md)
5. [`Theory_Science/DOT_tnr_chemical_realization_canon_stabilization_map_ru.md`](Theory_Science/DOT_tnr_chemical_realization_canon_stabilization_map_ru.md)

Здесь важно: chemical canon уже силён как late-stage synthesis, но appendix и
audit-слой нужны, чтобы не путать сильное соответствие с полностью закрытым
строгим выводом.

## Как устроен репозиторий сейчас

Актуальная структура `_Agent/` выглядит так:

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
│   ├── Theory_Science/
│   └── Machine/
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

Важно не путать роли:

- `ru/` — актуальная русская ветка корпуса;
- `en/` — английская ветка;
- `companion_code/` — repo-ready кодовый слой;
- `Code/` — плоский source-snapshot актуальных скриптов.

Центром кодовой части считается:

- [`../companion_code/README.md`](../companion_code/README.md)

## Как запускать код

Для базового запуска нужен Python 3 и `numpy`.

Минимальный вход:

```bash
cd ../companion_code
pip install -r requirements.txt
python3 scripts/tnr_comprehensive_engine.py
```

Этот запуск собирает несколько уровней сразу:

- константы;
- частицы;
- ядра;
- молекулярный слой;
- диагностические readout-ы.

Если нужен не полный агрегирующий прогон, а локальные отчёты, useful entry
points такие:

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

Lean для обычного Python-запуска не нужен. Он нужен только для formal proof
layer.

## Что уже сохранено в outputs

В `companion_code/outputs/` уже лежат не только агрегирующие отчёты, но и
отдельные readable artifacts:

- [`../companion_code/outputs/engine_full_report.txt`](../companion_code/outputs/engine_full_report.txt)
- [`../companion_code/outputs/readable_reports/l1_particle_readable_report.txt`](../companion_code/outputs/readable_reports/l1_particle_readable_report.txt)
- [`../companion_code/outputs/readable_reports/l4_element_readable_report.txt`](../companion_code/outputs/readable_reports/l4_element_readable_report.txt)
- [`../companion_code/outputs/readable_reports/l4_element_example_U92.txt`](../companion_code/outputs/readable_reports/l4_element_example_U92.txt)
- [`../companion_code/outputs/readable_reports/README.md`](../companion_code/outputs/readable_reports/README.md)

То есть кодовый слой уже даёт не только machine outputs, но и человекочитаемые
входы в particle и chemical layers.

## Формальные доказательства

Lean-файлы лежат в:

- [`../companion_code/formal_proofs/`](../companion_code/formal_proofs/)

Ключевые файлы:

- [`../companion_code/formal_proofs/DOT_Sn_Isotopes.lean`](../companion_code/formal_proofs/DOT_Sn_Isotopes.lean)
- [`../companion_code/formal_proofs/DOT_Particle_Spectrum.lean`](../companion_code/formal_proofs/DOT_Particle_Spectrum.lean)

Минимальный запуск:

```bash
cd ../companion_code
lean --run formal_proofs/DOT_Sn_Isotopes.lean
```

## Основные публикационные тома

Если нужен сжатый publication backbone, то читать удобно так:

| # | Текст | Фокус |
|:-:|:------|:------|
| **I** | [Foundations and Machine](Theory_Core/DOT_foundations_and_machine_ru.md) | foundations, octahedral machine, базовый carrier |
| **II** | [Mathematical Framework](Theory_Science/DOT_mathematical_framework_ru.md) | числа, spectral layer, modular and operator readings |
| **III** | [Physical Realization](Theory_Science/DOT_physical_realization_ru.md) | частицы, ядра, chemistry-layer, physical readouts |

Дополнительные опорные тексты:

| | Текст | Фокус |
|:-:|:------|:------|
| **IV** | [Machine Architecture Overview](Machine/DOT_machine_architecture_overview_ru.md) | полная карта слоёв машины |
| **V** | [Terminology and Layer Map](Machine/DOT_terminologiya_i_sloevaya_karta_ru.md) | словарь терминов и layer-map |
| **VI** | [Code Availability Statement](Machine/DOT_code_availability_ru.md) | воспроизводимость и кодовый слой |
| **VII** | [Formal Verification (Lean 4)](../companion_code/formal_proofs/DOT_Sn_Isotopes.lean) | исполняемая математическая проверка |

## Фундаментальные инварианты

Ниже — не “доказательство всей теории”, а минимальный набор опорных констант,
которые в текущем корпусе играют роль support constants машины:

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
  doi       = {10.5281/zenodo.19272459},
  url       = {https://github.com/nondual-observer/distinction-observable-theory}
}
```

## Поддержка исследования

Этот проект развивается как **независимое открытое исследование** без
институционального финансирования.

Пожертвования добровольны.

| Currency | Network | Address |
|----------|---------|---------|
| Bitcoin | BTC | `bc1qlaxsrum7fxpml57nsrtkjfkkxl5v3xtj4d0uxe` |
| USDT | TRC20 | `TM8U2EqVaT3tjvG6NyuKTqY4F5qc2A69Sy` |
| Ethereum | ETH | `0x4fFc68f0d55d19Fa5EBd5f6570a41E100aFe4a98` |

## Лицензии

**Code:** [Apache License 2.0](../LICENSE)  
**Theory & Documentation:** [CC BY-NC-SA 4.0](../LICENSE-THEORY.md)

---

*© 2026 Igor M. Zhuk. All rights reserved under the respective licenses.*
