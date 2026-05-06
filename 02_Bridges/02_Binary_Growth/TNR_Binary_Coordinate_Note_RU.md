# Заметка A. Бинарные координаты в ТНР

Статус: пояснительная заметка к strict finite core.

Эта заметка имеет статус internal explanatory note. Она фиксирует binary coordinate convention, используемую внутри finite-rank construction.

---

## A.1. Coordinate carrier

Для rank $n$:

$$
Q_n=\mathbb{F}_2^n.
$$

Элемент

$$
x=(x_n,\ldots,x_1)
$$

есть binary state с $n$ координатами.

Нулевое состояние:

$$
0^n=(0,\ldots,0).
$$

Полное состояние:

$$
1^n=(1,\ldots,1).
$$

Ненулевой слой:

$$
Q_n^*=Q_n\setminus\{0^n\}.
$$

Полный нетривиальный слой:

$$
U_n=Q_n\setminus\{0^n,1^n\}.
$$

---

## A.2. Hamming-вес и shells

Hamming-вес:

$$
|x|=\#\{i:x_i=1\}.
$$

Shell:

$$
S_k^{(n)}=\{x\in Q_n:|x|=k\}.
$$

Тогда:

$$
Q_n=\bigsqcup_{k=0}^n S_k^{(n)}.
$$

Для nonzero carrier:

$$
Q_n^*=\bigsqcup_{k=1}^n S_k^{(n)}.
$$

Для full nontrivial carrier:

$$
U_n=\bigsqcup_{k=1}^{n-1}S_k^{(n)}.
$$

---

## A.3. Hamming relations

Для $X\subseteq Q_n$:

$$
\mathsf H_k^{(n)}|_X
=
\{(x,y)\in X\times X:x\neq y,\ d_H(x,y)=k\}.
$$

Здесь:

$$
d_H(x,y)=|\{i:x_i\neq y_i\}|.
$$

В rank $3$ на carrier-е

$$
X_{\mathrm{adm}}=Q_3\setminus\{000,111\},
$$

эти relation-layers имеют вид:

$$
R_1,\quad R_2,\quad R_3.
$$

Они дают:

$$
R_1\cong C_6,
\qquad
R_2\cong K_3\sqcup K_3,
\qquad
R_3\cong 3K_2.
$$

---

## A.4. Complement

Complement map:

$$
\kappa_n(x)=x+1^n.
$$

Она удовлетворяет:

$$
\kappa_n^2=\mathrm{id}_{Q_n}.
$$

Shell action:

$$
\kappa_n:S_k^{(n)}\to S_{n-k}^{(n)}.
$$

Для нечётного $n=2m+1$:

$$
S_m^{(n)}
\leftrightarrow
S_{m+1}^{(n)}.
$$

Для чётного $n=2m$:

$$
S_m^{(n)}
\leftrightarrow
S_m^{(n)}.
$$

---

## A.5. Rank growth

Rank-lift из $n$ в $n+1$ использует приписывание нового старшего разряда слева:

$$
\varepsilon\,|\,x=(\varepsilon,x_n,\ldots,x_1).
$$

Binary rank-lift:

$$
\Lambda_n:\mathbb{F}_2\times Q_n\to Q_{n+1},
\qquad
\Lambda_n(\varepsilon,x)=\varepsilon\,|\,x.
$$

Отсюда:

$$
Q_{n+1}
=
(0\,|\,Q_n)\sqcup(1\,|\,Q_n).
$$

Для nonzero layer:

$$
Q_{n+1}^*
=
(0\,|\,Q_n^*)
\sqcup
\{1\,|\,0^n\}
\sqcup
(1\,|\,Q_n^*).
$$

Это emergence-order.

Shell-order вычисляется после сборки полного carrier-а.

---

## A.6. Статус

Binary coordinate system принадлежит strict finite construction.

Она задаёт:

$$
Q_n,
\qquad
S_k^{(n)},
\qquad
d_H,
\qquad
\kappa_n,
\qquad
\Lambda_n.
$$

Bridge-layer отображает конечные структуры в другой реализованный domain, например в RGB/Kuhn colour geometry. Эта заметка фиксирует внутренний coordinate language strict core.

---

## A.7. Полезные рисунки

### Рисунок A1. $Q_1,Q_2,Q_3$

$$
Q_1=\{0,1\},
$$

$$
Q_2=\{00,01,10,11\},
$$

$$
Q_3=\{000,001,010,011,100,101,110,111\}.
$$

### Рисунок A2. Shell-decomposition of $Q_3$

$$
S_0=\{000\},
$$

$$
S_1=\{001,010,100\},
$$

$$
S_2=\{011,101,110\},
$$

$$
S_3=\{111\}.
$$

### Рисунок A3. Complement-pairs in $Q_3$

$$
000\leftrightarrow111,
$$

$$
001\leftrightarrow110,
$$

$$
010\leftrightarrow101,
$$

$$
100\leftrightarrow011.
$$

### Рисунок A4. Rank-lift $Q_3^*\to Q_4^*$

$$
Q_4^*
=
(0\,|\,Q_3^*)
\sqcup
\{1000\}
\sqcup
(1\,|\,Q_3^*).
$$

Назначение: различить emergence-order и shell-order.
