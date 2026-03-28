#!/usr/bin/env python3
"""
Layer-prefixed compatibility entrypoint for the L4 screening family audit.

Canonical naming uses the `tnr_l4_*` prefix. The implementation still lives in
the shared audit module so older imports remain valid while the public layout
becomes easier to read.
"""

from tnr_screening_family_audit import *  # noqa: F401,F403


if __name__ == "__main__":
    from tnr_screening_family_audit import main

    main()
