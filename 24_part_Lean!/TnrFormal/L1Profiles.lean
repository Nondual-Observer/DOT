import TnrFormal.L1Terms

/-!
# L1Profiles

This module records the dominant profile/axis of each operator path. It is a
semantic classifier for the current `L1` symbolic law.

Theory references:
- `docs/prefin/en/DOT_machine_architecture_overview_en.md` (§3; §6; §7)
- `docs/prefin/en/DOT_physical_realization_en.md` (§31)
-/

namespace TnrFormal

/-- Dominant semantic axis of a path family in the current `L1` package. -/
inductive DominantAxis where
  | baseAlphabet
  | duplicationTransfer
  | continuationMellin
  | twistClosure
  deriving Repr, DecidableEq

/-- Dominant profile/axis associated with an operator path. -/
def dominantAxisOfPath : OperatorPath → DominantAxis
  | .anchorIdentityDirect => .baseAlphabet
  | .baryonProtonSingleLift => .duplicationTransfer
  | .leptonBridgeSingle => .continuationMellin
  | .leptonBulkDual => .continuationMellin
  | .quarkSeedDual => .continuationMellin
  | .baryonSigmaDualLift => .continuationMellin
  | .baryonBulkDual => .continuationMellin
  | .bosonGaugeDual => .continuationMellin
  | .bosonScalarDual => .continuationMellin
  | .mesonNeutralTailClosure => .twistClosure
  | .mesonChargedTailClosure => .twistClosure
  | .mesonStrangeTailClosure => .twistClosure
  | .baryonNeutronShadowTail => .twistClosure
  | .baryonLambdaTailClosure => .twistClosure
  | .bosonGaugeTailClosure => .twistClosure

theorem quark_path_is_continuation :
    dominantAxisOfPath .quarkSeedDual = .continuationMellin := rfl

theorem neutron_path_is_twist :
    dominantAxisOfPath .baryonNeutronShadowTail = .twistClosure := rfl

end TnrFormal
