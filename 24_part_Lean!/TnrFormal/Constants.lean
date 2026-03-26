import TnrFormal.Prelude

/-!
# Constants

This module stores the symbolic names of the base constants used across the
package. It intentionally keeps them symbolic. Their numerical/metric
derivation belongs to the theory corpus, not to the current Lean layer.

Theory references:
- `docs/prefin/en/DOT_machine_architecture_overview_en.md` (§§8-10)
- `docs/prefin/en/DOT_mathematical_framework_en.md` (§21; §26.2)
- `docs/prefin/en/DOT_physical_realization_en.md` (§30; §33)
-/

namespace TnrFormal

/-- Symbolic names of the base constants used by the package. -/
structure BaseConstants where
  gamma : String
  alpha : String
  rydberg : String
  bond : String
  deriving Repr, DecidableEq

/-- Canonical symbolic constant names used in the current Lean package. -/
def canonicalConstants : BaseConstants :=
  { gamma := "γ"
  , alpha := "α"
  , rydberg := "Ry"
  , bond := "Ry/3"
  }

end TnrFormal
