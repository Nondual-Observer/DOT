# DOT: Strict Core, Volume 1



## 0. Introduction

### 0.0. Role of the Volume

This file is the proof companion to the rank $3$ block of the main manuscript
`../00_Theory/DOT_main_EN.md`. It does not set the initial order of the whole
theory. The initial order in the main manuscript is:

$$
\text{presentation}
\to
\text{rank }1
\to
\text{rank }2
\to
\text{rank }3.
$$

In this volume, the rank $3$ layer is isolated as an independent finite block.
Its main carrier is:

$$
X_{\\mathrm{adm}}=Q_3\setminus\{000,111\}.
$$

On this carrier we construct the relation scheme, the graph readings $C_6$,
$K_3\sqcup K_3$, $3K_2$, and $K_{2,2,2}$, the chamber layer, the
incidence matrix, the spectral layer, the discrete $Z_2$-transport, and the
finite signature of the core.

The octahedron in this file is not the first foundation of the theory. It is the
graph reading of the combined relation $R_{12}=$R_1$\cup R_2$ on the already
constructed carrier $X_{\mathrm{adm}}$:

$$
(X_{\\mathrm{adm}},R_{12})\cong K_{2,2,2}\cong O_3^{(1)}.
$$

In the current package this volume should be read as the strict rank $3$
block. The full constructions of ranks $4$ and $5$, the general rank-growth
law, and the general external layer are located in the main manuscript
`../00_Theory/DOT_main_EN.md`. All notation in this volume is compatible with
that manuscript: $X_{\mathrm{adm}}$ denotes only the admissible carrier of
rank $3$, and the graph layer $R_2$ has the form $K_3\sqcup K_3$.

Statements are marked by the strictness scale: [A], [C], [D], [G1].

### 0.0.A. Text Structure

1. Sections $0.1$-$0.3$ specify $\mathbb{F}_2^1/\mathbb{F}_2^2$, the model levels, and the object types.
2. Sections $1$-$7$ construct the chosen model background, the admissible set, the relation scheme, the graphs $C_6$ and $K_{2,2,2}$, the octahedron, chambers, incidence, the spectral layer, and transport.
3. The shell extension, categorical layer, and operator closure are moved to volume `02B`.

Short scheme:

```text
\mathbb{F}_2^1 / \mathbb{F}_2^2
-> $Q_3$
-> $X_{\\mathrm{adm}}$
-> \mathrm{Rel}
-> $C_6$, $K_{2,2,2}$, \text{chambers}, \text{incidence}, \text{transport}.
```

- $\mathbb{F}_2^1/\mathbb{F}_2^2$ specify the pre-core binary foundation;
- $Q_3 \to X_{\mathrm{adm}}$ specifies the $3$-bit carrier;
- $\mathrm{Rel}$ specifies the relation scheme;
- the graphs, chambers, incidence, and transport form the main content of this volume.

### 0.1. On the Rank $1$-$2$ Foundation, the $3$-Bit Strict Core, and the $4$-Bit Extension

In the main manuscript, the rank $3$ layer appears after the construction of
the presentation, the polar layer of rank $1$, and the comparison grammar of
rank $2$. Within the present volume, this already prepared layer is taken as
the main proof object:

$$
X_{\\mathrm{adm}}=\{0,1\}^3\setminus\{000,111\},
$$

from which the cycle $C_6$, the relation carrier $K_{2,2,2}$, and the
chamber layer $Q_3$ are extracted.

This rank $3$ core is preceded by two finite layers:

- $\mathbb{F}_2^1=\{0,1\}$, the minimal dipole of distinction;
- $\mathbb{F}_2^2=\{00,01,10,11\}$, the first local carrier of two independent binary distinctions;
- its basic readings $C_4$, $2K_2$, $K_4-e$, $K_4$;
- and the simplex sector $\{01,10,11\}$, with the hidden role of $00$.

The full construction of rank $4$ in the current package is located in the
main manuscript. In this volume only the external $4$-dimensional layer $V_4$
appears, as part of the shell-operator extension moved to `02B`. Therefore
ranks $4$ and $5$ are not the object of proof in `02A`.

### Definition 0.1.A [C]. Pre-Core Binary Foundation



1. **One-bit primitive**

   $$
\mathbb{F}_2^1=\{0,1\},
$$

   the minimal dipole of distinction.

2. **Two-bit local carrier**

   $$
\mathbb{F}_2^2=\{00,01,10,11\},
$$

   the first local finite carrier of two independent binary axes of distinction.

3. **Four local graph readings of $\mathbb{F}_2^2$**

   - explicit reading:
     $$
C_4;
$$

   - opposite-pair reading:
     $$
2K_2;
$$

   - partial closure:
     $$
K_4-e;
$$

   - full closure:
     $$
K_4.
$$

4. **Minimal simplex sector**

   The nonzero triple

   $$
\{01,10,11\}
$$

   is the visible simplex sector, with the hidden algebraic role of the element
   $00$.

5. **Transition to the strict $3$-bit layer**

   The full cube

   $$
Q_3=\mathbb{F}_2^3
$$

   contains coordinate square faces, each isomorphic to $\mathbb{F}_2^2$. The
   $3$-bit layer is assembled from intersecting $2$-bit cells.

### Remark 0.1.A1 [C]. Typed Lifts of the Two-Bit Layer into the Strict $3$-Bit Carrier

The transition

$$
\mathbb{F}_2^2 \longrightarrow Q_3
$$

should not be understood as a single embedding. In the strict extension of the
binary foundation, at least five typed lift modes must be distinguished.

#### (i) Face-lift

The two-bit carrier $\mathbb{F}_2^2$ is realized as a coordinate square face of
the full cube $Q_3$ with the third coordinate fixed.

This is the basic geometric lift of a two-bit cell into the full three-bit
carrier.

#### (ii) Total-pole lift

The extreme poles of the two-bit layer

$$
00,\qquad 11
$$

continue into two total poles of the full carrier:

$$
00\leadsto 000,
\qquad
11\leadsto 111.
$$

This is a lift of polar totality, not of the admissible interior.

#### (iii) Pair-lift

The punctured axis

$$
01\leftrightarrow 10
$$

lifts to one of the three complementary pairs of the admissible hexad, that is,
to one axis of the reading

$$
3K_2.
$$

In other words, the two-bit duplex does not disappear in the strict core; it
becomes one of its three axial pairs.

#### (iv) Triad-lift

The minimal closure sector of the two-bit layer

$$
\{01,10,11\}
$$

or, dually,

$$
\{00,01,10\}
$$

lifts to one of the two triadic readings of the admissible hexad, that is, to
one component of the graph

$$
K_3\\sqcup K_3.
$$

Thus the two-bit simplex sector has a strict three-bit shadow inside the
relation-core.

#### (v) Transport-lift

The two-sidedness of the punctured two-bit axis

$$
01\to10,
\qquad
10\to01
$$

is a degenerate preform of the transport law. On the admissible hexad this law
first unfolds fully into the primitive cycle

$$
C_6,
$$

where a local admissible step changes one coordinate and preserves mixedness.

### Corollary 0.1.A2 [C]. Strict Meaning of the Transition $\mathbb{F}_2^2\to Q_3$

Thus the two-bit foundation enters the strict $3$-bit layer not in one way but
through several compatible modes:

- as a face of the full carrier;
- as the preimage of two total poles;
- as one axial pair;
- as the source of triad-reading;
- as a degenerate preform of the transport-cycle.

Therefore $Q_3$ should be understood not as a sharp break with
$\mathbb{F}_2^2$, but as the first carrier in which all main two-bit motifs
begin to coexist simultaneously.

### Remark 0.1.B [C]. Status of the Pre-Core Binary Foundation

The pre-core binary foundation does not replace the $3$-bit core and does not
replace the relation scheme by a four-point carrier.


The local machine check of this layer is given by the function

```text
precore_binary_layer_test()
```

from the file `DOT_Core_verifier.py`.

### Remark 0.1.C [C]. Status of the Pre-Core Binary Foundation Relative to the Bridge Layer

The present volume begins the strict core of DOT, but does not take over the
entire transition from the architectural foundation `01` to the strict
$3$-bit core.

This transition is already unfolded separately in the volume

`01A_DOT_Mathematical_Bridge_EN.md`,

where:

- the negative core of admissibility;
- binary legalization;
- the admissible hexad;
- relation/incidence/transport transitions

are assembled as an intermediate bridge between `01` and the strict core.

Therefore the pre-core binary foundation

$$
\mathbb{F}_2^1,\ \mathbb{F}_2^2
$$

in the present volume should not be read as an alternative start instead of the
bridge layer, but as its strict continuation: here it already enters the proof
$3$-bit module, the relation scheme, the octahedral carrier, chambers, and
transport.

### Definition 0.2 [C]. Three Model Levels

We consider three model levels.

1. **Model A: the strict $3$-bit core.**

   $$
X_{\\mathrm{adm}}^{(3)}=\{0,1\}^3\setminus\{000,111\}.
$$

   This level contains the relation scheme, the graphs $C_6$ and
   $K_{2,2,2}$, the octahedron, the chambers $Q_3$, and the transport layer.

2. **Model B: the external shell carrier.**

   $$
V_n:=S_1^{(n)}\sqcup S_{n-1}^{(n)}.
$$

   This level contains the general cross-polytope carriers, chamber graphs
   $Q_n$, incidence matrices $B_n$, and reductions $n\to n-1$.

3. **Model C: the extended nontrivial shell package.**

   $$
U_n:=\bigsqcup_{k=1}^{n-1}S_k^{(n)}.
$$

   This level is needed only where the full nontrivial package without the
   extreme shells is considered, and is not the main carrier of this volume.

Thus the $3$-bit punctured core, the $n$-dimensional shell carrier, and the
full shell package are not identified with each other.

### Definition 0.3 [C]. Object Types

The following object types are strictly distinguished.

1. **State space.**
   A finite set of admissible binary states. Examples:

   $$
X_{\\mathrm{adm}},\qquad V_n,\qquad U_n.
$$

2. **Relation.**
   A symmetric subset of the square of states. Examples:

   $$
R_0,$R_1, R_2, R_3$.
$$

3. **Graph.**
   A vertex set with one fixed adjacency relation. Examples:

   $$
C_6,\qquad K_{2,2,2},\qquad Q_n.
$$

4. **Geometric package.**
   A geometric carrier together with its poles, chambers, and their adjacency.
   Examples:

   $$
O_3,\qquad \mathrm{Cham}(O_3).
$$

5. **Incidence structure.**
   A Boolean matrix or an equivalent binary relation between two different
   object types, for example between poles and chambers:

   $$
B,\qquad B_n.
$$

6. **Categorical layer.**
   A path category of a graph, or an equivalent packaging of incidence in terms
   of maps and compositions.

7. **Operator layer.**
   Operators on the space of functions on the Boolean cube

   $$
\mathcal H_n=\mathbb R^{\{0,1\}^n},
$$

   such as

   $$
\Pi_k,\ E_n,\ F_n,\ H_n,\ C.
$$

The further text does not mix these types.

### Remark 0.3.1 [C]. Use of the Words “Standard” and “Fixed”

The words **“standard”** and **“fixed”** mean that the object is specified inside
the chosen model and is invariant with respect to the stated class of
symmetries. Absolute independence of every realization is not claimed.

### Remark 0.3.2 [G1]. External Bridges

External bridges are treated as additional structural interfaces. A full
universal interpretation at level [G1] is not claimed.

# Section 1. ADMISSIBILITY AND PROHIBITIONS

The first layer of DOT is the axiomatic background of prohibitions. The triad
$\{\mathcal{Z}_D, \mathcal{Z}_F, \mathcal{Z}_C\}$ is specified as initial.

## 1.0. The Triad of Prohibitions as the Primary Axiomatic Background of DOT

Primary reductions:

1. collapse of distinction into identity $(\mathcal{Z}_D)$;
2. loss of the trace of the act of distinction $(\mathcal{Z}_F)$;
3. dependence of distinction on an external ground $(\mathcal{Z}_C)$.

The triad $\{\mathcal{Z}_D,\mathcal{Z}_F,\mathcal{Z}_C\}$ is accepted as the
minimal set of independent prohibitions at this level.

The triad $\{\mathcal{Z}_D,\mathcal{Z}_F,\mathcal{Z}_C\}$ is accepted as the
main axiomatic background of admissibility of distinction.

### Lemma 1.0.1 [A]. Exhaustiveness of Primary Reductions at Level $0$

Within level $0$, every primary reduction of the admissibility of distinction
must affect at least one of the following aspects:

1. distinguishability as non-collapse into identity;
2. fixability of the act of distinction as the presence of a trace;
3. autonomy of distinction as absence of an external ground.

**Justification.**

At level $0$, the following have not yet been introduced:

- ready-made objects;
- state configurations;
- temporal processes;
- internal geometric or algebraic structure;
- an external coordinatizing position.

Therefore the admissibility of distinction itself can be weakened here only:

- through destruction of distinction as such;
- through destruction of fixability of the act;
- or through moving the ground of distinction outside the position itself.

This gives exactly the three primary reduction types corresponding to
$\mathcal{Z}_D$, $\mathcal{Z}_F$, and $\mathcal{Z}_C$. $∎$

### Remark 1.0.2 [A]. Boundary of the Lemma

Lemma 1.0.1 claims exhaustiveness only within level $0$.

It does not claim that in richer layers, where states, geometry, processes,
operators, or external models have already been introduced, no new derived
types of degeneration can arise. At the level of admissibility of distinction
itself, only the three primary reduction lines are considered.

### Definition 1.1 [A]. Three Negative Prohibitions

The axiomatic background of DOT is specified by three imported prohibitions.

1. $\mathcal{Z}_D$ — **prohibition of coincidence**.
   Distinction must not collapse into complete identity. In the minimal
   $3$-bit encoding this excludes the two extreme states $000$ and $111$.

2. $\mathcal{Z}_F$ — **prohibition of tracelessness**.
   The act of distinction must not be transport-trivial. In the strict
   transport layer this means that a nontrivial $\mathbb{Z}_2$-holonomy class
   is allowed, not only the trivial holonomy $+1$.

3. $\mathcal{Z}_C$ — **prohibition of an external ground**.
   The rules of the carrier, transport, and incidence must not depend on a
   label, observer, or additional flag external to the system.

### Remark 1.1.1 [A]. The Prohibitions Live on Different Levels

The three prohibitions do not act on the same object.

- $\mathcal{Z}_D$ is a **state** prohibition and directly restricts the admissible subset of the raw cube.
- $\mathcal{Z}_F$ is a **transport** prohibition and restricts admissible connectivity or monodromy classes on the chosen cycle.
- $\mathcal{Z}_C$ is a **relational** prohibition and prohibits the use of external labels in adjacency and transport rules.

In particular, in the strict $3$-bit core only $\mathcal{Z}_D$ acts as a
direct filter on

$$
X_0=\{0,1\}^3.
$$

If

$$
P_{\mathrm{adm}}:\mathbb R^{X_0}\to\mathbb R^{X_0}
$$

denotes the projector onto admissible states, then it encodes the state-level
admissibility filtering

$$
X_{\\mathrm{adm}}=X_0\setminus\{000,111\},
$$

not all three prohibitions at once.

### Definition 1.2 [C]. Chosen Model Class for the Axiomatic Level

The operational check of the axiomatic background is performed only in the
following chosen model class:

1. the raw carrier is

   $$
X_0=\{0,1\}^3;
$$

2. state admissibility is specified by deleting $000$ and $111$;
3. primitive dynamics is specified by admissible one-bit transitions;
4. the residual carrier is specified by the rule “all pairs except complementary pairs”;
5. the transport layer is specified by a $\mathbb{Z}_2$-connection on a fixed primitive cycle;
6. no external labels are introduced into the adjacency and transport rules.

Within this model class, three controlled countermodels of weakening are fixed
below.

### Remark 1.2.1 [C]. Boundary of the Model Class

This section considers the set

$$
\{0,1\}^3\setminus\{000,111\}.
$$


- this is the minimal $3$-bit realization of the state-level prohibition;
- on it we construct the graphs
  $$
C_6,\qquad K_3\\sqcup K_3,\qquad 3K_2,\qquad K_{2,2,2};
$$

- more complex shell constructions do not enter here.

Two different objects must not be mixed:

- the $4$-bit cube $Q_4$, which has $16$ binary states;
- the $16$-cell, that is, the $4$-dimensional cross-polytope, which has $8$ vertices.

The construction does not start from a reduction of the $16$-cell, but from the
chosen $3$-bit model class.

### Definition 1.3 [C]. Three Standard Countermodels of Weakening

Let $\mathfrak M_{\neg D}$, $\mathfrak M_{\neg F}$, and
$\mathfrak M_{\neg C}$ denote three systems in each of which exactly one
prohibition is weakened.

1. **Countermodel $\mathfrak M_{\neg D}$.**
   The prohibition $\mathcal{Z}_D$ is removed, and therefore the carrier state
   space is the whole raw cube

   $$
X_0=\{0,1\}^3.
$$

   On it we define residual adjacency by

   $$
x\sim y \iff x\neq y \text{ and } y\neq \bar x.
$$

2. **Countermodel $\mathfrak M_{\neg F}$.**
   The prohibition $\mathcal{Z}_F$ is removed, but the fixed cycle $C_6$ is
   preserved. On all its edges we take the trivial connection

   $$
\varepsilon_i=+1.
$$

3. **Countermodel $\mathfrak M_{\neg C}$.**
   The prohibition $\mathcal{Z}_C$ is removed by adding an external binary
   flag. The carrier becomes

   $$
X_{\\mathrm{adm}}\times\{0,1\},
$$

   and residual adjacency is specified by the rule

   $$
(x,a)\sim (y,b)
   \iff
   a=b \text{ and } x\sim_{\mathrm{res}} y.
$$

Here $\sim_{\mathrm{res}}$ is the usual residual adjacency of the strict
$6$-vertex core.

### Theorem 1.4 [D|mod]. Three Standard Degenerate Regimes

In the chosen model class, weakening each of the three prohibitions leads to its
own type of degeneration.

1. In the countermodel $\mathfrak M_{\neg D}$, the residual graph is
   isomorphic to

   $$
K_{2,2,2,2},
$$

   and therefore has $8$ vertices and $\lambda_2 = 6 \neq 4$.

2. In the countermodel $\mathfrak M_{\neg F}$, every $\mathbb{Z}_2$-gauge
   transformation preserves trivial holonomy. Hence the nontrivial transport
   class is absent.

3. In the countermodel $\mathfrak M_{\neg C}$, the carrier graph splits as
   the disjoint union of two copies of the residual graph:

   $$
G(\mathfrak{M}_{\neg C}) \cong G_{\mathrm{res}} \sqcup G_{\mathrm{res}}.
$$

   In particular, it is disconnected.


**Proof.**

1. On the full cube $\{0,1\}^3$ there are four complementary pairs. By the
   definition of residual adjacency, edges run between any two different pairs
   and are absent only inside a pair. Therefore we obtain the complete
   four-partite graph $K_{2,2,2,2}$. Its Laplacian has spectrum

   $$
\{0,6,6,6,6,8,8,8\},
$$

   hence $\lambda_2=6$.

2. For the trivial connection $\varepsilon_i=+1$ on all edges of the cycle,
   the product around the cycle is $+1$. Under a gauge transformation

   $$
\varepsilon_i' = g_{i+1}\varepsilon_i g_i,
   \qquad g_i \in \{\pm1\},
$$

   we have

   $$
\prod_{i=1}^{6}\varepsilon_i'
   =
   \prod_{i=1}^{6} g_{i+1}\varepsilon_i g_i
   =
   \left(\prod_{i=1}^{6} g_i^2\right)\left(\prod_{i=1}^{6}\varepsilon_i\right)
   =
   +1.
$$

   Therefore the trivial class cannot produce holonomy $-1$.

3. In the definition of $\mathfrak M_{\neg C}$, adjacency is allowed only when
   the external flag agrees. Therefore vertices with flag $0$ and vertices
   with flag $1$ are not connected to each other at all. Inside each flag
   layer lives the ordinary residual graph $G_{\mathrm{res}}$. Hence

   $$
G(\mathfrak M_{\neg C}) \cong G_{\mathrm{res}} \sqcup G_{\mathrm{res}},
$$

   and the graph is disconnected. $∎$

### Remark 1.4.1 [D|mod]. On the Tautological Nature of $\mathfrak M_{\neg C}$ and Its Function

The graph split in the countermodel $\mathfrak M_{\neg C}$ is trivial by
construction: the external flag is built into the adjacency rule and
automatically splits the carrier. Thus external marking destroys carrier
connectedness and internal transitivity.

### Corollary 1.5 [D|mod]. Operational Non-Redundancy of the Triad of Prohibitions

In the chosen model class, none of the prohibitions $Z_D$, $Z_F$, $Z_C$ is
operationally redundant.

- removing $Z_D$ leads to **combinatorial degeneration**;
- removing $Z_F$ leads to **dynamic degeneration**;
- removing $Z_C$ leads to **relational degeneration**.

Therefore no pair among these three prohibitions replaces the third inside the
chosen family of models.

### Remark 1.6 `[A]/[C]`. What Is Proved Here and What Is Not Claimed

Closed:

- a formal description of the triad of prohibitions;
- their separation across the state, transport, and relational layers;
- three explicit finite countermodels of weakening;
- operational non-redundancy of the triad of prohibitions in the chosen model class.

Not claimed:

- a metatheorem on logical independence of the triad $Z_D,Z_F,Z_C$ in all possible formal languages;
- an equivalence of the form “prohibitions alone $\Longleftrightarrow$ the whole positive part of the theory”.

To obtain the positive core, the accepted postulates [C] remain necessary:
admissible one-bit transitions, residual adjacency, the choice of carrier,
chamber layer, and transport realization.

The strict core of the model consists of four layers.

1. **Admissible binary states.** We take the $3$-bit cube and delete the two
   extreme states $000$ and $111$. Six admissible states remain.
2. **The standard relation scheme on the same set of six states.**
   - Hamming distance $1$ gives the cycle $C_6$;
   - Hamming distance $2$ gives the shell graph $K_3 \sqcup K_3$;
   - Hamming distance $3$ gives the three complementary axes $3K_2$;
   - the carrier graphs used are $C_6$ and the residual carrier $K_{2,2,2}=$R_1$\cup R_2$.
3. **Geometric realization.** The residual graph is realized as the $1$-skeleton
   of the standard octahedron. Its eight sign chambers form the cube $Q_3$.
4. **Transport of local status.** The topological transport law acts on the
   chosen minimal cycle $C_6$, not on the whole octahedral carrier. Its
   invariant is a $\mathbb{Z}_2$-holonomy class.

Structural summary:

- $C_6$ is the graph of the primitive process;
- $K_3 \sqcup K_3$ is the triadic shell layer;
- $3K_2$ is the axial layer of complementary opposition;
- $K_{2,2,2}$ is the positive surface $R_1 \cup R_2$;
- $Q_3$ is the chamber graph around the carrier;
- twisted transport lives on the chosen cycle, not on the whole carrier.

### Remark 1.6.2 [C]. Why $X_{\mathrm{adm}}$ and $Q_3$ Appear Simultaneously

The strict core uses two different but related objects:

- the active state carrier
  $$
X_{\\mathrm{adm}}=\{0,1\}^3\setminus\{000,111\},
$$

  on which the relations $R_1, R_2, R_3$ live;
- the surrounding sign cube of chambers $Q_3$, which encodes the eight
  chambers of the octahedron.

Therefore deleting $000$ and $111$ does not mean destroying the whole cubic
language as such. It only means that the two extreme total states do not belong
to the active admissible carrier.



- $X_{\mathrm{adm}}$ is the state layer;
- $Q_3$ is the chamber layer around the same carrier;
- the transition from one to the other is specified by the chosen model and does not follow from the prohibition $Z_D$ alone.

### Definition 1.6.3 [C]. Two Total Poles of the Full Carrier

In the full carrier

$$
Q_3=\{0,1\}^3
$$

the states

$$
000,\qquad 111
$$

should be understood not merely as two deleted words, but as two total poles:

- `000` is the pole of zero or invariant totality;
- `111` is the pole of full saturation or total objectness.

These states do not enter the active admissible carrier of the strict core, but
they belong to the full carrier as its two extreme limiting states.

### Definition 1.6.4 [C]. Shell-Puncture

The transition

$$
Q_3 \longrightarrow X_{\\mathrm{adm}}=Q_3\setminus\{000,111\}
$$

will be called the basic shell-puncture of the full carrier.

Its meaning is not destruction of the cubic language, but opening the
admissible-shell after deleting the two total poles. In this sense:

- $Q_3$ remains the full carrier and chamber layer;
- $X_{\mathrm{adm}}$ is its active admissible interior.

### Remark 1.6.5 [C]. Minimal Shell-Puncture Operator

On the space of functions on the full cube

$$
\mathcal H_3=\mathbb R^{Q_3}
$$

it is convenient to fix two projector operators:

$$
P_{\mathrm{tot}}:=|000\rangle\!\langle 000|+|111\rangle\!\langle 111|,
\qquad
P_{\mathrm{adm}}:=I-P_{\mathrm{tot}}.
$$

Then $P_{\mathrm{tot}}$ selects the two total poles of the full carrier, while
$P_{\mathrm{adm}}$ selects the admissible-shell of the strict core.

This operator language adds no new theory; it only makes explicit the already
used transition

$$
Q_3 \to X_{\\mathrm{adm}}.
$$

It is compatible both with the state reading of the strict core and with the
later chamber reading of $Q_3$.

---

### Prologue 2.0. Transition from Prohibitions to the Carrier

In this prologue the logical prohibitions are matched with a carrier ladder:

- the sequence of intermediate steps is specified;
- the first explicit carrier is isolated;
- then the transition to the order
  $$
8 \to 6 \to C_6 \to ($R_1, R_2, R_3$)
$$

  is constructed.

The ladder:

```text
0|1 -> NOT -> seal
1|2 -> Cut + Support -> pair / retained interval
2|3 -> Support + Witness + Knot -> simplex / closure
3|4 -> self-locking chamber
4|5 -> intermediate break
5|6 -> six-vertex carrier
6   -> R3 + R2 + R1
```

#### 2.0.0. Minimal Primitive Carrier and the Octahedral Consequence

Before reading the early descent as a ladder of carriers, we must fix the
rigidest geometric node of this bridge.

A **primitive carrier** is a geometric carrier whose vertices are independent
generators of distinction, not composite sign configurations of already
available axes.

If the vertices of a candidate already encode complete joint states along
several axes, then that candidate is not a primitive carrier but a derived shell
over a simpler carrier.

Requirements for a primitive carrier:

1. it carries $n$ independent axes;
2. it has two opposite poles on each axis;
3. it has a common center;
4. it contains no additional composite vertices beyond the axial poles themselves.

**Theorem.** Under these requirements, the minimal carrier in dimension $n$ is
specified by the vertices

$$
\pm e_1,\dots,\pm e_n,
$$

that is, it is the $n$-dimensional cross-polytope.

**Proof.**

1. Each of the $n$ independent axes requires a pair of opposite poles, so at
   least $2n$ vertices are necessary.
2. The primitiveness condition prohibits adding composite vertices encoding
   combinations of already available axes.
3. Therefore the number of vertices cannot exceed $2n$.
4. Hence the vertex set is fixed as

   $$
\pm e_1,\dots,\pm e_n.
$$

5. This vertex set determines the $n$-dimensional cross-polytope. $∎$

In dimension $3$, this immediately implies:

- the tetrahedron is not suitable, because it does not give three independent axes with antipodal pairs;
- the cube is not suitable, because its vertices are already complete sign configurations along three axes and belong to a composite state layer;
- the octahedron realizes exactly three independent axes, six axial poles, and a common center without composite vertices.

Therefore the **octahedron is the minimal three-dimensional primitive carrier**.

#### 2.0.1. Initial Steps

At level $0$ there is no ready-made object, but only minimal admissibility of
distinction specified by the triad of prohibitions.

The step

```text
0|1
```

specifies the first local fixation:

```text
NOT -> seal.
```

The corresponding arithmetic relation:

$$
0+1=1, \qquad 0 \cdot 1 = 0.
$$

The next step

```text
1|2
```

specifies the first pair:

- **Cut** localizes the prohibition;
- **Support** holds the cut as the first extension;
- the carrier is specified as the first one-dimensional interval.

The corresponding arithmetic relation:

$$
1+1=2, \qquad 1\cdot 1 = 1.
$$

At the step $1|2$, the additive branch gives a pair, while the multiplicative
branch preserves the seal.

The step

```text
2|3
```

specifies the first closure:

- **Support** has already been held;
- **Witness** turns it into a path;
- **Knot** first closes the path into a whole.

The minimal carrier here has the form

```text
simplex / triangular closure / K3.
```

The corresponding arithmetic relation:

$$
1+2=3, \qquad 1 \cdot 2 = 2.
$$

Here the pair passes into an indecomposable ternarity.

#### 2.0.2. Self-Lock, Intermediate Break, and Explicit Carrier

The step

```text
3|4
```

specifies the first self-lock:

$$
2+2 = 2 \cdot 2 = 4.
$$

This threshold fixes a carrier of the form

```text
self-locking chamber
```

The number $5$ then gives no new carrier. An intermediate break arises:

$$
2+3 = 5, \qquad 2 \cdot 3 = 6.
$$

This connects the previous layer with an explicit carrier, but does not yet give
the carrier itself.

Only the transition to $6$ gives full coincidence:

$$
1+2+3 = 1 \cdot 2 \cdot 3 = 6.
$$

This is the first relation specifying an explicit carrier.

#### 2.0.3. Transition to the Strict Core

After this, the carrier ladder prepares the shell combinatorics:

- the pair specifies the polar memory of future axes;
- the simplex specifies the germ of future triads;
- the self-lock stabilizes the local chamber structure;
- the six-vertex carrier first makes possible the simultaneous reading
  $$
R_1 = C_6,\qquad R_2 = K_3\\sqcup K_3,\qquad R_3 = 3K_2.
$$

We obtain the chain

```text
seal -> pair -> simplex -> self-locking chamber -> six-vertex carrier
```

The strict combinatorial skeleton begins below.

#### 2.0.4. Model Class without an External Flag

To remove unnecessary heuristic weight from the choice

$$
X_{\\mathrm{adm}} = \{0,1\}^3 \setminus \{000,111\},
$$

we fix a class of finite models.

By a rank $m$ model without an external flag we mean a finite quadruple

$$
\mathfrak A=(V,c,R_{\mathrm{res}},R_{\mathrm{prim}}),
$$

where:

1. $V$ is a finite set of active states;
2. $c:V\to V$ is an involution without fixed points;
3. the orbits of the action of $c$ are interpreted as complementary axes, and their number is $m$;
4. the residual relation is specified by the rule

   $$
x R_{\mathrm{res}} y
   \iff
   x \neq y \text{ and } y \neq c(x);
$$

   that is, inside a complementary pair there are no edges, and between
   different pairs all possible edges are drawn;
5. the primitive process $R_{\mathrm{prim}}$ is a connected $2$-regular
   spanning subgraph of the relation $R_{\mathrm{res}}$;
6. the data of the model include no external binary flag doubling the carrier.

Below we consider the case $m\ge 3$, that is, at least three complementary
axes.

#### 2.0.5. Minimality Theorem for the Active Carrier

In the class of flag-free axis-transport models of rank $m\ge 3$, the
following hold:

1. always

   $$
|V| \ge 6;
$$

2. the minimal case $|V|=6$ is equivalent to $m=3$;
3. in the minimal case the residual carrier is isomorphic to

   $$
K_{2,2,2}.
$$

**Proof.**

1. Since $c$ is an involution without fixed points, the set $V$ splits into
   orbits of size $2$. If the number of such orbits is $m$, then

   $$
|V|=2m.
$$

2. By definition we consider the case $m\ge 3$, hence

   $$
|V|=2m\ge 6.
$$

3. Equality $|V|=6$ is possible if and only if $m=3$.

4. In this case $V$ splits into exactly three complementary pairs. By the
   definition of $R_{\mathrm{res}}$, inside each pair there are no edges, and
   between different pairs all possible edges are drawn.

5. This is precisely the definition of the complete tripartite graph with parts
   of size $2$, that is,

   $$
(V,R_{\mathrm{res}})\cong K_{2,2,2}.
$$

This proves the claim. $∎$

#### 2.0.6. Uniqueness Theorem for the Primitive Process in the Minimal Case

Let

$$
\mathfrak A=(V,c,R_{\mathrm{res}},R_{\mathrm{prim}})
$$

be a minimal flag-free axis-transport model. Then the primitive process is
isomorphic to the cycle

$$
C_6.
$$

**Proof.**

1. By Theorem 2.0.5, $|V|=6$.
2. By definition, $R_{\mathrm{prim}}$ is a connected $2$-regular graph on
   all of $V$.
3. Every finite connected $2$-regular graph is a cycle.
4. On six vertices this means

   $$
(V,R_{\mathrm{prim}})\cong C_6.
$$

$∎$

#### 2.0.7. Corollary. Standard Realization of the Strict Core

Every minimal model without an external flag is isomorphic to the standard
$3$-bit active carrier of DOT.

More precisely, after numbering the three complementary axes one can choose a
bijection

$$
V \xrightarrow{\cong} \{100,011,010,101,001,110\},
$$

which:

- sends complementary pairs to the pairs
  $$
100\leftrightarrow 011,\quad
  010\leftrightarrow 101,\quad
  001\leftrightarrow 110;
$$

- sends the residual carrier to
  $$
K_{2,2,2}=R_1\cup R_2;
$$

- sends the primitive process to some graph isomorphic to $C_6$.

Therefore the $3$-bit admissible core is the standard representative of the
minimal model class.

#### 2.0.8. Remark on the Boundary of the Result

Theorems 2.0.5-2.0.7 establish minimality and uniqueness inside an explicitly
chosen class of models without an external flag.

The local machine check of this block is performed by the function

```text
minimal_active_carrier_test()
```

from the file `DOT_Core_verifier.py`.

They do not yet claim the stronger metatheorem:

- that the abstract prohibition $\mathcal{Z}_D$ alone must, in all possible
  formalizations, lead exactly to the $3$-bit model;
- or that the transition $AMR \to \text{core}$ already has a unique possible
  external interface.

Stronger statements at level [G1] are not proved here.

#### 2.0.9. Remark [Packaging]. Retrospective Companion Reading of Prologue `2.0`

Prologue `2.0` admits a later companion reading in the language of a local binary
comparator.

In this reading:

- level `1` expresses localization of a pole or carrier place;
- level `2` expresses a dyadic act of comparison, that is, the first polarization
  and the distinction between coincidence and non-coincidence;
- level `3` expresses the first retention of distinction in a closure or assembly
  form.

Thus the ladder

$$
1 \to 2 \to 3
$$

can be retrospectively read as the sequence

$$
\text{local pole} \to \text{comparison} \to \text{retained closure}.
$$

This is compatible with the later bridge-language, where:

- $\chi_0$ is the minimal binary comparator;
- $\chi_{\mathrm{ax}}$ is its first axial realization;
- the product of local comparator modes leads to the admissible hexad of the strict core.

#### 2.0.10. Remark [Packaging]. Boundary of This Retrospective Reading

This companion reading does not replace the strict statements `2.0.5-2.0.8` and
must not be used as their proof.

Its role is more modest:

- to show that the old arithmetic-structural prologue and the new
  binary-comparator bridge express the same early architecture in two different
  languages;
- and thereby to make the transition from the pre-core binary foundation to the
  strict $3$-bit core more transparent.

## 2. Strict Combinatorial Core

### Definition 2.1. Raw and Admissible State Spaces

Let

$$
X_0 := \{0,1\}^3.
$$

Define the admissible subspace by deleting the two extreme states:

$$
X_{\\mathrm{adm}} := X_0 \setminus \{000,111\}.
$$

### Theorem 2.2 [D]. Cardinalities

$$
|X_0| = 8, \qquad |X_{\\mathrm{adm}}| = 6.
$$

**Proof.** The set $X_0$ contains exactly $2^3$ states. By definition, two
states are deleted. $∎$

### Definition 2.3. Weight Classes

Let $w(x)$ be the Hamming weight of the state $x$. Then

$$
\mathcal{C}_1 := \{x \in X_{\\mathrm{adm}} : w(x)=1\}, \qquad
\mathcal{C}_2 := \{x \in X_{\\mathrm{adm}} : w(x)=2\}.
$$

Explicitly:

$$
\mathcal{C}_1 = \{100,010,001\}, \qquad
\mathcal{C}_2 = \{011,101,110\}.
$$

### Definition 2.4. Complement Operator

Set

$$
\bar{x} := (1-x_1, 1-x_2, 1-x_3).
$$

### Theorem 2.5 [D]. Complementary Partition and Three Axes

The complement preserves $X_{\mathrm{adm}}$, has no fixed points on
$X_{\mathrm{adm}}$, and partitions it into three pairs:

$$
100 \leftrightarrow 011, \qquad
010 \leftrightarrow 101, \qquad
001 \leftrightarrow 110.
$$

These three complementary pairs form the three standard axes of the strict core.

**Proof.** The complement sends states of weight $1$ to states of weight $2$
and conversely. A fixed point would require $x_i = 1-x_i$ for every $i$,
which is impossible over $\{0,1\}$. $∎$

### Definition 2.5.A [C]. Distinguished Axis and Polarity of an Admissible State

For every state

$$
x\in X_{\\mathrm{adm}}=\{0,1\}^3\setminus\{000,111\}
$$

there exists exactly one coordinate different from the other two. Denote the
index of this distinguished coordinate by

$$
\iota(x)\in\{D,F,C\}.
$$

Next set

$$
\pi(x)=-
\quad\text{if}\quad
w(x)=1,
\qquad
\pi(x)=+
\quad\text{if}\quad
w(x)=2.
$$

Then every admissible state is encoded by the pair

$$
(\iota(x),\pi(x))
\in
\{D,F,C\}\times\{-,+\}.
$$

This reading makes explicit that the admissible layer of the strict core is not
just a set of six words, but a set of axis-polar states.

### Theorem 2.5.B [C]. Factorization of the Admissible Hexad

The map

$$
\Phi:X_{\\mathrm{adm}}\to\{D,F,C\}\times\{-,+\},
\qquad
\Phi(x):=(\iota(x),\pi(x)),
$$

is a bijection.

Equivalently, the admissible hexad of the strict core factorizes as

$$
X_{\\mathrm{adm}}
\cong
\{D,F,C\}\times\{-,+\}.
$$

Thus every admissible state is determined by two independent data:

1. which axis is distinguished;
2. in which polarity this distinction lies.

### Definition 2.5.C [C]. Axial Selection Operators

For each axis $\alpha\in\{D,F,C\}$, define a projector-like indicator

$$
P_\alpha : \mathbb R^{X_{\\mathrm{adm}}}\to \mathbb R^{X_{\\mathrm{adm}}},
$$

which preserves only those basis states $|x\rangle$ for which

$$
\iota(x)=\alpha.
$$

Then:

- $P_D$ selects the pair $\{100,011\}$;
- $P_F$ selects the pair $\{010,101\}$;
- $P_C$ selects the pair $\{001,110\}$,

and

$$
P_D+P_F+P_C=I_{\mathbb R^{X_{\\mathrm{adm}}}}.
$$

These operators do not add a new layer beyond the strict core. They only make
explicit the axial partition of the admissible hexad that is already present in
the relation scheme through the graph $3K_2$.

### Corollary 2.5.D [C]. Four Standard Readings of One Factorization

After the factorization

$$
X_{\\mathrm{adm}}
\cong
\{D,F,C\}\times\{-,+\}
$$

the four standard graph readings of the strict core arise automatically.

1. **Pair-reading.**
   Fixing an axis and changing polarity gives

   $$
3K_2.
$$

2. **Triad-reading.**
   Fixing polarity and changing the axis gives

   $$
K_3\\sqcup K_3.
$$

3. **Relation-shell.**
   If all states with different axes are connected, one obtains

   $$
K_{2,2,2}.
$$

4. **Primitive transport-reading.**
   If one moves by local admissible steps that change one coordinate and
   preserve mixedness, one obtains

   $$
C_6.
$$

Therefore the graphs of the strict core should be understood not as an unrelated
collection of objects, but as four readings of the same axis-polar
factorization.

### Table 2.5.E [C]. Explicit Table of Axis-Polar Factorization

| state | axis-polarity |
| ----- | ------------- |
| `100` | `(D,-)`       |
| `011` | `(D,+)`       |
| `010` | `(F,-)`       |
| `101` | `(F,+)`       |
| `001` | `(C,-)`       |
| `110` | `(C,+)`       |

The global complement

$$
\bar x = 1-x
$$

preserves the axis and changes polarity:

$$
\iota(\bar x)=\iota(x),
\qquad
\pi(\bar x)=-\pi(x).
$$

It is in this sense that the three complementary pairs of the strict core are
three axes of one and the same admissible hexad.

### Theorem 2.6 [D]. Hamming Partition of Unordered Pairs

The fifteen unordered pairs of vertices of $X_{\mathrm{adm}}$ split as follows:

- $6$ pairs at Hamming distance $1$;
- $6$ pairs at Hamming distance $2$;
- $3$ complementary pairs at Hamming distance $3$.

**Proof.** This is a direct enumeration on the six admissible $3$-bit states.
$∎$

---
### Remark 2.6.0a. Order in Which the Layers Appear on the Six-Point Shell

Do not mix two steps.

1. First the triad of prohibitions selects the admissible six-point shell

   $$
X_{\\mathrm{adm}}=\{0,1\}^3\setminus\{000,111\}.
$$

2. The first graph law on this shell is the distance-$1$ layer, that is,

   $$
G_1\cong C_6.
$$

3. Only after this does the full Hamming metric unfold the whole package of
   relations

   $$
G_1,\quad G_2,\quad G_3.
$$

Thus the hierarchy is

$$
8 \to 6 \to C_6 \to ($R_1, R_2, R_3$),
$$

not a simple enumeration of unrelated graphs.

### Definition 2.6.1 [D|comb]. Standard Relations $R_1, $R_2$, R_3$

On the set $X_{\mathrm{adm}}$, define three symmetric relations:

$$
R_k := \bigl\{\{x,y\} \subset X_{\\mathrm{adm}} : d_H(x,y)=k\bigr\},
\qquad
k \in \{1,2,3\}.
$$

Let $G_k=($X_{\\mathrm{adm}}$,R_k)$ denote the corresponding undirected graph.

### Theorem 2.6.2 [D]. Three Standard Graphs of the Relation Scheme

For the graphs $G_1,G_2,G_3$, the following hold:

1.
   $$
G_1 \cong C_6;
$$

2.
   $$
G_2 \cong K_3 \sqcup K_3,
$$

   and its two components are the complete graphs on the shells

   $$
\mathcal C_1=\{100,010,001\},
   \qquad
   \mathcal C_2=\{011,101,110\};
$$

3.
   $$
G_3 \cong 3K_2,
$$

   and its three edges are the complementary pairs from Theorem 2.5.

**Proof.**

1. Pairs at distance $1$ connect only states of weights $1$ and $2$. Each
   admissible vertex has exactly two neighbors at distance $1$, and the
   resulting graph is connected. Therefore it is a connected $2$-regular graph
   on six vertices, hence $C_6$.
2. Among the three states of weight $1$, any two differ in exactly two bits;
   the same holds among the three states of weight $2$. Distance $2$ does
   not occur between states of different weights. Hence $G_2$ consists of two
   disconnected triangles, that is, $K_3 \sqcup K_3$.
3. On $X_{\mathrm{adm}}$, distance $3$ occurs only for complementary pairs.
   By Theorem 2.5 there are exactly three such pairs, and they are pairwise
   disjoint. Therefore $G_3 \cong 3K_2$. $∎$

### Remark 2.6.2a [C]. Notation for the Triadic Layer

Below it is preferable to use the notation

$$
K_3\\sqcup K_3
$$

instead of the informal notation $2K_3$. This emphasizes that the object in
question is the disjoint union of two components of the relation scheme, not a
new single figure.

### Corollary 2.6.3 [D|graph]. Decomposition of Complete and Residual Adjacency

Let $A_{$R_1$},A_{$R_2$},A_{$R_3$}$ be the adjacency matrices of the graphs
$G_1,G_2,G_3$ on the same vertex order of $X_{\mathrm{adm}}$. Then:

$$
J-I = A_{R_1}+A_{R_2}+A_{R_3},
$$

that is, the complete graph on $X_{\mathrm{adm}}$ decomposes into three
disjoint Hamming layers. Moreover,

$$
A_{\mathrm{res}} = A_{R_1}+A_{R_2},
\qquad
C = A_{R_3},
$$

where $A_{\mathrm{res}}$ is residual adjacency and $C$ is the complementary
matching matrix.

**Proof.** By Theorem 2.6 and Definition 2.6.1, every unordered pair of distinct
vertices lies in exactly one of the three relations $R_1, R_2, R_3$. This gives
the first formula. Residual adjacency, by definition, excludes only identity and
complementary pairs, so it consists exactly of the distance $1$ and $2$
layers. Finally, the distance $3$ layer is precisely the complementary
matching. $∎$

### Remark 2.6.4. Two Carrier Graphs and One Hidden Axial Layer

Two carrier graphs are used primarily:

- $G_1\cong C_6$, the graph of the primitive process;
- $G_{\mathrm{res}}=G_1\cup G_2\cong K_{2,2,2}$, the residual carrier.

However, over the same set of states there naturally exists a third layer:

$$
G_3\cong 3K_2,
$$

which encodes the three complementary axes. This layer is auxiliary; a small
package of relations is fixed on $X_{\mathrm{adm}}$.

This partition fixes the following roles:

- $R_1$ is the primitive cycle and the first connectivity law of the shell;
- $R_2$ is the triadic layer of internal grouping;
- $R_3$ is the axial layer of complementary opposition.

### Theorem 2.6.5 [D|graph]. Internal Compatibility of Shells and the Three Relations

Consider the partition

$$
X_{\\mathrm{adm}} = \mathcal{C}_1 \sqcup \mathcal{C}_2,
$$

where

$$
\mathcal C_1=\{100,010,001\},
\qquad
\mathcal C_2=\{011,101,110\}.
$$

Then:

1. the relation $R_1$ lies entirely between the shells $\mathcal C_1$ and $\mathcal C_2$ and gives no edges inside the shells;
2. the relation $R_2$ lies entirely inside the shells and gives no edges between them;
3. the relation $R_3$ gives a perfect matching between $\mathcal C_1$ and $\mathcal C_2$;
4. for the corresponding adjacency matrices, the quotient matrices with respect to the partition $\mathcal C_1\sqcup\mathcal C_2$ are

   $$
Q(R_1)=
   \begin{pmatrix}
   0&2\\
   2&0
   \end{pmatrix},
   \qquad
   Q(R_2)=
   \begin{pmatrix}
   2&0\\
   0&2
   \end{pmatrix},
   \qquad
   Q(R_3)=
   \begin{pmatrix}
   0&1\\
   1&0
   \end{pmatrix};
$$

5. consequently,

   $$
Q(A_{\mathrm{res}})=Q(R_1)+Q(R_2)=
   \begin{pmatrix}
   2&2\\
   2&2
   \end{pmatrix}.
$$

**Proof.** For vertices of weights $1$ and $2$, Hamming distance $1$ occurs
only between shells, while distance $2$ occurs only inside each shell. By
Theorem 2.6.2, distance $3$ is realized only by complementary pairs, each of
which connects one vertex of weight $1$ and one vertex of weight $2$. The
neighbor counts are read immediately from the descriptions of the graphs
$C_6$, $K_3\sqcup K_3$, and $3K_2$. $∎$

### Theorem 2.6.6 [D|graph]. Small Symmetric Relation Scheme on $X_{\mathrm{adm}}$

Let

$$
A_0:=I,
\qquad
A_1:=A_{R_1},
\qquad
A_2:=A_{R_2},
\qquad
A_3:=A_{R_3}.
$$

Then the family of relations

$$
\{R_0,$R_1, R_2, R_3$\},
\qquad
R_0:=\{(x,x):x\in X_{\\mathrm{adm}}\},
$$

forms a commutative symmetric association scheme of class $3$ on the set
$X_{\mathrm{adm}}$.

Equivalently, the matrices $A_0,A_1,A_2,A_3$ satisfy:

1. they are pairwise orthogonal $0$-$1$ matrices and

   $$
A_0+A_1+A_2+A_3=J;
$$

2. each of them is symmetric;

3. their linear span is closed under multiplication, with

   $$
A_1^2 = 2A_0 + A_2,
   \qquad
   A_2^2 = 2A_0 + A_2,
   \qquad
   A_3^2 = A_0,
$$

   $$
A_1A_2 = A_2A_1 = A_1 + 2A_3,
   \qquad
   A_1A_3 = A_3A_1 = A_2,
   \qquad
   A_2A_3 = A_3A_2 = A_1.
$$

In particular, the intersection numbers are uniquely defined and do not depend
on the choice of a vertex pair inside the given relation.

**Proof.** By Corollary 2.6.3, the matrices $A_0,A_1,A_2,A_3$ are pairwise
non-overlapping and sum to $J$. Symmetry follows from the fact that all
relations $R_k$ are specified by Hamming distance. It remains to check closure
of products. For this it is enough to count the number of intermediate vertices
$z$ such that $(x,z)\in R_i$ and $(z,y)\in R_j$, separately for pairs
$(x,y)$ in each relation.

- From the graph $G_1\cong C_6$, each vertex has exactly two neighbors in
  $R_1$, and for a pair in $R_2$ there is exactly one two-step path through
  $R_1$. Therefore

  $$
A_1^2 = 2A_0 + A_2.
$$

- From the graph $G_2\cong K_3\sqcup K_3$, similarly, inside each triangle a
  vertex has exactly two neighbors, and for an adjacent pair in $R_2$ there is
  exactly one two-step path through $R_2$. Therefore

  $$
A_2^2 = 2A_0 + A_2.
$$

- Since $G_3\cong 3K_2$ is a perfect matching, applying a complementary edge
  twice returns the initial vertex:

  $$
A_3^2 = A_0.
$$

- For a pair in $R_1$ there is exactly one path of type $($R_1$,$R_2$)$, and for
  a pair in $R_3$ there are exactly two such paths; no other cases occur.
  Hence

  $$
A_1A_2=A_1+2A_3.
$$

- If one first traverses a complementary edge and then an edge of distance $1$,
  the endpoint is always at distance $2$; moreover, for each pair in $R_2$
  such a path is unique. Thus

  $$
A_1A_3=A_2.
$$

- Similarly, traversing an edge of distance $2$ after a complementary edge
  gives exactly the relation $R_1$, that is,

  $$
A_2A_3=A_1.
$$

Commutativity follows from the symmetry of the same intersection numbers. Hence
all axioms of a commutative symmetric association scheme are satisfied. $∎$

### Remark 2.6.6a. Standard Algebraic-Combinatorial Position

In the standard language of algebraic combinatorics, the obtained structure is a
small symmetric association scheme of class $3$ on six points.

It can be viewed as:

- an association scheme on the six vertices of the three-dimensional cross-polytope;
- a refinement of the pair
  $$
K_{2,2,2}\quad\text{and}\quad 3K_2,
$$

  where the first relation specifies octahedral adjacency and the second
  specifies antipodal matching;
- a small orbital scheme on the signed coordinate carrier, lying in the same
  standard class of objects as finite association schemes and their
  Bose-Mesner algebras.

The full external classification of such schemes is not used here.

### Remark 2.6.6b [Context]. External Mathematical Precedent

The obtained association scheme is a special case of the known three-class
symmetric association scheme on the vertices of the three-dimensional
cross-polytope. Its intersection numbers coincide with the standard values for
the orbital action of $S_3\times \mathbb Z_2$ on the punctured Boolean cube;
see Bannai--Ito and Godsil--Royle.

### Corollary 2.6.6c [D|cat]. Restricted Evaluation Functors of the Relation Scheme

Consider the category

$$
\mathbf{ASch}_3^{\mathrm{lab}},
$$

whose objects are labeled three-class symmetric association schemes

$$
(X;R_0,$R_1, R_2, R_3$)
$$

of the same type as the six-point relation scheme of the strict core, and whose
morphisms are scheme isomorphisms preserving the numbering of relation classes.

Then functors to the category of graphs arise:

$$
\mathrm{Ev}_1(X;R_0,$R_1, R_2, R_3$)=(X,R_1),
$$

$$
\mathrm{Ev}_2(X;R_0,$R_1, R_2, R_3$)=(X,R_2),
$$

$$
\mathrm{Ev}_3(X;R_0,$R_1, R_2, R_3$)=(X,R_3),
$$

$$
\mathrm{Ev}_{\mathrm{res}}(X;R_0,$R_1, R_2, R_3$)=(X,R_1\cup R_2).
$$

Thus the graphs $(X,$R_1$)$, $(X,$R_2$)$, $(X,$R_3$)$, and
$(X,$R_1$\cup $R_2$)$ are obtained as values of functors on one and the same
relation scheme.

**Proof.** A morphism in $\mathbf{ASch}_3^{\mathrm{lab}}$, by definition,
preserves the carrier and sends each relation $R_i$ to the corresponding
$R'_i$. Therefore the same vertex bijection is an isomorphism of each graph
$(X,R_i)$ and of $(X,$R_1$\cup $R_2$)$. Identities and composition are inherited
directly. $∎$

### Remark 2.6.7. What Is Carrier-Level in This Relation Scheme and What Is Not

The relation scheme on $X_{\mathrm{adm}}$ is fully closed, but its layers are
used unevenly.

- $A_1$ is the process layer.
- $A_2$ is the triadic layer of internal grouping of the shell.
- $A_1+A_2$ is the residual geometric carrier.
- $A_3$ is the axial/complementary layer; the transport and chamber packages
  are not built on it.

The relation algebra of the core is fully closed; the carrier role remains with
the sublayers $A_1$ and $A_1+A_2$.

### Definition 2.6.8 [D|graph]. Finite Signature of the Relation Scheme

The finite signature of the relation scheme is the triple

$$
\Sigma_{\mathrm{core}}
=
\bigl(
\mathrm{relation\_counts},
\mathrm{chamber\_support},
\mathrm{shell\_types}
\bigr),
$$

where for each of the three relations $R_1, R_2, R_3$:

1. $relation_counts(R_i)$ is the number of edges of the graph $G_i=($X_{\\mathrm{adm}}$,R_i)$;
2. $shared_chambers(R_i)$ is the number of chambers shared by a typical pair of poles from $R_i$, computed from the fixed incidence matrix $B$; in the computational files the service name $chamber_support(R_i)$ is preserved for this quantity;
3. $shell_types(R_i)$ is a coarse positional label of the relation class relative to the partition

$$
X_{\\mathrm{adm}} = \mathcal{C}_1 \sqcup \mathcal{C}_2.
$$

### Theorem 2.6.9 [D]. Exact Values of the Finite Core Signature

For the strict $3$-bit core, the finite signature of the relation scheme is

$$
\mathrm{relation\_counts} = \{ R_1: 6,\ R_2: 6,\ R_3: 3 \},
$$

$$
\mathrm{shared\_chambers} = \{ R_1: 2,\ R_2: 2,\ R_3: 0 \},
$$

$$
\mathrm{shell\_types} = \{ R_1: \mathrm{between},\ R_2: \mathrm{within},\ R_3: \mathrm{axial} \}.
$$

**Proof.**

1. By Theorem 2.6.2, the graph $G_1$ is isomorphic to $C_6$, hence contains
   $6$ edges; the graph $G_2$ is isomorphic to $K_3\sqcup K_3$ and
   therefore also contains $6$ edges; the graph $G_3$ is isomorphic to
   $3K_2$ and contains $3$ edges.
2. By the fixed incidence matrix $B$, every pair in $R_1$ and every pair in
   $R_2$ has exactly two common chambers, while every pair in $R_3$ has no
   common chambers. Therefore

$$
\mathrm{shared\_chambers} = \{2, 2, 0\}.
$$

3. By Theorem 2.6.5, the relation $R_1$ lies entirely between the shells
   $\mathcal C_1,\mathcal C_2$, the relation $R_2$ lies entirely inside the
   shells, and the relation $R_3$ coincides with complementary axial
   antipodality. This gives the labels $between$, $within$, $axial$. $∎$

The local machine check of block $2.6.2$-$2.6.10$ is performed by the
functions

```text
relation_scheme_test()
compute_core_bridge_signature()
core_bridge_signature_test()
```

from the file `DOT_Core_verifier.py`.

### Corollary 2.6.10 [G1]. AMR/Core Interface

If $AMR$ is connected to the strict core only through the minimal external
interface, then only two readings arise:

$$
3 \rightsquigarrow (R_1, R_2), \qquad 4 \rightsquigarrow R_3.
$$

Here $3 \rightsquigarrow ($R_1$, $R_2$)$ means the supported pair, while
$4 \rightsquigarrow R_3$ means the axially locked layer. A full functor
$k \mapsto R_k$ is not claimed, and the case $k \ge 5$ is not considered.

---
## 3. Standard Graphs on Six States

Within the standard relation scheme, two carrier graphs are distinguished: the
graph of the primitive process and the residual carrier.

### Definition 3.1 [C]. Operator of Primitive Bit Transitions

Let $N_1, N_2, N_3$ be the three coordinate flips on $X_0$. Define

$$
A_{\mathrm{prim}} := P_{\mathrm{adm}} (N_1 + N_2 + N_3) P_{\mathrm{adm}}
$$

as an operator on functions on $X_{\mathrm{adm}}$.

Equivalently: two admissible states are connected by an edge in
$A_{\mathrm{prim}}$ if and only if they differ in exactly one bit and both
remain admissible.

### Theorem 3.2 [D|C]. The Primitive Process Is $C_6$

The graph with adjacency matrix $A_{\mathrm{prim}}$ is the cycle

$$
100 \to 110 \to 010 \to 011 \to 001 \to 101 \to 100.
$$

Consequently, it is isomorphic to $C_6$.

**Proof.** Each admissible state has exactly two admissible $1$-bit
transitions. The result is a connected $2$-regular graph on six vertices, that
is, $C_6$. $∎$

### Corollary 3.2.1 [D|C]. Fixedness of the Minimal Cycle

The minimal cycle requires no separate choice: it is uniquely specified by the
operator $A_{\mathrm{prim}}$, that is,

$$
\gamma_{\mathrm{prim}} := (X_{\\mathrm{adm}}, A_{\mathrm{prim}})
$$

is the unique connected graph on $X_{\mathrm{adm}}$ whose edges coincide
exactly with admissible one-coordinate flips.

**Proof.** The edge set is completely fixed by the definition of an admissible
one-bit transition. Therefore the graph with this edge set is unique. By
Theorem 3.2, it is $C_6$. $∎$

### Definition 3.3 [C]. Residual Adjacency

On the same set $X_{\mathrm{adm}}$, define a second graph:

$$
x \sim_{\mathrm{res}} y
\iff
x \neq y \text{ and } y \neq \bar{x}.
$$

That is, all pairs are connected except the three complementary pairs.

Let $C$ be the permutation matrix defining the complement on
$X_{\mathrm{adm}}$, and let $J$ be the all-ones matrix. Then

$$
A_{\mathrm{res}} = J - I - C.
$$

### Theorem 3.4 [D|C]. The Residual Carrier Is $K_{2,2,2}$

The residual graph is the complete tripartite graph whose parts are the three
complementary pairs. Hence

$$
G_{\mathrm{res}} \cong K_{2,2,2}.
$$

**Proof.** The complementary pairs form three parts; there are no edges inside
the parts, and all possible edges are drawn between different parts. $∎$

The local machine check of blocks $3.2$-$4.6$ is performed by the functions

```text
build_admissible_core()
combinatorial_core_test()
build_C6()
build_K222()
build_Q3()
build_incidence_matrix()
stanley_reisner_check()
```

from the file `DOT_Core_verifier.py`.

### Remark 3.5. Non-Identity of the Two Operators

$A_{\mathrm{prim}}$ and $A_{\mathrm{res}}$ are different operators on the
same set of six states.

- $A_{\mathrm{prim}}$ has degree $2$ and the spectrum of the cycle $C_6$;
- $A_{\mathrm{res}}$ has degree $4$ and the spectrum of $K_{2,2,2}$.
- more precisely,
  $$
A_{\mathrm{prim}}=A_{R_1},
  \qquad
  A_{\mathrm{res}}=A_{R_1}+A_{R_2}.
$$

This separation removes the main internal conflation of the previous version.

---

## 4. Octahedron and Chambers

### Definition 4.1 [D|graph]. Standard Octahedron

Let

$$
O_3 := \{x \in \mathbb{R}^3 : |x_1| + |x_2| + |x_3| \le 1\}.
$$

Its six vertices are the poles $\pm e_1, \pm e_2, \pm e_3$.

### Theorem 4.2 [D|graph]. Residual Graph as the $1$-Skeleton of the Octahedron

The $1$-skeleton of the octahedron $O_3$ is isomorphic to $K_{2,2,2}$.

**Proof.** Opposite poles are not connected, while any non-opposite pair of
poles is connected. $∎$

### Definition 4.3 [D|graph]. Sign Chambers

For each sign vector $\sigma = (\sigma_1,\sigma_2,\sigma_3) \in \{\pm 1\}^3$,
define the chamber

$$
T_\sigma := \{x \in O_3 : \sigma_i x_i \ge 0 \text{ for } i=1,2,3\}.
$$

### Theorem 4.4 [D|graph]. Chamber Graph

The eight chambers $T_\sigma$ are tetrahedra. Their adjacency graph is
isomorphic to the cube $Q_3$.

**Proof.** For fixed $\sigma$, the conditions

$$
\sigma_i x_i \ge 0 \qquad (i=1, 2, 3)
$$

cut out one of the eight sign sectors in the octahedron. Its vertices are the
three poles

$$
\sigma_1 e_1, \qquad \sigma_2 e_2, \qquad \sigma_3 e_3
$$

and the common center $0$, so each chamber is indeed a tetrahedron.

Now compare two chambers $T_\sigma$ and $T_\tau$.

1. If $\sigma$ and $\tau$ differ in exactly one coordinate, then two common
   coordinate half-planes agree, while the sign changes in one coordinate.
   Hence the chambers have a common triangular face passing through the center
   and two coincident poles.
2. If $\sigma$ and $\tau$ differ in two coordinates, then only one axis
   agrees; the intersection of the chambers shrinks to an edge.
3. If $\sigma$ and $\tau$ differ in all three coordinates, then their
   intersection consists only of the center.

Therefore chamber adjacency along a codimension-$1$ face occurs if and only if
the sign triples differ in exactly one coordinate. This is precisely the
adjacency rule of the hypercube $Q_3$. $∎$

### Corollary 4.4.1 [D|graph]. Explicit Bijection Between Chambers and Cube Vertices

The map

$$
\Phi(\sigma_1,\sigma_2,\sigma_3)
=
\left(
\frac{1+\sigma_1}{2},
\frac{1+\sigma_2}{2},
\frac{1+\sigma_3}{2}
\right)
$$

gives a bijection between the set of chambers of the octahedron and the vertex
set of the cube $Q_3$.

Moreover, two chambers are adjacent if and only if their images differ in
exactly one bit.

**Proof.** The formula

$$
\Phi(\sigma_1,\sigma_2,\sigma_3)
=
\left(
\frac{1+\sigma_1}{2},
\frac{1+\sigma_2}{2},
\frac{1+\sigma_3}{2}
\right)
$$

sends the sign $-1$ to the bit $0$, and the sign $+1$ to the bit $1$.
Therefore the inverse map is explicit:

$$
\Phi^{-1}(b_1, b_2, b_3) = (2b_1-1,\ 2b_2-1,\ 2b_3-1),
\qquad (b_1, b_2, b_3) \in \{0, 1\}^3.
$$

Thus $\Phi$ is a bijection between sign triples and cube vertices.

By Theorem 4.4, two chambers are adjacent if and only if the corresponding sign
triples differ in exactly one coordinate. After applying $\Phi$, this means
changing exactly one bit. Therefore $\Phi$ sends the chamber adjacency graph
to the standard hypercube graph $Q_3$. $∎$

### Corollary 4.4.2 [D|cat]. Induced Functor on Path Categories

If one considers not merely the graphs but their path categories, then the map
$\Phi$ induces a functor

$$
\Phi_* : \mathrm{Path}(\mathrm{Cham}(O_3)) \to \mathrm{Path}(Q_3)
$$

by the rule

$$
\Phi_*:=\mathrm{Path}(\Phi),
$$

which preserves identities and composition:

$$
\Phi_*(\mathrm{id}_X) = \mathrm{id}_{\Phi_*(X)}, \qquad \Phi_*(g \circ f) = \Phi_*(g) \circ \Phi_*(f).
$$

**Proof.** This is the standard functorial lift of the graph map $\Phi$. On
objects, the functor is given by the bijection $\Phi$. On generating
edge-morphisms it is given by the rule “change one sign $\leftrightarrow$
change one bit”. For paths, composition is concatenation, and $\Phi_*$ acts
componentwise on edge sequences, so it automatically preserves identities and
composition. $∎$

### Corollary 4.4.3 [D|cat]. $\Phi_*$ Is an Isomorphism of Path Categories

The functor

$$
\Phi_* : \mathrm{Path}(\mathrm{Cham}(O_3)) \to \mathrm{Path}(Q_3)
$$

is an isomorphism of categories. In particular, it is full, faithful, and
surjective on objects.

**Proof.** By Corollary 4.4.1, the map $\Phi$ is bijective on objects and
sends edges to edges and non-edges to non-edges. Therefore every path in $Q_3$
lifts uniquely along $\Phi^{-1}$ to a path in $\mathrm{Cham}($O_3$)$,
and conversely. Hence $\Phi_*$ has an inverse functor induced by
$\Phi^{-1}$. $∎$

### Definition 4.5 [D|graph]. Incidence Matrix

Define

$$
B \in \{0,1\}^{6 \times 8}, \qquad B_{v,\sigma} = 1 \iff v \in \partial T_\sigma.
$$

### Proposition 4.6 [D|graph]. Incidence Identities

The following hold:

$$
B \mathbf{1}_8 = 4 \mathbf{1}_6, \qquad
B^\top \mathbf{1}_6 = 3 \mathbf{1}_8.
$$

Moreover,

$$
B B^\top = 4 I_6 + 2 A_{\mathrm{oct}}.
$$

**Proof.** Below we use only the bit/sign combinatorics of chambers and poles;
the proof does not require appeal to geometric intuition about the octahedron.
Write the poles as $v=s e_i$ and $w=t e_j$, where
$s,t\in\{\pm1\}$ and $i,j\in\{1,2,3\}$.

1. The pole $v=s e_i$ lies in the chamber $T_\sigma$ if and only if

   $$
\sigma_i=s.
$$

   The other two signs are free, so each pole is incident to exactly $2^2=4$
   chambers. This gives the diagonal entries

   $$
(BB^\top)_{v,v}=4.
$$

2. If $v=s e_i$ and $w=-s e_i$ are opposite poles of the same axis, then the
   conditions

   $$
\sigma_i=s,
   \qquad
   \sigma_i=-s
$$

   are incompatible. Hence

   $$
(BB^\top)_{v,w}=0.
$$

3. If $i\neq j$, joint incidence requires only

   $$
\sigma_i=s,
   \qquad
   \sigma_j=t.
$$

   The third sign is free, so there are exactly $2$ common chambers. Therefore

   $$
(BB^\top)_{v,w}=2
   \qquad (i\neq j).
$$

   But exactly such pairs form the edges of the $1$-skeleton of the
   octahedron, that is,

   $$
(A_{\mathrm{oct}})_{v,w}=1
   \qquad \Longleftrightarrow \qquad i\neq j.
$$

Consequently,

$$
BB^\top = 4I_6 + 2A_{\mathrm{oct}}.
$$

In addition, each chamber fixes one sign on each of the three axes and therefore
has exactly three polar vertices, which gives

$$
B^\top \mathbf{1}_6 = 3\mathbf{1}_8.
$$

$∎$

---
## 5. Spectra of Basic Carriers

### Definition 5.1. Graph Laplacian

For any finite simple graph with adjacency matrix $A$ and diagonal degree
matrix $D$, set

$$
L := D - A.
$$

### Theorem 5.2 [D|graph]. Exact Laplacian Spectra

For the basic carriers of the strict core, we have:

$$
\mathrm{Spec}(L_{C_6}) = \{0, 1, 1, 3, 3, 4\},
$$

$$
\mathrm{Spec}(L_{Q_3}) = \{0, 2, 2, 2, 4, 4, 4, 6\},
$$

$$
\mathrm{Spec}(L_{K_{2,2,2}}) = \{0, 4, 4, 4, 6, 6\}.
$$

Therefore,

$$
\lambda_2(C_6) = 1, \qquad \lambda_2(Q_3) = 2, \qquad \lambda_2(K_{2,2,2}) = 4.
$$

**Proof.**

- For $C_6$, use the standard cycle formula $2-2\cos(2\pi k/6)$.
- For $Q_3$, use the hypercube spectrum $2m$ with binomial multiplicities.
- For $K_{2,2,2}$, use the known spectrum of the complete tripartite graph or the formula $A_{\mathrm{res}} = J - I - C$. $∎$

### Proposition 5.3 [D|graph]. Effective Resistances on Edges

For edges of the three basic graphs, we obtain:

$$
R_{\mathrm{eff}}^{C_6} = \frac{5}{6}, \qquad
R_{\mathrm{eff}}^{Q_3} = \frac{7}{12}, \qquad
R_{\mathrm{eff}}^{K_{2,2,2}} = \frac{5}{12}.
$$

**Proof.** Use edge-transitivity and Foster's theorem:

$$
\sum_{\{u,v\}\in E} R_{\mathrm{eff}}(u,v) = |V| - 1.
$$

$∎$

---

## 6. Composite Graph

### Definition 6.1 [C]. Composite Adjacency Matrix and Block Laplacian

Fix the incidence matrix $B$. Then

$$
A_{\mathrm{block}} =
\begin{pmatrix}
A_{\mathrm{oct}} & B \\
B^\top & A_{\mathrm{cube}}
\end{pmatrix},
\qquad
L_{\mathrm{block}} = D_{\mathrm{block}} - A_{\mathrm{block}}.
$$

The pole vertices of the octahedron have full degree $8$, and the chamber
vertices have full degree $6$.

### Definition 6.2. Axial Differences and Sign Characters of Chambers

For each axis $i \in \{1,2,3\}$, denote by $d_i \in \mathbb{R}^6$ the
difference of the two opposite poles on axis $i$, and by
$\chi_i \in \mathbb{R}^8$ the sign character

$$
\chi_i(\sigma) = \sigma_i, \qquad \sigma \in \{\pm 1\}^3.
$$

These vectors satisfy the identities

$$
A_{\mathrm{oct}} d_i = 0, \qquad
A_{\mathrm{cube}} \chi_i = \chi_i, \qquad
B \chi_i = 4 d_i, \qquad
B^\top d_i = \chi_i.
$$

### Theorem 6.3 [D|graph]. Exact Spectrum of the Block Laplacian

We have

$$
\mathrm{Spec}(L_{\mathrm{block}}) = \{0^1,\, 4^3,\, 7^4,\, 9^4,\, 10^2\}.
$$

In particular,

$$
\lambda_2(L_{\mathrm{block}})=4.
$$

**Proof.** Decompose the vertex space by symmetries.

1. **Constant sector.**
   On the linear span of the vectors $(\mathbf{1}_6,0)$ and
   $(0,\mathbf{1}_8)$, the block Laplacian reduces to the matrix

   $$
\begin{pmatrix}
   4 & -4\\
   -3 & 3
   \end{pmatrix},
$$

   whose eigenvalues are $0$ and $7$.

2. **Axial sector.**
   For each axis $i$, the space $\mathrm{span}\{(d_i,0),(0,\chi_i)\}$ is
   invariant. In this basis, the block Laplacian has the form

   $$
\begin{pmatrix}
   8 & -4\\
   -1 & 5
   \end{pmatrix},
$$

   whose eigenvalues are $4$ and $9$. For $\lambda=4$, we obtain

   $$
\begin{pmatrix}
   8 & -4\\
   -1 & 5
   \end{pmatrix}
   \binom{\alpha}{\beta}
   =
   4\binom{\alpha}{\beta}
   \quad\Longleftrightarrow\quad
   \alpha=\beta,
$$

   so in each axis the eigenline for $\lambda=4$ is
   $\mathrm{span}\{d_i\oplus\chi_i\}$. This contributes $4^3$ and $9^3$.

3. **Quadratic chamber characters.**
   The three Walsh characters $\chi_{ij}(\sigma)=\sigma_i\sigma_j$ satisfy
   $A_{\mathrm{cube}} \chi_{ij} = -\chi_{ij}$ and $B\chi_{ij}=0$. Therefore
   they are eigenvectors of the block Laplacian with eigenvalue $6-(-1)=7$.
   This contributes $7^3$.

4. **Cubic chamber character.**
   The character $\chi_{123}(\sigma)=\sigma_1\sigma_2\sigma_3$ satisfies
   $A_{\mathrm{cube}} \chi_{123}=-3\chi_{123}$ and $B\chi_{123}=0$, so its
   block eigenvalue is $6-(-3)=9$. This gives one additional $9$.

5. **Sector of sums over octahedral parts.**
   The subspace of vectors that are constant on each complementary pair and have
   zero total sum has dimension $2$. On it $A_{\mathrm{oct}}$ acts as $-2$,
   and $B^\top$ vanishes, because every chamber chooses one pole from each
   pair. Hence the block eigenvalue is $8-(-2)=10$, contributing $10^2$.

The sum of multiplicities is $14$, so the spectrum is exhausted. $∎$

### Theorem 6.4 [D|graph]. Exact Energy Ratio $4:1$ on the Slow Subspace

Let

$$
E_4 := \ker(L_{\mathrm{block}} - 4I).
$$

Then for every nonzero vector $v = x \oplus y \in E_4$, where
$x \in \mathbb{R}^6$ lives on the poles and $y \in \mathbb{R}^8$ on the
chambers, we have

$$
\frac{\|y\|^2}{\|x\|^2} = 4.
$$

**Proof.** From the previous theorem,

$$
(L_{\mathrm{block}} - 4I)(d_i \oplus \chi_i) = 0 \qquad (i=1, 2, 3),
$$

because in the axial $2\times2$ block of Theorem 6.3 the vector $(1,1)$ is
an eigenvector for $\lambda=4$. The vectors $d_i\oplus\chi_i$ are linearly
independent because their polar parts $d_i$ are linearly independent. By
Theorem 6.3, the multiplicity of eigenvalue $4$ is $3$. Hence

$$
E_4 = \mathrm{span}\{d_1 \oplus \chi_1,\ d_2 \oplus \chi_2,\ d_3 \oplus \chi_3\}.
$$

Now compute the norms. By definition, each $d_i$ has exactly two nonzero
coordinates $+1$ and $-1$, so

$$
\|d_i\|^2 = 1^2 + (-1)^2 = 2.
$$

Each character $\chi_i$ on the $8$ chambers takes only the values $\pm1$,
so

$$
\|\chi_i\|^2 = \sum_{\sigma \in \{\pm1\}^3}\chi_i(\sigma)^2 = 8.
$$

Moreover, the families $\{d_i\}$ and $\{\chi_i\}$ are pairwise orthogonal.
Therefore for

$$
v = \sum_{i=1}^3 a_i (d_i \oplus \chi_i)
$$

we obtain

$$
\|x\|^2 = 2 \sum_i a_i^2, \qquad
\|y\|^2 = 8 \sum_i a_i^2.
$$

Thus

$$
\|y\|^2 / \|x\|^2 = 4.
$$

$∎$

### Corollary 6.4.1 [D|graph]. Structural Origin of the Coefficient $4$ in the Three-Dimensional Case

The number $4$ in Theorem 6.4 arises from two independent $3$-dimensional
facts:

1. in the axial basis of the slow subspace, the coupling coefficient between the polar and chamber layers is

   $$
t_3=1;
$$

2. the norms of the basic axial and chamber vectors are

   $$
\|d_i\|^2=2,
   \qquad
   \|\chi_i\|^2=8.
$$

The first fact comes from the axial $2\times2$ block of Theorem 6.3, and the
second from the explicit norm computation in the proof of Theorem 6.4.

Therefore,

$$
\frac{\|\chi_i\|^2}{\|d_i\|^2}=\frac{8}{2}=4,
$$

and hence on the whole slow subspace

$$
\|y\|^2=4\|x\|^2.
$$

**Proof.** In Theorem 6.3, the slow eigenspace is obtained from axial vectors of
the form

$$
d_i\oplus t_3\chi_i.
$$

In the three-dimensional case no additional rescaling occurs, hence $t_3=1$.
After this, the coefficient $4$ is simply the ratio of squared norms of the
chamber and polar axial bases: $8/2=4$. $∎$

### Remark 6.4.2. Why This Is Not an All-$n$ Law

Theorem 6.4 closes the exact $4:1$ law only for the $3$-dimensional composite
block. In the general $n$-dimensional block, a dimension-dependent relation
holds:

$$
r_n:1,
$$

and only for $n=3$ do we have

$$
r_3=4.
$$

Therefore the open question is not “whether $4:1$ holds in all dimensions”,
but “why the coefficient in the $3$-dimensional slow sector is exactly $4$”.

This statement does not reduce to one isolated example.

### Theorem 6.4.3 [D|graph|rep]. Axial Intertwiner and the Invariant Origin of the Coefficient $4$

Let

$$
D:=\mathrm{span}\{d_1,d_2,d_3\}\subset\mathbb R^6,
\qquad
\mathcal X:=\mathrm{span}\{\chi_1,\chi_2,\chi_3\}\subset\mathbb R^8.
$$

Then the following statements hold.

1. The subspaces $D$ and $\mathcal X$ are invariant under the natural action
   of coordinate permutations and global complement on the polar and chamber layers.
2. The restriction

   $$
U:=B^\top\!\mid_D : D\to\mathcal X
$$

   is an equivariant isomorphism, with

$$
U(d_i) = \chi_i \qquad (i=1, 2, 3).
$$

3. After normalization

   $$
\widehat d_i:=\frac{d_i}{\sqrt2},
   \qquad
   \widehat\chi_i:=\frac{\chi_i}{\sqrt8}
$$

   the matrices $B$ and $B^\top$ act on the axial sector as the scalar $2$:

$$
B^\top \widehat d_i = 2\widehat\chi_i, \qquad B\widehat\chi_i = 2\widehat d_i.
$$

Therefore the coefficient $4$ in Theorem 6.4 is the square of the fixed
normalized axial coupling coefficient:

$$
4 = 2^2.
$$

**Proof.**

1. A coordinate permutation sends axis $i$ to axis $\pi(i)$, while global
   complement changes the sign of axial differences and sign characters:

   $$
d_i\mapsto d_{\pi(i)},\qquad \chi_i\mapsto \chi_{\pi(i)},
$$

   $$
d_i\mapsto -d_i,\qquad \chi_i\mapsto -\chi_i.
$$

   Therefore both $D$ and $\mathcal X$ are invariant subspaces.
2. From Definition 6.2 we already know that

   $$
B^\top d_i=\chi_i,
   \qquad
   B\chi_i=4d_i.
$$

   Hence $U=B^\top\!\mid_D$ sends the basis $\{d_i\}$ to the basis
   $\{\chi_i\}$ and is therefore an isomorphism. Equivariance follows from the
   fact that admissible symmetries simultaneously permute axes on the polar and
   chamber layers and preserve the incidence relation.
3. The normalized formulas are obtained by direct substitution:

   $$
B^\top \widehat d_i
   =
   \frac{1}{\sqrt2}B^\top d_i
   =
   \frac{1}{\sqrt2}\chi_i
   =
   2\widehat\chi_i,
$$

   $$
B\widehat\chi_i
   =
   \frac{1}{\sqrt8}B\chi_i
   =
   \frac{4}{\sqrt8}d_i
   =
   2\widehat d_i.
$$

   Therefore, on the normalized axial sector, the incidence-coupling has the
   single singular value $2$, and the coefficient $4$ is its square. $∎$

### Remark 6.4.4. Structure of the Coefficient $4$

Theorem 6.4.3 does not turn $4:1$ into an all-$n$ law and does not remove
the dimensional specificity of the case $n=3$. It makes a different point more
precise:

- the number $4$ in Theorem 6.4 does not arise as a numerical accident of one
  block diagonalization;
- it is the square of the normalized axial incidence coefficient between two
  equivariant subspaces $D$ and $\mathcal X$;
- $4:1$ is a special law of the three-dimensional slow sector, not a universal
  dimensional constant.

The local machine check of the spectral block $5$-$6$ is performed by the
functions

```text
spectral_test()
block_operator_spectral_test()
presentation_and_intertwiner_test()
```

from the file `DOT_Core_verifier.py`.

---

## 7. Twisted Transport

### Definition 7.1 [D|C]. Fixed Minimal Cycle

Let

$$
\gamma := \gamma_{\mathrm{prim}} = (X_{\\mathrm{adm}}, A_{\mathrm{prim}}).
$$

By Corollary 3.2.1, this is the fixed primitive cycle of length $6$ inside the
graph of admissible states, and combinatorially $\gamma \cong C_6$.

### Definition 7.2 [C]. $Z_2$-Transport Data

To each oriented edge $e$ of the cycle $\gamma$, assign a sign
$\varepsilon_e \in \{\pm 1\}$. A local status $s_i \in \{\pm 1\}$ is
transported by the rule

$$
s_{i+1} = \varepsilon_i s_i.
$$

### Theorem 7.3 [D|C]. Gauge-Invariant Combinatorial Holonomy

Under a gauge transformation $s_i' = g_i s_i$, where $g_i \in \{\pm 1\}$,
the edge signs transform as

$$
\varepsilon_i' = g_{i+1} \varepsilon_i g_i^{-1},
$$

and the product around the cycle

$$
\mathrm{Hol}(\gamma) := \prod_{i=0}^5 \varepsilon_i
$$

remains invariant.

**Proof.**

$$
\prod_i \varepsilon_i' = \prod_i g_{i+1} \varepsilon_i g_i^{-1} = \left(\prod_i g_{i+1} g_i^{-1}\right) \left(\prod_i \varepsilon_i\right) = \prod_i \varepsilon_i.
$$

$∎$

### Remark 7.3.1 [D|C]. Holonomy and Monodromy in the Discrete Context

The product

$$
\mathrm{Hol}(\gamma) = \prod_{i=0}^{5} \varepsilon_i
$$

is understood as **combinatorial holonomy** or, equivalently, **discrete
monodromy** of a flat $Z_2$-connection on the cycle.

- Since the carrier is a finite graph-cycle, and no curvature is introduced
  outside the cycle itself, there is no distinction here between smooth holonomy
  and monodromy.
- After identifying $\gamma \cong S^1$, this is the action

  $$
\pi_1(S^1)\cong \mathbb Z
$$

  on the fiber $\{\pm 1\}$ through a representation into $\mathbb{Z}_2$.

### Theorem 7.4 [D|C]. Classification of the Transport Class over $S^1$

Let $|\gamma|$ denote the geometric realization of the chosen cycle
$\gamma\cong C_6$. Then $|\gamma|$ is homeomorphic to the circle $S^1$,
and gauge-equivalence classes of $Z_2$-transports over $|\gamma|$ are
classified by the group

$$
H^1(|\gamma|;\mathbb{Z}_2) \cong H^1(S^1;\mathbb{Z}_2) \cong \mathbb{Z}_2.
$$

The trivial class has holonomy $+1$, and the nontrivial class has holonomy
$-1$.

**Proof.** The geometric realization of the finite cycle $C_6$ is a circle,
that is, $|\gamma| \cong S^1$. Therefore the standard classification of
principal $\mathbb{Z}_2$-bundles over the circle applies to $|\gamma|$, and
is equivalent to the description through

$$
\mathrm{Hom}(\pi_1(|\gamma|),\mathbb{Z}_2)
\cong
\mathrm{Hom}(\pi_1(S^1),\mathbb{Z}_2).
$$

$∎$

### Corollary 7.5 [D|C]. Double-Return Law

If holonomy is $-1$, then one full turn changes the local sign and two full
turns return it:

$$
\mathcal{T}(s) = -s, \qquad \mathcal{T}^2(s)=s.
$$

$∎$

The local machine check of transport block $7$ is performed by the function

```text
holonomy_test_exact()
```

from the file `DOT_Core_verifier.py`.

### Proposition 7.6 [D|C]. Correct Interpretation through the Associated Mobius Bundle

Let $P \to S^1$ be the nontrivial principal $Z_2$-bundle defined by the
holonomy class $-1$.

1. The associated interval bundle

   $$
P \times_{Z_2} [-1,1]
$$

   is the Mobius band.

2. The associated real line bundle

   $$
L := P \times_{Z_2} \mathbb{R}
$$

   is the nontrivial real line bundle over $S^1$.

3. The principal bundle $P$ has no global section.
4. The line bundle $L$ has the zero section, but has no everywhere nonzero global section.

**Proof.** This is the standard construction of associated bundles from the
nontrivial action of $\mathbb{Z}_2$ on $[-1,1]$ or $\mathbb{R}$. The
nontriviality of the bundle class forbids a global section of $P$ and forbids
an everywhere nonzero section of $L$. The zero section in a vector bundle
always exists. $∎$

The earlier idea of “Mobius twisting” should be read as the associated linear or
interval bundle of a nontrivial principal $Z_2$-bundle, not as an independent
surface.

### Remark 7.7. What Is Strict Here and What Is Not

Strict:

- nontrivial $Z_2$-holonomy on the chosen cycle;
- invariance of the product around the cycle;
- double return;
- interpretation through the associated Mobius bundle.

Not strict:

- any formulation claiming that the whole octahedral carrier itself is a
  Mobius-type object.

### Definition 7.8 [C]. Admissible Symmetries of the Presentation of the Strict $3$-Bit Core

Denote by

$$
\Gamma_3:=S_3\times \mathbb Z_2^{\mathrm{glob}}
$$

the group of admissible symmetries of the presentation, acting on the raw cube
$X_0=\{0,1\}^3$ as follows:

1. an element $\pi\in S_3$ permutes coordinates;
2. the nontrivial element of $\mathbb Z_2^{\mathrm{glob}}$ acts by global complement

   $$
x\mapsto \bar x.
$$

Thus an admissible change of presentation consists of a coordinate permutation
and, possibly, a subsequent full bitwise inversion.

### Theorem 7.8.1 [D|C]. Invariance under Change of Presentation in the Strict $3$-Bit Core

For every element $g\in\Gamma_3$, the following statements hold.

1. $g$ preserves the set of admissible states $X_{\mathrm{adm}}$.
2. $g$ preserves Hamming distance on $X_{\mathrm{adm}}$.
3. Consequently, $g$ preserves all relations

   $$
R_0,$R_1, R_2, R_3$,
$$

   and hence also the relation scheme, the graph of the primitive process

   $$
A_{\mathrm{prim}}=A_{R_1},
$$

   and the residual carrier

   $$
A_{\mathrm{res}}=A_{R_1}+A_{R_2}.
$$

4. On the geometric level, there is an induced isometry of the cross-polytope
   $O_3$ that sends poles to poles, chambers to chambers, and preserves the
   incidence matrix $B$ up to row and column permutations.

Therefore the package

$$
\mathfrak N_3:=
\bigl(
X_{\\mathrm{adm}},\,
\mathcal C_1\sqcup\mathcal C_2,\,
R_0,$R_1, R_2, R_3$,\,
A_{\mathrm{prim}},\,
A_{\mathrm{res}},\,
O_3,\,
\mathrm{Cham}(O_3),\,
B
\bigr)
$$

is stable with respect to all admissible presentation symmetries from
$\Gamma_3$, up to natural isomorphism.

**Proof.**

1. Coordinate permutation sends states of weights $0,1,2,3$ to states of the
   same weights. Global complement sends weight $k$ to weight $3-k$. Hence
   the set

   $$
X_{\\mathrm{adm}}=\{0,1\}^3\setminus\{000,111\}
$$

   is preserved.
2. Both coordinate permutation and global complement preserve Hamming distance.
   Thus for any $x,y\in X_{\mathrm{adm}}$ and any $k\in\{0,1,2,3\}$, we have

   $$
d_H(x,y)=k
   \iff
   d_H(gx,gy)=k.
$$

   Therefore each relation $R_k$ is preserved.
3. Since $A_{\mathrm{prim}}=A_{$R_1$}$ and $A_{\mathrm{res}}=A_{$R_1$}+A_{$R_2$}$,
   the graph of the primitive process and the residual carrier are preserved automatically.
4. A coordinate permutation is realized by a permutation linear isometry of
   $\mathbb R^3$, while global complement is the central symmetry $x\mapsto -x$.
   Both isometries send the pole set $\{\pm e_1,\pm e_2,\pm e_3\}$ to itself
   and act on sign chambers by permuting sign vectors $\sigma\in\{\pm1\}^3$.
   The incidence relation “the pole lies on the boundary of the chamber” is
   preserved, because it depends only on agreement between the sign of the pole
   and the corresponding component of $\sigma$. Hence the matrix $B$ is
   preserved up to simultaneous row and column permutations. $∎$

### Corollary 7.8.1.A [D|C]. Algebraic Condensation of the Relation Scheme

On the six-point admissible carrier $X_{\mathrm{adm}}$, define

$$
\mathcal A_6:=\mathrm{span}_{\mathbb R}\{I,A_{R_1},A_{R_2},A_{R_3}\}\subset M_6(\mathbb R).
$$

Then $\mathcal A_6$ is a commutative finite-dimensional subalgebra, and in the
basis $\{I,A_{$R_1$},A_{$R_2$},A_{$R_3$}\}$ the following formulas hold:

$$
A_{R_1}^2 = 2I + A_{R_2},\qquad
A_{R_1}A_{R_2} = A_{R_1} + 2A_{R_3},\qquad
A_{R_1}A_{R_3} = A_{R_2},
$$

$$
A_{R_2}^2 = 2I + A_{R_2},\qquad
A_{R_2}A_{R_3} = A_{R_1},\qquad
A_{R_3}^2 = I.
$$

Consequently, the relation scheme of the strict $3$-bit core admits an
algebraic condensation that isolates its relational sector as a separate
algebraic object.

**Proof.** For any $i,j\in\{1,2,3\}$, the matrix entry of
$A_{R_i}A_{R_j}$ counts the number of intermediate states $y$ through which
one can pass from $x$ to $z$, first along $R_i$ and then along $R_j$. By
Theorem 7.8.1 and the symmetry of the six-point carrier, this number depends
only on the class of the pair $(x,z)$, and therefore decomposes in the basis
$\{I,A_{$R_1$},A_{$R_2$},A_{$R_3$}\}$. Direct counting gives the stated
coefficients, and symmetry of the two-step schemes gives commutativity. $∎$

### Corollary 7.8.2 [D|C]. Invariance of the Transport Layer under Change of Presentation

Suppose a $Z_2$-transport with holonomy

$$
\mathrm{Hol}(\gamma_{\mathrm{prim}})\in\{\pm1\}
$$

is given on the fixed primitive cycle. Then every admissible presentation
symmetry from $\Gamma_3$ sends it to a gauge-equivalent transport class with
the same holonomy.

**Proof.** By Theorem 7.8.1, the cycle $\gamma_{\mathrm{prim}}$ is preserved
as a graph. An admissible symmetry only renames vertices and edges of the cycle;
if orientation is reversed, the product of signs around the cycle does not
change, since in the group $\{\pm1\}$ we have $\varepsilon^{-1}=\varepsilon$.
Therefore the gauge class and its holonomy are preserved. $∎$

### Remark 7.8.3. What Exactly Is Closed Here

Theorem 7.8.1 does not claim absolute independence from all possible
realizations of an abstract six-vertex object. The following is established:

- inside the class of admissible presentation symmetries specified by the group
  $\Gamma_3$, all constructions are equivalent;
- therefore the core does not depend on coordinate permutation and global complement.

### Theorem 7.8.4 [D|C]. Full Color-Preserving Automorphism Group of the Relation Scheme

Let

$$
\mathrm{Aut}_{\mathrm{rel}}(X_{\\mathrm{adm}})
$$

denote the group of all permutations of the set $X_{\mathrm{adm}}$ preserving
the relations

$$
R_0,$R_1, R_2, R_3$.
$$

Then

$$
\mathrm{Aut}_{\mathrm{rel}}(X_{\\mathrm{adm}})
\cong
\Gamma_3
\cong
S_3\times \mathbb Z_2^{\mathrm{glob}}.
$$

Moreover, the subgroup of automorphisms preserving each of the shells
$\mathcal C_1$ and $\mathcal C_2$ separately is isomorphic to $S_3$.

**Proof.**

1. The relation $R_2$ forms the graph

   $$
K_3\\sqcup K_3,
$$

   that is, exactly two connected components, each a triangle. Therefore any
   automorphism of the relation scheme either preserves both components
   separately or swaps them.
2. The relation $R_3$ forms a perfect matching between these two triangles.
   Hence after choosing the action on one triangle, the action on the other is
   already uniquely determined by the requirement that $R_3$ be preserved.
3. Thus every color-preserving automorphism of the relation scheme is specified
   by:
   - a permutation of the three complementary axes;
   - and, possibly, a global exchange of the two triangles.

   Therefore

   $$
|\mathrm{Aut}_{\mathrm{rel}}(X_{\\mathrm{adm}})|
   \le 2\cdot 3! = 12.
$$

4. Conversely, all elements of $\Gamma_3$ from Definition 7.8 preserve Hamming
   distance, and hence preserve all relations $R_0,$R_1$,$R_2$,R_3$. Therefore

   $$
\Gamma_3 \subseteq \mathrm{Aut}_{\mathrm{rel}}(X_{\\mathrm{adm}}).
$$

   Since $|\Gamma_3|=12$, the groups are equal.
5. If one additionally requires preserving the shells $\mathcal C_1$ and
   $\mathcal C_2$ separately, then the global exchange of the two triangles is
   prohibited, and only the permutation of the three axes remains, that is, a
   subgroup of order $3!$, isomorphic to $S_3$. $∎$

### Corollary 7.8.5 [D|C]. Theorem 7.8.1 Exhausts the Whole Class of Relation-Preserving Symmetries

The group $\Gamma_3$, introduced in Definition 7.8, is not an artificially
chosen subset of symmetries of the relation scheme. It coincides with the full
group of color-preserving automorphisms of the strict $3$-bit core preserving
the relations

$$
R_0,$R_1, R_2, R_3$.
$$

Therefore Theorem 7.8.1 exhausts the largest possible class of symmetries
preserving the relations. The stronger claim that every admissible presentation
symmetry automatically preserves the relations $R_0,$R_1$,$R_2$,R_3$ is not made.


---

## 8. Extension of the Strict Core

The shell extension, categorical packaging, operator closure, and sections
$8$-$11$ are moved to the separate volume
`02B_DOT_Shell_Extension_And_Categorical_Packaging_EN.md`. The present file
contains sections $0$-$7$.


[A]: # (Status Marker)
[D]: # (Status Marker)
[C]: # (Status Marker)
[D|mod]: # (Status Marker)
[G1]: # (Status Marker)


[D|comb]: # (Status Marker)
[D|C]: # (Status Marker)
[D|graph]: # (Status Marker)
[Context]: # (Status Marker)
[Packaging]: # (Status Marker)
[D|cat]: # (Status Marker)
