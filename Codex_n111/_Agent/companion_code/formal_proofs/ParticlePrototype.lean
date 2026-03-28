import TnrFormal.L1
import TnrFormal.L1Bare
import TnrFormal.L1Reference

open TnrFormal

/-!
# DOTheory Lean entry file: L1 bare formulas vs current particle data

Repository:
- https://github.com/Nondual-Observer/DOT

If someone opens only one Lean file in this repository, this should be the
entry point.

What this file shows, in one place:
- the bare carrier formula used for each canonical `L1` particle;
- the current bare numerical mass coming directly from that carrier;
- the current final `L1` mass after the imported correction / tail layer;
- the current reference mass and uncertainty used by the package;
- the current percentage error of the bare layer and the final layer.

What is actually formalized here:
- the symbolic `L1` particle registry;
- the bare family assignment of each particle;
- the bare carrier packet `(C, gamma-power)` for each family.

What is *not* yet derived from first principles inside this single Lean file:
- the full numerical correction / tail layer;
- the derivation of all packet numerators from an explicit graph construction;
- the current experimental reference table itself.

So the reading is deliberately honest:
- `bare mass` = what the Lean-visible bare carrier gives on its own;
- `final L1`   = what the current package gives after the imported correction layer;
- `reference`  = the current external target used by the package.

This is useful for a skeptical reader because it separates three different
things that often get mixed together:
- the symbolic carrier law;
- the raw numerical output of that carrier;
- the final fitted/closed package value.

Run:
- `lake build particle_prototype`
- `lake env lean --run ParticlePrototype.lean`
-/

/-- Repository URL shown in the demo header. -/
def repoUrl : String :=
  "https://github.com/Nondual-Observer/DOT"

/-- List of all 24 canonical particles in the L1 registry. -/
def allParticles : List ParticleName := [
  .electron, .muon, .tau,
  .upQuark, .downQuark, .strangeQuark, .charmQuark, .bottomQuark, .topQuark,
  .pionZero, .kaonPlus, .kaonZero, .dMesonZero, .dMesonPlus, .bMesonZero, .bsMesonZero,
  .proton, .neutron, .lambda, .sigmaPlus, .omegaMinus,
  .wBoson, .zBoson, .higgs
]

/--
Selected examples shown first so that a reader immediately sees the spread:
- exact anchor case;
- good bridge case;
- heavy raw-error quark cases;
- heavy raw-error baryon case;
- high-energy boson case.
-/
def highlightedParticles : List ParticleName := [
  .electron, .muon, .downQuark, .strangeQuark, .sigmaPlus, .higgs
]

/-- Computes the base representation string for a particle. -/
def baseMassString (p : ParticleName) : String :=
  let fam := bareFamilyOf p
  let c := carrierCOf fam
  let k := gammaPowerOf fam
  if k = 0 then
    s!"C = {c}, depth (k) = {k}  =>  M_bare = {c}·m_e"
  else if k > 0 then
    s!"C = {c}, depth (k) = {k}  =>  M_bare = {c}·γ^{k}·m_e"
  else
    let absK : Nat := Int.natAbs k
    if absK = 1 then
      s!"C = {c}, depth (k) = {k}  =>  M_bare = {c}/γ·m_e"
    else
      s!"C = {c}, depth (k) = {k}  =>  M_bare = {c}/γ^{absK}·m_e"

/-- Human-facing multiline report for one particle. -/
def particleReportString (p : ParticleName) : String :=
  let ref := l1ReferenceOf p
  let formula := baseMassString p
  String.intercalate "\n"
    [ s!"{ref.displayName} [{ref.category}]"
    , s!"  bare carrier : {formula}"
    , s!"  source law   : {ref.sourceFormula}"
    , s!"  bare mass    : {ref.bareMeV} MeV   (error {ref.bareErrorPct} vs reference)"
    , s!"  final L1     : {ref.finalMeV} MeV   (error {ref.finalErrorPct} vs reference)"
    , s!"  reference    : {ref.referenceMeV} ± {ref.referenceUncMeV} MeV"
    , s!"  dataset      : {l1ReferenceDataset}"
    ]

def main : IO Unit := do
  IO.println "--- DOTheory Lean entry: L1 bare formulas vs current reference data ---"
  IO.println s!"Repository       : {repoUrl}"
  IO.println s!"Reference dataset: {l1ReferenceDataset}"
  IO.println s!"Freshness note   : {l1ReferenceFreshnessNote}"
  IO.println "What this file shows:"
  IO.println "  1) the bare formula formalized in Lean"
  IO.println "  2) the raw mass produced by that bare formula"
  IO.println "  3) the current final L1 package value"
  IO.println "  4) the current reference mass and uncertainty"
  IO.println ""
  IO.println "Quick highlights:"
  for p in highlightedParticles do
    IO.println (particleReportString p)
    IO.println ""
  IO.println "P.S. One more funny thing: the script sort of keeps insisting there should be one more heavy state around there."
  IO.println "Maybe I'm just seeing patterns, but Ω_ccc^{++} is the one it seems to like most."
  IO.println ""
  IO.println "--- Full 24-particle L1 reference table ---"
  for p in allParticles do
    IO.println (particleReportString p)
    IO.println ""
  IO.println "--- End of DOTheory L1 reference table ---"
