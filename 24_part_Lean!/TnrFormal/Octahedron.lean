import TnrFormal.Prelude

/-!
# Octahedron

This module stores the current octahedral vocabulary used by the package:
- port classes;
- topology regimes;
- the visible/shadow seed packet.

Important boundary:
the explicit graph object `K(2,2,2)` is **not** constructed here. This file
only provides the declarative language that later symbolic layers use.

Theory references:
- `docs/prefin/en/DOT_machine_architecture_overview_en.md` (§4.4, §5, §8)
- `docs/prefin/en/DOT_mathematical_framework_en.md` (§20; §24; §26.2)
-/

namespace TnrFormal

/-- The four canonical port classes used in the current octahedral reading. -/
inductive OctahedralPort where
  | northSouth
  | eastWest
  | frontBack
  | diagonalShell
  deriving Repr, DecidableEq

/-- Coarse topology regimes used by the current package. -/
inductive TopologyRegime where
  | discreteCore
  | bridge
  | closure
  deriving Repr, DecidableEq

/-- Canonical visible/shadow seed packet of the octahedral carrier. -/
def visibleShadowSeed : List StructuralPacket :=
  [.visible24, .shell48, .shadow23, .complement47]

/-- The current package works with four octahedral port classes. -/
def octahedralPortCount : Nat := 4

end TnrFormal
