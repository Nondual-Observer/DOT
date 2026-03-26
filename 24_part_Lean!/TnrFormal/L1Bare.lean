import TnrFormal.Carriers

/-!
# L1Bare

Bare carrier registry for the current `L1` package.

This module stores the current canonical mapping

`BareFamily -> (C, gammaPower)`

used in the bare formula

`M_bare = C / gamma^k * m_e`.

Important boundary:
- the values below are a canonical imported registry;
- they are documented in the theory corpus;
- they are **not yet derived inside Lean** from an explicit octahedral/spectral
  construction.

Theory references:
- `docs/prefin/en/DOT_mathematical_framework_en.md` (§21; §26.2; §26.3)
- `docs/prefin/en/DOT_physical_realization_en.md` (§29.1; §30)
- `docs/prefin/en/DOT_machine_architecture_overview_en.md` (§8; §9)
-/

namespace TnrFormal

/--
Bare numerator `C` of each `BareFamily`.

Each composite numerator is documented by prime factorization so that the Lean
registry remains readable as a packet alphabet rather than a list of opaque
integers.
-/
def carrierCOf : BareFamily → Nat
  | .muonBridge => 56         -- 56 = 2^3 * 7
  | .tauBulk => 3456         -- 3456 = 2^7 * 3^3
  | .uSeed => 56             -- 56 = 2^3 * 7
  | .dSeed => 6528           -- 6528 = 2^7 * 3 * 17
  | .sSeed => 4              -- 4 = 2^2
  | .cSeed => 48             -- 48 = 2^4 * 3
  | .bSeed => 162            -- 162 = 2 * 3^4
  | .tSeed => 1872           -- 1872 = 2^4 * 3^2 * 13
  | .pionSeed => 72          -- 72 = 2^3 * 3^2
  | .kaonSeed => 72          -- 72 = 2^3 * 3^2
  | .dMesonSeed => 272       -- 272 = 2^4 * 17
  | .bMesonSeed => 56        -- 56 = 2^3 * 7
  | .nucleonSeed => 136      -- 136 = 2^3 * 17
  | .lambdaSigmaSeed => 162  -- 162 = 2 * 3^4
  | .omegaSeed => 18         -- 18 = 2 * 3^2
  | .wSeed => 64             -- 64 = 2^6
  | .zSeed => 72             -- 72 = 2^3 * 3^2
  | .higgsSeed => 27         -- 27 = 3^3
  | .anchor => 1

/--
Power of `gamma` used by each `BareFamily`.

This is the depth/exponent part of the lever law from mathematical framework
§26.2.
-/
def gammaPowerOf : BareFamily → Int
  | .anchor => 0
  | .muonBridge => -1
  | .tauBulk => 0
  | .uSeed => 2
  | .dSeed => 5
  | .sSeed => -3
  | .cSeed => -3
  | .bSeed => -3
  | .tSeed => -4
  | .pionSeed => -1
  | .kaonSeed => -2
  | .dMesonSeed => -2
  | .bMesonSeed => -4
  | .nucleonSeed => -2
  | .lambdaSigmaSeed => -2
  | .omegaSeed => -4
  | .wSeed => -6
  | .zSeed => -6
  | .higgsSeed => -7

/-- Whether the given family is the neutral anchor family. -/
def isAnchorFamily : BareFamily → Bool
  | .anchor => true
  | _ => false

theorem anchor_is_neutral_scale :
    carrierCOf .anchor = 1 ∧ gammaPowerOf .anchor = 0 := by
  constructor <;> rfl

theorem nucleon_seed_is_visible_shell :
    carrierCOf .nucleonSeed = 136 ∧ gammaPowerOf .nucleonSeed = -2 := by
  constructor <;> rfl

end TnrFormal
