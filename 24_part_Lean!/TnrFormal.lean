/-!
# TnrFormal

Umbrella import for the current Lean 4 formalization of the symbolic `L1`
particle layer of DOT.

What is formalized here:
- the declarative lower vocabulary (`L0`, floor nodes, structural packets);
- the particle registry and bare-family registry for `L1`;
- path classes, assembly classes, symbolic `δ₀ / Ω / T` terms;
- bundle/unfolding consistency for the current 24-particle layer.

What is **not** yet formalized here:
- the explicit graph object `K(2,2,2)`;
- the Laplacian/spectral derivation of `γ = √6 / 9`;
- the derivation of bare numerators `C` from the octahedral carrier itself.

Theory references in this repository:
- `docs/prefin/en/DOT_machine_architecture_overview_en.md`
- `docs/prefin/en/DOT_mathematical_framework_en.md`
- `docs/prefin/en/DOT_physical_realization_en.md`
-/

import TnrFormal.Axioms
import TnrFormal.Prelude
import TnrFormal.Octahedron
import TnrFormal.Constants
import TnrFormal.Carriers
import TnrFormal.Paths
import TnrFormal.L1
import TnrFormal.L1Bare
import TnrFormal.L1Assembly
import TnrFormal.L1Registry
import TnrFormal.L1Grammar
import TnrFormal.L1Terms
import TnrFormal.L1Delta
import TnrFormal.L1Tail
import TnrFormal.L1Profiles
import TnrFormal.L1Unfolding
