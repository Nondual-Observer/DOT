/-!
# Prelude

This module fixes the lowest declarative vocabulary shared by the rest of the
Lean package:
- layer names;
- the lower floor ladder `0 -> 1 -> 2 -> 6 -> 12 -> 8`;
- the visible/shadow structural packets `24 / 48 / 23 / 47`.

These values are named here as canonical vocabulary. Their deeper derivation is
described in the theory corpus and is not yet implemented as an executable
proof layer in Lean.

Theory references:
- `docs/prefin/en/DOT_machine_architecture_overview_en.md` (§§1-4, §8)
- `docs/prefin/en/DOT_mathematical_framework_en.md` (§20, §21, §26.2)
-/

namespace TnrFormal

/-- High-level layer labels used by the current package. -/
inductive Layer where
  | L0
  | L1
  | L2
  | L21
  | L3
  | L4
  deriving Repr, DecidableEq

/-- Nodes of the lower floor ladder `0 -> 1 -> 2 -> 6 -> 12 -> 8`. -/
inductive FloorNode where
  | z0
  | z1
  | z2
  | z6
  | z12
  | z8
  deriving Repr, DecidableEq

/-- Canonical visible/shadow packets used by the current package. -/
inductive StructuralPacket where
  | visible24
  | shell48
  | shadow23
  | complement47
  deriving Repr, DecidableEq

/-- Numeric values of the lower floor ladder nodes. -/
def floorValue : FloorNode → Nat
  | .z0 => 0
  | .z1 => 1
  | .z2 => 2
  | .z6 => 6
  | .z12 => 12
  | .z8 => 8

/-- Numeric values of the canonical structural packets. -/
def packetValue : StructuralPacket → Nat
  | .visible24 => 24
  | .shell48 => 48
  | .shadow23 => 23
  | .complement47 => 47

end TnrFormal
