# Distinction Observable Theory. Part II: Mathematical Framework

**Author:** Igor Zhuk  
**Affiliation:** Independent (Krasnodar, Russia)  
**Date:** March 2026  

> **DOI:** [10.5281/zenodo.19210790](https://doi.org/10.5281/zenodo.19210790)  
> **License:** [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)  
**Series:** Distinction Observable Theory (DOT), Part II of III  
**arXiv subject:** Mathematical Physics (math-ph); Number Theory (math.NT)

---

> "The unmanifest [Prakriti, primal matter] is endowed with the three gunas... The gunas, by their nature, are pleasure [Sattva], pain [Rajas], and indifference [Tamas]. Their purpose is to illuminate, to activate, and to restrict. They suppress each other, support each other, produce each other, and act together. Sattva (light) is considered light and illuminating; Rajas (passion) is stimulating and mobile; Tamas (darkness) is heavy and concealing. They work together for a single purpose, like a lamp [where oil, wick, and flame act in concert].
>
> ...
>
> Purusha [pure consciousness] is merely a witness to what occurs. It is endowed with absolute isolation, complete indifference, the capacity to contemplate, and absolute non-action.
>
> ...
>
> For the sake of Purusha's contemplation of Prakriti, and for its ultimate liberation, their union occurs. It is like the union of the lame and the blind. From this union, creation arises."
> *— Sankhya Karika, 11–21*

> *Neti neti* — "neither this, nor that."
> *— Brihadaranyaka Upanishad, II.3.6*

> "In the beginning was the Word, and the Word was with God, and the Word was God. He was in the beginning with God. All things were made through Him, and without Him nothing was made that was made."
> *— Gospel of John, 1:1–3*

---

## Abstract

This second volume of the Distinction Observable Theory (DOT; i.e. a theory of observable distinctions) demonstrates that the entire edifice of pure mathematics — numbers, algebraic operations, fundamental constants — is not imported from outside but **emanates** from the single nilpotent boundary operator $\partial$ ($\partial^2 = 0$) acting on the octahedral carrier $K(2,2,2)$ established in Part I. Beginning with the homological algebra of the gap (§19), we derive the Laplacian spectrum $(\lambda_0, \lambda_1, \lambda_2) = (0, 4, 6)$ and the universal projection invariant $\gamma = \sqrt{6}/9 \approx 0.27217$ (§20), from which the fine-structure constant $\alpha^{-1} \approx 137.036$ is calculated to seven significant digits (§21). The modular flow $SL(2,\mathbb{Z})$ on the upper half-plane emerges as the natural evolution of the distinction operator (§22). Prime numbers are shown to be indecomposable boundaries of $\partial$, while composite numbers are forms (§23). The full emanation atlas of mathematical operators — from addition and multiplication through differentiation and integration to Fourier and Mellin transforms — is derived from a single source (§24). Fractional charges ($1/3$, $2/3$) and confinement are proven as topological consequences of projecting dichotomy onto the triadic carrier (§25). The volume concludes with the bridge to physics: 64 binary vacuum configurations of $K(2,2,2)$ are classified into four defect sectors $\mathcal{D} \in \{0, 1/3, 1, 4/3\}$ with multiplicities $(10, 36, 12, 6)$ matching the particle content of the Standard Model (§26). No free parameters are introduced.

**Keywords:** boundary operator, nilpotency, spectral theory, fine-structure constant, modular forms, Hecke operators, arithmetic emanation, charge quantization, Standard Model.

**This is Part II of a three-part series.** Part I [arXiv:XXXX.XXXXX] establishes the octahedral carrier and the machine of distinction. Part III [arXiv:XXXX.XXXXX] performs the physical readout, including the complete particle spectrum and cosmological parameters.

---

## §19. Algebra of the Gap: $\partial^2 = 0$

In Part I, the carrier and the machine were assembled: six poles, twelve edges, eight faces, the operator $\partial$, projections, optics, and artifacts. In the closing sections of Part I, $\pi$, $i$, and $\nabla$ were already announced as emanations of the octahedral framework.

Part II fulfills this promise. It shows that **all pure mathematics** — numbers, operations, constants — are not brought in from outside but emanate from the single act of distinction.

The starting point is not a set of axioms or a formal system. The starting point is the operator $\partial$, already legalized in §10 of Part I as the action of the machine on the edges of the octahedron. Here we will show that its only property — **nilpotency** — generates not only homological algebra but also the entire subsequent hierarchy of mathematical structures.

---

### 19.0a. Protocol of Statuses in Part II

To avoid mixing rigorous derivation, external structural correspondence, and the DOT reading itself, three statuses are used below:

- **[D]** — strict derivation: the statement is directly derived from already fixed axioms, operators, or calculations.
- **[G1]** — strong structural correspondence: the statement is not a direct derivation but relies on a rigid structural coincidence with a known mathematical construction.
- **[G2]** — DOT reading / hypothesis: a strong reading or hypothesis that naturally follows from the DOT framework but is not yet closed as a theorem.

These statuses are used explicitly or by implication below.

---

### 19.0b. What Part II Inherits from the Machine

Part II does not build the carrier or launch the machine from scratch. It **inherits** the architecture already introduced in Part I and works on top of it.

From Part I, the following are transferred to the mathematical block:

- $6 = C_0$ — structural basis: the six poles of the octahedron;
- $12 = C_1$ — operational layer: edges as permissible acts of transition;
- $8 = C_2$ — contextual closure layer: faces as local context-cells;
- the prohibited center and the Borromean connectivity of the carrier.

From Part II of Part I:

- the ladder $1 \to 1|2 \to 2|3 \to 6 \to 12 \to 8$;
- distinction / split / closure as machine acts;
- optics ($1/2$, $2/3$, $3/4$) as reading modes, not as the carriers themselves;
- frame / shadow / tail / object as derivative artifacts of the machine.

Therefore, Part II should be read as follows:

- it **does not replace** the machine with mathematics;
- it shows how the already assembled machine begins to generate numbers, operators, constants, and algebraic structures;
- all formulas below are either direct algebraic readouts of the carrier or strong correspondences relying on the already introduced machine.

---

### 19.1. Definition of the Operator and Its Only Axiom

Let $\partial$ be a **homological boundary operator** in the category of chain complexes. Its only axiomatic property is:

$$\partial^2 = 0$$

This is not an abstract requirement. It is a direct consequence of the logical structure of distinction:

- Distinction draws a **boundary**.
- The boundary divides space into **two sides** (§8.2 of Part I: act $1|2$).
- But the boundary itself has **no side of its own**: the boundary of a boundary is empty.

If $\partial^2 \neq 0$, it would mean the boundary itself is subject to further fragmentation, leading to an infinite regress — a violation of the prohibition $FC^C$ (prohibition of an external foundation, §1.3 of Part I).

Thus, $\partial^2 = 0$ is not a mathematical convention but the **algebraic form of the prohibition of infinite support**.

---

### 19.2. Fundamental Inclusion and the Triadic Structure

From nilpotency, the fundamental inclusion follows immediately:

$$\operatorname{im} \partial \subset \ker \partial$$

Indeed: if $y = \partial(x)$, then $\partial(y) = \partial^2(x) = 0$, hence $y \in \ker \partial$.

This generates a **triadic structure** of the space on which $\partial$ acts:

1. **$\operatorname{im} \partial$** — **boundaries** (the image of the operator). Everything that is the result of an act of distinction. Everything that *has already been* sliced.
2. **$\ker \partial$** — **closed forms** (the kernel of the operator). Everything the operator cannot slice further. Everything that *for the operator* looks indistinguishable.
3. **$H = \ker \partial / \operatorname{im} \partial$** — **homologies** (the quotient space). The invariant part, the indestructible remainder. That which is closed but is not someone's boundary.

These three levels are linked by a **short exact sequence**:

$$0 \to \operatorname{im}\,\partial \to \ker\,\partial \to H \to 0$$

Exactness means the image of each mapping equals the kernel of the next. Nothing is added, nothing is lost. The sequence is a closed algebraic cycle.

---

### 19.2a. The Dual Pair $\partial \leftrightarrow \delta$

The boundary operator $\partial$ acts on **chains**: it transforms an object into its boundary. But for a full algebra of distinction, this is not enough. A second operator is needed — the **coboundary** operator $\delta$, acting on **cochains**:

$$\delta : C^n \to C^{n+1}$$

If $\partial$ answers the question *"what is the boundary?"*, then $\delta$ answers the question *"what higher context does this form allow?"*.

As with $\partial$, its own nilpotency holds:

$$\delta^2 = 0$$

This means: the context of a context does not create a new independent layer. The second superstructure collapses just like the boundary of a boundary.

On the space where both chains and cochains are defined, the operator of distinction closes into a **dual pair**:

$$\partial \; \leftrightarrow \; \delta$$

It is this pair that generates the discrete Laplacian:

$$\Delta = \partial \delta + \delta \partial$$

In DOT, this is important for two reasons:

1. **Shadow** ceases to be a purely geometric metaphor. It receives an operator reading as a part of the structure invisible to $\partial$ but active for $\delta$.
2. **Tail** ceases to be merely a visual remainder. It becomes a debt of inconsistency between the chain and cochain sides of the same local configuration.

Thus, the base algebra of DOT is built not on one operator, but on a pair:

$$\boxed{\partial^2 = 0, \qquad \delta^2 = 0, \qquad \Delta = \partial \delta + \delta \partial}$$

The operator $\partial$ sets the cut. The operator $\delta$ sets the context completion. Their non-reduction to each other generates the remainder that at later levels will be read as *shadow and tail*.

---

### 19.3. Combinatorial Dimension of the Operator: $\{2, 3\}$

In this triadic structure:

- **3 levels** (im, ker, H) — three qualitatively different statuses of a space element,
- but only **2 degrees of freedom**: $\operatorname{rank} \ker = \operatorname{rank} \operatorname{im} + \operatorname{rank} H$.

The third level (homology $H$) is **factored** — it is defined through the relationship of the first two.

This means that the basic combinatorial dimension of the operator $\partial$ is the pair $\{2, 3\}$:

- **Triadic depth** (three qualitative classes),
- **Two-dimensional effective freedom** (two independent ranks).

Here we see for the first time why the numerical pair $(2, 3)$ is inevitable, which will form the basis of all arithmetic (§23), and its product $2 \times 3 = 6$ — the basis of the Octahedron.

> **Note.** This is not a numerical coincidence. The operator $\partial$, by its algebraic structure, *forces* space to stratify into three layers with two degrees of freedom. This fact precedes any geometry, any coordinates, and any physics.

---

### 19.4. The Act of Distinction as a Projection of Boundary Ratios

What does the *application* of $\partial$ mean physically and mathematically?

The Act of Distinction is not an abstract "bit recording." In terms of homologies, it is the **slicing of a one-dimensional segment by an internal boundary**.

When we introduce a boundary into a continuous continuum, it divides it into exactly two parts. The only invariant metric of this Slice, its **unique topological address**, is the *ratio of the two resulting boundaries* — the two lengths or capacities separated by the limit. We record this act of Distinction as a **pair of numbers**.

This pair $\epsilon \in \{x^+, x^-\}$ is the record of the act. But how does it map onto geometry?

Since the Octahedron is not "physical space" itself but a projectional combinatorial screen, this single act (a segment with a boundary) possesses **projective duality**:

1. In one projection (Distinction of boundaries), this pair of numbers is mapped as **two opposite vertices** on an axis of the octahedron, and the act of Distinction itself as an empty axis between them.
2. In another projection (considering the isolated bounded continuum), this same segment can be perceived as a **face** (a geometric form) of a more complex structure.

Thus, the graph is born **not from points, but from projections of ratios** (distinctions of the continuum).

---

### 19.5. Syntax of Projections: Reading Topological Addresses

Since the Act of Distinction leaves behind a unique address (the ratio of boundaries), any space configuration can be clearly recorded in the form of a **topological barcode**. The basic syntax of the DOT Universe is as follows:

$$\text{Base} \;/\; \text{Projection} \;@\; \text{Operator}$$

In this record:

- **Base (numerator)** — the invariant topological combinatorics of the form (e.g., 56, 72, or 136). This is a configuration independent of the scale of observation.
- **Projection (denominator)** — the coefficient of the boundary ratio, the depth of the drift $\gamma$.
- **Operator (@)** — the rule of geometric stitching.

This means that the mass of a particle (e.g., the proton mass $136/\gamma^2$) is not a scalar value of a piece of matter. It is **literally the address of topological Slices**.

The power of the denominator ($\gamma^1$ or $\gamma^2$) strictly indicates the number of **intersections of independent boundaries**:

- If we have $\gamma^1$ (leptons, mesons) — we have an object formed by the projection of a single Distinction.
- If we have $\gamma^2$ (baryons) — we have the result of a double application of the boundary operator: the **intersection of two independent projections** ($\text{operator}_1 \circ \text{operator}_2$).

This is precisely why the "stitching" of a proton is fundamentally different from that of a meson. The intersection of two boundaries changes the very topological quality of the resulting object, closing its form (confinement) into a knot impenetrable to linear rupture.

Any formula of high-energy physics in DOT is read as a **script for assembling a topological matryoshka**.

---

### 19.6. Imaginary Unit $i$ as an Invisible Rotation within $\ker\,\partial$

From the triadic structure (§19.2), there follows the existence of the **operator kernel** $\ker\,\partial$ — a space where $\partial$ vanishes.

Topologically, $\partial$ annihilates cycles (closed paths). But **within** the vanished space ($\ker\,\partial$), movements are possible that do not change the boundary. The operator $i$ (a 90° rotation) takes a state in $\ker\,\partial$ and transforms it into a completely different state that **to $\partial$ looks exactly the same**.

Formally:

$$i: V \to V^{\perp}, \quad \|i(v)\| = \|v\|, \quad \partial(i(v)) = \partial(v) = 0$$

This is the quantum superposition $\psi = a + ib$. The phase $ib$ is **invisible to the macro-observer** until a measurement is made.

The imaginary unit is not a mathematical convention or a "convenient notation." It is the **only operator permissible within the invisible horizon of the kernel $\partial$**. It is not introduced but emanates from the structure $\partial^2 = 0$:

- $\partial^2 = 0$ creates $\ker\,\partial$.
- $\ker\,\partial$ contains forms indistinguishable to the observer.
- The only permissible transformation between indistinguishable forms is a norm-preserving rotation.
- This rotation is $i$.

This is precisely why complex numbers are not an "extension" of real numbers. They are the **algebraic remainder** of the nilpotency of $\partial$: the closed space $\ker\,\partial$ is wider than its subspace of boundaries $\operatorname{im}\,\partial$, and this gap accommodates exactly one internal rotation — the imaginary unit.

---

### 19.7. Levels of Emanation (Hierarchy of Intersections)

The order of emanation of elementary particles in the Universe is strictly dictated by the number of boundary intersections of the operator $\partial$. We observe this in the form of the exponent $\gamma^k$ in the mass formula denominator:

**Level 1 (Single rupture, $\gamma^1$):** Leptons (electron, muon, tau) and Mesons (pion, kaon). They represent a single boundary projected into space. This is the primary emanation: leptons are truly elementary, while mesons are unstable (a single boundary is easy to destroy by fluctuation).

**Level 2 (Intersection of two boundaries, $\gamma^2$):** Baryons (Proton, Neutron). The intersection of two groups of coefficients means that two independent acts of observation have intersected, overlapping each other. A topological knot of confinement is born. It is this double intersection that makes the proton an absolutely and eternally stable particle.

The following macro-emanations (atoms, molecules) are built on this foundation, increasing the complexity of intersections.

---

### 19.8. Spectral Operator of the Carrier: Spin 1/2 as a Topological Entity

How can an Observer see the one-dimensional boundary of the operator $\partial$ (a prime number $p$) if this boundary itself is an invisible abstract limit?

DOT mathematics gives an unambiguous answer: **the essence of a boundary is known only through the act of its manifestation on the objects of space.** When the operator $\partial$ introduces an invisible entity (axis $D$) into the Vacuum, this entity manifests in strictly one way — it **forcibly divides space into TWO opposites**.

This projection of an invisible boundary axis onto two symmetrical measures is called **Spin 1/2** in 20th-century physics. Spin 1/2 is not the rotation of a material ball; it is a purely topological property: *the division of an entity into two geometric opposites (Fermion)*.

From here arises the main beauty of the method: as soon as we correctly record the **spectral operator of the carrier** (the Laplacian on the octahedron graph $\Delta = 4I - A$), we no longer need to introduce separate external parameters. By calculating the geometric **imbalance of the axes**, we obtain the spectrum of eigenvalues $\{0, 4, 6\}$, which then unfolds into the further numerical apparatus of DOT through subsequent carrier-, metric-, and modular-readouts. In the publishable corpus, it is important to maintain this status: the Laplacian gives the spectral core, not automatically the entire physical derivation without intermediate bridges.

---

### 19.9. Summary of §19

§19 has fixed:

- The only axiom: $\partial^2 = 0$, and its origin from the prohibition of infinite regress ($FC^C$).
- The triadic structure ($\operatorname{im}\,\partial$, $\ker\,\partial$, $H$) and the short exact sequence.
- The combinatorial dimension of the operator $\{2, 3\}$: three levels with two degrees of freedom.
- The Act of Distinction as a projection of the boundary ratio and the syntax of topological addresses.
- The imaginary unit $i$ as the only permissible rotation within $\ker\,\partial$.
- The hierarchy of emanation ($\gamma^k$) and Spin 1/2 as a projection of an invisible boundary.

> **§19 does not introduce either the graph geometry, the spectrum, or the numbers. It lays down the algebra — the only genetic code from which all mathematics will be derived in §20–§26.**

---

## §20. Spectral Theorem of the Octahedron

In §19, the algebraic structure of the operator $\partial$ was established: nilpotency, triadic stratification, combinatorial dimension $\{2, 3\}$. Now this algebra must acquire **geometric realization** — a specific graph on which the operator $\partial$ works.

This section proves that the **spectrum of the Laplacian** of this graph uniquely determines masses, massless modes, and the basic fractions of the entire theory.

---

### 20.1. Construction of the Graph from $k$ Orthogonal Acts of $\partial$

Let the operator $\partial$ be applied $k$ times, each time along an **independent** (orthogonal) direction. This creates $k$ binary distinctions:

$$({\pm e_1}),\ ({\pm e_2}),\ \dots,\ ({\pm e_k})$$

Each act of $\partial$ generates a pair of antipodal poles $+e_i$ and $-e_i$: the two sides of a single boundary (§8.2 of Part I: act $1|2$).

**Adjacency Rule.** Two elements $\epsilon_i \in \{+e_i, -e_i\}$ and $\epsilon_j \in \{+e_j, -e_j\}$ are connected (interact) if and only if they belong to **different** axes ($i \neq j$). Elements of the same axis ($+e_i$ and $-e_i$) are **not connected** to each other — they are two sides of a single boundary, not two independent objects.

This is exactly the definition of a **complete $k$-partite graph** $K(\underbrace{2,\dots,2}_k)$ with $k$ groups of 2 vertices each.

Total vertices: $2k$. Each vertex is connected to everyone except its antipode. Vertex degree: $d = 2(k-1)$.

---

### 20.2. Isomorphism with the Cross-polytope

**Statement.** The graph $K(\underbrace{2,\dots,2}_k)$ is isomorphic to the 1-skeleton of a $k$-dimensional cross-polytope (hyperoctahedron).

*Justification.* A cross-polytope in $\mathbb{R}^k$ has $2k$ vertices $\{\pm e_1, \dots, \pm e_k\}$. Two vertices are connected by an edge if and only if they are **not antipodal** (not $\pm e_i$ for the same $i$). Antipodal pairs are exactly the partite groups of $K(2,\dots,2)$. Adjacency rules coincide. $\square$

For $k = 3$: $K(2,2,2)$ = **octahedron** — 6 vertices, 12 edges, each vertex has degree 4.

This is the very octahedron derived in §6 of Part I from the Borromean linkage of prohibitions. Now we see its **second birth** — from the purely algebraic properties of the operator $\partial$.

---

### 20.3. Spectral Theorem (Rigorous Proof)

The graph Laplacian $L = D - A$ is a discrete matrix implementation of the homological Laplacian $\Delta = \partial\delta + \delta\partial$ on the graph's vertices.

**Theorem (Laplacian Spectrum of $K(2,\dots,2)$).** For a complete $k$-partite graph $K(\underbrace{2,\dots,2}_k)$, $k \geq 2$, the non-zero eigenvalues of the Laplacian operator $L = D - A$ are:

$$\lambda_1 = 2(k-1), \quad \text{multiplicity } k$$
$$\lambda_2 = 2k, \quad \text{multiplicity } k-1$$

*Proof.*

Each vertex of the graph $K(2,\dots,2)$ is connected to all vertices except its antipode, i.e., it has degree $d = 2(k-1)$.

The adjacency matrix $A$ of the graph $K(2,\dots,2)$ has eigenvalues:

- $2(k-1)$ with multiplicity 1 (the all-ones vector),
- $-2$ with multiplicity $k-1$ (inter-group contrasts),
- $0$ with multiplicity $k$ (intra-group contrasts).

The Laplacian $L = dI - A = 2(k-1)I - A$, hence the eigenvalues of $L$:

- $\lambda_0 = 2(k-1) - 2(k-1) = 0$ (multiplicity 1),
- $\lambda_1 = 2(k-1) - 0 = 2(k-1)$ (multiplicity $k$),
- $\lambda_2 = 2(k-1) - (-2) = 2k$ (multiplicity $k-1$). $\square$

---

### 20.4. Corollaries of the Spectral Theorem

**Corollary 1. Ratio of Non-Zero Eigenvalues:**

$$\frac{\lambda_1}{\lambda_2} = \frac{k-1}{k}$$

This is an exact algebraic theorem, true for all $k \geq 2$. Not an approximation or a fit — pure algebra.

| $k$ | Graph | $\lambda_1/\lambda_2$ |
|:---:|:---|:---:|
| 2 | square $K(2,2)$ | $1/2$ |
| 3 | octahedron $K(2,2,2)$ | **$2/3$** |
| 4 | 16-cell $K(2,2,2,2)$ | $3/4$ |
| 5 | pentacross | $4/5$ |

At $k = 3$, the ratio **2/3** arises — the **fundamental fraction** of the entire theory.

**Corollary 2. Dimension of the Non-Trivial Spectrum.**

The total dimension of non-trivial subspaces:

$$\dim V_1 + \dim V_2 = k + (k-1) = 2k - 1$$

At $k = 3$: $\dim V_1 + \dim V_2 = 3 + 2 = \mathbf{5}$. The full space of non-trivial states of the octahedron is **five-dimensional**.

If DOT network operators act on a 5-dimensional state space ($S_0 \dots S_4$), then this space is now *derived* from the Laplacian spectrum as $\mathcal{S} = V_1 \oplus V_2$.

---

### 20.5. Characteristics of Eigenvectors: The Nature of Mass

The eigenspaces of the Laplacian have a clear physical meaning:

**$V_1$ ($\lambda_1 = 2(k-1)$, axial modes):**

The eigenvectors have the form $x_{+e_i} = -x_{-e_i}$ (the values at the ends of the axis are **opposite**). These are *dipole, antisymmetric* oscillations. The distinction on the axis is **preserved** — pure translation along the axis.

Physical interpretation: **mass = 0**. The dipole mode carries information without creating a remainder.

**$V_2$ ($\lambda_2 = 2k$, inter-axial modes):**

The eigenvectors have the form $x_{+e_i} = x_{-e_i}$ (the values at the ends of the axis **coincide**). These are *quadrupole, symmetric* oscillations. The distinction on the axis has "collapsed" — both poles carry the same signal, generating **inter-axial frustration** — an irreducible internal tension.

Physical interpretation: this is exactly what **mass** is.

> **Mass** ($\|\Pi_2(x)\|$) has a precise meaning: it is the amplitude of the quadrupole (symmetric) component, i.e., the amplitude of the unresolved inter-axial tension.

The purely mathematical remainder — the projection onto the subspace $V_2$ — is exactly what the observer perceives as inertia.

---

### 20.6. Decomposition of an Arbitrary Signal and Definition of the Defect

Let $\Pi_0, \Pi_1, \Pi_2$ be orthogonal projectors onto the subspaces $V_0, V_1, V_2$, respectively. For an arbitrary signal $x \in \mathbb{R}^{2k}$, the canonical decomposition is:

$$x = \Pi_0(x) + \Pi_1(x) + \Pi_2(x)$$

where $\Pi_0 + \Pi_1 + \Pi_2 = I$ (the identity matrix).

**Definition of the Defect.** A signal $x$ is called **resonant** (with respect to the axial structure) if $\Pi_2(x) = 0$, i.e., $x$ lies entirely in $V_0 \oplus V_1$. In this case, the defect is zero.

If $\Pi_2(x) \neq 0$, a **non-zero remainder** $r = \Pi_2(x)$ arises, orthogonal to the axial subspace and minimal in norm. This remainder **cannot be eliminated** without changing the graph structure (adding or removing edges).

**Interpretation.** In this model, the norm of the remainder $\|r\| = \|\Pi_2(x)\|$ is identified with what is measured in physical applications as **mass** (or mass defect). Resonant configurations ($r = 0$) correspond to massless or perfectly closed structures.

---

### 20.7. The 2/3 Projection as the Operator's Background ($k = 3$)

At $k = 3$, the graph $K(2,2,2)$ is the octahedron. Its spectral ratio is:

$$\frac{\lambda_1}{\lambda_2} = \frac{4}{6} = \frac{2}{3}$$

The **2/3 projection** is the **internal spectral filter** of the operator $\partial$ at $k = 3$.

Any signal decomposed into the eigenmodes of the $K(2,2,2)$ graph is distributed between the subspaces $\lambda_1 = 4$ (dimension 3) and $\lambda_2 = 6$ (dimension 2) with an energy ratio of 2/3.

This is **not an external constant** but a spectral characteristic of the minimal self-closed structure of three orthogonal distinctions.

The 2/3 ratio is the same invariant already discovered in §12.3 of Part I as the "triadic aperture." Now we see its rigorous origin: it is the **eigenvalue** of the spectral problem on the $K(2,2,2)$ graph.

> **Observer's Paradox.** An observer inside the Octahedron perceives the 2/3 projection not as a ratio, but as **background** — as the very fabric of the space in which they exist. The 2/3 projection is simultaneously:
> - the **background** of the operator (spectral characteristic of the $K(2,2,2)$ graph),
> - the **optics** of the observer (internal filter of perception).

---

### 20.8. Numerical Invariants of the Octahedron

The $K(2,2,2)$ graph generates a series of numerical invariants calculated from the spectrum.

**Number of Spanning Trees** (by Kirchhoff's theorem):

$$\tau = \frac{1}{6} \prod_{i=1}^{5} \lambda_i = \frac{1}{6} \cdot 4^3 \cdot 6^2 = \frac{1}{6} \cdot 64 \cdot 36 = 384$$

**General Formula for $K(2,\dots,2)$ with $k$ groups:**

$$\tau(k) = \frac{1}{2k} \cdot [2(k-1)]^k (2k)^{k-1}$$

| $k$ | Graph | $\lambda_1/\lambda_2$ | $\tau$ (spanning trees) |
|:---:|:---|:---:|---:|
| 2 | square $K(2,2)$ | $1/2$ | 4 |
| 3 | octahedron $K(2,2,2)$ | **$2/3$** | **384** |
| 4 | 16-cell $K(2,2,2,2)$ | $3/4$ | 82,944 |
| 5 | pentacross | $4/5$ | 32,768,000 |

The number 384 allows for a remarkable factorization:

$$384 = 1728 \times \frac{2}{9}$$

where $1728 = 12^3$ (the cube of the number of octahedron edges), and $2/9$ is an additional spectral invariant that will reappear in §21 as the square of the geometric invariant $\gamma$.

---

### 20.9. Note on $k = 1$: The Degenerate Case

At $k = 1$, the $K(2)$ graph is a single edge. The Laplacian has a single non-zero eigenvalue $\lambda = 2$. The ratio $\lambda_1/\lambda_2$ is not defined (there is no second non-zero eigenvalue).

The case $k = 1$ is **degenerate**: distinction exists, but without an orthogonal pair, there can be neither spectral structure nor filtration. This is the state of pre-geometric distinction — a pure cut without architecture.

---

### 20.10. Summary of §20

§20 has fixed:

- The construction of the $K(2,\dots,2)$ graph as the unique geometric consequence of $k$ orthogonal acts of $\partial$.
- Isomorphism with the cross-polytope.
- The **Spectral Theorem** of the Laplacian on $K(2,\dots,2)$ with a rigorous proof.
- The ratio $\lambda_1/\lambda_2 = (k-1)/k$, and at $k=3$: **2/3** as a fundamental spectral invariant.
- The nature of **mass** as the norm of the projection $\|\Pi_2(x)\|$ (amplitude of inter-axial tension).
- Numerical invariants: 384 spanning trees, factorization through $1728 = 12^3$.

> **§20 is the mathematical core of the whole theory. Here, from a single axiom ($\partial^2 = 0$), we rigorously derived the graph, its full spectrum, and the nature of mass as an algebraic remainder. No additional postulates were required.**

---

## §21. Geometric Invariant $\gamma$ and the Fine-Structure Constant $\alpha$

In §20, the spectral theorem for the $K(2,2,2)$ graph was proven and the 2/3 ratio was obtained as a fundamental spectral invariant. But the spectrum is not the only information encoded in the Octahedron. Its **metric geometry** (edge lengths, angles, area ratios) generates another fundamental constant — $\gamma$.

It is important here to remember the machine context of Part I: `6`, `12`, `8` have already been introduced as structural, operational, and contextual carriers. Therefore, $\gamma$ in this section should be read not as an abstract constant "from geometry in general," but as a **metric readout of the already assembled machine**.

---

### 21.1. Derivation of the Invariant $\gamma$

An octahedron inscribed in a unit sphere ($R = 1$) has an edge length of:

$$\ell = \sqrt{2}$$

(This follows from the fact that all edges connect vertices of the form $\pm e_i$ and $\pm e_j$ ($i \neq j$), the distance between which is $|\pm e_i - \pm e_j| = \sqrt{1 + 1} = \sqrt{2}$.)

The face of an octahedron is an equilateral triangle with side $\sqrt{2}$. Its area is:

$$S_{\triangle} = \frac{\sqrt{3}}{4} \cdot (\sqrt{2})^2 = \frac{\sqrt{3}}{2}$$

The total surface area of the octahedron (8 faces):

$$S_{\text{total}} = 8 \cdot \frac{\sqrt{3}}{2} = 4\sqrt{3}$$

For subsequent physics, edge length alone is not enough. A value is needed that simultaneously takes into account:

- the **measure of distinction** (edge),
- the **measure of internal maintenance** (face depth),
- and the **normalization for the framework dimension** ($k = 3$).

For an octahedron inscribed in a unit sphere, the inradius (distance from the center to the face center) is:

$$r_{\text{in}} = \frac{1}{\sqrt{3}}$$

Then the natural metric invariant of a single face is defined as:

$$\gamma = \frac{\ell \cdot r_{\text{in}}}{k}$$

Substituting $\ell = \sqrt{2}$, $r_{\text{in}} = 1/\sqrt{3}$, and $k = 3$, we get:

$$\gamma = \frac{\sqrt{2}\cdot \frac{1}{\sqrt{3}}}{3} = \frac{\sqrt{6}}{9}$$

Thus, the geometric invariant is defined as the normalized product of the measure of Distinction and the measure of Depth:

$$\boxed{\gamma = \frac{\sqrt{6}}{9} \approx 0.27216552698}$$

This is an exact algebraic value. It is determined **only by the geometry** of the inscribed octahedron and does not depend on scale, unit system, or physical observations.

Important: $\gamma$ does not follow from pure nilpotency $\partial^2 = 0$ without intermediate steps. It appears after the nilpotent machine receives its **first metric realization** on the $K(2,2,2)$ carrier. Therefore, $\gamma$ is not a primary axiomatic parameter but the first rigorous **metric invariant** of the already realized machine.

---

### 21.2. Square of the Invariant: $\gamma^2 = 2/27$

$$\gamma^2 = \frac{6}{81} = \frac{2}{27}$$

This number lies at the heart of the **lever formula** (§26), and its presence in various physical ratios carries deep meaning:

- The numerator $2$ — dichotomy (the binary act of distinction, the first prime number).
- The denominator $27 = 3^3$ — the cube of three-dimensionality (the third power of the number of axes).
- The ratio 2/27 is the measure of **incommensurability** between the dichotomic act and the volumetric framework.

---

### 21.3. Corollaries of the Invariant $\gamma$

**[D] Koide Invariant:**

The Koide formula for the masses of charged leptons ($e, \mu, \tau$) has the form:

$$K_4 = \frac{(\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau})^2}{m_e + m_\mu + m_\tau} = \frac{2}{3}$$

In DOT, this is not an empirical fit but an **identity**:

$$K_4 = \frac{2}{3} = 9\gamma^2$$

The Koide invariant is a ninefold square of the geometric invariant of the Octahedron. The factor 9 = $3^2$ reflects the square of three-dimensionality, through which lepton masses are linked to the face area.

**[D] Weinberg Angle (bare):**

$$\sin^2\theta_W = \frac{2}{9} = 3\gamma^2$$

Error: 0.44% relative to the value in the $\overline{MS}$ scheme.

Physical meaning: the octahedron and its dual cube possess **9 planes of symmetry**. In the strongest current geometric reading of DOT, 2 of these 9 planes are read as the electromagnetic sector, and the remaining 7 as the weak sector. The Weinberg angle then acts as a **measure of duality** between the octahedron and the cube, captured in the geometric invariant.

---

### 21.4. Fine-Structure Constant $\alpha$

**[D]** DOT derives the inverse value of $\alpha$ from Octahedron geometry and the modular $j$-invariant:

$$\alpha^{-1} = \frac{432}{\pi} - \frac{47\gamma}{27}$$

Or, in canonical notation:

$$\alpha^{-1} = \frac{j(i)}{4\pi} - \frac{(|2O|-1) \cdot \gamma^3}{2}$$

Breaking down each element:

| Parameter | Value | Role |
|:---|---:|:---|
| $432 = 2^4 \cdot 3^3$ | Ramanujan Pixel | $j(i)/4 = 1728/4$ |
| $j(i) = 1728 = 12^3$ | $j$-invariant of the elliptic curve with $\tau = i$ | Modular form characteristic |
| $\|2O\| = 48$ | Full group of octahedron symmetries | $(48-1) = 47$ — number of non-trivial elements |
| $\gamma^3$ | Volumetric unit of the octahedron | Third power of the edge, projected onto the unit sphere |

**[G1] Note on the number 47.** The number $47 = 48 - 1$ here should be read not as an arbitrary fit, but as the strongest structural reading of finite octahedral symmetry: the identity element of the group $\|2O\|$ gives the pure carrier contribution, while the other $47$ elements provide the cumulative non-trivial correction-term. In the language of the neighbor-boundary law, this same reading takes the form:

$$ \frac{47}{48}=1-\frac{1}{48}, $$

where $48$ acts as the full group-capacity of the carrier, and $1/48$ as the minimal irreducible debt of closure. This strengthens the geometric interpretation of the correction-term but does not replace the representation-theoretic proof of the character-sum.

**[D] Algebraic Core of the Number 47.** For the full octahedral symmetry group of the carrier:
\[ |O_h|=48. \]
If the vacuum carrier is read through the regular representation \(\mathbb C[O_h]\), and the pure symmetric vacuum through the trivial representation \(V_{\mathrm{triv}}\), then the space of the non-trivial carrier-response is:
\[ V_{\mathrm{fric}}=\mathbb C[O_h]\ominus V_{\mathrm{triv}}, \]
and therefore:
\[ \dim V_{\mathrm{fric}}=48-1=47. \]
This is a rigorous algebraic fact: the number `47` is the dimension of the non-trivial response-space of the carrier after extracting the pure vacuum subspace. The full algebraic fixation of this fact is also set in `§42.1`, included in the code of algebraic closures of Part VI.

**[G1] Connection with \(\alpha^{-1}\).** The fact that this specific dimension enters the correction-term:
\[ \alpha^{-1}=\frac{432}{\pi}-\frac{47\gamma}{27}, \]
remains the strongest current physical identification. The algebra of the number `47` is already closed, but the bridge to a specific electromagnetic correction-term still requires a separate representation-theoretic or character-sum argument.

Why does $j(i)$ appear in the formula? The point $\tau = i$ is the fixed point of the inversion $S: z \mapsto -1/z$ from the modular ladder in §22. It is the minimal self-dual modular node where the square sub-carrier ($k=2$) and the octahedral carrier ($k=3$) first agree through the same rotational center. The value:

$$j(i) = 1728 = 12^3$$

is thus not brought in from outside: it fixes the cubic power of the edge carrier of the octahedron. In this formula, $j(i)$ plays the role of a modular analog for the same structural body described in graph language through the 12 edges.

**Origin of the Number 432.** This number is not accidental. It is determined in two ways simultaneously:

1. **Arithmetic path:** $432 = 2^4 \times 3^3$. This is the product of the fourth power of dichotomy and the cube of three-dimensionality — the maximum "multiplicative volume" in the coordinates of the first two prime numbers.
2. **Modular path:** $432 = j(i)/4$, where $j(i) = 1728 = 12^3$ — the famous $j$-invariant of the elliptic curve with period $\tau = i$ (the imaginary unit). The number 1728 is the cube of the number of Octahedron edges (12).

The interaction of these two paths — arithmetic and modular — generates $\alpha$.

**Numerical Result:**

$$\alpha^{-1}_{\text{DOT}} = \frac{432}{\pi} - \frac{47 \times 0.27216552698}{27} \approx 137.5094 - 0.4734 = 137.0360$$

$$\alpha^{-1}_{\text{CODATA}} = 137.0360$$

**Error: $0.00007\%$.**

---

### 21.5. Schwinger Term: Anomalous Magnetic Moment of the Electron

**[D]** The first correction to the magnetic moment of the electron:

$$\frac{g-2}{2} \approx \frac{\alpha}{2\pi} \approx \frac{1}{864} = \frac{2}{j(i)}$$

The number 864 = $2 \times 432$. Here, $1/864$ should be understood as a **canonical lattice approximation** to the first correction, not as an exact identity with the physical value of $\alpha/(2\pi)$. In DOT, this number is read as the **structural lattice-reading** of the Schwinger term, i.e., as the nearest discrete aperture on the Ramanujan pixel grid.

The doubling ($2 \times 432$) reflects the dipole nature (spin 1/2) of the electron: the magnetic moment is "read" from two poles of the axis, each seeing half of the 432 pixel.

---

### 21.6. Relationship between $\gamma$, $\alpha$, and the Laplacian Spectrum

Let us show how the three key constants are interconnected:

| Constant | Definition | Source |
|:---|:---|:---|
| 2/3 | $\lambda_1/\lambda_2$ on $K(2,2,2)$ | Spectral theorem (§20) |
| $\gamma = \sqrt{6}/9$ | Metric geometry of an inscribed octahedron | Definition (§21.1) |
| $\alpha^{-1}$ | $432/\pi - 47\gamma/27$ | Modular arithmetic (§21.4) |

Key observation:

$$9\gamma^2 = \frac{2}{3} = \frac{\lambda_1}{\lambda_2}$$

That is, **the square of the metric invariant multiplied by 9 equals the spectral invariant**. This is not a coincidence. The number 9 = $3^2$ — the square of the space dimension — effects the transition from the metric of a single face ($\gamma$) to the spectrum of the entire graph (2/3).

Furthermore, $\alpha^{-1}$ is calculated as a modular correction to the "pure" field contribution $432/\pi$. The correction $47\gamma/27$ is the geometric friction due to the finiteness of the symmetry group ($|2O| = 48$, minus the identity element = 47), projected onto the volumetric invariant $\gamma/27 = \gamma^3/\gamma^2$.

---

### 21.7. Proton (136) and the Fine-Structure Constant: Topological Friction

From the mass passport (to be considered in detail in Part III): $m_p / m_e \approx 136/\gamma^2$ (error 0.008%). The basis of the proton is the number **136**.

In the natural sequence, immediately following the ideal baryonic node (136), is **137 — a prime number** (the 33rd). In DOT, a prime number is an absolute, indecomposable 1D boundary (§19.4).

The famous fine-structure constant $\alpha \approx 1/137.036$ is not a magically fitted parameter. In DOT, it is the **coefficient of topological surface tension**: a measure of the resistance experienced by a closed baryonic knot (136) when in contact with the nearest indecomposable vacuum boundary (137).

Electromagnetic interaction is born geometrically as an **edge effect** of baryonic confinement — the friction constant at the boundary between the world of forms (composite numbers, baryons) and the world of pure axes (prime numbers, vacuum).

Notation: $\alpha^{-1}_{\text{bare}} = 432/\pi \approx 137.510$, while the experimental $\alpha^{-1}_{\text{exp}} \approx 137.036$. The difference (0.474) is the quantum-field correction for the "polarization" of the vacuum wall (137) by the baryon.

---

### 21.8. Summary of §21

§21 has fixed:

- The geometric invariant $\gamma = \sqrt{6}/9$ as a strictly derivable constant from the metric of an inscribed octahedron.
- Its square $\gamma^2 = 2/27$ and its connection with the Koide invariant ($9\gamma^2 = 2/3$) and the Weinberg angle ($3\gamma^2 = 2/9$).
- The fine-structure constant formula $\alpha^{-1} = 432/\pi - 47\gamma/27$ with an accuracy of 0.00007%.
- The connection of the number 432 with the $j$-invariant of modular forms ($432 = j(i)/4$) and the number of Octahedron edges ($1728 = 12^3$).
- The physical interpretation of $\alpha$ as a measure of topological friction at the boundary between form and vacuum.

> **§21 turns the abstract spectral theorem of §20 into a set of specific numbers that will be used in Part III for the precise calculation of particle masses. Here, mathematics already interfaces with physics, but the mass tables are compiled only in Part III.**

---

## §22. Evolution of the Operator through the $SL(2,\mathbb{Z})$ Ladder

In §§19–21, the static properties of the operator $\partial$ and its spectrum on the $K(2,2,2)$ graph were established. But this structure does not appear instantly. It goes through a **ladder** — an evolutionary path from a degenerate state ($k=1$) to full closure ($k=3$).

This section shows that the ladder $k = 1 \to 2 \to 3$ **does not look like an arbitrary sequence** but allows for a natural reading through the algebraic logic of the modular group generators.

---

### 22.1. The Modular Group $SL(2,\mathbb{Z})$

The structures induced by the operator $\partial$ at each level $k$ allow for representation through the action of the fractional linear transformation group $SL(2,\mathbb{Z})$ on the projective line $\mathbb{P}^1$:

$$f(z) = \frac{az + b}{cz + d}, \quad ad - bc = 1, \quad a,b,c,d \in \mathbb{Z}$$

The group $SL(2,\mathbb{Z})$ is generated by **two generators**:

- $T: z \mapsto z + 1$ (shift / addition),
- $S: z \mapsto -1/z$ (inversion / division).

*[G1]* The development of the operator $\partial$ from $k=1$ to $k=3$ allows for a reading as the **sequential inclusion** of these generators.

---

### 22.2. Step 1: $k = 1$ (T-shift only)

**Generator:** $z \mapsto z + 1$.

**Spectrum:** degenerate. The only non-zero eigenvalue $\lambda = 2$. The ratio $\lambda_1/\lambda_2$ is **not defined** (there is no second non-zero eigenvalue).

**Structure:** an infinite discrete chain ($\mathbb{Z}$) generated by a single generator. Each vertex has exactly one neighbor on each side. Closure is impossible.

**View from within the 2/3 projection:** a purely linear form without internal geometry. Distinction exists but has neither an orthogonal pair, nor a spectral structure, nor filtration.

This is the pre-distinguished state — a single "cut" without architecture. Analogous to the distinction position before stabilization in §2 of Part I.

---

### 22.3. Step 2: $k = 2$ (S-inversion added)

**Generator:** $z \mapsto -1/z$.

**Spectral ratio:** $\lambda_1/\lambda_2 = 2/4 = 1/2$.

**Structure:** square $K(2,2)$ — 4 vertices, 4 edges. $2 \times 2$ matrices, emergence of a second pole.

**View from within the 2/3 projection:** a world capable of a cut ($T$) and scale inversion ($S$) but still **incapable of full closure**. The spectral ratio $1/2$ differs from the background 2/3, meaning the structure does not yet resonate with the observer.

At this level, distinction between "inside" and "outside" is first possible ($S$ flips the scale). But the third axis — the axis of closure — is not yet legalized.

---

### 22.4. Step 3: $k = 3$ (Full $SL(2,\mathbb{Z})$ Group: $T$ and $S$ together)

**Generators:** joint action of shift and inversion. The group is closed.

**Spectral ratio:** $\lambda_1/\lambda_2 = 4/6 = 2/3$.

**Structure:** octahedron $K(2,2,2)$. Three fixed points: $0, 1, \infty$ — the cusps of the fundamental domain of the modular group.

**Isomorphism $\Gamma(2)$.** The modular curve $X(2) = \mathbb{H}/\Gamma(2)$ has exactly 3 cusps. The quotient group $SL(2,\mathbb{Z})/\Gamma(2) \cong S_3$ is the permutation group of the three octahedron axes.

*[G1]* Thus, the $K(2,2,2)$ octahedron can be read as the **discrete combinatorial skeleton** of the modular curve $X(2)$.

**View from within the 2/3 projection:** the only dimension perceived as **complete**, since its spectral ratio matches the observer's background. The observer is "embedded" in this structure — they see 2/3 not as a fraction, but as the world itself.

---

### 22.5. Summary Table of Operator Evolution

| Parameter | $k=1$ | $k=2$ | $k=3$ |
|:---|:---:|:---:|:---:|
| Generators | $T$ | $T, S$ | $T, S$ (closed) |
| Graph | edge $K(2)$ | square $K(2,2)$ | octahedron $K(2,2,2)$ |
| Vertices | 2 | 4 | 6 |
| Edges | 1 | 4 | 12 |
| Degree | 1 | 2 | 4 |
| $\lambda_1/\lambda_2$ | undefined | $1/2$ | **$2/3$** |
| Cusps $X(k)$ | 1 | 2 | **3** |
| Closure | no | no | **yes** |

---

### 22.6. Infinitesimal Algebra of the Triad

After establishing the macroscopic evolution ($k = 1 \to 2 \to 3$), it is necessary to describe the *internal dynamics* on the fully deployed graph ($k = 3$). For this, we return to the triad of primal bases from §7 of Part I: Distinction (D), Fixation (F), Connection (C).

#### 22.6.1. Generators of the Flow

For small parameters $\epsilon \to 0$, the dynamics are described by three generators:

- $G_{DF}$: transfer Distinction → Fixation.
- $G_{DC}$: transfer Distinction → Connection.
- $G_{FC}$: transfer Fixation → Connection.

For the composition $COMP = A_{FC}(\gamma) \circ A_{DC}(\beta) \circ A_{DF}(\alpha)$, the triad components transform as follows:

$$\begin{aligned}
r_1' &= (1-\gamma)(r_1 + \alpha\, r_2) \\
r_2' &= (1-\beta)(1-\alpha)\, r_2 \\
r_3' &= r_3 + \beta(1-\alpha)\, r_2 + \gamma\, (r_1 + \alpha\, r_2)
\end{aligned}$$

#### 22.6.2. Spectrum and Attractor

The matrix of the full flow $G$ has a spectrum of $\{0,\; -c,\; -(a+b)\}$.

- **The zero value** corresponds to the preservation of the invariant (norm of the sum).
- **Negative values** prove that any deviation towards Distinction or Fixation **decays exponentially**, tending towards the pure state of Connection ($0, 0, 1$).

This is a fundamental result: **the algebra of the flow has a single attractor — Connection.**

Physical interpretation: in the absence of external influence, the system inevitably drifts towards the dominance of the third component (Connection). In the terms of §7 of Part I, this is Action / Actualization — an autonomous progression that does not need a subject.

#### 22.6.3. Minimum $r_3'$ and Triad Collapse

**Lemma.** The minimum $r_3'$ across the entire state space $\Delta^2$ (simplex) is:

$$\min_{r \in \Delta^2} r_3' = \min\!\big(\gamma,\; (1-\alpha)\beta + \alpha\gamma\big)$$

This means that for $\alpha, \beta, \gamma > 1/3$, the third component (Connection) **guaranteedly** becomes the dominant one, exceeding the threshold of equal distribution.

Algebraic meaning: as soon as all three transfer parameters exceed 1/3 (one-third — the measure of equal distribution among three components), the system "collapses" into a regime where Connection inevitably dominates. In physical terms, this is **confinement**: a closed action from which no exit is possible without an external "rupture."

---

### 22.7. Relationship of the Modular Ladder to the Triad

The three steps of the modular ladder ($k = 1, 2, 3$) reflect the inclusion of the three flow generators:

| Step | $SL(2,\mathbb{Z})$ Generator | Triad Generator | What Emerges |
|:---:|:---:|:---:|:---|
| $k=1$ | $T$ (shift) | $G_{DF}$ | Distinction → boundary |
| $k=2$ | $S$ (inversion) | $G_{DC}$ | Scale inversion → orthogonality |
| $k=3$ | $T \circ S$ (closure) | $G_{FC}$ | Fixation → Connection → confinement |

At each step, the spectral ratio $\lambda_1/\lambda_2 = (k-1)/k$ gets closer to one but never reaches it. At $k = 3$, the 2/3 ratio matches the observer's background, and the system **optically closes**: the observer ceases to "see" the $k < 3$ structure as a separate object.

---

### 22.8. Mathematical Summary of §9 of the Original Source

There exists a model in which the structures induced by the operator $\partial$ ($\partial^2 = 0$) allow for representation through the action of the group $SL(2,\mathbb{Z})$ on the projective line.

The operator develops from $k=1$ (degenerate, shift only) through $k=2$ (inversion, spectrum $1/2$) to $k=3$ (full closure, spectrum $2/3$). At $k=3$, the graph Laplacian $L = D - A$ is identically equal to the homological $\partial_1 \partial_1^T$.

In this context, the **2/3 projection** acts simultaneously as:

- the **background** of the operator (spectral characteristic of the $K(2,2,2)$ graph),
- the **optics** of the observer (internal filter of perception).

At the Part II level (carrier, spectral lever, and early mass-readouts), it can be organized based on:

1. Nilpotency $\partial^2 = 0$,
2. Formation of the $K(2,\dots,2)$ graph from $k$ orthogonal axes,
3. Spectral theorem $\lambda_1/\lambda_2 = (k-1)/k$,
4. Filtration of the orthogonal projection remainder $\Pi_2(x)$.

At this level, no additional physical entities are introduced; the carrier, operator, spectrum, and optics are sufficient.

---

### 22.9. Summary of §22

§22 has fixed:

- The development of the operator $\partial$ along the ladder $k = 1 \to 2 \to 3$ as the sequential inclusion of the $T$ and $S$ generators of the modular group $SL(2,\mathbb{Z})$.
- The $K(2,2,2)$ octahedron as the discrete skeleton of the modular curve $X(2)$, with the quotient group $S_3$.
- The infinitesimal algebra of the triad ($G_{DF}, G_{DC}, G_{FC}$), the spectrum $\{0, -c, -(a+b)\}$, and the single attractor — Connection.
- The triad collapse at $\alpha, \beta, \gamma > 1/3$ as the algebraic mechanism of confinement.
- Full self-consistency: spectrum, modular group, infinitesimal algebra — three languages for describing a single object.

> **[G1] §22 shows that the octahedron is the first point on the modular ladder considered where the spectral filter matches the observer's background: $\lambda_1/\lambda_2 = 2/3$. Within this ladder, any other $k$ is either not closed ($k < 3$) or does not resonate with the observer ($k > 3$).**

---

## §23. Arithmetic of the Boundary Operator

In §§19–22, the algebra of the operator $\partial$ was established, the $K(2,2,2)$ graph was built, the spectral theorem was proven, and the modular evolution was traced. All this apparatus operated with graph-theoretic and algebraic objects.

Now we ask: **where do the numbers themselves come from?** Why is "6" not a calculator button but a topological invariant? Why is "136" not a random figure but an address? This section transforms arithmetic from a language of description into an **object of the theory**.

---

### 23.1. Arithmetic of Ruptures: Prime and Composite Numbers

From the syntax of projection depth (§19.5), a strong consequence follows: arithmetic can be read not as an external language of description but as an internal layer of DOT itself.

In continuous topology (the working environment of 20th-century physics over the field of real numbers $\mathbb{R}$), the boundary is blurred. In DOT topology, **the Act of Distinction is always discrete**. A rupture creates two integer (discrete) boundaries, and their ratio is always rational ($p/q$). Therefore, DOT formulas are read through the arithmetic of integers.

In this mathematical foundation:

1. **Prime numbers are Pure Axes (Boundaries).** A prime number cannot be mathematically divided (factorized). It is impenetrable. In DOT topology, prime numbers ($2, 3, 5, 7, 11, 13, 17$) act as the **fundamental axes** (vectors) of the boundary operator $\partial$. Each prime number is a one-dimensional, indecomposable vector of a specific act of observation.

2. **Composite numbers are Topological Configurations (Forms).** A composite number can be factorized. Geometrically, this means that any composite number is a volume, area, or network stretched over a framework of prime axes.

---

### 23.2. Factorization of Base Numbers as Geometric Dismantling

Let's see how the base constants of particles (the numerator / Base from the syntax of §19.5) factorize:

- **Lepton Base (56)** = $2^3 \times 7$. This is a configuration: 3D-dichotomy ($2^3 = 8$ faces) projected onto the 7th axis of combinatorial independence.
- **Meson Base (72)** = $2^3 \times 3^2$. This is a geometric volume: the eight faces of the octahedron multiplied by the square of the 3rd axis (the space of axes D, F, C).
- **Baryon Base (136)** = $2^3 \times 17$. These are the 8 faces of the Vacuum, tightly closed on the 17th prime axis (the highest Eddington limit).

The composite number of the base in DOT formulas is not a random fitting constant. It is a **readable topological recipe**. Factorization (the decomposition of a number into prime factors) is equivalent to the **literal geometric dismantling of a physical particle into a set of fundamental rupture axes**. The Universe is engaged in the decomposition of graphs into prime factors.

---

### 23.3. The Natural Sequence as a Topological Synopsis of the Universe

If prime numbers are one-dimensional discrete boundaries (ruptures) and composite numbers are multi-dimensional continuous projections (forms), then the true meaning of the most basic mathematical object opens up before us.

**The natural sequence ($1, 2, 3, 4, 5, 6, 7, \dots$) is a highly compressed synopsis of the unfolding of the Universe's dimensions.**

The structure of the sequence through the lens of the DOT operator:

- In the natural sequence, discrete objects (prime numbers) and continuous configurations (composite ones) strictly **alternate**.
- The fundamental axiom of homologies states: $\partial^2 = 0$. The boundary of a boundary is zero. This means that **two discrete boundaries cannot exist in succession without an encompassing space between them**.
- And this is precisely what we see in Arithmetic: with the exception of the coordinate start (2 and 3, where dichotomy itself is born), **prime numbers never follow one after another**. They are always separated by composite numbers — continuous volumes that these boundaries compress.

The natural sequence is not an abstract sequence of "identical elements." In the DOT reading, it is the densest record of the alternation of Acts of Distinction (prime limits) and the filling of spaces (composite forms).

---

### 23.4. Why Space is Three-Dimensional: Singularity of the Pair $(2, 3)$

> **Corollary [G2]:** Notice the unique anomaly at the start of the natural sequence: **2 and 3 are the only prime numbers in all of infinite mathematics that follow one after another.**

This means that mathematics allows the existence of two "touching" discrete boundaries without space between them **ONLY at the very start of coordinates**.

This is an absolute topological singularity. The fundamental rupture (2, dichotomy) and its orthogonal intersection (3, volume) are permanently welded together.

*[G2]* This is precisely why the physical Vacuum has macroscopically frozen in the form of **Three-Dimensional Space (3)**, woven from **Binary dichotomies (2)**. The $K(2,2,2)$ graph is the inevitable geometric consequence of the fact that the numbers 2 and 3 are the only neighbor-ruptures in the Universe. Beyond that, starting from 5, Nature is obliged to insert empty spaces (composite numbers).

> ⚠️ **Note on the hypothesis:** The fact of the uniqueness of the pair $(2, 3)$ is rigorous (the proof is trivial: 2 is the only even prime, the next odd 3 is prime, and the next odd 5 is 2 away from 3). But the conclusion "therefore space is three-dimensional" is an interpretation, not a theorem. We record the observation: the $K(2,2,2)$ structure is algebraically inevitable at $k=3$, and the $(2, 3)$ pair is unique. However, a rigorous derivation of $k=3$ from the $\partial^2=0$ axioms has not yet been obtained.

---

### 23.5. Topological Scanner: Counting $1 \to 12$

If we accept that prime numbers are the introduction of new orthogonal axes (boundaries), and composite numbers are the generation of configurations on these axes, then the **act of counting** $1, 2, 3, \dots, N$ itself acts as a protocol for the quantum assembly of matter.

Let's scan the natural sequence from 1 to 12. We will see how the $K(2,2,2)$ geometry (Vacuum) is rendered step by step:

- **1** — pre-vacuum ($k=0$). A singularity without distinctions. The neutral element of multiplication.
- **2 (Prime)** — Act 1. **Dichotomy.** Emergence of an axis with two poles.
- **3 (Prime)** — Act 2. **Orthogonality.** The only case where a new axis is introduced immediately, without a structural gap ($gap = 1$).
- **4 (Composite, $2^2$)** — The first geometric form. Square of dichotomy (2D framework).
- **5 (Prime)** — Act 3. The first spatial limit.
- **6 (Composite, $2 \times 3$)** — The first orthogonal intersection of axes. Geometry: **6 vertices of the Octahedron**.
- **7 (Prime)** — Act 4. Limit of the differential structure.
- **8 (Composite, $2^3$)** — Dichotomy interwoven thrice. Geometry: **8 faces of the Octahedron** (8 spinors, fermion base).
- **9 (Composite, $3^2$)** — Square of the space axes. Meson base ($72 = 8 \times 9$).
- **10 (Composite, $2 \times 5$)** — 10 massless states in the Laplacian spectrum on the octahedron (Generation 0 from §20).
- **11 (Prime)** — Act 5.
- **12 (Composite, $2^2 \times 3$)** — A two-dimensional framework stretched in volume. Geometry: **12 edges of the Octahedron**.

Counting $1 \to 12$ is not an abstraction. It is a rigorous topological log of program execution: first, 6 vertices are highlighted ($N=6$), then 8 spinach-faces are stretched ($N=8$), and finally, the structure is linked by 12 edges ($N=12$), completing the construction of the basic 3D world.

---

### 23.6. First Composite Triplet $[8, 9, 10]$: The Base Code of the Octahedron

The twin prime pattern reveals an unexpected regularity. Between the first pair $(5, 7)$ and the second $(11, 13)$ stand exactly **three** composite numbers: $[8, 9, 10]$.

Let's uncover the internal anatomy of this "first generation of space":

1. **$8 = 2^3$**: The exact topological volume of a cube/octahedron. **8 spinors**, $K(2,2,2)$, the basic configuration of all fermions. Eight is dichotomy (axis 2) **interwoven with itself three times**. Raising a prime number to a power in DOT means the topological self-intersection of an axis in orthogonal dimensions. From a one-dimensional rupture $\partial$, a volumetric figure is born. The lepton base is generated from here ($56 = 8 \times 7$).

2. **$9 = 3^2$**: **Square** of the axes (axis 3 interwoven with itself twice). This is the exact combinatorial base of all Mesons in DOT ($72 = 8 \times 9$).

3. **$10 = 2 \times 5$**: Exactly **10 massless states** in the Laplacian spectrum on the octahedron (Generation 0 from §20.3). This is a linear intersection of different independent axes — dichotomy (2) and the first spatial limit (5).

**Corollary on the Operation of Exponentiation:**

In traditional arithmetic, exponentiation ($p^n$) is simply repeated multiplication. In DOT geometry, it is the generation of a multi-dimensional space from a single fundamental axis. When a prime boundary crosses itself orthogonally, the "fabric" of a particle arises. Factorization of a composite number is a literal geometric blueprint of which axes (prime numbers) and how many of their self-intertwining (powers) a quantum object is assembled from.

The first composite gap $[8, 9, 10]$ consists of non-abstract numbers. These are the **base code of the Octahedron topology $K(2,2,2)$**. The entire basic structure of the Standard Model (fermions, mesons, massless states) is written in the very first gap between twin prime numbers.

---

### 23.7. Second Composite Triplet $[14, 15, 16]$

Let's look at the next triplet, standing between the pair $(13, 17)$ — before the third generation:

1. **$14 = 2 \times 7$**: Intersection of the dichotomy and the 7th axis. Arithmetically, $56 = 4 \times 14$, i.e., the lepton base contains 14 as a building block.

2. **$15 = 3 \times 5$**: Intersection of the three-dimensional vacuum (3) and the 5th axis.

3. **$16 = 2^4$**: Dichotomy interwoven four times (hypercube). Arithmetically, $136 = 8 \times 17$, and $16 + 1 = 17$.

> ⚠️ **Note:** The coincidence $2^4 + 1 = p_{\text{Eddington}}$ may be significant, but *[G2]* the causal link ("16 forms the proton") is not yet proven — it remains an observation requiring justification.

Each composite triplet forms its own unique scale of relationships. Nature fractally projects these relationships onto different levels of intersection, and the **geometric meaning of these composite clusters is what we physically call "generations or families of particles."** A particle's properties are the properties of its composite factorization.

---

### 23.8. Multiplication as Structure, Addition as Collapse into Background

What does the difference between the two basic arithmetic operations mean geometrically?

1. **Multiplication ($2 \times 3 = 6$):** Means **preservation of orthogonality**. Distinction is maintained. Two axes have intersected at a right angle and created a rigid *structure* (6 vertices of the Octahedron). In the Laplacian spectrum, this corresponds to the subspace $V_1$ (antisymmetrical modes where the distinction of the axis poles is preserved). Multiplication is a pure operation in the algebra over $\mathbb{F}_1$.

2. **Addition ($2 + 3 = 5$):** Distinction has *flattened*, collapsed! Two axes have "fallen" onto each other. The internal structure (the orthogonal angle between them) is destroyed. The operation of addition creates a single indecomposable monolith — **a new prime axis**, which henceforth functions as a smooth, structureless Background (Vacuum limit). In the Laplacian spectrum, this corresponds to the subspace $V_2$ (symmetrical modes where distinction on the axis has collapsed, giving rise to inertia/tension).

A prime number is a **"scar" left by dimensions previously flattened into the background**. And a composite number is a "crystal" where dimensions held their orthogonality through multiplication.

---

## §24. Emanation Atlas of Mathematical Operators

In §23, we showed that numbers are not labels but topological instructions. Now it is necessary to show that **operations** on numbers equally emanate from the $\partial$ structure.

In this section, it is especially important to distinguish statuses: some of the operators are derived directly from the $\partial$ structure and the octahedron's carrier, while others are specified as a **strong structural correspondence** between the DOT layers and known algebraic languages.

This section represents a **complete layered atlas** — a catalog of mathematical operators organized by the depth (layer) of their emanation. Each layer is denoted by the fraction $\Omega_{n/(n+1)}$, where the numerator and denominator indicate the lower and upper bounds of the horizon.

Below, it is useful to keep in mind the following correspondence:

- `C_0 = 6` gives machine poles and binary statuses;
- `C_1 = 12` gives edge acts and the operational fan;
- `C_2 = 8` gives local closure-cells and the first contextual cycles.

Therefore, the operator atlas of Part II does not hang in a vacuum: each layer below will in one way or another rely on the `6/12/8` carriers already introduced in the machine.

**[G1] The Bose–Mesner bridge of the carrier.** The $K(2,2,2)$ graph allows for not only a Laplacian reading (§20) but also a standard algebraic packaging as a strongly regular carrier. In this language, the primitive idempotents of the Bose–Mesner algebra play the same role as the spectral projectors $\Pi_0, \Pi_1, \Pi_2$: they divide the space of functions on the vertices into the fundamental sectors of the carrier. For DOT, this is important as a second algebraic support: the operator atlas below does not introduce new entities but only unfolds the already existing projector structure of the finite graph-algebra.

---

### 24.1. Layer $\Omega_{0/1}$ — Vacuum Points: The Birth of Distinction

The first layer is the origin of coordinates. Only the act $\partial$ and its immediate consequences exist here.

| Object | Designation | Definition in DOT | Role |
|:---|:---:|:---|:---|
| **Zero** | $0$ | $\ker\,\partial \cap \operatorname{im}\,\partial$ | Vacuum point: that which is simultaneously a boundary and closed |
| **One** | $1$ | Neutral element $\partial^0$ | Identical act (pre-distinction) |
| **Prime number** | $p$ | Indecomposable 1D act $\partial$ | Axis / boundary |
| **NOT** | $\neg$ | The only Boolean operation acting on one bit | Inversion of a pole along an axis |

#### 24.1.1. Topological Anatomy of NOT ($\neg$)

The $\neg$ operator (negation) is the simplest of all operators. It switches the pole on one axis ($+e_i \leftrightarrow -e_i$) without affecting other axes.

On the $K(2,2,2)$ graph: $\neg$ is the **transposition of vertices of one part**: $(+e_i, -e_i) \to (-e_i, +e_i)$.

- Number of vertices affected: 2.
- Number of edges affected: 0 (the edge between $\pm e_i$ does not exist; edges to other axes are only reassigned).
- $\neg^2 = 1$ (applying twice returns the original).

NOT is a projection of the $\partial$ operator onto one axis. It does not create or destroy any links or structures — it only **changes the sign of the distinction**. This is the purest form of Distinction (D), without Fixation (F) and without Connection (C).

Physical projection: replacing a particle with an antiparticle ($C$-inversion) along one charge axis.

---

### 24.2. Layer $\Omega_{1/2}$ — Boolean Logic: The Fabric of Edges

The second layer emerges when two poles of **different** axes are first connected by an edge. Binary (two-input) logical operations appear.

| Object | Designation | Definition in DOT | Role |
|:---|:---:|:---|:---|
| **AND** | $\wedge$ | Intersection of two poles | Connection |
| **OR** | $\vee$ | Union of two poles | Choice |
| **XOR** | $\oplus$ | Symmetric difference | Octahedron edge |
| **Kronecker Delta** | $\delta_{ij}$ | $1$ if $i=j$, otherwise $0$ | Metric tensor |

#### 24.2.1. XOR as an Octahedron Edge

XOR ($a \oplus b = (a \wedge \neg b) \vee (\neg a \wedge b)$) is the only binary operation that returns $1$ if and only if the inputs are **different**. On the $K(2,2,2)$ graph, two poles $\varepsilon_i$ and $\varepsilon_j$ (from different axes) are connected by an edge if and only if they are distinguishable ($i \neq j$).

Thus, the **adjacency matrix of the octahedron is the XOR table** on the axial indices.

#### 24.2.2. Why there is NO addition here

At Layer $\Omega_{1/2}$, there are only **two** axes. Addition ($a + b$ with a carry) is impossible: a carry requires a **third** dimension — where to "carry" the excess. Two-dimensional logic ($K(2,2)$) is fully described by AND, OR, XOR, NOT — without arithmetic.

This explains why pure digital logic (transistor gates) works only with Boolean operations: it operates at the level of two distinctions, before the emergence of a third axis.

#### 24.2.3. Links and Dipole Forms

Each edge of the octahedron is a **link** between two poles of different axes. This link creates a **dipole**: a pair in which one pole attracts ($+$) and the other repels ($-$). Examples from physics: electric dipole, magnetic dipole. In DOT, a dipole pair is the simplest form of **Connection (C)** from the triad in §7 of Part I.

From §23.2: composite numbers in the range of Layer $\Omega_{1/2}$ are $4 = 2^2$ (square of dichotomy, self-intersection of an axis).

---

### 24.3. Layer $\Omega_{2/3}$ — Arithmetic: The Birth of Three-Dimensionality

The third layer is critically important: here the **third** axis first appears, and with it — the operation of **addition**.

| Object | Designation | Definition in DOT | Role |
|:---|:---:|:---|:---|
| **Addition** | $+$ | Collapse of two axes into a scalar via a third | Transfer of distinction to the Background |
| **Multiplication** | $\times$ | Orthogonal intersection of axes | Preservation of Structure |
| **Imaginary unit** | $i$ | Rotation inside $\ker\,\partial$ (§19.6) | Superposition |
| **Number $\pi$** | $\pi$ | Limit of the ratio of a cycle to its radius | Measure of closure |
| **Spin** | $\times_G$ | Grassmann product on a graph | $\mathfrak{su}(2)$ |
| **Contour integral** | $\oint$ | Sum along a closed path | Full cycle traversal |

#### 24.3.1. Addition: Transfer (Carry) to the Third Dimension

Why is addition impossible without a third axis?

Consider $1 + 1$ in the binary system. The result = $10_2$ — a two-digit number. The "carry bit" must be sent to the next digit. But the "next digit" is an **orthogonal position**, requiring a new dimension.

In the $K(2,2)$ graph (square), there is nowhere to carry — all axes are exhausted. In the $K(2,2,2)$ graph (octahedron), a third axis appears, and the carry is allowed. Thus, the operation of addition (and all arithmetic) **is born only at $k \geq 3$**.

#### 24.3.2. Multiplication on a Graph: Crossing Axes into a Face

If addition is the collapse of axes into the Background (§23.8), then multiplication is the **intersection of axes at a right angle** with the formation of a face:

$$e_i \times e_j = \text{face } (i,j) \in K(2,2,2), \quad i \neq j$$

The result of multiplication is a **two-dimensional object** (the face of a triangle) stretched over two edges. This is pure Structure, in contrast to addition.

On the octahedron, 8 faces are exactly $2^3$ possible intersections of three axes considering the sign: $(\pm e_1) \times (\pm e_2) \times (\pm e_3) = 8$ octants.

#### 24.3.3. Imaginary Unit $i$: Detailed Realization

In §19.6, it was shown that $i$ is the only operator inside $\ker\,\partial$. At Layer $\Omega_{2/3}$, it acquires a specific embodiment:

$i$ is a **rotation by $\pi/2$ in the plane** of two axes, which transforms a real vector into one perpendicular to it without changing the magnitude. Two such rotations ($i^2 = -1$) reverse the sign — inverting the pole.

Superposition $\psi = a + ib$ means: the observable part ($a$, projection on $\Pi_1$) and the unobservable part ($b$, rotation inside $\ker\,\partial$) coexist for the observer. The number of phase turns per unit of path length ($\frac{d\theta}{ds}$) is the wave number of the particle.

#### 24.3.4. Spin as a Grassmann Product

Spin $1/2$ (§19.8) at Layer $\Omega_{2/3}$ acquires an algebraic realization:

$$\times_G: V \otimes V \to \Lambda^2(V) \cong \mathfrak{su}(2)$$

The Grassmann (anticommutative) product of two axial vectors generates a bivector — the generator of rotation. On the octahedron, three bivectors $e_1 \wedge e_2$, $e_2 \wedge e_3$, and $e_1 \wedge e_3$ form the Lie algebra $\mathfrak{su}(2)$ — the algebra of spin.

This is the direct origin of quantum mechanics from the graph structure: three faces of the octahedron containing a common vertex define three generators $\sigma_x, \sigma_y, \sigma_z$ (Pauli matrices).

Here also arises the geometric reading of the **Pauli principle**. In Grassmann algebra:

$$v \wedge v = 0$$

This means: two completely coinciding fermion configurations do not create a new valid bivector. Their self-intersection is identically destroyed. In DOT, this is the algebraic prohibition on the double occupation of the same antisymmetric state.

#### 24.3.5. Number $\pi$ and Circular Limit

The number $\pi$ emerges as the **limit of a continuous traversal of a closed cycle** on the graph. Specifically: if one traverses the face of an octahedron (a triangle) and measures the ratio of the path length to the radius of the circumscribed circle, then by increasing the number of edges (moving to an increasingly fine approximation), this ratio tends toward $\pi$.

$\pi$ appears at Layer $\Omega_{2/3}$ and not earlier because a closed cycle requires at least **three** vertices (and therefore three axes) — there are no cycles at Layer $\Omega_{1/2}$.

#### 24.3.6. Spinor: Basic Unit of the Octahedron

An octahedron face is an equilateral triangle of three vertices. Each of the three vertices can be $+$ or $-$ (two poles). Total: $2^3 = 8$ types of faces. These are the **8 spinors** — the basic unit of the fermion structure.

Spinor = minimum closed cycle on the octahedron with a fixed pole orientation.

---

### 24.4. Layer $\Omega_{3/4}$ — Delocalization and Fields: The Birth of Continuity

At the fourth layer, the discrete graph structure begins to **delocalize** — fields grow out of point objects.

| Object | Designation | Definition in DOT | Role |
|:---|:---:|:---|:---|
| **Gradient** | $\nabla$ | Map of $\partial$ drift along axes | Non-equilibrium vector |
| **Curl (Rotor)** | $\nabla \times$ | Closed circulation of $\partial$ around faces | Source of rotation |
| **Number $\pi$** (unfolded) | $\pi$ | Full measure of a circle / limit of cyclicity | Normalization of continuous modes |
| **Phase operator** | $e^{i\theta}$ | Rotation by $\theta$ in $\ker\,\partial$ | Gauge transformation |
| **Green's function** | $L^+$ | Pseudo-inverse of the Laplacian | Non-local "response" of the graph to perturbation |
| **Propagator** | $B_{3/4}$ | $L^+ = (L + \Pi_0)^{-1} - \Pi_0$ | Propagation of a defect |

#### 24.4.1. Gradient as a Difference Operator

On the $K(2,2,2)$ graph, the gradient $\nabla f$ for the function $f: V \to \mathbb{R}$ is defined through the **differences** in values at the ends of the edges:

$$(\nabla f)_{ij} = f(v_i) - f(v_j) \quad \text{for edge } (v_i, v_j)$$

This is a discrete analog of the continuous gradient. In the transition to the limit (fine-grained lattice), the usual $\nabla$ is restored.

#### 24.4.2. Curl and Maxwell's Equations

At Layer $\Omega_{3/4}$, a closed cycle (an octahedron face) generates the circulation $\nabla \times$. The condition $\partial^2 = 0$ in the continuous limit take the form:

$$\nabla \cdot (\nabla \times \mathbf{F}) = 0 \quad \Leftrightarrow \quad \partial^2 = 0$$

These are **Maxwell's equations** — they do not need to be postulated. They are the continuous limit of graph nilpotency.

#### 24.4.3. Propagator $B_{3/4}$ as Green's Function

The pseudo-inverse of the Laplacian $L^+$ is the operator that "responds" to a point perturbation. On the $K(2,2,2)$ graph:

$$L^+ = (L + \Pi_0)^{-1} - \Pi_0$$

This operator describes how a perturbation at one vertex propagates to all others. In the continuous limit, $L^+$ turns into the Green's function — the core of Maxwell's equations.

#### 24.4.4. Proton Base (136) as a 17-Dimensional Structure

At Layer $\Omega_{3/4}$, objects of increased dimension appear for the first time.

The number $136 = 2^3 \times 17$. If $8 = 2^3$ is a 3D spinor (8 faces of the octahedron), then $17$ adds **another axis**. Result: $136$ is an object with $136$ distinguishable configurations projected onto the graph.

The number $136 = \binom{17}{2} + 17 = 136$ is the number of elements of an **upper-triangular $17 \times 17$ matrix**. Eddington was the first to notice this relationship and interpreted 136 as the number of fundamental degrees of freedom.

In DOT, this is not mysticism: $136$ is the topological address of the baryon structure, equal to the number of independent components of a symmetric tensor of dimension $17$.

---

### 24.5. Layer $\Omega_{4/5}$ — Global Symmetries: Closure of Arithmetic

At the fifth layer, **global** operators grow out of local ones — acting on the entire infinite structure.

| Object | Designation | Definition in DOT | Role |
|:---|:---:|:---|:---|
| **Hecke Operators** | $T_n$ | Averages over sublattices of index $n$ | Multiplicative unfolding |
| **Infinity** | $\infty$ | Limit $k \to \infty$ in $\lambda_1/\lambda_2 = (k-1)/k$ | Spectrum horizon |
| **$j$-invariant** | $j(\tau)$ | Modular function, $j(i) = 1728 = 12^3$ | Curve's passport |
| **Leech lattice $\Lambda_{24}$** | $\Lambda_{24}$ | Unique unimodular lattice in $\mathbb{R}^{24}$ | Superstructure |

#### 24.5.1. Hecke Operators: Multiplicative Unfolding

Hecke operators $T_n$ are defined as **sums over sublattices** of a given lattice of index $n$:

$$T_n f(\tau) = n^{k-1} \sum_{ad=n,\; 0 \leq b < d} f\left(\frac{a\tau+b}{d}\right)$$

Their key property is **multiplicativity**: $T_m T_n = T_{mn}$ when $(m, n) = 1$. This means that Hecke operators **inherit the structure of prime number multiplication**.

In DOT, Hecke operators are the algorithm by which one basic cell of the octahedron "remultiplies" into all scales. Each prime $p$ defines its own operator $T_p$, and the composition $T_p \circ T_q$ (for different $p, q$) gives $T_{pq}$ — exactly reproducing the factorization of composite numbers from §23.2.

#### 24.5.2. $j$-Invariant and the Number $1728$

The $j$-invariant is a function that uniquely classifies elliptic curves (tori):

$$j(\tau) = \frac{E_4(\tau)^3}{\Delta(\tau)}$$

where $E_4$ is an Eisenstein series and $\Delta$ is the modular discriminant.

For $\tau = i$ (imaginary unit):

$$j(i) = 1728 = 12^3$$

The number $1728$ is the **cube of the number of octahedron edges** ($12^3$). This is not a random coincidence: a modular curve with $\tau = i$ has **maximal symmetry** (automorphism group of order 2), and this symmetry generates exactly the same invariant as the cube of the $K(2,2,2)$ edge structure.

The number $432 = 1728/4$ (Ramanujan pixel) is $j(i)$ divided by 4 (the number of $K(2,2)$ vertices), i.e., the $j$-invariant **projected** from a 3D torus onto a 2D square. It is this number that is destined to become the numerator of the $\alpha$ formula.

#### 24.5.3. Leech Lattice $\Lambda_{24}$

The Leech lattice is a unique unimodular lattice in $\mathbb{R}^{24}$ without roots of length $\sqrt{2}$. Its connection to the octahedron:

$$24 = 2k \cdot (2k-1)|_{k=3} + 1 = 6 \cdot 5 - 6 = 24$$

More accurately: $24 = 8 \times 3$ (8 spinors × 3 axes). The number $24$ is the dimension of the "unfolded" octahedron, where each face (spinor) is provided with a full set of axial coordinates.

The theta-function of the Leech lattice:

$$\Theta_{\Lambda_{24}}(q) = 1 + 196560q^2 + 16773120q^3 + \dots$$

The coefficient $196560 = 2^4 \cdot 3^3 \cdot 5 \cdot 7 \cdot 13$ — contains exactly those prime numbers that make up the fundamental alphabet of DOT (§4 of Part III).

---

### 24.6. Layer $\Omega_{5/6}$ — Absolute Scaling: Renormgroup and Adeles

The sixths and final layer, where mathematics "returns to itself" — the emanation cycle closes.

| Object | Designation | Definition in DOT | Role |
|:---|:---:|:---|:---|
| **Renormgroup** | $\beta(g)$ | Scaling flow | How the structure changes when the scale changes |
| **Adeles** | $\mathbb{A}_\mathbb{Q}$ | $\mathbb{R} \times \prod_p \mathbb{Q}_p$ | Union of all prime "lenses" |

#### 24.6.1. Renormgroup Beta-Function

The Renormgroup is an operator describing how physical constants (connection constants) change when the scale of observation changes.

In DOT, a change of scale is a change of depth $k$ in the formula $1/\gamma^k$. Each "step" in $k$ is a transition to the next level of $K(2,2,2)$ self-embedding.

The beta-function $\beta(g) = \mu \frac{dg}{d\mu}$ describes how the "virtual viscosity" of the operator changes at the boundary of the intersection of two scales. The connection constant ("charge") is not a fixed number but a function of the scale of observation. The Renormgroup is an operator that turns a fixed constant into a field of scale dependence.

#### 24.6.2. Adeles $\mathbb{A}_\mathbb{Q}$: Union of All Prime Horizons

The Adelic ring $\mathbb{A}_\mathbb{Q}$ is the product:

$$\mathbb{A}_\mathbb{Q} = \mathbb{R} \times \prod_{p \text{ is prime}} \mathbb{Q}_p$$

Each prime number $p$ defines its own **$p$-adic lens** ($\mathbb{Q}_p$) through which it "sees" the number sequence. The Adelic ring unites **all** these lenses — all DOT axes — into a single object.

In DOT, adeles are the **final horizon**: a structure where all prime axis-boundaries coexist simultaneously, forming the full spectrum of the Vacuum. The Adelic approach is mathematics that "sees all faces of the octahedron at once," without choosing any of them.

Euler's product formula for the zeta function:

$$\zeta(s) = \prod_{p \text{ is prime}} \frac{1}{1 - p^{-s}}$$

— is a direct Adelic decomposition: each factor $(1 - p^{-s})^{-1}$ is the contribution of one prime axis to the full spectrum.

---

### 24.7. Summary Table of the Emanation Atlas

| Layer $\Omega$ | Horizon | Key Objects | Graph | Spectrum |
|:---:|:---|:---|:---:|:---:|
| $0/1$ | Vacuum points | $0, 1, p, \neg$ | $K(2)$ | degenerate |
| $1/2$ | Boolean logic | AND, OR, XOR, $\delta$ | $K(2,2)$ | $1/2$ |
| $2/3$ | Arithmetic | $+, \times, i, \pi, \text{Spin}$ | $K(2,2,2)$ | **$2/3$** |
| $3/4$ | Fields | $\nabla, \nabla\times, e^{i\theta}, L^+$ | continuous limit | — |
| $4/5$ | Global symmetries | $T_n, j(\tau), \Lambda_{24}$ | modular curve | — |
| $5/6$ | Absolute scaling | $\beta(g), \mathbb{A}_\mathbb{Q}$ | adelic space | — |

---

### 24.8. Key Principle of the Atlas: Layer $\Omega_{2/3}$ as the Fixation Zone

From the table in §24.7, it can be seen that the **physical world** (arithmetic, spin, mass) is fixed precisely at Layer $\Omega_{2/3}$. The lower layers ($\Omega_{0/1}, \Omega_{1/2}$) are "preparatory" structures that do not have enough dimension to realize physics. The upper layers ($\Omega_{3/4}, \Omega_{4/5}, \Omega_{5/6}$) are a "superstructure" that delocalizes, globalizes, and scales what was fixed at $\Omega_{2/3}$.

The $K(2,2,2)$ octahedron is the **focal point** of the entire atlas: the only structure on which addition, multiplication, the spectral ratio 2/3, 8 spinors, and 12 bosonic edges all simultaneously exist.

---

### 24.9. Summary of §24

§24 has fixed:

- A full layered atlas of mathematical operators ($\Omega_{0/1}$ — $\Omega_{5/6}$).
- NOT as the simplest projection of $\partial$, XOR as an octahedron edge.
- Impossibility of addition when $k < 3$ (absence of a third axis for carry).
- Spin as a Grassmann product, $i$ as rotation in $\ker\,\partial$, $\pi$ as limit of circular traversal.
- Delocalization: gradient, curl, Green's function as continuous limit of graph operators.
- Hecke operators as multiplicative unfolding of prime axes.
- $j$-invariant and the number $1728 = 12^3$ as the cube of the edge structure.
- Renormgroup as the scale dependence operator, adeles as the union of all prime horizons.
- Layer $\Omega_{2/3}$ as focal point of the atlas — zone of physical fixation.

> **[G1] §24 is the periodic table of mathematical operators. Each operator occupies its place in the DOT hierarchy of distinctions, and none are introduced as an arbitrary external axiom.**

---

## §25. Topological Anatomy of Fractions and Confinement

In §23, we established that prime numbers are indecomposable axis-boundaries and composite ones are forms. In §24, it was shown how these objects are organized into layers of emanation. Now we ask: **where do fractional charges come from?** Why does a quark carry a charge of $1/3$ or $2/3$ rather than an integer? And why is it **impossible** to observe fractional states in a free form?

---

### 25.1. Fraction as a Projection of Dichotomy onto a Three-Dimensional Framework

A fraction $p/q$ in DOT is not an abstract mathematical relationship. It is the **projection of an act of distinction (numerator) onto a structural framework (denominator)**.

Consider the simplest case. An Act of Distinction (§19) is a dichotomous rupture ($p = 2$). it acts on a three-axis framework ($q = 3$). The projection of one binary act onto three orthogonal axes:

$$\frac{2}{3}$$

This fraction is not the result of division. it is a **measure of the incommensurability** between dichotomy (which is always binary) and volume (which is three-dimensional).

The $2/3$ fraction means: a binary operator applied to a three-dimensional structure "covers" two axes out of three. The third axis remains **unobservable** — in the shadow (§12 of Part II).

Similarly:

- $1/3$ — one act of distinction is projected onto one of the three axes (quark charge).
- $2/3$ — two acts cover two of the three axes (antiquark charge).

---

### 25.2. Homological Torsion and Color Charge

The denominator of the fraction ($q = 3$) is rigid — it is determined by the dimension of the framework ($k = 3$ axes of the octahedron). The numerator ($p = 1$ or $2$) is determined by the choice of axes onto which the act is projected.

Algebraically, this should not be read as a direct embedding of $\mathbb{Z}_2 \hookrightarrow \mathbb{Z}_3$ — there is no such injective homomorphism. It is more correct to say this:

- the dichotomous act lives on the binary carrier of choice;
- the triadic frame lives on the cyclic carrier of three positions;
- when projecting a binary choice onto a triadic carrier, an **irreducible remainder modulo 3** arises.

It is precisely this remainder that is written in the language of the cyclic group:

$$\mathbb{Z}/3\mathbb{Z}$$

That is, the color remainder is not the image of the "embedded two," but a **remainder class** after the projection of the binary act onto the triadic framework. It is not eliminated by any purely dichotomous action because the carrier itself has triadic periodicity.

This remainder is the **color charge** of quantum chromodynamics (QCD): three colors (red, green, blue) are three elements of $\mathbb{Z}_3$ generated by the incommensurability of the dichotomous act of distinction and the triadic carrier.

---

### 25.3. Confinement as Denominator Cleaning

**[D] Integrality of the free spectrum.** Free cohomologies $H^*(X, \mathbb{Z})$ **do not allow fractional coefficients**. Observable (free) topological invariants are always integers.

**[G1] Corollary for confinement.** Any state with a fractional charge ($1/3$ or $2/3$) **cannot be free**. it must combine with other fractional states so that the sum of the charges is an **integer**.

**Mechanism of cleaning:**

1. **Baryons (three quarks):** $1/3 + 1/3 + 1/3 = 1$. Three identical fractions (three axes) add up to a whole. Denominator 3 is "cleaned." The result is a colorless hadron. Example: PROTON ($uud$, total charge +1).

2. **Mesons (quark + antiquark):** $1/3 + 2/3 = 1$. Additional projections ($1/3$ and $2/3$) add up to a whole. Denominator is cleaned. Example: PION ($u\bar{d}$, total charge 0 or $\pm 1$).

3. **Single quark ($1/3$):** denominator is **not** cleaned. Fractional charge = unresolved tensor remainder. Free cohomologies do not allow it. **Confined.**

In the DOT reading, confinement here acts not as a dynamic effect but as a **topological rule of the free spectrum**: fractional coefficients cannot be a finite observable invariant without cleaning the denominator.

---

### 25.4. Quark Charges as Spectrum Projections

Returning to the spectral theorem of §20: two subspaces of the Laplacian have dimensions 3 ($V_1$) and 2 ($V_2$) when $k = 3$.

The spectral ratio $\lambda_1/\lambda_2 = 2/3$ is realized concretely:

- $V_1$ (dipole modes, massless): **3 independent directions**. A projection of one state onto $V_1$ is $1/3$ of the full spectrum.
- $V_2$ (quadrupole modes, massive): **2 independent directions**. A projection onto $V_2$ is $2/3$ of the full spectrum.

A quark carrying a charge of $1/3$ is an object lying completely **in one** dipole direction of $V_1$. An antiquark ($2/3$) is in the complementary subspace $V_2$.

---

### 25.5. Three Generations of Fermions: Strong DOT Restriction

**[G2] Restriction of three generations.** In the $K(2,2,2)$ structure, exactly **three generations** of fermion patterns naturally stand out, defined by pairs of twin prime numbers.

*Proof.*

Twin primes are pairs of prime numbers differing by 2:

| Generation | Pair | Composite triplet between them | Physical families |
|:---:|:---:|:---|:---|
| 1st | $(5, 7)$ | $[8, 9, 10]$ | $e, \nu_e, u, d$ |
| 2nd | $(11, 13)$ | $[14, 15, 16]$ | $\mu, \nu_\mu, c, s$ |
| 3rd | $(17, 19)$ | $[18, 20, 21, 22, 23, \dots]$ | $\tau, \nu_\tau, t, b$ |

The pattern is interrupted at the **fourth level**. Reason: the next potential pair is $(23, 25)$. Но $25 = 5^2$ — a **composite number** (self-intersection of axis 5). The fifth axis "bent" back on itself, creating a **loop** instead of a new boundary.

Self-intersection of an axis means that the 5th axis ($p = 5$) has reached the limit of its 1D extent and collapsed into a 0D point ($5^2 = 25$). A new fermion structure at this level is **impossible**: the axis is looped.

> **[G2] Corollary:** A fourth generation of fermions within $K(2,2,2)$ does not arise naturally. For it to appear, a fourth independent axis ($k = 4$) would be required, with a $K(2,2,2,2)$ graph and a spectral ratio of $3/4$ — different from $2/3$.

It is useful to compare this with the previous threshold $k=2$. At the $k=2$ level, the spectral ratio

$$\frac{\lambda_1}{\lambda_2} = \frac{1}{2}$$

gives the minimum distinction between two poles — the same basic split that was read as spin $1/2$ in §19.8. In this sense, the generational ladder begins not with "full families," but with the simplest binary distinction; triadic generations already appear as a superstructure over this minimum half-split.

---

### 25.6. Fraction $1/n$ as a Mode of Access to the Whole

In §8.1 of Part II, the "apertures" of the observer were introduced: $1/2, 2/3, 3/4$. Now we can formulate a general principle:

> **The $1/n$ Principle.** The fraction $1/n$ is not the $1/n$-th part of a whole. it is the **minimum legal representation of the whole** at resolution $n$.

A part is not a fragment. A part is the full whole seen through limited optics ($n$ axes).

When an observer has access to $n$ of the $k$ axes:

- They see $n/k$ — that portion of the full spectrum that is projected onto their "screen."
- The remaining $(k-n)/k$ is in the shadow.
- But the shadow is not emptiness: it contains **additional** information, restorable through a change of frame (§13 of Part II).

The electric charge of $1/3$ of a quark is not "1/3 of an atom." it is the **full state** of the atom, seen through one of the three axes.

#### Neighbor Boundary Corollary

For the triadic carrier, the minimum law applies:

\[
2/3 = 1 - 1/3.
\]

This means:

- `2/3` is the occupied manifestation on the background of `3`;
- `1/3` is the irreducible hidden debt of the triadic carrier;
- the quark charge of `1/3` is not a piece of an object, but a minimum hidden share, inevitable when reading a binary act against the background of three axes.

Hence, confinement becomes even more transparent: it is exactly the uncleaned debt of denominator `3` that cannot be free.

---

### 25.7. Ramanujan Sum and Numerical Confinement

In addition to the spectral argument, there is also a purely arithmetic one.

**Ramanujan's sum** $c_q(n)$ is defined as:

$$c_q(n) = \sum_{\substack{a=1 \\ (a,q)=1}}^{q} e^{2\pi i a n/q}$$

At $q = 3$ (three-axis framework), Ramanujan's sum vanishes for $n$ not multiple of 3:

$$c_3(n) = \begin{cases} 2, & 3 | n \\ -1, & 3 \nmid n \end{cases}$$

Physical meaning: if the "charge" $n$ is not a multiple of 3, the sum is negative — the configuration is energetically unfavorable. The system tends to combine charges until they reach a multiple of 3 (confinement).

---

### 25.8. Summary of §25

§25 has fixed:

- The fraction $p/q$ as the projection of dichotomy ($p$) onto the framework ($q$), not arbitrary division.
- Color charge as a remainder class arising from the projection of a binary act onto a triadic carrier.
- Confinement as a topological rule of the free spectrum: free cohomologies do not allow fractional coefficients.
- Quark charges $1/3, 2/3$ as projections of spectral subspaces $V_1, V_2$.
- The three-generation theorem: the twin prime pattern is interrupted at $5^2 = 25$.
- The $1/n$ principle: a part is not a fragment, but a full representation with limited resolution.

> **[G1] §25 translates the "mystery of confinement" from a purely computational QCD problem into the language of homological algebra and the topological limitation of the free spectrum.**

---

## §26. Bridge to Part III: Projection of Mathematics on the Graph

Parts I–III have built a closed theoretical vertical:

- **Part I** assembled the carrier — the $K(2,2,2)$ octahedron from Borromean prohibitions.
- **Part II** launched the machine — the operator $\partial$, projections, optics.
- **Part III** unfolded the syntax — algebra, spectrum, numbers, operators, fractions.

Now this entire apparatus must be **projected back onto the carrier**: the six vertices of the octahedron must come alive as 64 binary states, the numerator of the formula as a specific particle address, and the denominator as a specific embedding depth. This is the task of Part III.

§26 does not solve this task — it formulates three tools necessary for its solution.

At the same time, §26 relies not only on the Part III algebra but also on the Part II machine itself:

- `64 = 2^6` inherits the six-pole carrier;
- defect uses axial loads, i.e., the machine decomposition of six vertices into three pairs;
- mass lever uses $\gamma$, already read from the octahedral carrier;
- tails in Part III will be read not as pure numbers but as artifacts of the unclosed coordination between topology and optics.

---

### 26.1. Defect Formula: 64 Vacuum States

#### 26.1.1. Binary Vacuum

Each of the 6 vertices of the $K(2,2,2)$ Octahedron can be "switched on" ($1$) or "switched off" ($0$). This generates $2^6 = 64$ **binary configurations** — the full state space of the Vacuum.

The configuration $x = (s_1, s_2, s_3, s_4, s_5, s_6) \in \{0, 1\}^6$ sets the load on each pole.

#### 26.1.2. Axial Loads

The six vertices are divided into three pairs (axes):

$$\text{axis } 1: \{s_1, s_2\}, \quad \text{axis } 2: \{s_3, s_4\}, \quad \text{axis } 3: \{s_5, s_6\}$$

Axial load:

$$n_i = s_{2i-1} + s_{2i}, \quad i = 1, 2, 3$$

Each load takes values $n_i \in \{0, 1, 2\}$.

Average load:

$$\bar{n} = \frac{n_1 + n_2 + n_3}{3}$$

#### 26.1.3. Defect Formula

**The defect of configuration** $x$ is the variance of the loads on the three axes, which algebraically is strictly expressed through the vacuum average of the coboundary defect $\langle \partial - \delta \rangle$ (where $\partial$ and $\delta$ are the dual pair of operators canonized in §19):

$$\mathcal{D}(x) = \langle \partial - \delta \rangle_x = \frac{1}{2}\sum_{i=1}^{3}(n_i - \bar{n})^2$$

This value is geometrically exactly equal to $\|\Pi_2(x)\|^2$ — the square of the projection onto the $V_2$ subspace from the spectral theorem of §20.5. The defect $\mathcal{D}(x)$ **is** the mass in the normalization of the vacuum Laplacian spectrum.

**[D] Defect equivalence lemma.** Let $x \in \mathbb{R}^6$ be the vector of loads on the six poles, and $n_i$ be the total loads on the three antipodal pairs. Then the mass projection from §20.5 satisfies the equality

$$\boxed{\|\Pi_2(x)\|^2 = \frac{1}{2}\sum_{i=1}^{3}(n_i - \bar{n})^2 = \mathcal{D}(x).}$$

The point of the lemma is that the $V_2$ subspace is the variance-sector of the three-axis machine: it specifically collects the deviations of axial loads from their mean value. Therefore, the defect of §26 is not a new empirical construction; it is the same quadratic form as the spectral mass projection of §20, only rewritten in the language of axial loads. The bridge §20 ↔ §26 thus becomes rigorous: spectral mass and combinatorial defect are two records of the same invariant.

#### 26.1.4. Four Classes

Traversing all 64 configurations gives exactly **four** defect values:

| Defect $\mathcal{D}$ | Number of configurations | Type |
|:---:|:---:|:---|
| $0$ | $10$ | Perfect axial balance |
| $1/3$ | $36$ | Minimum failure of one axis |
| $1$ | $12$ | All three axes are different |
| $4/3$ | $6$ | Annihilation of choice |

**Total:** $10 + 36 + 12 + 6 = 64 = 2^6$. $\checkmark$

Why are there exactly four values? Because each axial load only takes values $0, 1, 2$, and the defect only depends on the **sorted pattern** of three loads $(n_1, n_2, n_3)$ up to the permutation of axes. Only the following types are possible:

- $(0,0,0), (1,1,1), (2,2,2)$  $\Rightarrow \mathcal{D} = 0$
- $(0,0,1), (0,1,1), (1,1,2), (1,2,2)$  $\Rightarrow \mathcal{D} = 1/3$
- $(0,1,2)$  $\Rightarrow \mathcal{D} = 1$
- $(0,0,2), (0,2,2)$  $\Rightarrow \mathcal{D} = 4/3$

Variance on three axes with binary vertices simply allows for no other values. Therefore, the set

$$\mathcal{D} \in \left\{0,\; \frac13,\; 1,\; \frac43\right\}$$

is not empirical but combinatorially closed.

**[G1]** These four classes perfectly correspond to the fundamental particles of the Standard Model. Note that the graph combinatorics describe charge states (identity), and spin is superimposed on the graph and does not multiply here:

| Defect | Physical Type | Count |
|:---:|:---|:---|
| $0$ | Massless: True Vacuum (1), Photon (1), Gluons (8) | 10 |
| $1/3$ | Quarks: 3 generations × 2 flavors × 3 colors × 2 (p/ap) | 36 |
| $1$ | Leptons: 3 generations × 2 flavors (charged and neutrino) × 2 (p/ap) | 12 |
| $4/3$ | Heavy bosons: $W^+, W^-, Z^0$ and their charge conjugations | 6 |

This is a strong combinatorial correspondence of the number of states in each sector. In the current canon, it is read as a structural result of the $K(2,2,2)$ graph, not as an ultimately closed physical theorem.

---

### 26.2. Lever Formula: Mass from Embedding Depth

#### 26.2.1. Basic Formula

From the spectral theorem (§20), the geometric invariant $\gamma$ (§21), and the numerical factorization (§23) follows the **bare mass** formula for each particle:

$$M_{\text{bare}} = \frac{C}{\gamma^k} \cdot m_e$$

where:

| Parameter | Value | Source |
|:---|:---|:---|
| $C$ | **Structural coefficient** — integer address of the particle on the graph | Factorization from §23.2 |
| $k$ | **Embedding depth** — number of passes through the scale lever $\gamma$ | Spectral hierarchy from §19.7 |
| $m_e = 0.51099895$ MeV | Electron mass — basic quantum of information | Reference unit |
| $\gamma = \sqrt{6}/9 \approx 0.27217$ | Geometric invariant of the octahedron | Metric from §21.1 |

#### 26.2.2. Physical Meaning of the Lever

The inverse value $\gamma^{-1} \approx 3.674$ is the **scale lever**. Each "pass" through $\gamma$ is an embedding of the octahedron **into itself** (fractal recursion).

- Electron ($C = 56, k = 0$): zero embeddings. The electron is a "pure form" without a scale lever.
- Muon ($C = 56, k = 1$): one embedding. The same form ($C = 56$), but "viewed" through one recursion.
- Proton ($C = 136, k = 2$): two embeddings. Another form ($C = 136$), accessible only through a double crossing.
- Higgs ($C = 27, k = 7$): seven embeddings. The deepest node of the Vacuum.

**[G1] Bare mass accuracy:** in current DOT-readouts, it exceeds $99\%$ for basic particles and reaches around $99.99\%$ for the proton. This is a strong correspondence, not yet an ultimate universal law.

#### 26.2.3. Tails: Fine Structure

The remaining $< 1\%$ is described by **tails** — correction terms that use graph nodes as sources:

$$M = M_{\text{bare}} \cdot \left(1 + \delta_0 + \Omega + \Omega_2 + \dots \right)$$

Each tail is a fraction whose numerator and denominator belong to the DOT alphabet ($\{18, 24, 27, 39, 48, 56, 64, 72, 81, 110, 136, 162, 272, 432\}$). A detailed description of the tails is the subject of Part III.

---

### 26.3. Morphological Matrix: Passport of Each Particle

In §23.2, it was shown that each base number $C$ factorizes through the primes $\{2, 3, 5, 7, 11, 13, 17\}$. This defines the **morphological vector** of the particle:

$$\vec{v}(C) = (k_2, k_3, k_5, k_7, k_{11}, k_{13}, k_{17})$$

where $C = 2^{k_2} \cdot 3^{k_3} \cdot 5^{k_5} \cdot 7^{k_7} \cdot 11^{k_{11}} \cdot 13^{k_{13}} \cdot 17^{k_{17}}$.

Examples:

| Particle | $C$ | $\vec{v}(C)$ |
|:---|---:|:---|
| Electron | 56 | $(3, 0, 0, 1, 0, 0, 0)$ |
| Pion $\pi^0$ | 72 | $(3, 2, 0, 0, 0, 0, 0)$ |
| Proton | 136 | $(3, 0, 0, 0, 0, 0, 1)$ |
| Higgs $H^0$ | 27 | $(0, 3, 0, 0, 0, 0, 0)$ |
| $W$-boson | 64 | $(6, 0, 0, 0, 0, 0, 0)$ |

**[G2] Topological Grand Unification (Leptoquarks):** Particles with an identical vector $\vec{v}$ — the electron, muon, $u$-quark, and $B^0$-meson — all have $\vec{v} = (3, 0, 0, 1, 0, 0, 0)$, i.e., $C = 56 = 2^3 \times 7$. In a strong DOT reading, this means that the lepton, quark, and meson are the same topological form read at different depths $k$. The differences between them then lie not in the structure itself, but in the emanation register.

---

### 26.4. Zeta Function as Partition Function of the Vacuum

#### 26.4.1. Euler's Formula

In §24.6.2, the adelic decomposition of the Riemann zeta function was introduced:

$$\zeta(s) = \prod_{p \text{ is prime}} \frac{1}{1 - p^{-s}} = \sum_{n=1}^{\infty} \frac{1}{n^s}$$

In DOT this decomposition has a direct meaning:

- Each factor $(1 - p^{-s})^{-1}$ is the contribution of one prime axis $p$ to the full spectrum of the Vacuum.
- The variable $s$ is an analog of "inverse temperature" ($\beta = 1/kT$ in statistical mechanics).
- The total sum $\zeta(s)$ is the **Partition Function** of all Vacuum states, summed over all possible axial configurations.

#### 26.4.2. Critical Strip and Mass Spectrum

Non-trivial zeros of the zeta function (presumably) lie on the critical line $\text{Re}(s) = 1/2$.

In DOT, $s = 1/2$ is the **first non-trivial spectral horizon**: the ratio $\lambda_1/\lambda_2$ at $k = 2$ (§20.4). This is not yet a derivation of the Riemann hypothesis, but a DOT reading of the critical line: the minimum carrier on which dipole and quadrupole modes first find themselves in an exact half-split regime.

The Riemann hypothesis (all non-trivial zeros on $\text{Re}(s) = 1/2$) in the context of DOT means: **all resonance modes of the Vacuum are concentrated on the horizon of two-dimensional distinction** ($k = 2$), rather than three-dimensional ($k = 3$). The three-dimensional world ($k = 3$, ratio $2/3$) lies **outside** the critical strip — it is stable.

#### 26.4.3. Ramanujan $\tau(n)$ Function

Ramanujan's discriminant form:

$$\Delta(\tau) = q \prod_{n=1}^{\infty}(1-q^n)^{24} = \sum_{n=1}^{\infty} \tau(n) q^n, \quad q = e^{2\pi i \tau}$$

The exponent $24 = 4 \times 6$ is the product of the octahedron vertex degree ($d = 4$) and the number of vertices ($v = 6$). The $\tau(n)$ function encodes the "internal pulsation" of the Leech lattice (§24.5.3), and through it — the **global modulation** of all DOT-graph scales.

> **📎 Companion Note.** For a full analysis of what DOT proves internally about the Riemann Hypothesis and the Yang–Mills mass gap — and what external bridges are still needed — see the companion note:  
> [`DOT_yang_mills_and_riemann_note_en.md`](../companion_code/notes/DOT_yang_mills_and_riemann_note_en.md)

---

### 26.5. Part III Program (Preview)

With the tools prepared in §§19–26, Part III will build:

1. **Complete Catalog of Particles** — a systematic traversal of all 64 states with the calculation of $C$, $k$, and tails for each particle. Mass tables with accuracy up to $0.001\%$ and higher.

2. **Alphabet of Nodes** — the graph structure on the base numbers $\{18, 24, 27, 39, 48, 56, 64, 72, 81, 110, 136, 162, 272, 432\}$, their multiplicative and additive links, musical intervals.

3. **Shells and Confinement** — how baryons (triple nodes) and mesons (double nodes) are assembled from quark fractions (§25).

4. **Cosmological Projection** — metric compression $\phi$, dark sector, Hubble formula.

---

### 26.6. Summary of §26 and Summary of Part III

§26 has fixed three tools of transition:

- **Defect formula** — classification of 64 states into four sectors, providing a strong combinatorial correspondence to the Standard Model zoo.
- **Lever formula** $M_{\text{bare}} = C/\gamma^k \cdot m_e$ — calculation of bare mass from two integers.
- **Zeta function** — Partition Function of the vacuum, assembled from products over prime axes.

---

**Summary of Part III entirely (§§19–26):**

| § | Theme | Key Result |
|:---:|:---|:---|
| 19 | Algebra of Rupture | $\partial^2 = 0 \Rightarrow$ three-term structure, $i$ as rotation in $\ker\,\partial$ |
| 20 | Spectral Theorem | $\lambda_1/\lambda_2 = 2/3$, mass $= \|\Pi_2(x)\|$ |
| 21 | Invariant $\gamma$, Constant $\alpha$ | $\gamma = \sqrt{6}/9$, $\alpha^{-1} = 432/\pi - 47\gamma/27$ |
| 22 | $SL(2,\mathbb{Z})$ | Ladder $k = 1 \to 3$, attractor — Connection |
| 23 | Emanation of Numbers | Primes = axes, $\times$ = structure, $+$ = mass |
| 24 | Operator Atlas | 6 layers: $\Omega_{0/1} \to \Omega_{5/6}$ |
| 25 | Fractions and Confinement | $1/3$ as remainder of binary act projection on triadic carrier, strong three-generation limit |
| 26 | Bridge to Part III | 64 states, $M = C/\gamma^k \cdot m_e$, $\zeta(s)$ |

> **[G1/G2] Part II shows that numbers, operations, constants, and algebraic structures can be organized as emanations of a single act: $\partial^2 = 0$. Part III verifies this organization by reverse projection onto the particle graph, where specific masses, charges, and interactions appear.**

---

*Distinction Observable Theory — Part II: Mathematical Framework*  
*Canonical revision, March 21, 2026*
