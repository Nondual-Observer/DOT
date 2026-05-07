# §10. Orientation и cyclic transport на $C_6$

## §10.1. $R_1$ как неориентированный цикл

По §6 relation

$$
\begin{aligned}
R_1
\end{aligned}
$$

на

$$
\begin{aligned}
X_{\mathrm{adm}} &= \lbrace \mathtt{001},\mathtt{010},\mathtt{011},\mathtt{100},\mathtt{101},\mathtt{110}\rbrace.
\end{aligned}
$$

задано правилом:

$$
\begin{aligned}
(x,y) \in R_1 &\Longleftrightarrow d_H(x,y)=1.
\end{aligned}
$$

Graph-reading:

$$
\begin{aligned}
(X_{\mathrm{adm}}, R_1) &\cong C_6.
\end{aligned}
$$

Один cyclic order, совместимый с $R_1$, имеет вид:

$$
\begin{aligned}
\mathtt{001} &\to \mathtt{011} \to \mathtt{010} \to \mathtt{110} \to \mathtt{100} \to \mathtt{101} \to \mathtt{001}.
\end{aligned}
$$

Каждая соседняя пара имеет Hamming-distance $1$:

$$
\begin{aligned}
d_H(\mathtt{001},\mathtt{011}) &= d_H(\mathtt{011},\mathtt{010}) = d_H(\mathtt{010},\mathtt{110}) = 1.
\end{aligned}
$$

$$
\begin{aligned}
d_H(\mathtt{110},\mathtt{100}) &= d_H(\mathtt{100},\mathtt{101}) = d_H(\mathtt{101},\mathtt{001}) = 1.
\end{aligned}
$$

На уровне §6 это был только неориентированный graph-reading. В §10 добавляется orientation.


## §10.2. Выбор orientation

**Определение 10.1.**
Зафиксируем orientation на

$$
\begin{aligned}
(X_{\mathrm{adm}}, R_1) &\cong C_6
\end{aligned}
$$

следующим образом:

$$
\begin{aligned}
\mathtt{001} &\to \mathtt{011} \to \mathtt{010} \to \mathtt{110} \to \mathtt{100} \to \mathtt{101} \to \mathtt{001}
\end{aligned}
$$

Обозначим ориентированный цикл через

$$
\begin{aligned}
\vec C_6
\end{aligned}
$$

Этот выбор не следует из одного только отношения $R_1$. Relation $R_1$ задаёт неориентированный цикл; orientation является новым transport-данным.

Обратная orientation тоже допустима:

$$
\begin{aligned}
\mathtt{001} &\to \mathtt{101} \to \mathtt{100} \to \mathtt{110} \to \mathtt{010} \to \mathtt{011} \to \mathtt{001}
\end{aligned}
$$

В текущем transport-layer-е фиксируется первая orientation. Обратная orientation дала бы оператор

$$
\begin{aligned}
T^{-1}
\end{aligned}
$$


## §10.3. Cyclic transport operator

**Определение 10.2.**
Cyclic transport operator

$$
\begin{aligned}
T:X_{\mathrm{adm}}\to X_{\mathrm{adm}}
\end{aligned}
$$

задаётся по выбранной orientation:

$$
\begin{aligned}
T(\mathtt{001})=\mathtt{011}, \quad T(\mathtt{011})=\mathtt{010}, \quad T(\mathtt{010})=\mathtt{110}.
\end{aligned}
$$

$$
\begin{aligned}
T(\mathtt{110})=\mathtt{100}, \quad T(\mathtt{100})=\mathtt{101}, \quad T(\mathtt{101})=\mathtt{001}.
\end{aligned}
$$

В строковой форме:

$$
\begin{aligned}
T:\mathtt{001} \to \mathtt{011} \to \mathtt{010} \to \mathtt{110} \to \mathtt{100} \to \mathtt{101} \to \mathtt{001}.
\end{aligned}
$$

Оператор $T$ является биекцией множества $X_{\mathrm{adm}}$. Его обратный оператор

$$
\begin{aligned}
T^{-1}=T^5
\end{aligned}
$$

соответствует обратной orientation.


## §10.4. $T$ как $R_1$-step

**Утверждение 10.3.**
Для каждого

$$
\begin{aligned}
x\in X_{\mathrm{adm}}
\end{aligned}
$$

имеем:

$$
\begin{aligned}
(x,T(x))\in R_1.
\end{aligned}
$$

**Проверка.**
По определению $T$ каждая пара

$$
\begin{aligned}
x \to T(x)
\end{aligned}
$$

является соседней парой в цикле

$$
\begin{aligned}
\mathtt{001} \to \mathtt{011} \to \mathtt{010} \to \mathtt{110} \to \mathtt{100} \to \mathtt{101} \to \mathtt{001}.
\end{aligned}
$$

Этот цикл есть graph-reading отношения $R_1$. Следовательно,

$$
\begin{aligned}
d_H(x,T(x))=1,
\end{aligned}
$$

то есть

$$
\begin{aligned}
(x,T(x))\in R_1.
\end{aligned}
$$

$$
\begin{aligned}
\Box
\end{aligned}
$$

В сжатой форме: $T$ является ориентированным $R_1$-шагом.


## §10.5. Directed transport relation

**Определение 10.4.**
Directed transport relation есть отношение

$$
\begin{aligned}
\vec R_T \subset X_{\mathrm{adm}}\times X_{\mathrm{adm}}
\end{aligned}
$$

такое, что

$$
\begin{aligned}
(x,y)\in\vec R_T \quad\Longleftrightarrow\quad y=T(x).
\end{aligned}
$$

То есть

$$
\begin{aligned}
\vec R_T = \lbrace (x,T(x)):x\in X_{\mathrm{adm}}\rbrace.
\end{aligned}
$$

В явном виде:

$$
\begin{aligned}
\vec R_T = \lbrace (\mathtt{001},\mathtt{011}),(\mathtt{011},\mathtt{010}),(\mathtt{010},\mathtt{110}),(\mathtt{110},\mathtt{100}),(\mathtt{100},\mathtt{101}),(\mathtt{101},\mathtt{001}) \rbrace.
\end{aligned}
$$

Обратное directed relation:

$$
\begin{aligned}
\vec R_T^{-1} = \lbrace (T(x),x):x\in X_{\mathrm{adm}}\rbrace.
\end{aligned}
$$

**Следствие 10.5.**
Симметризация directed transport relation восстанавливает $R_1$:

$$
\begin{aligned}
R_1 = \vec R_T \cup \vec R_T^{-1}.
\end{aligned}
$$

**Проверка.**
По Утверждению 10.3:

$$
\begin{aligned}
\vec R_T\subset R_1.
\end{aligned}
$$

Relation $R_1$ является симметричным неориентированным $6$-cycle-ом в directed записи: он содержит $12$ направленных пар. Relation $\vec R_T$ содержит $6$ направленных пар, по одной orientation для каждого ребра цикла. Поэтому

$$
\begin{aligned}
\vec R_T\cup\vec R_T^{-1}
\end{aligned}
$$

содержит обе направленности всех шести рёбер $R_1$, и совпадает с $R_1$.

$$
\begin{aligned}
\Box
\end{aligned}
$$

Следовательно, $T$ выбирает одну из двух ориентаций уже построенного relation-layer-а $R_1$.


## §10.6. Relation-грамматика и transport

Relation-грамматика §6 была static:

$$
\begin{aligned}
\mathcal R_{\mathrm{adm}}^{(3)} = \lbrace R_1, R_2, R_3\rbrace.
\end{aligned}
$$

Transport-layer добавляет direction, composition, path, iteration и return. В этой записи

$$
\begin{aligned}
R_1
\end{aligned}
$$

есть неориентированное соседство,

$$
\begin{aligned}
\vec R_T
\end{aligned}
$$

есть ориентированное transport-соседство, а

$$
\begin{aligned}
T
\end{aligned}
$$

есть оператор следующего шага.


## §10.7. Path category ориентированного цикла

После выбора $T$ определены один шаг и композиции шагов.

**Определение 10.6.**
Path category ориентированного transport-cycle-а обозначается

$$
\begin{aligned}
\mathrm{Path}_T(C_6).
\end{aligned}
$$

Её объекты:

$$
\begin{aligned}
\mathrm{Ob}(\mathrm{Path}_T(C_6)) = X_{\mathrm{adm}}.
\end{aligned}
$$

Порождающие стрелки:

$$
\begin{aligned}
x \to T(x)
\end{aligned}
$$

для всех

$$
\begin{aligned}
x\in X_{\mathrm{adm}}.
\end{aligned}
$$

Композиция задаётся итерацией:

$$
\begin{aligned}
x \to T(x) \to T^2(x) \to \cdots \to T^k(x).
\end{aligned}
$$

То есть путь длины $k$ из $x$ приходит в

$$
\begin{aligned}
T^k(x).
\end{aligned}
$$

В §10 эта категория фиксирует path-composition. В §11 она факторизуется периодом

$$
\begin{aligned}
T^6=\mathrm{id}.
\end{aligned}
$$


## §10.8. Cyclic action до periodization

Оператор $T$ задаёт действие целочисленной итерации:

$$
\begin{aligned}
\rho_T:\mathbb Z\to \mathrm{Sym}(X_{\mathrm{adm}})
\end{aligned}
$$

по формуле

$$
\begin{aligned}
\rho_T(k)=T^k.
\end{aligned}
$$

Для каждого

$$
\begin{aligned}
x\in X_{\mathrm{adm}}
\end{aligned}
$$

получаем orbit-map:

$$
\begin{aligned}
\gamma_x:\mathbb Z\to X_{\mathrm{adm}},
\qquad
\gamma_x(k)=T^k(x).
\end{aligned}
$$
На уровне §10 это записано как итерация по $\mathbb Z$. В §11 orbit-map факторизуется через
$$
\begin{aligned}
\mathbb Z/6\mathbb Z.
\end{aligned}
$$

То есть §10 вводит cyclic transport, а §11 закрывает его periodization.


## §10.9. $T$ сохраняет static relation-грамматику

**Утверждение 10.7.**
Оператор $T$ сохраняет Hamming relation-слои:

$$
\begin{aligned}
(x,y)\in R_k
\quad\Longleftrightarrow\quad
(Tx,Ty)\in R_k
\end{aligned}
$$
для
$$
\begin{aligned}
k=1,2,3.
\end{aligned}
$$

**Проверка.**
Для $R_1$ это следует из того, что $T$ является rotation выбранного $C_6$. Rotation цикла переводит соседние вершины в соседние вершины.

Для $R_3$ relation задаёт complement-пары:

$$
\begin{aligned}
001\leftrightarrow110,
\qquad
010\leftrightarrow101,
\qquad
100\leftrightarrow011.
\end{aligned}
$$
Проверим действие $T$ на этих парах:
$$
\begin{aligned}
\lbrace 001,110\rbrace\mapsto\lbrace 011,100\rbrace,
\end{aligned}
$$

$$
\begin{aligned}
\lbrace 100,011\rbrace\mapsto\lbrace 101,010\rbrace,
\end{aligned}
$$

$$
\begin{aligned}
\lbrace 010,101\rbrace\mapsto\lbrace 110,001\rbrace.
\end{aligned}
$$

Значит, $T$ переставляет complement-пары и сохраняет $R_3$.

По §6.7 relation-грамматика

$$
\begin{aligned}
\lbrace R_1, R_2, R_3\rbrace
\end{aligned}
$$

разбивает все пары разных элементов $X_{\mathrm{adm}}$ по Hamming-distance. Так как $T$ биективен и сохраняет $R_1$ и $R_3$, он сохраняет и дополнение к ним внутри множества всех пар, то есть $R_2$.

$$
\begin{aligned}
\Box
\end{aligned}
$$

Следовательно,

$$
\begin{aligned}
T\in
\mathrm{Aut}
\bigl(
X_{\mathrm{adm}},
R_1, R_2, R_3
\bigr).
\end{aligned}
$$


## §10.10. Extension на chamber-side

По §§8–9 имеется chamber-side:

$$
\begin{aligned}
C_O=\mathrm{Cham}(O_3).
\end{aligned}
$$

Для подмножества $C\subset X_{\mathrm{adm}}$ обозначим

$$
\begin{aligned}
T[C]:=\lbrace T(x):x\in C\rbrace.
\end{aligned}
$$

Так как $T$ переставляет complement-пары

$$
\begin{aligned}
\beta_1,\beta_2,\beta_3,
\end{aligned}
$$

образ камеры снова является камерой.

**Определение 10.8.**
Chamber-transport

$$
\begin{aligned}
T_{\mathrm{ch}}:C_O\to C_O
\end{aligned}
$$

задаётся правилом

$$
\begin{aligned}
T_{\mathrm{ch}}(C)=T[C].
\end{aligned}
$$

Если

$$
\begin{aligned}
C\in \mathrm{Cham}(O_3),
\end{aligned}
$$

то $C$ содержит ровно одну вершину из каждой complement-пары. Поскольку $T$ переставляет complement-пары, множество $T[C]$ также содержит ровно одну вершину из каждой complement-пары. Значит,

$$
\begin{aligned}
T[C]\in \mathrm{Cham}(O_3).
\end{aligned}
$$

Поэтому $T_{\mathrm{ch}}$ корректно определён.


## §10.11. Совместимость с incidence

**Утверждение 10.9.**
Transport $T$ сохраняет incidence:

$$
\begin{aligned}
(x,C)\in\mathrm{Inc}_O
\quad\Longleftrightarrow\quad
(Tx,T_{\mathrm{ch}}C)\in\mathrm{Inc}_O.
\end{aligned}
$$

**Проверка.**
По определению incidence:

$$
\begin{aligned}
(x,C)\in\mathrm{Inc}_O
\quad\Longleftrightarrow\quad
x\in C.
\end{aligned}
$$
Но
$$
\begin{aligned}
x\in C
\quad\Longleftrightarrow\quad
T(x)\in T[C].
\end{aligned}
$$
А
$$
\begin{aligned}
T[C]=T_{\mathrm{ch}}(C).
\end{aligned}
$$
Следовательно,
$$
\begin{aligned}
(x,C)\in\mathrm{Inc}_O
\quad\Longleftrightarrow\quad
(Tx,T_{\mathrm{ch}}C)\in\mathrm{Inc}_O.
\end{aligned}
$$

$$
\begin{aligned}
\Box
\end{aligned}
$$

Тем самым transport действует на vertex-side и на incidence package.


## §10.12. Transport automorphism incidence-carrier-а

По §9 был построен two-type carrier:

$$
\begin{aligned}
Z_O = V_O\sqcup C_O,
\end{aligned}
$$

где

$$
\begin{aligned}
V_O=X_{\mathrm{adm}},
\qquad
C_O=\mathrm{Cham}(O_3).
\end{aligned}
$$

**Определение 10.10.**
Полный transport automorphism на incidence carrier-е есть отображение

$$
\begin{aligned}
T_Z:Z_O\to Z_O
\end{aligned}
$$

такое, что

$$
\begin{aligned}
T_Z(x)=T(x)
\end{aligned}
$$

для

$$
\begin{aligned}
x\in V_O,
\end{aligned}
$$

и

$$
\begin{aligned}
T_Z(C)=T_{\mathrm{ch}}(C)
\end{aligned}
$$

для

$$
\begin{aligned}
C\in C_O.
\end{aligned}
$$

Так как $T$ сохраняет $R_{12}$, $T_{\mathrm{ch}}$ сохраняет chamber-adjacency, а вместе они сохраняют incidence, получаем:

$$
\begin{aligned}
T_Z\in
\mathrm{Aut}(Z_O,R_O).
\end{aligned}
$$
Здесь
$$
\begin{aligned}
R_O = R_{vv}\cup R_{cc}\cup R_{vc}
\end{aligned}
$$

— full relation-package §9.


## §10.13. Transport presentations

**Определение 10.11.**
Vertex transport presentation есть exact presentation

$$
\begin{aligned}
\Pi_T^{V} = \left( X_{\mathrm{adm}}, \vec R_T, \mathrm{id}_{X_{\mathrm{adm}}}, \mathrm{rec}_{\mathrm{id}} \right),
\end{aligned}
$$

где

$$
\begin{aligned}
\vec R_T = \lbrace (x,T(x)):x\in X_{\mathrm{adm}}\rbrace.
\end{aligned}
$$

Reading является identity-reading-ом. Recovery datum задаётся как

$$
\begin{aligned}
\mathrm{rec}_{\mathrm{id}}(x) = (\lbrace x\rbrace,\varnothing),
\end{aligned}
$$

поскольку $\vec R_T$ иррефлексивно.

**Определение 10.12.**
Incidence transport presentation есть exact incidence presentation §9:

$$
\begin{aligned}
\Pi_O^{\mathrm{inc}} = \left( Z_O, R_O, \mathrm{id}_{Z_O}, \mathrm{rec}_{\mathrm{id}} \right),
\end{aligned}
$$

рассматриваемая вместе с дополнительным automorphism-данным

$$
\begin{aligned}
T_Z\in\mathrm{Aut}(Z_O,R_O).
\end{aligned}
$$

Строгий формат presentation остаётся четверкой. Transport фиксируется как operator-структура над exact presentation.
