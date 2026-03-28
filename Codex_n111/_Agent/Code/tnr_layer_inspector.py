#!/usr/bin/env python3
"""
Unified readable inspector for canonical TNR layers.

This is the recommended entrypoint for someone who wants to browse the
public-facing executable model without first learning the full file layout.

Layers:
  - l1: particle layer
  - l3: molecular layer
  - l4: chemical layer

Examples:
  python3 tnr_layer_inspector.py --layer l1
  python3 tnr_layer_inspector.py --layer l1 --name "Pion (π⁰)"
  python3 tnr_layer_inspector.py --layer l3 --name "H₂O"
  python3 tnr_layer_inspector.py --layer l4 --z 26
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from tnr_l1_particle_readable_report import (  # noqa: E402
    all_breakdowns as l1_all_breakdowns,
    print_catalog as l1_print_catalog,
    print_single as l1_print_single,
)
from tnr_l3_molecule_readable_report import (  # noqa: E402
    all_breakdowns as l3_all_breakdowns,
    print_catalog as l3_print_catalog,
    print_single as l3_print_single,
)
from tnr_l4_element_readable_report import (  # noqa: E402
    element_row as l4_element_row,
    load_generator as l4_load_generator,
    print_catalog as l4_print_catalog,
    print_single as l4_print_single,
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--layer",
        required=True,
        choices=["l1", "l3", "l4"],
        help="Canonical layer to inspect",
    )
    parser.add_argument("--name", help="Exact particle or molecule display name for l1/l3")
    parser.add_argument("--z", type=int, help="Atomic number for l4")
    args = parser.parse_args()

    if args.layer in {"l1", "l3"} and args.z is not None:
        raise SystemExit("--z is only valid for --layer l4")
    if args.layer == "l4" and args.name is not None:
        raise SystemExit("--name is only valid for --layer l1 or l3")

    if args.layer == "l1":
        rows = l1_all_breakdowns()
        if args.name:
            for row in rows:
                if row["name"] == args.name:
                    l1_print_single(row)
                    return
            raise SystemExit(f"Particle not found: {args.name}")
        l1_print_catalog(rows)
        return

    if args.layer == "l3":
        rows = l3_all_breakdowns()
        if args.name:
            for row in rows:
                if row["name"] == args.name:
                    l3_print_single(row)
                    return
            raise SystemExit(f"Molecule not found: {args.name}")
        l3_print_catalog(rows)
        return

    module = l4_load_generator()
    if args.z is not None:
        if args.z < 1 or args.z > 118:
            raise SystemExit("--z must be in 1..118")
        l4_print_single(l4_element_row(module, args.z))
        return

    rows = [l4_element_row(module, z) for z in range(1, 119)]
    l4_print_catalog(rows)


if __name__ == "__main__":
    main()
