# DOT: How to Read the Periodic Table of Elementary Particles

**Russian version:** [tnr_pure_topology_table_post_ru.md](./tnr_pure_topology_table_post_ru.md)

This document serves as an introductory guide to the particle table and the
core principle of DOT.

Its purpose is twofold. First, it provides a short and coherent introduction to
the core principle of DOT: particle masses are read not as arbitrary numerical
parameters, but as observable results of closure on a discrete layered carrier.
Second, it shows how this principle manifests in the already operational layer
`L1`: as a finite table of addresses, depths, and assembly paths, rather than
a collection of unrelated formulas.

Therefore, this text does not replace the full DOT corpus, but serves as an
entry map. It allows one to first see the general principle of the machine,
then cross-check it against the public particle table, and only then move on
to the expanded formulas, code, and formal proofs.

The central thesis of DOT is as follows. In the Standard Model, particle masses
are largely introduced as parameters. In DOT, a particle's mass is read
differently: as the observable result of closing a local configuration on a
layered octahedral carrier `K(2,2,2)`. Therefore, the table below is not a list
of lucky numerical coincidences, but a compressed map of the current layer `L1`:
each particle is defined by a discrete carrier node address, layer depth, and
assembly path type.

It is important to establish two things right away.

First, the image with formulas is a **compressed public view** of the current
engine. In the full `L1`, a particle is assembled not simply as `C / γ^k`, but
according to one of three schemes:

```text
M = B
M = B · exp(δ₀ + Ω)
M = B · exp(δ₀ + Ω) · T
```

where `B` is the carrier basis, `δ₀ + Ω` is the small grammar of internal
shifts, and `T` is the tail—the connection of the local node to the surrounding
boundary closure system. Second, `kₙ` in the table is not a free fitting
coefficient, but a public shorthand notation for this closure grammar.

In other words, the table should be read as follows: **the discrete carrier node
address first determines the mass basis, and then the machine completes it with
a small number of permitted operators.**

## What Exactly Is Shown in the Table

The table uses only three levels of data.

1. `γ = √6 / 3²`  
   This is the base invariant of the octahedral carrier.

2. The power `γ^k`  
   It determines the depth or layer. Growth of `k` does not mean an arbitrary
   scale, but a transition to a different carrier level.

3. The numerator `C`  
   This is not a random number on top, but a discrete node address on the
   carrier.

Therefore, a formula of the form

```text
C / γ^k
```

in DOT means not "we picked a nice fraction," but "we specified which layer the
particle sits on and which carrier node it reads."

The `Δ without kₙ` column is also important. It shows how well the carrier
basis alone works, **before** the full closure grammar `δ₀ + Ω + T`. Therefore,
large values there do not mean "the theory doesn't work"; they mean that for
this particle, not only the local address matters, but also how it is stitched
to the boundary system.

## Public Formula Table

The calculations are built on the invariant of the octahedral carrier
`γ = √6 / 3²`. The power `γ^k` determines the layer, and the numerator
determines the carrier node.

### Particles with Established Formulas

| Lvl | Part. | Matrix | Δ w/o `kₙ` |
|---|---|---|---:|
| `γ⁰` | `e⁻` | `1` | `0.00%` |
| `γ⁰` | `τ⁻` | `2⁷ · 3³ · kₙ` | `0.61%` |
| `γ¹` | `μ⁻` | `2³ · 7 / γ · kₙ` | `0.49%` |
| `γ¹` | `π⁰` | `2³ · 3² / γ · kₙ` | `0.15%` |
| `γ²` | `K⁺ / K⁰` | `2³ · 3² / γ² · kₙ` | `0.61%` |
| `γ²` | `p⁺`, `n⁰` | `2³ · 17 / γ² · kₙ` | `0.15%` |
| `γ²` | `Λ⁰`, `Σ⁺` | `2 · 3⁴ / γ² · kₙ` | `6.04%` |
| `γ²` | `D⁰ / D⁺` | `2⁴ · 17 / γ² · kₙ` | `0.62%` |
| `γ³` | `s` | `2² / γ³ · kₙ` | `8.55%` |
| `γ³` | `c` | `2⁴ · 3 / γ³ · kₙ` | `4.20%` |
| `γ³` | `Ξ_cc` *(already discovered)* | `2⁴ · 3² / γ³ · kₙ` | `0.83%` |
| `γ³` | `b` | `2 · 3⁴ / γ³ · kₙ` | `1.77%` |
| `γ⁴` | `Ω⁻` | `2 · 3² / γ⁴ · kₙ` | `0.23%` |
| `γ⁴` | `B⁰ / B_s⁰` | `2³ · 7 / γ⁴ · kₙ` | `2.83%` |
| `γ⁴` | `t` | `2⁴ · 3² · 13 / γ⁴ · kₙ` | `0.95%` |
| `γ⁶` | `W^±` | `2⁶ / γ⁶ · kₙ` | `0.11%` |
| `γ⁶` | `Z⁰` | `2³ · 3² / γ⁶ · kₙ` | `0.73%` |
| `γ⁷` | `H⁰` | `3³ / γ⁷ · kₙ` | `0.42%` |

### Predicted States

| Lvl | Target Part. | Matrix | Theor. Mass (MeV) | Tail (MeV) |
|---|---|---|---:|---:|
| `γ³` | `Ω_cc^+` | `3 · 7² / γ³ · kₙ` | `3716.370` | `−15.3 .. −3.9` |
| `γ⁴` | `Ξ_bc / Ω_bc` | `2 · 5 · 7 / γ⁴ · kₙ` | `6520.451` | `−8.9 .. +11.6` |
| `γ³` | `Ω_ccc^{++}` | `2⁶ · 3 / γ³ · kₙ` | `4862.291` | `−29.2 .. +20.7` |
| `γ³` | `Ω_bcc^+` | `2 · 3² · 17 / γ³ · kₙ` | `7762.057` | `−29.2 .. +41.2` |

## Why This Is Not Numerology

If the table were merely a collection of nice fractions, it would be easy to
suspect a numerical game. But the current `L1` holds together not through a
free set of formulas, but through a rigid architecture:

1. the same carrier node is reused across different families;
2. particles are assembled not from `24` independent expressions, but from a
   finite number of operator paths;
3. tails appear rarely and structurally, not for every particle at will;
4. heavy families continue the same grammar rather than introducing separate
   physics.

For the current `L1`, this is already visible explicitly:

- `24` particles,
- `15` operator paths,
- `5` superpaths.

That is, the layer is organized not as "mass equals formula number `n`," but as
a **fabric of assembly paths** over the same octahedral machine.

## What a Finite Alphabet of Prime Modes Means

It is most useful to read the numerator not as "just an integer," but as
a **mode packet** on the carrier.

In the current particle layer, the numerators decompose over a finite alphabet
of prime carrier modes:

```text
{2, 3, 5, 7, 11, 13, 17}
```

This does not mean that "everything in the world is made of prime numbers."
The meaning is different. DOT asserts that on the octahedral carrier there is a
finite number of irreducible basis modes, and composite numerators are already
packets of those modes.

For example:

- `2³ · 17 / γ²` for `p⁺`, `n⁰` is not random arithmetic, but a single
  specific carrier mode packet on layer `γ²`;
- `2² / γ³` for `s` is a different, more compact packet sitting at depth `γ³`;
- `2³ · 3² / γ²` for `K` shows that the kaon uses a different node, even though
  its strangeness is related to the same sector as `s`.

This matters because the tail in DOT appears **not as yet another number on
top**, but as a stitching rule for the already selected mode packet to the
boundary system.

### Why the `K` Family Is the Best First Example

The `K⁺ / K⁰` family is the cleanest place to see what a tail means in DOT in
the most general way. Both states sit on the same carrier basis

```text
72 / γ² = 2³ · 3² / γ²
```

but diverge not by changing the basis itself, but by taking different closure
paths. This means that the family is already fixed at the level of the carrier
node, while the difference between concrete states arises at the level of the
closure grammar. That is why the kaon family is the natural entry point for the
tail discussion: the tail does not create a particle from scratch, but completes
one and the same basis into different observable boundary configurations.

## What the Tail Really Is

The tail `T` is not a small numerical correction and not a free fitting
coefficient. In the full particle assembly, it plays the role of a **separate
closure operator**.

The full `L1` scheme has three forms:

```text
M = B
M = B · exp(δ₀ + Ω)
M = B · exp(δ₀ + Ω) · T
```

This means the following:

- if the carrier basis `B` and the internal shift `δ₀ + Ω` already fully close
  the particle readout, then `T = 0`;
- if the local node requires an additional connectivity channel with the
  boundary structure, an explicit tail `T ≠ 0` appears.

Therefore, the tail in DOT should be understood not as "an addition to mass,"
but as an **operator of additional closure alignment**. It activates not to
improve the match, but only where without it the local node does not yield the
full observable configuration.

### Example: Strange Quark

This is particularly well illustrated by the `s`-quark. In the full `L1`
unfolding, it has the form:

```text
B = 4 / γ^3
δ₀ = -1 / 12
Ω = 4 / 3136
T = 0
```

This is an important fact. It means that **strangeness itself is not equal to a
tail**. The strange quark already stabilizes as a local double-shift mode
without an explicit `T`.

### Example: Neutral Kaon

For `K⁰`, the situation is different. Here the strange mode enters not a single
quark readout, but a mesonic closure path:

```text
B = 72 / γ^2
δ₀ = 1 / (4 · 136)
Ω = 1 / (4 · 48 · 432)
T = BB11 · α / (120 · 55)
```

That is, the tail appears not because "the particle contains `s`," but because
the local node must be aligned with the boundary structure of the neutral
mesonic closure.

The same is visible even more strongly in `B_s^0`, where the strange mode again
enters the tail path, but on a different layer and with a different closure
load.

Therefore, the correct understanding is:

> the tail in DOT is not additional mass from nowhere, but a rule of topological
> connectivity showing how the local basis is brought to the observable boundary
> configuration.

## What the Table Already Shows

Even in the compressed public form, the table reveals several strong features.

1. **Leptons, quarks, baryons, and bosons sit in the same carrier language.**  
   They do not require different "ontologies."

2. **Particles of the same family often share a common basis.**  
   Differences arise not through a new formula from scratch, but through a
   different operator path.

3. **The tail is a rare and substantive entity.**  
   It is not needed everywhere.

4. **Heavy states continue the same language.**  
   The table does not split into disconnected "light" and "heavy" physics.

## Where to Find the Unfolding and Proofs

If you need the next step after this page, proceed in the following order.

First:

- [Particle Formula Fabric Law](./tnr_particle_formula_law_en.md)  
  A short mathematical framework for layer `L0 -> L1`: axioms, carrier bases,
  operator paths, superpaths, and the general assembly law.

- [Full L1 Unfolding](./tnr_l1_full_unfolding_en.md)  
  The complete list of current `24` particles with carrier bases, shifts `δ₀`,
  `Ω`, tails `T`, and final formulas.

- [L1 Coefficients Article (Russian)](./tnr_l1_coefficients_article_ru.md)  
  A focused article on how `B`, `δ₀`, `Ω`, and `T` are organized in `L1`, where
  the rigid core already is, and where the rare frontier coefficients still
  remain.

- [L1 Coefficient Registry (Russian)](./tnr_l1_coefficient_registry_ru.md)  
  A reference map of coefficient classes: bare basis, `δ₀`, `Ω`, and explicit
  tails.

- [Explicit L1 Tails (Russian)](./tnr_l1_explicit_tails_ru.md)  
  A separate audit of tails: where `T` appears, how large it really is, and why
  explicit tails should not be confused with the whole closure grammar.

Then:

- [Lean Package README](./README.md)  
  A general map of the formal contour: what has already been exported to Lean
  and how the package is structured.

- [Lean Package README (English)](./README_EN.md)  
  The same package overview in English.

- [Main Lean Package Entry File](./TnrFormal.lean)  
  Entry point into the current formalization.

- [Full Formal L1 Unfolding in Lean](./TnrFormal/L1Unfolding.lean)  
  The direct formal record of the `L1` unfolding.

If you need a rigorous verification route, it is as follows:

1. read this introductory page as a summary of the principle;
2. cross-check the public table against the expanded `L1` law;
3. proceed to the full unfolding;
4. then review the Lean formalization as the proof-level fixation layer.

This is exactly the order in which this document was designed: first the DOT
principle, then its partial numerical projection, then the expanded formulas,
and only then the proof contour.

## Final Note

This table does not require belief. It requires a simpler gesture:

1. verify whether the carrier node addresses are indeed structurally recurrent;
2. verify whether the tail is rare and appears only where it should;
3. verify whether the full `L1` reduces to a finite number of assembly paths;
4. check the code and Lean formalization.

If all of this withstands verification, then particle masses can no longer be
considered merely a set of empirical numbers. They must be read as topological
readouts of one and the same machine.
