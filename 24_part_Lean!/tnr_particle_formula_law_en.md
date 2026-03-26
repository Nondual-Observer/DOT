# DOT: The Particle Formula Fabric Law

This document establishes one specific thesis: particles are not derived from a
single one-dimensional formula. They are derived from a closed distinction
machine, and formulas are merely the readable tails of its modes.

Therefore, the task here is not to find a single expression of the form

```text
particle = F(n)
```

but to unfold the law that generates a **formula fabric** from a single
structure.

This document is written without formal proofs. Its purpose is to provide a
short mathematical unfolding of layer `L0 -> L1`, sufficient for:

1. reading the law as a whole;
2. cross-checking against the current solver code;
3. parallel formalization in Lean.

The direct unfolding of all `24` particles without formal proofs is placed
separately:
[tnr_l1_full_unfolding_en.md](./tnr_l1_full_unfolding_en.md).

---

## 1. Axioms

What is fixed below are not "all truths about the world," but the minimal
pillars without which one cannot consistently read the lower floor, the
octahedral carrier, and the particle layer.

### 1.1. Closure

Reality does not require an external origin. Only internally closed modes are
admissible.

### 1.2. Self-Identity

The absolute invariant is the identity of the structure with itself.

### 1.3. Distinction Is Primary

The object is not primary. What is primary is the act of distinction that makes
reading possible.

### 1.4. Boundary Is Mandatory

Every distinction requires a boundary. Without a boundary, there is neither
state nor transition.

### 1.5. An Act Leaves a Residue

Transition, normalization, opening, and closure are asymmetric and leave a
trace.

### 1.6. The Observable Is Projective

Formulas, numbers, masses, and connections are not primary reality, but
readable tails of the machine's internal modes.

### 1.7. Layers Are Unified

Topology, geometry, algebra, and analysis are not separate worlds, but different
readings of one and the same closed structure.

From these axioms, the main principle of this document follows immediately:

> particles must be unfolded not as a list of ready-made formulas, but as a
> readout of a finite number of operator paths over a single machine.

---

## 2. What We Abandon

At the current stage, it is already clear that the particle layer cannot be
reduced to a single one-dimensional law of the form:

```text
particle = F(n)
```

The reason is not a lack of technique, but the nature of the layer itself.
Particles in DOT are born not as values along a single axis, but as readouts of
different modes of one and the same machine:

- carrier family,
- role,
- shift grammar,
- tail grammar,
- closure mode.

Therefore, instead of a "universal formula," something stronger emerges here:
a **universal law of mode decomposition**, after which each particle is obtained
as a route within the shared operator fabric.

---

## 3. The Source Carrier

The source geometry is not an abstract smooth medium, but a local octahedral
carrier. It is needed not as an image, but as the minimal finite carrier of
distinction.

In this machine, the following are already separated:

- polarity,
- face,
- seam,
- closure,
- transition to the shell,
- shadow complementary branch.

The lower structural floor:

```text
0 -> 1 -> 2 -> 6 -> 12 -> 8
```

Here:

- `0` — prohibition of empty reading;
- `1` — identity;
- `2` — polarity;
- `6` — full triadic boundary;
- `12` — edge network of transition;
- `8` — first closure.

All subsequent numerical and operator structures must be compatible with this
floor. This is the first filter of admissible formulas.

---

## 4. Visible and Shadow Branches

The next layer of the machine is defined by two connected packages:

```text
24 / 48
23 / 47
```

These cannot be read as random numbers. This is the first stable visible/shadow
grammar.

- `24 / 48` — visible structural assembly;
- `23 / 47` — complementary witness layer.

From this, the following are then constructed:

- the shell corridor,
- horizon assembly,
- the Lucas/Fibonacci bridge,
- operator families on higher layers.

For the particle layer, this matters because the carrier bases and shifts do not
float freely: they must sit within the already assembled visible/shadow
architecture.

---

## 5. Base Constants

Computation begins not with the particle table, but with several base
quantities:

- `γ`
- `γ²`
- `γ³`
- `α`
- `Ry`
- `E_bond`

In the language of the machine, these are not "physical constants as given," but
derived readouts of the carrier.

At the current stage, the following are especially important for the particle
layer:

- `γ` as the scale transfer parameter;
- `γ^-k` as the heavy lift mode;
- carrier numerators `C`;
- families `BB_k`, `BD5`, `tail`, `closure`.

That is, in `L1` we begin not with "particle mass," but with:

```text
carrier family + gamma mode + operator path
```

---

## 6. Why the Formulas Form a Fabric

If one looks at the current `L1` from the code and solver, particles no longer
form a flat list of `24` independent expressions.

They collapse as follows:

- `24` particles
- `15` operator paths
- `5` superpaths

Current superpaths:

- `base_identity`
- `single_lift`
- `dual_shift_family`
- `tail_closure_family`
- `shadow_tail_family`

This is the main structural fact of the particle layer:

> particles are not twenty-four separate formulas, but a finite number of
> assembly paths over the same carrier families.

---

## 7. The Working Law of the Particle Layer

In its minimal form, layer `L1` currently reads as:

```text
carrier family
-> mode passport
-> operator path
-> superpath
-> particle mass
```

It is precisely this chain, not a single scalar formula, that constitutes the
law of the layer.

From this, two important conclusions follow immediately.

### 7.1. The Search for "One Formula"

The search for a single formula for all particles in the literal sense is almost
certainly mistaken. It erases the very structure of the layer.

### 7.2. The Correct Object of Formalization

What must be formalized is not "the mass table," but:

- classes of carrier bases,
- mode passports,
- operator paths,
- superpaths,
- the assembly law.

### 7.3. Carrier Basis Families

At the current stage, `L1` is no longer read as a list of twenty-four separate
carriers. It collapses to a finite set of carrier basis families:

- `anchor`
- `muon_bridge`
- `tau_bulk`
- `u_seed`, `d_seed`, `s_seed`, `c_seed`, `b_seed`, `t_seed`
- `pion_seed`, `kaon_seed`, `d_meson_seed`, `b_meson_seed`
- `nucleon_seed`, `lambda_sigma_seed`, `omega_seed`
- `w_seed`, `z_seed`, `higgs_seed`

This is an important boundary. Particles no longer "hang in the air": each must
begin from one of these carrier bases.

#### 7.3.1. The Carrier Basis Law

For all non-anchor cases, the carrier basis already reads simply:

```text
B = C · γ^k
```

where `C` is the carrier numerator and `k` is the gamma power mode. For
negative `k`, this reads as division by `γ^|k|`.

In the current `L1`, this yields, for example:

- `muon_bridge = 56 / γ`
- `tau_bulk = 3456`
- `u_seed = 56 · γ²`
- `d_seed = 6528 · γ^5`
- `pion_seed = 72 / γ`
- `kaon_seed = 72 / γ²`
- `nucleon_seed = 136 / γ²`
- `lambda_sigma_seed = 162 / γ²`
- `w_seed = 64 / γ^6`
- `z_seed = 72 / γ^6`
- `higgs_seed = 27 / γ^7`

The electron anchor case remains separate:

```text
B_anchor = e
```

That is, already at the base carrier level, particles emerge not from arbitrary
scales, but from a finite set of `C·γ^k` bases plus one anchor readout.

### 7.4. Fifteen Operator Paths

The particle layer is already collapsed not only by carrier basis families, but
also by assembly paths. The current solver yields `15` operator paths:

- `anchor.identity.direct`
- `lepton.bridge.single`
- `lepton.bulk.dual`
- `quark.seed.dual`
- `meson.neutral.tail_closure`
- `meson.charged.tail_closure`
- `meson.strange.tail_closure`
- `baryon.proton.single_lift`
- `baryon.neutron.shadow_tail`
- `baryon.lambda.tail_closure`
- `baryon.sigma.dual_lift`
- `baryon.bulk.dual`
- `boson.gauge.dual`
- `boson.gauge.tail_closure`
- `boson.scalar.dual`

That is, the formula fabric of `L1` is no longer arbitrary. It passes through
a finite number of assembly routes.

### 7.5. Five Superpaths

Above the assembly paths stands an even coarser compression. All `24` particles
currently reduce to `5` superpaths:

- `base_identity`
- `single_lift`
- `dual_shift_family`
- `tail_closure_family`
- `shadow_tail_family`

This is the first strong form of the law: the particle layer is not chaotic, but
assembles through a small number of superfamilies.

### 7.6. Unfolding of Twenty-Four Particles

In the current state of the solver, the layer unfolds as follows.

**`base_identity`**

- `e⁻`

**`single_lift`**

- `μ`
- `p`

**`dual_shift_family`**

- `τ`
- `u, d, s, c, b, t`
- `Σ⁺`
- `Ω⁻`
- `W±`
- `H⁰`

**`tail_closure_family`**

- `π⁰`
- `K⁺`, `K⁰`
- `D⁰`, `D⁺`
- `B⁰`, `Bs⁰`
- `Λ`
- `Z⁰`

**`shadow_tail_family`**

- `n`

This is already a sufficient record for the next step: unfolding not individual
formulas one by one, but superpath by superpath.

### 7.7. Three Forms of Mass Assembly

After reducing `24` particles to `5` superpaths, it turns out that the current
`L1` has not twenty-four independent forms, but only **three** assembly types:

```text
identity:  M = B
shifted:   M = B · exp(Δ)
tailed:    M = B · exp(Δ) · T
```

Here:

- `B` — carrier basis mass;
- `Δ = δ₀ + Ω` — total layer shift;
- `T` — tail closure multiplier.

Then the superpaths read as:

- `base_identity` -> `M = B`
- `single_lift` -> `M = B · exp(Δ)`
- `dual_shift_family` -> `M = B · exp(Δ)`
- `tail_closure_family` -> `M = B · exp(Δ) · T`
- `shadow_tail_family` -> `M = B · exp(Δ) · T`

This is the first short form of the law: different particles differ not in that
each has a special scalar formula written out, but in which carrier basis, which
operator path, and which assembly type is used.

### 7.8. Minimal Layer Formula

In minimal notation, the entire current `L1` can be captured as:

```text
P = Assemble(B, Δ, T ; path, superpath)
```

or, expanding only what is necessary:

```text
P = B
P = B · exp(Δ)
P = B · exp(Δ) · T
```

All twenty-four particle formulas are particular tails of these three schemes
over different carrier bases and different operator paths.

The complete working registry of the current `L1` is placed in the accompanying
publication contour of the package:

- `tnr_l1_formula_registry_ru.md`
- `tnr_l1_formula_registry.json`

---

## 8. Unfolding by Superpaths

From here, the layer should be read not by individual particles, but superpath
by superpath. This yields a short and stable derivation sequence.

### 8.1. `base_identity`

Here the assembly scheme uses neither shift nor tail:

```text
P = B
```

The current carrier is only one:

- `anchor -> e⁻`

That is, the electron in the current `L1` is a pure anchor readout without
intermediate lift and closure grammar.

### 8.2. `single_lift`

Here the layer uses a single lift without a closure tail:

```text
P = B · exp(Δ)
```

Current implementations:

- `muon_bridge -> μ`
- `nucleon_seed -> p`

This is the first place where the carrier basis does not yet require a tail, but
already requires an asymmetric lift.

### 8.3. `dual_shift_family`

This is the largest superfamily of `L1`.

```text
P = B · exp(Δ)
```

But unlike `single_lift`, here the carrier reads not a bridge lift, but a
dual-shift regime. This includes:

- `tau_bulk -> τ`
- `u_seed, d_seed, s_seed, c_seed, b_seed, t_seed -> quarks`
- `lambda_sigma_seed(sigma) -> Σ⁺`
- `omega_seed -> Ω⁻`
- `w_seed -> W±`
- `higgs_seed -> H⁰`

That is, the dual-shift family holds the `bulk`, `seed`, and `field` modes of a
single structural class.

### 8.4. `tail_closure_family`

Here the dual shift is no longer sufficient and the layer must close through a
tail:

```text
P = B · exp(Δ) · T
```

This includes:

- `pion_seed -> π⁰`
- `kaon_seed -> K⁺, K⁰`
- `d_meson_seed -> D⁰, D⁺`
- `b_meson_seed -> B⁰, Bs⁰`
- `lambda_sigma_seed(lambda) -> Λ`
- `z_seed -> Z⁰`

This is the main layer of the current `L1`, saturated with closure.

### 8.5. `shadow_tail_family`

This is the minimal neutral shadow-return case:

```text
P = B · exp(Δ) · T_shadow
```

In the current `L1`, it is represented by a single case:

- `nucleon_seed(neutron) -> n`

That is, the neutron is not simply a tail-closure, but specifically a shadow
tail readout.

## 9. Symbolic Grammar of `L1`

After compression by superpaths, the layer can be read even deeper: by modes of
symbolic assembly.

### 9.1. `δ₀` Modes

In the current `L1`, only four modes are actually used for `δ₀`:

- `none`
- `zero`
- `sum`
- `log1p`

The distribution is already very rigid:

- `none` — anchor case only;
- `zero` — bridge case `μ`;
- `log1p` — nucleon lift cases;
- `sum` — the entire remaining `L1`.

That is, `δ₀` is already not an arbitrary analytical tail, but a finite
grammatical layer.

### 9.2. `Ω` Modes

For `Ω`, the layer also uses only:

- `none`
- `zero`
- `sum`
- `log1p`

And here the machine organization is again visible:

- `Ω = none` only on the anchor;
- `Ω = log1p` only for `μ`;
- `Ω = zero` on the nucleon single/shadow branch;
- `Ω = sum` on the bulk dual mode and on families saturated with closure.

### 9.3. Tail as a Separate Class

The tail is not present everywhere. It is activated only on particles saturated
with closure:

- neutral/charged/strange meson branches;
- `Λ`;
- `n`;
- `Z⁰`.

That is, the tail is not a mandatory part of a particle formula, but a separate
closure class.

### 9.4. Special Multipliers

In the current `L1`, special multipliers are reduced to a very short set:

- `π`
- `√6`
- `r_avg`

They appear not everywhere, but only in specific paths:

- `π` — quark and strange meson branches;
- `√6` — `Λ` and `H⁰`;
- `r_avg` — top branch.

This is already an important boundary: even special multipliers in the current
`L1` do not form a forest, but sit on a short finite list.

### 9.5. Short Law of the Symbolic Formula

If one compresses the layer completely, the current `L1` already reads as:

```text
P = Assemble(B, Mode(δ₀), Mode(Ω), TailClass ; path, superpath)
```

That is, the law of the particle layer consists no longer of twenty-four
formulas, but of:

1. carrier basis;
2. `δ₀` mode;
3. `Ω` mode;
4. tail class;
5. operator path;
6. superpath.

This is the correct transition point for the next step: not gluing on new
formulas, but unfolding the current `L1` through a finite symbolic grammar.

### 9.6. Term Alphabet

In the current `L1`, even the formula terms themselves are no longer arbitrary.
They sit on a very short alphabet:

1. **rational tails**
2. **`BB_k` carriers**
3. **special multipliers**

The short set of special multipliers is already fixed:

- `π`
- `√6`
- `r_avg`

The short set of `BB_k` actually used in the current `L1`:

- in `δ₀`: `BB2, BB3, BB5, BB7, BB10`
- in `Ω`: `BB5, BB7, BB11`
- in `tail`: `BB3, BB4, BB6, BB11, BB14, BB15, BB19, BB22`

That is, even at the level of the terms themselves, the `L1` fabric is already
discrete. There is no continuous forest of arbitrary corrections here; there is
a finite alphabet from which `δ₀`, `Ω`, and `T` are assembled.

### 9.7. Dominant Axes

The operator paths of the current `L1` are already differentiated not only by
formulas, but also by dominant reading axes. The short set of such axes
currently is:

- `base alphabet`
- `duplication / transfer`
- `continuation / mellin`
- `twist / closure`

Their role across the layer is already visible:

- `base alphabet` holds the pure anchor case;
- `duplication / transfer` manifests in the proton single-lift;
- `continuation / mellin` holds the dual-shift bulk layer;
- `twist / closure` holds the closure-rich and shadow-return branches.

This matters because paths differ not only in their numerical values, but also
in the type of reading itself. That is, `L1` already has not just a formulaic,
but an operator-axial organization.

The complete accompanying artifacts of the current layer are placed in the
publication contour of the package:

- `tnr_l1_superpath_formula_deck_ru.md`
- `tnr_l1_path_profile_registry_ru.md`
- `tnr_l1_delta_tail_registry_ru.md`

### 9.8. Exact `Δ/T` Registry

After separating superpaths and path profiles, the current `L1` already allows
fixing not only modes, but also exact symbolic registries for `Δ` and `T`.

Here an important boundary is discovered:

- some operator paths indeed yield a single rigid symbolic set;
- some paths are already **parametric** and are refined only after bare-family/state
  refinement.

In the current `L1`, the parametric ones are primarily:

- `quark.seed.dual`
- `meson.neutral.tail_closure`
- `meson.charged.tail_closure`

This means that the layer law can no longer be read coarsely as:

```text
path -> one formula
```

The correct reading is already stronger:

```text
operator path -> variant -> (δ₀, Ω, T)
```

This is precisely why the exact `Δ/T` registry is placed separately: it fixes
not only the path architecture, but also the exact symbolic sets that this path
admits.

## 10. What to Unfold Next Mathematically

In this form, the document can already be continued without changing the
architecture. The next step is not to search for a new general formula, but to
unfold in order:

1. the carrier basis `B`;
2. the exact shift grammar `Δ = δ₀ + Ω`;
3. the exact tail grammar `T`;
4. formula tails by each operator path.

This will be the very short mathematical unfolding of all particles: not
twenty-four independent formulas, but several assembly types with a finite
number of carrier bases and readout corrections tied to the path.

---

## 11. Parallel Lean Line

This same structure will be formalized not as a long proof of a single formula,
but as a typed framework:

- floors,
- carrier basis families,
- operator classes,
- operator paths,
- superpaths,
- exact `Δ/T` registries,
- particles.

That is, Lean is needed here not for "proving one function," but for formalizing
the architectural law: first axioms, then the carrier, then operator families,
then exact symbolic sets `δ₀/Ω/T`, and only then readout formulas.

This is consistent with the fact that the layer itself is already structured as
a fabric of modes, not as a one-dimensional closed formula.
