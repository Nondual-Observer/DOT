import TnrFormal.L1
import TnrFormal.L1Bare
import TnrFormal.L1Reference

open TnrFormal

/-!
# DOTheory Lean entry file: L1 bare formulas vs current particle data

Repository:
- https://github.com/Nondual-Observer/DOT
-/

def repoUrl : String :=
  "https://github.com/Nondual-Observer/DOT"

def allParticles : List ParticleName := [
  .electron, .muon, .tau,
  .upQuark, .downQuark, .strangeQuark, .charmQuark, .bottomQuark, .topQuark,
  .pionZero, .kaonPlus, .kaonZero, .dMesonZero, .dMesonPlus, .bMesonZero, .bsMesonZero,
  .proton, .neutron, .lambda, .sigmaPlus, .omegaMinus,
  .wBoson, .zBoson, .higgs
]

def highlightedParticles : List ParticleName := [
  .electron, .muon, .downQuark, .strangeQuark, .sigmaPlus, .higgs
]

def bareSummaryLines : List String := [
  "--- Bare-layer summary ---",
  "Coefficient grammar: minimal low-prime packets, dominated by 2 and 3, with sparse 7 and 17 extensions.",
  "Level grammar: one shared spectral invariant γ = √6/9.",
  "Selection rule: each displayed packet is the current minimal bare-family packet used by the registry for its family.",
  "Largest bare drifts appear in deeper γ^3 sectors and composite baryon sectors.",
  "So the weak bare cases are not random: they sit deeper in the hierarchy or carry more composite structure.",
  "Bare-error summary across all 24 particles: mean |error| = 1.6222%, median |error| = 0.6105%, max |error| = 8.5510%."
]

def introLines : List String := [
  "--- DOTheory Lean entry: L1 bare formulas vs current reference data ---",
  s!"Repository       : {repoUrl}",
  s!"Reference dataset: {l1ReferenceDataset}",
  s!"Freshness note   : {l1ReferenceFreshnessNote}",
  "What this file shows:",
  "  1) the bare formula formalized in Lean",
  "  2) the raw mass produced by that bare formula",
  "  3) the current final L1 package value",
  "  4) the current reference mass and uncertainty",
  ""
]

def psLines : List String := [
  "P.S. One more funny thing: the script sort of keeps insisting there should be one more heavy state around there.",
  "Maybe I'm just seeing patterns, but Ω_ccc^{++} is the one it seems to like most.",
  ""
]

def headerForSection (s : String) : List String := [s]

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

def particleReportLines (p : ParticleName) : List String :=
  let ref := l1ReferenceOf p
  let formula := baseMassString p
  [ s!"{ref.displayName} [{ref.category}]"
  , s!"  bare carrier : {formula}"
  , s!"  source law   : {ref.sourceFormula}"
  , s!"  bare mass    : {ref.bareMeV} MeV   (error {ref.bareErrorPct} vs reference)"
  , s!"  final L1     : {ref.finalMeV} MeV   (error {ref.finalErrorPct} vs reference)"
  , s!"  reference    : {ref.referenceMeV} ± {ref.referenceUncMeV} MeV"
  , s!"  dataset      : {l1ReferenceDataset}"
  , ""
  ]

def emitBlock (xs : List String) : IO Unit := do
  for x in xs do
    IO.println x

def emitParticleList (xs : List ParticleName) : IO Unit := do
  for p in xs do
    emitBlock (particleReportLines p)

def main : IO Unit := do
  emitBlock introLines
  emitBlock (headerForSection "Quick highlights:")
  emitParticleList highlightedParticles
  emitBlock psLines
  emitBlock (headerForSection "--- Full 24-particle L1 reference table ---")
  emitParticleList allParticles
  emitBlock bareSummaryLines
  IO.println "--- End of DOTheory L1 reference table ---"
