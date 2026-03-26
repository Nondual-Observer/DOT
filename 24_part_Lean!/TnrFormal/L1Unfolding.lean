import TnrFormal.L1Tail
import TnrFormal.L1Assembly
import TnrFormal.L1Bare

/-!
# L1Unfolding

Bundle-level assembly of the current symbolic particle law.

This module collects, for each particle, the imported bare family together with
its path, superpath, assembly shape, `δ₀` terms, `Ω` terms, and explicit tail.
It is the closest Lean file to the public statement that each particle is a
finite assembled packet rather than an isolated formula.

Theory references:
- `docs/prefin/en/DOT_machine_architecture_overview_en.md` (§3; §8; §9)
- `docs/prefin/en/DOT_mathematical_framework_en.md` (§26.2; §26.3)
- `docs/prefin/en/DOT_physical_realization_en.md` (§30; §31)
-/

namespace TnrFormal

/--
Full symbolic bundle of one `L1` particle.

This is still a symbolic object: it records what must be assembled, but it does
not numerically evaluate the mass.
-/
structure L1Bundle where
  bareFamily : BareFamily
  path : OperatorPath
  superpath : Superpath
  assembly : AssemblyShape
  d0 : List SymbolicTerm
  omega : List SymbolicTerm
  tail : List SymbolicTerm
  deriving Repr

/--
Canonical symbolic bundle of a particle.

`bundleOf` is the main assembly point of the current Lean package: it gathers
the imported bare family and the three post-basis grammar layers.
-/
def bundleOf : ParticleName → L1Bundle
  | p => {
      bareFamily := bareFamilyOf p
      path := operatorPathOf p
      superpath := superpathOf p
      assembly := assemblyShapeOfSuperpath (superpathOf p)
      d0 := d0TermsOfParticle p
      omega := omegaTermsOfParticle p
      tail := tailTermsOfParticle p
    }

/-- The bundle stores the same path as the particle registry. -/
theorem bundle_path_consistency (p : ParticleName) :
    (bundleOf p).path = operatorPathOf p := by
  rfl

/-- Superpath in the bundle agrees with the path-level lift. -/
theorem bundle_superpath_consistency (p : ParticleName) :
    (bundleOf p).superpath = superpathOfPath ((bundleOf p).path) := by
  simp [bundleOf, superpath_matches_path p]

/-- Assembly shape in the bundle agrees with the recorded superpath. -/
theorem bundle_assembly_consistency (p : ParticleName) :
    (bundleOf p).assembly = assemblyShapeOfSuperpath ((bundleOf p).superpath) := by
  rfl

/-- Electron is the identity anchor: no shift and no explicit tail. -/
theorem electron_bundle_is_identity :
    (bundleOf .electron).assembly = .identity ∧
    (bundleOf .electron).d0 = [] ∧
    (bundleOf .electron).omega = [] ∧
    (bundleOf .electron).tail = [] := by
  constructor
  · rfl
  constructor
  · rfl
  constructor
  · rfl
  · rfl

/-- Neutron is one of the current packets with an explicit tail layer. -/
theorem neutron_bundle_uses_tail :
    (bundleOf .neutron).tail.length = 1 := by
  rfl

/-- Proton lives in the shifted assembly family. -/
theorem proton_bundle_is_shifted :
    (bundleOf .proton).assembly = .shifted := by
  rfl

end TnrFormal
