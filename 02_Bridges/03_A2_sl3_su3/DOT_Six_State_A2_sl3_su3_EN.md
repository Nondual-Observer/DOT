# A Six-State Binary Model for the Root Datum of Type $A_2$, $\mathfrak{sl}_3(\mathbb C)$, and the Compact Form $\mathfrak{su}(3)$

## Status

`[D]` Proven in the finite setting described below.

## Package note

This folder is intended to work as a small self-contained GitHub package.

Files:

- `DOT_Six_State_A2_sl3_su3_EN.md` — the English mathematical note;
- Russian mathematical note: paired RU version in the same folder;
- `verify_six_state_a2_sl3_su3.py` — the local verification script.

Quick run:

```bash
python3 verify_six_state_a2_sl3_su3.py
```

Expected output:

```text
PASS: six-state A2/sl3(C)/su3 standalone checks
```

## Introduction: purpose of this bridge

This note is an algebraic bridge from the six-state finite core of DOT to a standard object in Lie theory.

The source side is finite. It consists of the six admissible binary states

$$
X=\{100,010,001,011,101,110\},
$$

the two-triangle relation

$$
(X,R_2)\cong K_3\\sqcup K_3,
$$

and the complement involution

$$
c(x)=1-x.
$$

The target side is algebraic. After the standard linear realization of one triangle as the three coordinate weights $e_1,e_2,e_3$, the edge differences give the root system of type $A_2$. The two triangles then read as the weight diagrams of the fundamental module and its dual:

$$
\mathbf 3\oplus\overline{\mathbf 3}.
$$

From this root datum one obtains the standard Chevalley realization of $\mathfrak{sl}_3(\mathbb C)$. After choosing the standard Hermitian form, the compact real form $\mathfrak{su}(3)$ is recovered in the usual Lie-theoretic sense.

The bridge records the following correspondence: the same six-state datum that appears in the strict finite core admits a precise algebraic reading by two triangles, a complement exchange, an $A_2$ root datum, and the standard $3\oplus\bar 3$ representation package. In this role, a bridge adds no new native objects to the strict finite core. It gives a controlled external realization of already constructed finite data.

The boundary is part of the statement. The finite datum $(X,$R_2$,c)$ does not contain a physical gauge theory, particle dynamics, or the Lie group $SU(3)$ as a geometric object. Those require additional structures. This note proves only the finite-to-algebraic reconstruction described below.

## Abstract

We consider the six-point subset

$$
X=\{100,010,001,011,101,110\}\subset \{0,1\}^3
$$

equipped with:

1. the involution
   $$
c(x)=1-x,
$$

   where subtraction is taken coordinatewise;
2. the relation $R_2$ consisting of the edges inside the two triples
   $$
\{100,010,001\},\qquad \{011,101,110\}.
$$

We prove that this finite combinatorial datum determines a canonical combinatorial model of:

1. the root system of type $A_2$;
2. the complex Lie algebra $\mathfrak{sl}_3(\mathbb C)$;
3. the six-state module $\mathbf 3\oplus \overline{\mathbf 3}$;
4. the compact real form $\mathfrak{su}(3)$ after choosing the standard Hermitian form.

More precisely:

- the passage from the finite datum to the root datum is combinatorial;
- the passage from the root datum to $\mathfrak{sl}_3(\mathbb C)$ uses the standard linear
  realization and the standard Chevalley matrix model;
- the passage from $\mathfrak{sl}_3(\mathbb C)$ to $\mathfrak{su}(3)$ uses the standard
  Hermitian form.

This note does **not** claim that the finite datum by itself contains the full Lie group
$SU(3)$ as a geometric object, nor any gauge-theoretic or physical dynamics.

The six-state datum is not introduced here as an ad hoc graph chosen to fit the Lie data.
Its original provenance is the strict core of DOT, where the same six states carry the
carrier graph $K_{2,2,2}$ together with the primitive cycle $C_6$. In the present note,
however, that provenance is used only as motivation: the reconstruction below starts from
the finite six-state combinatorial datum itself.

In DOT language, this is the strict finite nucleus of the theory. In the present note,
the same object is read externally in standard mathematical language as the finite datum
$(X,$R_2$,c)$.

So the claim of this note is intentionally limited:

- not an intrinsic generation of $\mathfrak{sl}_3(\mathbb C)$ from pure combinatorics alone;
- but a canonical finite combinatorial model of the root datum of type $A_2$, together
  with its standard Lie-theoretic realization.

---

## 1. Input datum

Write

$$
X_1=\{100,010,001\},\qquad X_2=\{011,101,110\}.
$$

The relation $R_2$ is the union of the two triangles on $X_1$ and $X_2$:

$$
R_2 = K_3(X_1)\ \sqcup\ K_3(X_2).
$$

The involution $c(x)=1-x$ exchanges the two triangles:

$$
100\leftrightarrow 011,\qquad 010\leftrightarrow 101,\qquad 001\leftrightarrow 110.
$$

We use the standard embedding

$$
100\mapsto e_1,\qquad 010\mapsto e_2,\qquad 001\mapsto e_3
$$

into $\mathbb R^3$, where $e_1,e_2,e_3$ are the standard basis vectors.
This is a canonical linear realization of the lower triangle, not an additional theorem
derived from the bare combinatorics. The reconstruction of the root datum and the Lie
algebra is understood relative to this standard realization.

---

## 2. Weight splitting and the module $\mathbf 3\oplus \overline{\mathbf 3}$

The set $X$ splits into two 3-point sectors:

$$
X=X_1\sqcup X_2.
$$

We interpret:

- $X_1$ as the weight diagram of the fundamental representation $\mathbf 3$;
- $X_2$ as the weight diagram of the dual representation $\overline{\mathbf 3}$;
- $c$ as the discrete exchange
  $$
\mathbf 3 \leftrightarrow \overline{\mathbf 3}.
$$

Thus the six-point set carries the combinatorial shape of

$$
\mathbf 3 \oplus \overline{\mathbf 3}.
$$

At this stage no Lie algebra has yet been reconstructed; only the weight splitting and
the involutive exchange between the two sectors have been fixed.

---

## 3. Root extraction from the triangle relation

Inside the lower triangle $X_1=\{e_1,e_2,e_3\}$, the oriented edges have directions

$$
e_2-e_1,\qquad e_3-e_2,\qquad e_3-e_1.
$$

Set

$$
\alpha_1=e_1-e_2,\qquad \alpha_2=e_2-e_3.
$$

Then

$$
\alpha_1+\alpha_2=e_1-e_3.
$$

Hence the oriented edges of the triangle realize the positive roots

$$
\alpha_1,\qquad \alpha_2,\qquad \alpha_1+\alpha_2,
$$

and, after reversing orientation, the full root system

$$
\Delta(A_2)=\{\pm\alpha_1,\pm\alpha_2,\pm(\alpha_1+\alpha_2)\}.
$$

This is the standard root system of type $A_2$ in the plane

$$
\{x_1+x_2+x_3=0\}\subset \mathbb R^3.
$$

`∎`

---

## 4. Cartan matrix

With the standard Euclidean inner product,

$$
\langle\alpha_1,\alpha_1\rangle=2,\qquad
\langle\alpha_2,\alpha_2\rangle=2,\qquad
\langle\alpha_1,\alpha_2\rangle=-1.
$$

Therefore the Cartan matrix is

$$
A_{ij}=\frac{2\langle\alpha_i,\alpha_j\rangle}{\langle\alpha_j,\alpha_j\rangle}
=
\begin{pmatrix}
2 & -1\\
-1 & 2
\end{pmatrix}.
$$

This is the Cartan matrix of finite type $A_2$.

`∎`

---

## 5. Chevalley realization and reconstruction of $\mathfrak{sl}_3(\mathbb C)$

Let

$$
V=\mathbb C^3
$$

with basis vectors

$$
v_1=|100\rangle,\qquad v_2=|010\rangle,\qquad v_3=|001\rangle.
$$

Let $E_{ij}$ denote the standard matrix units. Define

$$
e_1=E_{12},\qquad e_2=E_{23},\qquad
f_1=E_{21},\qquad f_2=E_{32},
$$

$$
h_1=[e_1,f_1]=\mathrm{diag}(1,-1,0),\qquad
h_2=[e_2,f_2]=\mathrm{diag}(0,1,-1).
$$

Direct computation gives

$$
[h_i,h_j]=0,
$$

$$
[h_i,e_j]=A_{ij}e_j,\qquad
[h_i,f_j]=-A_{ij}f_j,
$$

$$
[e_i,f_j]=\delta_{ij}h_i,
$$

and the Serre relations

$$
(\mathrm{ad}e_1)^2e_2=0,\qquad
(\mathrm{ad}e_2)^2e_1=0,
$$

$$
(\mathrm{ad}f_1)^2f_2=0,\qquad
(\mathrm{ad}f_2)^2f_1=0.
$$

Further,

$$
e_3=[e_1,e_2]=E_{13},\qquad
f_3=[f_2,f_1]=E_{31}.
$$

The eight matrices

$$
E_{12},E_{23},E_{13},E_{21},E_{32},E_{31},h_1,h_2
$$

form a basis of the trace-zero matrix algebra. Hence the Lie algebra generated by the
Chevalley data is exactly

$$
\mathfrak{sl}_3(\mathbb C).
$$

By the Chevalley-Serre theorem, this is the unique complex semisimple Lie algebra of
type $A_2$.

`∎`

---

## 6. Action on the six-state module

Set

$$
W=V\oplus V^\ast
$$

with basis

$$
v_1=|100\rangle,\quad v_2=|010\rangle,\quad v_3=|001\rangle,
$$

$$
w_1=|011\rangle,\quad w_2=|101\rangle,\quad w_3=|110\rangle.
$$

Define the block representation

$$
\rho(X)=X\oplus(-X^\top),\qquad X\in\mathfrak{sl}_3(\mathbb C).
$$

Then:

1. $V$ carries the fundamental module $\mathbf 3$;
2. $V^\ast$ carries the dual module $\overline{\mathbf 3}$;
3. the six basis states of $W$ identify with the six binary states in $X$;
4. each root operator moves along an edge of one of the two triangles.

For example,

$$
e_1:v_2\mapsto v_1,\qquad e_2:v_3\mapsto v_2,\qquad e_3:v_3\mapsto v_1,
$$

while on the dual sector,

$$
e_1:w_1\mapsto -w_2,\qquad e_2:w_2\mapsto -w_3,\qquad e_3:w_1\mapsto -w_3.
$$

Thus the six-state combinatorial model realizes precisely

$$
\mathbf 3\oplus\overline{\mathbf 3}.
$$

In particular, this is **not** a claim that the six-state space carries a new irreducible
6-dimensional highest-weight module. The representation is explicitly reducible: it is
the direct sum of the two invariant 3-dimensional sectors $V$ and $V^\ast$.

The involution $c(x)=1-x$ exchanges the two summands and acts as a discrete conjugation
between the fundamental and dual sectors.

`∎`

---

## 7. The compact real form $\mathfrak{su}(3)$

Up to this point we have reconstructed only the complex Lie algebra

$$
\mathfrak{sl}_3(\mathbb C).
$$

To obtain the compact real form, endow $V=\mathbb C^3$ with the standard Hermitian form
for which $v_1,v_2,v_3$ are orthonormal. Then

$$
\mathfrak{su}(3)=\{X\in \mathfrak{sl}_3(\mathbb C): X^\ast=-X\}.
$$

A standard real basis is

$$
ih_1,\quad ih_2,
$$

$$
E_{12}-E_{21},\quad i(E_{12}+E_{21}),
$$

$$
E_{23}-E_{32},\quad i(E_{23}+E_{32}),
$$

$$
E_{13}-E_{31},\quad i(E_{13}+E_{31}).
$$

These eight matrices are anti-Hermitian, traceless, and linearly independent over
$\mathbb R$, so they form a basis of $\mathfrak{su}(3)$.

Hence the finite combinatorial datum determines the type-$A_2$ root datum, and after the
standard linear realization it yields the standard complex Lie algebra
$\mathfrak{sl}_3(\mathbb C)$ and, after Hermitian normalization, its compact real form.

`∎`

---

## 8. What is proved and what is not

### Proved

1. The six-state binary datum determines the root system $A_2$.
2. It yields the Cartan matrix of type $A_2$.
3. After the standard linear realization, it yields the standard complex Lie algebra
   $\mathfrak{sl}_3(\mathbb C)$.
4. After the same realization, it realizes the module $\mathbf 3\oplus\overline{\mathbf 3}$.
5. After fixing the standard Hermitian form, it yields the compact real form
   $\mathfrak{su}(3)$.

### Not proved here

1. the full Lie group $SU(3)$ as an independently reconstructed geometric manifold;
2. gauge theory, local gauge fields, or Yang-Mills dynamics;
3. any direct physical interpretation in particle physics.

---

## 9. Verification

The local verification script is:

```text
verify_six_state_a2_sl3_su3.py
```

It checks:

- the Chevalley-Serre relations for type $A_2$;
- that the generators span all of $\mathfrak{sl}_3(\mathbb C)$;
- that the six-state block module realizes $\mathbf 3\oplus\overline{\mathbf 3}$;
- that the chosen compact basis indeed spans $\mathfrak{su}(3)$.

The script uses only the Python standard library.


[D]: # (Status Marker)
