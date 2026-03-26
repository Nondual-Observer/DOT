/-!
# Axioms

This module fixes the compact axiom vocabulary used by the Lean package. It is
not a derivation layer; it is a canonical symbolic list of the machine-level
claims that the later `L1` files rely on.

Theory references:
- `docs/prefin/en/DOT_machine_architecture_overview_en.md` (Introduction; §§1-3)
- `docs/prefin/en/DOT_mathematical_framework_en.md` (operator atlas and
  machine vocabulary)
-/

namespace TnrFormal

/-- Canonical world-level axioms used by the current symbolic package. -/
inductive WorldAxiom where
  | closure
  | selfIdentity
  | distinctionPrimacy
  | boundaryNecessity
  | asymmetricAct
  | projectiveReadout
  | layerUnity
  deriving Repr, DecidableEq

/-- Ordered list of the seven canonical axioms of the current package. -/
def canonicalAxiomList : List WorldAxiom :=
  [ .closure
  , .selfIdentity
  , .distinctionPrimacy
  , .boundaryNecessity
  , .asymmetricAct
  , .projectiveReadout
  , .layerUnity
  ]

/-- Number of canonical axioms in the current Lean package. -/
def axiomCount : Nat := canonicalAxiomList.length

theorem canonical_axiom_count : axiomCount = 7 := rfl

/-- The package starts from closure as the first axiom. -/
def closureFirst : canonicalAxiomList.head? = some .closure := rfl

end TnrFormal
