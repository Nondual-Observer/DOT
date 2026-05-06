# DOT: AMR-SR — Scale/Residue Line

The AMR-SR line: scale, residue, and a partial bridge to the strict core.

## 0. Introduction

AMR-SR is the scale/residue branch inside the broader AMR package.

Its carrier is

$$
\mathcal R=\mathbb N_{>0}^2.
$$

AMR-SR studies the primitive-scale decomposition

$$
(a,b)=g(p,q),
\qquad
g=\gcd(a,b),
\qquad
\gcd(p,q)=1,
$$

difference layers

$$
\Sigma_k=\{(a,b):|a-b|=k\},
$$

primitive rays

$$
\rho_{(p,q)}=\{(gp,gq):g\ge1\},
$$

and the scalar residue

$$
\mathrm{Res}_{\mathrm{sr}}=(g-1)|p-q|.
$$

AMR-SR is not the divisor-carrier branch. The divisor-carrier branch is developed separately in `03B_AMR_Divisor_Carrier_and_Chain_Extension.md`.

AMR-SR uses divisibility theory, integer-lattice geometry, and rational directions for one task: to describe pairs of positive integers by scale, primitive direction, difference layer, and residue.

Text structure:

- arithmetic foundation;
- partial bridge;
- continuation after the threshold.

The prenuclear binary foundation

$$
\mathbb F_2^1, \qquad \mathbb F_2^2
$$

is already fixed in `02A` as a preparatory layer.

Statements without status [P] are explicitly marked as bridges or interpretive layers.

### 0.A. Reading Structure

1. **Arithmetic foundation**: paragraphs \(1-2\).
   This part defines:
   - primitive-scale decomposition;
   - layer / ray / local cell;
   - the residual block \(\operatorname{Res}_{\mathrm{sr}}\);
   - the frontier layer and branch decomposition.

2. **Minimal bridge**: paragraphs \(3.1-3.2.B\).
   This part contains the necessary minimum:
   - the case \(k=3\);
   - the case \(k=4\);
   - the boundary pair \((3,4)\);
   - the type of partial arrows
     $$
     \beta_3, \beta_4.
     $$

3. **Continuation after the threshold**: paragraph `3.3`.
   This part fixes a locally closed picture after the direct bridge.

Connection scheme:

$$
\begin{aligned}
&\text{AMR-SR arithmetic package} \\
&\to \text{partial bridge } (\beta_3, \beta_4) \\
&\to \text{selected core relations} \\
&\to \text{subsequent realisations}.
\end{aligned}
$$

This is the internal structure of AMR-SR only. After the introduction of AMR-DC, it should not be read as the full structure of the whole AMR package.

## 1. AMR-SR as a Scale/Residue Arithmetic Foundation

### 1.1. Basic Object and Standard Normalization

The defining carrier of AMR-SR is

$$
\mathcal{R} = \mathbb{N}_{>0}^2.
$$

The basic AMR-SR object is an integer pair \((a,b)\).

For every pair, introduce the primitive-scale decomposition

$$
(a, b) = g(p, q), \qquad g = \gcd(a, b), \qquad \gcd(p, q) = 1.
$$

Here the primitive direction of the pair is given by the ratio \(p:q\). This defines the standard normalization of every point in the relation plane.

### 1.1.A. Blocks of the Standard Reading

The arithmetic foundation is fixed in four blocks:

- the residual block \(\mathrm{Res}_{\mathrm{sr}}\);
- the metric block: the exact layer \(N_{\mathrm{Eis}}\), \(D_{\mathrm{chroma}}^2\).

### 1.2. Layers, Rays, and the Local Cell

AMR-SR uses two basic decompositions of the plane:

$$
\Sigma_k = \{(a, b) \in \mathcal{R} : |a-b| = k\}, \qquad \rho_{(p, q)} = \{(gp, gq) : g \ge 1 \},
$$

where \((p,q)\) is primitive.

\(\Sigma_k\) gives the external reading of a pair by its distance from the diagonal, while \(\rho_{(p,q)}\) gives the internal reading by primitive direction and scale.

These two readings meet in the local cell

$$
\Sigma_k \cap \rho_{(p, q)}.
$$

If \((p,q)\) is primitive and \(p \neq q\), then

$$
\Sigma_k \cap \rho_{(p, q)} \neq \varnothing
$$

if and only if \(|p-q|\) divides \(k\). In the nonempty case, the local cell consists of exactly one point.

### 1.3. The Residue \(\mathrm{Res}_{\mathrm{sr}}\) and Closed Statements

Introduce the quantities

$$
d_{\mathrm{prim}}(a, b) = |p-q|, \qquad \mathrm{Res}_{\mathrm{sr}}(a, b) = |a-b| - |p-q| = (g-1)|p-q|.
$$

\(\mathrm{Res}_{\mathrm{sr}}\) is an author-defined invariant on standard arithmetic material. It measures the scale excess of the full difference relative to the primitive defect and forms a separate residual block.

Within the AMR-SR arithmetic foundation, the following statements are fixed.

The word "residue" in this document refers to the scalar AMR-SR residue

$$
\mathrm{Res}_{\mathrm{sr}}.
$$

It must not be used as the name of the octahedral or cross-pair relation on divisor carriers, in particular on \(D^\circ(30)\).

### Statement A1. Uniqueness of Primitive-Scale Decomposition

For every pair \((a,b)\), there exists a unique representation

$$
(a, b) = g(p, q),
\quad
g = \gcd(a, b),
\quad
\gcd(p, q) = 1.
$$

**Check.**
Put \(g=\gcd(a,b)\), \(p=a/g\), \(q=b/g\). Then \(\gcd(p,q)=1\), since any common divisor of \(p\) and \(q\) would give a common divisor of \(a\) and \(b\) greater than \(g\).

If

$$
(a,b)=g'(p',q'),
\qquad
\gcd(p',q')=1,
$$

then \(g'\) divides both \(a\) and \(b\). Moreover, all common content of \(a\) and \(b\) has been extracted into \(g'\), since \(p'\) and \(q'\) are coprime. Hence \(g'=\gcd(a,b)=g\), and then \(p'=p\), \(q'=q\).

### Statement A2. Compatibility of Layer and Ray

$$
|a-b| = g|p-q|.
$$

**Check.**
By A1, \(a=gp\), \(b=gq\). Therefore

$$
|a-b|=|gp-gq|=g|p-q|.
$$

### Statement A3. Atomicity of the Local Cell

For a primitive pair \((p,q)\), the intersection

$$
\Sigma_k \cap \rho_{(p, q)}
$$

is nonempty if and only if \(|p-q|\) divides \(k\); in that case it consists of one point.

**Check.**
A point of the ray \(\rho_{(p,q)}\) has the form \((gp,gq)\), where \(g\ge 1\). It belongs to the layer \(\Sigma_k\) if and only if

$$
|gp-gq|=k.
$$

By A2, this is equivalent to

$$
g|p-q|=k.
$$

Thus the intersection is nonempty exactly when \(|p-q|\mid k\), and then the scale is unique:

$$
g=\frac{k}{|p-q|}.
$$

Therefore the local cell contains exactly one point.

$$
|a-b| = |p-q| + \mathrm{Res}_{\mathrm{sr}}(a, b), \qquad \mathrm{Res}_{\mathrm{sr}}(a, b) = (g-1)|p-q|.
$$

**Check of the residual formula.**
By A2,

$$
|a-b|-|p-q|=g|p-q|-|p-q|=(g-1)|p-q|.
$$

In particular, on the first layer \(\Sigma_1\), the residue is always zero.

### Statement A6. Finite Frontier Maximum

On the square

$$
\mathcal{R}_L = \{(a, b) : 1 \le a, b \le L\}
$$

the maximum residue is given by

$$
\mathrm{R}_{\max}(L) = \max_{1 \le g \le L} (g-1)(\lfloor L/g \rfloor - 1).
$$

$$
\mathrm{R}_{\max}(n^2) = (n-1)^2.
$$

**Check.**
For a fixed scale \(g\) inside the square \(\mathcal R_L\), the primitive coordinates satisfy

$$
1\le p,q\le \lfloor L/g\rfloor.
$$

The largest possible value of \(|p-q|\) is \(\lfloor L/g\rfloor-1\). Therefore, for this \(g\), the maximum residue is

$$
(g-1)(\lfloor L/g\rfloor-1).
$$

Maximizing over all \(1\le g\le L\) gives the stated formula for \(\mathrm R_{\max}(L)\).

If \(L=n^2\), then at \(g=n\) and \((p,q)=(1,n)\) one obtains

$$
(n-1)(n-1)=(n-1)^2.
$$

For every \(g\), the product

$$
(g-1)(\lfloor n^2/g\rfloor-1)
$$

does not exceed \((n-1)^2\). Indeed,

$$
(g-1)(\lfloor n^2/g\rfloor-1)
\le
(g-1)(n^2/g-1)
=
n^2-g-\frac{n^2}{g}+1.
$$

By the inequality \(g+n^2/g\ge 2n\), we obtain

$$
n^2-g-\frac{n^2}{g}+1\le n^2-2n+1=(n-1)^2.
$$

Hence

$$
\mathrm R_{\max}(n^2)=(n-1)^2.
$$

### Statement A8. Metric Layer

$$
N_{\mathrm{Eis}}(p, q) = p^2 - pq + q^2.
$$

$$
D_{\mathrm{chroma}}^2 = \frac{2}{3} g^2 N_{\mathrm{Eis}}(p, q).
$$

This layer fixes the natural metric mass of a direction inside the chosen sector.

**Check.**
In the chosen sector normalization, the two generators have Gram matrix

$$
G=
\begin{pmatrix}
2/3 & -1/3\\
-1/3 & 2/3
\end{pmatrix}.
$$

Therefore, for the primitive direction \((p,q)\),

$$
(p,q)G(p,q)^{\mathsf T}
=
\frac23 p^2-\frac23 pq+\frac23 q^2
=
\frac23 N_{\mathrm{Eis}}(p,q).
$$

Multiplying the direction by scale \(g\) multiplies the squared length by \(g^2\). Hence

$$
D_{\mathrm{chroma}}^2=\frac23 g^2N_{\mathrm{Eis}}(p,q).
$$

For the bridge and the frontier layer, minimal finite fragments of the plane \(\mathcal{R}\) are used.

1. Local cell

$$
\Sigma_k \cap \rho_{(p, q)}
$$

if nonempty, consists of one point.

2. Finite square

$$
\mathcal{R}_L = \{(a, b) : 1 \le a, b \le L\}.
$$

3. Frontier family

$$
\mathcal{F}_L = \{(a, b) \in \mathcal{R}_L : \mathrm{Res}_{\mathrm{sr}}(a, b) = \mathrm{R}_{\max}(L)\}.
$$

4. Frontier signature package

The finite package \(W_L\) serves as material for subsequent compression.

Minimal finite packages enter `03` as a preparatory layer between the arithmetic foundation and continuation procedures.

### 1.5. Admissible External Contexts and Boundaries

Only narrow external readings are admissible in this section:

- primitive reduction and visible lattice points;
- rational directions through a reduced fraction \(p/q\);
- narrow toric language of a primitive ray generator;
- circulant context through \(\gcd\);
- preservation of primitiveness under \(\mathrm{SL}(2,\mathbb{Z})\).

The main theorem of the section does not include:

- spectral reading of \(\operatorname{Res}_{\mathrm{sr}}\);
- modular reading of \(\operatorname{Res}_{\mathrm{sr}}\);
- full identity with \(\mathrm{SL}(2,\mathbb{Z})\)-orbits;
- strong toric interpretations.

They are used only as external contexts.

### 1.6. Colorimetric Layer

The colorimetric layer is a separate exact realisation of the already constructed six-point layer.

Fix the following:

- the chromatic six-point shell and the cycle \(C_6\) have an exact model in the colour body;
- the local sector form \((a,b)=g(p,q)\) and the metric law
  $$
  D^2_{\operatorname{chroma}} = \frac23 g^2 N_{\operatorname{Eis}}(p,q)
  $$
  are compatible with the colour reading;
- \(\mathrm{AMR\text{-}SR}\) is read as local arithmetic inside the chosen sector and does not generate the whole colour body;
- detailed colorimetry is moved to a separate dossier.

Its role:

- fix the metric block;
- clarify the place of \(\mathrm{AMR\text{-}SR}\) inside the realised geometry;
- give an exact realisation of the already found structure, without rewriting its origin.

The local compatibility of this layer with the minimal bridge
\(\text{core} \to \mathrm{AMR\text{-}SR} \to \text{colorimetry}\)
is checked by the function

```python
_assert_core_amr_color_integration()
```

from `DOT_AMR_verifier.py`
together with the strict-core check

```python
shell_face_kuhn_transition_test()
```

from `DOT_Core_verifier.py`.

## 2. Frontier Layer and Branching

### 2.1. Basic Frontier Problem

On the finite square

$$
\mathcal{R}_L = \{(a, b) \in \mathbb{N}_{>0}^2 : 1 \le a, b \le L\}
$$

we study the maximum of

$$
\mathrm{Res}_{\mathrm{sr}}(a, b) = (g-1)|p-q|.
$$

Main question:

$$
\text{where on } \mathcal{R}_L \text{ is the maximum of } \operatorname{Res}_{\mathrm{sr}}\text{ attained?}
$$

### Statement B1. Maximum at Fixed \(g\)

If

$$
N_g = \lfloor L/g \rfloor,
$$

then the maximal residue among pairs with a given common multiple \(g\) is

$$
\mathrm{R}_L(g) = (g-1)(\lfloor L/g \rfloor - 1).
$$

Extreme pairs may be taken in the form

$$
(g, g\lfloor L/g \rfloor), \qquad (g\lfloor L/g \rfloor, g).
$$

**Check.** At fixed \(g\), we have \(a=gp\), \(b=gq\), and

$$
1\le p,q\le N_g=\lfloor L/g \rfloor.
$$

The residue is

$$
\mathrm{Res}_{\mathrm{sr}}=(g-1)|p-q|.
$$

The maximum value of \(|p-q|\) on the interval \(\{1,\ldots,N_g\}\) is \(N_g-1\), attained at \((1,N_g)\) and \((N_g,1)\). These pairs are primitive because \(\gcd(1,N_g)=1\). Therefore the maximum at this \(g\) is

$$
(g-1)(N_g-1).
$$

### Statement B2. Exact Frontier Formula

We have

$$
\mathrm{R}_{\max}(L) = \max_{1 \le g \le L} \mathrm{R}_L(g).
$$

Thus the two-dimensional extremal problem reduces to one-dimensional maximization over the scale \(g\).

**Check.** Each pair \((a,b)\in\mathcal R_L\) has the unique scale \(g=\gcd(a,b)\). By Statement B1, the maximum inside each fixed scale layer is \(\mathrm R_L(g)\). The full maximum on the finite square is obtained by maximizing these values over all \(g\in\{1,\ldots,L\}\).

### Statement B3. Square Special Case

If \(L = n^2\), then

$$
\mathrm{R}_{\max}(n^2) = (n-1)^2.
$$

In this case the maximum is attained at \(g = n\).

**Check.** For \(L=n^2\) and \(g=n\), formula B1 gives

$$
\mathrm R_{n^2}(n)=(n-1)(n-1)=(n-1)^2.
$$

For every \(g\), we have

$$
\lfloor n^2/g\rfloor-1\le n^2/g-1,
$$

and hence

$$
\mathrm R_{n^2}(g)\le (g-1)(n^2/g-1)
=n^2-g-\frac{n^2}{g}+1.
$$

The right-hand side as a function of real \(g>0\) attains its maximum at \(g=n\), with value \((n-1)^2\). Therefore the discrete maximum also does not exceed \((n-1)^2\), and the value \(g=n\) attains it.

### Statement B4. Frontier Witnesses

For a scale \(g\) at which the maximum is attained, frontier witnesses have normal form

$$
W^-(g) = \bigl( <, g(\lfloor L/g \rfloor-1), g, 1:\lfloor L/g \rfloor, (g-1)(\lfloor L/g \rfloor-1) \bigr),
$$

$$
W^+(g) = \bigl( >, g(\lfloor L/g \rfloor-1), g, \lfloor L/g \rfloor:1, (g-1)(\lfloor L/g \rfloor-1) \bigr).
$$

It follows that:

- a diagonal witness does not appear on the frontier when \(L > 1\);
- the frontier lies on the extreme primitive rays;
- coordinate-swap symmetry pairs the witnesses \(W^-(g) \leftrightarrow W^+(g)\).

**Check.** The normal form is obtained from the extreme primitive pairs \((1,N_g)\) and \((N_g,1)\) in the proof of B1, where \(N_g=\lfloor L/g\rfloor\). For \(L>1\), the value \(N_g>1\) on every nontrivial frontier, so a diagonal pair \((p,p)\) does not attain the maximum. Coordinate swap sends \((1,N_g)\) to \((N_g,1)\) and therefore pairs the two witnesses.

### 2.2. Family of Maximizing Scales

For each \(L\), define the set of maximizing scales

$$
G_{\max}(L) = \{g \in \{1, \dots, L\} : \mathrm{R}_L(g) = \mathrm{R}_{\max}(L)\}.
$$

Hence:

- if \(|G_{\max}(L)| = 1\), the frontier family is unique;
- if \(|G_{\max}(L)| > 1\), the frontier splits into several branches.

Thus the frontier is read not only as the number \(\mathrm{R}_{\max}(L)\), but also as a small finite structure:

- numerical frontier;
- family of maximizing scales;
- frontier witnesses.

### 2.3. Computational Taxonomy of Branching

Over the theorem-level frontier, a computational classification by the cardinality

$$
m(L) = |G_{\max}(L)|
$$

is used.

Types:

- single frontier;
- two-branch frontier;
- three-branch frontier;
- multibranch frontier.

Only verified observations are fixed:

- on small and medium ranges, computation shows stable branching patterns;
- values of \(L\) close to squares often produce branch coarsening;
- many composite \(L\) give two-, three-, or multibranch pictures.

A full classification of all multiplicity regimes is not proved here.

The geometric vocabulary of the frontier, minimal carrier images, and closure language are used as an explanatory layer over the formulas \(\mathrm{R}_L(g), \mathrm{R}_{\max}(L)\), and \(G_{\max}(L)\).

The frontier layer is a superstructure over the residual block \(\operatorname{Res}_{\mathrm{sr}}\).

### 2.4. Sublayers of the Frontier Layer

Strict sublayer:

- formulas \(\mathrm{R}_L(g)\) and \(\mathrm{R}_{\max}(L)\);
- square special case;
- frontier witness;
- family \(G_{\max}(L)\).

Computational sublayer:

- taxonomy by \(m(L) = |G_{\max}(L)|\);
- branching types: single, two-branch, three-branch, multibranch;
- carrier vocabulary and closure language.

Status formula:

- theorem-level frontier is fixed;
- computational branching taxonomy is useful as verification material;
- full classification of multiplicity regimes remains a separate task.

## 3. Minimal Bridge into the Core

Bridge scheme:

$$
\mathrm{AMR\text{-}SR} \to \text{observable finite signature} \to \text{selected core relations}.
$$

Configuration:

- \(\mathrm{AMR\text{-}SR}\) functions here as local sector arithmetic;
- the strict core is taken in shell order
  \(8 \to 6 \to C_6 \to (R_1, R_2, R_3) \to R_1 \cup R_2\);
- the bridge fixes the first coarse interface between layers.

Chain for \(k = 3\):

$$
\text{AMR-SR: nontrivial exact signature} \to \text{balanced finite signature} \to (R_1, R_2).
$$

Target object: the supported pair \((R_1, R_2)\).

For \(k = 4\):

$$
\text{AMR-SR: axial fixed signature} \to R_3.
$$

Target object: the axial layer \(R_3\).

### Statement C3. Decomposition of the Boundary Pair \((3,4)\)

The pair \((3,4)\) falls onto the internal decomposition of the finite core into supported and axial parts:

\(k=3\) corresponds to the supported pair \((R_1,R_2)\), while \(k=4\) corresponds to the axial layer \(R_3\).

### 3.1. Bridge Restrictions

Asserted points:

- \(3 \to (R_1, R_2)\);
- \(4 \to R_3\);
- \(2\) gives no separate core relation;
- for \(k \ge 5\), no general transition to core relations is defined.

These points do not imply:

- a rule \(k \to R_k\);
- a full functor;
- identification of \(\mathrm{AMR\text{-}SR}\) with the strict core;
- a general bridge for the tail after the threshold;
- identity of mechanisms.

\(\mathrm{AMR\text{-}SR}\) does not autonomously generate:

- the six-point shell;
- the cycle \(C_6\);
- the octahedral surface;
- the colour body.

This list exhausts the minimal bridge fixed in the text.

### 3.2. Short Form

$$
\begin{aligned}
3 &\to (R_1, R_2) \\
4 &\to R_3 \\
2 &\to \text{no separate core relation} \\
k \ge 5 &\to \text{no general transition defined}
\end{aligned}
$$

Admissible conclusions:

- a partial finite interface \(\mathrm{AMR\text{-}SR} \to \text{core}\) is fixed;
- it distinguishes the supported positive side and the axial blocked layer;
- it is not a full functor or a general rule \(k \to R_k\).

### 3.2.A. Types of AMR-SR Transitions

The transitions have the status of partial typed bridge arrows:

$$
\beta_3 \colon \mathrm{AMR\text{-}SR}_{k=3} \to (R_1, R_2), \qquad \beta_4 \colon \mathrm{AMR\text{-}SR}_{k=4} \to R_3.
$$

Properties of \(\beta\):

- the signature lands in a selected core relation;
- the arrow is not a generation of a carrier, a shell realisation, or an operator lift.

These arrows are AMR-SR bridge arrows, not AMR-DC divisor-carrier theorems.

### Summary 3.2.B [P|cat]. Categorical Status of the AMR-SR Line

1. AMR-SR is not part of the strict core.
2. The links have the status of partial typed bridge arrows:
   $$
   \beta_3 \colon \mathrm{AMR\text{-}SR}_{k=3} \to (R_1, R_2), \qquad \beta_4 \colon \mathrm{AMR\text{-}SR}_{k=4} \to R_3.
   $$
3. The arrows \(\beta\) are not a shell realisation, operator lift, or full functor.
4. The shell, colour, and operator layers are realisations of an already found structure, not a direct derivation from \(\mathrm{AMR\text{-}SR}\).
5. Adjacent arrow typing is imported from `02A` and `02B`.

The line \(\mathrm{AMR\text{-}SR} \to \text{core}\) has the status of a partial typed bridge. The remaining arrow statuses of the corpus are fixed in `02B`.

### 3.3. Continuation After the Threshold: Minimal Extended AMR-SR

The status of this section is lower than that of statements C1-C3 and sections 3.1-3.2:

- it does not extend the minimal bridge to a theorem-level rule of the form \(k \to \text{core}\);
- it does not rise into the strict core;
- it defines a locally closed picture after the direct bridge within the current formalism.
- it is not AMR-DC, not divisor-carrier theory, and not a theorem about \(D(N)\).

The direct shell bridge closes at \(k = 3, 4\). Beyond this threshold, the shell tail gives no new direct landing in the core, but the frontier layer remains nonempty and has its own exact structure. This layer is called **extended AMR-SR after the threshold**.

Two exact towers (\(P_n\) and \(A_n\)) start at \(n = 2\):

- \(P_2 = 2 \cdot 3 = 6\): paired witnesses with shell levels \(4\) and \(3\);
- \(A_2 = 2^2 = 4\): axial witness with shell level \(2\).

The case \(n = 2\) coincides with the boundary node of the direct bridge:

- \(3 \to (R_1, R_2)\)
- \(4 \to R_3\)

and serves as the initial boundary point.

For \(n \ge 3\), both towers give proper carriers after the threshold:

- \(P_n\): shell levels \(n^2\) and \(n^2 - 1\) (already \(\ge 8\) for \(n = 3\));
- \(A_n\): shell level \(n(n-1)\) (already \(\ge 6\) for \(n = 3\)).

Boundary distinction: \(n = 2\) is the initial boundary point, while \(n \ge 3\) is the post-threshold zone.

#### 3.3.2. Two Exact Towers After the Threshold

For \(n \ge 2\), define two families of limits:

$$
P_n = n(n+1) \quad (\text{paired tower}), \qquad A_n = n^2 \quad (\text{axial tower}).
$$

##### Paired Tower \(P_n\)

At the limit \(P_n\), the frontier gives a reciprocal pair, i.e. two exact witnesses.

Outer branch:

$$
O_n \colon g = n, \quad \text{shell} = n^2, \quad \text{ray} = 1:(n+1), \quad \text{target} = R_1, \quad \text{type} = \text{between}.
$$

Inner branch:

$$
I_n \colon g = n+1, \quad \text{shell} = n^2 - 1, \quad \text{ray} = 1:n, \quad \text{target} = R_2, \quad \text{type} = \text{inside}.
$$

Both branches have the same frontier residue:

$$
\mathrm{Res}_{\mathrm{pair}}(n) = n(n-1).
$$

In the language of the current formalism, this means:

$$
\operatorname{frontier\_signature}(P_n)
\to \text{balanced supported pair}.
$$

##### Axial Tower \(A_n\)

At the limit \(A_n = n^2\), the frontier gives an axial fixed signature:

$$
X_n \colon g = n, \quad \text{shell} = n(n-1), \quad \text{ray} = 1:n, \quad \text{target} = R_3, \quad \text{type} = \text{axial}.
$$

In the language of the current formalism:

$$
\operatorname{frontier\_signature}(A_n)
\to \text{axial layer}.
$$

Thus in the post-threshold zone there are two exact sources:

- paired carriers directed toward \((R_1,R_2)\);
- axial carriers directed toward \(R_3\).

#### 3.3.3. Current Completion Scheme \(\mathfrak C_{\mathrm{AMR\text{-}SR}}\)

The public theory uses the local operator

$$
\operatorname{frontier\_completion\_signature}(\text{paired limit, axial limit})
$$

from `DOT_AMR_verifier.py`.

Its status in the current version is the following:

The scheme is an exact completion in the current local formalism and is not asserted as a theorem-level law of the entire geometry after the threshold; it acts on admissible paired and axial carriers.

The scheme is defined only under three conditions:

1. the paired limit has reciprocal form directed toward the core;
2. the paired limit gives a definite reciprocal decomposition;
3. the axial limit has a form directed toward the core.

If these conditions hold, the same fixed bridge profile is returned:

$$
\begin{aligned}
\operatorname{relation\_counts} &= \{R_1: 6, R_2: 6, R_3: 3\} \\
\operatorname{shared\_chambers} &= \{R_1: 2, R_2: 2, R_3: 0\} \\
\operatorname{shell\_types} &= \{R_1: \text{between}, R_2: \text{inside}, R_3: \text{axial}\} \\
\operatorname{completion\_mode} &= \text{reciprocal plus axial}
\end{aligned}
$$

The operator uniformly assembles paired and axial witnesses into the already known coarse profile of the core.

Local machine verification of this completion block is performed by the functions

$$
\begin{gathered}
\operatorname{frontier\_completion\_signature}() \\
\operatorname{frontier\_reciprocal\_split\_signature}() \\
\operatorname{frontier\_core\_facing\_signature}()
\end{gathered}
$$

and the summary check

$$
\operatorname{\_assert\_post\_break\_beta\_layer}()
$$

from `DOT_AMR_verifier.py`.

#### 3.3.4. Synchronous Diagonal and the Operator \(\Omega_{\operatorname{sync}}\)

Inside the two-input completion scheme, an exact sublayer with the same \(n\) is isolated.

For the pair with the same \(n\),

$$
(P_n, A_n) = (n(n+1), n^2)
$$

four exact identities hold.

##### 1. The outer paired shell equals the axial limit

$$
\operatorname{shell}(O_n) = n^2 = A_n.
$$

##### 2. The paired residue equals the axial shell

$$
\mathrm{Res}_{\mathrm{pair}}(n) = n(n-1) = \operatorname{shell}(X_n).
$$

##### 3. The outer gcd equals the axial gcd

$$
\gcd(O_n) = n = \gcd(X_n).
$$

##### 4. The inner ray equals the axial ray

$$
\operatorname{ray}(I_n) = 1:n = \operatorname{ray}(X_n).
$$

These coincidences isolate not an arbitrary pair of inputs, but the synchronous diagonal:

$$
\mathfrak{D}_{\operatorname{sync}} = \{ (P_n, A_n) : n \ge 3 \}.
$$

Moreover, it is uniquely selected:

- the equality \(\operatorname{shell}(O_n) = A_m\) is possible only when \(n = m\);
- the equality \(\operatorname{Res}_{\mathrm{pair}}(n) = \operatorname{shell}(X_m)\) is possible only when \(n = m\);
- the equality \(\gcd(O_n) = \gcd(X_m)\) is possible only when \(n = m\);
- the equality \(\operatorname{ray}(I_n) = \operatorname{ray}(X_m)\) is possible only when \(n = m\).

Therefore, inside the broad completion domain, the first exact one-parameter operator after the threshold appears:

$$
\Omega_{\mathrm{sync}}(n) = \mathfrak{C}_{\mathrm{AMR\text{-}SR}}(P_n, A_n), \qquad n \ge 3.
$$

- this is an exact derived operator of the current formalism;
- it is not a theorem-level operator of the whole post-threshold zone;
- it selects a fixed synchronous subfamily inside extended \(\mathrm{AMR\text{-}SR}\).

#### 3.3.5. Carrier Plateaus and the Broad Admissible Lattice

The objects of the post-threshold layer are stable carrier plateaus, not individual values of \(L\).

##### Paired Plateaus

Different values of \(L\) may realise the same paired carrier.

For example:

- \(L = 12, 13\) realise the same package \(((3, 4), (4, 3))\);
- \(L = 30, 31\) realise the same package \(((5, 6), (6, 5))\);
- \(L = 56, 57, 58, 59\) realise the same package \(((7, 8), (8, 7))\).

Inside one such plateau, the following are preserved:

- factors;
- witness families;
- direction class toward the core;
- reciprocal decomposition.

##### Axial Plateaus

Similarly, different values of \(L\) may realise the same axial carrier.

For example:

- \(L = 36, 37, 38, 39\) realise the singleton package \(((6,6),)\);
- \(L = 121, 122, 123, 124, 125\) realise the singleton package \(((11,11),)\).

Inside an axial plateau, the following are preserved:

- factors;
- witness family;
- axial direction class toward the core;
- reduced axial status.

Hence the important separation:

- \(L\) is the numerical input of the frontier problem;
- a plateau is a class of \(L\)-values realising the same carrier;
- completion acts on carriers, not on an arbitrary set of individual \(L\)-values.

Therefore the broad admissible domain is organized as

$$
\{\text{paired plateaus}\} \times \{\text{axial plateaus}\}.
$$

Inside this broad admissible lattice, the synchronous diagonal \(\mathfrak{D}_{\operatorname{sync}}\) is a selected exact subfamily, not the whole product.

#### 3.3.6. Off-Diagonal Geometry of Mismatch

Outside the synchronous diagonal, no second exact coupling law is fixed. Nevertheless, the off-diagonal part has its own exact structure.

Below, take only the exact sublattice of the two towers:

$$
(P_n, A_m) = (n(n+1), m^2), \quad n, m \ge 2.
$$

On it, introduce mismatch operators:

$$
d(n, m) = n - m, \qquad \Delta_L = n^2 - m^2, \qquad \Delta_X = n(n-1) - m(m-1), \qquad \Delta_g = n - m, \qquad \Delta_{\mathrm{ray}} = n - m.
$$

This gives the exact formulas:

$$
\Delta_L = d(n, m)(n+m), \qquad \Delta_X = d(n, m)(n+m-1), \qquad \Delta_L = \Delta_X + \Delta_g.
$$

All four mismatch quantities vanish simultaneously if and only if \(n = m\).

For \(n \neq m\), they always have the same sign, so the off-diagonal part automatically splits into two oriented sides:

- \(n > m\): paired predominance;
- \(n < m\): axial predominance.

The main parameter here is

$$
d = n - m.
$$

Fixed \(d\) defines a strip around the diagonal:

- \(d = 0\): synchronous diagonal;
- \(d = \pm 1\): first mismatch strip;
- \(d = \pm 2, \pm 3, \dots\): increasingly distant deviation layers.

The off-diagonal part of the exact two-tower lattice carries not a second coupling law, but a law of deviation from the synchronous diagonal.

#### 3.3.7. Boundaries of the Claims

This subsection fixes the following.

Exact:

- the initial boundary point \(n = 2\) is already visible inside the pair \((3,4)\);
- for \(n \ge 3\), the paired tower and the axial tower give post-threshold carriers;
- completion is exactly defined on admissible paired and axial carriers in the current formalism;
- the synchronous diagonal gives the one-parameter derived operator \(\Omega_{\operatorname{sync}}\);
- the broad admissible domain is organized through plateaus;
- the off-diagonal part of the exact two-tower lattice carries exact mismatch geometry.

Fixed boundaries:

- classification of all admissible paired and axial combinations is not proved;
- the geometric meaning of only equal-\(n\) combinations is not proved;
- no general functor \(\mathrm{AMR\text{-}SR} \to \text{core}\) is built after the threshold;
- no lift of \(\Omega_{\operatorname{sync}}\) into the strict core is built;
- a full theorem for the whole extension zone remains a separate task.

#### 3.3.8. Local Verification

This layer is accompanied by local verification scripts in the same folder:

- `DOT_AMR_verifier.py`: functions `run_self_tests()`, `run_core_check()`, `run_full_check()`, `_assert_post_break_beta_layer()`, `_assert_core_amr_color_integration()`;
- `DOT_Core_verifier.py`: function `shell_face_kuhn_transition_test()`.

Together, these two scripts confirm:

- the initial boundary point \(n = 2\) and the transition to the post-threshold zone \(n \ge 3\);
- the exact paired and axial towers;
- completion on admissible carriers;
- the synchronous diagonal and the operator \(\Omega_{\operatorname{sync}}\);
- the plateau structure of the broad admissible domain;
- the mismatch geometry of the off-diagonal part of the exact two-tower lattice.

## 4. Final Status of AMR-SR

In its shortest form, `03A` asserts the following.

1. AMR-SR defines scale/residue arithmetic on the carrier

   $$
   \mathcal R=\mathbb N_{>0}^2.
   $$

2. The basic decomposition is

   $$
   (a,b)=g(p,q),
   \qquad
   g=\gcd(a,b),
   \qquad
   \gcd(p,q)=1.
   $$

3. The basic scalar residue is

   $$
   \mathrm{Res}_{\mathrm{sr}}=(g-1)|p-q|.
   $$

4. AMR-SR yields only a partial typed bridge:

   $$
   \beta_3:\mathrm{AMR\text{-}SR}_{k=3}\to(R_1,R_2),
   $$

   $$
   \beta_4:\mathrm{AMR\text{-}SR}_{k=4}\to R_3.
   $$

5. For \(k=2\) there is an exception, and for \(k\ge5\) no general bridge is asserted.

6. AMR-SR is not divisor-carrier theory.

7. The divisor-carrier branch is developed in `03B_AMR_Divisor_Carrier_and_Chain_Extension.md`.
