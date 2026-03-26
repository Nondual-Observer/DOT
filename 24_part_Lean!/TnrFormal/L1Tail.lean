import TnrFormal.L1Delta

/-!
# L1Tail

Explicit tail registry for the current `L1` package.

The tail `T` is the rarest part of the particle law. It is not present for all
particles and must therefore be documented separately from the `δ₀` / `Ω`
grammar.

Theory references:
- `docs/prefin/en/DOT_machine_architecture_overview_en.md` (§3; §6; §7; §9)
- `docs/prefin/en/DOT_mathematical_framework_en.md` (§26.3)
- `docs/prefin/en/DOT_physical_realization_en.md` (§31.1.1)
-/

namespace TnrFormal

/--
Explicit tail terms of the current `L1` law.

Composite denominators are factorized inline:
- `12 = 2^2 * 3`
- `119 = 7 * 17`
- `240 = 2^4 * 3 * 5`
- `353` prime
- `120 = 2^3 * 3 * 5`
- `55 = 5 * 11`
- `221 = 13 * 17`
- `252 = 2^2 * 3^2 * 7`
- `412 = 2^2 * 103`
- `6176 = 2^5 * 193`
- `273 = 3 * 7 * 13`
- `1080 = 2^3 * 3^3 * 5`
- `1098 = 2 * 3^2 * 61`
- `224 = 2^5 * 7`
- `58 = 2 * 29`
-/
def tailTermsOfParticle : ParticleName → List SymbolicTerm
  | .electron => []
  | .muon => []
  | .tau => []
  | .upQuark => []
  | .downQuark => []
  | .strangeQuark => []
  | .charmQuark => []
  | .bottomQuark => []
  | .topQuark => []
  | .pionZero => [bbRatio (some .bb6) 1 1 0 3 [12, 119]]        -- 12 = 2^2 * 3; 119 = 7 * 17
  | .kaonPlus => [bbRatio (some .bb19) (-1) 1 0 1 [240, 353]]  -- 240 = 2^4 * 3 * 5; 353 prime
  | .kaonZero => [bbRatio (some .bb11) 1 1 1 0 [120, 55]]      -- 120 = 2^3 * 3 * 5; 55 = 5 * 11
  | .dMesonZero => [bbRatio (some .bb15) 1 1 0 1 [120, 221]]   -- 120 = 2^3 * 3 * 5; 221 = 13 * 17
  | .dMesonPlus => [bbRatio (some .bb22) 1 1 0 3 [252, 412]]   -- 252 = 2^2 * 3^2 * 7; 412 = 2^2 * 103
  | .bMesonZero => [bbRatio none 1 1 1 1 [6176]]               -- 6176 = 2^5 * 193
  | .bsMesonZero => [bbRatio (some .bb14) 1 1 0 2 [120, 273]]  -- 120 = 2^3 * 3 * 5; 273 = 3 * 7 * 13
  | .proton => []
  | .neutron => [bbRatio (some .bb4) (-1) 1 2 0 [1080, 1098]]  -- 1080 = 2^3 * 3^3 * 5; 1098 = 2 * 3^2 * 61
  | .lambda => [bbRatio (some .bb3) 1 1 0 3 [12, 224]]         -- 12 = 2^2 * 3; 224 = 2^5 * 7
  | .sigmaPlus => []
  | .omegaMinus => []
  | .wBoson => []
  | .zBoson => [bbRatio (some .bb14) 1 1 0 3 [252, 58]]        -- 252 = 2^2 * 3^2 * 7; 58 = 2 * 29
  | .higgs => []

/-- Predicate selecting paths that require an explicit tail layer. -/
def pathHasParametricTail : OperatorPath → Bool
  | .mesonNeutralTailClosure => true
  | .mesonChargedTailClosure => true
  | _ => false

theorem meson_neutral_tail_path_is_parametric :
    pathHasParametricTail .mesonNeutralTailClosure = true := rfl

theorem neutron_tail_term_count :
    (tailTermsOfParticle .neutron).length = 1 := rfl

end TnrFormal
