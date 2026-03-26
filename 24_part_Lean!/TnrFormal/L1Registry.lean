import TnrFormal.L1Assembly

/-!
# L1Registry

This module groups particles by their assembly family. It is a compact registry
view over the current `L1` layer and is useful for diagnostics, proofs of
counts, and package navigation.

Theory references:
- `docs/prefin/en/DOT_machine_architecture_overview_en.md` (§3; §8; §9)
- `docs/prefin/en/DOT_physical_realization_en.md` (§30; §31)
-/

namespace TnrFormal

/-- Particles with pure basis identity and no shift/tail. -/
def baseIdentityParticles : List ParticleName :=
  [.electron]

/-- Particles with one explicit lift above the basis. -/
def singleLiftParticles : List ParticleName :=
  [.muon, .proton]

/-- Particles using the dual-shift family without explicit tail. -/
def dualShiftParticles : List ParticleName :=
  [.tau, .upQuark, .downQuark, .strangeQuark, .charmQuark, .bottomQuark, .topQuark,
   .sigmaPlus, .omegaMinus, .wBoson, .higgs]

/-- Particles using explicit tail completion. -/
def tailClosureParticles : List ParticleName :=
  [.pionZero, .kaonPlus, .kaonZero, .dMesonZero, .dMesonPlus, .bMesonZero, .bsMesonZero,
   .lambda, .zBoson]

/-- Particles using the shadow-tail family. -/
def shadowTailParticles : List ParticleName :=
  [.neutron]

theorem base_identity_particle_count : baseIdentityParticles.length = 1 := rfl
theorem single_lift_particle_count : singleLiftParticles.length = 2 := rfl
theorem dual_shift_particle_count : dualShiftParticles.length = 11 := rfl
theorem tail_closure_particle_count : tailClosureParticles.length = 9 := rfl
theorem shadow_tail_particle_count : shadowTailParticles.length = 1 := rfl

end TnrFormal
