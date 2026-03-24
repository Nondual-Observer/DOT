# DOT Companion Code (Draft)

This repository contains a **companion code layer** for the *Distinction Observable Theory (DOT)* manuscript bundle.

The code is intended for **numerical reproducibility and diagnostics**, not as a replacement for formal derivations in the manuscript.

## Quickstart

Run the single entrypoint script:

```bash
python3 scripts/dot_companion_verify.py --chem
python3 scripts/dot_companion_verify.py --full
python3 scripts/dot_companion_verify.py --tails
python3 scripts/dot_companion_verify.py --vacuum64
python3 scripts/dot_companion_verify.py --hydrogen-dyn
python3 scripts/dot_companion_verify.py --all
```

## What’s Included

- `scripts/tnr_hydrogen_dynamic_v10.py`
  - exploratory “topological chemistry” model for hydrides and a bounded `C2Hn` multi-center branch.
- `scripts/dot_companion_verify.py`
  - a stable CLI wrapper that runs selected scripts and prints their outputs.
- `scripts/companion_legacy/`
  - legacy snapshot scripts (useful as a dashboard; they mix exact identities, baseline predictions, and candidate layers).

## Output Snapshots

For GitHub readability, representative runs are saved under `outputs/`:

- `outputs/chemistry_v10.txt`
- `outputs/full_verification_legacy.txt`
- `outputs/tails_legacy.txt`
- `outputs/vacuum64_legacy.txt`
- `outputs/hydrogen_dynamics_v5_1.txt`

## Status

- Chemistry (`--chem`) is explicitly **exploratory** and limited to specific carrier classes.
- Legacy scripts are kept as a **snapshot/dashboard** and are not treated as a single closed proof.

## License

- **Code:** [Apache License 2.0](../LICENSE)
- **Theory and documentation:** [CC BY-NC-SA 4.0](../LICENSE-THEORY.md)
