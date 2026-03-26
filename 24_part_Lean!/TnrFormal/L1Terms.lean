import TnrFormal.L1Grammar

/-!
# L1Terms

Alphabet-level metadata for the term system used by the current `L1` law.

This module names:
- the finite `BB_k` alphabet currently used by Lean;
- coarse term categories (`rational`, `bbCarrier`, `specialCarrier`);
- which alphabets are admissible on each operator path.

Theory references:
- `docs/prefin/en/DOT_mathematical_framework_en.md` (§24; §26.2.3; §26.3)
- `docs/prefin/en/DOT_physical_realization_en.md` (§31; tail algebra)
-/

namespace TnrFormal

/-- Finite `BB_k` alphabet currently used by the symbolic `L1` layer. -/
inductive BBTag where
  | bb2
  | bb3
  | bb4
  | bb5
  | bb6
  | bb7
  | bb10
  | bb11
  | bb14
  | bb15
  | bb19
  | bb22
  deriving Repr, DecidableEq

/-- Coarse term classes used by the current package. -/
inductive TermAlphabet where
  | rational
  | bbCarrier
  | specialCarrier
  deriving Repr, DecidableEq

/-- `BB_k` tags currently used by the `δ₀` layer. -/
def d0UsedBBTags : List BBTag :=
  [.bb2, .bb3, .bb5, .bb7, .bb10]

/-- `BB_k` tags currently used by the `Ω` layer. -/
def omegaUsedBBTags : List BBTag :=
  [.bb5, .bb7, .bb11]

/-- `BB_k` tags currently used by the explicit tail layer. -/
def tailUsedBBTags : List BBTag :=
  [.bb3, .bb4, .bb6, .bb11, .bb14, .bb15, .bb19, .bb22]

/-- Coarse term alphabet admitted by each operator path. -/
def termAlphabetOfPath : OperatorPath → List TermAlphabet
  | .anchorIdentityDirect => []
  | .leptonBridgeSingle => [.bbCarrier]
  | .leptonBulkDual => [.rational]
  | .quarkSeedDual => [.rational, .specialCarrier]
  | .mesonNeutralTailClosure => [.rational, .bbCarrier]
  | .mesonChargedTailClosure => [.rational, .bbCarrier]
  | .mesonStrangeTailClosure => [.rational, .bbCarrier, .specialCarrier]
  | .baryonProtonSingleLift => [.bbCarrier]
  | .baryonNeutronShadowTail => [.rational, .bbCarrier]
  | .baryonLambdaTailClosure => [.rational, .bbCarrier, .specialCarrier]
  | .baryonSigmaDualLift => [.rational]
  | .baryonBulkDual => [.rational]
  | .bosonGaugeDual => [.rational]
  | .bosonGaugeTailClosure => [.rational, .bbCarrier]
  | .bosonScalarDual => [.rational, .specialCarrier]

theorem tail_bb_tag_count : tailUsedBBTags.length = 8 := rfl

theorem d0_bb_tag_count : d0UsedBBTags.length = 5 := rfl

end TnrFormal
