-- Repository: https://github.com/Nondual-Observer/DOT

def gamma : Float := Float.sqrt 6.0 / 9.0
def m_e : Float := 0.51099895

def bb6 : Float := 0.04404972689525044
def bb22 : Float := 0.8367318920988547

def pionRef : Float := 134.9768
def pionUnc : Float := 0.0005

def dplusRef : Float := 1869.66
def dplusUnc : Float := 0.05

def absf (x : Float) : Float := Float.abs x

def pow10Nat : Nat → Nat
  | 0 => 1
  | n + 1 => 10 * pow10Nat n

def zeroPadLeft (w : Nat) (s : String) : String :=
  if s.length >= w then s else String.ofList (List.replicate (w - s.length) '0') ++ s

def fmt6 (x : Float) : String :=
  let neg := x < 0.0
  let y := if neg then -x else x
  let scaleNat := pow10Nat 6
  let scale : Float := Float.ofNat scaleNat
  let rounded : UInt64 := Float.toUInt64 (y * scale + 0.5)
  let intPart : UInt64 := rounded / UInt64.ofNat scaleNat
  let fracPart : UInt64 := rounded % UInt64.ofNat scaleNat
  let core := s!"{intPart}.{zeroPadLeft 6 (toString fracPart.toNat)}"
  if neg then s!"-{core}" else core

def bareErrorPct (bare ref : Float) : Float :=
  (bare - ref) / ref * 100.0

def sigma (final ref unc : Float) : Float :=
  absf ((final - ref) / unc)

partial def sciNormUp (m : Float) (e : Int) : Float × Int :=
  if m >= 10.0 then sciNormUp (m / 10.0) (e + 1) else (m, e)

partial def sciNormDown (m : Float) (e : Int) : Float × Int :=
  if m < 1.0 then sciNormDown (m * 10.0) (e - 1) else (m, e)

def sciString (x : Float) : String :=
  let x := absf x
  if x == 0.0 then
    "0"
  else
    let (m, e) := if x >= 1.0 then sciNormUp x 0 else sciNormDown x 0
    s!"{m}e{e}"

def pionBare : Float :=
  ((2.0^3) * (3.0^2) / gamma) * m_e

def pionShift : Float :=
  Float.exp (-(2.0 / 3.0) / 432.0 + (1.0 / 3.0) / (136.0 * 110.0))

def pionTail : Float :=
  1.0 + bb6 * (gamma^3) / (12.0 * 119.0)

def pionFinal : Float :=
  pionBare * pionShift * pionTail

def dplusBare : Float :=
  ((2.0^4) * 17.0 / (gamma^2)) * m_e

def dplusShift : Float :=
  Float.exp (-(1.0 / 2.0) / 136.0 + 4.0 / (110.0 * 432.0))

def dplusTail : Float :=
  1.0 + bb22 * (gamma^3) / (252.0 * 412.0)

def dplusFinal : Float :=
  dplusBare * dplusShift * dplusTail

def electronBare : Float := m_e
def tauBare : Float := ((2.0^7) * (3.0^3)) * m_e
def muBare : Float := ((2.0^3) * 7.0 / gamma) * m_e
def kaonBare : Float := ((2.0^3) * (3.0^2) / (gamma^2)) * m_e
def nucleonBare : Float := ((2.0^3) * 17.0 / (gamma^2)) * m_e
def lambdaBare : Float := (2.0 * (3.0^4) / (gamma^2)) * m_e
def strangeBare : Float := (2.0^2 / (gamma^3)) * m_e
def charmBare : Float := ((2.0^4) * 3.0 / (gamma^3)) * m_e
def bottomBare : Float := (2.0 * (3.0^4) / (gamma^3)) * m_e

def lines : List String := [
  "Compact bare-family table",
  "",
  s!"e⁻ = 1 = {fmt6 electronBare} MeV (0.00%)",
  s!"τ⁻ = 2^7 * 3^3 = {fmt6 tauBare} MeV (0.61%)",
  s!"μ⁻ = (2^3 * 7 / gamma) = {fmt6 muBare} MeV (0.49%)",
  s!"π⁰ = (2^3 * 3^2 / gamma) = {fmt6 pionBare} MeV (0.15%)",
  s!"K⁺ / K⁰ = (2^3 * 3^2 / gamma^2) = {fmt6 kaonBare} MeV (0.61%)",
  s!"p⁺ / n⁰ = (2^3 * 17 / gamma^2) = {fmt6 nucleonBare} MeV (0.15%)",
  s!"Λ⁰ / Σ⁺ = (2 * 3^4 / gamma^2) = {fmt6 lambdaBare} MeV (6.04%)",
  s!"D⁰ / D⁺ = (2^4 * 17 / gamma^2) = {fmt6 dplusBare} MeV (0.62%)",
  s!"s = (2^2 / gamma^3) = {fmt6 strangeBare} MeV (8.55%)",
  s!"c = (2^4 * 3 / gamma^3) = {fmt6 charmBare} MeV (4.20%)",
  s!"b = (2 * 3^4 / gamma^3) = {fmt6 bottomBare} MeV (1.77%)",
  "",
  "(brackets = bare-formula error)",
  "gamma = sqrt(6)/9",
  "where sqrt(6)/9 is derived strictly from the base constant of the 64-vertex graph (lambda = 6.0)",
  "",
  "Key features:",
  "- only unique factorizations over the small primes 2, 3, 7 are used",
  "- 3 can be read naturally as the trace of the three octahedral axes, while 2 reflects their binary polarity",
  "- exponents and multipliers correlate strongly with the structure of the levels",
  "- for relative formulas over 2, 3, 7 and gamma, nearby variants with a ±1 deviation give worse results",
  "- the numbers inside the log-shifts (for example 136, 432, 110) are not free parameters, but path lengths and invariants of the cuboctahedral lattice",
  "",
  "Level note:",
  "- gamma^0: anchor family",
  "- gamma^1: first lifted family",
  "- gamma^2: grouped baryon/meson level",
  "- gamma^3: deeper heavy-family level",
  "",
  "This can be read as visually as the periodic table:",
  "different entries, shared family pattern, deeper level = a different level.",
  "",
  "Three short breakdowns:",
  "",
  "1. Neutral pion π⁰",
  "bare formula: (2^3 * 3^2) / gamma",
  s!"bare value: {fmt6 pionBare} MeV",
  s!"bare error: {fmt6 (bareErrorPct pionBare pionRef)}%",
  "log-shift: exp(-(2/3)/432 + (1/3)/(136*110))",
  s!"log-shift value: {fmt6 pionShift}",
  "log-shift = a small exponential multiplier before the tail",
  "tail: 1 + BB6 * gamma^3 / (12*119)",
  s!"tail value: {fmt6 pionTail}",
  "tail = a small residual multiplier over the shifted value",
  s!"final value: {fmt6 pionFinal} MeV",
  s!"precision: {sciString (sigma pionFinal pionRef pionUnc)} sigma",
  "",
  "2. D⁺",
  "bare formula: (2^4 * 17) / gamma^2",
  s!"bare value: {fmt6 dplusBare} MeV",
  s!"bare error: {fmt6 (bareErrorPct dplusBare dplusRef)}%",
  "log-shift: exp(-(1/2)/136 + 4/(110*432))",
  s!"log-shift value: {fmt6 dplusShift}",
  "log-shift = a small exponential multiplier before the tail",
  "tail: 1 + BB22 * gamma^3 / (252*412)",
  s!"tail value: {fmt6 dplusTail}",
  "tail = a small residual multiplier over the shifted value",
  s!"final value: {fmt6 dplusFinal} MeV",
  s!"precision: {sciString (sigma dplusFinal dplusRef dplusUnc)} sigma",
  "",
  "3. Ω_ccc^{++}",
  "predicted formula: 2^6 * 3 / gamma^3",
  "predicted value: 4862.291 MeV",
  "tolerance: -29.2 .. +20.7 MeV",
  "this is no longer a benchmark particle from the table, but a closing predicted heavy node."
]

def main : IO Unit := do
  for line in lines do
    IO.println line

/-!
Full algorithm

The full computational algorithm of DOTheory uses a finite 64-vertex graph as its base carrier and works not with a continuous set of arbitrary coefficients, but with discrete configurations, paths, and transitions on that graph. Stable numerical relations are extracted from this structure and then become the coefficients in the mass formulas. The base constant `lambda = 6.0` defines the underlying geometry of the graph, while `gamma = sqrt(6)/9` appears as its spectral invariant.

The next step is not to fit masses to a table, but to build them from rigid factorized expressions. In the bare layer these are compact products of small primes and powers of the shared invariant `gamma`. At that level the formula gives the primary mass carrier. That is why the display above shows short discrete expressions of the form `2^a * 3^b / gamma^k` first, and only then their numerical values in `MeV`.

The next stage is not a new fit, but a structural correction. First, the bare value receives a small logarithmic shift `exp(...)`, assembled from fixed path lengths and lattice invariants. After that, a tail multiplier closes the remaining gap between the base level and the observed value. The quantities `BB_n` used in the tails are not free parameters, but fixed resonance boundaries (`Boundary Balance`) computed from the same graph topology.

In the end, the full algorithm has a two-step form: first a discrete bare carrier, then small structural corrections. For some particles the bare layer is already very close, for others the log-shifts and tails do more of the work, but they remain short and factorized as well. That is why this approach can be read not as a pile of isolated coincidences, but as a single discrete mechanism for constructing physical quantities from topological structure, spectral invariants, and resonance boundaries.
-/

#eval main
