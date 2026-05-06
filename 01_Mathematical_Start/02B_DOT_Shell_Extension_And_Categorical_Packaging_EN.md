# DOT: Shell Extension and Categorical-Operator Layer

This volume continues the strict finite core from
`02A_DOT_Core_Foundation_And_Theorems_EN.md`. The mathematical transition from
the architectural foundation `01` to the strict core is already unfolded
separately in `01A_DOT_Mathematical_Bridge_EN.md`; the present volume begins
only after that bridge and does not replace either `01A` or `02A`.

In the current package, this file has the status of a shell-operator extension
of rank \(3\), not a complete construction of ranks \(4\) and \(5\). The full
finite atlas of rank \(4\), the compositional atlas of rank \(5\), and the
general growth laws are moved to the main manuscript
`../00_Theory/DOT_main_EN.md`. Here \(V_n\) denotes the external layer
\(S_1^{(n)}\sqcup S_{n-1}^{(n)}\), while \(X_{\mathrm{adm}}\) remains reserved
for rank \(3\) only.

This volume considers the shell extension, categorical formulations of finite
objects, the operator layer, and the boundaries of applicability of the
statements.

## 8. Correct \(4D\)-Extension

The section contains three successively superposed layers:

- shell extension;
- categorical formulations;
- operator closure.

Section \(8\) extends Sections \(1{-}7\) to the higher shell, categorical, and
operator layer.

### 8.0.A. Structure of Section \(8\)

Reading order:

1. **Shell extension** is considered in \(8.0-8.7\).
   Here we construct:
   - the general shell law;
   - the higher residual carrier;
   - the chamber layer;
   - the reduction \(4D \to 3D\);
   - the geometric picture of section and projection.

2. **Categorical formulations** are considered in \(8.8-8.14.B\).
   Here we construct:
   - path categories;
   - reduction functors;
   - incidence as a span and a profunctor;
   - the square embedding of the two-bit layer;
   - object and arrow types;
   - a short categorical summary.

3. **Operator closure** is considered in \(8.15-8.28.5\).
   Here we construct:
   - aperture projectors;
   - the \(\mathfrak{sl}_2\)-layer;
   - the enhanced aperture algebra;
   - the exact closure back into the strict \(3\)-bit core at \(n=3\).

In compressed form, the structure of the section is:

```text
    $$
    V_n / U_n, O_n, \operatorname{Cham}(O_n)
    $$
    $$
    \to \text{reduction } n \to n-1
    $$
-> \text{categorical formulations}
-> \text{operator layer}
-> \text{exact closure in } n=3.
```

The section introduces no new core and does not reduce all material to one
graph. Its task is the correct extension of the already constructed finite core.

The transition from the \(4D\)-layer to the \(3D\)-package of DOT is fixed with
two restrictions:

1. without mixing different vertex sets;
2. with two separate steps fixed instead of a single bijection

$$
V_4 \to V(Q_3).
$$

The proof form of the transition is given by the composition of two different
fixed steps:

$$
G_4 \rightsquigarrow K_{2,2,2} \cong O_3^{(1)},
\qquad
\operatorname{Cham}(O_3) \cong Q_3.
$$

### Proof Plan 8.0

The proof is built in five steps.

1. Fix the external \(4\)-dimensional layer

   $$
   V_4=S_1^{(4)}\sqcup S_3^{(4)}
   $$

   and do not mix it with the full cube \(\{0,1\}^4\) or with the future
   \(6\)-vertex reduction.

2. Show that the residual graph on \(V_4\) is

   $$
   K_{2,2,2,2}.
   $$

3. Delete one complementary pair and prove that the induced subgraph is

   $$
   K_{2,2,2}.
   $$

4. Identify this graph with the standard \(1\)-skeleton of the octahedron.

5. Independently of the graph reduction, use the already constructed bijection

   $$
   \operatorname{Cham}(O_3)\cong Q_3
   $$

   and conclude that the full \(4D \to 3D\) transition in DOT has a two-step,
   not one-step, nature.

### Definition 8.1 [C]. Higher External States

For \(n \ge 3\), set

$$
V_n := \{x \in \{0,1\}^n : w(x)=1 \text{ or } w(x)=n-1\}
      = S_1^{(n)}\sqcup S_{n-1}^{(n)}.
$$

In the \(4\)-dimensional case, fix the notation

$$
V_4 := S_1^{(4)}\sqcup S_3^{(4)}.
$$

This set contains exactly \(8\) vertices and only them. The full \(4\)-cube
\(\{0,1\}^4\) and any subsequent \(6\)-vertex reductions are treated as separate
objects and are not mixed with \(V_4\).

### Remark 8.1.1 [C]. Status of the Filter for \(n \ge 4\)

The filter

$$
w(x)\in\{1,n-1\}
$$

for \(n \ge 4\) is an accepted postulate [C], not a logical consequence of the
\(3\)-dimensional case. This filter preserves the cross-polytope skeleton and
complementary pairing. Other filters would produce other graph families.

### Definition 8.1.2 [D|comb]. Hamming Shell Ladder

For each \(n\ge 1\) and each \(k\in\{0,1,\dots,n\}\), set

$$
S_k^{(n)}:=\{x\in\{0,1\}^n:w(x)=k\}.
$$

Then the full Boolean cube decomposes into the disjoint sum of shells

$$
\{0,1\}^n=\bigsqcup_{k=0}^n S_k^{(n)},
\qquad
|S_k^{(n)}|=\binom{n}{k}.
$$

The normalized height of a shell is

$$
\alpha_k:=\frac{k}{n}.
$$

### Proposition 8.1.3 [D|comb]. Complementary Symmetry of Shells

The bitwise complement gives a bijection

$$
\overline{\phantom{x}}:S_k^{(n)}\xrightarrow{\cong} S_{n-k}^{(n)}.
$$

Consequently, the natural pairs in the shell ladder are

$$
\frac{k}{n}\longleftrightarrow \frac{n-k}{n}.
$$

In particular, for even \(n\) the middle shell

$$
S_{n/2}^{(n)}
$$

is self-paired and requires separate treatment.

**Proof.** If \(w(x)=k\), then the word \(x\) has exactly \(k\) ones and
\(n-k\) zeros. After complement, ones and zeros are exchanged, so
\(w(\bar x)=n-k\). Moreover,
$$
\overline{\bar x}=x,
$$
that is, complement is indeed an involution and therefore pairs the shells
$$
S_k^{(n)}\longleftrightarrow S_{n-k}^{(n)}.
$$
\(∎\)

### Corollary 8.1.4 [D|comb]. Shell Picture for \(n=4\)

For the \(4\)-cube we have the decomposition

$$
\{0,1\}^4=S_0^{(4)}\sqcup S_1^{(4)}\sqcup S_2^{(4)}\sqcup S_3^{(4)}\sqcup S_4^{(4)}
$$

with cardinalities

$$
1, \ 4, \ 6, \ 4, \ 1.
$$

This yields three different combinatorial entities:

1. the external cross-polytope layer

   $$
   V_4=S_1^{(4)}\sqcup S_3^{(4)},
   \qquad |V_4|=8;
   $$

2. the equatorial shell

   $$
   S_2^{(4)},
   \qquad |S_2^{(4)}|=6;
   $$

3. the full nontrivial package

   $$
   U_4:=S_1^{(4)}\sqcup S_2^{(4)}\sqcup S_3^{(4)},
   \qquad |U_4|=14.
   $$

**Proof.** This is a direct binomial count. \(∎\)

Theorem 8.5 on the correct transition \(4D \to 3D\) uses only the external layer

$$
V_4=S_1^{(4)}\sqcup S_3^{(4)}.
$$

The equatorial shell \(S_2^{(4)}\) and the extended package \(U_4\) are correct
as combinatorial objects in their own right, but they do not enter the current
strict carrier. Therefore the number \(14\) in \(4D\) does not contradict the
number \(8\): it is simply another, broader level of the shell ladder.

### Definition 8.1.6 [C]. Strict Carrier and Extended Shell Package in Dimension \(n\)

For each \(n\ge 3\), define two structurally different objects:

1. the strict external carrier

   $$
   V_n:=S_1^{(n)}\sqcup S_{n-1}^{(n)};
   $$

2. the extended nontrivial shell package

   $$
   U_n:=\bigsqcup_{k=1}^{n-1} S_k^{(n)}=\{0,1\}^n\setminus\{0^n,1^n\}.
   $$

The object \(V_n\) is intended for the strict cross-polytope carrier, while
\(U_n\) is intended for the broader shell extension.

### Remark 8.1.6a [C]. Unified Ladder of Shell Filtration

After introducing \(U_n\) and \(V_n\), it is useful to keep explicit the unified
two-step filtration of the full cube:

$$
Q_n=\{0,1\}^n
\longrightarrow
U_n=Q_n\setminus\{0^n,1^n\}
\longrightarrow
V_n=S_1^{(n)}\sqcup S_{n-1}^{(n)}.
$$

The first step deletes the two poles of the full carrier and opens the full
nontrivial shell package. The second step selects from it the strict external
layer preserving the cross-polytope structure.

Therefore in the general case one must strictly distinguish:

- the full cubic carrier \(Q_n\);
- the full nontrivial package \(U_n\);
- the strict external layer \(V_n\).

### Theorem 8.1.7 [D|C|comb]. General \(n\)-Dimensional Law of Shell Assembly


For each \(n\ge 3\), the following statements hold.

1. The strict carrier has cardinality

$$
|V_n| = \binom{n}{1} + \binom{n}{n-1} = 2n.
$$

2. The extended shell package has cardinality

$$
|U_n| = \sum_{k=1}^{n-1} \binom{n}{k} = 2^n - 2.
$$

3. On \(V_n\), the bitwise complement partitions the vertices into exactly \(n\)
   complementary pairs, and the residual graph on \(V_n\) is

   $$
   K_{2,2,\dots,2}
   $$

   with \(n\) parts.

4. For even \(n\), the middle shell

   $$
   S_{n/2}^{(n)}
   $$

   enters \(U_n\), but does not enter \(V_n\).

Consequently, the external cross-polytope carrier and the full nontrivial shell
package form two different but compatible lines of DOT development.

**Proof.**

1. The first formula is a binomial count.
2. The second formula is the sum of all binomial coefficients without the two extreme terms.
3. On \(S_1^{(n)}\sqcup S_{n-1}^{(n)}\), complement pairs vertices of weight
   \(1\) and \(n-1\). There are exactly \(n\) such pairs, and residual adjacency
   forbids only complementary pairs; hence one obtains the complete
   \(n\)-partite graph with parts of size \(2\).
4. For even \(n\), \(n/2 \notin \{1,n-1\}\) for \(n\ge 4\), so the middle shell
   does not enter the external carrier, but by definition enters \(U_n\). \(∎\)

### Corollary 8.1.8 [D|C]. Place of the Strict \(4D\to3D\) Transition in the General Law

Theorem 8.5 is the special case of the general law 8.1.7 at \(n=4\), where

$$
V_4=S_1^{(4)}\sqcup S_3^{(4)},
\qquad
U_4=S_1^{(4)}\sqcup S_2^{(4)}\sqcup S_3^{(4)}.
$$

It uses only the external carrier \(V_4\) and does not require including the
middle shell \(S_2^{(4)}\).

A later unified representation theory and continuous interpretation of these
objects is not part of this section. Here only the finite shell-graph part is
fixed.

### Proposition 8.2 [D|C]. Higher Residual Carrier

The residual complement graph on \(V_n\) is

$$
K_{2,2,\dots,2}
$$

with \(n\) parts. In particular, for \(n=4\) one obtains \(K_{2,2,2,2}\), that
is, the \(1\)-skeleton of the \(4\)-dimensional cross-polytope.

**Proof.** The vertices \(V_n\) split into \(n\) complementary pairs, and
residual adjacency connects all vertices from different pairs. \(∎\)

### Corollary 8.2.1 [D|C]. Spectrum of the \(4D\)-Residual Carrier

For \(V_4=S_1^{(4)}\sqcup S_3^{(4)}\), the residual graph has Laplacian spectrum

$$
\operatorname{Spec}(L_{K_{2,2,2,2}}) = \{0,6,6,6,6,8,8,8\}.
$$

**Proof.** This is the standard spectrum of the complete four-partite graph with
parts of size \(2\), or a special case of the general spectrum of a complete
multipartite graph. \(∎\)

### Definition 8.2.2 [C|geom]. General Chamber Layer of the Cross-Polytope

Let

$$
O_n := \{x \in \mathbb{R}^n : |x_1| + \dots + |x_n| \le 1\}
$$

be the standard \(n\)-dimensional cross-polytope. Its poles are
\(\pm e_1,\dots,\pm e_n\).

For each sign vector \(\sigma\in\{\pm1\}^n\), define the chamber

$$
T_\sigma := \{x \in O_n : \sigma_i x_i \ge 0 \text{ for all } i\}.
$$

Denote the set of chambers by

$$
\operatorname{Cham}(O_n).
$$

### Proposition 8.2.3 [D|graph]. Chamber Graph in Dimension \(n\)

The chambers of the cross-polytope \(O_n\) are naturally indexed by sign vectors
\(\sigma\in\{\pm1\}^n\), and their adjacency graph is isomorphic to the hypercube

$$
Q_n.
$$

**Proof.** For a fixed sign vector \(\sigma\), the conditions
$$
\sigma_i x_i\ge 0\qquad (i=1,\dots,n)
$$
select one chamber of the cross-polytope. Each such chamber is determined by
exactly one sign set, so indexing \(\operatorname{Cham}(O_n)\) by
\(\{\pm1\}^n\) is natural.

Now let \(\sigma,\tau\in\{\pm1\}^n\).

1. If they differ in exactly one coordinate, then the chambers agree on all
   other half-spaces and differ in only one sign. Their intersection has
   codimension \(1\), so the chambers are adjacent along a facet.
2. If they differ in at least two coordinates, then the intersection satisfies
   at least two independent equations of the form \(x_i=0\), and therefore has
   codimension at least two. Such an intersection is no longer a facet.

Thus chamber adjacency occurs if and only if the sign vectors differ in one
coordinate. This is precisely the adjacency rule of the hypercube \(Q_n\). \(∎\)

### Definition 8.2.4 [D|graph]. General Incidence Matrix \(B_n\)

Let the rows of \(B_n\) be indexed by the poles \(\pm e_i\), and the columns by
the chambers \(T_\sigma\). Set

$$
(B_n)_{v, \sigma} = 1 \iff v \in \partial T_\sigma.
$$

Equivalently, if the row corresponds to the pole with sign \(s\in\{\pm1\}\) on
axis \(i\), then

$$
(B_n)_{(i,s),\sigma} = 1 \iff \sigma_i = s.
$$

### Proposition 8.2.5 [D|graph]. Basic Identities for \(B_n\)

For the general incidence matrix, the following hold:

$$
B_n \mathbf{1}_{2^n} = 2^{n-1} \mathbf{1}_{2n}, \qquad B_n^\top \mathbf{1}_{2n} = n \, \mathbf{1}_{2^n},
$$

and

$$
B_n B_n^\top = 2^{n-1} I_{2n}+2^{n-2}A_{\mathrm{cross}}^{(n)},
$$

where \(A_{\mathrm{cross}}^{(n)}\) is the adjacency matrix of the graph
\(K_{2,2,\dots,2}\) on \(2n\) poles.

**Proof.** Let a row of \(B_n\) correspond to the pole \(s e_i\), where
\(s\in\{\pm1\}\).

1. The incidence condition has the form \(\sigma_i=s\). The remaining \(n-1\)
   signs are free, so the pole belongs to exactly
   $$
   2^{n-1}
   $$
   chambers. This gives
$$
B_n \mathbf{1}_{2^n} = 2^{n-1} \mathbf{1}_{2n}.
$$
2. Each chamber \(T_\sigma\) chooses exactly one pole on each axis, namely
   \(\sigma_i e_i\). Therefore each column of \(B_n\) contains exactly \(n\)
   ones, and
$$
B_n^\top \mathbf{1}_{2n} = n \, \mathbf{1}_{2^n}.
$$
3. The diagonal entry \((B_nB_n^\top)_{v,v}\) equals the number of chambers
   incident to pole \(v\), that is, \(2^{n-1}\).
4. Let \(v=s e_i\) and \(w=t e_j\) with \(i\neq j\). Then the incidence
   conditions are
   $$
   \sigma_i=s,\qquad \sigma_j=t.
   $$
   The remaining \(n-2\) coordinates are free, so the number of common chambers is
   $$
   2^{n-2}.
   $$
   Exactly such pairs form the edges of \(K_{2,2,\dots,2}\).
5. If \(w=-v\), then one would need simultaneously \(\sigma_i=s\) and
   \(\sigma_i=-s\), which is impossible. Therefore the corresponding entry for
   antipodal poles is zero.

Thus \(B_nB_n^\top\) has diagonal \(2^{n-1}\), value \(2^{n-2}\) on all
non-antipodal polar pairs, and zero on antipodal pairs. This is exactly
$$
2^{n-1} I_{2n} + 2^{n-2} A_{\mathrm{cross}}^{(n)}.
$$
\(∎\)

### Theorem 8.2.6 [D|graph]. General Block Spectrum of the Chamber Layer


Define the block adjacency matrix

$$
A_{\mathrm{block}}^{(n)} = \begin{pmatrix} A_{\mathrm{cross}}^{(n)} & B_n \\ B_n^\top & A_{Q_n} \end{pmatrix},
$$

and the block Laplacian

$$
L_{\mathrm{block}}^{(n)}:=D_{\mathrm{block}}^{(n)}-A_{\mathrm{block}}^{(n)}.
$$

Set

$$
\Delta_n := \sqrt{\bigl(2^{n-1}+n-4\bigr)^2+2^{n+1}}
$$

and

$$
\lambda_\pm^{(n)} := \frac{3n+2^{n-1} \pm \Delta_n}{2}.
$$

Then the spectrum of \(L_{\mathrm{block}}^{(n)}\) is the union of the following
multisets:

$$
\{0\}, \qquad \{n+2^{n-1}\},
$$

$$
\{\lambda_-^{(n)}\}^{\times n}, \qquad \{\lambda_+^{(n)}\}^{\times n},
$$

$$
\{n+2k\}^{\times \binom{n}{k}} \quad (k=2,\dots,n),
$$

$$
\{2n+2^{n-1}\}^{\times (n-1)}.
$$

Identical numerical values, if they occur, are combined by multiplicities.

**Proof.** The vertex space decomposes into a direct sum of invariant sectors.

1. On the constant sector we obtain the matrix

$$
\begin{pmatrix} 2^{n-1} & -2^{n-1} \\ -n & n \end{pmatrix},
$$

   whose eigenvalues are \(0\) and \(n+2^{n-1}\).

2. For each axis \(i\), the space generated by the antipodal pole difference
   \(d_i\) and the linear character \(\chi_i(\sigma)=\sigma_i\) is invariant.
   In this basis the Laplacian matrix is

$$
\begin{pmatrix} 2n-2+2^{n-1} & -2^{n-1} \\ -1 & n+2 \end{pmatrix},
$$

   so the eigenvalues are \(\lambda_-^{(n)}\) and \(\lambda_+^{(n)}\). This gives
   \(n\) multiplicities of each.

3. For Walsh characters of degree \(k\ge 2\), the matrix \(B_n\) vanishes, and
   the cube Laplacian gives values \(2k\). After adding the interlayer degree
   \(n\), we obtain eigenvalues \(n+2k\) with multiplicity \(\binom nk\).

4. On the subspace of vectors constant on each antipodal polar pair and having
   zero total sum, of dimension \(n-1\), the operator \(B_n^\top\) is zero, and
   \(A_{\mathrm{cross}}^{(n)}\) acts as \(-2\). Hence we obtain the eigenvalue
   \(2n+2^{n-1}\).

The sum of multiplicities is

$$
2+n+n+\sum_{k=2}^n \binom nk +(n-1)=2n+2^n,
$$

which is the dimension of the whole block space. The spectrum is exhausted. \(∎\)

### Corollary 8.2.7 [D|graph]. General Slow Mode and Dimension-Dependent Energy Ratio


Let

$$
E_-^{(n)} := \ker\bigl(L_{\mathrm{block}}^{(n)} - \lambda_-^{(n)}I\bigr).
$$

Then

$$
E_-^{(n)} = \operatorname{span}\bigl\{ d_i \oplus t_n \chi_i \;:\; i=1,\dots,n \bigr\},
$$

where

$$
t_n = \frac{2n-2+2^{n-1}-\lambda_-^{(n)}}{2^{n-1}} = \frac{1}{n+2-\lambda_-^{(n)}}.
$$

For every nonzero vector \(v=x\oplus y\in E_-^{(n)}\), the exact relation

$$
\frac{\|y\|^2}{\|x\|^2} = r_n, \qquad r_n := 2^{n-1} t_n^2 = \frac{2^{n-1}}{(n+2-\lambda_-^{(n)})^2}
$$

holds.

**Proof.** Every vector in \(E_-^{(n)}\) has the form
$$
v=\sum_{i=1}^n c_i\,(d_i\oplus t_n\chi_i)
=
\left(\sum_{i=1}^n c_i d_i\right)\oplus
\left(t_n\sum_{i=1}^n c_i\chi_i\right)
=x\oplus y.
$$
The vectors \(d_i\) are pairwise orthogonal and have norm \(2\), while the
characters \(\chi_i\) are pairwise orthogonal and have norm \(2^n\). Therefore
$$
\|x\|^2
=
\sum_{i=1}^n c_i^2\|d_i\|^2
=
2\sum_{i=1}^n c_i^2,
$$
and
$$
\|y\|^2
=
t_n^2\sum_{i=1}^n c_i^2\|\chi_i\|^2
=
t_n^2\,2^n\sum_{i=1}^n c_i^2.
$$
If \(v\neq 0\), then not all coefficients \(c_i\) are zero, and hence
$$
\frac{\|y\|^2}{\|x\|^2}
=
\frac{t_n^2\,2^n\sum c_i^2}{2\sum c_i^2}
=
2^{n-1}t_n^2
=
r_n.
$$
Constancy of the norm ratio on all of \(E_-^{(n)}\) is proved. \(∎\)

### Corollary 8.2.8 [D|graph]. Special Case \(n=3\)

For \(n=3\), we obtain

$$
\lambda_-^{(3)}=4,
\qquad
\lambda_+^{(3)}=9,
\qquad
r_3=4.
$$

Therefore the previous \(4:1\) law is an exact special case of the general
dimension-dependent law \(r_n:1\), not a universal constant for all dimensions.

### Theorem 8.2.9 [D|C|comb]. General Reduction of the External Carrier \(n\to n-1\)


Fix an axis \(k\in\{1,\dots,n\}\). Let

$$
p_k := e_k \in S_1^{(n)}, \qquad \bar{p}_k := \mathbf{1} - e_k \in S_{n-1}^{(n)}.
$$

Delete the complementary pair \(\{p_k,\bar p_k\}\) from \(V_n\) and denote

$$
V_n^{(k)} := V_n \setminus \{p_k, \bar{p}_k\}.
$$

Then forgetting the \(k\)-th coordinate gives a bijection

$$
\rho_k:V_n^{(k)}\xrightarrow{\cong} V_{n-1},
$$

with \((n-1)\) parts.

**Proof.** If \(x\in S_1^{(n)}\) and \(x\neq p_k\), then after deleting the
\(k\)-th coordinate we obtain a vector of weight \(1\) in \(\{0,1\}^{n-1}\). If
\(x\in S_{n-1}^{(n)}\) and \(x\neq \bar p_k\), then its only zero bit is not on
axis \(k\), so after deleting the \(k\)-th coordinate we obtain a vector of
weight \((n-2)=(n-1)-1\). Thus the image lies in

$$
V_{n-1} = S_1^{(n-1)} \sqcup S_{n-2}^{(n-1)}.
$$

Counting cardinalities gives

$$
|V_n^{(k)}| = 2n-2 = 2(n-1) = |V_{n-1}|.
$$

It remains to check injectivity. Suppose
$$
\rho_k(x)=\rho_k(y).
$$
Then all coordinates of \(x\) and \(y\), except the \(k\)-th, coincide. Since
\(x,y\in V_n^{(k)}\), each has weight either \(1\) or \(n-1\). If both have
weight \(1\), the unique one cannot stand on axis \(k\); otherwise deleting the
\(k\)-th coordinate would produce the zero vector, not lying in \(V_{n-1}\).
Hence in this case the \(k\)-th coordinates also coincide. If both have weight
\(n-1\), the same argument shows that their unique zero cannot stand on axis
\(k\), and again the \(k\)-th coordinates coincide. The mixed case is
impossible, because after deleting one coordinate the weights of the images
would differ by one and could not coincide.

Therefore \(x=y\), so \(\rho_k\) is injective. With equal cardinalities this
gives a bijection
$$
\rho_k:V_n^{(k)}\xrightarrow{\sim}V_{n-1}.
$$
The complementarity rule is preserved because deleting the same coordinate
commutes with bitwise complement on the remaining coordinates. Residual
adjacency is also preserved: two vertices differ in exactly two
non-complementary coordinates if and only if their images after deleting the
common fixed coordinate differ in the same two coordinates. \(∎\)

### Theorem 8.2.10 [D|graph]. General Reduction of the Chamber Layer \(n\to n-1\)


Fix the same axis \(k\). The map forgetting one sign

$$
\tau_k \colon \{\pm 1\}^n \to \{\pm 1\}^{n-1}, \qquad \tau_k(\sigma_1, \dots, \sigma_n) = (\sigma_1, \dots, \widehat{\sigma_k}, \dots, \sigma_n)
$$

defines a surjection

$$
\tau_k \colon \operatorname{Cham}(O_n) \twoheadrightarrow \operatorname{Cham}(O_{n-1})
$$

with fibers of size \(2\). If two chambers that differ only in the \(k\)-th
coordinate are identified, then the quotient chamber graph is naturally
isomorphic to

$$
Q_{n-1}.
$$

Equivalently, \(\tau_k\) is a cellular projection of cubic complexes

$$
\operatorname{Cham}(O_n)\cong[0,1]^n \longrightarrow [0,1]^{n-1}\cong \operatorname{Cham}(O_{n-1}),
$$

contracting pairs of faces that differ only in the \(k\)-th coordinate to a
single face of smaller dimension.

**Proof.** Each chamber of \(O_{n-1}\) is specified by signs on all axes except
the \(k\)-th, so it has exactly two preimages, corresponding to the choices
\(\sigma_k=\pm1\). Edges of the hypercube \(Q_n\) are of two types:

1. change of sign on axis \(k\), which collapses after factorization;
2. change of sign on another axis, which remains a change of exactly one bit in \(\{\pm1\}^{n-1}\).

Thus after contracting all edges of the first type, we obtain exactly
\(Q_{n-1}\). \(∎\)

### Theorem 8.2.11 [D|graph]. Descent of Incidence under Reduction \(n\to n-1\)


After choosing axis \(k\) and the corresponding maps \(\rho_k\) and \(\tau_k\),
the incidence matrix \(B_n\) descends to the matrix \(B_{n-1}\).

More precisely: if the two rows of \(B_n\) corresponding to the poles
\(\pm e_k\) are deleted, and the columns are grouped in pairs that differ only
by the sign \(\sigma_k\), then the resulting quotient matrix coincides with
\(B_{n-1}\) after the natural relabeling of axes.

**Proof.** For any pole \(\pm e_i\) with \(i\neq k\), incidence with a chamber
depends only on the sign \(\sigma_i\) and does not depend on \(\sigma_k\).
Therefore on each \(2\)-element \(\tau_k\)-fiber the values of the corresponding
row are constant. After grouping columns by these fibers and deleting the rows
of axis \(k\), we obtain the same formula as in Definition 8.2.4, now for the
\((n-1)\)-dimensional cross-polytope. \(∎\)

### Corollary 8.2.12 [D|C|graph]. General Two-Step Law of Dimension Reduction

$$
4D \to 3D
$$


After choosing one axis, the dimensional transition in the strict DOT body
always splits into two different steps:

$$
V_n \rightsquigarrow V_{n-1}, \qquad \operatorname{Cham}(O_n) \twoheadrightarrow \operatorname{Cham}(O_{n-1}).
$$

The first step is a graph reduction of the external carrier; the second is a
factorization of the chamber layer. Therefore the transition \(n\to n-1\) is
not specified by one bijection between vertices, but always has a two-level
nature.

### Corollary 8.2.13 [D|C]. Theorem 8.5 as the Case \(n=4\to 3\)

Theorem 8.5 is the special case of Corollary 8.2.12 at \(n=4\), where

$$
V_4\rightsquigarrow V_3\cong K_{2,2,2}\cong O_3^{(1)},
\qquad
\operatorname{Cham}(O_4)\twoheadrightarrow \operatorname{Cham}(O_3)\cong Q_3.
$$

In the special \(4D \to 3D\) description, Theorem 8.5 is formulated only on the
finite \(3D\)-package, so the second step is already written in its target form

$$
\operatorname{Cham}(O_3)\cong Q_3.
$$

### Lemma 8.3 [D|C]. Explicit Complementary Partition of \(V_4\)

The set

$$
V_4 = S_1^{(4)}\sqcup S_3^{(4)}
$$

splits into four complementary pairs:

$$
\{1000,0111\},\quad
\{0100,1011\},\quad
\{0010,1101\},\quad
\{0001,1110\}.
$$

**Proof.** Vectors of weights \(1\) and \(3\) pairwise complement each other to
\((1,1,1,1)\). There are exactly four such pairs. \(∎\)

### Lemma 8.4 [D|C]. Graph Reduction \(K_{2,2,2,2} \to K_{2,2,2}\)

If any one complementary pair is deleted from \(V_4\), then the induced subgraph
on the remaining six vertices is isomorphic to

$$
K_{2,2,2}.
$$

**Proof.** After deleting one pair, three complementary pairs remain. By the
definition of residual adjacency, there are no edges inside a pair, and all
possible edges are drawn between different pairs. This is exactly the definition
of \(K_{2,2,2}\). \(∎\)

### Theorem 8.5 [D|C]. Correct \(4D\to3D\) Transition in DOT


There exist two different fixed steps describing the transition from the
\(4D\)-layer to the \(3D\)-package of DOT.

1. Graph reduction:

   $$
   G_4 = K_{2,2,2,2} \rightsquigarrow K_{2,2,2}\cong O_3^{(1)}.
   $$

2. Independent cellular duality:

   $$
   \operatorname{Cham}(O_3)\cong Q_3.
   $$

Therefore the correct \(4D\to3D\) transition in DOT is not described by one
bijection

$$
V_4 \to V(Q_3),
$$

but by a composition of two different constructions:

$$
G_4 \rightsquigarrow O_3^{(1)},
\qquad
\operatorname{Cham}(O_3)\cong Q_3.
$$

**Proof.**

1. By Lemma 8.4, deleting one complementary pair from \(V_4\) sends the residual
   graph \(K_{2,2,2,2}\) to the induced subgraph
   $$
   K_{2,2,2},
   $$
   which by Theorem 4.2 is realized as the graph of the octahedral carrier
   \(O_3^{(1)}\).
2. By Corollary 4.4.1, the set of octahedral chambers is bijectively encoded by
   the vertices of the cube \(Q_3\):
   $$
   \operatorname{Cham}(O_3)\cong Q_3.
   $$
3. The first step concerns vertices of the residual graph and reduces the number
   of polar pairs from four to three. The second step concerns no longer the
   vertices of the residual graph, but another type of object: chambers of the
   octahedron.

Thus two different constructions really act here:
$$
G_4 \rightsquigarrow O_3^{(1)},
\qquad
\operatorname{Cham}(O_3)\cong Q_3.
$$
They are compatible with each other, but do not merge into one “universal”
bijection between vertices of \(V_4\) and vertices of \(Q_3\), because the
intermediate transition changes the type of object under consideration. \(∎\)

### Proposition 8.5.1 [D|C|model]. Explicit Coordinate Reduction after Choosing One Pair

Fix the complementary pair

$$
\{0001,1110\}\subset V_4.
$$

Let

$$
V_4' := V_4 \setminus \{0001,1110\}.
$$

Then projection to the first three coordinates

$$
\rho(x_1,x_2,x_3,x_4):=(x_1,x_2,x_3)
$$

defines a bijection

$$
\rho:V_4' \xrightarrow{\cong} P_3,
\qquad
P_3:=\{y\in\{0,1\}^3: w(y)\in\{1,2\}\}.
$$

Moreover, \(\rho\) is an isomorphism of residual graphs

$$
G_4[V_4'] \cong K_{2,2,2} \cong G_{\mathrm{res}}(P_3).
$$

**Proof.** The images of the six elements of \(V_4'\) under projection to the
first three coordinates are exactly

$$
\{001,010,011,100,101,110\}=P_3.
$$

Thus \(\rho\) is surjective onto \(P_3\). Injectivity also holds: if two vertices
from \(V_4'\) have the same first three coordinates, then they also agree in the
fourth coordinate, because in a binary word of length \(4\) the fourth bit is
completely determined by the condition of weight \(1\) or \(3\). Hence \(\rho\)
is a bijection.

Next, on \(V_4'\) the complementary pairs
$$
\{1000,0111\},\quad
\{0100,1011\},\quad
\{0010,1101\}
$$
are sent respectively to
$$
\{100,011\},\quad
\{010,101\},\quad
\{001,110\},
$$
that is, to the three complementary pairs of \(P_3\). Residual adjacency in both
\(V_4'\) and \(P_3\) connects all vertices from different complementary pairs
and connects no vertices inside one pair. Therefore \(\rho\) preserves both
vertices and the adjacency rule, hence is an isomorphism of residual graphs. \(∎\)

### Proposition 8.5.2 [D|C|model]. Explicit \(8\leftrightarrow 8\) Parametrization of Chambers

After the same choice of distinguished pair, the map

$$
\psi(x_1,x_2,x_3,x_4)
:=
\bigl((-1)^{x_1},(-1)^{x_2},(-1)^{x_3}\bigr)
$$

defines a bijection

$$
\psi:V_4 \xrightarrow{\cong} C_3,
\qquad
C_3:=\{\pm1\}^3.
$$

**Proof.** Suppose the first three coordinates
\((x_1,x_2,x_3)\in\{0,1\}^3\) are given. The requirement that \(x\) belong to
\(V_4=S_1^{(4)}\sqcup S_3^{(4)}\) means that the full word weight must be \(1\)
or \(3\). Therefore the fourth coordinate is recovered from the condition

$$
w(x)\in\{1,3\}.
$$

Equivalently,

$$
x_4 = 1-(x_1+x_2+x_3 \bmod 2).
$$

If the sum \(x_1+x_2+x_3\) is even, then the full weight must be odd, so
\(x_4=1\). If the sum is odd, then weight \(1\) or \(3\) requires \(x_4=0\).
Thus each binary triple corresponds to exactly one element of \(V_4\), and the
map
$$
\psi(x_1,x_2,x_3,x_4)=((-1)^{x_1},(-1)^{x_2},(-1)^{x_3})
$$
is bijective: its inverse first recovers the bits
$$
x_i = \frac{1-\sigma_i}{2} \qquad (i=1, 2, 3),
$$
and then recovers the fourth coordinate by the formula above. \(∎\)

### Proposition 8.5.3 [D|C|model]. Explicit Formula for the Incidence Matrix

In the coordinate encodings from Propositions 8.5.1 and 8.5.2, the incidence
matrix between poles and chambers is specified by the rule

$$
B_{v,\sigma}=1
\iff
\sigma_{k(v)}=(-1)^{v_{k(v)}},
$$

where \(k(v)\in\{1,2,3\}\) is the unique index of the minority bit of the vertex
\(v\in P_3\), that is, the unique coordinate on which the bit value differs from
the other two. Equivalently,

$$
v_{k(v)} \equiv w(v) \pmod 2.
$$

Equivalently: for each pole, exactly one sign on one axis is fixed, and the
signs on the other two axes are free. Therefore each row of \(B\) contains \(4\)
ones, each column contains \(3\) ones, and this is exactly the same incidence
matrix as in Definition 4.5.

**Proof.** In the encoding \(P_3\), each vertex has weight \(1\) or \(2\), and
therefore among its three bits there is exactly one minority bit. It is this bit
that specifies the working axis of the corresponding octahedral pole.

1. If \(v=100\), then \(w(v)=1\) and the minority bit is on axis \(1\). The
   condition gives

   $$
   \sigma_1=(-1)^1=-1,
   $$

   while \(\sigma_2,\sigma_3\) are free. We obtain \(4\) chambers of the form
   \((-1,\pm1,\pm1)\).

2. If \(v=011\), then \(w(v)=2\) and the minority bit is again on axis \(1\).
   The condition gives

   $$
   \sigma_1=(-1)^0=+1,
   $$

   while \(\sigma_2,\sigma_3\) are free. We obtain \(4\) chambers of the form
   \((+1,\pm1,\pm1)\).

The other vertices are analogous. Thus each pole is incident to exactly four
chambers, and the resulting matrix coincides with the fixed incidence matrix of
the octahedron. \(∎\)

### Remark 8.5.4 [D|C]. What Is Fixed in This Model and What Is Not

Fixed:

- the fact that deleting any one complementary pair gives \(K_{2,2,2}\);
- the fact that octahedral chambers are bijectively encoded by elements of \(\{\pm1\}^3\);
- the two-step structure of the transition from Theorem 8.5 itself.

Not fixed without an additional choice:

- which complementary pair is deleted;
- which coordinate is considered “hidden” in the formulas \(\rho\) and \(\psi\).

Therefore Propositions 8.5.1-8.5.3 are a strict coordinate model after a fixed
choice, while Theorem 8.5 remains the invariant form of the statement.

### Theorem 8.6 [D|geo]. Geometric Section/Projection Reduction of the Cross-Polytope


Fix an axis \(k\in\{1,\dots,n\}\) and denote

$$
H_k := \{x \in \mathbb{R}^n : x_k = 0\}.
$$

Let

$$
\iota_k \colon \mathbb{R}^{n-1} \to H_k \subset \mathbb{R}^n
$$

be the embedding inserting zero in place of the \(k\)-th coordinate, and let

$$
\pi_k \colon \mathbb{R}^n \to \mathbb{R}^{n-1}
$$

be the orthogonal projection forgetting the \(k\)-th coordinate. Then:

1. the section of the cross-polytope is given by

   $$
   O_n\cap H_k=\iota_k(O_{n-1});
   $$

2. the projection is surjective:

   $$
   \pi_k(O_n)=O_{n-1};
   $$

3. for every \(y\in O_{n-1}\), the preimage is the segment

   $$
   \pi_k^{-1}(y)\cap O_n
   =
   \{\iota_k(y)+t e_k:\ |t|\le 1-\|y\|_1\};
   $$

4. the vertices of the section are

   $$
   \{\pm e_i:\ i\neq k\},
   $$

   that is, exactly the poles of the \((n-1)\)-dimensional cross-polytope.

**Proof.** For a point \(x=(x_1,\dots,x_n)\in H_k\), the condition \(x\in O_n\)
is equivalent to

$$
\sum_{i\neq k}|x_i|\le 1,
$$

which gives the first statement. The second follows from the fact that for every
\(y\in O_{n-1}\), the point \(\iota_k(y)\) already lies in \(O_n\). The third
statement follows from the equality

$$
\|\iota_k(y) + t e_k\|_1 = \|y\|_1 + |t|.
$$

The fourth follows from the standard description of the vertices of \(O_n\) and
from the fact that the points \(\pm e_k\) do not lie in \(H_k\). \(∎\)

### Corollary 8.6.1 [D|geo]. Geometric Pairing of Chambers under Reduction

Let \(\sigma'\in\{\pm1\}^{n-1}\), and let \(\sigma^\pm\in\{\pm1\}^n\) be
obtained by inserting the sign \(\pm1\) in the \(k\)-th coordinate. Then

$$
T_{\sigma^+}^{(n)}\cap H_k
=
T_{\sigma^-}^{(n)}\cap H_k
=
\iota_k\bigl(T_{\sigma'}^{(n-1)}\bigr),
$$

and simultaneously

$$
\pi_k\bigl(T_{\sigma^+}^{(n)}\bigr)
=
\pi_k\bigl(T_{\sigma^-}^{(n)}\bigr)
=
T_{\sigma'}^{(n-1)}.
$$

Therefore the chambers of \(O_n\) are naturally grouped in pairs by the sign on
axis \(k\), and their section/projection image is the chambers of \(O_{n-1}\).

**Proof.** First consider the section. For a point \(x\in H_k\) we have
\(x_k=0\), so the inequality
$$
\sigma_k x_k\ge 0
$$
holds for both sign \(+1\) and sign \(-1\). The remaining conditions
$$
\sigma_i x_i\ge 0\qquad (i\neq k)
$$
coincide with the definition of the chamber \(T_{\sigma'}^{(n-1)}\) after the
embedding \(\iota_k\). Hence
$$
T_{\sigma^+}^{(n)}\cap H_k
=
T_{\sigma^-}^{(n)}\cap H_k
=
\iota_k\bigl(T_{\sigma'}^{(n-1)}\bigr).
$$

Now consider the projection. If \(x\in T_{\sigma^\pm}^{(n)}\), then after
deleting the \(k\)-th coordinate the remaining inequalities are
$$
\sigma_i x_i\ge 0\qquad (i\neq k),
$$
that is,
$$
\pi_k(x)\in T_{\sigma'}^{(n-1)}.
$$
Conversely, for every \(y\in T_{\sigma'}^{(n-1)}\), the point \(\iota_k(y)\)
lies in both \(T_{\sigma^+}^{(n)}\) and \(T_{\sigma^-}^{(n)}\), and its
projection equals \(y\). Hence
$$
\pi_k\bigl(T_{\sigma^+}^{(n)}\bigr)
=
\pi_k\bigl(T_{\sigma^-}^{(n)}\bigr)
=
T_{\sigma'}^{(n-1)}.
$$
Thus pairs of chambers differing only by the sign on axis \(k\) indeed have a
common section/projection image. \(∎\)

### Corollary 8.6.2 [D|geo]. Geometric Descent of Incidence

After deleting the poles \(\pm e_k\) and pairwise identifying chambers that
differ only by the sign on axis \(k\), the pole-chamber incidence of \(O_n\)
passes to the incidence of \(O_{n-1}\). At the matrix level this is the same
descent

$$
B_n \rightsquigarrow B_{n-1},
$$

already proved combinatorially in Theorem 8.2.11.

**Proof.** A pole \(\pm e_i\) with \(i\neq k\) belongs to a chamber if and only
if the sign on axis \(i\) agrees; the sign on axis \(k\) plays no role.
Therefore after geometric pairing of chambers along the \(k\)-th coordinate, we
obtain exactly the same incidence as in dimension \((n-1)\). \(∎\)

### Corollary 8.6.3 [D|geo]. Strong Geometric Reduction \(4D \to 3D\)

For \(n=4\) and the choice of axis \(k=4\), we have:

1. the \(16\)-cell

   $$
   O_4=\{x\in\mathbb R^4:\ |x_1|+|x_2|+|x_3|+|x_4|\le 1\}
   $$

   intersects the hyperplane \(x_4=0\) in the standard octahedron \(O_3\);

2. its \(16\) sign chambers collapse pairwise by the sign of \(x_4\) into the
   \(8\) chambers of the octahedron;

3. pole-chamber incidence descends exactly to the matrix \(B\) of the
   three-dimensional body.

Therefore the strong geometric story \(4D \to 3D\) in the strict body of DOT is
closed as a section/projection reduction of the \(16\)-cell to the octahedron
with its \(8\)-chamber package.

### Remark 8.7 [D|geo]. What Exactly Is Proved and What Is Not Claimed

Proved:

- the geometric section \(O_n\cap H_k\cong O_{n-1}\);
- the projection \(\pi_k:O_n\twoheadrightarrow O_{n-1}\);
- pairwise pairing of chambers;
- geometric descent of incidence.

Not claimed:

- a bijection between vertices of \(V_n\) and vertices of \(Q_{n-1}\);
- any direct geometric morphism from the full Boolean cube \(\{0,1\}^n\) to the
  polyhedral package of the cross-polytope;
- replacement of the two-step structure by one “magical” map.

Moreover:

- the poles \(\pm e_k\) deleted in the graph reduction are sent by the geometric
  projection \(\pi_k\) to the origin \(0\in\mathbb R^{n-1}\), that is, to the
  center of the cross-polytope \(O_{n-1}\), not to its vertices;
- therefore the geometric projection of the ambient polyhedron and the graph
  reduction of the external carrier are conjugate but structurally different
  operations.

### Definition 8.8 [D|cat]. Path Category of a Graph

For any finite undirected graph \(G\), denote by

$$
\operatorname{Path}(G)
$$

its path category.

- objects: vertices of the graph;
- morphisms \(x\to y\): finite oriented paths from \(x\) to \(y\);
- composition: concatenation of paths;
- identities: empty paths.

This is the free category on the directed graph obtained by replacing each edge
with two oppositely directed arrows.

### Theorem 8.8.1 [D|cat]. Universal Property of the Path Category

Let \(\vec G\) be the directed graph obtained from an undirected graph \(G\) by
doubling edges. Then \(\operatorname{Path}(G)\) is the free category on
\(\vec G\) in the following sense:

if \(\mathcal D\) is any category and \(\eta\) assigns vertices of \(\vec G\)
to objects of \(\mathcal D\), and oriented edges of \(\vec G\) to morphisms of
\(\mathcal D\), compatibly with sources and targets, then there exists a unique
functor

$$
\widetilde{\eta} \colon \operatorname{Path}(G) \to \mathcal{D}
$$

extending \(\eta\).

**Proof.** Every morphism in \(\operatorname{Path}(G)\) is a finite
concatenation of generating oriented edges. Therefore the image of such a path
must be the composition of the images of its edges, which determines the functor
uniquely. Correctness follows from associativity of composition in
\(\mathcal D\). \(\square\)

### Definition 8.9 [D|cat]. Minimal Categories of the Strict Body

For each \(n\ge 3\), define:

1. the category of the external carrier

   $$
   \mathcal{R}_n:=\operatorname{Path}\bigl(G_{\mathrm{res}}(V_n)\bigr);
   $$

2. the category of chambers

   $$
   \mathcal{C}_n:=\operatorname{Path}\bigl(\operatorname{Cham}(O_n)\bigr);
   $$

3. the category of the block carrier

   $$
   \mathcal{B}_n:=\operatorname{Path}\bigl(A_{\mathrm{block}}^{(n)}\bigr).
   $$

### Proposition 8.10 [D|cat]. General Chamber Functor of Sign-Bit Encoding

The map

$$
\Phi_n(\sigma_1,\dots,\sigma_n)
=
((1+\sigma_1)/2, \dots, (1+\sigma_n)/2)
$$

induces an isomorphism of categories

$$
(\Phi_n)_* \colon \mathcal{C}_n \xrightarrow{\cong} \operatorname{Path}(Q_n).
$$

**Proof.** On objects, \(\Phi_n\) is a bijection between \(\{\pm1\}^n\) and
\(\{0,1\}^n\). On generating edge morphisms, it sends a change of one sign to
a change of one bit, and conversely. Hence any path is transferred and lifted
uniquely, so \((\Phi_n)_*\) has an inverse functor. \(\square\)

### Theorem 8.11 [D|cat]. Dimension-Reduction Functors

Fix an axis \(k\).

1. The graph isomorphism \(\rho_k:V_n^{(k)}\to V_{n-1}\) from Theorem 8.2.9
   induces an isomorphism of categories

   $$
R_k := \operatorname{Path}(\rho_k) \colon \operatorname{Path}\bigl(G_{\mathrm{res}}(V_n^{(k)})\bigr) \xrightarrow{\cong} \mathcal{R}_{n-1}.
   $$

2. Forgetting one sign,
   \(\tau_k:\{\pm1\}^n\to\{\pm1\}^{n-1}\), from Theorem 8.2.10 induces a
   functor

   $$
T_k \colon \mathcal{C}_n \to \mathcal{C}_{n-1},
   $$

   acting on generating edges as follows:
   - an edge changing the sign on axis \(k\) is sent to an identity;
   - an edge changing the sign on another axis is sent to the corresponding
     edge of the smaller chamber graph.

**Proof.** The first part is immediate because \(\rho_k\) is a graph
isomorphism. In the second part, the rule on generating edges is compatible
with source and target, and extends to arbitrary paths by concatenation.
Preservation of identities and composition follows by construction.
\(\square\)

### Definition 8.12 [D|cat]. Incidence as a Span, Not as a Functor-Matrix

Let

$$
I_n := \{(v, \sigma) : (B_n)_{v, \sigma} = 1\}
$$

be the set of incident "pole-chamber" pairs. Consider the discrete category

$$
\mathcal{I}_n := \operatorname{Disc}(I_n).
$$

Then incidence is given by the span diagram of categories

$$
\operatorname{Disc}(V_n)\xleftarrow{\;\pi_{\mathrm{pole}}\;}\mathcal{I}_n
\xrightarrow{\;\pi_{\mathrm{ch}}\;}\operatorname{Disc}(\operatorname{Cham}(O_n)).
$$

This is the correct minimal categorical packaging of the matrix \(B_n\).

### Definition 8.12.A [D|cat]. Edge Incidence as a Span in the Strict \(3\)-Bit Case

For the strict six-point shell, set

$$
E_3^{\mathrm{adm}} := E(R_1)
$$

and consider the set of incident "pole-safe edge" pairs

$$
I_3^{\mathrm{edge}} := \{(v, e) \in X_{\mathrm{adm}} \times E_3^{\mathrm{adm}} : v \text{ is an endpoint of } e\}.
$$

Then edge incidence is given by the span diagram

$$
\operatorname{Disc}(X_{\mathrm{adm}})
\xleftarrow{\;\pi_{\mathrm{pole}}\;}
\operatorname{Disc}(I_3^{\mathrm{edge}})
\xrightarrow{\;\pi_{\mathrm{edge}}\;}
\operatorname{Disc}(E_3^{\mathrm{adm}}).
$$

This is the correct minimal categorical packaging of the pole-edge incidence
matrix \(M_3\).

### Corollary 8.12.B [D|cat]. Reconstruction of the Relational Core from Chamber and Edge Incidence in Dimension \(3\)

Let \(B=B_3\) be the pole-chamber incidence matrix, and let \(M=M_3\) be the
pole-edge incidence matrix for admissible edges \(R_1\). Then

$$
B B^T = 4I + 2A_{R_1} + 2A_{R_2},
\qquad
M M^T = 2I + A_{R_1}.
$$

Hence the reconstruction formulas for the generators of the relational core
follow immediately:

$$
A_{R_1}=M M^T - 2I,
$$

$$
A_{R_2}=\frac12(B B^T - 2M M^T),
$$

$$
A_{R_3} = J - I - A_{R_1} - A_{R_2}.
$$

Therefore the chamber interface and the admissible-edge interface jointly
reconstruct the full relational layer of the strict six-point core.

**Proof.** The first two formulas are direct counts of common chambers and
common admissible edges for pairs of admissible poles. The remaining equalities
are obtained by rearranging terms and by using the fact that the relation
classes \(R_0,R_1,R_2,R_3\) partition the complete graph on
\(X_{\mathrm{adm}}\). \(\square\)

### Remark 8.12.C [D|cat]. Why Counting-Language Is Needed Here

If the corresponding span objects are considered only as Boolean relations,
composition answers only whether a common chamber or a common admissible edge
exists. The formulas of Corollary 8.12.B count multiplicities. Therefore the
correct functorial packaging of this point must not be purely Boolean; it must
record cardinalities, for example through linear matrix composition or through
an \(\mathbb N\)-enriched profunctor.

### Corollary 8.12.D [D|cat]. Local Square Law between States and the Operator Layer

Let \(F\subset Q_3\) be any coordinate square face of the cube. Then:

1. the induced subgraph on the vertices of \(F\) is isomorphic to \(C_4\);
2. the edge set of this face, considered as a vertex set of the line graph
   \(L(Q_3)\), also induces a subgraph isomorphic to \(C_4\).

Therefore any local \(2\)-bit carrier of type \(\mathbb F_2^2\), realized as a
square face of \(Q_3\), also determines a square face inside \(L(Q_3)\).

**Proof.** A coordinate face of the cube is obtained by fixing one value of one
coordinate and leaving the two remaining coordinates free. Hence exactly four
one-bit transitions are allowed on its vertices, forming a cycle of length
\(4\), that is, \(C_4\). The edges of the same face in \(Q_3\) are adjacent
pairwise exactly when they share a vertex on the face; in a square this again
gives a cycle of length \(4\). The line graph sends edges of the original graph
to vertices and adjacency to incidence at a common vertex. Therefore the
induced subgraph in \(L(Q_3)\) is again \(C_4\). \(\square\)

### Corollary 8.12.D1 [D|cat]. Restricted Square Functor of the Two-Bit Layer

Denote by

$$
\mathbf{Bin}_2^{\mathrm{sq}}
$$

the small groupoid of realizations of the two-bit carrier \(\mathbb F_2^2\),
where morphisms are bijections preserving explicit Hamming adjacency. Then the
square reading defines a functor

$$
\mathrm{Sq} \colon \mathbf{Bin}_2^{\mathrm{sq}} \to \mathbf{Graph}_{\mathrm{locinj}},
$$

which assigns to each object a square \(C_4\), and to each morphism a graph
isomorphism between such squares.

Moreover, the restricted line-graph functor gives

$$
L(\mathrm{Sq}(-))\cong \mathrm{Sq}(-),
$$

because

$$
L(C_4)\cong C_4.
$$

Thus the precore two-bit carrier \(\mathbb F_2^2\) determines a local
functorial bundle: a binary cell, a square face in state space, and the
corresponding square face in \(L(Q_3)\).

**Proof.** The explicit Hamming reading on \(\mathbb F_2^2\) naturally gives
the graph \(C_4\). A morphism in \(\mathbf{Bin}_2^{\mathrm{sq}}\), by
definition, preserves one-bit adjacency and therefore induces a graph
isomorphism between the corresponding squares; identities and composition are
preserved automatically. Further, \(\mathbf{Graph}_{\mathrm{locinj}}\) admits
the standard line-graph functor, and for the square \(C_4\) its image is again
isomorphic to \(C_4\). \(\square\)

### Remark 8.12.D2 [D|cat]. What Is Not Included in This Statement

Corollary 8.12.D1 concerns only the explicit square law of the two-bit carrier.

It does not lift the following to functorial statements:

- the oppositional reading \(2K_2\);
- the partial closure \(K_4-e\);
- the full closure \(K_4\);
- the simplex-sector \(\{01,10,11\}\) with the hidden role of \(00\).

These local structures remain separate readings of the precore binary
foundation and are not part of the minimal functorial component.

### Corollary 8.12.D3 [D|cat]. Square Embedding of the Two-Bit Layer through Cube Faces

Denote by

$$
\mathbf{Face}_2(Q_3)
$$

the small category of coordinate square faces of the cube \(Q_3\), whose
morphisms are restrictions of cube automorphisms sending one such face to
another.

Then:

1. there is a restricted realization map from
   \(\mathbf{Bin}_2^{\mathrm{sq}}\) to \(\mathbf{Face}_2(Q_3)\), realizing the
   two-bit cell as a square face of \(Q_3\);
2. the induced subgraph on the vertices of the face defines a functor

   $$
   V_{\mathrm{sq}}:\mathbf{Face}_2(Q_3)\to \mathbf{Graph}_{\mathrm{locinj}},
   $$

   and always gives \(C_4\);

3. the edge reading of the same face inside \(L(Q_3)\) defines a functor

   $$
   E_{\mathrm{sq}}:\mathbf{Face}_2(Q_3)\to \mathbf{Graph}_{\mathrm{locinj}},
   $$

   and also always gives \(C_4\).

Thus the local two-bit square functor enters the strict \(3\)-bit layer through
square faces of the cube and their images in \(L(Q_3)\).

**Proof.** The first point fixes the fact that any two-bit cell is realized as
a coordinate square face of the cube. The second point is the induced subgraph
on the vertices of the face, which by Corollary 8.12.D is always isomorphic to
\(C_4\). The third point is the induced subgraph in \(L(Q_3)\) on the set of
edges of the same face, which by the same Corollary 8.12.D is again isomorphic
to \(C_4\). Preservation of identities and composition follows because the
morphisms in \(\mathbf{Face}_2(Q_3)\) are induced by restrictions of cube
automorphisms. \(\square\)

### Remark 8.12.E [D|cat]. Composition Scheme in Dimension \(3\)

The local square law and the deletion of poles determine the order of
construction of the strict \(3\)-bit layer: \(\mathbb F_2^2\) is realized on a
square face of \(Q_3\), then the transition goes to the admissible layer, the
relational layer, the incidence layer, and the operator layer.

The corresponding diagram is fixed in Definition 8.12.E1.

### Definition 8.12.E1 [D|cat]. Fixed Composition Diagram of the Strict \(3\)-Bit Body

As a minimal composition scheme, fix the diagram

```text
\mathbb F_2^2
-> Q_3
-> X_{\mathrm{adm}}
-> (R_1,R_2,R_3)
-> B,M
-> L(Q_3).
```

Its meaning is:

1. a local \(2\)-bit cell is realized as a square face of the state space;
2. then deletion of the two poles gives the admissible six-vertex layer;
3. then relational reading gives the relational core;
4. then the relational core is lifted to incidence interfaces;
5. separately, the cubic layer gives the operator graph \(L(Q_3)\).

This diagram is not asserted as a universal property. It fixes the minimal
order of transitions, which should not be violated below.

### Corollary 8.12.E2 [D|cat]. Decomposition of \(L(Q_3)\) into Internal and Polar Edges

In the strict \(3\)-bit case, the line graph

$$
L(Q_3)
$$

gives the graph of edges of elementary one-bit transitions. Its vertices
naturally split into three classes:

1. **six internal shell transitions**

   these are the edges of the cube \(Q_3\) whose two endpoints both lie in the
   admissible layer

   $$
   X_{\mathrm{adm}}=Q_3\setminus\{000,111\};
   $$

2. **three descending polar edges**

   these are edges incident to the pole \(000\);

3. **three ascending polar edges**

   these are edges incident to the pole \(111\).

Therefore the vertex set of the graph \(L(Q_3)\) has the decomposition

$$
12 = 6 + 3 + 3.
$$

After restriction to the internal shell part, we obtain the induced subgraph on
six vertices, naturally isomorphic to the cycle

$$
C_6.
$$

This internal six-vertex subgraph forms the minimal safe transport layer. The
full graph \(L(Q_3)\) does not reduce to \(C_6\): the polar edges remain as
separate vertices, although they do not belong to the internal transport along
the shell.

**Proof.** The cube \(Q_3\) has \(12\) edges in total, so \(L(Q_3)\) has
\(12\) vertices. The edges incident to \(000\) are the three possible one-step
flips from \(000\); analogously, for \(111\) we obtain three more edges. The
remaining six edges have both endpoints in \(X_{\mathrm{adm}}\). But the
induced graph on \(X_{\mathrm{adm}}\) under the relational reading is
\(R_1=C_6\), that is, precisely the six admissible one-bit transitions inside
the shell. Two such internal vertices in \(L(Q_3)\) are adjacent exactly when
the corresponding transitions share a common admissible vertex; this gives
adjacency along the hexagonal shell cycle. Therefore the internal induced
subgraph in \(L(Q_3)\) is isomorphic to \(C_6\). \(\square\)

### Remark 8.12.E3 [D|cat]. What Follows from the \(6+3+3\) Decomposition

Corollary 8.12.E2 fixes only the lower operator skeleton:

- the internal \(C_6\) as the minimal safe transport layer;
- three edges to \(000\);
- three edges to \(111\).

It does not assert:

- a rule for choosing a concrete active edge inside \(C_6\);
- a full operator calculus over \(L(Q_3)\);
- identification of \(Q_3 \to L(Q_3)\) with a general functor of the whole body.

Thus the cube-octahedral decomposition refines the operator lift, but does not
change its status.

### Definition 8.12.F [D|cat]. Minimal Type Vocabulary of the Strict \(3\)-Bit Body

In dimension \(3\), for the subsequent categorical packaging, fix the following
classes of objects:

1. **carrier objects**
   - \(\mathbb F_2^2\) as a local precore carrier,
   - \(Q_3\),
   - \(X_{\mathrm{adm}}\),
   - coordinate square faces of \(Q_3\);

2. **relational objects**
   - the package \((R_0,R_1,R_2,R_3)\),
   - the relation algebra \(\mathcal A_6\);

3. **graph objects**
   - \(C_4\),
   - \(C_6\),
   - \(K_3 \sqcup K_3\),
   - \(3K_2\),
   - \(K_{2,2,2}\),
   - \(L(Q_3)\) as a finite graph also admitting a separate operator reading;

4. **incidence objects**
   - the chamber span \(B\),
   - the edge span \(M\);

5. **operator objects**
   - the operator structure on \(L(Q_3)\),
   - the encompassing operator package.

This is the minimal type vocabulary that should not be mixed below.

### Definition 8.12.G [D|cat]. Minimal Arrow Types

For the same objects, distinguish the following basic arrow types:

1. **local embedding**
   $$
   \mathbb F_2^2 \hookrightarrow Q_3;
   $$

2. **restriction / deletion of poles**
   $$
   Q_3 \to X_{\mathrm{adm}};
   $$

3. **relational reading**
   $$
   X_{\mathrm{adm}} \to (R_1,R_2,R_3);
   $$

4. **graph realization**
   $$
   (R_i) \rightsquigarrow C_6,K_3\sqcup K_3,3K_2,K_{2,2,2};
   $$

5. **incidence lift**
   $$
   (X_{\mathrm{adm}},R_i)\to B,M;
   $$

6. **operator lift**
   $$
   Q_3 \to L(Q_3);
   $$

7. **restricted square functor**
   $$
   \mathrm{Sq}:\mathbf{Bin}_2^{\mathrm{sq}}\to \mathbf{Graph}_{\mathrm{locinj}};
   $$

8. **reduction**
   $$
   n \to n-1.
   $$

Here the different notational arrows \((\hookrightarrow,\to,\rightsquigarrow)\)
do not indicate different formal categories; they indicate that the transition
types are different and should not be identified without an additional proof.

### Remark 8.12.G1 [D|cat]. Typed Language of Lifts and the Boundary of the Categorical Layer

After volume `01A`, the transition \(\mathbb F_2^2\to Q_3\) is useful to read
as typed: face lift, pair lift, triad lift, transport lift, and pole lift.

The categorical layer of the present volume does not formalize all these lift
modes at once, but only those already having strict status in the finite body:

- local square embedding;
- deletion of poles;
- relational reading;
- incidence lift;
- operator lift.

This is why the arrow types in 8.12.G are not declared to be a complete
functorial vocabulary of all bridge operations, but specify a strict
sublanguage of transitions already constructed.

### Remark 8.12.H [D|cat]. Why This Typing Is Needed

The categorical layer of the body is not built from one abstract arrow. A
minimal set of distinguished types is needed here:

- a carrier is not a relational object;
- relational reading is not incidence lift;
- graph reading is not operator lift;
- a bridge is not a strict functor.

Only after such typing does it make sense to ask which of these arrows extend
to functors and which remain readings or interfaces.

### Remark 8.12.I [D|cat]. Immediate Consequence of Typing

After Definitions 8.12.F-8.12.G, the following is already fixed:

1. the strict \(3\)-bit body is no longer treated as one undifferentiated arrow,
   but only as a set of typed objects and transitions;
2. relational reading, incidence lift, and operator lift are distinguished by
   type and must not be identified automatically;
3. functorial statements here are restricted to what has already been fixed
   separately:
   - \(Path(G)\),
   - the chamber functor,
   - dimension-reduction functors,
   - the span/profunctor interface,
   - the restricted square functor of the two-bit precore layer;
4. the final brief summary is given below in Remark 8.14.

### Corollary 8.13 [D|cat]. Descent of Span Incidence under Reduction

For a chosen axis \(k\), the reductions \(\rho_k\) and \(\tau_k\) are compatible
with span incidence: after deleting the poles \(\pm e_k\) and quotienting
chambers by \(\tau_k\), one obtains a span isomorphic to

$$
\operatorname{Disc}(V_{n-1}) \xleftarrow{\;} \mathcal{I}_{n-1} \xrightarrow{\;} \operatorname{Disc}(\operatorname{Cham}(O_{n-1})).
$$

**Proof.** This is just the categorical reformulation of Theorem 8.2.11 on the
descent of the matrix \(B_n\to B_{n-1}\). \(\square\)

### Corollary 8.13.1 [D|cat]. Incidence as a Profunctor

Span incidence is equivalently given by the profunctor

$$
\mathbb{I}_n \colon \operatorname{Disc}(\operatorname{Cham}(O_n))^{\mathrm{op}} \times \operatorname{Disc}(V_n) \to \mathbf{Set},
$$

where

$$
\mathbb{I}_n(v, \sigma) = \begin{cases} \{*\}, & (B_n)_{v, \sigma} = 1, \\ \varnothing, & (B_n)_{v, \sigma} = 0. \end{cases}
$$

By the standard convention, this is a profunctor from the polar layer to the
chamber layer. Since both categories are discrete and incidence is binary, the
same object can naturally be regarded as a \(\mathbf{2}\)-enriched profunctor;
in that case it mathematically trivializes to the ordinary Boolean matrix
\(B_n\). The categorical language here serves only as an interface.

**Proof.** For discrete categories, profunctors are equivalent to sets of pairs
marked "empty/nonempty", that is, ordinary relations. The span of Definition
8.12 encodes exactly such a relation. \(\square\)

### Remark 8.14 [D|cat]. Brief Categorical Summary of the Strict \(3\)-Bit Body

In compressed form, the categorical status of the strict core is as follows.

1. **No full DOT category is constructed here.** Only the minimal categorical
   form of the strict \(3\)-bit body is fixed.

2. **Classes of objects**:
   - carrier objects: \(Q_3\), \(X_{\mathrm{adm}}\), coordinate square faces;
   - relational objects: \(R_1,R_2,R_3\), \(\mathcal A_6\);
   - incidence objects: \(B\), \(M\);
   - operator object: \(L(Q_3)\) as a finite graph with a separate operator
     reading.

3. **Classes of arrows**:
   - local embedding \(\mathbb F_2^2 \hookrightarrow Q_3\);
   - deletion of poles \(Q_3 \to X_{\mathrm{adm}}\);
   - relational reading \(X_{\mathrm{adm}} \to (R_1,R_2,R_3)\);
   - incidence and operator lifts \(X_{\mathrm{adm}} \to B,M\) and
     \(Q_3 \to L(Q_3)\);
   - reduction \(n \to n-1\).

4. **What is already given functorially**:
   - path categories and induced graph functors;
   - the restricted functor of relational reading on
     \(\mathbf{Adm3}^{\mathrm{iso}}\);
   - restricted functors for computing the relational layer;
   - the chamber functor;
   - dimension-reduction functors;
   - incidence as a span/profunctor;
   - the restricted square functor of the precore \(\mathbb F_2^2\)-layer.

5. **Minimal composition diagram**:

   ```text
\mathbb F_2^2 -> Q_3 -> X_{\mathrm{adm}} -> (R_1,R_2,R_3) -> B,M -> L(Q_3).
   ```

6. **Boundaries of the claims**:
   - relational reading and \(Q_3 \to L(Q_3)\) remain structured readings and
     lifts, not general functors of the body;
   - \(AMR \to \text{core}\) is not included here, since in line \(03\) it is a
     partial typed bridge;
   - \(F_7\) is not included here, since it is an auxiliary projective layer,
     not a shell carrier;
   - higher categorical, monoidal, fibrational, and homotopical refinements are
     not asserted here.

### Remark 8.14.A [D|cat]. Status of the Four Key Arrows

Fix the following separation.

1. \(X_{\mathrm{adm}} \to (R_1,R_2,R_3)\)  
   has the status of a **structured relational reading**, not a full functorial
   block;

2. \((R_i) \rightsquigarrow C_6,K_3\sqcup K_3,3K_2,K_{2,2,2}\)  
   has the status of a **family of structured graph readings**, not one unified
   graph functor of the body;

3. \(Q_3 \to L(Q_3)\)  
   has the status of a **strong structured lift** to the operator layer, not a
   general functor of the body;

4. \(AMR \to \text{core}\)  
   is not part of the strict core and in \(03\) has the status of a **partial
   typed bridge**.

This separation is adopted as the minimal categorical discipline for the arrows
of the body.

### Remark 8.14.B [D|cat]. Refinements on Restricted Categories

On restricted categories, more precise formulations of the first three arrows
are possible without changing their global status in the body.

- \(X_{\mathrm{adm}} \to (R_1,R_2,R_3)\) admits a restricted functorial
  refinement
  $$
  \mathrm{Rel}:\mathbf{Adm3}^{\mathrm{iso}}\to \mathbf{ASch}_3^{\mathrm{lab}},
  $$
  where \(\mathbf{Adm3}^{\mathrm{iso}}\) is the small groupoid of strict
  admissible \(3\)-bit realizations and relation-preserving bijections;
- graph reading admits a functorial refinement not as one general functor of the
  body, but as a family of evaluation functors from an already fixed
  relation-scheme object;
- the line-graph construction for \(Q_3 \to L(Q_3)\) admits a restricted
  functorial refinement on the category of finite simple graphs with
  locally injective morphisms.

On this restricted side, there is also an explicit factorization

$$
\mathbf{Adm3}^{\mathrm{iso}}
\xrightarrow{\ \mathrm{Rel}\ }
\mathbf{ASch}_3^{\mathrm{lab}}
\xrightarrow{\ \mathrm{Ev}_i,\ \mathrm{Ev}_{\mathrm{res}}\ }
\mathbf{Graph},
$$

but these refinements do not replace the global arrow statuses adopted above;
they only locally sharpen them.

### Remark 8.14.C [D|cat]. Transition to Operator Closure

At this point, Section \(8\) completes the categorical block and passes to
operator closure.

By now the following has been obtained:

1. the shell extension has produced higher carrier, chamber, and reduction
   objects;
2. the categorical block has produced:
   - path categories;
   - dimension-reduction functors;
   - span and profunctor interfaces for incidence;
   - square embedding of the two-bit layer;
   - a vocabulary of object and arrow types;
   - a brief summary of statuses;
3. the rest of Section \(8\) does not introduce a new relational core, but
   translates the already constructed shell layer into operator language.

Therefore block \(8.15-8.28.5\) should be read as the operator closure of the
already constructed finite layer.

### Definition 8.15 [D|alg]. Shell Apertures

Let

$$
\mathcal{H}_n := \mathbb{R}^{\{0,1\}^n}
$$

be the space of functions on the full \(n\)-cube. For each
\(k\in\{0,\dots,n\}\), define the orthogonal projector onto the shell
\(S_k^{(n)}\):

$$
\Pi_k:\mathcal{H}_n\to\mathcal{H}_n,
\qquad
(\Pi_k f)(x)=
\begin{cases}
f(x), & x\in S_k^{(n)},\\
0, & x\notin S_k^{(n)}.
\end{cases}
$$

The projector \(\Pi_k\) is called the aperture of level

$$
\alpha=\frac{k}{n}.
$$

### Definition 8.15.A [D|alg]. Two-Stage Shell Apertures

For the full cube \(Q_n\), define two special projector families:

$$
P_{\mathrm{shell}}^{(n)}:=I-\Pi_0-\Pi_n=\sum_{k=1}^{n-1}\Pi_k,
\qquad
P_{\mathrm{out}}^{(n)}:=\Pi_1+\Pi_{n-1}.
$$

Here:

- \(P_{\mathrm{shell}}^{(n)}\) selects the full nontrivial shell package \(U_n\);
- \(P_{\mathrm{out}}^{(n)}\) selects the strict external carrier \(V_n\).

### Proposition 8.15.B [D|alg]. Operator Realization of the Ladder

For every \(n\ge 3\),

$$
\operatorname{Im} P_{\mathrm{shell}}^{(n)}=\mathbb R^{U_n},
\qquad
\operatorname{Im} P_{\mathrm{out}}^{(n)}=\mathbb R^{V_n}.
$$

Moreover,

$$
P_{\mathrm{out}}^{(n)}P_{\mathrm{shell}}^{(n)}=
P_{\mathrm{shell}}^{(n)}P_{\mathrm{out}}^{(n)}=
P_{\mathrm{out}}^{(n)},
$$

that is, the external shell is a subaperture of the full nontrivial package.

**Proof.** By definition, \(\Pi_k\) projects exactly onto the shell
\(S_k^{(n)}\). Therefore the sum of all projectors except \(\Pi_0\) and
\(\Pi_n\) has as its image the space of functions on the union

$$
\bigsqcup_{k=1}^{n-1}S_k^{(n)}=U_n.
$$

The sum \(\Pi_1+\Pi_{n-1}\) has as its image the functions on

$$
S_1^{(n)}\sqcup S_{n-1}^{(n)}=V_n.
$$

Since the projectors onto distinct shells are orthogonal, multiplying
\(P_{\mathrm{out}}^{(n)}\) by \(P_{\mathrm{shell}}^{(n)}\) simply keeps the same
two extreme nontrivial layers, hence equals \(P_{\mathrm{out}}^{(n)}\).
\(\square\)

### Corollary 8.15.C [D|alg]. The Special Three-Dimensional Case

For \(n=3\),

$$
P_{\mathrm{shell}}^{(3)}=P_{\mathrm{out}}^{(3)}=I-\Pi_0-\Pi_3,
$$

because in the three-dimensional case there are no intermediate shells between
\(S_1^{(3)}\) and \(S_2^{(3)}\).

Therefore the strict six-point shell in dimension \(3\) is simultaneously:

- the full nontrivial package;
- the external shell carrier.

For \(n\ge 4\), these two statuses diverge.

### Proposition 8.16 [D|alg]. Basic Aperture Identities

The projectors \(\Pi_k\) form an orthogonal decomposition of the identity:

$$
\Pi_j\Pi_k=\delta_{jk}\Pi_k,
\qquad
\sum_{k=0}^n \Pi_k=I_{\mathcal H_n}.
$$

Moreover, complement satisfies

$$
C\,\Pi_k=\Pi_{n-k}\,C.
$$

**Proof.** The shells

$$
S_0^{(n)},S_1^{(n)},\dots,S_n^{(n)}
$$

form a disjoint partition of the whole cube \(\{0,1\}^n\). Therefore each
standard basis vector lies in exactly one shell, whence immediately

$$
\sum_{k=0}^n \Pi_k=I,
\qquad
\Pi_k\Pi_\ell=0\quad (k\neq \ell),
\qquad
\Pi_k^2=\Pi_k.
$$

Further, complement sends a word of weight \(k\) to a word of weight \(n-k\),
that is,

$$
C(S_k^{(n)})=S_{n-k}^{(n)}.
$$

Hence applying \(C\) after the projector onto \(S_k^{(n)}\) coincides with
applying the projector onto \(S_{n-k}^{(n)}\) after \(C\), and therefore

$$
C\,\Pi_k=\Pi_{n-k}\,C.
$$

\(\square\)

### Definition 8.17 [D|alg]. Primitive Cubic Operator and Its Aperture Blocks

Let

$$
A_{Q_n}
$$

be the adjacency matrix of the full hypercube \(Q_n\). For aperture levels
\(j,k\), define the block

$$
A_{j,k}^{(n)} := \Pi_j A_{Q_n} \Pi_k.
$$

### Theorem 8.18 [D|alg]. Aperture Band Structure of the Primitive Dynamics

For the full hypercube,

$$
\Pi_j A_{Q_n}\Pi_k=0
\qquad
\text{when } |j-k|\neq 1.
$$

Consequently,

$$
A_{Q_n}=U_n+D_n,
$$

where

$$
U_n := \sum_{k=0}^{n-1} \Pi_{k+1} A_{Q_n} \Pi_k, \qquad D_n := \sum_{k=1}^n \Pi_{k-1} A_{Q_n} \Pi_k.
$$

The operators \(U_n\) and \(D_n\) raise and lower Hamming weight exactly by
\(1\).

**Proof.** A one-bit flip changes Hamming weight exactly by \(\pm1\), and by
nothing else. \(\square\)

### Corollary 8.19 [D|alg]. The Nontrivial Package and External Carrier as Corners, Not Ideals

Define two projectors

$$
\Pi_{\mathrm{nt}} := I - \Pi_0 - \Pi_n = \sum_{k=1}^{n-1} \Pi_k,
$$

$$
\Pi_{\mathrm{ext}} := \Pi_1 + \Pi_{n-1}.
$$

Then the corresponding compressions

$$
\Pi_{\mathrm{nt}} \, \mathrm{End}(\mathcal{H}_n) \, \Pi_{\mathrm{nt}}, \qquad \Pi_{\mathrm{ext}} \, \mathrm{End}(\mathcal{H}_n) \, \Pi_{\mathrm{ext}}
$$

are correct corner algebras. They are not called ideals.

### Corollary 8.20 [D|alg]. Special Feature of the Three-Dimensional Case for Primitive External Dynamics

The compressed primitive operator on the external carrier has the form

$$
\Pi_{\mathrm{ext}} A_{Q_n} \Pi_{\mathrm{ext}} = \begin{cases} A_{\mathrm{prim}} \cong C_6, & n=3, \\ 0, & n \ge 4. \end{cases}
$$

**Proof.** For \(n=3\),

$$
\Pi_{\mathrm{ext}}=\Pi_1+\Pi_2=\Pi_{\mathrm{nt}},
$$

and the primitive dynamics on the compressed cube gives exactly the six-cycle.
For \(n\ge 4\), vertices of weight \(1\) and \(n-1\) are not connected by
one-bit transitions either to each other or within their own shells, since one
flip sends them to shells of weights \(0,2,n-2,n\). Therefore the corresponding
compression is zero. \(\square\)

### Remark 8.21 [D|alg]. Dimensional Boundary of the Primitive Cycle

The statement shows that the \(3\)-dimensional primitive cycle does not transfer
mechanically to all dimensions.

- In dimension \(3\), the external carrier and the nontrivial package coincide.
- In dimensions \(n\ge 4\), the external carrier \(V_n\) remains a strict
  residual carrier, but is no longer a closed carrier of the one-bit primitive
  dynamics of the hypercube.

Therefore the higher DOT program uses the residual graph \(K_{2,\dots,2}\) on
\(V_n\), and does not declare it to be a direct primitive cycle.

### Definition 8.22 [D|alg]. Enhanced Aperture Operators

Set

$$
E_n := D_n, \qquad F_n := U_n,
$$

and introduce the diagonal operator

$$
H_n := \sum_{k=0}^n (n-2k) \Pi_k.
$$

Then \(H_n\) acts on the shell \(S_k^{(n)}\) by multiplication by

$$
n-2k.
$$

### Theorem 8.23 [D|alg]. Exact Commutation Relations

The operators \(E_n,F_n,H_n\) satisfy

$$
[H_n, E_n] = 2E_n, \qquad [H_n, F_n] = -2F_n, \qquad [E_n, F_n] = H_n.
$$

Therefore the space \(\mathcal H_n\) carries a concrete representation of the
Lie algebra \(\mathfrak{sl}_2\).

**Proof.** On the shell \(S_k^{(n)}\), the operator \(E_n\) sends vectors to
\(S_{k-1}^{(n)}\), while \(F_n\) sends them to \(S_{k+1}^{(n)}\). Therefore

$$
H_nE_n-E_nH_n=((n-2(k-1))-(n-2k))E_n=2E_n,
$$

$$
H_nF_n-F_nH_n=((n-2(k+1))-(n-2k))F_n=-2F_n.
$$

For a basis vector \(\delta_x\) of weight \(k\), the operator \(F_n\) selects
all \(n-k\) zero coordinates and then \(E_n\) returns downward; the operator
\(E_n\) selects all \(k\) one coordinates and then \(F_n\) returns upward. The
difference is

$$
(n-k)-k=n-2k,
$$

that is,

$$
[E_n,F_n]=H_n.
$$

\(\square\)

### Remark 8.23.A [D|alg]. Encompassing Operator Layer and Admissible Layers

The relations of Theorem 8.23 are asserted on the full finite-dimensional space

$$
\mathcal H_n=\mathbb R^{\{0,1\}^n},
$$

where the shell operators \(E_n,F_n,H_n\) are closed over the weight shells of
the Boolean cube. This does not contradict the strict DOT separation of
carriers:

- the admissible core \(X_{\mathrm{adm}}^{(3)}\) and the external residual
  carrier \(V_n\) are graph-combinatorial layers;
- the operator \(\mathfrak{sl}_2\)-layer is an encompassing layer on
  \(\mathcal H_n\);
- for \(n\ge 4\), the residual carrier \(V_n\) is no longer a closed carrier of
  one-bit primitive dynamics, as fixed in Remark 8.21.

It is not asserted that \(V_n\) or \(X_{\mathrm{adm}}\) is invariant under the
full action of \(E_n,F_n\); only the existence of an encompassing operator layer
is asserted, over which residual and admissible packages are read as narrower
combinatorial realizations. For \(n=3\), an exact projection interpreter is
constructed below, closing this layer back into the finite signature of the
strict core.

### Remark 8.23.B [Context]. External Mathematical Precedent

The commutation relations

$$
[H_n,E_n]=2E_n,\qquad [H_n,F_n]=-2F_n,\qquad [E_n,F_n]=H_n
$$

on the space of functions on the Boolean cube correspond to the standard
\(\mathfrak{sl}_2\)-representation known in algebraic combinatorics as the
action of raising and lowering operators by Hamming weight; see Stanley and
Terwilliger. In DOT, these operators are not merely reproduced in standard
form, but are then tied to the aperture projectors \(\Pi_k\) and the complement
involution \(C\), giving a closed operator algebra
\(\mathcal A_n^{\mathrm{ap}}\) inside the strict body.

### Proposition 8.24 [D|alg]. Action of Complement on Enhanced Operators

Complement \(C\) satisfies

$$
C^2 = I, \qquad C H_n = -H_n C, \qquad C E_n = F_n C, \qquad C F_n = E_n C.
$$

**Proof.** Complement sends the shell \(S_k^{(n)}\) to \(S_{n-k}^{(n)}\), and
therefore changes the sign of the eigenvalue \(n-2k\) of \(H_n\). At the same
time, it changes a flip \(1\to 0\) into a flip \(0\to 1\), hence interchanges
\(E_n\) and \(F_n\). \(\square\)

### Proposition 8.25 [D|alg]. Recovering Apertures from the Spectrum of \(H_n\)

All shell projectors \(\Pi_k\) are expressed as polynomials in \(H_n\):

$$
\Pi_k = \prod_{\substack{0 \le j \le n \\ j \ne k}} \frac{H_n-(n-2j)I}{(n-2k)-(n-2j)}.
$$

Consequently, they belong to the algebra generated by \(H_n\) alone.

**Proof.** The eigenvalues of \(H_n\) on different shells are pairwise distinct
and equal to \(n,n-2,\dots,-n\). Therefore the standard Lagrange formula for
spectral projectors gives exactly the displayed polynomial. \(\square\)

### Definition 8.26 [D|alg]. Enhanced Aperture Algebra

Define

$$
\mathcal{A}_n^{\mathrm{ap}} := \langle E_n, F_n, H_n, C \rangle \subset \operatorname{End}(\mathcal{H}_n).
$$

### Corollary 8.27 [D|alg]. Structure of the Enhanced Aperture Algebra

The algebra \(\mathcal A_n^{\mathrm{ap}}\) contains:

- all shell projectors \(\Pi_k\);
- the raising and lowering operators \(U_n,F_n\) and \(D_n,E_n\);
- the representation of \(\mathfrak{sl}_2\) on \(\mathcal H_n\);
- the complement involution, which interchanges \(E_n\) and \(F_n\) and reverses
  the sign of \(H_n\).

The aperture layer is not only projective, but also operator-algebraic.

### Theorem 8.27.1 [D|alg]. Universal Smash/Enveloping Realization

Let \(\theta\) be the automorphism of the Lie algebra \(\mathfrak{sl}_2\) given
on the standard generators by

$$
\theta(E) = F, \qquad \theta(F) = E, \qquad \theta(H) = -H.
$$

Then there exists a unique algebra homomorphism

$$
\rho_n:
U(\mathfrak{sl}_2)\#_\theta \mathbb{R}[\mathbb{Z}_2]
\longrightarrow
\mathrm{End}(\mathcal H_n)
$$

such that

$$
\rho_n(E) = E_n, \qquad \rho_n(F) = F_n, \qquad \rho_n(H) = H_n, \qquad \rho_n(c) = C,
$$

where \(c\) is the nontrivial element of the group \(\mathbb{Z}_2\). The image
of this homomorphism is

$$
\operatorname{Im}(\rho_n)=\mathcal A_n^{\mathrm{ap}}.
$$

**Proof.** By Theorem 8.23, the operators \(E_n,F_n,H_n\) satisfy the
\(\mathfrak{sl}_2\) relations, so by the universal property of the enveloping
algebra there exists a unique homomorphism

$$
U(\mathfrak{sl}_2)\to \mathrm{End}(\mathcal H_n).
$$

By Proposition 8.24, the operator \(C\) realizes the automorphism \(\theta\) by
conjugation. Consequently, by the universal property of the smash product
(skew group ring), this homomorphism extends uniquely to \(\rho_n\). Equality
of the image with \(\mathcal A_n^{\mathrm{ap}}\) follows from the definition of
the latter as the algebra generated by \(E_n,F_n,H_n,C\). \(\square\)

### Remark 8.27.2 [D|alg]. On the Kernel of the Representation \(\rho_n\)

Since the representation \(\rho_n\) is realized on the finite-dimensional space

$$
\mathcal H_n=\mathbb R^{\{0,1\}^n}
$$

of dimension \(2^n\), while the algebra

$$
U(\mathfrak{sl}_2)\#_\theta \mathbb{R}[\mathbb Z_2]
$$

is infinite-dimensional, the homomorphism \(\rho_n\) is not faithful and
therefore has a nontrivial kernel. Theorem 8.27.1 asserts only existence,
uniqueness, and a description of the image, not faithfulness of this
representation.

### Remark 8.28 [D|alg]. What Is Still Not Asserted

It is not asserted that \(\mathcal A_n^{\mathrm{ap}}\) is a faithful or full
image of the universal smash algebra, or that it has a standard
\(*\)-completion. A concrete finite-dimensional operator layer and its
universal origin have been fixed.

### Definition 8.28.1 [D|alg]. Projection Interpreter of the Strict \(3\)-Bit Core

For \(n=3\), set

$$
P := \Pi_1 + \Pi_2 = I - \Pi_0 - \Pi_3.
$$

This projector selects the external aperture of the Boolean cube, which
coincides with the admissible package

$$
X_{\mathrm{adm}}=\{0,1\}^3\setminus\{000,111\}.
$$

The projection interpreter of the strict \(3\)-bit core is defined as the
restriction of the operator layer to the image of \(P\):

$$
\mathcal I_3:=P:\mathcal H_3\to P\mathcal H_3\cong \mathbb R^{X_{\mathrm{adm}}}.
$$

The coincidence of the external aperture with the admissible core makes the
three-dimensional case a point of exact closure.

### Theorem 8.28.2 [D|alg]. Operator Reconstruction of the Relational Layer for \(n=3\)

On the space \(P\mathcal H_3\cong \mathbb R^{X_{\mathrm{adm}}}\), the relations
of the strict core are recovered by the formulas

$$
A_{R_1}=P(E_3+F_3)P,
$$

$$
A_{R_3}=PCP,
$$

$$
A_{R_2}=A_{R_1}^2-2I.
$$

**Proof.** The first equality follows because \(E_3+F_3\) is the adjacency
matrix of the full cube \(Q_3\), while the projector \(P\) deletes only the
vertices \(000\) and \(111\); hence on the admissible package exactly the
one-bit transitions remain, that is, the relation \(R_1\). The second equality
follows because complement \(C\) on \(X_{\mathrm{adm}}\) coincides with the
antipodal relation \(R_3\). The third equality is a direct algebraic
consequence of Theorem 2.6.6:

$$
A_{R_1}^2=2I+A_{R_2}.
$$

Therefore the full relational layer of the strict core is reconstructed from
the \(\mathfrak{sl}_2\)-layer and complement after projection by \(P\).
\(\square\)

### Lemma 8.28.3 [D|alg]. Cliques \(K_{2,2,2}\) and Fixed Incidence

Let

$$
A_{\mathrm{oct}} := A_{R_1} + A_{R_2}.
$$

Then \(A_{\mathrm{oct}}\) is the graph \(K_{2,2,2}\), and its three parts are
given by complementary pairs determined by the matrix \(A_{R_3}\). The maximal
cliques of this graph are the triangles obtained by choosing one vertex from
each part; there are exactly \(2^3=8\) such cliques.

The incidence matrix "vertex-maximal clique" coincides with the fixed incidence
matrix of chambers of the strict \(3\)-bit core.

**Proof.** By Theorem 2.6.5, the graph \(A_{R_1}+A_{R_2}\) is isomorphic to
\(K_{2,2,2}\), and the edges \(R_3\) pairwise connect vertices in the same
part. Therefore each maximal clique is determined by choosing one vertex from
each of the three parts, that is, by a sign vector
\(\sigma\in\{\pm1\}^3\). But exactly such a sign vector defines a chamber of
the octahedron, and a vertex belongs to a chamber exactly when the sign on its
axis agrees with \(\sigma\). This is precisely the definition of the fixed
incidence. \(\square\)

### Corollary 8.28.4 [D|alg]. Exact Closure of the Bridge

For the strict \(3\)-bit core, the finite signature

$$
\Sigma_{\mathrm{core}} = \bigl( \operatorname{relation\_counts}, \operatorname{shared\_chambers}, \operatorname{shell\_types} \bigr)
$$

is recovered from the operator layer \((E_3,F_3,H_3,C)\).

More precisely:

1. \(\operatorname{relation\_counts}\) is extracted from the matrices
   \(A_{R_1},A_{R_2},A_{R_3}\);
2. \(\operatorname{shell\_types}\) is extracted from the block behavior of these
   matrices with respect to the decomposition
   $$
   P\mathcal H_3=\mathcal C_1\oplus \mathcal C_2;
   $$
3. \(\operatorname{shared\_chambers}\) is extracted from the clique incidence of
   the graph \(K_{2,2,2}\), recovered from \(A_{R_1}+A_{R_2}\).

In particular,

$$
\Sigma_{\mathrm{core}} = \bigl( \{6, 6, 3\}, \{2, 2, 0\}, \{\mathrm{between}, \mathrm{within}, \mathrm{axial}\} \bigr).
$$

**Proof.** Points (1) and (2) follow from Theorem 8.28.2 and from the definition
of the finite signature of the relational core. Point (3) follows from Lemma
8.28.3: the number of common chambers for a pair of poles equals the number of
common maximal cliques in \(K_{2,2,2}\). For a pair in \(R_1\) or \(R_2\), this
number equals \(2\); for a pair in \(R_3\), it is zero. The finite signature of
the strict core is read both combinatorially and through the projection of the
operator \(\mathfrak{sl}_2\)-layer. \(\square\)

### Remark 8.28.5 [D|alg]. Boundary of Applicability of the Bridge

The previous corollary is exact only for \(n=3\). For \(n\ge 4\), the external
aperture

$$
\Pi_{\mathrm{ext}}^{(n)} = \Pi_1 + \Pi_{n-1}
$$

no longer carries one-bit primitive dynamics: the compressed operator

$$
\Pi_{\mathrm{ext}}^{(n)}(E_n + F_n) \Pi_{\mathrm{ext}}^{(n)}
$$

is zero. Therefore the bridge

$$
\mathfrak{sl}_2 \to \Sigma_{\mathrm{core}}
$$

in its exact present form is a special three-dimensional fact, not a universal
law for all \(n\).

### Remark 8.28.6 [D|alg]. Compressed Summary of Section \(8\)

After all blocks, Section \(8\) asserts the following.

1. The higher shell layer is built through Hamming shells, cross-polytopes,
   chambers, and the reduction \(4D \to 3D\).
2. This layer is given a minimal categorical form through path categories,
   dimension-reduction functors, span/profunctor interfaces, and restricted
   local functorial fragments.
3. The same layer then receives an operator closure through apertures,
   \(\mathfrak{sl}_2\)-operators, complement, and the enhanced aperture algebra.
4. The exact reverse closure of the operator layer into the strict relational
   core is proved only for \(n=3\).

Therefore the whole of Section \(8\) describes a finite extension of the strict
core:

- to shells and reductions;
- to categorical formulations;
- to operator closure;
- and back to exact strict closure only in the special three-dimensional case.

---

## 9. What Remains Open

The following blocks are deliberately not closed:

1. higher categorical extensions over the minimal layer 8.8-8.13;
2. representation-theoretic and universal enhancements beyond the concrete
   image \(\mathcal A_n^{\mathrm{ap}}\);
3. identification of logical negation, coordinate involutions, and the cellular
   boundary in one operator calculus;
4. continuous limiting statements about \(\pi\), \(i\), and other physically
   interpretable constants.

These directions may be meaningful, but they are not part of the strict core.

### Remark 9.1 `[G1]/[G2]`. Continuous Limits

All statements requiring a continuous limiting transition, including topics
about \(\pi\), \(i\), spectral densities, and Sobolev-type metrics, remain
outside the strict core. A finite graph by itself does not derive such constants
without a separate theory of convergence.

---

## 10. Bibliographic Pointers

The external standard sources below are listed not to replace the proofs in the
present text, but to position the results already obtained in a known
mathematical context.

1. **Association schemes and algebraic combinatorics**
   - E. Bannai, T. Ito, *Algebraic Combinatorics I: Association Schemes*, Benjamin/Cummings, 1984.
   - C. Godsil, G. Royle, *Algebraic Graph Theory*, Springer, 2001.

2. **Graph spectra**
   - D. Cvetkovic, P. Rowlinson, S. Simic, *An Introduction to the Theory of Graph Spectra*, Cambridge University Press, 2010.
   - A. Brouwer, W. Haemers, *Spectra of Graphs*, Springer, 2012.

3. **Effective resistances and Foster's formula**
   - R. M. Foster, "The Average Impedance of an Electrical Network", 1949.
   - P. Tetali, "Random walks and the effective resistance of networks", 1991.

4. **Circle cohomology and \(Z_2\)-bundles**
   - A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002.
   - D. Husemoller, *Fibre Bundles*, Springer, 1993.

5. **\(\mathfrak{sl}_2\)-structures on the Boolean cube and the Terwilliger algebra**
   - R. P. Stanley, "Weyl groups, the hard Lefschetz theorem, and the Sperner property", *SIAM Journal on Algebraic and Discrete Methods*, 1980.
   - J. T. Go, *The Terwilliger algebra of the Hypercube*, 2002.
   - P. Terwilliger, *The subconstituent algebra of an association scheme*, 1992.
   - K. Tanabe, works on the Terwilliger algebra of the hypercube, 1990s.

6. **Cross-polytopes, chambers, and convex geometry**
   - H. S. M. Coxeter, *Regular Polytopes*, Dover / Methuen, 1973.
   - G. M. Ziegler, *Lectures on Polytopes*, Springer, 1995.

These references are especially important for Theorems 2.6.6, 4.2, 4.4, 5.2,
5.3, 7.4, 7.6, 8.6, 8.23, and 8.27.1: they fix the standard mathematical
context of the objects used from algebraic combinatorics, spectral graph
theory, convex geometry, and elementary algebraic topology.

---

## 11. Conclusion

The strict DOT core takes the following form.

1. **The preparatory precore layer is fixed.**  
   The binary foundation \(\mathbb F_2^1/\mathbb F_2^2\) is fixed as the minimal
   preparatory base of the strict \(3\)-bit core.

2. **The strict finite carrier is defined.**  
   The axiomatic layer [A] is formalized by the three initial constraints
   \(Z_D,Z_F,Z_C\), after which the admissible carrier takes the exact form
   $$
   X_{\mathrm{adm}} = \{0, 1\}^3 \setminus \{000, 111\}.
   $$

3. **The relational layer is defined.**  
   The six admissible states carry the package \(R_0,R_1,R_2,R_3\), from which
   two main exact graph structures are extracted: the primitive cycle \(C_6\)
   and the residual octahedral graph \(K_{2,2,2}\).

4. **The geometric-chamber layer is defined.**  
   The residual graph is realized as the \(1\)-skeleton of the standard
   octahedron, and its eight sign chambers form the surrounding cube \(Q_3\).

5. **The spectral-transport layer is defined.**  
   The composite graph "octahedron + cube" has exact slow spectral gap
   \(\lambda_2 = 4\) and exact energy ratio \(4:1\) between chambers and poles
   on the slow eigenspace. Twisted transport is correctly modeled by the
   nontrivial class of \(Z_2\)-holonomy on the fixed minimal cycle, and the
   Mobius strip appears only as the associated bundle of this class.

6. **The categorical-interface layer is given in minimal form.**  
   The core now distinguishes:
   - carrier;
   - relation scheme;
   - graph readings;
   - incidence interfaces;
   - operator layer;
   - restricted functorial fragments.

   In particular, the following are already in place:
   - the restricted functor of relational reading;
   - restricted evaluations of the relation scheme;
   - chamber and reduction functors;
   - the span/profunctor interface;
   - the local square functor coming from \(\mathbb F_2^2\).

7. **The \(4D\)-extension and operator algebra are embedded without replacing the core.**  
   The strong geometric branch \(4D \to 3D\) is built as a reduction of the
   \(16\)-cell to the octahedron with pairwise descent of chambers and
   incidence. The aperture layer is closed as a concrete operator algebra with
   \(\mathfrak{sl}_2\)-structure and the complement involution.

The theory preserves:

- integrity;
- minimalism;
- a typed finite framework;
- the internal three-axis structure;
- the octahedral-chamber framework;
- the strict spectral layer;
- the idea of nontrivial return;
- the distinction between core, extension, and bridge.

The boundaries of topological, categorical, and algebraic readings are fixed in
the corresponding sections.
