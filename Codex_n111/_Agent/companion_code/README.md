# DOT Companion Code

Репозиторная папка с companion-code для ТНР / DOT.

Эта директория собрана как нормализованный кодовый слой вокруг теории:

- `scripts/` — актуальные исполняемые Python-скрипты;
- `formal_proofs/` — Lean-доказательства и формальные заготовки;
- `notes/` — короткие research-notes по отдельным направлениям;
- `outputs/` — сохранённые текстовые отчёты и результаты запусков.

## Что считается центром

Центром этой папки является **актуальный код в `scripts/`**.

Плоская папка `/Users/abc/Codex_n111/_Agent/Code` используется как
рабочий source-snapshot финальных скриптов.
При синхронизации её содержимое переносится в `scripts/`,
а сама `companion_code` остаётся repo-ready структурой
для хранения кода, примечаний, формальных доказательств и результатов.

## Дерево проекта

```text
companion_code/
├── README.md
├── README_code.md
├── requirements.txt
├── .gitignore
├── docs/
│   └── REPO_STRUCTURE.md
├── scripts/
│   ├── tnr_comprehensive_engine.py
│   ├── tnr_molecular_engine_v2.py
│   ├── tnr_layer_inspector.py
│   ├── tnr_l1_particle_readable_report.py
│   ├── tnr_l3_molecule_readable_report.py
│   ├── tnr_l4_element_readable_report.py
│   ├── tnr_same_shell_screening_extractor.py
│   ├── tnr_l4_same_shell_screening_extractor.py
│   ├── tnr_screening_family_audit.py
│   ├── tnr_l4_screening_family_audit.py
│   └── README_chemistry_code_map.md
├── formal_proofs/
│   ├── DOT_Particle_Spectrum.lean
│   └── DOT_Sn_Isotopes.lean
├── notes/
│   ├── DOT_yang_mills_and_riemann_note_ru.md
│   ├── DOT_yang_mills_and_riemann_note_en.md
│   ├── DOT_yang_mills_mass_gap_note_ru.md
│   └── DOT_yang_mills_mass_gap_note_en.md
└── outputs/
    ├── engine_full_report.txt
    └── readable_reports/
        ├── README.md
        ├── l1_particle_readable_report.txt
        ├── l4_element_readable_report.txt
        └── l4_element_example_U92.txt
```

## Базовые точки входа

### Полный движок

```bash
python3 scripts/tnr_comprehensive_engine.py
```

Это основной агрегирующий запуск. Он собирает несколько уровней:

- константы;
- частицы;
- ядра;
- молекулярный слой;
- диагностические readout’ы.

### Молекулярный движок

```bash
python3 scripts/tnr_molecular_engine_v2.py
```

Используется как отдельный chemistry-layer / bond-energy слой.

### Линейные readable-report скрипты

```bash
python3 scripts/tnr_l1_particle_readable_report.py
python3 scripts/tnr_l3_molecule_readable_report.py
python3 scripts/tnr_l4_element_readable_report.py
```

Они дают человекочитаемые отчёты по слоям.

### Screening / audit

```bash
python3 scripts/tnr_same_shell_screening_extractor.py
python3 scripts/tnr_l4_same_shell_screening_extractor.py
python3 scripts/tnr_screening_family_audit.py
python3 scripts/tnr_l4_screening_family_audit.py
```

Это инструменты для чтения экранирования и family-audit химического слоя.

## Formal proofs

Lean-файлы лежат в `formal_proofs/`.

Минимальный запуск:

```bash
lean --run formal_proofs/DOT_Sn_Isotopes.lean
```

## Outputs

Папка `outputs/` предназначена для сохраняемых результатов.
Сейчас там уже лежит:

- `engine_full_report.txt` — полный текстовый отчёт агрегирующего движка.

Отдельно сохранены человекочитаемые generated artifacts в `outputs/readable_reports/`:

- `l1_particle_readable_report.txt` — полный каталог L1-частиц из report-скрипта;
- `l4_element_readable_report.txt` — полный каталог 118 элементов из chemical-layer report-скрипта;
- `l4_element_example_U92.txt` — развёрнутый пример для `U (Z=92)` как тяжёлого `5f`-узла с малой ошибкой и видимым family-context;
- `README.md` — краткая карта этих saved outputs.

## Что здесь важно не путать

- `companion_code` — это **структурированная репо-папка**;
- `Code` — это **плоский источник актуальных скриптов**;
- конечной точкой для GitHub и дальнейшего сопровождения
  должна быть именно эта папка `companion_code`.
