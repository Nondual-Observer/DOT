import TnrFormal.L1Registry

/-!
# L1Grammar

Grammar-level description of how `δ₀`, `Ω`, and `T` behave along each operator
path.

This module does not assign concrete coefficients. Instead it specifies:
- which series mode a path uses;
- whether a path requires an explicit tail;
- which special factors (`π`, `√6`, `rAvg`) are admissible.

Theory references:
- `docs/prefin/en/DOT_machine_architecture_overview_en.md` (§3; §6; §7)
- `docs/prefin/en/DOT_mathematical_framework_en.md` (§26.2.3; §26.3)
- `docs/prefin/en/DOT_physical_realization_en.md` (§31.1; §31.1.1)
-/

namespace TnrFormal

/-- Symbolic aggregation mode used by `δ₀` and `Ω`. -/
inductive SeriesMode where
  | none
  | zero
  | sum
  | log1p
  deriving Repr, DecidableEq

/-- Non-rational special factors admitted by the current package. -/
inductive SpecialFactor where
  | pi
  | sqrt6
  | rAvg
  deriving Repr, DecidableEq

/-- `δ₀` aggregation mode associated with an operator path. -/
def d0ModeOfPath : OperatorPath → SeriesMode
  | .anchorIdentityDirect => .none
  | .leptonBridgeSingle => .zero
  | .leptonBulkDual => .sum
  | .quarkSeedDual => .sum
  | .mesonNeutralTailClosure => .sum
  | .mesonChargedTailClosure => .sum
  | .mesonStrangeTailClosure => .sum
  | .baryonProtonSingleLift => .log1p
  | .baryonNeutronShadowTail => .log1p
  | .baryonLambdaTailClosure => .sum
  | .baryonSigmaDualLift => .sum
  | .baryonBulkDual => .sum
  | .bosonGaugeDual => .sum
  | .bosonGaugeTailClosure => .sum
  | .bosonScalarDual => .sum

/-- `Ω` aggregation mode associated with an operator path. -/
def omegaModeOfPath : OperatorPath → SeriesMode
  | .anchorIdentityDirect => .none
  | .leptonBridgeSingle => .log1p
  | .leptonBulkDual => .sum
  | .quarkSeedDual => .sum
  | .mesonNeutralTailClosure => .sum
  | .mesonChargedTailClosure => .sum
  | .mesonStrangeTailClosure => .sum
  | .baryonProtonSingleLift => .zero
  | .baryonNeutronShadowTail => .zero
  | .baryonLambdaTailClosure => .sum
  | .baryonSigmaDualLift => .sum
  | .baryonBulkDual => .sum
  | .bosonGaugeDual => .sum
  | .bosonGaugeTailClosure => .sum
  | .bosonScalarDual => .sum

/-- Whether a path requires an explicit tail layer. -/
def pathUsesTail : OperatorPath → Bool
  | .anchorIdentityDirect => false
  | .leptonBridgeSingle => false
  | .leptonBulkDual => false
  | .quarkSeedDual => false
  | .mesonNeutralTailClosure => true
  | .mesonChargedTailClosure => true
  | .mesonStrangeTailClosure => true
  | .baryonProtonSingleLift => false
  | .baryonNeutronShadowTail => true
  | .baryonLambdaTailClosure => true
  | .baryonSigmaDualLift => false
  | .baryonBulkDual => false
  | .bosonGaugeDual => false
  | .bosonGaugeTailClosure => true
  | .bosonScalarDual => false

/-- Special factors admitted for a given path family. -/
def pathSpecials : OperatorPath → List SpecialFactor
  | .anchorIdentityDirect => []
  | .leptonBridgeSingle => []
  | .leptonBulkDual => []
  | .quarkSeedDual => [.pi, .rAvg]
  | .mesonNeutralTailClosure => []
  | .mesonChargedTailClosure => []
  | .mesonStrangeTailClosure => [.pi]
  | .baryonProtonSingleLift => []
  | .baryonNeutronShadowTail => []
  | .baryonLambdaTailClosure => [.sqrt6]
  | .baryonSigmaDualLift => []
  | .baryonBulkDual => []
  | .bosonGaugeDual => []
  | .bosonGaugeTailClosure => []
  | .bosonScalarDual => [.sqrt6]

theorem anchor_path_has_no_series :
    d0ModeOfPath .anchorIdentityDirect = .none ∧
    omegaModeOfPath .anchorIdentityDirect = .none := by
  constructor <;> rfl

theorem tail_closure_paths_use_tail :
    pathUsesTail .mesonNeutralTailClosure = true ∧
    pathUsesTail .mesonChargedTailClosure = true ∧
    pathUsesTail .mesonStrangeTailClosure = true := by
  constructor
  · rfl
  constructor
  · rfl
  · rfl

end TnrFormal
