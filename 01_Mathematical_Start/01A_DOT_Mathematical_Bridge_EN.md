# DOT: Mathematical Bridge to the Strict Core

## 0. Document Status

This file is a transition from the main manuscript
`../00_Theory/DOT_main_EN.md` to the proof volume
`02A_DOT_Core_Foundation_And_Theorems_EN.md`.

The main manuscript defines the general language of DOT: presentations, finite
carriers, relations, readings, recoveries, ranks, and the general growth law.
Volume `02A` isolates one layer of this construction: the strict finite block of
rank \(3\).

The purpose of the present document is to show which data from the main
manuscript are needed to enter `02A`, and why the proof block `02A` begins with
the carrier

\[
X_{\mathrm{adm}}=Q_3\setminus\{000,111\}.
\]

This document introduces no new DOT objects. All objects used below are either
already constructed in the main manuscript or proved in detail in `02A`.

## 1. Source Formal Unit

The main manuscript begins the strict part with a presentation, that is, a
**presentation of structure**. A finite object is not specified by a set alone,
but together with a relation, a chosen reading, and recovery data. This form is
needed in order to distinguish the carrier itself, the graph relation on it, and
what remains after the reading.

A presentation of structure has four components:

\[
(X,R,q,\operatorname{rec}).
\]

Here:

- \(X\) is a finite carrier;
- \(R\subseteq X\times X\) is a relation on the carrier;
- \(q:X\to Y\) is a reading;
- \(\operatorname{rec}\) is recovery data over the fibers of the reading.

This form fixes the rule that a name in the strict core receives status only
after specifying its carrier, relation, reading, and recovery, or after an
explicitly specified operator status.

Therefore the transition to `02A` is not a transition to a new metaphor. It is a
transition to a concrete finite presentation of structure of rank \(3\).

## 2. Ranks as Binary Carriers

Rank specifies the level of coordinate complexity. Rank \(n\) means that a state
is written with \(n\) binary coordinates. Thus each next rank adds one new bit,
and already constructed states receive a new position inside a larger carrier.

The full coordinate carrier of rank \(n\):

\[
Q_n=\mathbb F_2^n.
\]

The nonzero layer:

\[
Q_n^*=Q_n\setminus\{0^n\}.
\]

The full nontrivial layer without the two total poles:

\[
U_n=Q_n\setminus\{0^n,1^n\}.
\]

The weight-\(k\) shell:

\[
S_k^{(n)}=\{x\in Q_n: |x|=k\},
\]

where \(|x|\) is the Hamming weight, i.e. the number of ones in the bit string.

Relations in rank blocks are defined through Hamming distance:

\[
d_H(x,y)=k.
\]

This notation is used in the main manuscript and in `02A`.

## 3. Rank \(1\): The Polar Pair

Rank \(1\) defines the first finite carrier:

\[
Q_1=\mathbb F_2=\{0,1\}.
\]

At this level the minimal polar pair appears. The only nontrivial symmetry of
this pair is an involution:

\[
\tau^2=\operatorname{id}.
\]

For the transition to `02A`, the important point is this: the first rank fixes
the binary form of distinction. Each subsequent coordinate repeats this form as
a new independent bit.

## 4. Rank \(2\): The First Comparison Carrier

Rank \(2\) has the carrier

\[
Q_2=\mathbb F_2^2=\{00,01,10,11\}.
\]

Different graph readings are built on the same four-point carrier:

\[
C_4,
\qquad
2K_2,
\qquad
K_4,
\qquad
K_4-e.
\]

Their role is to prepare the reader for the main DOT rule: one carrier may have
several different relations and several different readings. Therefore a graph
name does not replace the carrier; it points to the chosen relation layer.

In rank \(2\), the total poles are also isolated:

\[
00,\qquad 11.
\]

Removing them leaves a two-point layer:

\[
Q_2\setminus\{00,11\}=\{01,10\}.
\]

This simple puncture pattern prepares the analogous, now six-point, transition
in rank \(3\).

## 5. Transition to Rank \(3\)

The full carrier of rank \(3\):

\[
Q_3=\mathbb F_2^3.
\]

It contains eight states:

\[
000,001,010,011,100,101,110,111.
\]

It has two total poles:

\[
0^3=000,
\qquad
1^3=111.
\]

The strict active carrier of rank \(3\) is obtained by removing these two poles:

\[
X_{\mathrm{adm}}
=
Q_3\setminus\{000,111\}.
\]

Therefore,

\[
X_{\mathrm{adm}}
=
\{001,010,011,100,101,110\}.
\]

This is the main carrier of `02A`. Its cardinality is \(6\).

It is important to distinguish two objects:

- \(Q_3\) is the full coordinate carrier and, later, the chamber layer;
- \(X_{\mathrm{adm}}\) is the six-point active carrier on which the relations
  \(R_1,R_2,R_3\) are built.

## 6. Shells of Rank \(3\)

In \(Q_3\), states are distributed by weight:

\[
S_0^{(3)}=\{000\},
\]

\[
S_1^{(3)}=\{001,010,100\},
\]

\[
S_2^{(3)}=\{011,101,110\},
\]

\[
S_3^{(3)}=\{111\}.
\]

After removing \(000\) and \(111\), one obtains

\[
X_{\mathrm{adm}}=S_1^{(3)}\sqcup S_2^{(3)}.
\]

This is exactly what makes rank \(3\) special: the active carrier coincides with
the outer shell

\[
V_3=S_1^{(3)}\sqcup S_2^{(3)}.
\]

In higher ranks, the full nontrivial layer \(U_n\) and the outer shell \(V_n\)
are different. In rank \(3\), they coincide:

\[
U_3=V_3=X_{\mathrm{adm}}.
\]

This feature explains why `02A` can build the whole strict core of rank \(3\) on
one six-point carrier.

## 7. The Three Relations on \(X_{\mathrm{adm}}\)

After choosing the six-point carrier, one specifies which pairs of its points are
considered linked. In rank \(3\), the natural grammar of relations is given by
Hamming distance: two points are compared by the number of coordinates in which
they differ.

On \(X_{\mathrm{adm}}\), introduce three relations:

\[
R_1=\{(x,y):x\neq y,\ d_H(x,y)=1\},
\]

\[
R_2=\{(x,y):x\neq y,\ d_H(x,y)=2\},
\]

\[
R_3=\{(x,y):x\neq y,\ d_H(x,y)=3\}.
\]

In graph reading they give:

\[
(X_{\mathrm{adm}},R_1)\cong C_6,
\]

\[
(X_{\mathrm{adm}},R_2)\cong K_3\sqcup K_3,
\]

\[
(X_{\mathrm{adm}},R_3)\cong 3K_2.
\]

Conceptually:

- \(R_1\) defines a six-cycle of one-step transitions;
- \(R_2\) splits the carrier into two triples of equal weight;
- \(R_3\) defines three complementary pairs.

These three relations decompose all unordered pairs of distinct points of
\(X_{\mathrm{adm}}\).

## 8. Octahedral Reading

The union relation:

\[
R_{12}=R_1\cup R_2
\]

gives the graph

\[
(X_{\mathrm{adm}},R_{12})
\cong
K_{2,2,2}.
\]

The graph \(K_{2,2,2}\) is the \(1\)-skeleton of the octahedron:

\[
K_{2,2,2}\cong O_3^{(1)}.
\]

The octahedron is not introduced here as source geometry. It is a graph reading
of the already constructed relation \(R_{12}\) on the six-point carrier
\(X_{\mathrm{adm}}\).

## 9. Chambers and the Full Carrier \(Q_3\)

The octahedron has \(8\) chambers. Each chamber chooses one vertex from each of
the three complementary pairs. Therefore the set of chambers has cardinality

\[
2^3=8.
\]

In `02A`, one proves the bijection

\[
\operatorname{Cham}(O_3)\cong Q_3.
\]

Thus the full \(Q_3\), from which \(X_{\mathrm{adm}}\) was obtained, returns as
the chamber layer of the octahedral reading.

This is not a contradiction. In rank \(3\), the same \(Q_3\) plays two different
roles:

- first it is the full coordinate carrier;
- after the octahedral layer is constructed, it is read as the chamber carrier.

## 10. Incidence and Transport

After constructing the octahedral reading, `02A` introduces incidence between
the vertices of the octahedron and its chambers:

\[
\operatorname{Inc}_O\subset V_O\times C_O.
\]

This incidence defines a matrix \(B\) and allows the adjacencies on both sides,
vertices and chambers, to be recovered.

Then one chooses an orientation of the cycle \(C_6\) defined by the relation
\(R_1\). After choosing an orientation, one obtains a cyclic transport operator:

\[
T:X_{\mathrm{adm}}\to X_{\mathrm{adm}},
\]

\[
T^6=\operatorname{id}.
\]

Transport is built not on all of \(K_{2,2,2}\), but on the chosen cycle \(C_6\).
This distinction matters: octahedral reading and cyclic transport use the same
carrier, but different relations.

## 11. What Exactly `02A` Proves

The volume `02A_DOT_Core_Foundation_And_Theorems_EN.md` unfolds this bridge into
a proof block.

Its main parts are:

1. model background and object types;
2. construction of \(X_{\mathrm{adm}}\);
3. relations \(R_1,R_2,R_3\);
4. graph readings \(C_6\), \(K_3\sqcup K_3\), \(3K_2\);
5. union relation \(R_{12}\) and octahedral reading \(K_{2,2,2}\);
6. chamber layer \(\operatorname{Cham}(O_3)\cong Q_3\);
7. incidence between vertices and chambers;
8. spectral checks;
9. cyclic \(Z_2\)-transport;
10. finite signature of the rank-\(3\) core.

In this sense, `01A` is the entry map, while `02A` gives the proofs.

## 12. Boundary of the Bridge

The present document does not treat:

- the full construction of rank \(4\);
- the compositional atlas of rank \(5\);
- the general growth law \(\Lambda_n\);
- colour, \(A_2/\mathfrak{sl}_3/\mathfrak{su}_3\), Hopf/Borromean, and spectral
  application bridges.

These layers are located in other parts of the package.

The boundary of `01A` is:

\[
\text{presentation and ranks }1,2
\longrightarrow
Q_3
\longrightarrow
X_{\mathrm{adm}}
\longrightarrow
(R_1,R_2,R_3)
\longrightarrow
02A.
\]

After this, the strict proof volume `02A` begins.
