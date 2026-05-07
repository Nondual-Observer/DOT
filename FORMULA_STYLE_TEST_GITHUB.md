
# §9. Incidence package октаэдрального слоя

## §9.1. Две стороны incidence-слоя

Обозначим vertex-side:

$$
V_O:=X_{\mathrm{adm}}.
$$

Обозначим chamber-side:

$$
C_O:=\mathrm{Cham}(O_3).
$$

По §7:

$$
V_O = \lbrace 001,010,011,100,101,110\rbrace.
$$

По §8.5 зафиксирована маркировка complement-пар:

$$
b_1^0=001,
\qquad
b_1^1=110,
$$

$$
b_2^0=010,
\qquad
b_2^1=101,
$$

$$
b_3^0=100,
\qquad
b_3^1=011.
$$
То есть
$$
\beta_1=\lbrace b_1^0,b_1^1\rbrace,
\qquad
\beta_2=\lbrace b_2^0,b_2^1\rbrace,
\qquad
\beta_3=\lbrace b_3^0,b_3^1\rbrace.
$$

Эта маркировка реализует знаковый произвол §7.6: перестановка $b_i^0\leftrightarrow b_i^1$ внутри любой $\beta_i$ меняет координатную запись и сохраняет incidence-структуру с точностью до изоморфизма.

Камера имеет вид

$$
C_\varepsilon = \lbrace b_1^{\varepsilon_1},b_2^{\varepsilon_2},b_3^{\varepsilon_3}\rbrace, \qquad \varepsilon=(\varepsilon_1,\varepsilon_2,\varepsilon_3)\in\lbrace 0,1\rbrace^3.
$$

В битовой записи §3.6 та же камера обозначается

$$
C_{\varepsilon_3\,\varepsilon_2\,\varepsilon_1}.
$$

Следовательно,

$$
|V_O|=6,
\qquad
|C_O|=8.
$$


## §9.2. Incidence relation

**Определение 9.1.**
Incidence relation октаэдрального package-а есть отношение

$$
\mathrm{Inc}_O \subset V_O\times C_O
$$

такое, что

$$
(x,C)\in\mathrm{Inc}_O
$$

тогда и только тогда, когда

$$
x\in C.
$$

То есть вершина incident камере тогда и только тогда, когда она входит в vertex-support этой камеры.

В координатной записи:

$$
(b_i^\eta,C_\varepsilon)\in\mathrm{Inc}_O
$$

тогда и только тогда, когда

$$
\varepsilon_i=\eta.
$$

Эквивалентно:

$$
b_i^\eta\in C_\varepsilon
\quad\Longleftrightarrow\quad
\varepsilon_i=\eta.
$$

Эта формула следует прямо из определения камеры в §8.5: камера $C_\varepsilon$ содержит ровно элемент $b_i^{\varepsilon_i}$ из пары $\beta_i$.


## §9.3. Incidence как vertex-chamber relation

Incidence relation не совпадает с отношением

$$
R_{12}
$$

на vertex-side.

Отношение

$$
R_{12}\subset V_O\times V_O
$$

связывает вершины с вершинами.

Отношение

$$
R_{\mathrm{ch}}\subset C_O\times C_O
$$

связывает камеры с камерами.

А отношение

$$
\mathrm{Inc}_O\subset V_O\times C_O
$$

связывает объекты разных типов:

$$
\text{vertex} \longleftrightarrow \text{chamber}.
$$

Поэтому §9 вводит новый two-type relation-layer на $V_O\sqcup C_O$.


## §9.4. Incidence-count

**Замечание 9.2.**
Каждая камера incident ровно трём вершинам, а каждая вершина incident ровно четырём камерам.

Действительно, камера имеет вид

$$
C_\varepsilon = \lbrace b_1^{\varepsilon_1},b_2^{\varepsilon_2},b_3^{\varepsilon_3}\rbrace.
$$

Она содержит ровно по одной вершине из каждой complement-пары, значит ровно три вершины.

Если

$$
x=b_i^\eta,
$$

то камера $C_\varepsilon$ содержит $x$ тогда и только тогда, когда

$$
\varepsilon_i=\eta.
$$

Одна координата $\varepsilon_i$ зафиксирована. Две остальные свободны, поэтому число таких камер равно

$$
2\cdot 2=4.
$$

Общее число incidences равно

$$
24.
$$

Оно вычисляется с двух сторон:

$$
|C_O|\cdot 3 = 8\cdot 3 = 24,
$$

$$
|V_O|\cdot 4 = 6\cdot 4 = 24.
$$


## §9.5. Star вершины и coordinate faces

**Определение 9.3.**
Для вершины

$$
x\in V_O
$$

её incidence-star называется множество

$$
\mathrm{Star}(x) = \lbrace C\in C_O:(x,C)\in\mathrm{Inc}_O\rbrace.
$$

То есть $\mathrm{Star}(x)$ есть множество всех камер, содержащих вершину $x$.

Для

$$
x=b_i^\eta
$$

получаем координатную формулу:

$$
\mathrm{Star}(b_i^\eta) = \lbrace C_\varepsilon:\varepsilon_i=\eta\rbrace.
$$

По §9.4:

$$
|\mathrm{Star}(b_i^\eta)|=4.
$$

**Определение 9.4.**
Coordinate face в $Q_3$ называется подмножество вида

$$
F_i^\eta = \lbrace \varepsilon\in Q_3:\varepsilon_i=\eta\rbrace,
$$

где

$$
i\in\lbrace 1,2,3\rbrace,
\qquad
\eta\in\lbrace 0,1\rbrace.
$$

Каждая coordinate face имеет четыре элемента и изоморфна $Q_2$.

В chamber-coordinate reading-е

$$
C_O\cong Q_3
$$

множество $\mathrm{Star}(b_i^\eta)$ читается как coordinate face

$$
F_i^\eta.
$$

Следовательно, каждая вершина октаэдрального skeleton-а соответствует одной coordinate face chamber-cube:

$$
\text{vertex of }O_3^{(1)} \longleftrightarrow \text{coordinate face of }Q_3.
$$

Это прямое следствие incidence relation.


## §9.6. Complement-пары как противоположные coordinate faces

Пусть

$$
b_i^0,b_i^1\in\beta_i
$$

— две вершины одной complement-пары.

Тогда

$$
\mathrm{Star}(b_i^0) = \lbrace C_\varepsilon:\varepsilon_i=0\rbrace,
$$

$$
\mathrm{Star}(b_i^1) = \lbrace C_\varepsilon:\varepsilon_i=1\rbrace.
$$

**Замечание 9.5.**
Эти два множества не пересекаются:

$$
\mathrm{Star}(b_i^0) \cap \mathrm{Star}(b_i^1) = \varnothing.
$$

Их объединение даёт весь chamber-side:

$$
\mathrm{Star}(b_i^0) \cup \mathrm{Star}(b_i^1) = C_O.
$$

Следовательно, complement-пара вершин октаэдрального skeleton-а читается на chamber-side как пара противоположных coordinate faces в $Q_3$:

$$
\beta_i = \lbrace b_i^0,b_i^1\rbrace \quad \longleftrightarrow \quad \lbrace F_i^0,F_i^1\rbrace.
$$

Это следствие выбранной координатной записи камер.


## §9.7. Смежность вершин восстанавливается из incidence

**Утверждение 9.6.**
Для двух разных вершин

$$
x,y\in V_O
$$

имеем:

$$
(x,y)\in R_{12}
$$

тогда и только тогда, когда

$$
\mathrm{Star}(x)\cap\mathrm{Star}(y)\neq\varnothing.
$$

Более точно:

$$
|\mathrm{Star}(x)\cap\mathrm{Star}(y)|=2
$$

если $x$ и $y$ лежат в разных complement-парах, и

$$
|\mathrm{Star}(x)\cap\mathrm{Star}(y)|=0
$$

если

$$
\lbrace x,y\rbrace=\beta_i
$$

для некоторого $i$.

**Проверка.**
Пусть

$$
x=b_i^\eta,
\qquad
y=b_j^\mu.
$$
Тогда
$$
\mathrm{Star}(x) = \lbrace C_\varepsilon:\varepsilon_i=\eta\rbrace,
$$

$$
\mathrm{Star}(y) = \lbrace C_\varepsilon:\varepsilon_j=\mu\rbrace.
$$

Если

$$
i=j
$$

и

$$
\eta\neq \mu,
$$

то условия

$$
\varepsilon_i=\eta,
\qquad
\varepsilon_i=\mu
$$
несовместимы. Поэтому
$$
\mathrm{Star}(x)\cap\mathrm{Star}(y)=\varnothing.
$$

Это случай complement-пары.

Если

$$
i\neq j,
$$

то два условия

$$
\varepsilon_i=\eta,
\qquad
\varepsilon_j=\mu
$$
фиксируют две координаты $\varepsilon$, а третья остаётся свободной. Поэтому существует ровно две камеры, содержащие одновременно $x$ и $y$:
$$
|\mathrm{Star}(x)\cap\mathrm{Star}(y)|=2.
$$
По §7 relation $R_{12}$ связывает ровно вершины из разных complement-пар и не связывает две вершины одной complement-пары. Следовательно,
$$
(x,y)\in R_{12}
\quad\Longleftrightarrow\quad
\mathrm{Star}(x)\cap\mathrm{Star}(y)\neq\varnothing.
$$

$$
\Box
$$

Это означает, что skeleton

$$
(V_O,R_{12})
$$

можно восстановить из incidence relation.


## §9.8. Chamber-adjacency восстанавливается из incidence

Для камеры

$$
C\in C_O
$$

обозначим её vertex-support:

$$
\mathrm{Vert}(C) = \lbrace x\in V_O:(x,C)\in\mathrm{Inc}_O\rbrace.
$$

По определению камеры:

$$
|\mathrm{Vert}(C)|=3.
$$

**Утверждение 9.7.**
Для двух разных камер

$$
C,D\in C_O
$$

имеем:

$$
(C,D)\in R_{\mathrm{ch}}
$$

тогда и только тогда, когда

$$
|\mathrm{Vert}(C)\cap\mathrm{Vert}(D)|=2.
$$

**Проверка.**
По §8.6 relation $R_{\mathrm{ch}}$ было задано правилом:

$$
(C,D)\in R_{\mathrm{ch}}
\quad\Longleftrightarrow\quad
C\neq D \land |C\cap D|=2.
$$
Но $C$ и $D$ в §8 уже являются vertex-support-ами камер, поэтому
$$
C\cap D = \mathrm{Vert}(C)\cap\mathrm{Vert}(D).
$$
Также по §8.6:
$$
|C_\varepsilon\cap C_\delta|=2 \quad\Longleftrightarrow\quad d_H(\varepsilon,\delta)=1.
$$

Значит, определение через пересечение vertex-support-ов и Hamming-one definition на $Q_3$ дают одно и то же отношение $R_{\mathrm{ch}}$.

Следовательно,

$$
(C,D)\in R_{\mathrm{ch}}
\quad\Longleftrightarrow\quad
|\mathrm{Vert}(C)\cap\mathrm{Vert}(D)|=2.
$$

$$
\Box
$$

Таким образом, incidence relation восстанавливает vertex-skeleton и chamber-adjacency.


## §9.9. Incidence matrix

После фиксации маркировки камер

$$
C_{\varepsilon_3\,\varepsilon_2\,\varepsilon_1}, \quad \varepsilon_i \in \lbrace 0,1\rbrace.
$$

incidence relation можно записать булевой матрицей.

Пусть строки индексируются вершинами:

$$
b_1^0,
b_1^1,
b_2^0,
b_2^1,
b_3^0,
b_3^1.
$$
Пусть столбцы индексируются камерами в порядке, согласованном с bit-order §3.6:
$$
C_{000},C_{001},C_{010},C_{011},
C_{100},C_{101},C_{110},C_{111}.
$$
Здесь индекс $abc$ у $C_{abc}$ означает
$$
a=\varepsilon_3,
\qquad
b=\varepsilon_2,
\qquad
c=\varepsilon_1.
$$

**Определение 9.8.**
Incidence matrix октаэдрального package-а есть матрица

$$
B_O
\in
\lbrace 0,1\rbrace^{6\times 8}
$$
с элементами
$$
(B_O)_{b_i^\eta,\varepsilon} = 1
$$
тогда и только тогда, когда
$$
(b_i^\eta,C_\varepsilon)\in\mathrm{Inc}_O.
$$
По формуле §9.2 это равносильно:
$$
(B_O)_{b_i^\eta,\varepsilon} = 1 \quad\Longleftrightarrow\quad \varepsilon_i=\eta.
$$
В выбранном порядке строк и столбцов:
$$
B_O =
\begin{pmatrix}
1&0&1&0&1&0&1&0\\
0&1&0&1&0&1&0&1\\
1&1&0&0&1&1&0&0\\
0&0&1&1&0&0&1&1\\
1&1&1&1&0&0&0&0\\
0&0&0&0&1&1&1&1
\end{pmatrix}.
$$
Каждый столбец содержит три единицы:
$$
\sum_{x\in V_O}(B_O)_{x,\varepsilon}=3.
$$
Каждая строка содержит четыре единицы:
$$
\sum_{\varepsilon\in Q_3}(B_O)_{b_i^\eta,\varepsilon}=4.
$$

Матрица $B_O$ является записью incidence relation. Relation-грамматика остаётся заданной самими relation-слоями. Другой выбор маркировки внутри complement-пар или другой порядок строк и столбцов даёт матрицу, полученную перестановками строк и столбцов.


## §9.10. Incidence graph

**Определение 9.9.**
Incidence graph октаэдрального package-а есть двудольный граф

$$
G_{\mathrm{inc}}(O)
$$

с множеством вершин

$$
V_O\sqcup C_O
$$

и рёбрами

$$
x \mathrel{-} C
$$

тогда и только тогда, когда

$$
(x,C)\in\mathrm{Inc}_O.
$$

Этот graph двудольный, потому что все его рёбра идут только между vertex-side $V_O$ и chamber-side $C_O$.

Он имеет

$$
|V_O|+|C_O|=6+8=14
$$

вершин и

$$
24
$$

рёбер.

Степени двух типов различны:

$$
\deg(x)=4 \quad (x\in V_O),
$$

$$
\deg(C)=3 \quad (C\in C_O).
$$

То есть

$$
G_{\mathrm{inc}}(O)
$$

является $(4,3)$-bipartite incidence graph-ом.

Число

$$
14=6+8
$$

здесь означает typed sum:

$$
6\ \text{vertices} + 8\ \text{chambers}.
$$

Это дизъюнктный $14$-элементный carrier с двумя типами вершин.


## §9.11. Двухтипный carrier

Чтобы записать incidence как relation на одном carrier-е, вводится дизъюнктная сумма:

$$
Z_O = V_O \sqcup C_O.
$$

Элементы $Z_O$ имеют type:

$$
\mathrm{type}(z)=
\begin{cases}
\mathrm{v}, & z\in V_O,\\
\mathrm{c}, & z\in C_O.
\end{cases}
$$

Здесь $\mathrm{v}$ означает vertex-type, а $\mathrm{c}$ означает chamber-type.

На $Z_O$ задаются три отношения.

Vertex-relation:

$$
R_{vv}:=R_{12} \subset V_O\times V_O.
$$

Chamber-relation:

$$
R_{cc}:=R_{\mathrm{ch}} \subset C_O\times C_O.
$$

Cross-type incidence relation:

$$
R_{vc} \subset Z_O\times Z_O
$$

задаётся как симметризация $\mathrm{Inc}_O$:

$$
R_{vc} = \lbrace (x,C),(C,x):x\in V_O, \ C\in C_O, \ (x,C)\in\mathrm{Inc}_O\rbrace.
$$

**Определение 9.10.**
Полное relation-package §9 есть

$$
R_O = R_{vv} \cup R_{cc} \cup R_{vc}.
$$

Тогда

$$
(Z_O,R_O)
$$

является two-type incidence carrier-ом октаэдрального слоя.


## §9.12. Incidence presentation

**Определение 9.11.**
Incidence presentation октаэдрального слоя есть

$$
\Pi_O^{\mathrm{inc}} = \left( Z_O, R_O, \mathrm{id}_{Z_O}, \mathrm{rec}_{\mathrm{id}} \right),
$$

где

$$
Z_O=V_O\sqcup C_O,
$$

$$
R_O=R_{vv}\cup R_{cc}\cup R_{vc},
$$

$$
\mathrm{id}_{Z_O}:Z_O\to Z_O
$$

— identity-reading.

Отношение $R_O$ иррефлексивно: $R_{vv}$ и $R_{cc}$ связывают разные элементы внутри своих типов, а $R_{vc}$ связывает элементы разных типов. Поэтому

$$
R_O|_{\lbrace z\rbrace}=\varnothing
$$

для каждого

$$
z\in Z_O.
$$

Recovery datum задаётся как

$$
\mathrm{rec}_{\mathrm{id}}(z) = (\lbrace z\rbrace,\varnothing).
$$

Так как reading является identity-reading-ом, presentation exact.

Эта presentation записывает incidence-layer как relation-carrier с фиксированным identity-reading и recovery datum.


## §9.13. Recoverability incidence package

Из incidence package восстанавливаются две relation-структуры.

Первая:

$$
\begin{aligned}
R_{12}
\end{aligned}
$$

на vertex-side, потому что

$$
\begin{aligned}
(x,y) &\in R_{12} \\
\Longleftrightarrow\quad \mathrm{Star}(x)\cap\mathrm{Star}(y) &\neq \varnothing.
\end{aligned}
$$
Вторая:
$$
\begin{aligned}
R_{\mathrm{ch}}
\end{aligned}
$$
на chamber-side, потому что
$$
\begin{aligned}
(C,D) &\in R_{\mathrm{ch}} \\
\Longleftrightarrow\quad |\mathrm{Vert}(C)\cap\mathrm{Vert}(D)| &= 2.
\end{aligned}
$$
Дополнительно incidence relation имеет матричную форму:
$$
\begin{aligned}
(B_O)_{x,C} &= 1 \\
\Longleftrightarrow\quad (x,C) &\in \mathrm{Inc}_O.
\end{aligned}
$$
Следовательно, incidence package связывает две стороны октаэдрального graph-reading-а:
$$
\begin{aligned}
O_3^{(1)} \\
\mathrm{and} \\
\mathrm{Cham}(O_3) &\cong Q_3
\end{aligned}
$$

в одну two-type finite structure.






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
