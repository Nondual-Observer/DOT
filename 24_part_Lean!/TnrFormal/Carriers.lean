/-!
# Carriers

This module names the current `L1` bare families. At this stage they are a
canonical registry, not yet a first-principles derivation from the explicit
octahedral graph.

Theory references:
- `docs/prefin/en/DOT_mathematical_framework_en.md` (§26.2, §26.3)
- `docs/prefin/en/DOT_physical_realization_en.md` (§29.1, §30)
-/

namespace TnrFormal

/-- Bare carrier families used by the symbolic `L1` law. -/
inductive BareFamily where
  | anchor
  | muonBridge
  | tauBulk
  | uSeed
  | dSeed
  | sSeed
  | cSeed
  | bSeed
  | tSeed
  | pionSeed
  | kaonSeed
  | dMesonSeed
  | bMesonSeed
  | nucleonSeed
  | lambdaSigmaSeed
  | omegaSeed
  | wSeed
  | zSeed
  | higgsSeed
  deriving Repr, DecidableEq

/-- Number of bare families in the current package. -/
def bareFamilyCount : Nat := 19

theorem bare_family_count_is_19 : bareFamilyCount = 19 := rfl

end TnrFormal
