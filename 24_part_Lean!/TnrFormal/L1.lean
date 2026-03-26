import TnrFormal.Prelude
import TnrFormal.Octahedron
import TnrFormal.Carriers
import TnrFormal.Paths

/-!
# L1

Central symbolic registry of the current particle layer.

This module does three things:
- names the current 24 particle readouts;
- assigns each particle a superpath, a bare family, and an operator path;
- relates path-level and superpath-level classifications.

This is a symbolic ontology/grammar layer. It does **not** perform numeric mass
evaluation.

Theory references:
- `docs/prefin/en/DOT_machine_architecture_overview_en.md` (§3; §8; §9)
- `docs/prefin/en/DOT_mathematical_framework_en.md` (§26.2, §26.3)
- `docs/prefin/en/DOT_physical_realization_en.md` (§29.1; §30; §31)
-/

namespace TnrFormal

/-- Coarse operator classes of the current particle layer. -/
inductive OperatorClass where
  | familyAnchor
  | familySingleShift
  | familyDualShift
  | familyTail
  | familyTailCompletion
  deriving Repr, DecidableEq

/-- Coarse superpaths used to compress the particle layer. -/
inductive Superpath where
  | baseIdentity
  | singleLift
  | dualShiftFamily
  | tailClosureFamily
  | shadowTailFamily
  deriving Repr, DecidableEq

/-- Canonical 24-particle registry used by the current Lean package. -/
inductive ParticleName where
  | electron
  | muon
  | tau
  | upQuark
  | downQuark
  | strangeQuark
  | charmQuark
  | bottomQuark
  | topQuark
  | pionZero
  | kaonPlus
  | kaonZero
  | dMesonZero
  | dMesonPlus
  | bMesonZero
  | bsMesonZero
  | proton
  | neutron
  | lambda
  | sigmaPlus
  | omegaMinus
  | wBoson
  | zBoson
  | higgs
  deriving Repr, DecidableEq

/-- Number of particles in the current symbolic `L1` package. -/
def particleCount : Nat := 24

/-- Superpath class of each particle. See overview §3 and physical realization §30-§31. -/
def superpathOf : ParticleName → Superpath
  | .electron => .baseIdentity
  | .muon => .singleLift
  | .tau => .dualShiftFamily
  | .upQuark => .dualShiftFamily
  | .downQuark => .dualShiftFamily
  | .strangeQuark => .dualShiftFamily
  | .charmQuark => .dualShiftFamily
  | .bottomQuark => .dualShiftFamily
  | .topQuark => .dualShiftFamily
  | .pionZero => .tailClosureFamily
  | .kaonPlus => .tailClosureFamily
  | .kaonZero => .tailClosureFamily
  | .dMesonZero => .tailClosureFamily
  | .dMesonPlus => .tailClosureFamily
  | .bMesonZero => .tailClosureFamily
  | .bsMesonZero => .tailClosureFamily
  | .proton => .singleLift
  | .neutron => .shadowTailFamily
  | .lambda => .tailClosureFamily
  | .sigmaPlus => .dualShiftFamily
  | .omegaMinus => .dualShiftFamily
  | .wBoson => .dualShiftFamily
  | .zBoson => .tailClosureFamily
  | .higgs => .dualShiftFamily

/-- Operator class associated with a superpath. -/
def operatorClassOfSuperpath : Superpath → OperatorClass
  | .baseIdentity => .familyAnchor
  | .singleLift => .familySingleShift
  | .dualShiftFamily => .familyDualShift
  | .tailClosureFamily => .familyTailCompletion
  | .shadowTailFamily => .familyTail

/--
Bare-family assignment for each particle.

Important boundary:
this is a canonical registry imported into Lean; the current package does not
yet derive these families from an explicit `K(2,2,2)` proof layer.
-/
def bareFamilyOf : ParticleName → BareFamily
  | .electron => .anchor
  | .muon => .muonBridge
  | .tau => .tauBulk
  | .upQuark => .uSeed
  | .downQuark => .dSeed
  | .strangeQuark => .sSeed
  | .charmQuark => .cSeed
  | .bottomQuark => .bSeed
  | .topQuark => .tSeed
  | .pionZero => .pionSeed
  | .kaonPlus => .kaonSeed
  | .kaonZero => .kaonSeed
  | .dMesonZero => .dMesonSeed
  | .dMesonPlus => .dMesonSeed
  | .bMesonZero => .bMesonSeed
  | .bsMesonZero => .bMesonSeed
  | .proton => .nucleonSeed
  | .neutron => .nucleonSeed
  | .lambda => .lambdaSigmaSeed
  | .sigmaPlus => .lambdaSigmaSeed
  | .omegaMinus => .omegaSeed
  | .wBoson => .wSeed
  | .zBoson => .zSeed
  | .higgs => .higgsSeed

/-- Fine operator path assigned to each particle. -/
def operatorPathOf : ParticleName → OperatorPath
  | .electron => .anchorIdentityDirect
  | .muon => .leptonBridgeSingle
  | .tau => .leptonBulkDual
  | .upQuark => .quarkSeedDual
  | .downQuark => .quarkSeedDual
  | .strangeQuark => .quarkSeedDual
  | .charmQuark => .quarkSeedDual
  | .bottomQuark => .quarkSeedDual
  | .topQuark => .quarkSeedDual
  | .pionZero => .mesonNeutralTailClosure
  | .kaonPlus => .mesonChargedTailClosure
  | .kaonZero => .mesonNeutralTailClosure
  | .dMesonZero => .mesonNeutralTailClosure
  | .dMesonPlus => .mesonChargedTailClosure
  | .bMesonZero => .mesonNeutralTailClosure
  | .bsMesonZero => .mesonStrangeTailClosure
  | .proton => .baryonProtonSingleLift
  | .neutron => .baryonNeutronShadowTail
  | .lambda => .baryonLambdaTailClosure
  | .sigmaPlus => .baryonSigmaDualLift
  | .omegaMinus => .baryonBulkDual
  | .wBoson => .bosonGaugeDual
  | .zBoson => .bosonGaugeTailClosure
  | .higgs => .bosonScalarDual

/-- Projection from fine path classes back to coarse superpaths. -/
def superpathOfPath : OperatorPath → Superpath
  | .anchorIdentityDirect => .baseIdentity
  | .leptonBridgeSingle => .singleLift
  | .leptonBulkDual => .dualShiftFamily
  | .quarkSeedDual => .dualShiftFamily
  | .mesonNeutralTailClosure => .tailClosureFamily
  | .mesonChargedTailClosure => .tailClosureFamily
  | .mesonStrangeTailClosure => .tailClosureFamily
  | .baryonProtonSingleLift => .singleLift
  | .baryonNeutronShadowTail => .shadowTailFamily
  | .baryonLambdaTailClosure => .tailClosureFamily
  | .baryonSigmaDualLift => .dualShiftFamily
  | .baryonBulkDual => .dualShiftFamily
  | .bosonGaugeDual => .dualShiftFamily
  | .bosonGaugeTailClosure => .tailClosureFamily
  | .bosonScalarDual => .dualShiftFamily

theorem superpath_matches_path (p : ParticleName) :
    superpathOf p = superpathOfPath (operatorPathOf p) := by
  cases p <;> rfl

theorem particle_count_is_24 : particleCount = 24 := rfl

end TnrFormal
