import TnrFormal.L1Profiles

/-!
# L1Delta

Symbolic term layer for the post-basis particle grammar.

This module defines the finite term language used by the current Lean package
for:
- `δ₀`, the local shift layer;
- `Ω`, the closure/continuation field;
- the path-level predicate saying whether a family admits parametric shift.

The current package records these terms symbolically. It does **not** derive
their coefficients from an explicit octahedral proof layer inside Lean.

Theory references:
- `docs/prefin/en/DOT_machine_architecture_overview_en.md` (§3; §6; §7; §8)
- `docs/prefin/en/DOT_mathematical_framework_en.md` (§24; §26.2; §26.2.3; §26.3)
- `docs/prefin/en/DOT_physical_realization_en.md` (§31; §31.1; §31.1.1)
-/

namespace TnrFormal

/-- Symbolic form used by a term in `δ₀` or `Ω`. -/
inductive ShiftForm where
  | ratio
  | bbRatio
  | piRatio
  | sqrt6Ratio
  | ravgGammaRatio
  | alphaCouplingSq
  deriving Repr, DecidableEq

/--
One symbolic term of the `δ₀` / `Ω` grammar.

`coeffNum / coeffDen` stores the visible rational front coefficient, while
`denoms` stores additional structural denominators that remain explicit in the
registry. This keeps the symbolic layer readable and closer to the theory
presentation.
-/
structure SymbolicTerm where
  form : ShiftForm
  coeffNum : Int
  coeffDen : Nat := 1
  bb : Option BBTag := none
  alphaPower : Nat := 0
  gammaPower : Int := 0
  denoms : List Nat := []
  deriving Repr, DecidableEq

/-- Pure rational term. -/
def ratio (n : Int) (d : Nat := 1) (denoms : List Nat := []) : SymbolicTerm :=
  { form := .ratio, coeffNum := n, coeffDen := d, denoms := denoms }

/-- `BB_k`-weighted rational term, optionally with `α`/`γ` exponents. -/
def bbRatio (bb : Option BBTag) (n : Int) (d : Nat := 1)
    (alphaPower : Nat := 0) (gammaPower : Int := 0)
    (denoms : List Nat := []) : SymbolicTerm :=
  { form := .bbRatio
    coeffNum := n
    coeffDen := d
    bb := bb
    alphaPower := alphaPower
    gammaPower := gammaPower
    denoms := denoms }

/-- Rational term multiplied by `π`. -/
def piRatio (n : Int) (d : Nat := 1) (denoms : List Nat := []) : SymbolicTerm :=
  { form := .piRatio, coeffNum := n, coeffDen := d, denoms := denoms }

/-- Rational term multiplied by `√6`. -/
def sqrt6Ratio (n : Int) (d : Nat := 1) (denoms : List Nat := []) : SymbolicTerm :=
  { form := .sqrt6Ratio, coeffNum := n, coeffDen := d, denoms := denoms }

/-- Rational term multiplied by the `r_avg * γ` carrier factor. -/
def ravgGammaRatio (n : Int) (d : Nat := 1) (denoms : List Nat := []) : SymbolicTerm :=
  { form := .ravgGammaRatio, coeffNum := n, coeffDen := d, denoms := denoms }

/-- Rational term multiplied by `α_coupling²`. -/
def alphaCouplingSq (n : Int) (d : Nat := 1) : SymbolicTerm :=
  { form := .alphaCouplingSq, coeffNum := n, coeffDen := d }

/--
Symbolic `δ₀` terms for each particle.

Composite denominators are factorized inline so the registry stays readable as a
finite packet alphabet:
- `3136 = 2^6 * 7^2`
- `39 = 3 * 13`
- `12 = 2^2 * 3`
- `162 = 2 * 3^4`
- `56 = 2^3 * 7`
- `110 = 2 * 5 * 11`
- `432 = 2^4 * 3^3`
- `136 = 2^3 * 17`
- `81 = 3^4`
- `684 = 2^2 * 3^2 * 19`
- `120 = 2^3 * 3 * 5`
- `9 = 3^2`
- `48 = 2^4 * 3`
- `576 = 2^6 * 3^2`
- `1728 = 2^6 * 3^3`
-/
def d0TermsOfParticle : ParticleName → List SymbolicTerm
  | .electron => []
  | .muon => []
  | .tau => [ratio 2 3 [110]]                         -- 110 = 2 * 5 * 11
  | .upQuark => [ratio 1 1 [3136]]                   -- 3136 = 2^6 * 7^2
  | .downQuark => [ratio (-1) 4 [39]]                -- 39 = 3 * 13
  | .strangeQuark => [ratio (-1) 1 [12]]             -- 12 = 2^2 * 3
  | .charmQuark => [ratio (-1) 1 [162]]              -- 162 = 2 * 3^4
  | .bottomQuark => [ratio 1 1 [56]]                 -- 56 = 2^3 * 7
  | .topQuark => [ratio (-1) 1 [110]]                -- 110 = 2 * 5 * 11
  | .pionZero => [ratio (-2) 3 [432]]                -- 432 = 2^4 * 3^3
  | .kaonPlus => [ratio (-2) 3 [110]]                -- 110 = 2 * 5 * 11
  | .kaonZero => [ratio 1 4 [136]]                   -- 136 = 2^3 * 17
  | .dMesonZero => [ratio (-2) 3 [110]]              -- 110 = 2 * 5 * 11
  | .dMesonPlus => [ratio (-1) 2 [136]]              -- 136 = 2^3 * 17
  | .bMesonZero => [ratio 1 1 [81]]                  -- 81 = 3^4
  | .bsMesonZero => [piRatio 1 1 [110]]              -- 110 = 2 * 5 * 11
  | .proton =>
      [ bbRatio (some .bb7) (-1) 1 1 0 [7]
      , bbRatio (some .bb5) (-1) 1 2 0 [120, 17]     -- 120 = 2^3 * 3 * 5; 17 prime
      , bbRatio (some .bb3) 1 1 2 0 [47, 252]        -- 47 prime; 252 = 2^2 * 3^2 * 7
      , bbRatio (some .bb10) 1 1 2 0 [47, 1728]      -- 47 prime; 1728 = 2^6 * 3^3
      ]
  | .neutron =>
      [ ratio 1 1 [684]                              -- 684 = 2^2 * 3^2 * 19
      , bbRatio (some .bb2) (-1) 1 1 0 [120, 9]     -- 120 = 2^3 * 3 * 5; 9 = 3^2
      ]
  | .lambda => [ratio (-2) 3 [432]]                  -- 432 = 2^4 * 3^3
  | .sigmaPlus => [ratio 3 1 [48]]                  -- 48 = 2^4 * 3
  | .omegaMinus => [ratio (-1) 1 [432]]             -- 432 = 2^4 * 3^3
  | .wBoson => [ratio (-1) 3 [162]]                 -- 162 = 2 * 3^4
  | .zBoson => [ratio 1 1 [136]]                    -- 136 = 2^3 * 17
  | .higgs => [sqrt6Ratio 1 1 [576]]                -- 576 = 2^6 * 3^2

/--
Symbolic `Ω` terms for each particle.

This is the current closure/continuation field of `L1`. The registry still
remains symbolic in Lean; comments only expose the packet structure of rare
composite denominators:
- `54 = 2 * 3^3`
- `64 = 2^6`
- `2304 = 2^8 * 3^2`
- `18496 = 2^6 * 17^2`
- `186624 = 2^8 * 3^6`
- `1521 = 3^2 * 13^2`
- `24 = 2^3 * 3`
- `4096 = 2^12`
- `59319 = 3^3 * 13^3`
-/
def omegaTermsOfParticle : ParticleName → List SymbolicTerm
  | .electron => []
  | .muon =>
      [ bbRatio (some .bb5) 1 1 1 (-1) []
      , bbRatio (some .bb7) 1 1 2 (-1) [56, 24]      -- 56 = 2^3 * 7; 24 = 2^3 * 3
      , bbRatio (some .bb11) 1 1 2 (-1) [56, 120]    -- 56 = 2^3 * 7; 120 = 2^3 * 3 * 5
      ]
  | .tau => [ratio 3 1 [110, 432]]                  -- 110 = 2 * 5 * 11; 432 = 2^4 * 3^3
  | .upQuark => [ratio 3 1 [162]]                   -- 162 = 2 * 3^4
  | .downQuark => [piRatio (-1) 1 [54]]             -- 54 = 2 * 3^3
  | .strangeQuark => [ratio 4 1 [3136]]             -- 3136 = 2^6 * 7^2
  | .charmQuark => [piRatio 1 1 [64]]               -- 64 = 2^6
  | .bottomQuark => [ratio (-2) 1 [59319]]          -- 59319 = 3^3 * 13^3
  | .topQuark => [ravgGammaRatio (-1) 1 [81]]       -- 81 = 3^4
  | .pionZero => [ratio 1 3 [136, 110]]             -- 136 = 2^3 * 17; 110 = 2 * 5 * 11
  | .kaonPlus => [alphaCouplingSq (-1) 2]
  | .kaonZero => [ratio 1 4 [48, 432]]              -- 48 = 2^4 * 3; 432 = 2^4 * 3^3
  | .dMesonZero => [bbRatio none (-2) 3 0 2 [432]]  -- 432 = 2^4 * 3^3
  | .dMesonPlus => [ratio 4 1 [110, 432]]           -- 110 = 2 * 5 * 11; 432 = 2^4 * 3^3
  | .bMesonZero => [ratio (-1) 6 [2304]]            -- 2304 = 2^8 * 3^2
  | .bsMesonZero => [alphaCouplingSq 2 1]
  | .proton => []
  | .neutron => []
  | .lambda => [sqrt6Ratio (-1) 1 [18496]]          -- 18496 = 2^6 * 17^2
  | .sigmaPlus => [ratio (-1) 3 [1521]]             -- 1521 = 3^2 * 13^2
  | .omegaMinus => [ratio (-2) 3 [186624]]          -- 186624 = 2^8 * 3^6
  | .wBoson => [ratio 4 1 [4096]]                   -- 4096 = 2^12
  | .zBoson => [alphaCouplingSq (-1) 2]
  | .higgs => [bbRatio none (-1) 1 0 2 [1521]]      -- 1521 = 3^2 * 13^2

/--
Predicate selecting path families whose shift layer is parameterized by the
current symbolic `δ₀` grammar.
-/
def pathHasParametricDelta : OperatorPath → Bool
  | .quarkSeedDual => true
  | .mesonNeutralTailClosure => true
  | .mesonChargedTailClosure => true
  | _ => false

theorem quark_seed_path_is_parametric :
    pathHasParametricDelta .quarkSeedDual = true := rfl

theorem proton_d0_term_count :
    (d0TermsOfParticle .proton).length = 4 := rfl

theorem muon_omega_term_count :
    (omegaTermsOfParticle .muon).length = 3 := rfl

end TnrFormal
