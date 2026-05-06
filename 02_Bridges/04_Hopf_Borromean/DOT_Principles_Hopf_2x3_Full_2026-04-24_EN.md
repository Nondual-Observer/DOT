# Appendix C. Hopf/Borromean Bridge

Status: bridge document / protocol for topological preimages.

This document fixes the place of Möbius-, Hopf-, and Borromean-type readings relative to the strict finite core. The source is finite: $Q_3$, $X_{\mathrm{adm}}$, relations $R_1,R_2,R_3$, transport $T$, axial factorization, and exact axial presentations. Topological preimages receive a separate bridge status.

---

## C.0. Abstract and Document Route

The Hopf/Borromean bridge connects three finite structures of rank $3$ with three topological readings.

The first structure is an axial pair

$$
H_i=\{I_i^-,I_i^+\}.
$$

It gives a two-pole carrier of one axis. In the topological reading, such a pair may be matched with a pair of Hopf-linked circles, but only after a separate topological carrier and embedding have been specified.

The second structure is the half-return of transport

$$
T^3(I_i^\eta)=I_i^{-\eta}.
$$

It is a finite $Z_2$-holonomy on $X_{\mathrm{adm}}$. In the topological reading, this half-return corresponds to the motif of Möbius monodromy: one circuit changes the sign in a two-point fiber.

The third structure is the decomposition of the whole six-position carrier into three axial pairs:

$$
X_{\mathrm{adm}}=H_1\sqcup H_2\sqcup H_3.
$$

In the topological reading, this triple may be matched with a Borromean triad of blocks. This reading does not assert the presence of literal Borromean rings inside the finite core. It fixes only the schema: three blocks hold a common motif that is not reducible to one selected pair.

Document route:

$$
\text{strict rank-3 source}
\to
\text{axial pairs}
\to
\text{exact axial presentations}
\to
\text{finite }Z_2\text{-holonomy}
\to
\text{Hopf/Möbius/Borromean readings}
\to
\text{status boundary}.
$$

Main boundary: $R_3=3K_2$, $T^3$, and $X_{\mathrm{adm}}\cong I_3\times\Sigma$ are objects of the strict finite core. The Möbius band, the Hopf link, and the Borromean link do not belong to that core. They become native objects only in a separate topological layer with specified carriers, embeddings, and invariants.

---

## C.1. Source Strict Layer

Rank $3$ defines the full carrier:

$$
Q_3=\mathbb F_2^3.
$$

Admissible carrier:

$$
X_{\mathrm{adm}}=Q_3\setminus\{000,111\}.
$$

On $X_{\mathrm{adm}}$, the Hamming relations are defined by:

$$
R_k=\{(x,y)\in X_{\mathrm{adm}}\times X_{\mathrm{adm}}:
x\neq y,\ d_H(x,y)=k\},
\qquad
k=1,2,3.
$$

Graph-readings:

$$
(X_{\mathrm{adm}},R_1)\cong C_6,
$$

$$
(X_{\mathrm{adm}},R_2)\cong K_3\sqcup K_3,
$$

$$
(X_{\mathrm{adm}},R_3)\cong 3K_2.
$$

Union relation:

$$
R_{12}=R_1\cup R_2,
\qquad
(X_{\mathrm{adm}},R_{12})\cong K_{2,2,2}.
$$

The strict source for the Hopf/Borromean bridge is the relation $R_3$ and axial factorization:

$$
X_{\mathrm{adm}}\cong I_3\times\Sigma,
\qquad
I_3=\{I_1,I_2,I_3\},
\qquad
\Sigma=\{-,+\}.
$$

---

## C.2. Axial Pairs

For $i\in\{1,2,3\}$:

$$
H_i=\{I_i^-,I_i^+\}\subset X_{\mathrm{adm}}.
$$

The three axial pairs decompose the carrier:

$$
X_{\mathrm{adm}}=H_1\sqcup H_2\sqcup H_3.
$$

The relation $R_3$ restricts to each pair as $K_2$:

$$
(H_i,R_3|_{H_i})\cong K_2.
$$

The whole $R_3$-structure:

$$
(X_{\mathrm{adm}},R_3)
\cong
H_1\sqcup H_2\sqcup H_3
\cong
3K_2.
$$

This is a native finite layer. The Hopf term adds no new strict object to this layer.

---

## C.3. Axial Presentations

For each axial pair, define a reading:

$$
\pi_i:H_i\to\{I_i\},
$$

$$
\pi_i(I_i^-)=I_i,
\qquad
\pi_i(I_i^+)=I_i.
$$

Recovery datum:

$$
\mathrm{rec}_i(I_i)
=
(H_i,R_3|_{H_i}).
$$

Axial presentation:

$$
\Pi_i^{\mathrm{ax},(3)}
=
(H_i,R_3|_{H_i},\pi_i,\mathrm{rec}_i).
$$

This presentation is exact: the unique fiber of the reading is $H_i$, and recovery returns that fiber together with the induced relation.

Conceptual formula of the strict layer:

$$
\text{one axial invariant}
\quad
\longmapsto
\quad
\text{two polar manifestations}.
$$

---

## C.4. Finite Holonomy

Transport $T$ on $X_{\mathrm{adm}}$ is constructed after choosing an orientation on the $C_6$-reading of the relation $R_1$:

$$
T:X_{\mathrm{adm}}\to X_{\mathrm{adm}},
\qquad
T^6=\mathrm{id}_{X_{\mathrm{adm}}}.
$$

Half-return:

$$
T^3(x)=x+111.
$$

In axial notation:

$$
T^3(I_i^\eta)=I_i^{-\eta}.
$$

Strict status:

$$
T^3
$$

is finite $Z_2$-holonomy on $X_{\mathrm{adm}}$.

Bridge-reading:

$$
T^3
\quad
\text{is read as}
\quad
\text{Möbius-type monodromy}.
$$

A literal Möbius band requires its own topological carrier:

$$
p:E\to S^1,
\qquad
p^{-1}(\theta)\cong\Sigma,
$$

with monodromy swap after one circuit. This carrier has bridge status.

---

## C.5. Hopf-Type Reading

For each strict axial pair:

$$
H_i=\{I_i^-,I_i^+\},
$$

the bridge-target is a two-component topological pair:

$$
\mathcal H_i=(L_i^-,L_i^+),
$$

where $L_i^-$ and $L_i^+$ are oriented closed curves in an ambient $3$-manifold, for example in $S^3$.

Literal Hopf condition:

$$
\mathrm{lk}(L_i^-,L_i^+)=\pm1.
$$

Bridge-handoff:

$$
I_i^-\mapsto L_i^-,
\qquad
I_i^+\mapsto L_i^+,
$$

$$
R_3|_{H_i}
\quad
\mapsto
\quad
\text{linked two-component relation}.
$$

Status:

$$
(H_i,R_3|_{H_i})\cong K_2
$$

is native strict data.

$$
\mathcal H_i
$$

is Hopf-target data after an embedding model has been specified.

Hopf-type reading is defined by the bridge formula:

$$
\text{one axial invariant in two polar manifestations}
\quad
\leadsto
\quad
\text{two linked boundary components}.
$$

---

## C.6. Borromean Block-Triad

Strict finite source:

$$
\mathcal B_3=\{H_1,H_2,H_3\}.
$$

Each $H_i$ is a two-point axial block. The triad of blocks is fixed after the factorization:

$$
X_{\mathrm{adm}}\cong I_3\times\Sigma.
$$

Borromean-type bridge reading:

$$
(H_1,H_2,H_3)
\quad
\leadsto
\quad
\text{three block-components held as one triadic dependency}.
$$

Literal Borromean rings consist of three topological components with nontrivial triple linking and trivial pairwise linking. The strict finite source defines different data:

$$
3\text{ axial blocks},
\qquad
2\text{ polar states in each block}.
$$

A compatible topological target has the block-level form:

$$
\mathcal L_{\mathrm{block}}
=
(\mathcal H_1,\mathcal H_2,\mathcal H_3),
$$

where each $\mathcal H_i$ may have Hopf-type structure.

Status:

$$
\mathcal B_3
$$

is native finite block data.

$$
\text{Borromean block-triad}
$$

has bridge-readable status.

$$
\text{literal six-component topological link}
$$

has not-yet status until explicit curves, ambient space, and linking invariants have been specified.

---

## C.7. Möbius, Hopf-Band, Hopf Pair

The three topological names have different roles.

Möbius avatar:

$$
\text{one circuit}
\quad
\mapsto
\quad
\text{fiber swap}.
$$

Strict source:

$$
T^3(I_i^\eta)=I_i^{-\eta}.
$$

Hopf-band avatar:

$$
\text{annular/twisted surface with two boundary components}.
$$

Bridge-role:

$$
I_i^-,
\ I_i^+
$$

are read as two boundary components of one axial block.

Hopf pair:

$$
\mathrm{lk}(L_i^-,L_i^+)=\pm1.
$$

Bridge-role:

$$
H_i
$$

is realised as a linked pair after an embedding has been specified.

Status discipline:

$$
\text{finite }Z_2\text{-holonomy}
$$

has native status.

$$
\text{Möbius/Hopf/Hopf-band}
$$

have bridge-target status.

---

## C.8. Legacy Labels

Earlier notes used the labels:

$$
D,\quad F,\quad C.
$$

In the current strict architecture, these labels are not native names of the axial carrier. The native carrier is:

$$
I_3=\{I_1,I_2,I_3\}.
$$

Diagrams may use a label map:

$$
\lambda:I_3\to\{D,F,C\}.
$$

Such a map has readable status. In proofs, it is used only after the target layer defines $D,F,C$ as its own carrier labels.

---

## C.9. Status Table

| Object / Claim | Strict Core Status | Hopf/Borromean Bridge Status |
|---|---:|---:|
| $X_{\mathrm{adm}}$ | native | source carrier |
| $R_3=3K_2$ | native | source relation for axial pairs |
| $H_i=\{I_i^-,I_i^+\}$ | native | source block |
| $\Pi_i^{\mathrm{ax},(3)}$ | native exact presentation | source presentation |
| $T^3(I_i^\eta)=I_i^{-\eta}$ | native finite holonomy | Möbius-readable monodromy |
| $p:E\to S^1$ with swap monodromy | outside strict core | Möbius bridge carrier |
| Hopf link $(L_i^-,L_i^+)$ | outside strict core | bridge target after embedding |
| $\mathrm{lk}(L_i^-,L_i^+)=\pm1$ | outside strict core | topological verification |
| $(H_1,H_2,H_3)$ | native finite block triad | Borromean-readable source |
| literal six-component link | not-yet | requires explicit construction |
| physical interpretation | outside strict core | downstream interpretation |

---

## C.10. Necessary Figures

### Figure C1. $R_3=3K_2$

Show three disjoint $K_2$-pairs:

$$
H_1,\quad H_2,\quad H_3.
$$

Purpose: strict finite source for Hopf-type reading.

### Figure C2. Axial Factorization

Show:

$$
X_{\mathrm{adm}}\cong I_3\times\Sigma.
$$

Rows: $I_1,I_2,I_3$. Columns: $-,+$.

Purpose: show that a Hopf-type pair belongs to one axial invariant.

### Figure C3. Half-Return $T^3$

Show the $C_6$-cycle and the three antipodal jumps:

$$
I_i^-\leftrightarrow I_i^+.
$$

Purpose: finite $Z_2$-holonomy before Möbius reading.

### Figure C4. Möbius Target Schema

Show base circle $S^1$, two-point fiber $\Sigma$, and monodromy swap after one circuit.

Purpose: bridge carrier for Möbius-readable $T^3$.

### Figure C5. Hopf Pair per Axis

Show two linked curves $L_i^-,L_i^+$ with label:

$$
\mathrm{lk}=\pm1.
$$

Purpose: topological target of one axial pair.

### Figure C6. Borromean Block-Triad

Show three blocks:

$$
\mathcal H_1,\quad\mathcal H_2,\quad\mathcal H_3.
$$

Each block contains two polar components. The block-level dependency is shown separately from internal Hopf-pair linking.

Purpose: separate ordinary Borromean rings from $3$ two-component blocks.

### Figure C7. Status Boundary

Show:

$$
\text{strict finite core}
\to
\text{Möbius/Hopf bridge}
\to
\text{literal topological link model}.
$$

Purpose: preserve the boundary between finite relations and topological embedding.

---

## C.11. What Is Fixed

The Hopf/Borromean layer has correct bridge status.

Strict finite source:

$$
(X_{\mathrm{adm}},R_3)\cong 3K_2,
\qquad
X_{\mathrm{adm}}\cong I_3\times\Sigma.
$$

Exact axial presentations:

$$
\Pi_i^{\mathrm{ax},(3)}
=
(H_i,R_3|_{H_i},\pi_i,\mathrm{rec}_i).
$$

Finite holonomy:

$$
T^3(I_i^\eta)=I_i^{-\eta}.
$$

Bridge readings:

$$
T^3
\leadsto
\text{Möbius-type monodromy},
$$

$$
H_i
\leadsto
\text{Hopf-type axial pair},
$$

$$
(H_1,H_2,H_3)
\leadsto
\text{Borromean block-triad}.
$$

Literal topological models require explicit carriers, embeddings, and linking invariants. Until these data are specified, they remain outside the strict finite core.
