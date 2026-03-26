/-!
# Paths

This module names the canonical operator paths used by the current symbolic
`L1` law. These are path classes, not yet executable numeric operators.

Theory references:
- `docs/prefin/en/DOT_machine_architecture_overview_en.md` (§3; §6; §7)
- `docs/prefin/en/DOT_mathematical_framework_en.md` (§26.2, §26.3)
- `docs/prefin/en/DOT_physical_realization_en.md` (§30, §31)
-/

namespace TnrFormal

/-- Canonical operator paths of the current `L1` particle layer. -/
inductive OperatorPath where
  | anchorIdentityDirect
  | leptonBridgeSingle
  | leptonBulkDual
  | quarkSeedDual
  | mesonNeutralTailClosure
  | mesonChargedTailClosure
  | mesonStrangeTailClosure
  | baryonProtonSingleLift
  | baryonNeutronShadowTail
  | baryonLambdaTailClosure
  | baryonSigmaDualLift
  | baryonBulkDual
  | bosonGaugeDual
  | bosonGaugeTailClosure
  | bosonScalarDual
  deriving Repr, DecidableEq

/-- Number of canonical operator paths used by the current package. -/
def operatorPathCount : Nat := 15

theorem operator_path_count_is_15 : operatorPathCount = 15 := rfl

end TnrFormal
