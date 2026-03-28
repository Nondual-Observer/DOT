# TNR Chemistry Code Map

## Purpose

This note explains the current split of the chemical / particle executable layer.

The guiding rule is:

> one model law, multiple readable entry points.

The code is split not because the theory is fragmented,
but because a readable model must separate:

- canonical engine,
- one unified entrypoint,
- layer-prefixed readable reports,
- narrow extractors,
- generalized audits,
- and human-facing reports.

---

## Reading Order

For a new reader, the shortest correct path through the code is:

1. Run [tnr_layer_inspector.py](/Users/abc/Codex_n8n/docs/prefin/companion_code/scripts/tnr_layer_inspector.py) once for `l1`, `l3`, or `l4`.
2. Read the corresponding readable report file:
   - [tnr_l1_particle_readable_report.py](/Users/abc/Codex_n8n/docs/prefin/companion_code/scripts/tnr_l1_particle_readable_report.py)
   - [tnr_l3_molecule_readable_report.py](/Users/abc/Codex_n8n/docs/prefin/companion_code/scripts/tnr_l3_molecule_readable_report.py)
   - [tnr_l4_element_readable_report.py](/Users/abc/Codex_n8n/docs/prefin/companion_code/scripts/tnr_l4_element_readable_report.py)
3. Open [tnr_comprehensive_engine.py](/Users/abc/Codex_n8n/docs/prefin/companion_code/scripts/tnr_comprehensive_engine.py) and find the matching `L1`, `L3`, or `L4` section.
4. Check how the staged breakdown is assembled:
   - bare state
   - local/intermediate correction
   - tail or environment correction
   - final value
5. Only after that open the `L4` extractor and audit files.
6. Open [tnr_molecular_engine_v2.py](/Users/abc/Codex_n8n/docs/prefin/companion_code/scripts/tnr_molecular_engine_v2.py) last, as a research extension rather than canonical entrypoint.

If someone starts from the research file first, they will get a distorted picture of the model.

---

## File Roles

### Recommended starting point

- [tnr_layer_inspector.py](/Users/abc/Codex_n8n/docs/prefin/companion_code/scripts/tnr_layer_inspector.py)

Role:

- single entrypoint for browsing the canonical executable model;
- dispatches to `L1`, `L3`, and `L4` readable inspectors.

Use this file when you need:

- the easiest first contact with the code;
- one command that exposes the staged model without knowing the internal layout.

Examples:

- `python3 tnr_layer_inspector.py --layer l1`
- `python3 tnr_layer_inspector.py --layer l3 --name "H₂O"`
- `python3 tnr_layer_inspector.py --layer l4 --z 26`

---

### Core engine

- [tnr_comprehensive_engine.py](/Users/abc/Codex_n8n/docs/prefin/companion_code/scripts/tnr_comprehensive_engine.py)

Role:

- canonical multi-layer executable engine;
- stores the shared particle grammar;
- stores the chemical `TOPO_MAP`;
- exposes readable L1 breakdown helpers.

Use this file when you need:

- the model itself;
- shared constants;
- canonical registry data;
- reusable layer APIs;
- the canonical implementation behind the readable reports.

---

### Research extension

- [tnr_molecular_engine_v2.py](/Users/abc/Codex_n8n/docs/prefin/companion_code/scripts/tnr_molecular_engine_v2.py)

Role:

- extended research playground for molecular laws beyond the canonical `L3` subset;
- contains broader exploratory molecule families and additional hypotheses.

Use this file when you need:

- research coverage beyond the canonical 14-molecule layer;
- experimental molecular ideas that are not the best first entrypoint for readers.

Do not start here if the goal is to understand the model architecture.
Start with `tnr_layer_inspector.py` and `tnr_comprehensive_engine.py`.

---

### Representative extractor

- [tnr_l4_same_shell_screening_extractor.py](/Users/abc/Codex_n8n/docs/prefin/companion_code/scripts/tnr_l4_same_shell_screening_extractor.py)

Role:

- standalone reverse-extraction of representative `ΔS_same` values from the IE dataset;
- proves the specific closure families:
  - `1s`
  - `3d`
  - `4f`
  - `5f`

Use this file when you need:

- the minimal executable backbone of the screening table;
- a direct check that the canonical targets are not entered by hand.

Compatibility alias retained:

- [tnr_same_shell_screening_extractor.py](/Users/abc/Codex_n8n/docs/prefin/companion_code/scripts/tnr_same_shell_screening_extractor.py)

---

### Generalized audit

- [tnr_l4_screening_family_audit.py](/Users/abc/Codex_n8n/docs/prefin/companion_code/scripts/tnr_l4_screening_family_audit.py)

Role:

- computes closure trajectories for all subshell families;
- distinguishes representative locks from period-depth drift.

Use this file when you need:

- a defense against overclaiming;
- a full-family map instead of selected showcase families.

Compatibility alias retained:

- [tnr_screening_family_audit.py](/Users/abc/Codex_n8n/docs/prefin/companion_code/scripts/tnr_screening_family_audit.py)

---

### Readable particle report

- [tnr_l1_particle_readable_report.py](/Users/abc/Codex_n8n/docs/prefin/companion_code/scripts/tnr_l1_particle_readable_report.py)

Role:

- human/AI-facing particle inspector;
- shows:
  - bare carrier
  - shifted state
  - residual tail
  - final value

Use this file when you need:

- to show that the long formula is not fitting the whole mass;
- to demonstrate that the tail is a small correction over a much larger carrier.

---

### Readable molecule report

- [tnr_l3_molecule_readable_report.py](/Users/abc/Codex_n8n/docs/prefin/companion_code/scripts/tnr_l3_molecule_readable_report.py)

Role:

- human/AI-facing molecular inspector for the canonical L3 layer;
- shows:
  - bare carrier
  - local topology correction
  - environment multiplier
  - final value

Use this file when you need:

- to show that the molecular layer is also staged and not one opaque fit;
- to compare bare bond carrier against topology and shell corrections.

---

### Readable element report

- [tnr_l4_element_readable_report.py](/Users/abc/Codex_n8n/docs/prefin/companion_code/scripts/tnr_l4_element_readable_report.py)

Role:

- human/AI-facing chemical inspector;
- supports:
  - full catalog mode
  - single-element inspect mode

Use this file when you need:

- a table-like overview of all 118 elements;
- one-element contextual inspection (`--z`).

---

## Design Rule

The main anti-fitting rule is:

1. show the **bare state** first;
2. show the **intermediate state** second;
3. show the **tail correction** explicitly;
4. only then show the **final value**.

If a script cannot expose that structure, it should not be used as a public-facing
representation of the model.

## Naming Rule

Canonical public-facing names should make the layer explicit:

- `tnr_l1_*` for particle layer
- `tnr_l3_*` for molecular layer
- `tnr_l4_*` for chemical layer

Older unprefixed audit/extractor names are kept only as compatibility aliases.

---

## Theory Anchors

The scripts follow a stable theory grammar, even when document names or
section numbers still move:

- carrier first, tail second;
- registry first, correction second;
- representative lock separated from later drift;
- readable staged output preferred over opaque closed formulas.

The theory corpus explains **why** these operators exist.
The scripts are responsible for showing **how** they behave on data.
