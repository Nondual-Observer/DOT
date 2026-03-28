#!/usr/bin/env python3
"""
Layer-prefixed compatibility entrypoint for the L4 same-shell screening extractor.

Canonical naming uses the `tnr_l4_*` prefix. The implementation still lives in
the shared extractor module so older imports remain valid while the public
layout becomes easier to read.
"""

from tnr_same_shell_screening_extractor import *  # noqa: F401,F403


if __name__ == "__main__":
    from tnr_same_shell_screening_extractor import main

    main()
