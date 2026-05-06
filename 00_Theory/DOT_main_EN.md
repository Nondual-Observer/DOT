# Theory of Observable Distinction (DOT)

## Introduction

### I.1. Subject of the Manuscript

The Theory of Observable Distinction is a finite combinatorial theory organized around one principle: **distinction is the primary structural fact, and objects arise as stable forms of held and pre-held distinction**.

The idea of the theory responds to a general scientific intuition: observation participates in how a distinction becomes available, stable, and checkable. In quantum physics, in contemporary artificial intelligence, and in cognitive sciences, the distinction between positions often cannot be separated from how it is held and read.

The strict part of DOT is a finite combinatorial apparatus. Every statement in it rests on an explicitly constructed carrier, an explicit relation, an explicit reading, and explicit recovery data.

The objects of the theory are finite sets with fixed relations. Distinction between them is a finite check. Growth of the theory is a finite procedure of adding a new binary digit to an already constructed carrier.

### I.2. Main Principle

Simple inequality only says that two positions are different; therefore distinction in DOT is not reduced to the statement "one thing is not equal to another." A distinction must be **held** by a structure.

For this purpose, four basic roles are introduced: **carrier**, **relation**, **reading**, and **recovery**.

The carrier specifies a finite domain of positions. The relation fixes which positions are connected and how their distinguishability is held. The reading translates distinction into another domain, allowing several positions to be read as one. Recovery fixes which data from the original carrier remains recoverable over each element of the reading.

These four roles specify a way of recording finite data, not an external interpretation. The formal unit of this notation is a **presentation**, the quadruple

$$
(X, R, q, \mathrm{rec}).
$$

A presentation gives each distinction a checkable finite form. Every statement of the theory reduces to checking properties of such a quadruple on a finite carrier.

A held distinction in DOT has three levels of closure.

**Pairwise level.** A position receives its role only together with the opposite position. A pair appears as one distinction: each member points to the other and does not have the same role without its opposite.

**Cyclic level.** When there are several distinctions, separate pairs of opposites are connected by transitions between positions. If a sequence of transitions returns the structure to its initial position, it is a closed cycle.

**Integral level.** Several distinctions may be held as one common scene. In such a scene, positions, opposites, transitions between them, and admissible joint configurations all matter; in formal notation, this is the incidence layer.

The minimal complete scene of this type contains three opposite pairs — six positions forming the first complete geometric configuration of the theory.

### I.3. Structure of the Document

The formal part of DOT is organized by ranks. A rank indicates how many binary coordinates participate in the current level of construction: at rank one there is one coordinate, at rank two there are two, at rank three there are three, and so on.

The document begins with the protocol of presentation: relational carrier, reading, recovery datum, exact presentation, and recovery conditions are introduced. After that it constructs the minimal nontrivial presentation — the polar layer with two opposites.

Rank 2 introduces a four-position carrier and the first different graph readings of one and the same carrier: a cycle $C_4$, complement pairs $2K_2$, full connectedness $K_4$, and partial connectedness $K_4 - e$ with diagonal partitioning into two simplices.

**Rank 3** introduces the admissible carrier

$$
X_{\mathrm{adm}} = Q_3 \setminus \{000,111\},
$$

on which simultaneously appear the relation grammar $R_1, R_2, R_3$, the cycle reading $C_6$, two triangular components $K_3\sqcup K_3$, complement pairs $3K_2$, the octahedral shell $K_{2,2,2}$, the chamber layer with eight chambers, the incidence package, and the transport operator with period 6.

Rank 4 shows how the octahedral structure already constructed is re-read inside a larger carrier. Here one obtains the shell decomposition $4+6+4+1$, the self-dual middle layer, the outer shell, and the operator layer with edge spectrum.

Rank 5 closes the finite carrier atlas of the manuscript. Its carrier has 31 positions and shell decomposition $5+10+10+5+1$. In the two middle layers one obtains relation grammars on ten-point and ten-point carriers with additional structure.

After the rank construction, the general law of growth is formulated. The transition from rank $n$ to rank $n+1$ is written as the addition of a new highest binary digit:

$$
\Lambda_n: \{0,1\}\times Q_n\to Q_{n+1},
\qquad
\Lambda_n(\varepsilon,x)=\varepsilon\mid x.
$$

This law explains how carriers, shells, complement pairs, outer shells, and operator layers are transported. The finite part of the manuscript closes as the package

$$
\mathfrak{R}_{\leq 5}^{\mathrm{fin}}
=
(\Pi_1,\mathfrak{C}_2,\mathfrak{C}_3,\mathfrak{C}_4,\mathfrak{A}_5),
$$

which gathers the constructed ranks under one name.

### I.4. Bridge Layers and External Projections

The main document fixes the strict finite core. External readings are not mixed into the core automatically: a bridge receives structural status only when its carrier, relation, reading, and recovery data are explicitly constructed.

The accompanying notes develop several such projections. The binary growth note separately unfolds the rank lift and binary-coordinate mechanism. The color bridge reads $Q_3$ as the RGB/CMY cube and connects the theory to color perception.

These notes show which projection readings become possible after the finite core has already been constructed.

### I.5. Status of Names and Transition to the Formal Part

The text uses three statuses of names.

**Native.** A name is constructed inside the formal part. Its carrier, relation, reading, recovery data, or operator role are specified. Such names participate in statements and checks.

**Readable.** A name is a reading of a structure already constructed. It helps see a carrier as a cycle, graph, shell, system of chambers, incidence layer, or another structural image. A readable name obtains status only through explicit construction of a native structure.

**Not-yet / bridge.** A name points to a future layer or an external extension of the theory. It serves as a navigation label and obtains proof status only after an explicit construction.

This separation keeps the boundary between the finite-combinatorial basis of the theory and possible bridge extensions beyond it. After this boundary, the formal part begins.

## §0. Presentation

### §0.1. Relational Carrier

In the first part of the theory, a relation is written as a subset of the Cartesian square. This notation is suitable for symmetric, directed, and more complex relation structures.

**Definition 0.1.**
A relational carrier is a pair

$$
(X,R),
$$

where

$$
X
$$

is a set of elements, and

$$
R\subseteq X\times X
$$

is a relation on $X$.

The set $X$ specifies the domain of elements. The relation $R$ specifies the way in which they are structurally held.

### §0.2. Subcarriers

Before introducing recovery datum, one must specify the type of object returned by recovery datum.

**Definition 0.2.**
For a relational carrier

$$
(X,R)
$$

denote by

$$
\mathrm{SubRel}(X,R)
$$

the set of all pairs

$$
(X',R')
$$

such that

$$
X'\subseteq X,
$$

$$
R'\subseteq R\cap(X'\times X').
$$

Elements of $\mathrm{SubRel}(X,R)$ are called subcarriers of the carrier $(X,R)$.

### §0.3. Reading

Reading sends the carrier to a reading domain. In the initial formalism, the reading domain consists only of actually occurring images.

**Definition 0.3.**
A reading is a surjective map

$$
q:X\to Y.
$$

Surjectivity means

$$
\mathrm{Im}(q)=Y.
$$

For each

$$
y\in Y
$$

the fiber

$$
X_y=q^{-1}(y)=\{x\in X:q(x)=y\}
$$

is defined. The fiber shows which elements of the original carrier are read as one element $y$.

### §0.4. Recovery Datum

A reading can collapse several carrier elements to one element of the reading domain. Recovery datum fixes which part of the original carrier remains recoverable over each element of the reading.

**Definition 0.4.**
A recovery datum for a reading

$$
q:X\to Y
$$

is a map

$$
\mathrm{rec}:Y\to \mathrm{SubRel}(X,R).
$$

For each $y\in Y$,

$$
\mathrm{rec}(y)=(X_y^{\mathrm{rec}},R_y^{\mathrm{rec}}),
$$

where

$$
X_y^{\mathrm{rec}}\subseteq q^{-1}(y),
$$

$$
R_y^{\mathrm{rec}}
\subseteq
R\cap
\bigl(X_y^{\mathrm{rec}}\times X_y^{\mathrm{rec}}\bigr).
$$

Recovery datum fixes which elements of the fiber and which relation inside them remain recoverable.

### §0.5. Presentation

**Definition 0.5.**
A presentation is a quadruple

$$
\Pi=(X,R,q,\mathrm{rec}),
$$

where

$$
(X,R)
$$

is a relational carrier,

$$
q:X\to Y
$$

is a surjective reading,

$$
\mathrm{rec}:Y\to \mathrm{SubRel}(X,R)
$$

is a recovery datum.

A presentation fixes four components:

$$
\text{carrier},
$$

$$
\text{relation},
$$

$$
\text{reading},
$$

$$
\text{recoverability}.
$$

A term is considered introduced in a given layer if a presentation is specified in which this term has all four components.

### §0.6. Full Recovery over a Reading Element

**Definition 0.6.**
Recovery datum is called full over $y\in Y$ if

$$
\mathrm{rec}(y)
=
\bigl(q^{-1}(y),\ R|_{q^{-1}(y)}\bigr),
$$

where

$$
R|_{q^{-1}(y)}
=
R\cap(q^{-1}(y)\times q^{-1}(y)).
$$

In this case, the entire fiber of the reading over $y$, together with the induced relation, is recoverable.

### §0.7. Exact Presentation

**Definition 0.7.**
A presentation

$$
\Pi=(X,R,q,\mathrm{rec})
$$

is called exact over $y\in Y$ if the recovery datum is full over $y$.

A presentation is called exact if it is exact over every

$$
y\in Y.
$$

# §1. Polar Presentation

### §1.1. Trivial and Nontrivial Presentations

The formal structure of a presentation admits trivial cases. For example,

$$
X=\{*\},
$$

$$
R=\varnothing,
$$

$$
q=\mathrm{id}_{\{*\}},
$$

$$
\mathrm{rec}(*)=(\{*\},\varnothing).
$$

This is a correct presentation with a one-point fiber of the identity reading. The recovery datum has the form $(\{*\},\varnothing)$.

A meaningful initial unit must contain at least one nontrivial fiber: two distinguishable elements of the carrier are read as one element of the reading and remain recoverable as distinct.

The minimal such case contains exactly two elements.

### §1.2. Polar Layer

**Definition 1.1.**
The polar layer is the relational carrier

$$
(P,R_P),
$$

where

$$
P=\{a,-a\},
$$

and

$$
R_P=\{(a,-a),(-a,a)\}.
$$

The relation $R_P$ is symmetric and irreflexive. It is written using ordered pairs for compatibility with the general notation

$$
R\subseteq X\times X.
$$

The polar layer fixes the unoriented pair $(a,-a)$.

The elements

$$
a,\quad -a
$$

are called polarities.

### §1.3. Invariant Reading

Let

$$
\mathbf I=\{I\}.
$$

Define the reading

$$
\pi:P\to \mathbf I
$$

by

$$
\pi(a)=I,
$$

$$
\pi(-a)=I.
$$

The map $\pi$ is surjective:

$$
\mathrm{Im}(\pi)=\mathbf I.
$$

The carrier $P$ contains two distinguishable polarities:

$$
a,\quad -a.
$$

In the reading $\mathbf I$, they have one image:

$$
\pi(a)=\pi(-a)=I.
$$

The element $I$ is the image of both polarities in the reading $\pi$. Therefore $I$ is called the invariant reading of the polar layer.

### §1.4. Recovery Datum of the Polar Layer

The fiber over $I$ is

$$
\pi^{-1}(I)=P=\{a,-a\}.
$$

The restriction of the relation to this fiber is

$$
R_P|_{\pi^{-1}(I)}=R_P.
$$

**Definition 1.2.**
The recovery datum of the polar layer is given by

$$
\mathrm{rec}_P(I)=(P,R_P).
$$

This is full recovery over $I$.

### §1.5. First Presentation

**Definition 1.3.**
The first presentation is

$$
\Pi_1=(P,R_P,\pi,\mathrm{rec}_P),
$$

where

$$
P=\{a,-a\},
$$

$$
R_P=\{(a,-a),(-a,a)\},
$$

$$
\pi:P\to \mathbf I,
\qquad
\pi(a)=\pi(-a)=I,
$$

$$
\mathrm{rec}_P(I)=(P,R_P).
$$

The presentation $\Pi_1$ is exact: the only element of the reading has full recovery.

Indeed,

$$
\pi^{-1}(I)=P,
\qquad
R_P|_{\pi^{-1}(I)}=R_P,
$$

and therefore

$$
\mathrm{rec}_P(I)=(P,R_P)
=
\bigl(\pi^{-1}(I),R_P|_{\pi^{-1}(I)}\bigr).
$$

Compressed notation:

$$
\{a,-a\}\xrightarrow{\pi} I,
\qquad
\mathrm{rec}_P(I)=(P,R_P).
$$

In $\Pi_1$, the following are fixed:

$$
\text{two polarities},
$$

$$
\text{one invariant reading},
$$

$$
\text{full recovery of the polar relation}.
$$

The empty circle $I$ denotes the image of the reading:

$$
\pi(a)=\pi(-a)=I.
$$

# §2. Automorphisms over the Invariant Reading

### §2.1. Automorphism of the Polar Layer over $I$

After defining $\Pi_1$, one can consider bijections of the carrier preserving the presentation data.

**Definition 2.1.**
An automorphism of the polar layer over $I$ is a bijection

$$
f:P\to P
$$

such that

$$
(x,y)\in R_P
\Longleftrightarrow
(f(x),f(y))\in R_P,
$$

and

$$
\pi\circ f=\pi.
$$

The set of such automorphisms is denoted

$$
\mathrm{Aut}_I(P,R_P).
$$

In the case of $\Pi_1$, both conditions are satisfied by every bijection $P\to P$: the reading $\pi$ is constant, and $R_P$ is the complete symmetric relation between two distinct elements.

The meaningful role of these conditions appears on richer carriers, where the reading and relation cease to be trivial.

### §2.2. Two Bijections of the Polar Layer

The two-element set $P$ has exactly two bijections.

The first is

$$
\mathrm{id}_P(a)=a,
$$

$$
\mathrm{id}_P(-a)=-a.
$$

The second is

$$
\tau(a)=-a,
$$

$$
\tau(-a)=a.
$$

**Statement 2.2.**

$$
\mathrm{Aut}_I(P,R_P)=\{\mathrm{id}_P,\tau\}.
$$

**Check.**
On a two-element set, every bijection either leaves both elements fixed or interchanges them. These two cases give

$$
\mathrm{id}_P
$$

and

$$
\tau.
$$

There are no other bijections of a two-element set.

Both bijections preserve $R_P$ and $\pi$. Therefore

$$
\mathrm{Aut}_I(P,R_P)=\{\mathrm{id}_P,\tau\}.
$$

### §2.3. Canonical Swap

**Definition 2.3.**
The automorphism

$$
\tau(a)=-a,
\qquad
\tau(-a)=a
$$

is called the canonical swap of the polar layer.

It satisfies

$$
\tau^2=\mathrm{id}_P.
$$

Check:

$$
\tau^2(a)=\tau(-a)=a,
$$

$$
\tau^2(-a)=\tau(a)=-a.
$$

### §2.4. Local Involution

The property

$$
\tau^2=\mathrm{id}_P
$$

describes the local involution of the polar layer.

Applying the swap twice recovers the original polarity:

$$
a\mapsto -a\mapsto a,
$$

$$
-a\mapsto a\mapsto -a.
$$

Sections §§0-2 define the local involution of the exact polar fiber.

# §3. First Rank Lift: Coordinate Notation of Polarity

### §3.1. From Polarity to Coordinate

The polar layer

$$
P=\{a,-a\}
$$

defines two distinguishable polarities of one invariant reading.

For rank extension, one needs notation in which several independent polar layers can be placed side by side as coordinates. This notation is a bit.

**Definition 3.1.**
A coordinate notation of the polar layer is a bijection

$$
c:P\to \mathbb{F}_2
$$

of the form

$$
c(a)=0,
\qquad
c(-a)=1.
$$

The choice of which polarity receives $0$ and which receives $1$ is a choice of notation. The structure of the polar layer is determined by two-elementness, the relation $R_P$, and swap symmetry.

If the opposite notation is chosen,

$$
c'(a)=1,
\qquad
c'(-a)=0,
$$

then

$$
c'=s\circ c,
\qquad
s(x)=x+1.
$$

Thus the two coordinate notations differ by the same swap already defined inside the polar layer.

In the chosen coordinate notation, the canonical swap takes the form

$$
c\circ\tau\circ c^{-1}(x)=x+1
\qquad
(x\in\mathbb{F}_2).
$$

Check:

$$
0\mapsto 1,
\qquad
1\mapsto 0.
$$

Thus the local swap receives the algebraic notation of adding one in $\mathbb{F}_2$.

### §3.2. Rank 1 as the Coordinate Form of the First Layer

**Definition 3.2.**
The coordinate carrier of rank $1$ is

$$
Q_1=\mathbb{F}_2=\{0,1\}.
$$

On it, the polar relation is defined by

$$
R_1^{\mathrm{pol}}=\{(0,1),(1,0)\}.
$$

The reading of rank $1$ is

$$
q_1:Q_1\to\mathbf I,
$$

$$
q_1(0)=q_1(1)=I.
$$

The recovery datum is

$$
\mathrm{rec}_1(I)=(Q_1,R_1^{\mathrm{pol}}).
$$

This gives the coordinate presentation

$$
\Pi_1^{\mathrm{coord}}
=
(Q_1,R_1^{\mathrm{pol}},q_1,\mathrm{rec}_1).
$$

This notation is obtained from $\Pi_1$ by replacing the names of elements through $c$:

$$
a\mapsto 0,
\qquad
-a\mapsto 1.
$$

The reading is preserved under this replacement:

$$
q_1(c(x))=\pi(x)
\qquad
(x\in P).
$$

The relation and recovery datum are also transported by $c$:

$$
(c\times c)(R_P)=R_1^{\mathrm{pol}},
$$

$$
\mathrm{rec}_1(I)=(c(P),(c\times c)(R_P)).
$$

The polar layer has received a coordinate form.

### §3.3. Full Carrier and Manifest States

Coordinate notation makes it possible to build carriers from several independent bits.

**Definition 3.3.**
The full coordinate carrier of rank $n$ is

$$
Q_n=\mathbb{F}_2^n.
$$

Its element

$$
x=(x_1,\ldots,x_n)
$$

records the state of $n$ polar coordinates.

The zero state

$$
0^n=(0,\ldots,0)
$$

is called the empty coordinate state.

A state

$$
x\neq 0^n
$$

is called a manifest coordinate state: at least one coordinate is in position $1$.

The set of all manifest states is denoted

$$
Q_n^*=\mathbb{F}_2^n\setminus\{0^n\}.
$$

For $n=1$:

$$
Q_1=\{0,1\},
$$

$$
Q_1^*=\{1\}.
$$

Here $Q_1$ is the full coordinate carrier of the polar layer, while $Q_1^*$ is the register of its nonzero manifestation.

$Q_1$ and $Q_1^*$ have different carrier roles.

### §3.4. Coordinate Carrier $Q_n$

The carrier

$$
Q_n=\mathbb{F}_2^n
$$

is used as the coordinate domain of states.

A presentation on $Q_n$ still requires three further data:

$$
\text{relation},
\qquad
\text{reading},
\qquad
\text{recovery datum}.
$$

They are specified by separate constructions over the chosen set.

### §3.5. Coordinate Swaps

Let

$$
e_i=(0,\ldots,0,1,0,\ldots,0)
$$

be the basis vector with $1$ in the $i$-th coordinate.

The local swap in the $i$-th coordinate is written as

$$
\sigma_i(x)=x+e_i.
$$

Here addition is taken in $\mathbb{F}_2^n$.

For $n=1$, this coincides with the notation of the canonical swap:

$$
x\mapsto x+1.
$$

For $n>1$, the formula

$$
x\mapsto x+e_i
$$

changes only one polar coordinate and leaves the remaining coordinates fixed.

The local swaps $\sigma_i$ are used in §4 to describe symmetries of the two-bit carrier.

### §3.6. New Bit

Notation convention: the new bit occupies the highest position on the left. The opposite convention gives an isomorphic carrier by permutation of coordinates.

For the transition

$$
Q_{n-1}\to Q_n
$$

we identify the old carrier with the subset

$$
Q_{n-1}\cong \{0\}\times Q_{n-1}\subset Q_n.
$$

The new basis bit is

$$
e_n=(1,0,\ldots,0)\in Q_n.
$$

Then

$$
Q_n=\mathbb{F}_2 e_n\oplus Q_{n-1}.
$$

The block of the new bit is

$$
B_n=e_n+Q_{n-1}.
$$

It contains all states in which the new bit is switched on.

### §3.7. Emergence Decomposition

Set

$$
Q_0=\{0\},
\qquad
Q_0^*=\varnothing.
$$

**Statement 3.4.**
For $n\geq 1$,

$$
Q_n^*
=
Q_{n-1}^*
\sqcup
\{e_n\}
\sqcup
(e_n+Q_{n-1}^*).
$$

**Check.**
Each element $x\in Q_n$ has the form

$$
x=\varepsilon e_n+y,
$$

where

$$
\varepsilon\in\mathbb{F}_2,
\qquad
y\in Q_{n-1}.
$$

If $x\neq 0^n$, then either $y\neq 0^{n-1}$ (so $y\in Q_{n-1}^*$), or $y=0^{n-1}$ and $\varepsilon=1$.

This gives the disjoint union

$$
Q_n^*
=
Q_{n-1}^*
\sqcup
\{e_n\}
\sqcup
(e_n+Q_{n-1}^*).
$$

The first component is: all manifest states of old bits (without the new bit).

The second component is: only the new bit switched on.

The third component is: the new bit plus a manifest state of old bits.
