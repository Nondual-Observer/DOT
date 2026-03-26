import TnrFormal.L1

/-!
# L1Assembly

This module records the three assembly shapes used in the current `L1` law:
identity, shifted, and tailed. It is a symbolic classification layer over the
particle/superpath registry.

Theory references:
- `docs/prefin/en/DOT_machine_architecture_overview_en.md` (§3; §6; §7)
- `docs/prefin/en/DOT_physical_realization_en.md` (§30; §31.1)
-/

namespace TnrFormal

/-- Coarse assembly shape of a particle profile. -/
inductive AssemblyShape where
  | identity
  | shifted
  | tailed
  deriving Repr, DecidableEq

/-- Assembly shape implied by a superpath class. -/
def assemblyShapeOfSuperpath : Superpath → AssemblyShape
  | .baseIdentity => .identity
  | .singleLift => .shifted
  | .dualShiftFamily => .shifted
  | .tailClosureFamily => .tailed
  | .shadowTailFamily => .tailed

/-- Whether the given superpath uses the shift/closure field. -/
def usesShift : Superpath → Bool
  | .baseIdentity => false
  | .singleLift => true
  | .dualShiftFamily => true
  | .tailClosureFamily => true
  | .shadowTailFamily => true

/-- Whether the given superpath uses an explicit tail layer. -/
def usesTail : Superpath → Bool
  | .baseIdentity => false
  | .singleLift => false
  | .dualShiftFamily => false
  | .tailClosureFamily => true
  | .shadowTailFamily => true

theorem base_identity_has_no_shift_or_tail :
    usesShift .baseIdentity = false ∧ usesTail .baseIdentity = false := by
  constructor <;> rfl

theorem tail_superpaths_use_tail :
    usesTail .tailClosureFamily = true ∧ usesTail .shadowTailFamily = true := by
  constructor <;> rfl

end TnrFormal
