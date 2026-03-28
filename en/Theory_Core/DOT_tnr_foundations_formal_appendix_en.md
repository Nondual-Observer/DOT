# Theory of Observable Distinction (DOT) — Formal Appendix to the Foundations

**Status:** technical formal appendix  
**Purpose:** to provide a clean working formalisation of level zero and minimal admissibility, without supplanting either the liminal canon or the full architectural edition of the foundations.  
**Scope of the document:** only positions, the act of distinction, the three prohibitions, admissibility, and the global invariant are formalised here. The machine, optics, and artefacts are not included in this file.

---

## Introduction

1. **Function of the formalisation.**  
This document is not a canon and does not replace the architectural explication. Its task is narrower: to provide a uniform formal language in which level-0 statements can be fixed without external ontology.

2. **What is NOT introduced here.**  
The following are not introduced here:
- objects;
- states;
- external time;
- external measures;
- dynamics;
- the machine;
- optics;
- artefacts.

3. **What IS introduced here.**  
The following are introduced here:
- the set of positions;
- the act of distinction;
- three reduction predicates;
- three forbidden configurations;
- admissibility of a position;
- the global invariant and Borromean independence of the prohibitions.

---

# §1. Primitives and Primary Notation

### 1.1. Positions

**Definition 1.1 (Positions).**  
Let `P` be a non-empty set whose elements are called *positions of distinction*.  
An element `p ∈ P` is not:
- an object;
- a state;
- an event;
- a subject.

It is the minimal logical context in which an act of distinction can be asserted.

---

### 1.2. Act of Distinction

**Definition 1.2 (Act of Distinction).**  
For each position `p ∈ P` a Boolean predicate `A(p)` is introduced, meaning:

```text
A : P → {0,1},   A(p) = 1  ⇔  in position p an act of distinction is fixed.
```

`A(p)` fixes the fact of the act but does not specify its substantive content.

---

### 1.3. Three Reduction Predicates

Three Boolean predicates on positions are introduced:

- `Coincidence(p)` — coincidence of the distinguishing and the distinguished;
- `NoTrace(p)` — tracelessness of the act of distinction;
- `ExternalBasis(p)` — dependence of distinction on an external foundation.

Formally:

```text
Coincidence, NoTrace, ExternalBasis : P → {0,1}.
```

These predicates do not describe states of the world; they mark logico-structural reductions in position `p`.

---

### 1.4. Forbidden Configurations

**Definition 1.3 (Forbidden Configurations).**  
Three forbidden configurations are defined:

- `FC_D(p) := A(p) ∧ Coincidence(p)`
- `FC_F(p) := A(p) ∧ NoTrace(p)`
- `FC_C(p) := A(p) ∧ ExternalBasis(p)`

Substantively:
- `FC_D` fixes the inadmissibility of coincidence;
- `FC_F` fixes the inadmissibility of tracelessness;
- `FC_C` fixes the inadmissibility of an external foundation.

---

### 1.5. Level-0 Invariants

**Axiom 1.1 (Level-0 Invariants).**  
For all `p ∈ P` the following is required:

```text
∀p ∈ P: ¬FC_D(p),  ¬FC_F(p),  ¬FC_C(p).
```

This means: no position in which an act of distinction is performed admits the simultaneous realisation of the corresponding reduction.

These invariants:
- are accepted as primitive;
- are not derived from simpler statements;
- are not ontological laws about the world;
- set only the boundaries of admissibility of distinction.

---

### 1.6. Admissibility of a Position

**Definition 1.4 (Admissible Position).**  
A position `p ∈ P` is called admissible if and only if

```text
Admissible(p) ⇔ (A(p)=0) ∨ (A(p)=1 ∧ ¬FC_D(p) ∧ ¬FC_F(p) ∧ ¬FC_C(p)).
```

That is:
- either the act of distinction in `p` is not performed;
- or it is performed and in `p` no forbidden configuration is realised.

---

### 1.7. Active Positions

**Definition 1.5 (Active Positions).**  
Define:

```text
Active := { p ∈ P | A(p)=1 }.
```

And a useful refinement:

```text
Active_adm := { p ∈ Active | Admissible(p) }.
```

---

### 1.8. Global Invariant

**Definition 1.6 (Global Invariant).**  
The invariant `Inv` in DOT is not localised at a single position. It sets a global constraint on admissible configurations or routes of distinction.

Two equivalent projections are convenient:

1. as the set of forbidden routes `I`;
2. as a global Boolean predicate `Inv(γ)` on configurations `γ`.

In brief:

```text
Inv : Conf → {0,1},
Inv(γ) = 1  ⇔  configuration γ violates the architectural invariant.
```

Important:
- `Inv` is not reducible to a local `Inv(p)`;
- `Inv` is not a local object;
- `Inv` constrains not the position itself but the admissible routes and combinations.

---

### 1.9. Global Axiom of the Invariant

**Axiom 1.2 (Global Invariant).**  
No admissible configuration realises a forbidden route:

```text
∀γ ∈ Conf: AdmissibleConfig(γ) ⇒ Inv(γ)=0.
```

This fixes that the architectural invariant acts globally, not locally.

---

### 1.10. Borromean Independence of the Prohibitions

**Axiom 1.3 (Borromean Independence).**  
The three basic prohibitions are independent: none of them is derivable from the other two together with the remaining axioms of level 0.

Substantively this means:
- removal of any one of the three prohibitions destroys the sustaining of distinction;
- none of the three is a consequence of the other two;
- the triad of prohibitions is minimal.

---

### 1.11. Immediate Consequences

**Lemma 1.1.**  
From the level-0 axioms three local forms follow:

```text
∀p ∈ P: A(p)=1 ⇒ Coincidence(p)=0
∀p ∈ P: A(p)=1 ⇒ NoTrace(p)=0
∀p ∈ P: A(p)=1 ⇒ ExternalBasis(p)=0
```

These three forms do not replace the original axioms but are their direct unfoldings.

---

### 1.12. Semantic Projections

Below are two admissible interpretations of the apparatus already introduced.

#### (A) Modal Projection

- `P` is read as a set of worlds or situations;
- `A(p)` is read as an atomic proposition of the act of distinction;
- `FC_i(p)` are read as forbidden formulae in world `p`.

This projection is useful for the analysis of unprovability and invariance.

#### (B) Combinatorial Projection

- `P` is read as a set of vertices;
- `Active_adm` defines admissible active positions;
- on this basis one can subsequently introduce admissible transitions, cycles, and the bearer.

This projection is useful for the further architectural unfolding of the foundations.

---

### 1.13. Index of Notation

- `P` — set of positions
- `p, q, r` — elements of `P`
- `A(p)` — act of distinction in position `p`
- `Coincidence(p)` — coincidence
- `NoTrace(p)` — tracelessness
- `ExternalBasis(p)` — external foundation
- `FC_D(p), FC_F(p), FC_C(p)` — forbidden configurations
- `Admissible(p)` — admissibility of a position
- `Active` — set of active positions
- `Active_adm` — set of active admissible positions
- `Inv` — global invariant

---

## Closure of the Appendix

This document formalises only level zero and minimal admissibility.

It deliberately does not formalise:
- the early canon `0 -> NOT -> cut -> support -> Witness -> ...`;
- legalization and stabilisation;
- axes, cycles, faces, and the octahedron;
- the machine vocabulary `6 / 12 / 8`;
- optics and artefacts.

This means: it is useful as a technical foundation but does not replace the canon and does not replace the architectural treatise.

---

## Boundary of Applicability to the Machine

The same language **can be extended** towards the machine, but **not in its present form**.

For a minimal formalisation of the machine one would need to add at least:
- a typed bearer of states/nodes;
- a relation of admissible transition;
- the distinction of vertices, edges, and faces;
- local contexts;
- reading operators.

Therefore the correct formula is:

> this formal appendix is suitable as a language for the formalisation of the foundations;  
> for the machine it is suitable only after extension, not as is.
