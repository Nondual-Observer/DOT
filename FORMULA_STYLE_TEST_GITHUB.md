# GitHub Formula Style Test

Temporary diagnostic file for choosing a stable formula style for GitHub Markdown.

Each item repeats the same mathematical content in several forms:

- **A**: compact one-line display formula;
- **B**: display formula with `aligned`;
- **C**: split multiline formula without `aligned` where useful, to test whether GitHub breaks it.

## 1. Representation Tuple

### 1A. One-line display

$$
(X, R, q, \mathrm{rec}).
$$

### 1B. Aligned

$$
\begin{aligned}
\Pi &= (X, R, q, \mathrm{rec}).
\end{aligned}
$$

## 2. Rank Growth Map

### 2A. One-line display

$$
\Lambda_n: \{0,1\} \times Q_n \to Q_{n+1}, \qquad \Lambda_n(\varepsilon, x)=\varepsilon \mid x.
$$

### 2B. Aligned

$$
\begin{aligned}
\Lambda_n &: \{0,1\} \times Q_n \to Q_{n+1},\\
\Lambda_n(\varepsilon, x) &= \varepsilon \mid x.
\end{aligned}
$$

### 2C. Split without aligned

$$
\Lambda_n: \{0,1\} \times Q_n \to Q_{n+1},
\qquad
\Lambda_n(\varepsilon, x)=\varepsilon \mid x.
$$

## 3. Closure Package

### 3A. One-line display

$$
\mathfrak R_{\leq 5}^{\mathrm{fin}} = (\Pi_1, \mathfrak C_2, \mathfrak C_3, \mathfrak C_4, \mathfrak A_5).
$$

### 3B. Aligned

$$
\begin{aligned}
\mathfrak R_{\leq 5}^{\mathrm{fin}} &= (\Pi_1, \mathfrak C_2, \mathfrak C_3, \mathfrak C_4, \mathfrak A_5).
\end{aligned}
$$

### 3C. Split without aligned

$$
\mathfrak R_{\leq 5}^{\mathrm{fin}}
=
(\Pi_1,\mathfrak C_2,\mathfrak C_3,\mathfrak C_4,\mathfrak A_5).
$$

## 4. Emergence Decomposition

### 4A. One-line display

$$
Q_n^* = Q_{n-1}^* \sqcup \{e_n\} \sqcup (e_n + Q_{n-1}^*).
$$

### 4B. Aligned

$$
\begin{aligned}
Q_n^* &= Q_{n-1}^* \sqcup \{e_n\} \sqcup (e_n + Q_{n-1}^*).
\end{aligned}
$$

### 4C. Broken/missing-equals control

$$
Q_n^*
Q_{n-1}^* \sqcup \{e_n\} \sqcup (e_n + Q_{n-1}^*).
$$

## 5. Recovery Subrelation

### 5A. One-line display

$$
R_y^{\mathrm{rec}} \subseteq R \cap \bigl(X_y^{\mathrm{rec}} \times X_y^{\mathrm{rec}}\bigr).
$$

### 5B. Aligned

$$
\begin{aligned}
R_y^{\mathrm{rec}} &\subseteq R \cap \bigl(X_y^{\mathrm{rec}} \times X_y^{\mathrm{rec}}\bigr).
\end{aligned}
$$

### 5C. Split without aligned

$$
R_y^{\mathrm{rec}}
\subseteq
R \cap
\bigl(X_y^{\mathrm{rec}} \times X_y^{\mathrm{rec}}\bigr).
$$

## 6. Coordinate Swap Chain

### 6A. One-line display

$$
\sigma_1\sigma_2(x) = \sigma_1(x+10) = x+10+01 = x+11.
$$

### 6B. Aligned chain

$$
\begin{aligned}
\sigma_1\sigma_2(x) &= \sigma_1(x+10)\\
&= x+10+01\\
&= x+11.
\end{aligned}
$$

### 6C. Split without aligned

$$
\sigma_1\sigma_2(x)
\sigma_1(x+10)
x+10+01
x+11.
$$

## 7. Shell Definition

### 7A. One-line display

$$
S_k^{(n)} = \{x \in Q_n : |x| = k\}.
$$

### 7B. Aligned

$$
\begin{aligned}
S_k^{(n)} &= \{x \in Q_n : |x| = k\}.
\end{aligned}
$$

### 7C. Split without aligned

$$
S_k^{(n)}
=
\{x \in Q_n : |x| = k\}.
$$

## 8. Divisor Carrier Relation

### 8A. One-line display

$$
C_{30}^{\circ} = C_{30} \cap \binom{D^{\circ}(30)}{2}.
$$

### 8B. Aligned

$$
\begin{aligned}
C_{30}^{\circ} &= C_{30} \cap \binom{D^{\circ}(30)}{2}.
\end{aligned}
$$

### 8C. Split without aligned

$$
C_{30}^{\circ}
=
C_{30} \cap \binom{D^{\circ}(30)}{2}.
$$

## 9. Product Formula

### 9A. One-line display

$$
\prod_{i=1}^{6}\varepsilon_i' = \prod_{i=1}^{6} g_{i+1}\varepsilon_i g_i = \left(\prod_{i=1}^{6} g_i^2\right)\left(\prod_{i=1}^{6}\varepsilon_i\right) = +1.
$$

### 9B. Aligned chain

$$
\begin{aligned}
\prod_{i=1}^{6}\varepsilon_i'
&= \prod_{i=1}^{6} g_{i+1}\varepsilon_i g_i\\
&= \left(\prod_{i=1}^{6} g_i^2\right)\left(\prod_{i=1}^{6}\varepsilon_i\right)\\
&= +1.
\end{aligned}
$$

### 9C. Split without aligned

$$
\prod_{i=1}^{6}\varepsilon_i'
\prod_{i=1}^{6} g_{i+1}\varepsilon_i g_i
\left(\prod_{i=1}^{6} g_i^2\right)\left(\prod_{i=1}^{6}\varepsilon_i\right)
+1.
$$

## 10. Set and Complement

### 10A. One-line display

$$
X_{\mathrm{adm}} = Q_3 \setminus \{000,111\}.
$$

### 10B. Aligned

$$
\begin{aligned}
X_{\mathrm{adm}} &= Q_3 \setminus \{000,111\}.
\end{aligned}
$$

### 10C. Split without aligned

$$
X_{\mathrm{adm}}
=
Q_3 \setminus \{000,111\}.
$$

