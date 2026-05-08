# DOT: AMR-DC - Divisor Carrier and Chain Extension

## 0. Introduction

This document defines the **AMR-DC** branch on the divisor carrier

$$
D(N)=\{d\in\mathbb N:d\mid N\}.
$$

The purpose of this branch is to build a strict arithmetic avatar of the Boolean core of DOT and fix the boundaries of the chain extension.

The document `03A_DOT_AMR_Scale_Residue_Line_EN.md` defines another branch, **AMR-SR**, with carrier

$$
\mathcal R=\mathbb N_{>0}^{2},
$$

decomposition

$$
(a,b)=g(p,q),\qquad g=\gcd(a,b),\qquad \gcd(p,q)=1,
$$

and scalar residue

$$
\mathrm{Res}_{\mathrm{sr}}=(g-1)|p-q|.
$$

AMR-SR and AMR-DC are not mixed in this file. Key boundary:

$$
\mathrm{Res}_{\mathrm{sr}}\neq R_{\mathrm{oct}}.
$$

Working unit of notation in AMR-DC:

$$
\Pi=(X,R,q,\mathrm{rec}),
$$

where $X$ is the carrier, $R$ is the relation, $q$ is the reading, $\mathrm{rec}$ is the recovery data.

### 0.A. Key formulas of the branch

For a square-free number

$$
N_n=p_1p_2\cdots p_n
$$

we have a Boolean form:

$$
D(N_n)\cong Q_n,\qquad D^\circ(N_n)\cong Q_n\setminus\{0^n,1^n\}=U_n.
$$

For a general number

$$
N=p_1^{a_1}\cdots p_r^{a_r}
$$

we get a chain form:

$$
D(N)\cong\prod_{i=1}^{r}\{0,1,\ldots,a_i\}.
$$

### 0.B. Rank 3 and number 30

$$
30=2\cdot3\cdot5,\qquad D(30)=\{1,2,3,5,6,10,15,30\}.
$$

Proper carrier:

$$
D^\circ(30)=D(30)\setminus\{1,30\}=\{2,3,5,6,10,15\}.
$$

Through ordered basis $(2,3,5)$:

$$
D^\circ(30)\cong Q_3\setminus\{000,111\}.
$$

This gives the first complete arithmetic scene of rank $3$ in the divisor carrier branch.

---

## Table of Key Notation

| Designation | Meaning | Status |
| ---------------------------- | ----------------------------------------------------- | ------------ |
| $D(N)$ | set of positive divisors $N$ | [D] |
| $D^\circ(N)$ | proper divisor carrier $D(N)\setminus\{1,N\}$ | [D] |
| $Q_n$ | binary cube $\{0,1\}^n$ | [K] |
| $Q_n^*$ | punctured cube $Q_n\setminus\{0^n\}$ | [K] |
| $U_n$ | non-trivial layer $Q_n\setminus\{0^n,1^n\}$ | [K] |
| $V_n$ | outer layer $S_1^{(n)}\sqcup S_{n-1}^{(n)}$ | [K] |
| $R_{\mathrm{oct}}$ | rank $3$ octahedral relation | [D]/[K] |
| $R_{\mathrm{cross}}$ | bridge name interpair relation | [B] |
| $R_{\mathrm{noncomp}}$ | bridge name of non-complement relation | [B] |
| $\mathrm{Res}_{\mathrm{sr}}$ | AMR-SR residue | [D] in AMR-SR |

# §0. Status and boundaries

## §0.1. Statuses

The document uses four statuses:

- [D] proven finite statements;
- [K] corpus-fixed conventions;
- [B] bridge readings;
- [H] horizon of open expansion.

Basic rigorous facts [D]:

$$
D(N)\cong\prod_{i=1}^{r}\{0,\ldots,a_i\},\qquad
D(p_1\cdots p_n)\cong Q_n,
$$

$$
D^\circ(p_1\cdots p_n)\cong Q_n\setminus\{0^n,1^n\},
\qquad
\delta_N(d)=N/d,
$$

$$
(D(N),C_N)\cong P_{a_1+1}\square\cdots\square P_{a_r+1}.
$$

## §0.2. Statement boundaries

1. AMR-SR and AMR-DC use different carriers:

$$
\mathcal R=\mathbb N_{>0}^2
\quad\text{and}\quad
D(N)=\{d:d\mid N\}.
$$

2. The $\mathrm{Res}_{\mathrm{sr}}$ designation is reserved for the AMR-SR branch; for rank $3$ in AMR-DC the names are
$R_{\mathrm{oct}}$, $R_{\mathrm{cross}}$, $R_{\mathrm{noncomp}}$.

3. For square-free rank $n$:

$$
D^\circ(N_n)\cong U_n=Q_n\setminus\{0^n,1^n\}.
$$

This is not identical to $V_n$ for $n\ge4$; there is a match only in the rank $3$:

$$
U_3=V_3.
$$

4. The complete functor

$$
\mathrm{AMR\text{-}SR}\longrightarrow \mathrm{AMR\text{-}DC}
$$

is not stated in the document. Partial arrows $\beta_3,\beta_4$ of AMR-SR branch are not automatically derived from AMR-DC.

5. Chain extension beyond the Boolean case has status [H] until a separate closed theory of operators and reconstructions on products of chains.

---

# §1. Divisor carrier

## §1.1. (D(N))

### 1.1.1. Definition of the divisor carrier

Let

$$
N>1
$$

be a natural number.

Let us expand (N) into prime powers:

$$
N=p_1^{a_1}p_2^{a_2}\cdots p_r^{a_r},
$$

where

$$
p_1,\ldots,p_r
$$

are distinct prime numbers, and

$$
a_i\ge1.
$$

**Definition 1.1 [D].**
The divisor carrier of a number (N) is the finite set of all positive divisors of a number (N):

$$
D(N)=\{d\in\mathbb N:d\mid N\}.
$$

The elements of $D(N)$ are called **divisor states** of the number $N$.

### 1.1.2. Carrier status

In AMR-DC, number (N) is not considered only as a quantity.

It is read as a finite carrier:

$$
N
\rightsquigarrow
D(N).
$$

This is the first principle of AMR-DC:

```text
number as a scalar → number as a divisor carrier.
```

That is, (N) holds the finite internal structure:

```text
prime coordinates;
divisive states;
divisibility relation;
extreme poles 1 and N;
conjugation d -> N/d.
```

### 1.1.3. Poles of the divisor carrier

In (D(N)) there are always lower and upper elements:

$$
1\in D(N),
\qquad
N\in D(N).
$$

They have a special status.

$$
1
$$

is an empty divisor that does not contain any prime coordinates.

$$
N
$$

is a complete divisor containing all prime coordinates with maximum allowed multiplicities.

In what follows they will be called full poles of the divisor carrier.

### 1.1.4. Example

Let

$$
N=12=2^2\cdot3.
$$

Then

$$
D(12)={1,2,3,4,6,12}.
$$

Here the lower pole:

$$
1,
$$

upper pole:

$$
12.
$$

Internal proper states:

$$
2,3,4,6.
$$

---

## §1.2. Exponent carrier (E(N))

### 1.2.1. The coordinates of the exponents

Each divisor (d\mid N) has the form

$$
d=p_1^{b_1}p_2^{b_2}\cdots p_r^{b_r},
$$

where

$$
0\le b_i\le a_i.
$$

This follows from the uniqueness of the decomposition into prime factors.

The exponents

$$
(b_1,\ldots,b_r)
$$

specify the coordinates of the divisor inside the number (N).

### 1.2.2. Definition of the carrier of exponents

**Definition 1.2 [D].**
The carrier of exponents of a number (N) is a finite product of chains

$$
E(N)=\prod_{i=1}^{r}{0,1,\ldots,a_i}.
$$

Element

$$
b=(b_1,\ldots,b_r)\in E(N)
$$

indicates with what multiplicity each prime factor (p_i) is included in the divisor.

### 1.2.3. Reading exponents

**Definition 1.3 [D].**
Reading exponents of the divisor carrier is a mapping

$$
\eta_N:D(N)\to E(N)
$$

by the formula

$$
\eta_N
\left(
p_1^{b_1}\cdots p_r^{b_r}
\right)
=
(b_1,\ldots,b_r).
$$

The reverse mapping:

$$
\mu_N:E(N)\to D(N)
$$

is given by the formula

$$
\mu_N(b_1,\ldots,b_r)
=
p_1^{b_1}\cdots p_r^{b_r}.
$$

### 1.2.4. Representation

In DOT form this gives the representation:

$$
\Pi_{\mathrm{exp}}(N)
=
(D(N),\mid,\eta_N,rec_{\eta}).
$$

Here:

```text
X = D(N);
R = divisibility relation |;
q = η_N;
rec_η = recovery of the divisor from the exponent vector through μ_N.
```

Recovery is exact:

$$
rec_{\eta}(b_1,\ldots,b_r)
=
p_1^{b_1}\cdots p_r^{b_r}.
$$

That is, reading the exponents does not lose data if the expansion (N) and the order of the prime factors are fixed.

---

## §1.3. Theorem: $D(N)$ as a product of chains

### Theorem 1.4 [D]. The divisor carrier as a product of chains

Let

$$
N=p_1^{a_1}\cdots p_r^{a_r}.
$$

Then

$$
\boxed{
D(N)\cong
\prod_{i=1}^{r}{0,1,\ldots,a_i}.
}
$$

The isomorphism is given by reading the exponents:

$$
\eta_N(d)=(b_1,\ldots,b_r),
$$

where

$$
d=p_1^{b_1}\cdots p_r^{b_r}.
$$

### Proof

Let (d\in D(N)). Then (d\mid N). By the fundamental theorem of arithmetic (d) has a unique factorization. Since (d\mid N), only primes (p_1,\ldots,p_r) can participate in the expansion of (d), and their exponents cannot exceed those in (N). This means,

$$
d=p_1^{b_1}\cdots p_r^{b_r},
\qquad
0\le b_i\le a_i.
$$

Therefore, each divisor (d) corresponds to a single vector

$$
(b_1,\ldots,b_r)\in
\prod_{i=1}^{r}{0,\ldots,a_i}.
$$

Conversely, any such vector specifies the number

$$
p_1^{b_1}\cdots p_r^{b_r},
$$

which divides (N). Consequently, the mappings

$$
\eta_N:D(N)\to E(N)
$$

and

$$
\mu_N:E(N)\to D(N)
$$

are mutually inverse.

This means that

$$
D(N)\cong E(N)
=
\prod_{i=1}^{r}{0,\ldots,a_i}.
$$

$$
\blacksquare
$$

### Corollary 1.4.1 [D]. Number of divisors

If

$$
N=p_1^{a_1}\cdots p_r^{a_r},
$$

then

$$
|D(N)|=\prod_{i=1}^{r}(a_i+1).
$$

This follows from isomorphism

$$
D(N)\cong\prod_{i=1}^{r}\{0,\ldots,a_i\},
$$

since each coordinate chain has $a_i+1$ states.

### 1.3.1. The meaning of the theorem

Theorem 1.4 is the first rigorous foundation of AMR-DC.

It says:

```text
the entire internal dividing structure of the number N
is a finite product of coordinate chains.
```

Each prime power

$$
p_i^{a_i}
$$

gives one coordinate chain

$$
0,1,\ldots,a_i.
$$

With

$$
a_i=1
$$

this chain becomes binary:

$$
{0,1}.
$$

Therefore, the Boolean carrier appears as a special case of the divisor carrier.

---

## §1.4. Divisibility lattice

### 1.4.1. Divisibility as an order

On (D(N)) there is a natural relation:

$$
d\preceq_N e
\quad\Longleftrightarrow\quad
d\mid e.
$$

If

$$
\eta_N(d)=(b_1,\ldots,b_r),
\qquad
\eta_N(e)=(c_1,\ldots,c_r),
$$

then

$$
d\mid e
\quad\Longleftrightarrow\quad
b_i\le c_i
\quad
\text{for all}i.
$$

That is, divisibility becomes a coordinate-wise order on the product of chains in the support.

### Proposition 1.5 [D]. Coordinate form of divisibility

For any (d,e\in D(N)):

$$
d\mid e
$$

if and only if

$$
\eta_N(d)\le \eta_N(e)
$$

coordinatewise.

### Proof

Let

$$
d=p_1^{b_1}\cdots p_r^{b_r},
\qquad
e=p_1^{c_1}\cdots p_r^{c_r}.
$$

Then (d\mid e) if and only if for each prime (p_i) the exponent in (d) does not exceed the exponent in (e):

$$
b_i\le c_i.
$$

This is exactly the coordinate order on (E(N)).

$$
\blacksquare
$$

### 1.4.2. The operations meet and join

For any (d,e\in D(N)) exist:

$$
d\wedge e=\gcd(d,e),
$$

$$
d\vee e=\mathrm{lcm}(d,e).
$$

In coordinates:

$$
\eta_N(\gcd(d,e))
=
(\min(b_1,c_1),\ldots,\min(b_r,c_r)),
$$

$$
\eta_N(\mathrm{lcm}(d,e))
=
(\max(b_1,c_1),\ldots,\max(b_r,c_r)).
$$

### Proposition 1.6 [D]. (D(N)) as a finite lattice

Structure

$$
(D(N),\mid,\gcd,\mathrm{lcm})
$$

is a finite lattice.

Bottom element:

$$
\bot=1.
$$

Upper element:

$$
\top=N.
$$

Meet:

$$
d\wedge e=\gcd(d,e).
$$

Join:

$$
d\vee e=\mathrm{lcm}(d,e).
$$

### Proof

In coordinates (D(N)\cong E(N)), and (E(N)) is the product of finite chains

$$
{0,\ldots,a_i}.
$$

The product of finite chains is a finite lattice with coordinate-wise minimum and maximum.

Through reading the exponents, these operations become gcd and lcm, respectively.

$$
\blacksquare
$$

### 1.4.3. The lattice of divisors as a carrier of the relation

In representation-language:

$$
\Pi_{\mid}(N)
=
(D(N),\mid,id,rec_{id}).
$$

Here (id) means that reading for now leaves the carrier in itself.

You can also use exponent representation:

$$
\Pi_{\eta}(N)
=
(D(N),\mid,\eta_N,\mu_N).
$$

It is exact because (\mu_N\eta_N=id_{D(N)}).

---

## §1.5. Cover relation

### 1.5.1. Covering step

Divisibility sets the order. For graph reading, the nearest step of this order is needed.

**Definition 1.7 [D].**
For (d,e\in D(N)) we write

$$
d\lessdot_N e,
$$

if:

1. (d\mid e);
2. (d\ne e);
3. there is no (h\in D(N)) such that

$$
d\mid h\mid e,
\qquad
h\ne d,e.
$$

That is, (e) covers (d) in the lattice of divisors.

### 1.5.2. Coordinate form of the cover relation

If

$$
\eta_N(d)=(b_1,\ldots,b_r),
$$

then

$$
d\lessdot_N e
$$

if and only if there is a single index (i) for which

$$
\eta_N(e)
=
(b_1,\ldots,b_i+1,\ldots,b_r),
$$

subject to

$$
b_i<a_i.
$$

In arithmetic form:

$$
e=d\cdot p_i.
$$

That is, the cover step is a multiplication by one prime factor if this does not lead beyond (N).

### 1.5.3. Undirected cover graph

For graph reading it is convenient to forget the orientation of the order.

**Definition 1.8 [D].**
The undirected cover graph $C_N$ on $D(N)$ is defined as follows:

$$
{d,e}\in C_N
$$

if and only if

$$
d\lessdot_N e
$$

or

$$
e\lessdot_N d.
$$

Equivalently:

$$
{d,e}\in C_N
$$

if and only if (d) and (e) differ by multiplication or division by one prime factor (p_i), and both remain divisors of (N).

### Theorem 1.9 [D]. Cover graph as a product of paths

Let

$$
N=p_1^{a_1}\cdots p_r^{a_r}.
$$

Then

$$
\boxed{
(D(N),C_N)
\cong
P_{a_1+1}\square P_{a_2+1}\square\cdots\square P_{a_r+1}.
}
$$

Here (P_m) is a path with (m) vertices, and (\square) is the Cartesian product of graphs.

### Proof

By Theorem 1.4:

$$
D(N)\cong
\prod_{i=1}^{r}{0,\ldots,a_i}.
$$

At each coordinate

$$
{0,\ldots,a_i}
$$

the covering step connects neighboring values:

$$
0-1-2-\cdots-a_i.
$$

This path is

$$
P_{a_i+1}.
$$

In a complete product of chains in a carrier, the covering step changes exactly one coordinate to (+1) or (-1), leaving the remaining coordinates unchanged.

It is this adjacency rule that defines the Cartesian product of paths:

$$
P_{a_1+1}\square\cdots\square P_{a_r+1}.
$$

$$
\blacksquare
$$

### 1.5.4. DOT-reading

The cover relation gives a local transition layer on the divisor carrier:

```text
transition along one prime factor = one cover step.
```

In the square-free Boolean case, this transition becomes a Hamming step of 1 transition.

---

## §1.6. Duality of divisors

### 1.6.1. Definition

**Definition 1.10 [D].**
The duality of the divisors of a number (N) is a mapping

$$
\delta_N:D(N)\to D(N)
$$

by the formula

$$
\delta_N(d)=\frac{N}{d}.
$$

If (d\mid N), then (N/d\in D(N)), so the mapping is correct.

### 1.6.2. Coordinate form

Let

$$
N=p_1^{a_1}\cdots p_r^{a_r},
$$

and

$$
d=p_1^{b_1}\cdots p_r^{b_r}.
$$

Then

$$
\delta_N(d)
=
\frac{N}{d}
=
p_1^{a_1-b_1}\cdots p_r^{a_r-b_r}.
$$

Consequently,

$$
\eta_N(\delta_N(d))
=
(a_1-b_1,\ldots,a_r-b_r).
$$

That is, the duality of divisors reflects each coordinate chain:

$$
b_i\mapsto a_i-b_i.
$$

### Proposition 1.11 [D]. Duality of divisors is an involution

$$
\delta_N^2=id_{D(N)}.
$$

### Proof

For any (d\mid N):

$$
\delta_N(\delta_N(d))
=
\delta_N\left(\frac Nd\right)
=
\frac{N}{N/d}
=
d.
$$

$$
\blacksquare
$$

### Proposition 1.12 [D]. Duality of divisors reverses the order

For any (d,e\in D(N)):

$$
d\mid e
\quad\Longleftrightarrow\quad
\delta_N(e)\mid \delta_N(d).
$$

### Proof

Let

$$
\eta_N(d)=(b_1,\ldots,b_r),
\qquad
\eta_N(e)=(c_1,\ldots,c_r).
$$

Condition

$$
d\mid e
$$

equivalent

$$
b_i\le c_i
\quad
\forall i.
$$

After applying (\delta_N) we get coordinates:

$$
\eta_N(\delta_N(d))
=
(a_i-b_i)_i,
$$

$$
\eta_N(\delta_N(e))
=
(a_i-c_i)_i.
$$

Inequality

$$
b_i\le c_i
$$

equivalent to

$$
a_i-c_i\le a_i-b_i.
$$

So,

$$
\delta_N(e)\mid \delta_N(d).
$$

The opposite follows by the same reasoning, since (\delta_N) is an involution.

$$
\blacksquare
$$

### 1.6.3. Poles and complement

Duality of divisors swaps the lower and upper pole:

$$
\delta_N(1)=N,
$$

$$
\delta_N(N)=1.
$$

In the square-free case, this will become a Boolean complement:

$$
x\mapsto \bar x=x+1^n.
$$

In general, the product of case chains is a reflection with respect to the middle of each chain.

### 1.6.4. Fixed points

A point (d\in D(N)) is a fixed point duality of divisors if and only if

$$
d=\frac Nd.
$$

That is

$$
d^2=N.
$$

Therefore, a fixed point exists if and only if (N) is a square. In coordinates, this means that all (a_i) are even, and

$$
b_i=\frac{a_i}{2}.
$$

In the square-free case, there are no fixed points at (n\ge1), because the exponents (a_i=1) are odd.

---

## §1.7. Layer readings

### 1.7.1. Why are there multiple layer readings

The carrier of the divisors has the coordinates of the exponents. Therefore, it has several natural ways to reading the “level” of a state.

In the Boolean case, all these readings are often the same. In a chain case they diverge. Therefore, you need to divide:

```text
total multiplicity layer;
layer of active coordinates;
support reading.
```

### 1.7.2. Full multiplicity layer (\Omega_N)

**Definition 1.13 [D].**
For

$$
d=p_1^{b_1}\cdots p_r^{b_r}
$$

let

$$
\Omega_N(d)=b_1+\cdots+b_r.
$$

This is the number of prime factors of the divisor (d) taking into account the multiplicity.

In classical arithmetic notation this is a limited version of the function (\Omega(d)), but here it is reading inside a fixed carrier (D(N)).

### 1.7.3. Active coordinates layer (\omega_N)

**Definition 1.14 [D].**
For

$$
d=p_1^{b_1}\cdots p_r^{b_r}
$$

let

$$
\omega_N(d)=|{i:b_i>0}|.
$$

This is the number of active prime coordinates.

Otherwise:

```text
ω_N(d) counts how many prime coordinates are included at least once.
```

### 1.7.4. Coordinate reading of the carrier

**Definition 1.15 [D].**
The carrier of the coordinates of the divisor (d\mid N) is the set of prime coordinates included in (d):

$$
\mathrm{supp}_N(d)={p_i:b_i>0}.
$$

Then

$$
\omega_N(d)=|\mathrm{supp}_N(d)|.
$$

### 1.7.5. Divergence of (\Omega) and (\omega)

If (N) is square-free, then

$$
b_i\in{0,1}
$$

for all (i). Therefore

$$
\Omega_N(d)=\omega_N(d).
$$

But if there are multiplicities, these readings diverge.

Example:

$$
N=12=2^2\cdot3.
$$

For a divisor

$$
d=4=2^2
$$

we have:

$$
\Omega_{12}(4)=2,
$$

because the overall exponent is (2), but

$$
\omega_{12}(4)=1,
$$

because only one prime coordinate is active (2).

Coordinate carrier:

$$
\mathrm{supp}_{12}(4)={2}.
$$

For divisor

$$
d=6=2\cdot3
$$

we have:

$$
\Omega_{12}(6)=2,
\qquad
\omega_{12}(6)=2,
\qquad
\mathrm{supp}_{12}(6)={2,3}.
$$

That is, (4) and (6) lie on the same (\Omega)-layer, but on different support readings.

### 1.7.6. Layer-representation

For the total multiplicity layer:

$$
\Pi_{\Omega}(N)
=
(D(N),C_N,\Omega_N,rec_{\Omega}).
$$

Here

$$
rec_{\Omega}(k)
=
\Omega_N^{-1}(k).
$$

This is not the exact recovery of one divisor. This is fiber recovery:

$$
\Omega_N^{-1}(k)
=
{d\in D(N):\Omega_N(d)=k}.
$$

For active coordinate layer:

$$
\Pi_{\omega}(N)
=
(D(N),C_N,\omega_N,rec_{\omega}),
$$

where

$$
rec_{\omega}(k)
=
\omega_N^{-1}(k).
$$

For support reading:

$$
\Pi_{\mathrm{supp}}(N)
=
(D(N),C_N,\mathrm{supp}_N,rec_{\mathrm{supp}}).
$$

In the square-free case, the support reading is accurate:

$$
d=\prod_{p\in\mathrm{supp}_N(d)}p.
$$

In the non-square-free case, the support reading is not exact because it loses multiplicities.

Example:

$$
2,\ 4,\ 8
$$

have the same support ({2}) inside the carrier (D(8)), but are different divisors.

---

## §1.8. Proper divisor carrier

### 1.8.1. Definition

**Definition 1.16 [D].**
The proper divisor carrier of a number (N) is

$$
D^\circ(N)=D(N)\setminus\{1,N\}.
$$

That is, the lower and upper poles are removed from the divisor carrier.

### 1.8.2. Boundary status of the poles

Important: the transition

$$
D(N)\to D^\circ(N)
$$

does not mean the destruction of (1) and (N).

It means the transfer of two full poles to the boundary status.

That is:

```text
full carrier D(N) is preserved;
active proper scene is $D^\circ(N)$;
poles 1 and N are not included in the active scene,
but remain boundary states of the full carrier.
```

This is consistent with the logic of the puncture into the strict DOT core: the full carrier ($Q_3$) is preserved, and (000) and (111) transferred to limit status; the active layer becomes six mixed states.

### 1.8.3. Proper carrier as a mixed scene

If (N) is composite, then the elements of (D^\circ(N)) are between two extremes:

$$
1<d<N.
$$

They are neither an empty state nor a full state. Therefore, the proper divisor carrier can be read as an arithmetic mixed scene for (N).

### 1.8.4. Small cases

If (N=p) is a prime number, then

$$
D(p)={1,p},
$$

and

$$
D^\circ(p)=\varnothing.
$$

A prime number has no internal proper stage of divisors.

If

$$
N=pq
$$

for two different primes (p,q), then

$$
D(N)={1,p,q,pq},
$$

$$
D^\circ(N)={p,q}.
$$

This is one complement pair:

$$
p\leftrightarrow q.
$$

If

$$
N=pqr
$$

for three different primes, then

$$
D(N)={1,p,q,r,pq,pr,qr,pqr},
$$

$$
D^\circ(N)={p,q,r,pq,pr,qr}.
$$

This is the first six-state proper scene.

### 1.8.5. The induced cover relation on $D^\circ(N)$

On (D^\circ(N)) we can consider the induced cover relation:

$$
C_N^\circ
=
C_N\cap
\binom{D^\circ(N)}{2}.
$$

That is, only those edges of the cover of the full $D(N)$ are preserved whose two endpoints lie in the proper carrier.

But the complete covering graph itself

$$
(D(N),C_N)
$$

remains important, because some of the transitions from the proper scene lead to boundary poles.

### 1.8.6. Leakage boundary

Some operations natural on (D(N)) do not close inside (D^\circ(N)).

For example, a partial multiplication later will be:

$$
d\odot_N e=de
$$

subject to

$$
de\mid N.
$$

But if

$$
N=30,
$$

then

$$
2\odot_{30}15=30.
$$

Both inputs lie in (D^\circ(30)), but the result falls within the pole boundary (30), and not in (D^\circ(30)).

Therefore, the correct type is:

$$
\odot_N:
D^\circ(N)\times D^\circ(N)
\dashrightarrow
D(N),
$$

and not always

$$
D^\circ(N)\times D^\circ(N)
\dashrightarrow
D^\circ(N).
$$

### 1.8.7. Summary §1

The carrier of number divisors (N) has the following basic layers:

$$
D(N)=\{d:d\mid N\}.
$$

$$
D(N)\cong
\prod_i{0,\ldots,a_i}.
$$

$$
(D(N),\mid)
$$

- finite lattice of divisors.

$$
(D(N),C_N)
$$

- covering graph.

$$
\delta_N(d)=N/d
$$

- duality of divisors.

$$
\Omega_N,\ \omega_N,\ \mathrm{supp}_N
$$

- layer/support reading.

$$
D^\circ(N)=D(N)\setminus\{1,N\}
$$

- active proper scene of divisors.

These structures make a composite number finite relation-carrier.

---

# §2. AMR for square-free numbers

## §2.1. Ordered prime basis

### 2.1.1. Square-free numbers

Let

$$
N_n=p_1p_2\cdots p_n,
$$

where

$$
p_1,\ldots,p_n
$$

are distinct prime numbers.

Such a number is called square-free.

In this case, all exponents are equal to one:

$$
a_1=\cdots=a_n=1.
$$

By Theorem 1.4:

$$
D(N_n)\cong
\prod_{i=1}^{n}{0,1}.
$$

That is

$$
D(N_n)\cong{0,1}^{n}.
$$

### 2.1.2. Canonical and coordinate options

There are two levels of canonicity.

Without choosing the order of the prime factors, there is a canonical bijection:

$$
D(N_n)
\cong
\mathcal P({p_1,\ldots,p_n}),
$$

where (\mathcal P) is the set of all subsets of the set of prime divisors.

The divisor

$$
d\mid N_n
$$

goes to the set of primes that divide it:

$$
d
\mapsto
{p:p\mid d}.
$$

To get namely

$$
D(N_n)\cong Q_n=\{0,1\}^{n},
$$

you need to choose the order of prime factors:

$$
(p_1,\ldots,p_n).
$$

This order is called **ordered prime basis**.

### 2.1.3. Definition of an ordered prime basis

**Definition 2.1 [K].**
An ordered prime basis for a square-free number

$$
N_n=p_1\cdots p_n
$$

has a fixed order of its prime factors:

$$
\mathfrak p=(p_1,\ldots,p_n).
$$

After selection (\mathfrak p), each divisor (d\mid N_n) receives a bit coordinate:

$$
x_i(d)=
\begin{cases}
1,& p_i\mid d,\\
0,& p_i\nmid d.
\end{cases}
$$

### 2.1.4. A note about symmetry

If we change the order of the primes, then the isomorphism with ($Q_n$) changes by rearranging the coordinates.

Consequently:

```text
D(N_n) ≅ Boolean lattice for a fixed prime order;
D(N_n) ≅ $Q_n$ after choosing an ordered prime basis.
```

This is not a defect. This is an exact indication of labeling-data.

---

## §2.2. Square-free mapping (\theta_N)

### 2.2.1. Definition (\theta_N)

Let

$$
N=p_1p_2\cdots p_n
$$

and an ordered prime basis is chosen

$$
(p_1,\ldots,p_n).
$$

**Definition 2.2 [D].**
A square-free mapping

$$
\theta_N:Q_n\to D(N)
$$

is given by the formula

$$
\theta_N(x_1,\ldots,x_n)
=
\prod_{i:x_i=1}p_i.
$$

If all (x_i=0), the product over the empty set is considered equal to (1):

$$
\theta_N(0,\ldots,0)=1.
$$

If all (x_i=1), we get:

$$
\theta_N(1,\ldots,1)=N.
$$

### 2.2.2. Inverse mapping

The inverse mapping

$$
\theta_N^{-1}:D(N)\to Q_n
$$

is given by the formula

$$
\theta_N^{-1}(d)
=
(\mathbf 1_{p_1\mid d},\ldots,\mathbf 1_{p_n\mid d}).
$$

That is, the (i)-th coordinate is equal to (1) if (p_i) divides (d), and equal to (0) if it does not divide.

### 2.2.3. Example: (N=30)

For

$$
30=2\cdot3\cdot5
$$

with an ordered prime basis

$$
(2,3,5)
$$

we get:

$$
000\mapsto1,
$$

$$
100\mapsto2,
$$

$$
010\mapsto3,
$$

$$
001\mapsto5,
$$

$$
110\mapsto6,
$$

$$
101\mapsto10,
$$

$$
011\mapsto15,
$$

$$
111\mapsto30.
$$

This will be the central table of §4. In the current section it is used only as an example of a display for square-free numbers.

---

## §2.3. Theorem: $D(p_1\cdots p_n)\cong Q_n$

### Theorem 2.3 [D]. The divisor carrier of a square-free number

Let

$$
N=p_1p_2\cdots p_n
$$

is a square-free number, and let an ordered prime basis be chosen

$$
(p_1,\ldots,p_n).
$$

Then the mapping for square-free numbers

$$
\theta_N:Q_n\to D(N)
$$

is a bijection.

Therefore,

$$
\boxed{
D(p_1p_2\cdots p_n)\cong Q_n.
}
$$

### Proof

Let

$$
x=(x_1,\ldots,x_n)\in Q_n.
$$

Then

$$
\theta_N(x)=\prod_{i:x_i=1}p_i.
$$

Since (N) is the product of all (p_i) with multiplicity (1), the product of any subset of these primes divides (N). So,

$$
\theta_N(x)\in D(N).
$$

Now let

$$
d\in D(N).
$$

Since (N) is square-free, each prime (p_i) can enter into (d) only with exponent (0) or (1). Therefore (d) is uniquely determined by the set of those (p_i) that divide it.

This set defines the bit vector

$$
x(d)
=
(\mathbf 1_{p_1\mid d},\ldots,\mathbf 1_{p_n\mid d}).
$$

Then

$$
\theta_N(x(d))=d.
$$

On the other hand, if you start with (x), construct (\theta_N(x)), and then take the exponent vector of prime factors, you get the same (x).

So, (\theta_N) and (\theta_N^{-1}) are mutually inverse.

Therefore,

$$
D(N)\cong Q_n.
$$

$$
\blacksquare
$$

### 2.3.1. Strict sense

This is not an analogy or a metaphor.

This is a strict finite isomorphism of the carriers.

The bridge interpretation begins only when we reading this isomorphism as an arithmetic implementation of the Boolean core of DOT.

---

## §2.4. Compatibility theorem

Now we need to prove that the isomorphism for a square-free number preserves not only the set of states, but also the basic relations and readings.

Let

$$
N=p_1\cdots p_n
$$

be free of squares, and an ordered prime basis is chosen.

Let

$$
\theta_N:Q_n\to D(N)
$$

be a bijection for square-free numbers.

On ($Q_n$=\{0,1\}^n) we use:

```text
Hamming weight;
Boolean coordinate order;
Hamming-step-1 relation;
Boolean addition.
```

On (D(N)) we use:

```text
number of prime factors;
divisibility;
covering ratio;
duality of divisors.
```

### Theorem 2.4 [D]. Compatibility theorem

For square-free (N=p_1\cdots p_n) the mapping

$$
\theta_N:Q_n\to D(N)
$$

has the following compatibilities.

#### (1) Poles

$$
\theta_N(0^n)=1,
$$

$$
\theta_N(1^n)=N.
$$

#### (2) Layer/Hamming weight

For any (x\in $Q_n$):

$$
w(x)=\omega_N(\theta_N(x))=\Omega_N(\theta_N(x)).
$$

Here (w(x)) is the Hamming weight.

#### (3) Boolean order / divisibility

For (x,y\in $Q_n$):

$$
x_i\le y_i\quad\forall i
$$

if and only if

$$
\theta_N(x)\mid\theta_N(y).
$$

#### (4) Meet / join

For (x,y\in $Q_n$):

$$
\theta_N(x\wedge y)=\gcd(\theta_N(x),\theta_N(y)),
$$

$$
\theta_N(x\vee y)=\mathrm{lcm}(\theta_N(x),\theta_N(y)),
$$

where (\wedge,\vee) are coordinate-wise Boolean AND/OR.

#### (5) Complement / duality of divisors

Let

$$
\bar x=x+1^n
$$

in (\mathbb{F}_2^n), that is (\bar x_i=1-x_i). Then

$$
\theta_N(\bar x)
=
\frac{N}{\theta_N(x)}
\delta_N(\theta_N(x)).
$$

#### (6) Hamming step 1 / cover relation

For (x,y\in $Q_n$):

$$
d_H(x,y)=1
$$

if and only if

$$
{\theta_N(x),\theta_N(y)}\in C_N.
$$

That is, the complete cover graph

$$
(D(N),C_N)
$$

isomorphic to the (n)-cube ($Q_n$) as a Hamming graph.

#### (7) Proper carrier / puncture

$$
\theta_N
\left(
Q_n\setminus\{0^n,1^n\}
\right)
=
D^\circ(N).
$$

Otherwise:

$$
D^\circ(N)
\cong
Q_n\setminus\{0^n,1^n\}.
$$

### Proof

(1) By definition (\theta_N), the empty set of chosen primes gives the product (1), and the full set of all primes gives (N). Therefore:

$$
\theta_N(0^n)=1,
\qquad
\theta_N(1^n)=N.
$$

(2) Hamming weight (w(x)) counts the number of coordinates, where (x_i=1). By definition (\theta_N(x)) is exactly the number of primes (p_i) included in the divisor. Since (N) is free of squares, each active coordinate has exponent (1). Therefore, the number of active coordinates and the sum of exponents coincide:

$$
w(x)=\omega_N(\theta_N(x))=\Omega_N(\theta_N(x)).
$$

(3) In the Boolean order, the condition

$$
x_i\le y_i
$$

means: if (p_i) is included in (\theta_N(x)), then it is also included in (\theta_N(y)). This is exactly the divisibility condition

$$
\theta_N(x)\mid\theta_N(y).
$$

(4) Coordinate AND leaves one exactly where both vectors have one. This corresponds to common prime factors, that is, gcd.

Coordinate OR puts one where at least one vector has one. This corresponds to the union of prime factors, that is, lcm.

Consequently:

$$
\theta_N(x\wedge y)=\gcd(\theta_N(x),\theta_N(y)),
$$

$$
\theta_N(x\vee y)=\mathrm{lcm}(\theta_N(x),\theta_N(y)).
$$

(5) The vector (\bar x) selects exactly those prime factors (p_i) that are not selected in (x). Therefore, the products (\theta_N(x)) and (\theta_N(\bar x)) contain disjoint subsets of primes, and together they give all the prime factors (N). So,

$$
\theta_N(\bar x)=\frac{N}{\theta_N(x)}.
$$

(6) Condition

$$
d_H(x,y)=1
$$

means that (x) and (y) differ in exactly one coordinate (i). Then (\theta_N(x)) and (\theta_N(y)) differ by multiplication or division by (p_i). This is exactly the cover relation (C_N) on the divisor carrier of a square-free number.

Conversely, if (\theta_N(x)) and (\theta_N(y)) are related by the cover relation, then they differ in exactly one prime factor, which means (x) and (y) differ in exactly one coordinate.

(7) According to point (1):

$$
0^n\leftrightarrow1,
\qquad
1^n\leftrightarrow N.
$$

Deleting these two points on the side ($Q_n$) corresponds to removing (1) and (N) on the (D(N)) side. Therefore

$$
D^\circ(N)
\cong
Q_n\setminus\{0^n,1^n\}.
$$

$$
\blacksquare
$$

### 2.4.1. Immediate corollary

For square-free (N):

$$
(D(N),C_N)
\cong
Q_n
$$

as a graph carrier with the Hamming-step-1 relation.

And the proper divisor carrier:

$$
(D^\circ(N),C_N^\circ)
$$

one obtains the induced punctured Hamming graph:

$$
Q_n\setminus\{0^n,1^n\}.
$$

For (n=3) this induced graph is a cycle:

$$
C_6.
$$

The proof of the rank-3 case will be given in §4.

---

## §2.5. AMR status for square-free numbers

### 2.5.1. Strict conclusion

Square-free AMR has a strict status in the following sense:

$$
\boxed{
D(p_1\cdots p_n)\cong Q_n
}
$$

as finite carriers.

Moreover, compatible:

```text
Boolean order ↔ divisibility;
Hamming weight ↔ number of prime factors;
Hamming step 1 ↔ cover by one prime factor;
Boolean complement ↔ divisor duality;
puncture of full poles ↔ proper divisor carrier.
```

This is no longer just a numerical analogy. This is an exact finite representation.

### 2.5.2. Representation Form

The square-free AMR can be written as the representation:

$$
\Pi_{\mathrm{sf}}(N)
=
(D(N),C_N,\theta_N^{-1},rec_{\theta}).
$$

Here:

$$
X=D(N),
$$

$$
R=C_N,
$$

$$
q=\theta_N^{-1}:D(N)\to Q_n,
$$

$$
rec_{\theta}=\theta_N:Q_n\to D(N).
$$

Since (\theta_N) is a bijection, the recovery is exact.

You can also use the order of divisibility:

$$
\Pi_{\mathrm{sf},\mid}(N)
=
(D(N),\mid,\theta_N^{-1},\theta_N).
$$

Then the relation (R) is not an adjacency graph, but a partial order.

### 2.5.3. Bridge output

AMR bridge reading for square-free numbers:

```text
a square-free number is an arithmetic representation of a Boolean carrier.
```

Or more details:

```text
number N=p_1...p_n contains n independent prime coordinates;
divisor d|N is the state of these coordinates;
transition along one prime is a step Hamming 1 transition;
conjugate divisor N/d is Boolean complement;
proper divisors form a punctured active scene.
```

### 2.5.4. Corollary for rank 3

For

$$
N=30=2\cdot3\cdot5
$$

we have:

$$
D(30)\cong Q_3.
$$

And

$$
D^\circ(30)
\cong
Q_3\setminus\{000,111\}.
$$

This is exactly a strict rank-3 admissible carrier of DOT.

In the strict core of DOT this six-point scene carries relation readings:

$$
C_6,
\qquad
K_3\sqcup K_3,
\qquad
3K_2,
\qquad
K_{2,2,2}.
$$

In AMR-DC these readings will be received as different relations on the same carrier

$$
D^\circ(30)=\{2,3,5,6,10,15\}.
$$

This will be the topic §4.

### 2.5.5. Generalization boundary

For (n\ge4) the proper divisor carrier of a square-free number gives:

$$
D^\circ(p_1\cdots p_n)
\cong
U_n
=
Q_n\setminus\{0^n,1^n\}.
$$

It is not automatically equal to the strict outer layer

$$
V_n=S_1^{(n)}\sqcup S_{n-1}^{(n)}.
$$

Therefore, further development must distinguish between two lines:

```text
proper divisor package $U_n$;
outer layer / cross-polytope package $V_n$.
```

Rank 3 is a special coincidence point:

$$
U_3=V_3.
$$

This explains why the number (30) falls so well into the strict core hexad: in rank 3 proper the carrier of the divisors and the outer admissible layer are the same.

---

# Short summary of block §0–§2

In this block it is fixed:

$$
D(N)=\{d:d\mid N\}.
$$

$$
D(p_1^{a_1}\cdots p_r^{a_r})
\cong
\prod_{i=1}^{r}{0,\ldots,a_i}.
$$

$$
D(p_1\cdots p_n)\cong Q_n.
$$

$$
\delta_N(d)=N/d.
$$

$$
D^\circ(p_1\cdots p_n)
\cong
Q_n\setminus\{0^n,1^n\}.
$$

Main meaning:

```text
AMR-DC turns a composite number from a scalar
into a finite relational divisor carrier.
```

The square-free case gives a strict Boolean core:

```text
prime factors = coordinates;
divisors = Boolean states;
divisibility = coordinate order;
cover relation = Hamming step 1;
duality = complement;
proper divisor carrier = punctured active scene.
```

---

Continuation of the document.

---

# §3. Puncture, proper carrier and boundary states

This chapter captures the difference between:

```text
complete carrier;
active proper scene;
pole boundary status.
```

The main error to eliminate is:

```text
removed from active scene = destroyed from theory.
```

In AMR-DC this is not true. The transition

$$
D(N)\longrightarrow D^\circ(N)
$$

does not destroy (1) and (N). It transfers them from the active interior to the boundary status.

In the square-free case, this is exactly an arithmetic reading of the puncture:

$$
Q_n
\longrightarrow
Q_n\setminus\{0^n,1^n\}.
$$

In the DOT corpus, a similar move is already fixed for rank 3: the full carrier ($Q_3$) is retained, (000) and (111) receive a limit status, and the active-layer becomes six mixed states. This was formulated as obstructive puncture.

---

## §3.1. Full carrier and active scene

### 3.1.1. Complete square-free carrier

Let

$$
N_n=p_1p_2\cdots p_n
$$

be a square-free number.

After choosing an ordered prime basis

$$
(p_1,\ldots,p_n)
$$

we have a strict isomorphism:

$$
D(N_n)\cong Q_n.
$$

Complete divisor carrier:

$$
D(N_n)
$$

contains all states:

$$
1,
\quad
p_i,
\quad
p_ip_j,
\quad
\ldots,
\quad
N_n.
$$

In Boolean coordinates:

$$
1\leftrightarrow0^n,
\qquad
N_n\leftrightarrow1^n.
$$

### 3.1.2. Full poles

**Definition 3.1 [D|K].**
In the divisor carrier of a square-free number (D(N_n)), two elements

$$
1,
\qquad
N_n
$$

are called full poles.

Lower full pole:

$$
1
$$

corresponds to the empty state:

$$
0^n.
$$

Upper full pole:

$$
N_n
$$

corresponds to the fully saturated state:

$$
1^n.
$$

That is:

```text
1 = no prime coordinate is active;
N_n = all prime coordinates are active.
```

### 3.1.3. Active proper scene

**Definition 3.2 [D].**
The active proper scene of the divisor carrier of a square-free number is

$$
D^\circ(N_n)=D(N_n)\setminus\{1,N_n\}.
$$

By the compatibility theorem from §2:

$$
D^\circ(N_n)
\cong
Q_n\setminus\{0^n,1^n\}.
$$

This set contains all non-trivial mixed states: divisors that are neither an empty state nor a complete totality.

### 3.1.4. Difference at the representation level

Full carrier:

$$
\Pi_{\mathrm{full}}(N_n)
=
(D(N_n),C_N,\theta_N^{-1},\theta_N).
$$

Active proper scene:

$$
\Pi_{\mathrm{act}}(N_n)
=
(D^\circ(N_n),C_N^\circ,\theta_N^{-1}|_{D^\circ},\theta_N|_{U_n}).
$$

Here

$$
C_N^\circ
=
C_N\cap \binom{D^\circ(N_n)}{2}
$$

is the induced cover relation on the proper carrier.

In other words:

```text
D(N_n) = complete carrier;
$D^\circ(N_n)$ = active mixed carrier;
{1,N_n} = boundary poles;
C_N = complete transition graph;
C_N° = active induced transition graph.
```

### Proposition 3.3 [D]. The proper divisor carrier is like a punctured cube

For square-free

$$
N_n=p_1\cdots p_n
$$

after choosing an ordered prime basis is true:

$$
\boxed{
D^\circ(N_n)
\cong
Q_n\setminus\{0^n,1^n\}.
}
$$

### Proof

By Theorem 2.3:

$$
D(N_n)\cong Q_n.
$$

In this case:

$$
1\leftrightarrow0^n,
\qquad
N_n\leftrightarrow1^n.
$$

The removal of (1) and (N_n) on the side of the divisor carrier corresponds to the removal of (0^n) and (1^n) on the Boolean carrier side. So,

$$
D^\circ(N_n)
=
D(N_n)\setminus\{1,N_n\}
\cong
Q_n\setminus\{0^n,1^n\}.
$$

$$
\blacksquare
$$

---

## §3.2. Boundary status of poles

### 3.2.1. A puncture is not destruction

Transition

$$
D(N)\to D^\circ(N)
$$

has two different meanings.

Set-theoretic sense:

$$
D^\circ(N)=D(N)\setminus\{1,N\}.
$$

Representation sense:

```text
1 and N leave the active scene,
but remain boundary states of the complete carrier.
```

It is the second meaning that is the DOT-sense of a puncture.

### 3.2.2. Boundary status

**Definition 3.4 [K].**
Let (X) be a full carrier and

$$
X^\circ=X\setminus\{\bot,\top\}
$$

be the active scene after removing two full poles.

Then (\bot,\top) have **boundary status** if:

1. they are not included in the active scene (X^\circ);
2. they remain in full carrier (X);
3. operations or relations on (X^\circ) can refer to them as limit states;
4. they preserve the recoverability of the full carrier.

In AMR-DC:

$$
X=D(N),
\qquad
X^\circ=D^\circ(N),
\qquad
\bot=1,
\qquad
\top=N.
$$

### 3.2.3. Arithmetic form boundary status

In the divisor carrier, the boundary status appears imcarriertely.

For example, for

$$
N=30
$$

we have

$$
2,15\in D^\circ(30),
$$

but

$$
2\cdot15=30.
$$

That is, the internal proper pair can, by product, fall into the upper boundary of the pole.

Therefore, the correct type of operation is:

$$
D^\circ(N)\times D^\circ(N)
\dashrightarrow
D(N),
$$

and not necessarily

$$
D^\circ(N)\times D^\circ(N)
\dashrightarrow
D^\circ(N).
$$

### 3.2.4. DOT-reading

In DOT-language:

```text
full poles are not erased;
they become limit conditions
for the active mixed scene.
```

For rank 3:

$$
Q_3
\to
X_{\mathrm{adm}}=Q_3\setminus\{000,111\}.
$$

In AMR-DC:

$$
D(30)
\to
D^\circ(30)=D(30)\setminus\{1,30\}.
$$

Correspondence:

$$
000\leftrightarrow1,
\qquad
111\leftrightarrow30.
$$

This is the same structural move:

```text
full carrier remains;
two full poles leave active reading;
mixed scene becomes internal.
```

---

## §3.3. Important difference between ($U_n$) and ($V_n$)

### 3.3.1. Hamming layers

For a full Boolean carrier

$$
Q_n=\{0,1\}^n
$$

we denote the Hamming layer:

$$
S_k^{(n)}={x\in Q_n:w(x)=k},
$$

where (w(x)) is the Hamming weight.

Then

$$
Q_n=
\bigsqcup_{k=0}^{n}S_k^{(n)}.
$$

### 3.3.2. Complete non-trivial package ($U_n$)

**Definition 3.5 [D|K].**
Complete non-trivial package:

$$
U_n=Q_n\setminus\{0^n,1^n\}.
$$

Equivalent to:

$$
U_n=
\bigsqcup_{k=1}^{n-1}S_k^{(n)}.
$$

Number of elements:

$$
|U_n|=2^n-2.
$$

In AMR-DC, the proper carrier square-free gives the carrier of the divisors exactly ($U_n$):

$$
D^\circ(p_1\cdots p_n)\cong U_n.
$$

### 3.3.3. Strict outer layer ($V_n$)

**Definition 3.6 [K].**
Strict outer layer:

$$
V_n=S_1^{(n)}\sqcup S_{n-1}^{(n)}.
$$

It contains only weight (1) and weight (n-1) states.

Number of elements at (n\ge3):

$$
|V_n|=2n.
$$

In the language of divisors for square-free (N_n=p_1\cdots p_n):

$$
V_n
\leftrightarrow
{p_i:1\le i\le n}
\cup
{N_n/p_i:1\le i\le n}.
$$

That is ($V_n$) consists of:

```text
single-prime states;
with one-missing-prime-factor state.
```

### 3.3.4. Why $U_n\neq V_n$ in the general case

By definition:

$$
V_n\subseteq U_n.
$$

But for (n\ge4) the inclusion is strict:

$$
V_n\subsetneq U_n.
$$

Reason: ($U_n$) includes all internal layers

$$
S_2^{(n)},S_3^{(n)},\ldots,S_{n-2}^{(n)}.
$$

And ($V_n$) leaves only two outer layers:

$$
S_1^{(n)}
\quad
\text{and}
\quad
S_{n-1}^{(n)}.
$$

In the shell continuation corpus this distinction is already fixed as the difference between a complete non-trivial package ($U_n$) and strict external carrier ($V_n$). Two-step filtering is also indicated there:

$$
Q_n
\to
U_n=Q_n\setminus\{0^n,1^n\}
\to
V_n=S_1^{(n)}\sqcup S_{n-1}^{(n)}.
$$

It is this distinction that protects the (4D)-continuation from mixing different sets of vertices.

### 3.3.5. Match in rank 3

When (n=3):

$$
U_3
=
Q_3\setminus\{000,111\}.
$$

But

$$
Q_3
=
S_0^{(3)}\sqcup S_1^{(3)}\sqcup S_2^{(3)}\sqcup S_3^{(3)}.
$$

So,

$$
U_3=S_1^{(3)}\sqcup S_2^{(3)}.
$$

A

$$
V_3=S_1^{(3)}\sqcup S_{3-1}^{(3)}
=
S_1^{(3)}\sqcup S_2^{(3)}.
$$

Consequently:

$$
\boxed{
U_3=V_3.
}
$$

### Theorem 3.7 [D|K]. Rank-3 coincidence theorem

For (n=3):

$$
\boxed{
Q_3\setminus\{000,111\}
=
S_1^{(3)}\sqcup S_2^{(3)}.
}
$$

That is:

$$
\boxed{
U_3=V_3.
}
$$

For (n\ge4):

$$
\boxed{
U_n\neq V_n.
}
$$

### Proof

For (n=3) the internal weights between (0) and (3) are only

$$
1
\quad
\text{and}
\quad
2.
$$

Therefore, after removing (S_0^{(3)}={000}) and (S_3^{(3)}={111}) remain exactly

$$
S_1^{(3)}\sqcup S_2^{(3)}.
$$

But this is it

$$
S_1^{(3)}\sqcup S_{3-1}^{(3)}=V_3.
$$

For (n\ge4) there is at least one internal layer different from (S_1) and (S_{n-1}). For example, (S_2^{(n)}) with (n\ge4) does not coincide with either (S_1^{(n)}) or (S_{n-1}^{(n)}). It is included in ($U_n$), but not in ($V_n$). So,

$$
U_n\neq V_n.
$$

$$
\blacksquare
$$

### 3.3.6. Key Warning

Key Warning AMR-DC:

$$
D^\circ(p_1\cdots p_n)
\cong U_n,
$$

not automatically ($V_n$).

Only at (n=3):

$$
D^\circ(p_1p_2p_3)
\cong U_3=V_3.
$$

Therefore, rank 3 is the point of agreement:

```text
proper carrier square-free = full non-trivial packet = outer cross-polytopic layer.
```

At (n\ge4):

```text
proper carrier square-free $U_n$
and strict outer layer $V_n$
diverge.
```

---

## §3.4. Small ranks

For primorial ladder:

$$
N_n=p_1p_2\cdots p_n
$$

we get the following picture.

| $n$ | $N_n$ | $|D(N_n)|$ | $|D^\circ(N_n)|$ | Boolean form | Meaning |
| ---: | ---: | ---: | ---: | --- | --- |
| $1$ | $2$ | $2$ | $0$ | $Q_1\setminus\{0,1\}=\varnothing$ | no proper stage |
| $2$ | $6$ | $4$ | $2$ | $Q_2\setminus\{00,11\}$ | one complement pair |
| $3$ | $30$ | $8$ | $6$ | $Q_3\setminus\{000,111\}$ | first hexad |
| $4$ | $210$ | $16$ | $14$ | $U_4=Q_4\setminus\{0000,1111\}$ | proper package $U_4$, not $V_4$ |

### 3.4.1. Rank 1

$$
N_1=2.
$$

$$
D(2)={1,2}.
$$

$$
D^\circ(2)=\varnothing.
$$

Meaning:

```text
there are only two full poles;
there is no active proper scene yet.
```

### 3.4.2. Rank 2

$$
N_2=2\cdot3=6.
$$

$$
D(6)={1,2,3,6}.
$$

$$
D^\circ(6)={2,3}.
$$

Addition:

$$
2\leftrightarrow3.
$$

Meaning:

```text
one complement-pair;
no six-point relation-grammar yet.
```

### 3.4.3. Rank 3

$$
N_3=2\cdot3\cdot5=30.
$$

$$
D(30)=\{1,2,3,5,6,10,15,30\}.
$$

$$
D^\circ(30)=\{2,3,5,6,10,15\}.
$$

Meaning:

```text
first proper six-point scene;
first match point U_3=V_3;
first arithmetic avatar X_adm.
```

### 3.4.4. Rank 4

$$
N_4=2\cdot3\cdot5\cdot7=210.
$$

$$
|D(210)|=16.
$$

$$
|D^\circ(210)|=14.
$$

Here:

$$
D^\circ(210)\cong U_4.
$$

But:

$$
V_4=S_1^{(4)}\sqcup S_3^{(4)}
$$

has

$$
|V_4|=8.
$$

That is, rank 4 already separates three objects:

$$
Q_4,
\qquad
U_4,
\qquad
V_4.
$$

These three objects cannot be glued together.

---

## §3.5. Relation to (P1\text{–}P15)

### 3.5.1. $D(210)$ as $Q_4$

Let

$$
210=2\cdot3\cdot5\cdot7.
$$

After choosing an ordered prime basis

$$
(2,3,5,7)
$$

we get:

$$
D(210)\cong Q_4.
$$

Poles:

$$
1\leftrightarrow0000,
\qquad
210\leftrightarrow1111.
$$

### 3.5.2. Non-zero divisor carrier

If we remove only the lower pole (1), we get:

$$
D(210)\setminus\{1\}
\cong
Q_4\setminus\{0000\}.
$$

Denote:

$$
Q_4^*=Q_4\setminus\{0000\}.
$$

Then:

$$
D(210)\setminus\{1\}
\cong
Q_4^*.
$$

Number of elements:

$$
|D(210)\setminus\{1\}|=15.
$$

This is exactly the dimension of the layer (P1\text{–}P15), which in the corpus is read as

$$
F_2^4\setminus\{0000\}.
$$

In the document about (P1\text{–}P15) It is directly stated that the fifteen principles can be read as a complete non-zero layer of a (4)-bit carrier, where (P15=1111) plays the role of full saturation.

### 3.5.3. The proper divisor carrier is not (P1\text{–}P15)

But the proper divisor carrier:

$$
D^\circ(210)=D(210)\setminus\{1,210\}
$$

has

$$
14
$$

elements.

Therefore:

$$
D^\circ(210)
\not\cong
Q_4^*.
$$

Namely:

$$
D^\circ(210)
\cong
Q_4\setminus\{0000,1111\}
=
U_4.
$$

That is:

$$
\begin{aligned}
&D(210)\setminus\{1\} = Q_4^* \quad \text{(arithmetic avatar, possible package P1--P15)}; \\
&D^\circ(210) = U_4 \quad \text{(arithmetic avatar)}; \\
&V_4 \quad \text{strict outer layer, only 8 states}. \\
\end{aligned}
$$

### 3.5.4. Saturation point and removed upper pole

In the (P1\text{–}P15)-carrier, the point

$$
1111
$$

is not removed. It is the saturation point:

$$
P15=1111.
$$

In AMR-DC this corresponds to the divisor

$$
210.
$$

Therefore, if you build an arithmetic avatar for (P1\text{–}P15), you need to use:

$$
D(210)\setminus\{1\},
$$

and not

$$
D^\circ(210).
$$

Otherwise we will mistakenly remove the saturation point.

**Note [B].**
In this projection, the upper pole $1111\leftrightarrow210$ is not an extra vertex. It plays the role of the saturated state of $P15$, so the arithmetic avatar for $P1\text{–}P15$ uses $D(210)\setminus\{1\}$ rather than the proper carrier $D^\circ(210)$.

### 3.5.5. Future bridge note

Possible future formula:

$$
P1\text{–}P15
\quad
\leftrightarrow
\quad
D(210)\setminus\{1\}.
$$

But the status of this formula:

```text
[B] bridge / candidate arithmetic avatar,
not yet strict identification of meanings.
```

The strict part is only this:

$$
D(210)\setminus\{1\}
\cong
F_2^4\setminus\{0000\}.
$$

Bridge part:

```text
a non-zero package of divisors of the number 210 can serve as an
arithmetic carrier for the methodological layer P1-P15.
```

---

# §4. Rank-3 AMR scene: number (30)

This is the central chapter of AMR-DC.

In §2 the general statement was proven:

$$
D(p_1\cdots p_n)\cong Q_n.
$$

In §3 it was shown:

$$
D^\circ(p_1\cdots p_n)\cong U_n,
$$

and only for (n=3):

$$
U_3=V_3.
$$

Now the first complete case is considered:

$$
30=2\cdot3\cdot5.
$$

Here the divisor carrier, its proper puncture, the Boolean core, the strict outer layer, and the rank-3 admissible hexad coincide in one six-point scene.

---

## §4.1. Why (30)

### 4.1.1. Minimal representative of rank 3 square-free

$$
30=2\cdot3\cdot5.
$$

This is the first natural square-free number with three different prime coordinates.

It is the minimal representative of all numbers of the form

$$
pqr,
$$

where (p,q,r) are distinct primes.

Any such number gives the support

$$
D(pqr)\cong Q_3.
$$

But (30) is the first natural representative, because that

$$
2,3,5
$$

are the first three prime numbers.

### 4.1.2. Four Reasons

The number (30) is important for four reasons.

1. This is the first square-free number with three independent prime coordinates:

$$
30=2\cdot3\cdot5.
$$

2. It gives the first full (3)-bit divisor carrier:

$$
D(30)\cong Q_3.
$$

3. Its proper divisor carrier has six elements:

$$
| D^ \circ(30)| = 6.
$$

4. It gives an exact arithmetic avatar of a strict rank-3 admissible carrier:

$$
D^ \circ(30)
\cong
Q_3 \setminus\{000,111\} = X_{\mathrm{adm}}.
$$

(30) acts as the first carrier square-free with three independent prime coordinates, and after removing the full poles, a six-point proper scene remains

$$
D^\circ(30)=\{2,3,5,6,10,15\}.
$$



### 4.1.3. Full and proper carrier

Full carrier:

$$
D(30)=\{1,2,3,5,6,10,15,30\}.
$$

Proper carrier:

$$
D^\circ(30)=\{2,3,5,6,10,15\}.
$$

Full poles:

$$
1,
\qquad
30.
$$

Boundary reading:

$$
1\leftrightarrow000,
\qquad
30\leftrightarrow111.
$$

Active scene:

$$
D^\circ(30)
\leftrightarrow
Q_3\setminus\{000,111\}.
$$

---

## §4.2. Complete correspondence table

Choose an ordered prime basis:

$$
(2,3,5).
$$

Then the mapping for square-free numbers

$$
\theta_{30}:Q_3\to D(30)
$$

is given:

$$
\theta_{30}(x_1,x_2,x_3) =
2^{x_1}3^{x_2}5^{x_3}.
$$

Full table (D(30)):

| bit | divisor | status | layer |
| ----- | -------: | ------------------ | ---: |
| (000) |      (1) | lower full pole |  (0) |
| (100) |      (2) | proper |  (1) |
| (010) |      (3) | proper |  (1) |
| (001) |      (5) | proper |  (1) |
| (110) |      (6) | proper |  (2) |
| (101) |     (10) | proper |  (2) |
| (011) |     (15) | proper |  (2) |
| (111) |     (30) | upper full pole |  (3) |

Proper carrier table:

| bit | divisor | layer | addition |
| ----- | -------: | ---: | ---------: |
| (100) |      (2) |  (1) |       (15) |
| (010) |      (3) |  (1) |       (10) |
| (001) |      (5) |  (1) |        (6) |
| (110) |      (6) |  (2) |        (5) |
| (101) |     (10) |  (2) |        (3) |
| (011) |     (15) |  (2) |        (2) |

Addition-pairs:

$$
2\leftrightarrow15,
\qquad
3\leftrightarrow10,
\qquad
5\leftrightarrow6.
$$

Layer-and:

$$
S_1^{30}={2,3,5},
$$

$$
S_2^{30}={6,10,15}.
$$

Here

$$
S_1^{30}
\leftrightarrow
S_1^{(3)},
\qquad
S_2^{30}
\leftrightarrow
S_2^{(3)}.
$$

---

## §4.3. Theorem 4.1: \(D^\circ(30) \cong X_{\mathrm{adm}}\)

### Theorem 4.1 [D|K]. Rank-3 arithmetic avatar

$$
\boxed{ D^\circ(30)
\cong
Q_3\setminus\{000,111\}
= X_{\mathrm{adm}}.}
$$

### Proof

Decomposition:

$$
30=2\cdot3\cdot5.
$$

By theorem for square-free numbers:

$$
D(30)\cong Q_3.
$$

Explicitly:

$$
D(30)=\{1,2,3,5,6,10,15,30\}.
$$

With an ordered prime basis ((2,3,5)):

$$
1\leftrightarrow000,
$$

$$
2\leftrightarrow100,
\qquad
3\leftrightarrow010,
\qquad
5\leftrightarrow001,
$$

$$
6\leftrightarrow110,
\qquad
10\leftrightarrow101,
\qquad
15\leftrightarrow011,
$$

$$
30\leftrightarrow111.
$$

Removal of full poles (1) and (30) gives:

$$
D^\circ(30)=D(30)\setminus\{1,30\}.
$$

On the side ($Q_3$) this corresponds to the removal

$$
000
\quad
\text{and}
\quad
111.
$$

Therefore,

$$
D^\circ(30)
\cong
Q_3\setminus\{000,111\}.
$$

By definition, strict rank-3 is admissible of the bearer:

$$
X_{\mathrm{adm}}=Q_3\setminus\{000,111\}.
$$

So,

$$
D^\circ(30)\cong X_{\mathrm{adm}}.
$$

$$
\blacksquare
$$

### 4.3.1. Status

Strict part:

$$
D^\circ(30)\cong Q_3\setminus\{000,111\}.
$$

Corpus fixed identification:

$$
Q_3\setminus\{000,111\}=X_{\mathrm{adm}}.
$$

Bridge reading:

```text
30 is the first natural arithmetic avatar
of an admissible DOT scene of rank 3.
```

---

## §4.4. Relation-reading 1: Cover Cycle ($C_6$)

### 4.4.1. Definition

On (D^\circ(30)) consider the induced cover relation:

$$
C_{30}^\circ = C_{30} \cap \binom{D^\circ(30)}{2}.
$$

That is, two proper divisors are connected if they differ by multiplying or dividing by one prime factor, and both remain proper.

### 4.4.2. Edges

Edges:

$$
2-6,
\qquad
6-3,
\qquad
3-15,
\qquad
15-5,
\qquad
5-10,
\qquad
10-2.
$$

Can be written as a cycle:

$$
2
\longrightarrow
6
\longrightarrow
3
\longrightarrow
15
\longrightarrow
5
\longrightarrow
10
\longrightarrow
2.
$$

Consequently:

$$
(D^\circ(30),C_{30}^\circ)\cong C_6.
$$

### Theorem 4.2 [D]. The cover relation is given by $C_6$

The induced covering graph on (D^\circ(30)) is a cycle of length (6):

$$
\boxed{
(D^\circ(30),C_{30}^\circ)\cong C_6.
}
$$

### Proof

In full divisor carrier

$$
D(30)\cong Q_3.
$$

Cover graph of the complete (D(30)) corresponds to Hamming step 1 graph of the complete cube ($Q_3$).

Remove two vertices:

$$
1\leftrightarrow000,
\qquad
30\leftrightarrow111.
$$

In the complete cube ($Q_3$) after removing the opposite vertices (000) and (111), an induced subgraph remains on six vertices:

$$
100,010,001,110,101,011.
$$

Each remaining vertex had exactly three neighbors in $Q_3$ Hamming-1. Exactly one of these neighbors is removed: for vertices of weight $1$ it is $000$, for vertices of weight $2$ it is $111$. Therefore, in the induced graph on $U_3$, each vertex has degree $2$.

It remains to check that this is one cycle and not two components. Explicit traversal:

$$
100\to110\to010\to011\to001\to101\to100
$$

passes all six vertices and closes. Consequently, the induced graph is a connected $2$-regular graph on six vertices, that is, a cycle $C_6$.

In the notation for divisors of its edges:

$$
2-6,
\quad
6-3,
\quad
3-15,
\quad
15-5,
\quad
5-10,
\quad
10-2.
$$

So,

$$
(D^\circ(30),C_{30}^\circ)\cong C_6.
$$

$$
\blacksquare
$$

### 4.4.3. DOT-reading

This is an arithmetic version of the transport-cycle:

```text
transition by one prime factor
=
step Hamming 1 permissible transition.
```

In the strict core DOT ($C_6$) is one of the main graph readings on ($X_{\mathrm{adm}}$).

---

## §4.5. Relation-reading 2: Intralayer Relation ($K_3\sqcup K_3$)

### 4.5.1. Layer decomposition

The proper carrier is decomposed into two layers:

$$
D^\circ(30)=S_1^{30}\sqcup S_2^{30},
$$

where

$$
S_1^{30}={2,3,5},
$$

$$
S_2^{30}={6,10,15}.
$$

Here:

$$
S_1^{30}
=
{d\in D^\circ(30):\omega_{30}(d)=1},
$$

$$
S_2^{30}
=
{d\in D^\circ(30):\omega_{30}(d)=2}.
$$

### 4.5.2. Intralayer relation

**Definition 4.3 [D].**
Layer-internal relation (R_{\mathrm{sh}}) on (D^\circ(30)):

$$
d\sim_{\mathrm{sh}}e
$$

if

$$
d\ne e
$$

and

$$
\omega_{30}(d)=\omega_{30}(e).
$$

Else:

```text
connect two different proper divisors
if they lie in the same layer.
```

### 4.5.3. Edges

To layer (S_1^{30}):

$$
2-3,
\qquad
2-5,
\qquad
3-5.
$$

This is (K_3).

To layer (S_2^{30}):

$$
6-10,
\qquad
6-15,
\qquad
10-15.
$$

This is the second (K_3).

Consequently:

$$
(D^\circ(30),R_{\mathrm{sh}})
\cong
K_3\sqcup K_3.
$$

### Theorem 4.4 [D]. The intra-layer relation is given by $K_3\sqcup K_3$

$$
\boxed{
(D^\circ(30),R_{\mathrm{sh}})
\cong
K_3\sqcup K_3.
}
$$

### Proof

The relation (R_{\mathrm{sh}}) connects all different vertices within one layer and does not connect the vertices of different layers.

The layer (S_1^{30}) has three vertices:

$$
2,3,5.
$$

The complete graph on three vertices is (K_3).

The layer (S_2^{30}) has three vertices:

$$
6,10,15.
$$

There is also a complete graph on them (K_3).

There are no edges between the layers (R_{\mathrm{sh}}).

This means that the entire graph is a disjoint union:

$$
K_3\sqcup K_3.
$$

$$
\blacksquare
$$

---

## §4.6. Relation-reading 3: complement graph ($3K_2$)

### 4.6.1. Complement relation of divisors

On (D^\circ(30)) restriction duality of divisors:

$$
\delta_{30}(d)=\frac{30}{d}.
$$

For proper divisors it remains inside its proper carrier:

$$
\delta_{30}:D^\circ(30)\to D^\circ(30).
$$

Because if (1<d<30), then

$$
1<\frac{30}{d}<30.
$$

### 4.6.2. Definition

**Definition 4.5 [D].**
Complement relation (R_{\pm}) on (D^\circ(30)):

$$
d\sim_{\pm}e
$$

if

$$
e=\frac{30}{d}
$$

and

$$
d\ne e.
$$

In the rank square-free there are 3 fixed points, so each complement-orbit has size (2).

### 4.6.3. Edges

$$
2-15,
\qquad
3-10,
\qquad
5-6.
$$

Total:

$$
(D^\circ(30),R_{\pm})
\cong
3K_2.
$$

### Theorem 4.6 [D]. The complement graph gives $3K_2$

$$
\boxed{
(D^\circ(30),R_{\pm})
\cong
3K_2.
}
$$

### Proof

Duality of divisors:

$$
d\mapsto30/d.
$$

Calculate:

$$
30/2=15,
$$

$$
30/3=10,
$$

$$
30/5=6.
$$

Inverse:

$$
30/15=2,
\qquad
30/10=3,
\qquad
30/6=5.
$$

Therefore (D^\circ(30)) is divided into three pairs:

$$
{2,15},
\qquad
{3,10},
\qquad
{5,6}.
$$

The graph relation contains exactly these three disjoint edges.

Consequently:

$$
(D^\circ(30),R_{\pm})
\cong
3K_2.
$$

$$
\blacksquare
$$

### 4.6.4. DOT-reading

This is an arithmetic addition-line:

```text
duality of divisors d ↦ 30/d
=
Boolean complement x -> x+111.
```

---

## §4.7. Relation-reading 4: Octahedral Graph ($K_{2,2,2}$)

### 4.7.1. Terminological clarification

This relation is not given a residue name. That name is reserved for the AMR-SR scalar residue.

Reason: There is already another object in AMR-SR:

$$
\mathrm{Res}_{\mathrm{sr}}=(g-1)|p-q|.
$$

Therefore, for the rank-3 divisor relation the name is used:

$$
R_{\mathrm{oct}}.
$$

Acceptable synonyms:

```text
octahedral relation;
interpair relation;
non-complement relation.
```

The main name in this document:

$$
R_{\mathrm{oct}}.
$$

### 4.7.2. Definition

**Definition 4.7 [D].**
The octahedral relation (R_{\mathrm{oct}}) on (D^\circ(30)) is given as follows:

$$
d\sim_{\mathrm{oct}}e
$$

if

$$
d\ne e
$$

and

$$
e\ne\frac{30}{d}.
$$

That is, we connect all the different vertices except addition-par.

Equivalent to:

$$
R_{\mathrm{oct}}
=
K_6
\setminus
R_{\pm}.
$$

### 4.7.3. Partitioning into complement pairs

Complement pairs:

$$
P_2={2,15},
$$

$$
P_3={3,10},
$$

$$
P_5={5,6}.
$$

They form partition:

$$
D^\circ(30)
=
P_2\sqcup P_3\sqcup P_5.
$$

B (R_{\mathrm{oct}}):

1. within each pair of edges are prohibited;
2. between different pairs all edges are allowed.

This means that the graph is a complete tripartite graph with shares of size (2):

$$
K_{2,2,2}.
$$

### 4.7.4. Edges

Full list of edges (R_{\mathrm{oct}}):

$$
2-3,
\quad
2-10,
\quad
2-5,
\quad
2-6,
$$

$$
15-3,
\quad
15-10,
\quad
15-5,
\quad
15-6,
$$

$$
3-5,
\quad
3-6,
$$

$$
10-5,
\quad
10-6.
$$

Total (12) edges.

This coincides with the number of edges ($K_{2,2,2}$):

$$
\frac12\cdot 3\cdot2\cdot(6-2)=12.
$$

### Theorem 4.8 [D]. The octahedral relation is given by $K_{2,2,2}$

$$
\boxed{
(D^\circ(30),R_{\mathrm{oct}})
\cong
K_{2,2,2}.
}
$$

### Proof

The complement relation (R_{\pm}) splits six vertices into three pairs:

$$
{2,15},
\qquad
{3,10},
\qquad
{5,6}.
$$

By definition (R_{\mathrm{oct}}) only forbidden:

1. loops (d=d);
2. pair of complement edges (d-30/d).

All other pairs of distinct vertices are connected.

Consequently, there is no edge inside each complement-share of size (2), and between any two different shares there are all edges.

This is the definition of a complete tripartite graph:

$$
K_{2,2,2}.
$$

$$
\blacksquare
$$

### 4.7.5. The multiplication relation by one in rank 3

In rank 3 is additionally true:

$$
R_{\mathrm{oct}}
=
R_{\mathrm{cov}}
\cup
R_{\mathrm{sh}}.
$$

Where:

$$
R_{\mathrm{cov}}=C_{30}^\circ,
$$

$$
R_{\mathrm{sh}}=\text{layer-internal relation}.
$$

Check:

* (R_{\mathrm{cov}}) gives (6) loop edges ($C_6$);
* (R_{\mathrm{sh}}) gives (6) edges ($K_3\sqcup K_3$);
* these two sets of edges do not intersect: $R_{\mathrm{cov}}$ connects the weights $1$ and $2$, and $R_{\mathrm{sh}}$ connects the vertices of the same weight;
* together (12) edges;
* this is exactly ($K_{2,2,2}$).

Then is:

$$
C_6
\cup
(K_3\sqcup K_3)
=
K_{2,2,2}
$$

on the same carrier (D^\circ(30)).

### 4.7.6. Status

Strict:

$$
K_6\setminus3K_2\cong K_{2,2,2}.
$$

Bridge:

```text
octahedral relation is an arithmetic interpair reading of
octahedral carrier DOT rank 3.
```

The relation-grammar of number (30) is constructed as one carrier $D^\circ(30)$ with different readings:

$$
C_6,
\quad
K_3\sqcup K_3,
\quad
3K_2,
\quad
K_{2,2,2}.
$$



---

## §4.8. Comparison with the strict core DOT

### 4.8.1. Side of the strict core

To the strict core of DOT:

$$
X_{\mathrm{adm}}
=
Q_3\setminus\{000,111\}.
$$

On this carrier the relation readings are specified:

$$
C_6,
\qquad
K_3\sqcup K_3,
\qquad
3K_2,
\qquad
K_{2,2,2}.
$$

In the mathematical bridge to the strict core this is formulated through the package relation (R_0,$R_1$,$R_2$,$R_3$): ($R_1$) gives ($C_6$), ($R_2$) gives ($K_3\sqcup K_3$), ($R_3$) gives ($3K_2$), and ($R_1$\cup $R_2$) gives ($K_{2,2,2}$).

### 4.8.2. AMR-DC side

In AMR-DC:

$$
D^\circ(30)
=
{2,3,5,6,10,15}.
$$

By Theorem 4.1:

$$
D^\circ(30)\cong X_{\mathrm{adm}}.
$$

Relation readings are set on this same carrier:

$$
C_{30}^\circ\cong C_6,
$$

$$
R_{\mathrm{sh}}\cong K_3\sqcup K_3,
$$

$$
R_{\pm}\cong3K_2,
$$

$$
R_{\mathrm{oct}}\cong K_{2,2,2}.
$$

### 4.8.3. Correspondence table

| strict core DOT | AMR-DC | graph |
| -------------------- | ---------------------------------------------------- | ---------------------- |
| ($X_{\mathrm{adm}}$) | (D^\circ(30)) | six-state carrier |
| ($R_1$) | cover by one prime factor (C_{30}^\circ) | ($C_6$) |
| ($R_2$) | layer-internal(R_{\mathrm{sh}}) | ($K_3\sqcup K_3$) |
| ($R_3$) | addition of divisors (R_{\pm}) | ($3K_2$) |
| ($R_1$\cup $R_2$) | octahedral (R_{\mathrm{oct}}) | ($K_{2,2,2}$) |

### 4.8.4. Interpretation

This is not just a coincidence of the number of vertices.

Coincid:

```text
carrier;
puncture;
layer decomposition;
pairing addition;
Hamming step 1 / transition by one prime factor;
octahedral interpair relation.
```

That is, $30$ implements not only the set $X_{\mathrm{adm}}$, but also the complete relation grammar of the strict rank-3 core.

### 4.8.5. Statement boundary

Strongly proven:

$$
D^\circ(30)
\cong
X_{\mathrm{adm}}
$$

and graph correspondences above.

Not automatically asserted:

```text
all meanings of D/F/C are derived from the arithmetic of the number 30;
AMR-SR is derived from D^\circ(30);
Res_sr coincides with R_oct;
beta_3, beta_4 are derived from the divisor carrier.
```

These statements refer to the future integration chapter §10.

---

## §4.9. Axial reading (3\times2)

### 4.9.1. Factorization by complement

The complement relation (R_{\pm}) splits (D^\circ(30)) into three pairs:

$$
{2,15},
\qquad
{3,10},
\qquad
{5,6}.
$$

Let us denote the factor-set complement-pair:

$$
I_{30}
=
D^\circ(30)/\delta_{30}.
$$

Then

$$
I_{30}
=
{\langle2\rangle,\langle3\rangle,\langle5\rangle},
$$

where

$$
\langle2\rangle={2,15},
$$

$$
\langle3\rangle={3,10},
$$

$$
\langle5\rangle={5,6}.
$$

### 4.9.2. Axial product form

After choosing a side in each complement pair, you can write:

$$
D^\circ(30)
\cong
I_{30}\times\{-,+\}.
$$

For example:

$$
(\langle2\rangle,-)\leftrightarrow2,
\qquad
(\langle2\rangle,+)\leftrightarrow15,
$$

$$
(\langle3\rangle,-)\leftrightarrow3,
\qquad
(\langle3\rangle,+)\leftrightarrow10,
$$

$$
(\langle5\rangle,-)\leftrightarrow5,
\qquad
(\langle5\rangle,+)\leftrightarrow6.
$$

This is an exact finite bijection after choosing an orientation convention.

### 4.9.3. Atom/coatom axis reading

There is a stronger way to write the same three complement pairs. Since

$$
\begin{aligned}
30 &= 2\cdot 3\cdot 5,
\end{aligned}
$$

each pair has the form

$$
\begin{aligned}
(p_i,\prod_{j\neq i}p_j).
\end{aligned}
$$

For the number \(30\), this gives

$$
\begin{aligned}
(2,3\cdot5) &\to \pm e_1,\\
(3,2\cdot5) &\to \pm e_2,\\
(5,2\cdot3) &\to \pm e_3.
\end{aligned}
$$

Thus each octahedral axis is not generated by an isolated prime alone. It is generated by a pair:

```text
one prime coordinate is manifested;
the complementary divisor holds the remaining two coordinates.
```

In Boolean-lattice language, the first entry is an atom and the second entry is the opposite coatom. In divisor language, this is exactly the duality

$$
\begin{aligned}
\delta_{30}(d) &= \frac{30}{d}.
\end{aligned}
$$

The octahedral reading appears when these atom/coatom pairs are read as antipodal poles. This does not claim that the divisor lattice by itself is the octahedral graph: the divisor order gives its own incidence structure. The octahedral relation is the additional interpair reading in which all distinct vertices are connected except the complement-pair partners.

The DOT reading is therefore:

```text
prime coordinate / complementary divisor
= manifested coordinate / holding complement
= one axis of the rank-3 octahedral carrier.
```

This paragraph has bridge status. The strict arithmetic statement is the complement involution \(d\mapsto30/d\); the manifested/holding language is the DOT reading of that arithmetic duality.

### 4.9.4. Bridge to $I_3\times\{-,+\}$

In the Hopf–Borromean layer of DOT, rank 3 is read as:

$$
X_{\mathrm{adm}}
\cong
I_3\times\{-,+\},
$$

where

$$
I_3=\{I_1,I_2,I_3\}.
$$

Meaning: three axial invariants, each with two polar manifestations. This formula is directly related to the initial motif $P=\{a,-a\}\to I$, but in rank-3 form.

AMR-DC gives the arithmetic avatar of this form:

$$
D^\circ(30)
\cong
I_{30}\times\{-,+\}.
$$

Bridge-identification:

$$
I_{30}=\{\langle2\rangle,\langle3\rangle,\langle5\rangle\}
\quad\leftrightarrow\quad
I_3=\{I_1,I_2,I_3\}.
$$

For example, after choosing the axial convention:

$$
\langle2\rangle\leftrightarrow I_1,
$$

$$
\langle3\rangle\leftrightarrow I_2,
$$

$$
\langle5\rangle\leftrightarrow I_3.
$$

Legacy-labels $D,F,C$ are not the strict names of this layer. If the target bridge layer has already entered such names, you can optionally specify a readable mapping

$$
\lambda:I_3\to\{D,F,C\}.
$$

Then entries of the form $I_D,I_F,I_C$ appear, but they refer to the selected readable layer, and not to the strict AMR-DC carrier.

### 4.9.5. Status

Strict:

$$
D^\circ(30)/\delta_{30}
$$

has three complement orbits.

Strictly after choosing a side:

$$
D^\circ(30)
\cong
I_{30}\times\{-,+\}.
$$

Bridge:

$$
I_{30}
\leftrightarrow
I_3=\{I_1,I_2,I_3\}.
$$

Consequently:

```text
$D^\circ(30)$ is strictly the carrier of three complement pairs;
its reading as three axial DOT invariants with two polar manifestations
has the status of a bridge, not a pure one arithmetic theorem.
```

---

# Short summary §3–§4

In §3 it is fixed:

$$
D^\circ(p_1\cdots p_n)
\cong
U_n
=
Q_n\setminus\{0^n,1^n\}.
$$

But:

$$
V_n
=
S_1^{(n)}\sqcup S_{n-1}^{(n)}.
$$

And only at rank 3:

$$
U_3=V_3.
$$

This explains the special status of the number (30).

In §4, a rank-3 AMR scene is constructed:

$$
30=2\cdot3\cdot5.
$$

$$
D^\circ(30)=\{2,3,5,6,10,15\}.
$$

$$
D^\circ(30)
\cong
Q_3\setminus\{000,111\}
=
X_{\mathrm{adm}}.
$$

Four relation readings are obtained on one carrier:

$$
(D^\circ(30),C_{30}^\circ)\cong C_6,
$$

$$
(D^\circ(30),R_{\mathrm{sh}})
\cong
K_3\sqcup K_3,
$$

$$
(D^\circ(30),R_{\pm})
\cong
3K_2,
$$

$$
(D^\circ(30),R_{\mathrm{oct}})
\cong
K_{2,2,2}.
$$

Main formula of the block:

$$
\boxed{
30
\text{is the first natural arithmetic avatar of the rank-3 valid scene DOT.}
}
$$

With clarification:

```text
not the only divisor carrier of rank 3;
the first natural square-free representative.
```

---

# §5. The general ladder of square-free numbers

In §4, the number

$$
30=2\cdot3\cdot5
$$

was singled out as the first natural representative of the rank-3 stage of divisors. Now we need to separate two facts:

```text
the structure depends on the number of distinct prime coordinates;
the specific natural representative depends on the choice of primes.
```

That is, (30) is important not because it alone gives rank 3, but because it gives the **minimal natural** rank-3 square-free carrier.

---

## §5.1. Arbitrary square-free number

### 5.1.1. Common square-free carrier

Let

$$
N=p_1p_2\cdots p_n,
$$

where

$$
p_1,\ldots,p_n
$$

are distinct prime numbers.

Then (N) is square-free, and by Theorem 2.3:

$$
\boxed{
D(N)\cong Q_n.
}
$$

After selection, the ordered prime basis

$$
(p_1,\ldots,p_n)
$$

isomorphism is given by the formula

$$
\theta_N(x_1,\ldots,x_n)
=
\prod_{i:x_i=1}p_i.
$$

Reverse reading:

$$
d\mapsto
(\mathbf 1_{p_1\mid d},\ldots,\mathbf 1_{p_n\mid d}).
$$

### 5.1.2. Structure and representative

If (N) is not a primorial number, the structure of the carrier does not change.

For example:

$$
42=2\cdot3\cdot7.
$$

Then

$$
D(42)
=
{1,2,3,6,7,14,21,42},
$$

and

$$
D(42)\cong Q_3.
$$

Proper carrier:

$$
D^\circ(42)={2,3,6,7,14,21}
$$

also has six elements and is isomorphic

$$
Q_3\setminus\{000,111\}.
$$

But (42) is not the first rank-3 representative, because that

$$
30=2\cdot3\cdot5<42.
$$

### Proposition 5.1 [D]. All $n$-prime numbers square-free carry $Q_n$

Let

$$
N=p_1\cdots p_n,
\qquad
M=q_1\cdots q_n
$$

be two square-free numbers with the same number of distinct prime factors.

Then after choosing the ordered prime bases:

$$
D(N)\cong Q_n\cong D(M).
$$

Therefore,

$$
D(N)\cong D(M)
$$

as Boolean carriers of the divisors.

### Proof

Each divisor (N) is specified by a subset of the set

$$
{p_1,\ldots,p_n}.
$$

Each divisor (M) is specified by a subset of the set

$$
{q_1,\ldots,q_n}.
$$

After choosing the order, both sets of subsets are coordinated through

$$
{0,1}^n.
$$

This means that both divisor carriers are isomorphic ($Q_n$), and therefore isomorphic to each other.

$$
\blacksquare
$$

### 5.1.4. AMR-reading

```text
Square-free AMR class of rank n
=
all square-free numbers with $n$ distinct by prime factors.
```

Within this class, different numbers give different natural representatives, but the same Boolean carrier type:

$$
Q_n.
$$

---

## §5.2. Primorial staircase

### 5.2.1. Definition

Let

$$
p_1=2,\quad p_2=3,\quad p_3=5,\quad p_4=7,\quad\ldots
$$

be a sequence of prime numbers.

**Definition 5.2 [D].**
Primorial representative rank (n) is given by a number

$$
P_n^#=p_1p_2\cdots p_n.
$$

That is,

$$
P_n^#
$$

is the product of the first (n) prime numbers.

### 5.2.2. Divisor carrier of the primorial

Since (P_n^#) is square-free, we have:

$$
\boxed{
D(P_n^#)\cong Q_n.
}
$$

This gives a natural ladder of minimal representatives of Boolean carriers.

|  (n) | (P_n^#) | carrier |
| ---: | ------: | -------- |
|  (1) |     (2) | (Q_1)    |
|  (2) |     (6) | (Q_2)    |
|  (3) |    (30) | ($Q_3$)  |
|  (4) |   (210) | (Q_4)    |
|  (5) |  (2310) | (Q_5)    |

### Proposition 5.3 [D]. Minimality of the primorial

Among square-free numbers with (n) different prime factors, the minimum is

$$
P_n^#=p_1p_2\cdots p_n.
$$

### Proof

Let

$$
N=q_1q_2\cdots q_n
$$

be a number without square factors with (n) different prime factors, written in ascending order:

$$
q_1<q_2<\cdots<q_n.
$$

Then for each (i):

$$
q_i\ge p_i,
$$

because (p_i) - (i)th prime number.

Hence,

$$
N=q_1\cdots q_n
\ge
p_1\cdots p_n
=
P_n^#.
$$

Equality is possible only if

$$
q_i=p_i
$$

for all (i).

So, (P_n^#) is the minimum natural representative rank (n).

$$
\blacksquare
$$

### 5.2.4. Interpretation

Primorial ladder gives the canonical natural sequence:

$$
2,\ 6,\ 30,\ 210,\ 2310,\ldots
$$

and the corresponding Boolean ladder:

$$
Q_1,\ Q_2,\ Q_3,\ Q_4,\ Q_5,\ldots
$$

AMR-reading:

```text
P_n^# is the first natural arithmetic representative of $Q_n$.
```

Especially:

$$
30=P_3^#
$$

is the first representative of a strict admissible scene of rank 3.

---

## §5.3. Proper ladder

### 5.3.1. The proper primorial carrier

For primorial representative

$$
P_n^#=p_1\cdots p_n
$$

the proper divisor carrier:

$$
D^\circ(P_n^#)
=
D(P_n^#)\setminus\{1,P_n^#\}.
$$

By the square-free compatibility theorem:

$$
\boxed{
D^\circ(P_n^#)
\cong
Q_n\setminus\{0^n,1^n\}.
}
$$

Denote:

$$
U_n=Q_n\setminus\{0^n,1^n\}.
$$

Then:

$$
\boxed{
D^\circ(P_n^#)\cong U_n.
}
$$

This is exactly the one ($U_n$), which in the shell continuation is separated from the strict outer layer ($V_n$): the full cube ($Q_n$), the full non-trivial package ($U_n$) and the outer layer ($V_n$) do not mix.

### 5.3.2. Size

Since

$$
|Q_n|=2^n,
$$

and two points are removed

$$
0^n,\quad1^n,
$$

then

$$
\boxed{
|D^\circ(P_n^#)|=|U_n|=2^n-2.
}
$$

Examples:

$$
n=1:
\quad
2^1-2=0.
$$

$$
n=2:
\quad
2^2-2=2.
$$

$$
n=3:
\quad
2^3-2=6.
$$

$$
n=4:
\quad
2^4-2=14.
$$

$$
n=5:
\quad
2^5-2=30.
$$

### 5.3.3. Table

|  (n) | (P_n^#) | (D^\circ(P_n^#)) size | Boolean form |
| ---: | ------: | --------------------: | --------------------------------- |
|  (1) |     (2) |                   (0) | (U_1=\varnothing)                 |
|  (2) |     (6) |                   (2) | (U_2=Q_2\setminus\{00,11\})       |
|  (3) |    (30) |                   (6) | (U_3=$Q_3$\setminus\{000,111\})   |
|  (4) |   (210) |                  (14) | (U_4=Q_4\setminus\{0000,1111\})   |
|  (5) |  (2310) |                  (30) | (U_5=Q_5\setminus\{00000,11111\}) |

### 5.3.4. Warning

An proper ladder gives $U_n$, not $V_n$:

$$
D^\circ(P_n^#)\cong U_n.
$$

This does not automatically match:

$$
V_n=S_1^{(n)}\sqcup S_{n-1}^{(n)}.
$$

For (n=3) they agree:

$$
U_3=V_3.
$$

For (n\ge4) they diverge:

$$
U_n\neq V_n.
$$

This was already a key warning of §3 and should be maintained in all further chapters.

### Lemma 5.3.5 [D]. Connectedness of the proper cubic support

For $n\ge3$ the induced Hamming-1 graph is

$$
U_n=Q_n\setminus\{0^n,1^n\}
$$

connected.

### Proof

Let us identify the vertices of $Q_n$ with the subsets of $\{1,\ldots,n\}$. Then $U_n$ consists of all non-empty proper subsets.

We show that any vertex is connected by a path to $\{1\}$. If the subset $S$ contains $1$, then we sequentially remove all elements $S\setminus\{1\}$; at each step a non-empty proper subset remains. If $1\notin S$ and $S\ne\{2,\ldots,n\}$, first add $1$ and then remove the extra elements. If $S=\{2,\ldots,n\}$, first remove any element, then add $1$, then remove other unnecessary elements. When $n\ge3$ all intercarrierte sets remain in $U_n$.

Consequently, each vertex $U_n$ is connected to $\{1\}$, and the induced graph is connected.

---

## §5.4. Outer layer ladder

### 5.4.1. Definition of $V_n$

For (n\ge3) the strict outer layer is defined as

$$
V_n=S_1^{(n)}\sqcup S_{n-1}^{(n)}.
$$

Here

$$
S_k^{(n)}={x\in Q_n:w(x)=k}.
$$

That is, ($V_n$) contains only two layers:

```text
weight 1;
weight n-1.
```

In the shell continuation, it is ($V_n$) that serves as a strict external cross-polytopic carrier, while ($U_n$) is a broader non-trivial package. This distinction is explicitly captured in the layer-extension corpus.

### 5.4.2. Form through divisors for $V_n$

Let

$$
N=p_1p_2\cdots p_n
$$

square-free.

Then the layer (S_1^{(n)}) corresponds to one-prime divisors:

$$
S_1^{(n)}
\leftrightarrow
{p_1,\ldots,p_n}.
$$

The layer (S_{n-1}^{(n)}) corresponds to divisors with one missing prime factor:

$$
S_{n-1}^{(n)}
\leftrightarrow
\left\{
\frac{N}{p_1},\ldots,\frac{N}{p_n}
\right\}.
$$

Consequently, in AMR-DC:

$$
\boxed{
V_n
\leftrightarrow
V(N)
=
{p_i:1\le i\le n}
\cup
{N/p_i:1\le i\le n}.
}
$$

### 5.4.3. Size

For (n\ge3) the sets

$$
S_1^{(n)}
\quad
\text{and}
\quad
S_{n-1}^{(n)}
$$

do not intersect.

Therefore:

$$
|V_n|
=
|S_1^{(n)}|+|S_{n-1}^{(n)}|
=
n+n
=
2n.
$$

That is:

$$
\boxed{
|V_n|=2n
\quad(n\ge3).
}
$$

Examples:

$$
|V_3|=6,
$$

$$
|V_4|=8,
$$

$$
|V_5|=10.
$$

### 5.4.4. Complement pairs on $V_n$

Boolean complement:

$$
x\mapsto \bar x=x+1^n
$$

translates

$$
S_1^{(n)}
$$

to

$$
S_{n-1}^{(n)}.
$$

In divisor language:

$$
p_i
\longleftrightarrow
\frac{N}{p_i}.
$$

Therefore ($V_n$) is split into (n) complement pairs:

$$
\left\{p_1,\frac{N}{p_1}\right\},
\ldots,
\left\{p_n,\frac{N}{p_n}\right\}.
$$

### 5.4.5. Interpair / octahedral relation on $V_n$

On ($V_n$) we can define in general the interpair relation:

$$
x\sim_{\mathrm{cross}}y
$$

if

$$
x\ne y
$$

and

$$
y\ne \bar x.
$$

In the form of divisors:

$$
d\sim_{\mathrm{cross}}e
$$

if

$$
d\ne e
$$

and

$$
e\ne \frac{N}{d}.
$$

That is, all different vertices are connected, except for the complement pair.

Since ($V_n$) is split into (n) complement-pairs of size (2), this graph reading gives a complete (n)-partite graph:

$$
\boxed{
K_{2,2,\ldots,2}
}
$$

with (n) shares.

For (n=3):

$$
K_{2,2,2}.
$$

For (n=4):

$$
K_{2,2,2,2}.
$$

This is exactly the general layer-law that is formulated in `02B` for the external carrier ($V_n$): the complement splits ($V_n$) into (n) pairs, and the interpair ratio gives (K_{2,2,\dots,2}).

### 5.4.6. Relation to proper ladder

There are two different ladders.

First:

$$
D^\circ(P_n^#)\cong U_n.
$$

This is a complete nontrivial package of divisors.

Second:

$$
V(P_n^#)
=
{p_i}\cup{P_n^#/p_i}
\cong V_n.
$$

This is the outer-layer package.

At (n=3):

$$
D^\circ(30)=V(30).
$$

At (n\ge4):

$$
V(P_n^#)\subsetneq D^\circ(P_n^#).
$$

For example, at (n=4):

$$
D^\circ(210)
$$

has (14) elements, and

$$
V(210)
$$

has (8) elements:

$$
V(210)=
{2,3,5,7,105,70,42,30}.
$$

---

## §5.5. Rank-3 coincidence theorem

### Theorem 5.4 [D|K]. Match at rank 3

$$
\boxed{
U_3=V_3.
}
$$

### Proof

By definition:

$$
U_3=Q_3\setminus\{000,111\}.
$$

Hamming layer expansion:

$$
Q_3
=
S_0^{(3)}
\sqcup
S_1^{(3)}
\sqcup
S_2^{(3)}
\sqcup
S_3^{(3)}.
$$

Here

$$
S_0^{(3)}={000},
\qquad
S_3^{(3)}={111}.
$$

Therefore,

$$
U_3
=
S_1^{(3)}\sqcup S_2^{(3)}.
$$

But

$$
V_3
=
S_1^{(3)}\sqcup S_{3-1}^{(3)}
=
S_1^{(3)}\sqcup S_2^{(3)}.
$$

So,

$$
U_3=V_3.
$$

$$
\blacksquare
$$

### 5.5.1. Meaning

```text
Rank 3 is special because the proper divisor carrier already equals the outer layer.
```

In AMR-DC this means:

$$
D^\circ(30)
\cong
U_3
=
V_3
X_{\mathrm{adm}}.
$$

That is, the number (30) simultaneously realizes:

```text
proper divisor package;
punctured Boolean carrier;
external cross-polytopic layer;
strict rank-3 valid scene.
```

At (n\ge4) these roles diverge.

---

# §6. Chain extension: numbers with multiplicities

Until now, the main strict core of AMR-DC was built on square-free numbers:

$$
N=p_1\cdots p_n.
$$

Now we return to the general case:

$$
N=p_1^{a_1}\cdots p_r^{a_r}.
$$

Here the coordinates cease to be binary. Each prime coordinate (p_i) receives not two states, but a chain of length (a_i+1):

$$
0,1,\ldots,a_i.
$$

This is no longer a Boolean carrier ($Q_n$), but a product of carrier chains.

Numbers with multiplicities realize products of chains, and the Boolean case is obtained at $a_i=1$ for all coordinates.

---

## §6.1. General carrier

### 6.1.1. Formula

Let

$$
N=p_1^{a_1}\cdots p_r^{a_r}.
$$

Then by Theorem 1.4:

$$
\boxed{
D(N)\cong
\prod_{i=1}^{r}{0,1,\ldots,a_i}.
}
$$

Each divisor

$$
d\mid N
$$

has the form

$$
d=p_1^{b_1}\cdots p_r^{b_r},
$$

where

$$
0\le b_i\le a_i.
$$

Exponent vector:

$$
\eta_N(d)=(b_1,\ldots,b_r).
$$

### 6.1.2. Boolean core as a special case

If

$$
a_1=\cdots=a_r=1,
$$

then

$$
{0,\ldots,a_i}={0,1}.
$$

Therefore:

$$
D(p_1\cdots p_r)
\cong
{0,1}^r
=
Q_r.
$$

That is:

$$
\boxed{
\text{Boolean core is a special case}a_i=1.
}
$$

### 6.1.3. Chain extension reading

In chain extension the coordinate (p_i) has not only two states:

```text
absent / present,
```

but several degrees of presence:

$$
0,1,\ldots,a_i.
$$

AMR-reading:

```text
prime factor = coordinate;
exponent = depth along the coordinate;
divisor = point in the product of chains;
multiplicity = internal depth of the coordinate.
```

### 6.1.4. Example

Let

$$
N=12=2^2\cdot3.
$$

Then

$$
D(12)\cong{0,1,2}\times{0,1}.
$$

Table:

| exponent vector | divisor |
| ------------------ | -------: |
| ((0,0))            |      (1) |
| ((1,0))            |      (2) |
| ((2,0))            |      (4) |
| ((0,1))            |      (3) |
| ((1,1))            |      (6) |
| ((2,1))            |     (12) |

Here coordinate (2) has depth (2), and coordinate (3) remains Boolean.

---

## §6.2. Two types of growth

Chain expansion introduces a difference that was not present in a pure Boolean ladder.

There are two different ways to expand a carrier:

```text
increase in rank;
increase in depth.
```

They cannot be mixed.

---

### 6.2.1. Type A: adding a new coordinate

Let

$$
N=p_1^{a_1}\cdots p_r^{a_r},
$$

and let (p_{r+1}) be a new prime factor that does not divide (N).

Transition:

$$
N\mapsto Np_{r+1}.
$$

Then:

$$
D(N)
\cong
\prod_{i=1}^{r}{0,\ldots,a_i},
$$

a

$$
D(Np_{r+1})
\cong
\left(
\prod_{i=1}^{r}{0,\ldots,a_i}
\right)
\times
{0,1}.
$$

That is, a new Boolean coordinate is added.

This is **growth rank**:

```text
new prime factor = new coordinate;
former carrier doubles;
the previous states are repeated without and with a new prime factor.
```

In the language of exponents:

$$
(b_1,\ldots,b_r)
\mapsto
(b_1,\ldots,b_r,0)
$$

and

$$
(b_1,\ldots,b_r)
\mapsto
(b_1,\ldots,b_r,1).
$$

### 6.2.2. Type B: increasing the depth of the existing coordinate

Let now (p_i) already divide (N).

Transition:

$$
p_i^{a_i}
\mapsto
p_i^{a_i+1}.
$$

That is,

$$
N
=
p_1^{a_1}\cdots p_i^{a_i}\cdots p_r^{a_r}
$$

transitions to

$$
N'
=
p_1^{a_1}\cdots p_i^{a_i+1}\cdots p_r^{a_r}.
$$

The carrier changes like this:

$$
{0,\ldots,a_i}
\mapsto
{0,\ldots,a_i+1}.
$$

Completely:

$$
D(N')
\cong
{0,\ldots,a_1}
\times\cdots\times
{0,\ldots,a_i+1}
\times\cdots\times
{0,\ldots,a_r}.
$$

This is **increase in depth**:

```text
the previous coordinate becomes longer;
the rank does not increase;
the depth of the coordinate increases.
```

### 6.2.3. Rank growth and depth growth

So:

| growth type | arithmetic move | carrier change | DOT-reading |
| --------- | ------------------------------ | ------------------ | ------------ |
| Type A | (N\mapsto Np_{r+1}) | add $\{0,1\}$ | rank growth |
| Type B | (p_i^{a_i}\mapsto p_i^{a_i+1}) | lengthen one chain | depth increase |

### 6.2.4. Principle

$$
\boxed{
\text{A chain extension of DOT must distinguish between rank growth and depth growth.}
}
$$

increasing rank adds a new independent prime coordinate.

increasing depth deepens an already existing coordinate.

The Boolean core uses Type A. Chain expansion adds Type B.

---

## §6.3. Cover graph

### 6.3.1. Statement

For

$$
N=p_1^{a_1}\cdots p_r^{a_r}
$$

the covering graph of the divisor carrier:

$$
(D(N),C_N)
$$

is isomorphic to the Cartesian product of paths:

$$
\boxed{
(D(N),C_N)
\cong
P_{a_1+1}\square\cdots\square P_{a_r+1}.
}
$$

This has already been proven in §1.5. Here the formula receives a chain extension interpretation.

### 6.3.2. Sketch of the proof

Exponent carrier:

$$
E(N)=\prod_{i=1}^{r}{0,\ldots,a_i}.
$$

Cover step changes exactly one coordinate:

$$
b_i\mapsto b_i+1
$$

or in undirected reading

$$
b_i\mapsto b_i\pm1.
$$

Each coordinate

$$
{0,\ldots,a_i}
$$

with adjacent transitions is a path:

$$
P_{a_i+1}.
$$

If the product carrier is allowed to change exactly one coordinate to the adjacent one, a Cartesian product is obtained paths:

$$
P_{a_1+1}\square\cdots\square P_{a_r+1}.
$$

$$
\blacksquare
$$

### 6.3.3. Examples

If

$$
N=30=2\cdot3\cdot5,
$$

then

$$
a_1=a_2=a_3=1,
$$

and

$$
(D(30),C_{30})
\cong
P_2\square P_2\square P_2
=
Q_3.
$$

If

$$
N=12=2^2\cdot3,
$$

then

$$
(D(12),C_{12})
\cong
P_3\square P_2.
$$

This is a rectangular grid structure (3\times2).

If

$$
N=72=2^3\cdot3^2,
$$

then

$$
(D(72),C_{72})
\cong
P_4\square P_3.
$$

This is a grid (4\times3).

### 6.3.4. DOT-reading

```text
boolean cover graph = hypercube;
chain cover graph = product of paths.
```

That is, the chain extension replaces the cubic Boolean geometry with a finite lattice geometry.

---

## §6.4. Duality and fixed points

### 6.4.1. Duality of divisors

For any

$$
N=p_1^{a_1}\cdots p_r^{a_r}
$$

duality of divisors:

$$
\delta_N(d)=\frac{N}{d}.
$$

If

$$
d=p_1^{b_1}\cdots p_r^{b_r},
$$

then

$$
\delta_N(d)
=
p_1^{a_1-b_1}\cdots p_r^{a_r-b_r}.
$$

In coordinates:

$$
(b_1,\ldots,b_r)
\mapsto
(a_1-b_1,\ldots,a_r-b_r).
$$

### 6.4.2. Fixed point condition

Fixed point duality of divisors means:

$$
\delta_N(d)=d.
$$

That is:

$$
\frac{N}{d}=d.
$$

Therefore:

$$
d^2=N.
$$

In coordinates this means:

$$
b_i=a_i-b_i
$$

for all (i), that is

$$
2b_i=a_i.
$$

Means:

$$
b_i=\frac{a_i}{2}.
$$

### Theorem 6.1 [D]. Fixed point criterion

Duality of divisors (\delta_N) has a fixed point if and only if (N) is a square.

In this case the fixed point is unique and equal to:

$$
d=\sqrt N.
$$

### Proof

If (d) fixed, then

$$
d=N/d,
$$

means

$$
d^2=N.
$$

Hence, (N) is square.

Conversely, if (N) is a square, then all exponents (a_i) are even:

$$
a_i=2m_i.
$$

Then

$$
d=p_1^{m_1}\cdots p_r^{m_r}
=
\sqrt N.
$$

And

$$
\delta_N(d)=N/d=d.
$$

Uniqueness follows from the coordinate equality

$$
b_i=a_i/2.
$$

$$
\blacksquare
$$

### 6.4.3. Boolean case

In the square-free case:

$$
a_i=1.
$$

All exponents are odd. Therefore there is no fixed point.

This corresponds to the Boolean complement:

$$
x\mapsto x+1^n,
$$

which has no fixed points on ($Q_n$).

### 6.4.4. Example

Let

$$
N=36=2^2\cdot3^2.
$$

Then

$$
D(36)\cong{0,1,2}\times{0,1,2}.
$$

Fixed point:

$$
(1,1)
\leftrightarrow
2\cdot3=6.
$$

And indeed:

$$
\delta_{36}(6)=36/6=6.
$$

---

## §6.5. Separation of layers

### 6.5.1. Two layer readings

In the chain extension you need to distinguish:

$$
\Omega_N(d)=\sum_i b_i
$$

and

$$
\omega_N(d)=|{i:b_i>0}|.
$$

Here:

```text
Ω_N counts total multiplicity;
$\omega_N$ counts active coordinates.
```

In the square-free case:

$$
\Omega_N=\omega_N.
$$

In the chain case they diverge.

### 6.5.2. Example: $N=72$

Let

$$
N=72=2^3\cdot3^2.
$$

Then

$$
D(72)\cong{0,1,2,3}\times{0,1,2}.
$$

Coordinates:

$$
d=2^{b_1}3^{b_2}.
$$

Reading table:

|   divisor $d$ | exponent vector | (\Omega_N(d)) | (\omega_N(d)) | support |
| -------------: | ------------------ | ------------: | ------------: | --------- |
|        (8=2^3) | ((3,0))            |           (3) |           (1) | ({2})     |
|        (9=3^2) | ((0,2))            |           (2) |           (1) | ({3})     |
| (12=2^2\cdot3) | ((2,1))            |           (3) |           (2) | ({2,3})   |
| (18=2\cdot3^2) | ((1,2))            |           (3) |           (2) | ({2,3})   |

Here:

$$
8
$$

and

$$
12
$$

have the same total multiplicity layer:

$$
\Omega=3,
$$

but different layers of active coordinates layers:

$$
\omega(8)=1,
\qquad
\omega(12)=2.
$$

Also

$$
12
$$

and

$$
18
$$

have the same readings:

$$
\Omega=3,\qquad \omega=2,\qquad \mathrm{supp}=\{2,3\}.
$$

but differ in the distribution of multiplicities:

$$
(2,1)\ne(1,2).
$$

Consequently, reading

$$
\Omega,\quad \omega,\quad \mathrm{supp}
$$

not accurate in the chain case. Exact recovery provides only the full exponent vector.

### 6.5.3. Interpretation

Chain expansion introduces several layers of information:

```text
full depth;
active support;
exact exponent profile.
```

the Boolean core compresses these levels into one, because each coordinate has only values ​​(0) and (1).

---

## §6.6. Status

### 6.6.1. Strict status

Strict arithmetic part:

$$
D(p_1^{a_1}\cdots p_r^{a_r})
\cong
\prod_i{0,\ldots,a_i}.
$$

$$
(D(N),C_N)
\cong
P_{a_1+1}\square\cdots\square P_{a_r+1}.
$$

$$
\delta_N(d)=N/d
$$

is an involution that reverses the order.

Fixed point criterion:

$$
\delta_N(d)=d
\Longleftrightarrow
d^2=N.
$$

These statements are ordinary finite arithmetic and combinatorics.

### 6.6.2. Bridge and horizontal status

Bridge reading:

```text
the divisor carrier as a product of chains is an arithmetic extension of the DOT Boolean core.
```

Horizon reading:

```text
a chain extension of DOT must develop internal relation reads,
layer readings and recovery rules for carriers-products of chains.
```

Final status:

$$
\boxed{
\text{Chain extension is strictly like finite lattice arithmetic.}
}
$$

$$
\boxed{
\text{Its interpretation as a chain extension of DOT has a bridge or horizontal status.}
}
$$

---

# §7. Multiplicative operations on the divisor carrier

Until now, the divisor carrier was considered as:

```text
set;
lattice;
covering graph;
dual structure;
layer carrier.
```

Now the multiplicative layer itself is introduced.

It is important not to mix:

$$
\gcd/\mathrm{lcm}
$$

as lattice operations and

$$
de
$$

as a multiplicative operation.

On (D(N)), the usual product of divisors does not always remain a divisor (N). Therefore, multiplication becomes a partial operation.

---

## §7.1. gcd and lcm as lattice operations

### 7.1.1. Intersection and union

On the lattice of divisors:

$$
(D(N),\mid)
$$

we have:

$$
d\wedge e=\gcd(d,e),
$$

$$
d\vee e=\mathrm{lcm}(d,e).
$$

In coordinates:

$$
\eta_N(d)=(b_1,\ldots,b_r),
$$

$$
\eta_N(e)=(c_1,\ldots,c_r).
$$

Then:

$$
\eta_N(d\wedge e)
=
(\min(b_i,c_i))_{i=1}^{r},
$$

$$
\eta_N(d\vee e)
=
(\max(b_i,c_i))_{i=1}^{r}.
$$

### 7.1.2. Lattice operations are total

For any

$$
d,e\in D(N)
$$

both elements

$$
\gcd(d,e)
$$

and

$$
\mathrm{lcm}(d,e)
$$

again lie in

$$
D(N).
$$

Therefore $\wedge$ and $\vee$ are total operations:

$$
\wedge,\vee:D(N)\times D(N)\to D(N).
$$

### 7.1.3. Multiplication works differently

Ordinary product:

$$
de
$$

may not divide (N).

Example:

$$
N=12.
$$

$$
4,6\in D(12),
$$

but

$$
4\cdot6=24
$$

and

$$
24\nmid12.
$$

This means that multiplication is not a total operation on $D(N)$.

In this case,

$$
\mathrm{lcm}(4,6)=12
$$

remains inside (D(12)).

Consequently:

```text
The lcm always remains internal;
the product remains internal only if the capacity condition is met.
```

---

## §7.2. Partial multiplication

### 7.2.1. Definition

**Definition 7.1 [D].**
Partial multiplication on the divisor carrier $D(N)$ is given as follows:

$$
d\odot_N e=de
$$

if

$$
de\mid N.
$$

If

$$
de\nmid N,
$$

then

$$
d\odot_N e
$$

is not defined.

Writing:

$$
\odot_N:D(N)\times D(N)\dashrightarrow D(N).
$$

Here

$$
\dashrightarrow
$$

means partial display.

### 7.2.2. Coordinate form

Let

$$
N=p_1^{a_1}\cdots p_r^{a_r}.
$$

Let

$$
d=p_1^{b_1}\cdots p_r^{b_r},
$$

$$
e=p_1^{c_1}\cdots p_r^{c_r}.
$$

Then

$$
de
=
p_1^{b_1+c_1}\cdots p_r^{b_r+c_r}.
$$

Condition

$$
de\mid N
$$

is equivalent to:

$$
b_i+c_i\le a_i
\quad
\text{for all}i.
$$

That is:

$$
\boxed{
d\odot_N e\text{ is defined}
\Longleftrightarrow
\eta_N(d)+\eta_N(e)\le(a_1,\ldots,a_r)
}
$$

coordinatewise.

If the operation is defined, then:

$$
\eta_N(d\odot_N e)
=
\eta_N(d)+\eta_N(e).
$$

### 7.2.3. Capacity condition

In AMR-DC this condition can be read as capacity condition:

```text
two divisor state can be multiplied inside N
only if their exponent profiles do not exceed the coordinate capacities $N$.
```

Coordinate capacity of a number (N):

$$
\mathbf a=(a_1,\ldots,a_r).
$$

Two states

$$
\mathbf b,\mathbf c
$$

are compatible for product assembly if:

$$
\mathbf b+\mathbf c\le\mathbf a.
$$

### Theorem 7.2 [D]. ((D(N),\odot_N,1)) is a partial commutative monoid

On the full divisor carrier (D(N)), the operation

$$
\odot_N
$$

gives a partial commutative monoid with identity (1).

### Proof

Let

$$
\eta_N(d)=\mathbf b,
\quad
\eta_N(e)=\mathbf c,
\quad
\eta_N(f)=\mathbf h,
\quad
\mathbf a=(a_1,\ldots,a_r).
$$

#### 1. Commutativity

If

$$
d\odot_N e
$$

is defined, then

$$
\mathbf b+\mathbf c\le\mathbf a.
$$

But

$$
\mathbf b+\mathbf c=\mathbf c+\mathbf b.
$$

So,

$$
e\odot_N d
$$

is also defined, and

$$
d\odot_N e=de=ed=e\odot_N d.
$$

#### 2. Unit

For

$$
1\in D(N)
$$

we have a vector of exponents:

$$
\eta_N(1)=(0,\ldots,0).
$$

For any (d\in D(N)):

$$
\eta_N(1)+\eta_N(d)=\eta_N(d)\le\mathbf a.
$$

So,

$$
1\odot_N d=d,
\qquad
d\odot_N1=d.
$$

#### 3. Associativity where defined

Consider three elements (d,e,f).

The operation

$$
(d\odot_N e)\odot_N f
$$

is defined if and only if

$$
\mathbf b+\mathbf c+\mathbf h\le\mathbf a.
$$

Indeed, if the total sum does not exceed (\mathbf a), then the intercarrierte sum

$$
\mathbf b+\mathbf c
$$

also does not exceed (\mathbf a), because all coordinates are non-negative.

Similarly,

$$
d\odot_N(e\odot_N f)
$$

is defined if and only if, when

$$
\mathbf b+\mathbf c+\mathbf h\le\mathbf a.
$$

In both cases the result has a vector of exponents:

$$
\mathbf b+\mathbf c+\mathbf h.
$$

Hence,

$$
(d\odot_N e)\odot_N f
=
d\odot_N(e\odot_N f)
$$

everywhere one of the sides is defined.

So,

$$
(D(N),\odot_N,1)
$$

is a partial commutative monoid.

$$
\blacksquare
$$

### 7.2.4. Square-free case

If

$$
N=p_1\cdots p_n
$$

square-free, then

$$
a_i=1.
$$

Condition

$$
b_i+c_i\le1
$$

means:

```text
d and e have disjoint prime support.
```

Consequently, in the square-free case:

$$
d\odot_N e
$$

is defined if and only if

$$
\gcd(d,e)=1.
$$

If defined, then:

$$
d\odot_N e=de=\mathrm{lcm}(d,e).
$$

That is, in a Boolean carrier square-free, the partial multiplication coincides with union of disjoint support.

### 7.2.5. Example: $N=30$

$$
D(30)=\{1,2,3,5,6,10,15,30\}.
$$

On its proper carrier

$$
D^\circ(30)=\{2,3,5,6,10,15\}
$$

some products are defined:

$$
2\odot_{30}3=6,
$$

$$
2\odot_{30}5=10,
$$

$$
3\odot_{30}5=15,
$$

$$
2\odot_{30}15=30,
$$

$$
3\odot_{30}10=30,
$$

$$
5\odot_{30}6=30.
$$

And some are not defined:

$$
2\odot_{30}6
$$

not defined, because

$$
2\cdot6=12
$$

and

$$
12\nmid30.
$$

$$
6\odot_{30}10
$$

not defined, because

$$
6\cdot10=60
$$

and

$$
60\nmid30.
$$

---

## §7.3. Complement pairs as maximal products

### 7.3.1. Product of complement

For any

$$
d\in D(N)
$$

we have:

$$
\delta_N(d)=\frac Nd.
$$

Then:

$$
d\odot_N\delta_N(d)
=
d\cdot\frac Nd
=
N.
$$

That is:

$$
\boxed{
d\odot_N\frac Nd=N.
}
$$

### 7.3.2. Coordinate form

Let

$$
\eta_N(d)=\mathbf b=(b_1,\ldots,b_r).
$$

Then

$$
\eta_N(\delta_N(d))
=
\mathbf a-\mathbf b
=
(a_1-b_1,\ldots,a_r-b_r).
$$

Sum:

$$
\mathbf b+(\mathbf a-\mathbf b)=\mathbf a.
$$

This is exactly the upper pole:

$$
\eta_N(N)=\mathbf a.
$$

### Proposition 7.3 [D]. Complement pairs are maximal admissible products

For every

$$
d\in D(N)
$$

pair

$$
\left(d,\frac Nd\right)
$$

is a maximal product pair within (D(N)):

$$
d\odot_N\frac Nd=N.
$$

If

$$
d\odot_N e=N,
$$

then

$$
e=\frac Nd.
$$

### Proof

First statement:

$$
d\odot_N\frac Nd
=
d\cdot\frac Nd
N.
$$

Now let

$$
d\odot_N e=N.
$$

Then by definition operations:

$$
de=N.
$$

Since (d>0), we get:

$$
e=N/d.
$$

$$
\blacksquare
$$

### 7.3.3. AMR reading

```text
complement pair is the maximum valid product.
```

In the square-free Boolean case, this coincides with the fact that the complement-support complements the support to the full set of coordinates.

For

$$
N=30
$$

complement-products:

$$
2\odot_{30}15=30,
$$

$$
3\odot_{30}10=30,
$$

$$
5\odot_{30}6=30.
$$

These are the same three complement-pairs:

$$
2\leftrightarrow15,
\qquad
3\leftrightarrow10,
\qquad
5\leftrightarrow6.
$$

---

## §7.4. Leakage limit

### 7.4.1. Closing a full carrier

On a full (D(N)):

$$
\odot_N:D(N)\times D(N)\dashrightarrow D(N)
$$

is correct as a partial operation.

If the operation is defined, the result always lies in the full carrier:

$$
d\odot_N e\in D(N).
$$

But if you go to your proper carrier:

$$
D^\circ(N)=D(N)\setminus\{1,N\},
$$

then the operation is no longer closed within the active scene.

### 7.4.2. Leakage to the upper pole

Let

$$
d,e\in D^\circ(N).
$$

It may turn out that

$$
d\odot_N e=N.
$$

Then the inputs are in the active proper scene, and the result falls into the upper boundary pole.

Example:

$$
2,15\in D^\circ(30),
$$

but

$$
2\odot_{30}15=30.
$$

And

$$
30\notin D^\circ(30).
$$

Consequently:

$$
\odot_N:
D^\circ(N)\times D^\circ(N)
\dashrightarrow
D(N),
$$

and not at all

$$
D^\circ(N)\times D^\circ(N)
\dashrightarrow
D^\circ(N).
$$

### 7.4.3. The lower boundary output does not occur in forward multiplication

If

$$
d,e\in D^\circ(N),
$$

then

$$
d>1,
\qquad
e>1.
$$

Hence,

$$
de>1.
$$

Therefore, forward partial multiplication cannot produce the lower pole:

$$
d\odot_N e\ne1.
$$

That is, for the normal product operation, it is possible to leak into the upper pole, but not the lower boundary output.

The lower pole can only appear in other readings, for example through a reverse construction, a reading factor, or a return to the complete carrier with the unit included. For $\odot_N$ on proper positive divisors there is no lower exit to the boundary.

### 7.4.4. The proper carrier is not a monoid

On

$$
D(N)
$$

there is a unit:

$$
1.
$$

On

$$
D^\circ(N)
$$

one is removed.

Therefore, even if we restrict $\odot_N$ only to those pairs whose result remains proper, the structure

$$
D^\circ(N)
$$

is not a monoid.

Reasons:

1. no unit (1);
2. the operation is partial;
3. products can extend into the pole boundary (N).

### 7.4.5. Boundary principle

$$
\boxed{
\text{partial multiplication requires full support}D(N)\text{as a boundary closures.}
}
$$

Active proper scene:

$$
D^\circ(N)
$$

useful for valid/mixed reading.

But multiplicative closure requires remembering the full carrier:

$$
D(N)=D^\circ(N)\sqcup{1,N}.
$$

### 7.4.6. DOT-reading

In DOT-language:

```text
proper scene is active;
boundary poles are not active;
operations may still terminate at border.
```

This is exactly the same logic that was recorded in the puncture:

```text
removed from active scene ≠ destroyed from full carrier.
```

For AMR-DC:

$$
1,N
$$

the boundary states necessary for operations, duality and recovery remain.

---

# Short summary of §5–§7

In §5 a staircase is built square-free numbers:

$$
D(p_1\cdots p_n)\cong Q_n.
$$

Primorial representatives:

$$
P_n^#=p_1\cdots p_n.
$$

$$
D(P_n^#)\cong Q_n.
$$

Own ladder:

$$
D^\circ(P_n^#)\cong U_n=Q_n\setminus\{0^n,1^n\}.
$$

Ladder of the outer layer:

$$
V_n=S_1^{(n)}\sqcup S_{n-1}^{(n)}.
$$

Form through divisors:

$$
V(P_n^#)=
{p_i}\cup{P_n^#/p_i}.
$$

Counts:

$$
|U_n|=2^n-2,
\qquad
|V_n|=2n
\quad(n\ge3).
$$

Special coincidence of rank 3:

$$
U_3=V_3.
$$

In §6 a chain extension is constructed:

$$
D(p_1^{a_1}\cdots p_r^{a_r})
\cong
\prod_i{0,\ldots,a_i}.
$$

Two types are separated growth:

```text
rank increase = adding new prime coordinate;
depth increase = increasing exponent of an existing prime.
```

Cover graph:

$$
(D(N),C_N)
\cong
P_{a_1+1}\square\cdots\square P_{a_r+1}.
$$

Duality of divisors:

$$
\delta_N(d)=N/d.
$$

Fixed point:

$$
\delta_N(d)=d
\Longleftrightarrow
d^2=N.
$$

In §7 a multiplicative layer is introduced:

$$
d\odot_N e=de
\quad
\text{if}
\quad
de\mid N.
$$

Coordinate condition:

$$
\eta_N(d)+\eta_N(e)\le(a_1,\ldots,a_r).
$$

On full (D(N)):

$$
(D(N),\odot_N,1)
$$

—partial commutative monoid.

Addition-pairs:

$$
d\odot_N\frac Nd=N.
$$

On your proper carrier, access to the border is possible:

$$
2\odot_{30}15=30.
$$

Final formula of the block:

$$
\boxed{
\text{AMR-DC has two matched layers: a lattice of divisors and a partial assembly of the product.}
}
$$

---


I continue with §8–§10.

---

# §8. The Discipline of Reading and Restoration

This chapter is the methodological heart of AMR-DC.

Up to this point we have built the carriers:

$$
D(N),
\qquad
D^\circ(N),
\qquad
R_N=\mathbb Z/N\mathbb Z \ \text{will be introduced in §9}.
$$

But the carrier itself does not yet define the theory. It is necessary to indicate:

```text
what is read;
what relation is held;
which is restored after reading;
which is folded without recovery.
```

In the DOT language this is written as a representation:

$$
\Pi=(X,R,q,rec),
$$

where (X) is the carrier, (R) is the relation, (q) is reading, (rec) is recovery data. A term is considered introduced only when the representation in which it occurs is indicated.

The methodological protocol of DOT requires for a new term to indicate the carrier, relationship, role, load, recoverability, status and rank; if the bearer is not specified, the term cannot be internal.

In AMR-DC this is especially important: the same divisor can be read as an exponent vector, a support, a layer, a complement pair, or a gcd-residue state. These readings are not equal to each other.

---

## §8.1. Why recovery is needed

### 8.1.1. Basic rule

Arithmetic readings cannot be mixed.

Each reading preserves some data and collapses others.

For example, for a

$$
N=72=2^3\cdot3^2
$$

divisor

$$
12=2^2\cdot3
$$

has a vector of exponents

$$
(2,1).
$$

But different readings give different images:

$$
\Omega_{72}(12)=3,
$$

$$
\omega_{72}(12)=2,
$$

$$
\mathrm{supp}_{72}(12)={2,3}.
$$

If you leave only

$$
\Omega=3,
$$

then you cannot restore whether there was a divisor (8), (12), (18) or another divisor of the same total multiplicity layer.

If you leave only

$$
\mathrm{supp}={2,3},
$$

then you cannot distinguish

$$
6=2\cdot3,
\qquad
12=2^2\cdot3,
\qquad
18=2\cdot3^2,
\qquad
36=2^2\cdot3^2.
$$

Consequently, reading without recovery status turns the structure into an ambiguous mark.

### 8.1.2. Accurate, fiber, lossy

In AMR-DC we will distinguish three types of recoverability.

#### Exact recovery

Read

$$
q:X\to Y
$$

has exact recovery if there exists

$$
rec_q:Y\to X
$$

such that

$$
rec_q(q(x))=x
$$

for all (x\in X).

Example:

$$
\eta_N:D(N)\to E(N)
$$

exact, because the vector of exponents completely restores the divisor:

$$
(b_1,\ldots,b_r)
\mapsto
p_1^{b_1}\cdots p_r^{b_r}.
$$

#### Fiber recovery

A reading has fiber recovery if, over the image $y=q(x)$, it is not $x$ itself that is recovered, but the entire fiber:

$$
rec_q(y)=q^{-1}(y).
$$

Example:

$$
\omega_N(d)=k.
$$

Here recovery gives:

$$
rec_\omega(k)={d\in D(N):\omega_N(d)=k}.
$$

This is not a single divisor, but a layer.

#### Lossy / bridge recovery

A reading has lossy or bridge status if it saves only part of the structure, and recovery requires additional data.

Example:

$$
q_{\pm}(d)={d,N/d}.
$$

It preserves the complement pair, but loses the side of the pair.

To restore (d), you must additionally specify the orientation / selection sides.

### 8.1.3. Recovery as a reading load

In terms of the methodological coordinate (D) from the DOT protocol, recovery is not a technical detail, but an inscription-load: data that is retained after the transition to reading.

Therefore, in AMR-DC, each reading must be accompanied by the question:

```text
which load is retained?
which load disappears?
what additional label is needed for recovery?
```

---

## §8.2. Reading table

### 8.2.1. Basic readings of AMR-DC

Let

$$
N=p_1^{a_1}\cdots p_r^{a_r}.
$$

And let

$$
d=p_1^{b_1}\cdots p_r^{b_r}.
$$

Then the basic readings are as follows.

| reading | carrier | image | saves | loses / requires choice | recovery status |
| ---------------------------- | ---------------------- | ------------------------------- | -------------------------- | ------------------------------------ | ------------------------------------ |
| (\eta_N(d)) | (D(N)) | (\prod_i{0,\ldots,a_i}) ​​| full exponent profile | requires a fixed prime basis | exact |
| (d\mapsto\omega_N(d)) | (D(N)) | ({0,\ldots,r}) | number of active primes | support, multiples | fiber |
| (d\mapsto\Omega_N(d)) | (D(N)) | ({0,\ldots,\sum_i a_i}) ​​| sum of multiples | distribution by coordinates | fiber |
| (d\mapsto\mathrm{supp}_N(d)) | (D(N)) | subsets of prime factors | active coordinates | multiplicity | exact only square-free |
| $q_{\pm}(d)=\{d,N/d\}$ | (D(N)) | dual-pairs | couple additions | side of the couple | orbit/fiber |
| ([a]\mapsto\gcd(a,N)) | (\mathbb Z/N\mathbb Z) | (D(N)) | divisor state | reversible multiplier data | fiber |

These readings have different levels of recoverability and should not be mixed: $\omega_N$, $\Omega_N$, $\mathrm{supp}_N$, $q_{\pm}$ and $q_{\gcd}$ preserve different parts of the original carrier.

### 8.2.2. Exact coordinate reading

Main Precise Reading on (D(N)):

$$
\eta_N:D(N)\to E(N),
$$

$$
\eta_N(d)=(b_1,\ldots,b_r).
$$

Recovery:

$$
rec_\eta(b_1,\ldots,b_r)
=
p_1^{b_1}\cdots p_r^{b_r}.
$$

Representation:

$$
\Pi_{\eta}(N)
=
(D(N),C_N,\eta_N,rec_\eta).
$$

Here (C_N) can be replaced by (\mid) if order representation is needed:

$$
\Pi_{\eta,\mid}(N)
=
(D(N),\mid,\eta_N,rec_\eta).
$$

### 8.2.3. Layer readings

Total multiplicity reading:

$$
\Omega_N:D(N)\to{0,\ldots,\sum_i a_i}.
$$

Recovery:

$$
rec_{\Omega}(k)=\Omega_N^{-1}(k).
$$

Active coordinates reading reading:

$$
\omega_N:D(N)\to{0,\ldots,r}.
$$

Recovery:

$$
rec_{\omega}(k)=\omega_N^{-1}(k).
$$

Neither $\Omega$ nor $\omega$ are accurate in the general case.

These are layer readings, not state readings.

### 8.2.4. Carrier coordinate reading

Coordinate carrier reading:

$$
\mathrm{supp}_N:D(N)\to \mathcal P({p_1,\ldots,p_r}),
$$

$$
\mathrm{supp}_N(d)={p_i:b_i>0}.
$$

It forgets multiplicities.

It is exact in the case of square-free numbers.

This is proven in §8.3.

### 8.2.5. Reading a complement pair

Reading a complement pair:

$$
q_{\pm}:D(N)\to D(N)/\delta_N,
$$

$$
q_{\pm}(d)={d,N/d}.
$$

It preserves the complement orbit.

It loses a side:

$$
d
\quad
\text{versus}
\quad
N/d.
$$

This is proven in §8.4.

### 8.2.6. Reading residues through gcd

The residue reading is introduced in §9:

$$
q_{\gcd}:\mathbb Z/N\mathbb Z\to D(N),
$$

$$
q_{\gcd}([a])=\gcd(a,N).
$$

It preserves the divisor state of the residue class.

It loses the invertible multiplier data inside the fiber.

---

## §8.3. Reading accuracy support

### Theorem 8.1 [D]. Support reading is exact if and only if N is square-free

Let

$$
N=p_1^{a_1}\cdots p_r^{a_r}.
$$

Support reading

$$
\mathrm{supp}_N:D(N)\to\mathcal P({p_1,\ldots,p_r})
$$

exactly on $D(N)$ if and only if $N$ is square-free, that is,

$$
a_i=1
\quad
\text{for all}i.
$$

### Proof

#### 1. Square-free case

Let

$$
N=p_1\cdots p_r
$$

square-free.

Then any divisor (d\mid N) has the form

$$
d=\prod_{p_i\in S}p_i
$$

for a single subset

$$
S\subseteq{p_1,\ldots,p_r}.
$$

But this subset is exactly:

$$
S=\mathrm{supp}_N(d).
$$

Consequently,

$$
d=
\prod_{p_i\in\mathrm{supp}_N(d)}p_i.
$$

That is, support completely recovers (d).

#### 2. The case with square divisors

Let (N) not be square-free.

Then there is an index (i), such that

$$
a_i\ge2.
$$

Consider two divisors:

$$
p_i
\quad
\text{and}
\quad
p_i^2.
$$

They are different:

$$
p_i\ne p_i^2,
$$

but have the same support:

$$
\mathrm{supp}_N(p_i)={p_i},
$$

$$
\mathrm{supp}_N(p_i^2)={p_i}.
$$

This means that the reading of the support is not injective and not exact.

Consequently, the reading of the support is exactly exactly in the case of square-free numbers.

$$
\blacksquare
$$

### 8.3.1. AMR reading

In AMR for square-free numbers:

```text
support = state.
```

In chain extension:

```text
support = set of active coordinates,
but not complete state.
```

That is, support ceases to be a carrier point and becomes a rough reading.

---

## §8.4. Accuracy of reading complement pair

### 8.4.1. Reading the complement orbit

Recall:

$$
\delta_N(d)=\frac Nd.
$$

Reading the complement pair:

$$
q_{\pm}(d)={d,N/d}.
$$

This is a factor reading by the action of involution (\delta_N).

### 8.4.2. Fiber structure

A fiber $q_{\pm}$ above the orbit of a pair:

$$
{d,N/d}
$$

usually has two points:

$$
d
\quad
\text{and}
\quad
N/d.
$$

It has one point only when

$$
d=N/d.
$$

That is:

$$
d^2=N.
$$

### Theorem 8.2 [D]. Reading a complement pair pointwise is exact only at fixed points

For

$$
q_{\pm}(d)={d,N/d}
$$

is correct:

$$
q_{\pm}^{-1}(q_{\pm}(d))={d}
$$

if and only if

$$
d^2=N.
$$

Otherwise the fiber has two points:

$$
q_{\pm}^{-1}(q_{\pm}(d))={d,N/d}.
$$

### Proof

By definition:

$$
q_{\pm}(d)={d,N/d}.
$$

If

$$
d=N/d,
$$

then the orbit contains one point:

$$
{d}.
$$

This is equivalent to:

$$
d^2=N.
$$

If

$$
d\ne N/d,
$$

then the orbit contains two different points:

$$
d,
\qquad
N/d.
$$

This means that reading loses the complement-pair side.

$$
\blacksquare
$$

### 8.4.3. Fixed point criterion

From §6.4:

$$
d^2=N
$$

is possible if and only if (N) is a square.

If

$$
N=p_1^{a_1}\cdots p_r^{a_r},
$$

then a fixed point exists if and only if all $a_i$ are even.

Then the only fixed point is:

$$
d=\sqrt N.
$$

### 8.4.4. Square-free case

If $N$ is square-free and $N>1$, then everything is $a_i=1$, so there are no fixed points.

Hence:

$$
q_{\pm}:D(N)\to D(N)/\delta_N
$$

is two-sheeted throughout.

For

$$
N=30
$$

three proper complement pairs:

$$
{2,15},
\qquad
{3,10},
\qquad
{5,6}.
$$

Reading a complement pair preserves the pair, but not side.

### 8.4.5. AMR reading

```text
Read complement pair exactly like an orbit,
but not exactly like a side-selected state.
```

To recover the original divisor from a pair, the side data is needed:

$$
{d,N/d}
+
\text{side}
\longrightarrow
d.
$$

This data is a bridge mark and is not contained in the $q_{\pm}$ itself.

---

## §8.5. Recovery data as part of the presentation

### 8.5.1. General Form

For each AMR $q$ reading, the following is written:

$$
\Pi_q=(X,R,q,rec_q).
$$

The same $X$ carrier can support different readings.

The same $q$ reading can be used with different $R$ relationships.

Hence, the representation must specify both components.

### 8.5.2. Layer Representation

For the active coordinates layer:

$$
\Pi_{\omega}(N)
=
(D(N),C_N,\omega_N,rec_\omega).
$$

Here:

$$
rec_\omega(k)=\omega_N^{-1}(k).
$$

This recovery returns the layer, not the divisor.

For the full multiplicity layer:

$$
\Pi_{\Omega}(N)
=
(D(N),C_N,\Omega_N,rec_\Omega),
$$

$$
rec_\Omega(k)=\Omega_N^{-1}(k).
$$

### 8.5.3. Support Reading

For support:

$$
\Pi_{\mathrm{supp}}(N)
=
(D(N),C_N,\mathrm{supp}_N,rec_{\mathrm{supp}}).
$$

If $N$ is free of squares:

$$
rec_{\mathrm{supp}}(S)=\prod_{p_i\in S}p_i.
$$

If $N$ is not free of squares:

$$
rec_{\mathrm{supp}}(S)
=
{d\in D(N):\mathrm{supp}_N(d)=S}.
$$

This is fiber recovery, not exact recovery.

### 8.5.4. Complement Pair Representation

To reading a complement pair:

$$
\Pi_{\pm}(N)
=
(D(N),R_{\pm},q_{\pm},rec_{\pm}).
$$

Where:

$$
R_{\pm}
=
{{d,N/d}:d\in D(N),d\ne N/d}.
$$

And:

$$
q_{\pm}(d)={d,N/d}.
$$

Reconstruction:

$$
rec_{\pm}({d,N/d})={d,N/d}.
$$

Exact side reconstruction requires an additional side label.

### 8.5.5. Representation of gcd-residue

After §9:

$$
\Pi_{\gcd}(N)
=
(\mathbb Z/N\mathbb Z,R_N^{\mathrm{res}},q_{\gcd},rec_{\gcd}).
$$

The $R_N^{\mathrm{res}}$ relation must be specified depending on the selected residue graph:

```text
zero-product relation;
difference-gcd relation;
unit-action relation;
CRT-coordinate relation.
```

Without this relation, (q_{\gcd}) is only a reading, not a full representation.

### 8.5.6. Recovery principle

$$
\boxed{
\text{AMR reading is correct only together with the recovery status.}
}
$$

Otherwise you can accidentally identify:

$$
\omega,
\qquad
\Omega,
\qquad
\mathrm{supp},
\qquad
q_{\pm},
\qquad
q_{\gcd},
$$

although they save different data.

---

# §9. Residue bridge

In §1–§8 the main carrier was the carrier of the divisors:

$$
D(N)=\{d:d\mid N\}.
$$

Now a second arithmetic carrier is introduced:

$$
\mathbb Z/N\mathbb Z.
$$

It does not replace (D(N)). It gives an outer residue space from which the divisor states are retrieved via gcd reading.

---

## §9.1. Second carrier: carrier of residues

### 9.1.1. Definition

**Definition 9.1 [D].**
The carrier of residues of a number (N) is a ring of residue classes:

$$
R_N=\mathbb Z/N\mathbb Z.
$$

Its elements are designated:

$$
[a].
$$

Here

$$
[a]=[b]
$$

if

$$
a\equiv b\pmod N.
$$

### 9.1.2. Two carriers

AMR-DC now has two associated carriers:

```text
D(N) = divisor carrier;
Z/NZ = carrier of residues.
```

Divisor carrier:

$$
D(N)
$$

contains the divisor states of the number (N).

Residue carrier:

$$
R_N=\mathbb Z/N\mathbb Z
$$

contains residue states modulo (N).

### 9.1.3. The relationship between them

The relationship between them is given not by the equality of the carriers, but by the reading:

$$
q_{\gcd}:R_N\to D(N).
$$

A residue state is read through its common divisor with $N$.

---

## §9.2. gcd-reading

### 9.2.1. Definition

**Definition 9.2 [D].**
gcd-reading of the residue carrier:

$$
q_{\gcd}:R_N\to D(N)
$$

is given by the formula

$$
q_{\gcd}([a])=\gcd(a,N).
$$

### 9.2.2. Correctness of definition

We need to check that this is correct for the residue class.

If

$$
[a]=[b]\in\mathbb Z/N\mathbb Z,
$$

then

$$
a\equiv b\pmod N.
$$

So,

$$
b=a+Nm
$$

for some (m\in\mathbb Z).

Any divisor (t\mid N) divides (a) if and only if it divides (b), because that

$$
b-a=Nm
$$

and

$$
t\mid N.
$$

Consequently, the sets of common divisors (a) and (N), (b) and (N) coincide.

So,

$$
\gcd(a,N)=\gcd(b,N).
$$

Therefore,

$$
q_{\gcd}
$$

is correctly defined.

### 9.2.3. The meaning

$$
q_{\gcd}([a])=d
$$

means:

```text
residue $[a]$ has the divisor state $d$ relative to $N$.
```

That is, (d) records which prime-capacities (N) are already present in the residue (a).

### 9.2.4. Data units

If

$$
q_{\gcd}([a])=d,
$$

then

$$
a=d u
$$

with the condition

$$
\gcd(u,N/d)=1.
$$

This means that the residue state consists of two parts:

```text
divisor state d;
data of the invertible factor u modulo N/d.
```

gcd reading retains (d) but loses (u).

---

## §9.3. Fiber theorem

### Theorem 9.3 [D]. Fiber theorem for $q_{\gcd}$

Let

$$
d\in D(N).
$$

Then

$$
\boxed{
|q_{\gcd}^{-1}(d)|=\varphi(N/d).
}
$$

Here (\varphi) is the Euler function.

### Proof

We need to calculate the residue classes ([a]\in\mathbb Z/N\mathbb Z), such that

$$
\gcd(a,N)=d.
$$

The condition

$$
\gcd(a,N)=d
$$

is equivalent to the fact that

$$
a=d u
$$

and

$$
\gcd(u,N/d)=1.
$$

Suppose

$$
M=N/d.
$$

Then the condition becomes:

$$
a=d u,
\qquad
\gcd(u,M)=1.
$$

The classes of residues (a\pmod N) of the form (du) are different if and only if (u) are different in modulus (M).

Valid:

$$
du_1\equiv du_2\pmod N
$$

equivalent to:

$$
N\mid d(u_1-u_2).
$$

Since (N=dM), this is equivalent to:

$$
M\mid u_1-u_2.
$$

This means that the fiber over (d) is in bijection with the unit group:

$$
(\mathbb Z/M\mathbb Z)^\times.
$$

The number of such unit-classes:

$$
\varphi(M)=\varphi(N/d).
$$

Hence:

$$
|q_{\gcd}^{-1}(d)|=\varphi(N/d).
$$

$$
\blacksquare
$$

### Corollary 9.3.1 [D]. Sum of fiber sizes

Fibers $q_{\gcd}$ break up the entire carrier of residues $R_N=\mathbb Z/N\mathbb Z$. Therefore

$$
\sum_{d\in D(N)} |q_{\gcd}^{-1}(d)|
=
|\mathbb Z/N\mathbb Z|
=
N.
$$

By Theorem 9.3 this gives the classical identity

$$
\sum_{d\mid N}\varphi(N/d)=N.
$$

In AMR-DC the residue bridge is formulated exactly like this: $q_{\gcd}([a])=\gcd(a,N)$, and the fiber above $d\in D(N)$ has the size $\varphi(N/d)$.

### 9.3.1. Description of the fiber

More precisely:

$$
q_{\gcd}^{-1}(d)
=
{[du]\in\mathbb Z/N\mathbb Z:\gcd(u,N/d)=1}.
$$

That is:

$$
q_{\gcd}^{-1}(d)
\cong
(\mathbb Z/(N/d)\mathbb Z)^\times.
$$

This is not a canonical equality of sets, but a canonical parameterization of the fiber after choosing $d$.

### 9.3.2. Example: $N=30$

$$
D(30)=\{1,2,3,5,6,10,15,30\}.
$$

Fiber sizes:

|  (d) | (N/d) | (\varphi(N/d)) | meaning |
| ---: | ----: | -------------: | ------------------------------- |
|  (1) |  (30) |            (8) | invertible classes modulo (30) |
|  (2) |  (15) |            (8) | residue classes with gcd (2) |
|  (3) |  (10) |            (4) | residue classes with gcd (3) |
|  (5) |   (6) |            (2) | residue classes with gcd (5) |
|  (6) |   (5) |            (4) | residue classes with gcd (6) |
| (10) |   (3) |            (2) | residue classes with gcd (10) |
| (15) |   (2) |            (1) | residue class (15) |
| (30) |   (1) |            (1) | zero residue |

Check:

$$
8+8+4+2+4+2+1+1=30.
$$

This gives:

$$
|\mathbb Z/30\mathbb Z|=30.
$$

### 9.3.3. The recovery status

$$
q_{\gcd}
$$

is not exact.

It has fiber recovery:

$$
rec_{\gcd}(d)=q_{\gcd}^{-1}(d).
$$

To restore the residue class $[a]$, you need to add the reversible multiplier data:

$$
u\in(\mathbb Z/(N/d)\mathbb Z)^\times.
$$

Total:

```text
q_gcd retains the divisor state;
q_gcd loses the position of the invertible multiplier within the fiber of the divisor state.
```

---

## §9.4. CRT reading in the case of square-free numbers

### 9.4.1. CRT expansion

Let

$$
N=p_1p_2\cdots p_n
$$

square-free.

By the Chinese residue theorem:

$$
\mathbb Z/N\mathbb Z
\cong
\prod_{i=1}^{n}\mathbb Z/p_i\mathbb Z.
$$

The residue class $[a]$ corresponds to the tuple:

$$
([a]_{p_1},\ldots,[a]_{p_n}).
$$

### 9.4.2. Null pattern

For every prime $p_i$:

$$
p_i\mid \gcd(a,N)
$$

if and only if

$$
p_i\mid a.
$$

Equivalent to:

$$
p_i\mid \gcd(a,N)
\quad\Longleftrightarrow\quad
a\equiv0\pmod{p_i}.
$$

Therefore, $q_{\gcd}$ captures the zero pattern of a CRT tuple.

### Theorem 9.4 [D]. $q_{\gcd}$ fixes the null pattern of CRT

Let

$$
N=p_1\cdots p_n
$$

square-free.

In the CRT expansion,

$$
\mathbb Z/N\mathbb Z
\cong
\prod_i\mathbb Z/p_i\mathbb Z,
$$

The divisor

$$
q_{\gcd}([a])=\gcd(a,N)
$$

corresponds to the set of coordinates where the CRT component is zero:

$$
\mathrm{supp}(q_{\gcd}([a]))
=
{p_i:[a]_{p_i}=0}.
$$

### Proof

Since $N$ is free of squares,

$$
\gcd(a,N)
$$

is the product of exactly those $p_i$ that divide $a$.

But

$$
p_i\mid a
$$

if and only if

$$
a\equiv0\pmod{p_i}.
$$

Consequently, the support of the gcd divisor is exactly equal to the set of zero coordinates of the CRT tuple.

$$
\blacksquare
$$

### 9.4.3. Fiber size in CRT form

If

$$
d=\prod_{i\in S}p_i,
$$

then $q_{\gcd}([a])=d$ means:

$$
[a]_{p_i}=0
\quad
\text{for}i\in S,
$$

and

$$
[a]_{p_i}\ne0
\quad
\text{for}i\notin S.
$$

Hence:

$$
|q_{\gcd}^{-1}(d)|
=
\prod_{i\notin S}(p_i-1).
$$

But:

$$
N/d=\prod_{i\notin S}p_i,
$$

therefore

$$
\varphi(N/d)=\prod_{i\notin S}(p_i-1).
$$

This is consistent with Theorem 9.3.

### 9.4.4. Reading AMR

```text
In the residue carrier for a square-free number
gcd read takes the zero CRT pattern into the divisor state.
```

This is different from support reading on the divisor carrier.

Support reading on $D(N)$:

$$
d\mapsto{p_i:p_i\mid d}.
$$

gcd reading on $\mathbb Z/N\mathbb Z$:

$$
[a]\mapsto\gcd(a,N).
$$

In composition:

$$
[a]
\mapsto
\gcd(a,N)
\mapsto
\mathrm{supp}(\gcd(a,N))
=
\text{null CRT pattern}[a].
$$

---

## §9.5. Projection of zero divisors

### 9.5.1. Zero product relation

On the residue carrier (R_N=\mathbb Z/N\mathbb Z), you can define a zero product relation:

$$
[a]\sim_0[b]
$$

if

$$
[a]\cdot[b]\equiv0\pmod N.
$$

Equivalent to:

$$
N\mid ab.
$$

Depending on convention, the graph of zero divisors can exclude:

```text
zero residue;
invertible residues;
loops.
```

Hence, a complete definition of the graph requires an explicit convention.

### 9.5.2. Criterion for gcd classes

Let

$$
d=q_{\gcd}([a])=\gcd(a,N),
$$

$$
e=q_{\gcd}([b])=\gcd(b,N).
$$

Write

$$
N=p_1^{a_1}\cdots p_r^{a_r},
$$

$$
d=p_1^{\alpha_1}\cdots p_r^{\alpha_r},
$$

$$
e=p_1^{\beta_1}\cdots p_r^{\beta_r}.
$$

Then

$$
[a][b]\equiv0\pmod N
$$

if and only if

$$
\alpha_i+\beta_i\ge a_i
\quad
\text{for all}i.
$$

Equivalent to:

$$
N\mid de.
$$

### Statement 9.5 [D]. The zero product is determined by the gcd states

For any $[a],[b]\in\mathbb Z/N\mathbb Z$:

$$
[a][b]\equiv0\pmod N
$$

if and only if

$$
N\mid q_{\gcd}([a])\cdot q_{\gcd}([b]).
$$

### Proof

Let

$$
v_i(x)=v_{p_i}(x)
$$

is the $p_i$-adic estimate cut off at the level of $a_i$ when taking gcd with $N$.

If

$$
q_{\gcd}([a])=d,
$$

then the indicator $\alpha_i$ at $p_i$ in $d$ is equal to

$$
\alpha_i=\min(v_i(a),a_i).
$$

Similarly:

$$
\beta_i=\min(v_i(b),a_i).
$$

Condition

$$
[a][b]\equiv0\pmod N
$$

means:

$$
N\mid ab.
$$

This is equivalent to:

$$
v_i(a)+v_i(b)\ge a_i
\quad
\text{for all}i.
$$

Let's check the transition to gcd states coordinate-wise. If $v_i(a)\ge a_i$, then $\alpha_i=a_i$, and the inequality $\alpha_i+\beta_i\ge a_i$ holds regardless of $\beta_i$. The same is true if $v_i(b)\ge a_i$. If both values ​​are less than $a_i$, then $\alpha_i=v_i(a)$, $\beta_i=v_i(b)$, and the inequality continues unchanged.

The reverse implication is also direct: $\alpha_i\le v_i(a)$ and $\beta_i\le v_i(b)$, therefore from $\alpha_i+\beta_i\ge a_i$ follows $v_i(a)+v_i(b)\ge a_i$. This means that the condition above is equivalent to:

$$
\alpha_i+\beta_i\ge a_i
\quad
\text{for all}i.
$$

But this is exactly the condition:

$$
N\mid de.
$$

Consequently, the zero product depends only on the gcd states.

$$
\blacksquare
$$

### 9.5.3. What is lost

Although the adjacency of the zero product is determined by the gcd states, the complete residue graph is not reconstructed from a single $D(N)$.

Reason:

$$
q_{\gcd}^{-1}(d)
$$

may contain many residues.

The gcd class graph glues all residues to the same divisor state.

Consequently:

```text
zero product relation descends to classes divisors;
a complete residue graph requires invertible multiplier data within each class.
```

### 9.5.4. Form without square factors

If $N$ is free of squares, then

$$
[a][b]\equiv0\pmod N
$$

if and only if the zero patterns $[a]$ and $[b]$ cover all prime factors.

In divisor form:

$$
N\mid q_{\gcd}([a])q_{\gcd}([b]).
$$

For a number without square factors $N$ this means:

$$
\mathrm{supp}(q_{\gcd}([a]))
\cup
\mathrm{supp}(q_{\gcd}([b]))
=
{p_1,\ldots,p_n}.
$$

### 9.5.5. Status

Strict:

$$
[a][b]\equiv0\pmod N
\Longleftrightarrow
N\mid q_{\gcd}([a])q_{\gcd}([b]).
$$

Bridge / open:

```text
what convention of a zero divisor graph should be internal to AMR-DC?
```

Possible conventions:

```text
all non-zero zero divisors;
proper gcd classes;
no class [0];
including weighted classes;
factor graph on $D(N)$;
weighted factor graph on $\varphi(N/d)$.
```

This is a future choice of graph construction, not part of the strict core of AMR-DC.

---

## §9.6. gcd graphs

### 9.6.1. Reading the difference through gcd

On the residue carrier $R_N$ we set

$$
q_{\Delta}([a],[b])=\gcd(a-b,N).
$$

This is correctly defined: if

$$
a\equiv a'\pmod N,
\qquad
b\equiv b'\pmod N,
$$

then

$$
a-b\equiv a'-b'\pmod N,
$$

and therefore

$$
\gcd(a-b,N)=\gcd(a'-b',N).
$$

### 9.6.2. Layers of relations

For each divisor $d\mid N$ you can specify a relation

$$
R_{\Delta,d}
=
\{([a],[b]):\gcd(a-b,N)=d\}.
$$

You can also specify a threshold relation

$$
R_{\Delta,\succeq d}
=
\{([a],[b]):d\mid \gcd(a-b,N)\}.
$$

Both options are arithmetic layers of relations on the residue carrier.

### 9.6.3. The square-free case

If

$$
N=p_1\cdots p_n
$$

is free from square divisors, then

$$
p_i\mid\gcd(a-b,N)
$$

if and only if

$$
a\equiv b\pmod{p_i}.
$$

So, $q_{\Delta}$ captures the pattern of CRT coordinate matches. This is different from reading

$$
q_{\gcd}([a])=\gcd(a,N),
$$

which captures the zero pattern of a single residue class.

### 9.6.4. Status

Strict status has only an explicitly defined relationship:

$$
R_{\Delta,d}
\quad
\text{or}
\quad
R_{\Delta,\succeq d}.
$$

Open bridge problem: determine which gcd graph layers are internal to AMR-DC, which correspond to DOT relation readings, and how they interact with $D(N)$, $U_n$, $V_n$.

---


# Short summary §8–§9

Restoring discipline:

$$
\Pi=(X,R,q,rec).
$$

Main reading:

$$
\eta_N(d),
\qquad
\omega_N(d),
\qquad
\Omega_N(d),
\qquad
\mathrm{supp}_N(d),
\qquad
q_{\pm}(d)=\{d,N/d\},
\qquad
q_{\gcd}([a])=\gcd(a,N).
$$

Coordinate carrier accuracy:

$$
\mathrm{supp}_N
\text{exact}
\Longleftrightarrow
N \text{free of squares}.
$$

Dual-pair reading:

$$
q_{\pm}(d)={d,N/d}
$$

recovering side only at a fixed point:

$$
d=N/d
\Longleftrightarrow
d^2=N.
$$

Residue bridge:

$$
q_{\gcd}:\mathbb Z/N\mathbb Z\to D(N),
\qquad
q_{\gcd}([a])=\gcd(a,N).
$$

Fiber theorem:

$$
|q_{\gcd}^{-1}(d)|=\varphi(N/d).
$$

Free from squares zero CRT pattern:

$$
p_i\mid\gcd(a,N)
\Longleftrightarrow
a\equiv0\pmod{p_i}.
$$

Criterion for the zero product class:

$$
[a][b]\equiv0\pmod N
\Longleftrightarrow
N\mid q_{\gcd}([a])q_{\gcd}([b]).
$$

Main principle:

$$
\boxed{
\text{Each AMR reading must carry its own recovery status.}
}
$$

---

# §10. Integration with AMR-SR

This chapter fixes the boundary between two arithmetic branches. AMR-SR works with pairs of natural numbers, scale and residue. AMR-DC works with a finite divisor carrier. They have a common motive: both branches use gcd extraction. But the carrier, relationships and recovery data are different.

## §10.1. Two AMR branches

The AMR-SR branch has a carrier

$$
\mathcal R=\mathbb N_{>0}^{2}.
$$

Each pair is decomposed as

$$
(a,b)=g(p,q),
\qquad
g=\gcd(a,b),
\qquad
\gcd(p,q)=1.
$$

Here $g$ is the scale of the pair, and $(p,q)$ is the primitive direction. The difference has the form

$$
|a-b|=g|p-q|,
$$

therefore, the residue of AMR-SR is equal to

$$
\mathrm{Res}_{\mathrm{sr}}(a,b)=|a-b|-|p-q|=(g-1)|p-q|.
$$

The AMR-DC branch has a different carrier:

$$
D(N)=\{d:d\mid N\}.
$$

If

$$
N=p_1^{a_1}\cdots p_r^{a_r},
$$

then

$$
D(N)\cong\prod_i\{0,\ldots,a_i\}.
$$

For a square-free number

$$
N=p_1\cdots p_n
$$

the Boolean carrier is obtained

$$
D(N)\cong Q_n.
$$

The proper divisor carrier in this case is equal to

$$
D^\circ(N)\cong Q_n\setminus\{0^n,1^n\}.
$$

For $30=2\cdot3\cdot5$:

$$
D^\circ(30)\cong Q_3\setminus\{000,111\}=X_{\mathrm{adm}}.
$$

## §10.2. General gcd extraction

In AMR-SR, the gcd extracts the scale of the pair:

$$
(a,b)\mapsto \gcd(a,b)=g.
$$

This leaves the primitive direction $(p,q)$.

In AMR-DC, the gcd can reading the residue state relative to a fixed number $N$:

$$
q_{\gcd}:\mathbb Z/N\mathbb Z\to D(N),
\qquad
q_{\gcd}([a])=\gcd(a,N).
$$

The fiber above $d\in D(N)$ has the form

$$
q_{\gcd}^{-1}(d)\cong(\mathbb Z/(N/d)\mathbb Z)^\times,
$$

and size

$$
|q_{\gcd}^{-1}(d)|=\varphi(N/d).
$$

Comparison types:

| branch | source carrier | extraction | what remains |
| ---------------- | ---------------------- | ------------------------------ | ------------------------------- |
| AMR-SR | $\mathbb N_{>0}^2$ | $\gcd(a,b)=g$ | primitive direction $(p,q)$ |
| AMR-DC, residues | $\mathbb Z/N\mathbb Z$ | $\gcd(a,N)=d$ | reversible multiplier in fiber |
| AMR-DC, divisors | $D(N)$ | the state is already specified by the divisor | exponent profile |

Main limit:

$$
\boxed{\text{AMR-SR and AMR-DC use gcd but do not have the same carrier.}}
$$

## §10.3. What is not stated

From the strict design of the AMR-DC it does not follow that the AMR-SR $\beta_3,\beta_4$ bridge switches are derived from the $D^\circ(30)$ carrier. In AMR-DC, only

$$
D^\circ(30)\cong X_{\mathrm{adm}}.
$$

The residue of AMR-SR is not the octahedral relation of AMR-DC:

$$
\mathrm{Res}_{\mathrm{sr}}\ne R_{\mathrm{oct}}.
$$

The first object is a scalar function on $\mathbb N_{>0}^2$, the second is a graph relation on $D^\circ(30)$.

The functor is also not proven

$$
\mathrm{AMR\text{-}SR}\to\mathrm{AMR\text{-}DC}.
$$

In particular, it is not proven that primitive rays, difference layers or the residue $\mathrm{Res}_{\mathrm{sr}}$ naturally passes to divisor carriers and their relations. Numerical parallel

$$
30=P_3^#,
\qquad
210=P_4^#
$$

is important as a candidate connection, but it does not automatically produce statements of the form $k=3\Longleftrightarrow N=30$ or $k=4\Longleftrightarrow N=210$.

## §10.4. Candidate bridges

For a fixed $N$, multiple mappings from AMR-SR to the final divisor carrier can be considered.

Projection of a common divisor:

$$
\pi_N:\mathbb N_{>0}^2\to D(N),
\qquad
\pi_N(a,b)=\gcd(a,b,N).
$$

If $(a,b)=g(p,q)$ and $\gcd(p,q)=1$, then

$$
\pi_N(a,b)=\gcd(g,N).
$$

Two-way reading of residues:

$$
\kappa_N:\mathbb N_{>0}^2\to D(N)\times D(N),
\qquad
\kappa_N(a,b)=(\gcd(a,N),\gcd(b,N)).
$$

Difference reading:

$$
\lambda_N:\mathbb N_{>0}^2\to D(N),
\qquad
\lambda_N(a,b)=\gcd(a-b,N).
$$

Read primitive defect:

$$
\mu_N(a,b)=\gcd(|p-q|,N),
\qquad
(a,b)=g(p,q),
\quad
\gcd(p,q)=1.
$$

Each such mapping remains a bridge candidate until the source, image, transportable relation and recovery data are specified.

Check for any candidate:

1. What is the source: $\mathbb N_{>0}^2$, difference layer, primitive ray, or other carrier?
2. What is the image: $D(N)$, $D^\circ(N)$, $U_n$, $V_n$ or other carrier?
3. What relation is transferred: difference layer, ray, covering, complement, gcd-state?
4. What is restored and what is lost: scale, direction, reversible factor, side of the pair, position in the layer?
5. For $N=30$, does one of the relations $C_6$, $K_3\sqcup K_3$, $3K_2$, $K_{2,2,2}$ arise on $D^\circ(30)$?

A candidate is rejected if it identifies $\mathrm{Res}_{\mathrm{sr}}$ with $R_{\mathrm{oct}}$ without a separate construction.

## §10.5. Brief summary

AMR-SR:

$$
\mathcal R=\mathbb N_{>0}^2,
\qquad
(a,b)=g(p,q),
\qquad
\mathrm{Res}_{\mathrm{sr}}=(g-1)|p-q|.
$$

AMR-DC:

$$
D(N)=\{d:d\mid N\},
\qquad
D(N)\cong\prod_i\{0,\ldots,a_i\},
\qquad
D(p_1\cdots p_n)\cong Q_n.
$$

The joint motive is the extraction of gcd. There is no strict merging of branches in this document; it remains a task for a separate bridge construction.

---

# §11. Birkhoff horizon

The strict core of AMR-DC is built on divisor carriers

$$
D(N)=\{d:d\mid N\}.
$$

For

$$
N=p_1^{a_1}\cdots p_r^{a_r}
$$

there is

$$
D(N)\cong\prod_{i=1}^{r}\{0,\ldots,a_i\}.
$$

Such a carrier is a finite product of chains. This is already a finite distributive lattice: intersection and union are given by coordinate-wise minimum and maximum, and in arithmetic language they correspond to gcd and lcm:

$$
d\wedge e=\gcd(d,e),
\qquad
d\vee e=\mathrm{lcm}(d,e).
$$

## §11.1. The expansion ladder

AMR-DC defines a ladder of finite lattices:

$$
\text{Boolean lattices}
\subset
\text{products of chains}
\subset
\text{finite distributive lattices}.
$$

The first level appears for square-free numbers:

$$
D(p_1\cdots p_n)\cong Q_n.
$$

The second level is the common divisor carrier:

$$
D(p_1^{a_1}\cdots p_r^{a_r})\cong\prod_i\{0,\ldots,a_i\}.
$$

The third level specifies the Birkhoff horizon. Birkhoff's theorem on finite distributive lattices states that every such lattice has the form

$$
L\cong J(P),
$$

where $P$ is a finite partially ordered set and $J(P)$ is the lower ideal lattice $P$. The lower ideal $I\subseteq P$ satisfies the condition

$$
y\in I,
\quad
x\le y
\quad\Longrightarrow\quad
x\in I.
$$

The product of chains is a special case. If

$$
P=C_{a_1}\sqcup\cdots\sqcup C_{a_r},
$$

then

$$
J(P)\cong\prod_{i=1}^{r}\{0,\ldots,a_i\}.
$$

The lower ideal in a disconnected union of chains is given by an independent choice of the initial segment in each chain. The length of this segment coincides with the $b_i$ exponent in the divisor

$$
d=p_1^{b_1}\cdots p_r^{b_r}.
$$

## §11.2. What changes outside the divisor carriers

In the divisor carrier the coordinates are independent. For example, for

$$
N=2^3\cdot3^2
$$

we have

$$
D(72)\cong\{0,1,2,3\}\times\{0,1,2\}.
$$

You can independently select the exponents $b_2$ and $b_3$ within acceptable limits.

In the general carrier $J(P)$ the choices depend on the order. If $x\le y$, then an ideal containing $y$ must contain $x$. For the two-element chain $x<y$ the lower ideals are equal to

$$
\varnothing,
\qquad
\{x\},
\qquad
\{x,y\}.
$$

The set $\{y\}$ is not a lower ideal. Therefore, dependent coordinates appear outside the products of chains: the state cannot be assembled as an independent profile of prime exponent exponents.

## §11.3. Horizon status

Strict AMR-DC result:

$$
D(N)\cong\prod_i\{0,\ldots,a_i\}.
$$

Birkhoff horizon:

$$
L\cong J(P).
$$

It is not included in the strict core of divisors. Its purpose is to denote the natural finite lattice extension after products of chains.

A future paper on the Birkhoff extension should separately specify:

```text
carrier: J(P);
relations: inclusion of ideals and cover relation;
readings: ideal size, boundary, support, orbits;
recovery: exact recovery of the ideal or explicitly specified factor readings;
status: horizon before integration with DOT relational grammar.
```

---

# §12. Additional Views

This chapter captures additional readings that may be useful but are not automatically included in the strict core of AMR-DC. The basic structure of AMR-DC is given by the data

$$
D(N),\quad \mid,\quad C_N,\quad \delta_N,\quad \Omega_N,\omega_N,\mathrm{supp}_N,\quad q_{\gcd}.
$$

Finite-field, Singer, spectral and topological readings require additional selections or produce coarser invariants. Their status is pavement or horizontal unless they have a carrier, relation, reading, and recovery specified.

## §12.1. Finite field reading

For a square-free number

$$
N_n=p_1\cdots p_n
$$

there is a strict isomorphism

$$
D(N_n)\cong Q_n.
$$

After choosing an additional structure, the vector space $Q_n\cong\mathbb{F}_2^n$ can be identified with the finite field $\mathbb{F}_{2^n}$. This is not the canonical structure of the divisor carrier: you need to choose a basis, a field multiplication and, if a Singer cycle is required, a primitive element.

It is important to maintain the distinction:

$$
Q_n^*=Q_n\setminus\{0^n\},
\qquad
U_n=Q_n\setminus\{0^n,1^n\},
\qquad
V_n=S_1^{(n)}\sqcup S_{n-1}^{(n)}.
$$

The finite-field multiplicative reading naturally lives on $Q_n^*$, while the divisor carrier gives $U_n$, and the outer DOT layer is $V_n$. Therefore, for $n=4$ you cannot mix three different objects:

$$
|Q_4^*|=15,
\qquad
|U_4|=14,
\qquad
|V_4|=8.
$$

## §12.2. Spectral reading

If a finite graph is given on the carrier

$$
G=(X,R),
$$

the spectrum of the adjacency matrix or Laplacian can be considered:

$$
\mathrm{Spec}(A_G),
\qquad
\mathrm{Spec}(L_G).
$$

For AMR-DC, for example, cover graphs, layer-interior graphs, complement graphs, $R_{\mathrm{oct}}$, residue graphs and gcd-difference graphs are possible. A spectrum is a valid invariant of a given graph, but it is rough: different graphs can be cospectral, and the same carrier can support several different relations. Therefore, spectral reading does not replace the explicit setting of $R$.

## §12.3. Topological reading

From a finite lattice of divisors one can construct order complexes, cellular complexes and shell complexes. For example, for a partially ordered set $(D(N),\mid)$ we can consider the order complex $\Delta(D(N))$, whose simplices are chains

$$
d_0<d_1<\cdots<d_k.
$$

For its proper carrier we can similarly consider $\Delta(D^\circ(N))$. In the case of square-free numbers, the carrier $D(N_n)\cong Q_n$ can be read through the geometry of the cube after choosing an ordered prime basis. These constructions remain finite and verifiable, but their topological status is supplementary reading and not an automatic part of the strict core of AMR-DC.

## §12.4. Algebraic-Lie reading $A_2/\mathfrak{sl}_3/\mathfrak{su}(3)$

Status of this item: [B].

On its proper carrier

$$
D^\circ(30)=\{2,3,5,6,10,15\}
$$

relation

$$
R_{\mathrm{sh}}\cong K_3\sqcup K_3
$$

splits the scene into two three-point layers:

$$
S_1^{30}=\{2,3,5\},
\qquad
S_2^{30}=\{6,10,15\}.
$$

Complement involution

$$
\delta_{30}(d)=30/d
$$

specifies pairs

$$
2\leftrightarrow15,
\qquad
3\leftrightarrow10,
\qquad
5\leftrightarrow6.
$$

This provides a bridge to the six-position $A_2/\mathfrak{sl}_3/\mathfrak{su}(3)$-reading from `../02_Bridges/03_A2_sl3_su3/DOT_Six_State_A2_sl3_su3_RU.md`:

$$
\{2,3,5\}
\quad\leftrightarrow\quad
\mathbf 3,
$$

$$
\{15,10,6\}
\quad\leftrightarrow\quad
\overline{\mathbf 3}.
$$

Here the prime coordinates $2,3,5$ are read as the three weights of the fundamental three-point layer, and the additional divisors $15,10,6$ are read as the dual three-point layer. The relation $R_{\mathrm{sh}}$ gives two components $K_3$, and $\delta_{30}$ gives a duality between them.

This does not add new algebra inside AMR-DC. Only the support $D^\circ(30)$, layers, relation $R_{\mathrm{sh}}$ and involution $\delta_{30}$ are strictly constructed. Algebro-Lie names are bridged readings of these finite data.

## §12.5. Hopf/Borromean-reading of the complement

Status of this item: [B].

Three pairs of complement

$$
\{2,15\},
\qquad
\{3,10\},
\qquad
\{5,6\}
$$

give the arithmetic image of three axial blocks of rank $3$:

$$
H_1,\quad H_2,\quad H_3.
$$

With the chosen order of prime coordinates, we can write:

$$
\{2,15\}\leftrightarrow H_1,
\qquad
\{3,10\}\leftrightarrow H_2,
\qquad
\{5,6\}\leftrightarrow H_3.
$$

Involution

$$
\delta_{30}:d\mapsto30/d
$$

has here the status of an arithmetic avatar half return:

$$
\delta_{30}
\quad\leftrightarrow\quad
T^3
$$

in the rank transport reading of the Hopf/Borromean-bridge `../02_Bridges/04_Hopf_Borromean/DOT_Principles_Hopf_2x3_Full_2026-04-24.md`.

The strict AMR-DC layer contains only finite pairs of complement and involution. Hopf-, Möbius- and Borromean-images require a separate topological layer with a given support, embedding and invariants.

## §12.6. Möbius function as horizontal reading

Status of this item: [H].

The classical Möbius function naturally appears on the divisor carrier. For

$$
d=p_1^{b_1}\cdots p_r^{b_r}
$$

it is given by the rule:

$$
\mu(d)=0
\quad
\text{if at least one} b_i>1,
$$

and

$$
\mu(d)=(-1)^{\omega(d)}
$$

for divisors without squares.

If $N$ is square-free, then all divisors $d\in D(N)$ are also square-free, and the Möbius function becomes a pure layer reading:

$$
\mu(d)=(-1)^{\omega_N(d)}.
$$

In the general case, $\mu$ distinguishes between the Boolean part of the support and the chain ones thickenings: it resets states where any prime coordinate has an exponent greater than $1$. Therefore, the Möbius function can be used as a horizontal reading of the boundary between square-free Boolean carrier and product-of-chains carrier.

The classical identity

$$
\sum_{d\mid N}\mu(d)=
\begin{cases}
1,&N=1,\\
0,&N>1
\end{cases}
$$

is not a new statement of AMR-DC. In this document it fixes a possible external inverse language for layer functions on $D(N)$.

---

# §13. Open Issues and Validation Tests

This section specifies the tests that new AMR-DC assertions must pass.

## §13.1. Strict core tests

For number

$$
N=p_1^{a_1}\cdots p_r^{a_r}
$$

the following data is checked.

1. Carrier degradation:

$$
D(N)\cong\prod_i\{0,\ldots,a_i\}.
$$

2. Cover graph:

$$
(D(N),C_N)\cong P_{a_1+1}\square\cdots\square P_{a_r+1}.
$$

3. Involution of addition:

$$
\delta_N(d)=N/d,
\qquad
\delta_N^2=id,
\qquad
d\mid e\Longleftrightarrow \delta_N(e)\mid\delta_N(d).
$$

4. Layer readings:

$$
\Omega_N(d)=\sum_i b_i,
\qquad
\omega_N(d)=|\{i:b_i>0\}|,
\qquad
\mathrm{supp}_N(d)=\{p_i:b_i>0\}.
$$

Support reading is accurate only in the case of square-free numbers.

## §13.2. Test of rank 3

For a

$$
30=2\cdot3\cdot5
$$

central carrier:

$$
D^\circ(30)=\{2,3,5,6,10,15\}.
$$

Four relations must be tested on it:

$$
(D^\circ(30),C_{30}^\circ)\cong C_6,
$$

$$
R_{\mathrm{sh}}\cong K_3\sqcup K_3,
$$

$$
R_{\pm}\cong 3K_2,
$$

$$
R_{\mathrm{oct}}\cong K_{2,2,2}.
$$

The last relation is called $R_{\mathrm{oct}}$, $R_{\mathrm{cross}}$ or $R_{\mathrm{noncomp}}$, not by a residue name.

## §13.3. Recovery

Each reading must be accompanied by a recovery status. For $q_{\gcd}$:

$$
q_{\gcd}:\mathbb Z/N\mathbb Z\to D(N),
\qquad
q_{\gcd}([a])=\gcd(a,N),
$$

the fiber over $d\in D(N)$ has the form

$$
q_{\gcd}^{-1}(d)\cong (\mathbb Z/(N/d)\mathbb Z)^\times,
$$

and size

$$
|q_{\gcd}^{-1}(d)|=\varphi(N/d).
$$

This is exact recovery of the divisor, but not exact recovery of the original residue class: it requires data on the invertible multiplier in the fiber.

## §13.4. Integration with AMR-SR

AMR-SR and AMR-DC have a common gcd extraction motif, but different carriers:

$$
\mathcal R=\mathbb N_{>0}^2
\qquad\text{and}\qquad
D(N)=\{d:d\mid N\}.
$$

Potential bridge mappings:

$$
F_N(a,b)=\gcd(a,b,N),
$$

$$
G_N(a,b)=(\gcd(a,N),\gcd(b,N)),
$$

$$
H_N(a,b)=\gcd(a-b,N),
$$

$$
K_N(a,b)=\gcd(|p-q|,N),
\qquad
(a,b)=g(p,q),\quad \gcd(p,q)=1.
$$

The first test ground for such mappings is the synchronous diagonal of AMR-SR

$$
\mathfrak D_{\mathrm{sync}}=\{(P_n,A_n):n\ge3\},
$$

introduced into `03A_DOT_AMR_Scale_Residue_Line_EN.md`. On this diagonal, the scale/residue branch has exact one-parameter matches, so any SR bridge $\to$ DC must first check the behavior of $F_N,G_N,H_N,K_N$ there.

Any such bridge must explicitly specify the source, image, transportable relation, and recovery data. It is forbidden to identify the scalar residue AMR-SR

$$
\mathrm{Res}_{\mathrm{sr}}=(g-1)|p-q|
$$

with a graph relation

$$
R_{\mathrm{oct}}.
$$

## §13.5. Open problem of rank 3

Central open problem: compare the arithmetic scene

$$
D^\circ(30)\cong Q_3\setminus\{000,111\}
$$

with other readings of rank 3: graph, octahedral, Hopf-pair, finite field, color, topological and transport. Each comparison must maintain the boundary between strict construction, bridge reading, and horizontal expansion.

---

# §14. Conclusion

AMR-DC formalizes a composite number as a finite carrier of distinctions. For

$$
N=p_1^{a_1}\cdots p_r^{a_r}
$$

divisors form a finite lattice

$$
D(N)\cong\prod_i\{0,\ldots,a_i\}.
$$

In the case of square-free numbers, this lattice becomes a Boolean carrier:

$$
D(p_1\cdots p_n)\cong Q_n.
$$

The first complete case of rank 3 is given by the number

$$
30=2\cdot3\cdot5,
$$

and its proper carrier

$$
D^\circ(30)=\{2,3,5,6,10,15\}
$$

implements a strict grammar of relations

$$
C_6,
\qquad
K_3\sqcup K_3,
\qquad
3K_2,
\qquad
K_{2,2,2}.
$$

The strict core of AMR-DC consists of the divisor carrier, divisibility, cover relations, $d\mapsto N/d$ duality, layered readings, and recovery discipline. The bridge layer connects this arithmetic with the Boolean core of DOT. Horizontal areas include chain expansion, Birkhoff lattices, residue fibers, zero divisor graphs, spectral readings, finite field labeling, and integration with AMR-SR.

Final status:

$$ 
\boxed{\text{AMR-DC is a strict arithmetic divisor core and a bridge to the Boolean DOT core.}}
$$
