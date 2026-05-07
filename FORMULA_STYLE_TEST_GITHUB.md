
# §1. Полярная presentation

### §1.1. Тривиальные и содержательные presentations

Формальная структура presentation допускает тривиальные случаи. Например,

$$
X=\lbrace *\rbrace,
$$

$$
R=\varnothing,
$$

$$
q=\mathrm{id}_{\lbrace *\rbrace},
$$

$$
\mathrm{rec}(*)=(\lbrace *\rbrace,\varnothing).
$$

Это корректная presentation с одноточечным волокном identity-reading-а. Recovery datum имеет вид $(\lbrace *\rbrace,\varnothing)$.

Содержательная начальная единица должна содержать хотя бы одно нетривиальное волокно: два различимых элемента carrier-а читаются как один элемент reading-а и остаются восстановимыми как различимые.

Минимальный такой случай содержит ровно два элемента.


### §1.2. Полярный слой

**Определение 1.1.**
Полярный слой есть relational carrier

$$
(P,R_P),
$$

где

$$
P=\lbrace a,-a\rbrace,
$$

а

$$
R_P=\lbrace (a,-a),(-a,a)\rbrace.
$$

Отношение $R_P$ симметрично и иррефлексивно. Оно записано через упорядоченные пары для согласования с общей записью

$$
R\subseteq X\times X.
$$

Полярный слой фиксирует неориентированную пару $(a,-a)$.

Элементы

$$
a,\quad -a
$$

называются полярностями.


### §1.3. Инвариантное чтение

Пусть

$$
\mathbf I=\lbrace I\rbrace.
$$

Задаётся reading

$$
\pi:P\to \mathbf I
$$

по формуле

$$
\pi(a)=I,
$$

$$
\pi(-a)=I.
$$

Отображение $\pi$ сюръективно:

$$
\mathrm{Im}(\pi)=\mathbf I.
$$

В carrier-е $P$ имеются две различимые полярности:

$$
a,\quad -a.
$$

В reading-е $\mathbf I$ они имеют один образ:

$$
\pi(a)=\pi(-a)=I.
$$

Элемент $I$ есть образ обеих полярностей в reading-е $\pi$. Поэтому $I$ называется инвариантным чтением полярного слоя.


### §1.4. Recovery datum полярного слоя

Волокно над $I$:

$$
\pi^{-1}(I)=P=\lbrace a,-a\rbrace.
$$

Ограничение отношения на это волокно:

$$
R_P|_{\pi^{-1}(I)}=R_P.
$$

**Определение 1.2.**
Recovery datum полярного слоя задаётся формулой

$$
\mathrm{rec}_P(I)=(P,R_P).
$$

Это полное восстановление над $I$.


### §1.5. Первая presentation

**Определение 1.3.**
Первая presentation есть

$$
\Pi_1=(P,R_P,\pi,\mathrm{rec}_P),
$$

где

$$
P=\lbrace a,-a\rbrace,
$$

$$
R_P=\lbrace (a,-a),(-a,a)\rbrace,
$$

$$
\pi:P\to \mathbf I,
\qquad
\pi(a)=\pi(-a)=I,
$$

$$
\mathrm{rec}_P(I)=(P,R_P).
$$

Presentation $\Pi_1$ является exact: единственный элемент reading-а имеет полное восстановление.

Действительно,

$$
\pi^{-1}(I)=P,
\qquad
R_P|_{\pi^{-1}(I)}=R_P,
$$
поэтому
$$
\mathrm{rec}_P(I)=(P,R_P) = \bigl(\pi^{-1}(I),R_P|_{\pi^{-1}(I)}\bigr).
$$
Сжатая запись:
$$
\lbrace a,-a\rbrace\xrightarrow{\pi} I,
\qquad
\mathrm{rec}_P(I)=(P,R_P).
$$

В $\Pi_1$ зафиксированы:

- две полярности;
- одно инвариантное чтение;
- полное восстановление полярного отношения.

<p align="center">
  <a href="../assets/figures/1.1-P_R_P.png">
    <img src="../assets/figures/1.1-P_R_P.png" width="500" alt="Полярный слой $(P,R_P)$">
  </a>
</p>

Пустой круг $I$ на рисунке не является вершиной носителя $P$. Он обозначает образ чтения:

$$
\pi(a)=\pi(-a)=I.
$$

# §2. Автоморфизмы над инвариантным чтением

### §2.1. Автоморфизм полярного слоя над $I$

После задания $\Pi_1$ можно рассматривать биекции carrier-а, сохраняющие данные presentation.

**Определение 2.1.**
Автоморфизмом полярного слоя над $I$ называется биекция

$$
f:P\to P
$$

такая, что

$$
(x,y)\in R_P
\Longleftrightarrow
(f(x),f(y))\in R_P,
$$
и
$$
\pi\circ f=\pi.
$$
Множество таких автоморфизмов обозначается
$$
\mathrm{Aut}_I(P,R_P).
$$

В случае $\Pi_1$ оба условия выполняются для любой биекции $P\to P$: reading $\pi$ постоянен, а $R_P$ является полным симметричным отношением между двумя различными элементами.

Содержательная роль этих условий проявляется на более богатых carrier-ах, где reading и relation перестают быть тривиальными.


### §2.2. Две биекции полярного слоя

Двухэлементное множество $P$ имеет ровно две биекции.

Первая:

$$
\mathrm{id}_P(a)=a,
$$

$$
\mathrm{id}_P(-a)=-a.
$$

Вторая:

$$
\tau(a)=-a,
$$

$$
\tau(-a)=a.
$$

**Утверждение 2.2.**

$$
\mathrm{Aut}_I(P,R_P)=\lbrace \mathrm{id}_P,\tau\rbrace.
$$

**Проверка.**
На двухэлементном множестве всякая биекция либо оставляет оба элемента на месте, либо меняет их местами. Эти два случая дают

$$
\mathrm{id}_P
$$

и

$$
\tau.
$$

Других биекций двухэлементного множества нет.

Обе биекции сохраняют $R_P$ и $\pi$. Следовательно,

$$
\mathrm{Aut}_I(P,R_P)=\lbrace \mathrm{id}_P,\tau\rbrace.
$$

### §2.3. Канонический swap

**Определение 2.3.**
Автоморфизм

$$
\tau(a)=-a,
\qquad
\tau(-a)=a
$$

называется каноническим swap-ом полярного слоя.

Он удовлетворяет

$$
\tau^2=\mathrm{id}_P.
$$

Проверка:

$$
\tau^2(a)=\tau(-a)=a,
$$

$$
\tau^2(-a)=\tau(a)=-a.
$$

### §2.4. Локальная инволюция

Свойство

$$
\tau^2=\mathrm{id}_P
$$

описывает локальную инволюцию полярного слоя.

Двойное применение swap-а восстанавливает исходную полярность:

$$
a\mapsto -a\mapsto a,
$$

$$
-a\mapsto a\mapsto -a.
$$

В §§0–2 задана локальная инволюция exact-полярного волокна.


# §3. Первый rank-lift: координатная запись полярности

### §3.1. От полярности к координате

Полярный слой

$$
P=\lbrace a,-a\rbrace
$$

задаёт две различимые полярности одного инвариантного чтения.

Для рангового расширения нужна запись, в которой несколько независимых полярных слоёв можно ставить рядом как координаты. Такой записью является бит.

**Определение 3.1.**
Координатной записью полярного слоя называется биекция

$$
c:P\to \mathbb{F}_2
$$

вида

$$
c(a)=0,
\qquad
c(-a)=1.
$$

Выбор, какая полярность получает $0$, а какая получает $1$, является выбором записи. Структура полярного слоя задаётся двухэлементностью, отношением $R_P$ и swap-симметрией.

Если выбрать обратную запись

$$
c'(a)=1,
\qquad
c'(-a)=0,
$$
то
$$
c'=s\circ c,
\qquad
s(x)=x+1.
$$

То есть две координатные записи отличаются тем же swap-ом, который уже задан внутри полярного слоя.

В выбранной координатной записи канонический swap принимает вид

$$
c\circ\tau\circ c^{-1}(x)=x+1
\qquad
x\in\mathbb{F}_2.
$$
Проверка:
$$
0\mapsto 1,
\qquad
1\mapsto 0.
$$

Так локальный swap получает алгебраическую запись как прибавление единицы в $\mathbb{F}_2$.


### §3.2. Ранг 1 как координатная форма первого слоя

**Определение 3.2.**
Координатный carrier ранга $1$ есть

$$
Q_1=\mathbb{F}_2=\lbrace 0,1\rbrace.
$$

На нём задано полярное отношение

$$
R_1^{\mathrm{pol}}=\lbrace (0,1),(1,0)\rbrace.
$$

Reading ранга $1$:

$$
q_1:Q_1\to\mathbf I,
$$

$$
q_1(0)=q_1(1)=I.
$$

Recovery datum:

$$
\mathrm{rec}_1(I)=(Q_1,R_1^{\mathrm{pol}}).
$$

Получается координатная presentation

$$
\Pi_1^{\mathrm{coord}} = (Q_1,R_1^{\mathrm{pol}},q_1,\mathrm{rec}_1).
$$

Эта запись получается из $\Pi_1$ заменой имён элементов через $c$:

$$
a\mapsto 0,
\qquad
-a\mapsto 1.
$$
Reading сохраняется при этой замене:
$$
q_1(c(x))=\pi(x)
\qquad
x\in P.
$$
Relation и recovery datum также переносятся по $c$:
$$
(c\times c)(R_P)=R_1^{\mathrm{pol}},
$$

$$
\mathrm{rec}_1(I)=(c(P),(c\times c)(R_P)).
$$

Полярный слой получил координатную форму.


### §3.3. Полный carrier и проявленные состояния

Координатная запись позволяет строить carrier-ы из нескольких независимых битов.

**Определение 3.3.**
Полный координатный carrier ранга $n$ есть

$$
Q_n=\mathbb{F}_2^n.
$$

Его элемент

$$
x=(x_1,\ldots,x_n)
$$

записывает состояние $n$ полярных координат.

Нулевое состояние

$$
0^n=(0,\ldots,0)
$$

называется пустым координатным состоянием.

Состояние

$$
x\neq 0^n
$$

называется проявленным координатным состоянием: хотя бы одна координата находится в положении $1$.

Множество всех проявленных состояний обозначается

$$
Q_n^*=\mathbb{F}_2^n\setminus\lbrace 0^n\rbrace.
$$

Для (n=1):

$$
Q_1=\lbrace 0,1\rbrace,
$$

$$
Q_1^*=\lbrace 1\rbrace.
$$

Здесь $Q_1$ — полный координатный carrier полярного слоя, а $Q_1^*$ — register его ненулевого проявления.

$Q_1$ и $Q_1^*$ имеют разные carrier-роли.


### §3.4. Координатный carrier $Q_n$

Carrier

$$
Q_n=\mathbb{F}_2^n
$$

используется как координатная область состояний.

Presentation на $Q_n$ требует ещё трёх данных:

$$
\text{relation},
\qquad
\text{reading},
\qquad
\text{recovery datum}.
$$

Они задаются отдельными конструкциями поверх выбранного множества.


### §3.5. Координатные swap-ы

Пусть

$$
e_i=(0,\ldots,0,1,0,\ldots,0)
$$

— базисный вектор с единицей в $i$-й координате.

Локальный swap в $i$-й координате записывается как

$$
\sigma_i(x)=x+e_i.
$$

Здесь сложение берётся в $\mathbb{F}_2^n$.

Для $n=1$ это совпадает с записью канонического swap-а:

$$
x\mapsto x+1.
$$

Для $n>1$ формула

$$
x\mapsto x+e_i
$$

меняет только одну полярную координату и оставляет остальные координаты неизменными.

Локальные swap-ы $\sigma_i$ используются в §4 для описания симметрий двухбитного carrier-а.


### §3.6. Новый разряд

Соглашение о записи: новый разряд занимает старшую позицию слева. Обратное соглашение даёт изоморфный carrier через перестановку координат.
Для перехода

$$
Q_{n-1}\to Q_n
$$

мы отождествляем старый carrier с подмножеством

$$
Q_{n-1}\cong \lbrace 0\rbrace\times Q_{n-1}\subset Q_n.
$$

Новый базисный разряд:

$$
e_n=(1,0,\ldots,0)\in Q_n.
$$

Тогда

$$
Q_n=\mathbb{F}_2 e_n\oplus Q_{n-1}.
$$

Блок нового разряда:

$$
B_n=e_n+Q_{n-1}.
$$

Он содержит все состояния, в которых новый разряд включён.


### §3.7. Emergence-разложение

Положим

$$
\begin{aligned}
Q_0 &= \lbrace 0\rbrace, \\
Q_0^* &= \varnothing.
\end{aligned}
$$

**Утверждение 3.4.**
Для $n\geq 1$

$$
\begin{aligned}
Q_n^* &= Q_{n-1}^* \sqcup \lbrace e_n\rbrace \sqcup (e_n+Q_{n-1}^*).
\end{aligned}
$$

**Проверка.**
Каждый элемент $x\in Q_n$ имеет вид

$$
\begin{aligned}
x &= \varepsilon e_n+y,
\end{aligned}
$$

где

$$
\begin{aligned}
\varepsilon &\in \mathbb{F}_2, \\
y &\in Q_{n-1}.
\end{aligned}
$$

Если

$$
\begin{aligned}
\varepsilon &= 0,
\end{aligned}
$$

то

$$
\begin{aligned}
x &= y.
\end{aligned}
$$

Так как $x\neq 0^n$, получаем

$$
\begin{aligned}
y &\in Q_{n-1}^*.
\end{aligned}
$$

Значит,
$$
\begin{aligned}
x &\in Q_{n-1}^*.
\end{aligned}
$$

Если

$$
\begin{aligned}
\varepsilon &= 1,
\end{aligned}
$$

то

$$
\begin{aligned}
x &= e_n+y.
\end{aligned}
$$

При

$$
\begin{aligned}
y &= 0
\end{aligned}
$$

получаем

$$
\begin{aligned}
x &= e_n.
\end{aligned}
$$

При

$$
\begin{aligned}
y &\neq 0
\end{aligned}
$$

получаем

$$
\begin{aligned}
x &\in e_n+Q_{n-1}^*.
\end{aligned}
$$

Три случая не пересекаются. Следовательно,

$$
\begin{aligned}
Q_n^* &= Q_{n-1}^* \sqcup \lbrace e_n\rbrace \sqcup (e_n+Q_{n-1}^*).
\end{aligned}
$$

### §3.8. Смысл rank-lift

Rank-lift имеет три части:

$$
\text{old},
$$

$$
\text{new},
$$

$$
\text{old-with-new}.
$$

В формуле:

$$
Q_n^* = Q_{n-1}^* \sqcup \lbrace e_n\rbrace \sqcup (e_n+Q_{n-1}^*).
$$

Старый слой сохраняется:

$$
Q_{n-1}^*.
$$

Новый разряд задаёт отдельную координату:

$$
\lbrace e_n\rbrace.
$$

Старый слой с новой координатной нагрузкой:

$$
e_n+Q_{n-1}^*.
$$

Rank-lift добавляет новый разряд и одновременно перечитывает весь уже собранный ненулевой слой.

Первые emergence-блоки:

$$
B_1=\lbrace 1\rbrace,
$$

$$
B_2=\lbrace 10,11\rbrace,
$$

$$
B_3=\lbrace 100,101,110,111\rbrace.
$$

Полные ненулевые слои при этом:

$$
Q_1^*=\lbrace 1\rbrace,
$$

$$
Q_2^*=\lbrace 01\rbrace\sqcup\lbrace 10\rbrace\sqcup\lbrace 11\rbrace,
$$

$$
Q_3^* = \lbrace 001,010,011\rbrace \sqcup \lbrace 100\rbrace \sqcup \lbrace 101,110,111\rbrace.
$$

Emergence-order задаёт порядок появления новых блоков:

$$
1;
$$

$$
10,\ 11;
$$

$$
100,\ 101,\ 110,\ 111.
$$

### §3.9. Shell-order

После сборки полного carrier-а его можно классифицировать по весу Хэмминга.

**Определение 3.5.**
Для

$$
x=(x_1,\ldots,x_n)\in Q_n
$$

вес Хэмминга равен

$$
|x|=x_1+\cdots+x_n.
$$

Shell ранга $n$:

$$
S_k^{(n)} = \lbrace x\in Q_n:\ |x|=k\rbrace.
$$

Emergence-order отвечает за порядок появления разрядов.

Shell-order отвечает за роль элемента внутри уже собранного carrier-а.

Эти два порядка различаются.

Например, в $Q_3^*$ состояние

$$
100
$$

входит как новый разряд rank $3$, а по shell-order имеет вес $1$.
Состояние

$$
011
$$

принадлежит старому слою $Q_2^*$ в emergence-order и имеет вес $2$ по shell-order.



# §4. Ранг 2: первый carrier сравнения

## §4.1. Relation-reading

В §0 reading был определён как отображение

$$
q:X\to Y.
$$

На ранге $2$ используется чтение carrier-а через выбранное отношение $R$. Для этого вводится отдельный термин.

**Определение 4.1.**
Relation-reading на carrier-е $X$ есть presentation

$$
\Pi=(X,R,q,\mathrm{rec}),
$$

в которой структурное различие между чтениями задаётся выбором отношения $R$.

Relation-reading сохраняет общее определение presentation и выделяет relation-компоненту как основной носитель чтения.


## §4.2. Graph-reading

**Определение 4.2.**
Graph-reading называется relation-reading

$$
\Pi=(X,R,q,\mathrm{rec}),
$$

в котором:

$$
R
$$

является графовым отношением смежности на $X$.

Если дополнительно

$$
q=\mathrm{id}_X,
$$

то graph-reading называется identity graph-reading.

В identity graph-reading-е все волокна отображения $q$ одноточечны. Структурная нагрузка находится в $R$.


## §4.3. Exact recovery для identity graph-reading

Далее в graph-reading-ах $C_4$, $2K_2$, $K_4$, $K_4-e$ используется один и тот же recovery datum для identity-reading-а.

Пусть

$$
q=\mathrm{id}_X.
$$

Тогда для каждого $x\in X$

$$
q^{-1}(x)=\lbrace x\rbrace.
$$

Если $R$ иррефлексивно, то

$$
R|_{\lbrace x\rbrace} = R\cap(\lbrace x\rbrace\times\lbrace x\rbrace) = \varnothing.
$$

Поэтому exact recovery для identity graph-reading-а задаётся формулой

$$
\mathrm{rec}_{\mathrm{id}}(x)=(\lbrace x\rbrace,\varnothing).
$$

Это соглашение применяется ниже к graph-reading-ам

$$
C_4,\qquad 2K_2,\qquad K_4,\qquad K_4-e.
$$


## §4.4. Двухбитный carrier

**Определение 4.3.**
Двухбитный carrier есть

$$
Q_2=\mathbb{F}_2^2 = \lbrace 00,01,10,11\rbrace.
$$

<p align="center">
  <a href="../assets/figures/1.2-2_bits_Q_2.png">
    <img src="../assets/figures/1.2-2_bits_Q_2.png" width="500" alt="Двухбитный носитель $Q_2$">
  </a>
</p>

Запись

$$
b_2b_1
$$

означает кортеж

$$
(x_2,x_1)=(b_2,b_1).
$$

Запись согласована с §3.6: новый разряд $x_2$ занимает старшую позицию слева, старая координата $x_1$ — младшую позицию справа.

Координата $x_1$ — старая координата ранга $1$.
Координата $x_2$ — новый разряд, добавленный rank-lift-ом.

По emergence-разложению:

$$
Q_2^* = Q_1^* \sqcup \lbrace e_2\rbrace \sqcup (e_2+Q_1^*).
$$

В битовой записи:

$$
Q_2^* = \lbrace 01\rbrace \sqcup \lbrace 10\rbrace \sqcup \lbrace 11\rbrace.
$$

Здесь

$$
01
$$

— старый проявленный слой,

$$
10
$$

— новый разряд,

$$
11
$$

— старый слой с новой координатной нагрузкой.


## §4.5. Coordinate swap-ы

Пусть

$$
e_1=01,
\qquad
e_2=10.
$$

**Определение 4.4.**
Первый coordinate swap:

$$
\sigma_1(x)=x+e_1.
$$

Второй coordinate swap:

$$
\sigma_2(x)=x+e_2.
$$

В развёрнутой записи:

$$
\sigma_1:
00\leftrightarrow 01,
\qquad
10\leftrightarrow 11.
$$

$$
\sigma_2:
00\leftrightarrow 10,
\qquad
01\leftrightarrow 11.
$$
Оба swap-а продолжают локальный закон ранга $1$:
$$
x\mapsto x+1.
$$

На ранге $2$ этот закон имеет две независимые координатные реализации.


## §4.6. Координатная коммутативность

**Утверждение 4.5.**

$$
\sigma_1\sigma_2=\sigma_2\sigma_1.
$$

Их произведение равно complement-переходу:

$$
\sigma_1\sigma_2(x)=x+11.
$$

**Проверка.**
Для любого $x\in Q_2$:

$$
\sigma_1\sigma_2(x) = \sigma_1(x+10) = x+10+01 = x+11.
$$

Аналогично,

$$
\sigma_2\sigma_1(x) = \sigma_2(x+01) = x+01+10 = x+11.
$$

Следовательно,

$$
\sigma_1\sigma_2=\sigma_2\sigma_1.
$$


## §4.7. Hamming-отношения на $Q_2$

В §3 был введён вес Хэмминга

$$
|x|.
$$

На $Q_2$ расстояние Хэмминга задаётся через этот вес.

**Определение 4.6.**
Для $x,y\in Q_2$

$$
d_H(x,y)=|x+y|.
$$

Вектор $x+y$ отмечает координаты, в которых $x$ и $y$ различаются.

На $Q_2$ есть два нетривиальных Hamming-отношения:

$$
H_1^{(2)} = \lbrace (x,y)\in Q_2^2:x\neq y,\ d_H(x,y)=1\rbrace,
$$

$$
H_2^{(2)} = \lbrace (x,y)\in Q_2^2:x\neq y,\ d_H(x,y)=2\rbrace.
$$

**Утверждение 4.7.**

$$
H_1^{(2)} = \lbrace (x,x+e_i):x\in Q_2,\ i=1,2\rbrace.
$$

$$
H_2^{(2)} = \lbrace (x,x+11):x\in Q_2\rbrace.
$$

**Проверка.**
Если

$$
d_H(x,y)=1,
$$

то

$$
|x+y|=1.
$$

В $Q_2$ это означает

$$
x+y=e_i
$$

для единственного $i\in\lbrace 1,2\rbrace$. Следовательно,

$$
y=x+e_i.
$$

Обратно, если

$$
y=x+e_i,
$$

то

$$
x+y=e_i
$$

и потому

$$
d_H(x,y)=1.
$$

Для расстояния $2$ имеем

$$
|x+y|=2.
$$

В $Q_2$ единственный вектор веса $2$ есть

$$
11.
$$

Значит,

$$
x+y=11,
$$

откуда

$$
y=x+11.
$$

Иными словами,

$$
H_1^{(2)}
$$

есть рёберная структура, порождённая coordinate swap-ами

$$
\sigma_1,\sigma_2.
$$

Переходы $H_1^{(2)}$ — это ровно переходы вида

$$
x\mapsto \sigma_i(x)=x+e_i.
$$


## §4.8. Graph-reading $C_4$

**Определение 4.8.**
Graph-reading $C_4$ на $Q_2$ есть presentation

$$
\Pi_2^{C_4} = (Q_2,H_1^{(2)},\mathrm{id}_{Q_2},\mathrm{rec}_{\mathrm{id}}),
$$

где

$$
\mathrm{rec}_{\mathrm{id}}(x)=(\lbrace x\rbrace,\varnothing).
$$

**Утверждение 4.9.**

$$
(Q_2,H_1^{(2)})\cong C_4.
$$

**Проверка.**
Отношение $H_1^{(2)}$ связывает состояния, отличающиеся ровно в одной координате:

$$
00\leftrightarrow 01,
$$

$$
01\leftrightarrow 11,
$$

$$
11\leftrightarrow 10,
$$

$$
10\leftrightarrow 00.
$$

Каждая вершина имеет степень $2$:

$$
\deg(00)=2,
\quad
\deg(01)=2,
\quad
\deg(10)=2,
\quad
\deg(11)=2.
$$

Граф связен: из любой вершины можно попасть в любую другую по указанным рёбрам.

Связный граф на четырёх вершинах, в котором каждая вершина имеет степень $2$, является циклом длины $4$. Следовательно,

$$
(Q_2,H_1^{(2)})\cong C_4.
$$

Orientation и path-composition здесь не заданы.

<p align="center">
  <a href="../assets/figures/1.3-C_4.png">
    <img src="../assets/figures/1.3-C_4.png" width="500" alt="Graph-reading $C_4$ на $Q_2$">
  </a>
</p>


## §4.9. Graph-reading $2K_2$

**Определение 4.10.**
Graph-reading $2K_2$ на $Q_2$ есть presentation

$$
\Pi_2^{2K_2} = (Q_2,H_2^{(2)},\mathrm{id}_{Q_2},\mathrm{rec}_{\mathrm{id}}).
$$

**Утверждение 4.11.**

$$
(Q_2,H_2^{(2)})\cong 2K_2.
$$

**Проверка.**
Отношение $H_2^{(2)}$ связывает каждое состояние с его complement-состоянием:

$$
x\mapsto x+11.
$$

Получаются две пары:

$$
00\leftrightarrow 11,
$$

$$
01\leftrightarrow 10.
$$

Каждая вершина имеет степень $1$. Компонент связности ровно две:

$$
\lbrace 00,11\rbrace,
\qquad
\lbrace 01,10\rbrace.
$$
Каждая компонента является полным графом на двух вершинах, то есть $K_2$. Следовательно,
$$
(Q_2,H_2^{(2)})\cong K_2\sqcup K_2=2K_2.
$$

<p align="center">
  <a href="../assets/figures/1.4-2K_2.png">
    <img src="../assets/figures/1.4-2K_2.png" width="500" alt="Graph-reading $2K_2$ на $Q_2$">
  </a>
</p>


## §4.10. Компаратор $\chi$

Ранг $1$ содержит одну полярную координату. Сравнение двух координат начинается на ранге $2$.

На ранге $2$ состояние

$$
x=(x_2,x_1)
$$

содержит две координаты. Поэтому вводится comparison-reading.

**Определение 4.12.**
Компаратором ранга $2$ называется отображение

$$
\chi:Q_2\to\mathbb{F}_2
$$

по формуле

$$
\chi(x_2,x_1)=x_2+x_1.
$$

Значения:

$$
\chi(00)=0,
$$

$$
\chi(11)=0,
$$

$$
\chi(01)=1,
$$

$$
\chi(10)=1.
$$

Значение $0$ означает совпадение координат.
Значение $1$ означает различие координат.

Для $Q_2$

$$
\chi(x)=|x|\pmod 2.
$$

Эта формула относится именно к двухбитному carrier-у. Обобщение parity-reading-а на $Q_n$ требует отдельного определения.


## §4.11. Волокна компаратора и comparison-presentation

Компаратор $\chi$ имеет два волокна:

$$
\mathrm{Eq} = \chi^{-1}(0) = \lbrace 00,11\rbrace,
$$

$$
\mathrm{Opp} = \chi^{-1}(1) = \lbrace 01,10\rbrace.
$$

Для comparison-presentation выбирается отношение

$$
H_2^{(2)}.
$$

Причина выбора: $H_2^{(2)}$ является минимальным нетривиальным Hamming-отношением на $Q_2$, рёбра которого лежат внутри волокон $\chi$.

Действительно,

$$
H_2^{(2)} = \lbrace 00\leftrightarrow 11,\ 01\leftrightarrow 10\rbrace.
$$

Обе связи находятся внутри волокон:

$$
00,11\in \chi^{-1}(0),
$$

$$
01,10\in \chi^{-1}(1).
$$

Напротив, отношение

$$
H_1^{(2)}
$$

связывает состояния из разных волокон $\chi$, поскольку изменение одной координаты меняет значение

$$
x_2+x_1.
$$

Поэтому $H_2^{(2)}$ — естественный relation-компонент для comparison-presentation: он сохраняет внутреннюю структуру каждого волокна.

**Определение 4.13.**
Comparison-presentation ранга $2$ есть

$$
\Pi_2^\chi = (Q_2,H_2^{(2)},\chi,\mathrm{rec}_\chi),
$$

где

$$
\mathrm{rec}_\chi(0) = (\lbrace 00,11\rbrace,H_2^{(2)}|_{\lbrace 00,11\rbrace}),
$$

$$
\mathrm{rec}_\chi(1) = (\lbrace 01,10\rbrace,H_2^{(2)}|_{\lbrace 01,10\rbrace}).
$$

**Утверждение 4.14.**
Presentation

$$
\Pi_2^\chi
$$

является exact.

**Проверка.**
Имеем

$$
\chi^{-1}(0)=\lbrace 00,11\rbrace,
$$

$$
\chi^{-1}(1)=\lbrace 01,10\rbrace.
$$

Recovery datum на каждом волокне совпадает с индуцированным отношением $H_2^{(2)}$:

$$
\mathrm{rec}_\chi(0) = (\chi^{-1}(0),H_2^{(2)}|_{\chi^{-1}(0)}),
$$

$$
\mathrm{rec}_\chi(1) = (\chi^{-1}(1),H_2^{(2)}|_{\chi^{-1}(1)}).
$$

Следовательно, $\Pi_2^\chi$ exact.

Reading $\chi$ сводит $Q_2$ к двум режимам:

совпадение и различие.

Recovery datum сохраняет complement-пары, на которых эти режимы реализуются.


## §4.12. Инвариантность comparison-reading-а

**Утверждение 4.15.**
Компаратор $\chi$ инвариантен относительно complement-перехода

$$
x\mapsto x+11.
$$

То есть

$$
\chi(x+11)=\chi(x).
$$

**Проверка.**
Пусть

$$
x=(x_2,x_1).
$$

Тогда

$$
x+11=(x_2+1,x_1+1).
$$

Следовательно,

$$
\chi(x+11) = (x_2+1)+(x_1+1) = x_2+x_1+1+1 = x_2+x_1 = \chi(x).
$$

Значит, complement сохраняет режим сравнения: совпадение остаётся совпадением, различие остаётся различием.



## §4.13. Total poles и puncture на ранге 2

Total poles задаются структурным свойством.

**Определение 4.16.**
Total pole в $Q_n$ называется состояние, в котором все $n$ координат совпадают.

Таких состояний ровно два:

$$
0^n=(0,\ldots,0),
$$

$$
1^n=(1,\ldots,1).
$$

Для ранга $2$ total poles имеют вид

$$
00,
\qquad
11.
$$
Иными словами, в $Q_2$ это состояния
$$
x_2=x_1.
$$

**Определение 4.17.**
Punctured coordinate subset ранга $2$ есть подмножество

$$
Q_2^\circ = Q_2\setminus\lbrace 00,11\rbrace.
$$

То есть

$$
Q_2^\circ=\lbrace 01,10\rbrace.
$$

**Определение 4.18.**
Rank-2 puncture называется переход от полного coordinate carrier-а $Q_2$ к подмножеству $Q_2^\circ$, полученному исключением total poles:

$$
Q_2 \rightsquigarrow Q_2^\circ = Q_2\setminus\lbrace 00,11\rbrace.
$$

Puncture здесь означает переход от полного координатного carrier-а к выделенному подмножеству.

Полный carrier $Q_2$ сохраняет total poles

$$
00,\qquad 11,
$$

а $Q_2^\circ$ фиксирует active mixed-остаток ранга $2$.

После выбора relation на $Q_2^\circ$ соответствующая пара становится relational subcarrier.

## §4.14. Центральный шов

**Определение 4.19.**
Центральным швом ранга $2$ называется подноситель

$$
A_2 = (\lbrace 01,10\rbrace,H_2^{(2)}|_{\lbrace 01,10\rbrace}).
$$

В графовой записи:

$$
01\leftrightarrow 10.
$$

То есть

$$
A_2
$$

есть punctured coordinate subset $Q_2^\circ$, оснащённый complement-отношением.

**Утверждение 4.20.**
Центральный шов $A_2$ имеет тип $K_2$.

**Проверка.**
Под $K_2$ понимается полный граф на двух вершинах.

Carrier шва:

$$
\lbrace 01,10\rbrace
$$

содержит две вершины. Между ними есть единственное неориентированное ребро:

$$
01\leftrightarrow 10.
$$

Следовательно,

$$
A_2\cong K_2.
$$

В rank $2$ puncture задаёт двухточечную ось. В rank $3$ puncture total poles в $Q_3$ задаёт шеститочечный mixed carrier.


## §4.15. Полное graph-reading $K_4$

**Определение 4.21.**
Полное relation-reading на $Q_2$ задаётся отношением

$$
R_{K_4}^{(2)} = \lbrace (x,y)\in Q_2^2:x\neq y\rbrace.
$$

Соответствующая presentation:

$$
\Pi_2^{K_4} = (Q_2,R_{K_4}^{(2)},\mathrm{id}_{Q_2},\mathrm{rec}_{\mathrm{id}}).
$$

**Утверждение 4.22.**

$$
(Q_2,R_{K_4}^{(2)})\cong K_4.
$$

**Проверка.**
В $R_{K_4}^{(2)}$ каждая вершина $Q_2$ связана с каждой другой вершиной:

$$
x\neq y
\quad\Longrightarrow\quad
(x,y)\in R_{K_4}^{(2)}.
$$
У carrier-а $Q_2$ четыре состояния. Полный граф на четырёх вершинах есть $K_4$. Следовательно,
$$
(Q_2,R_{K_4}^{(2)})\cong K_4.
$$

<p align="center">
  <a href="../assets/figures/1.5-K_4.png">
    <img src="../assets/figures/1.5-K_4.png" width="500" alt="Полное graph-reading $K_4$ на $Q_2$">
  </a>
</p>


## §4.16. Симплексные секторы

Фиксируются два трёхточечных carrier-подмножества, которые содержат центральный шов и ровно один total pole. Их relation-структура задаётся partial closure $R_{K_4-e}^{(2)}$.

**Определение 4.23.**
Нижний сектор:

$$
\Delta_{\wedge} = \lbrace 00,01,10\rbrace.
$$

Верхний сектор:

$$
\Delta_{\vee} = \lbrace 11,01,10\rbrace.
$$

Их пересечение:

$$
\Delta_{\wedge}\cap\Delta_{\vee} = \lbrace 01,10\rbrace.
$$

Следовательно, оба сектора имеют общий центральный шов

$$
A_2=\lbrace 01,10\rbrace.
$$

**Утверждение 4.24.**
Среди трёхточечных подмножеств $Q_2$ ровно два содержат центральный шов $A_2$.

Это

$$
\Delta_{\wedge} = A_2\cup\lbrace 00\rbrace,
$$

$$
\Delta_{\vee} = A_2\cup\lbrace 11\rbrace.
$$

**Проверка.**
Трёхточечное подмножество, содержащее

$$
A_2=\lbrace 01,10\rbrace,
$$

должно иметь вид

$$
A_2\cup\lbrace z\rbrace,
$$

где

$$
z\in Q_2\setminus A_2.
$$

Но

$$
Q_2\setminus A_2=\lbrace 00,11\rbrace.
$$

Поэтому возможны ровно два выбора:

$$
z=00
$$

или

$$
z=11.
$$

Они дают $\Delta_{\wedge}$ и $\Delta_{\vee}$.

Каждый из этих двух секторов содержит ровно один total pole; carrier шва $A_2$ состоит из $01$ и $10$.


## §4.17. Partial closure $K_4-e$

**Определение 4.25.**
Отношение

$$
R_{K_4-e}^{(2)}
$$

задаётся удалением total-pole diagonal из полного relation-reading-а $K_4$:

$$
R_{K_4-e}^{(2)} = R_{K_4}^{(2)} \setminus \lbrace (00,11),(11,00)\rbrace.
$$

Соответствующая presentation:

$$
\Pi_2^{K_4-e} = (Q_2,R_{K_4-e}^{(2)},\mathrm{id}_{Q_2},\mathrm{rec}_{\mathrm{id}}).
$$

**Утверждение 4.26.**

$$
(Q_2,R_{K_4-e}^{(2)})\cong K_4-e.
$$

**Проверка.**
Граф $K_4$ имеет шесть неориентированных рёбер между четырьмя вершинами.

Из него удаляется одно неориентированное ребро:

$$
00\leftrightarrow 11.
$$

Остаются пять рёбер:

$$
00\leftrightarrow 01,
$$

$$
00\leftrightarrow 10,
$$

$$
11\leftrightarrow 01,
$$

$$
11\leftrightarrow 10,
$$

$$
01\leftrightarrow 10.
$$

Это полный граф на четырёх вершинах без одного ребра. Следовательно,

$$
(Q_2,R_{K_4-e}^{(2)})\cong K_4-e.
$$

**Следствие 4.27.**
В graph-reading-е $K_4-e$ carrier $Q_2$ читается как две треугольные сцены, склеенные по центральному шву.

**Проверка.**
Удалённое ребро в $R_{K_4-e}^{(2)}$ только одно:

$$
00\leftrightarrow 11.
$$

Нижний сектор

$$
\Delta_{\wedge}=\lbrace 00,01,10\rbrace.
$$

Пара $\lbrace 00,11\rbrace$ отсутствует в $\Delta_{\wedge}$. Все три пары его вершин остаются связанными:

$$
00\leftrightarrow 01,
$$

$$
00\leftrightarrow 10,
$$

$$
01\leftrightarrow 10.
$$

Значит, $\Delta_{\wedge}$ является треугольником.

Верхний сектор

$$
\Delta_{\vee}=\lbrace 11,01,10\rbrace.
$$

Пара $\lbrace 00,11\rbrace$ отсутствует в $\Delta_{\vee}$. Все три пары его вершин остаются связанными:

$$
11\leftrightarrow 01,
$$

$$
11\leftrightarrow 10,
$$

$$
01\leftrightarrow 10.
$$

Значит, $\Delta_{\vee}$ является треугольником.

Общее ребро двух треугольников:

$$
01\leftrightarrow 10.
$$

Это центральный шов $A_2$.

Relation на симплексных секторах берётся индуцированным из partial closure:

$$
R_{\Delta_{\wedge}} = R_{K_4-e}^{(2)} \cap (\Delta_{\wedge}\times\Delta_{\wedge}),
$$

$$
R_{\Delta_{\vee}} = R_{K_4-e}^{(2)} \cap (\Delta_{\vee}\times\Delta_{\vee}).
$$

Тем самым симплексные секторы как relation-carriers имеют вид

$$
(\Delta_{\wedge},R_{\Delta_{\wedge}}),
\qquad
(\Delta_{\vee},R_{\Delta_{\vee}}).
$$

<p align="center">
  <a href="../assets/figures/1.6-K_4-e.png">
    <img src="../assets/figures/1.6-K_4-e.png" width="500" alt="Partial closure $K_4-e$ на $Q_2$">
  </a>
</p>


## §4.18. Relation-readings ранга 2

На одном carrier-е

$$
Q_2=\lbrace 00,01,10,11\rbrace
$$

получены разные relation-readings:

$$
C_4,
$$

$$
2K_2,
$$

$$
K_4,
$$

$$
K_4-e.
$$

Они имеют один carrier, но разные отношения.

$$
C_4
$$

читает $Q_2$ через изменение одной координаты.

$$
2K_2
$$

читает $Q_2$ через complement-пары.

$$
K_4
$$

читает $Q_2$ как полную связность четырёх состояний.

$$
K_4-e
$$

читает $Q_2$ как две треугольные сцены, склеенные по центральному шву.

Эти чтения являются разными relation-presentations одного carrier-а.

## §4.19. Closure package rank $2$

Rank-2 comparison package фиксирует все relation-presentations, построенные на $Q_2$:

$$
\mathfrak C_2 = \left( Q_2, \Pi_2^{C_4}, \Pi_2^{2K_2}, \Pi_2^\chi, \Pi_2^{K_4}, \Pi_2^{K_4-e}, A_2 \right).
$$

Здесь $A_2=\lbrace 01,10\rbrace$ — центральный шов §4.14.

$\mathfrak C_2$ имеет статус structure/package. В смысле §0.5 presentation имеет форму $(X,R,q,\mathrm{rec})$; $\mathfrak C_2$ даёт closure-name rank-2 comparison layer-а для пяти уже построенных presentations.


# §5. Ранг 3: admissible carrier

## §5.1. Трёхбитный carrier

**Определение 5.1.**
Трёхбитный carrier есть

$$
Q_3=\mathbb{F}_2^3.
$$

В развёрнутой записи:

$$
Q_3=
\lbrace 000,001,010,011,100,101,110,111\rbrace.
$$

<p align="center">
  <a href="../assets/figures/2.1-Q_3.png">
    <img src="../assets/figures/2.1-Q_3.png" width="500" alt="Трёхбитный carrier $Q_3$">
  </a>
</p>

Запись

$$
b_3b_2b_1
$$

означает кортеж

$$
(x_3,x_2,x_1)=(b_3,b_2,b_1).
$$

Запись согласована с §3.6 для rank-lift-а: новый разряд $x_3$ занимает старшую позицию слева, координаты $x_2,x_1$ наследуются от $Q_2$.


## §5.2. Emergence-разложение ранга 3

По Утверждению 3.4 (§3.7) для rank-lift при $n=3$:

$$
Q_3^* = Q_2^* \sqcup \lbrace e_3\rbrace \sqcup (e_3+Q_2^*).
$$

Здесь

$$
e_3=100.
$$

Так как

$$
Q_2^*=\lbrace 01,10,11\rbrace,
$$

в трёхбитной записи получаем:

$$
Q_3^* = \lbrace 001,010,011\rbrace \sqcup \lbrace 100\rbrace \sqcup \lbrace 101,110,111\rbrace.
$$

Первый блок — старый проявленный слой:

$$
\lbrace 001,010,011\rbrace.
$$

Второй блок — новый разряд:

$$
\lbrace 100\rbrace.
$$

Третий блок — старый слой с новой координатной нагрузкой:

$$
\lbrace 101,110,111\rbrace.
$$

Это emergence-order. Он показывает порядок появления координатных ролей; shell-role состояний задаётся после сборки carrier-а.


## §5.3. Total poles в $Q_3$

По Определению 4.16 (§4.13) total pole в $Q_n$ — состояние, в котором все $n$ координат совпадают.

В $Q_3$ таких состояний два:

$$
0^3=000,
$$

$$
1^3=111.
$$

Они называются total poles ранга $3$.

Состояние

$$
000
$$

является нижним total pole.

Состояние

$$
111
$$

является верхним total pole.

Оба состояния однородны: в них нет mixed-распределения координат.


## §5.4. Mixed-состояния

На ранге $2$ mixed-состояния формально составляли punctured carrier $Q_2^\circ = \lbrace 01, 10\rbrace$. На ранге $3$ это множество перестаёт быть простой двухточечной осью.

**Определение 5.2.**
Состояние

$$
x\in Q_n
$$

называется mixed-состоянием, если оно лежит вне total-pole pair.

Множество mixed-состояний ранга $3$:

$$
Q_3\setminus\lbrace 000,111\rbrace.
$$

В развёрнутой записи:

$$
\lbrace 001,010,011,100,101,110\rbrace.
$$



## §5.5. Admissible carrier

В §4.13 puncture был введён как переход от полного coordinate carrier-а к подмножеству, полученному исключением total poles. Теперь фиксируется общий вид этого перехода.

**Определение 5.3.**
Punctured coordinate subset ранга $n$ есть подмножество

$$
Q_n^\circ = Q_n\setminus\lbrace 0^n,1^n\rbrace.
$$

Rank-$n$ puncture называется переход

$$
Q_n \rightsquigarrow Q_n^\circ
$$

от полного coordinate carrier-а к подмножеству, полученному исключением двух total poles.

Полный carrier $Q_n$ сохраняется как coordinate carrier ранга $n$. Подмножество $Q_n^\circ$ фиксирует active mixed-остаток данного ранга.

После выбора relation $R$ на $Q_n^\circ$ пара

$$
(Q_n^\circ,R)
$$

становится relational carrier-ом. До выбора relation $Q_n^\circ$ является только выделенным координатным подмножеством.

**Определение 5.4.**
Admissible carrier ранга $3$ есть punctured coordinate subset ранга $3$:

$$
X_{\mathrm{adm}} = Q_3^\circ = Q_3\setminus\lbrace 000,111\rbrace.
$$

То есть

$$
X_{\mathrm{adm}} = \lbrace 001,010,011,100,101,110\rbrace.
$$

<p align="center">
  <a href="../assets/figures/2.2-X_adm.png">
    <img src="../assets/figures/2.2-X_adm.png" width="500" alt="Admissible carrier $X_{\mathrm{adm}}$">
  </a>
</p>

В §5 $X_{\mathrm{adm}}$ вводится как carrier-множество.

Полный carrier

$$
Q_3
$$

остаётся полным coordinate carrier-ом ранга $3$. Подмножество $X_{\mathrm{adm}}$ является его active mixed-остатком.

## §5.6. Shell-разложение $X_{\mathrm{adm}}$

По Определению 3.5 (§3.9) shell ранга $n$ задаётся как $S_k^{(n)}=\lbrace x\in Q_n:\ |x|=k\rbrace$. Для $n=3$:

$$
S_k^{(3)}=\lbrace x\in Q_3:|x|=k\rbrace.
$$

Полное shell-разложение $Q_3$:

$$
S_0^{(3)}=\lbrace 000\rbrace,
$$

$$
S_1^{(3)}=\lbrace 001,010,100\rbrace,
$$

$$
S_2^{(3)}=\lbrace 011,101,110\rbrace,
$$

$$
S_3^{(3)}=\lbrace 111\rbrace.
$$

Total poles — это крайние shell-и:

$$
S_0^{(3)}=\lbrace 000\rbrace,
\qquad
S_3^{(3)}=\lbrace 111\rbrace.
$$
После puncture остаются средние shell-и:
$$
X_{\mathrm{adm}} = S_1^{(3)} \sqcup S_2^{(3)}.
$$
То есть
$$
X_{\mathrm{adm}} = \lbrace 001,010,100\rbrace \sqcup \lbrace 011,101,110\rbrace.
$$



## §5.7. Rank 2 puncture и rank 3 puncture

Rank-2 puncture:

$$
Q_2\setminus\lbrace 00,11\rbrace = \lbrace 01,10\rbrace.
$$

Остаток имеет два состояния и возвращает carrier типа $K_2$.

Rank-3 puncture:

$$
Q_3\setminus\lbrace 000,111\rbrace = \lbrace 001,010,011,100,101,110\rbrace.
$$

**Утверждение 5.5.**
Мощность admissible carrier-а ранга $3$ равна $6$:

$$
|X_{\mathrm{adm}}| = 2^3 - 2 = 6.
$$

На ранге $2$ мощность punctured coordinate subset равна $2$.

**Проверка.**
Для rank $2$:

$$
2^2-2=2.
$$

После удаления total poles остаются два состояния.

Для rank $3$:

$$
2^3-2=6.
$$

После удаления total poles остаются шесть состояний.

**Замечание.**
В отличие от ранга $2$, где после puncture остаётся двухточечное подмножество, ранг $3$ впервые даёт шеститочечный mixed-carrier:

$$
X_{\mathrm{adm}} = Q_3\setminus\lbrace 000,111\rbrace.
$$

В §5 фиксируется carrier-слой.

## §5.8. Complement на $X_{\mathrm{adm}}$

На $Q_3$ есть побитовый complement:

$$
\overline{x}=x+111.
$$

Он переводит total poles друг в друга:

$$
000\leftrightarrow 111.
$$

Он также сохраняет admissible carrier:

$$
x\in X_{\mathrm{adm}}
\quad\Longrightarrow\quad
\overline{x}\in X_{\mathrm{adm}}.
$$

**Утверждение 5.6.**
Complement переводит shell $S_1^{(3)}$ в shell $S_2^{(3)}$, и обратно:

$$
\overline{S_1^{(3)}}=S_2^{(3)},
$$

$$
\overline{S_2^{(3)}}=S_1^{(3)}.
$$

**Проверка.**
В общем случае complement в $Q_n$ меняет вес $x$ на $n - |x|$. Для $n = 3$ это означает, что если

$$
|x|=1,
$$

то $|\overline{x}| = 3 - 1 = 2$. Если

$$
|x|=2,
$$

то $|\overline{x}| = 3 - 2 = 1$. Следовательно,

$$
S_1^{(3)}\leftrightarrow S_2^{(3)}.
$$

В развёрнутой записи:

$$
001\leftrightarrow 110,
$$

$$
010\leftrightarrow 101,
$$

$$
100\leftrightarrow 011.
$$

<p align="center">
  <a href="../assets/figures/3.3-R_3-3K_2.png">
    <img src="../assets/figures/3.3-R_3-3K_2.png" width="500" alt="Complement-пары на $X_{\mathrm{adm}}$">
  </a>
</p>

На этом уровне complement является инволюцией ($x \mapsto \overline{x} \mapsto x$), продолжая complement-переход, введённый в §4.



# §6. Relation-грамматика admissible carrier-а

## §6.1. Carrier §6

В §6 используется carrier, построенный в §5:

$$
X_{\mathrm{adm}} = Q_3\setminus\lbrace 000,111\rbrace = S_1^{(3)}\sqcup S_2^{(3)}.
$$

Carrier §6 равен $X_{\mathrm{adm}}$. Новый слой задаёт отношения между уже построенными admissible-состояниями.


## §6.2. Hamming-distance на $X_{\mathrm{adm}}$

По аналогии с Определением 4.6 (§4.7), Hamming-distance на $Q_n$ задаётся формулой

$$
d_H(x,y)=|x+y|,
$$

где сложение берётся в $\mathbb{F}_2^n$, а $|x+y|$ означает Hamming-вес. В §6 используется случай $n=3$.

Для различных

$$
x,y\in X_{\mathrm{adm}}
$$

возможны ровно три значения:

$$
d_H(x,y)=1,
\qquad
d_H(x,y)=2,
\qquad
d_H(x,y)=3.
$$

**Определение 6.1.**
Для

$$
k\in\lbrace 1,2,3\rbrace
$$

отношение $R_k$ на $X_{\mathrm{adm}}$ задаётся формулой

$$
R_k = \lbrace (x,y)\in X_{\mathrm{adm}}\times X_{\mathrm{adm}}: x\neq y,\ d_H(x,y)=k\rbrace.
$$

Каждое $R_k$ симметрично и иррефлексивно.


## §6.3. Presentation для Hamming graph-readings

Для каждого

$$
k\in\lbrace 1,2,3\rbrace
$$

рассматривается identity graph-reading

$$
\Pi_{3,k} = \bigl( X_{\mathrm{adm}}, R_k, \mathrm{id}_{X_{\mathrm{adm}}}, \mathrm{rec}_{\mathrm{id}} \bigr).
$$

По §4.3, для identity graph-reading-а с иррефлексивным отношением $R$ recovery datum имеет вид

$$
\mathrm{rec}_{\mathrm{id}}(x) = (\lbrace x\rbrace,\varnothing).
$$

Поскольку $R_k$ иррефлексивно, эта формула применима к каждому $\Pi_{3,k}$. Поэтому все

$$
\Pi_{3,1},
\qquad
\Pi_{3,2},
\qquad
\Pi_{3,3}
$$

являются exact identity graph-readings.


## §6.4. Relation $R_1$: одношаговое Hamming-отношение

Отношение $R_1$ связывает состояния, различающиеся ровно одной координатой:

$$
(x,y)\in R_1
\quad\Longleftrightarrow\quad
d_H(x,y)=1.
$$
Неориентированные рёбра $R_1$:
$$
001\leftrightarrow 011,
$$

$$
011\leftrightarrow 010,
$$

$$
010\leftrightarrow 110,
$$

$$
110\leftrightarrow 100,
$$

$$
100\leftrightarrow 101,
$$

$$
101\leftrightarrow 001.
$$

Эти рёбра образуют шестичленный цикл:

$$
001 \leftrightarrow 011 \leftrightarrow 010 \leftrightarrow 110 \leftrightarrow 100 \leftrightarrow 101 \leftrightarrow 001.
$$

**Утверждение 6.2.**

$$
(X_{\mathrm{adm}},R_1)\cong C_6.
$$

**Проверка.**
Выписанная последовательность проходит через все шесть вершин $X_{\mathrm{adm}}$ и возвращается в начальную вершину. Каждая вершина имеет ровно две $R_1$-смежные вершины. Поэтому graph-reading $(X_{\mathrm{adm}},R_1)$ является связным $2$-регулярным графом на шести вершинах. Следовательно,

$$
(X_{\mathrm{adm}},R_1)\cong C_6.
$$

<p align="center">
  <a href="../assets/figures/3.1-R_1-C_6.png">
    <img src="../assets/figures/3.1-R_1-C_6.png" width="500" alt="Graph-reading $R_1\cong C_6$ на $X_{\mathrm{adm}}$">
  </a>
</p>

**Замечание.**
В полном $Q_3$ каждая вершина имеет три одношаговых Hamming-соседа. При переходе к $X_{\mathrm{adm}}$ вершины из $S_1^{(3)}$ теряют соседство с $000$, а вершины из $S_2^{(3)}$ теряют соседство с $111$. Оставшаяся одношаговая смежность даёт $C_6$.

В §6 $C_6$ является только graph-reading-ом на $X_{\mathrm{adm}}$. Orientation и transport на этом цикле не вводятся.


## §6.5. Relation $R_2$: двухшаговое Hamming-отношение

Отношение $R_2$ связывает состояния, различающиеся ровно двумя координатами:

$$
(x,y)\in R_2
\quad\Longleftrightarrow\quad
d_H(x,y)=2.
$$
**Утверждение 6.3.**
$$
(X_{\mathrm{adm}},R_2) \cong K_3\sqcup K_3.
$$

**Проверка.**
Пусть

$$
x,y\in S_1^{(3)},
\qquad
x\neq y.
$$
Оба состояния имеют вес $1$, и их единицы стоят в разных координатах. Поэтому $x+y$ имеет вес $2$, то есть
$$
d_H(x,y)=2.
$$

Значит, все различные пары внутри $S_1^{(3)}$ связаны отношением $R_2$, и $S_1^{(3)}$ даёт компоненту $K_3$.

Теперь пусть

$$
x,y\in S_2^{(3)},
\qquad
x\neq y.
$$
Оба состояния имеют вес $2$, и их нули стоят в разных координатах. При сложении $x+y$ остаются ровно две единицы. Поэтому
$$
d_H(x,y)=2.
$$

Значит, $S_2^{(3)}$ даёт вторую компоненту $K_3$.

Если

$$
x\in S_1^{(3)},
\qquad
y\in S_2^{(3)},
$$
то возможны только значения
$$
d_H(x,y)=1
$$
или
$$
d_H(x,y)=3.
$$
Значение $2$ между shell-ами не возникает. Следовательно,
$$
(X_{\mathrm{adm}},R_2) \cong K_3\sqcup K_3.
$$
Каждый $K_3$ содержит $3$ ребра, поэтому
$$
|E(R_2)|=6.
$$

<p align="center">
  <a href="../assets/figures/3.2-R_2-2_triangles.png">
    <img src="../assets/figures/3.2-R_2-2_triangles.png" width="500" alt="Graph-reading $R_2\cong K_3\sqcup K_3$ на $X_{\mathrm{adm}}$">
  </a>
</p>


## §6.6. Relation $R_3$: complement-отношение

Отношение $R_3$ связывает состояния, различающиеся во всех трёх координатах:

$$
(x,y)\in R_3
\quad\Longleftrightarrow\quad
d_H(x,y)=3.
$$
Для трёхбитных состояний это равносильно
$$
y=x+111.
$$
По Утверждению 5.6 (§5.8), complement-инволюция переводит
$$
S_1^{(3)} \leftrightarrow S_2^{(3)}.
$$
Она разбивает $X_{\mathrm{adm}}$ на три complement-пары:
$$
001\leftrightarrow110,
$$

$$
010\leftrightarrow101,
$$

$$
100\leftrightarrow011.
$$

**Утверждение 6.4.**

$$
(X_{\mathrm{adm}},R_3)\cong 3K_2.
$$

**Проверка.**
Для каждого

$$
x\in X_{\mathrm{adm}}
$$

состояние

$$
x+111
$$

также принадлежит $X_{\mathrm{adm}}$, и

$$
d_H(x,x+111)=3.
$$

Так как

$$
(x+111)+111=x,
$$

complement является инволюцией. Поэтому $X_{\mathrm{adm}}$ разбивается на три непересекающиеся пары:

$$
\lbrace 001,110\rbrace,
\qquad
\lbrace 010,101\rbrace,
\qquad
\lbrace 100,011\rbrace.
$$
Каждая пара имеет тип $K_2$, а между разными complement-парами relation $R_3$ рёбер не задаёт. Следовательно,
$$
(X_{\mathrm{adm}},R_3)\cong 3K_2.
$$

<p align="center">
  <a href="../assets/figures/3.3-R_3-3K_2.png">
    <img src="../assets/figures/3.3-R_3-3K_2.png" width="500" alt="Graph-reading $R_3\cong 3K_2$ на $X_{\mathrm{adm}}$">
  </a>
</p>

**Замечание.**
$R_1$ и $R_3$ используют один и тот же carrier $X_{\mathrm{adm}}$, но задают разные relation-readings. $R_1$ связывает одношаговых Hamming-соседей, а $R_3$ связывает complement-пары.


## §6.7. Relation-грамматика как разбиение пар

**Утверждение 6.5.**
Hamming-отношения

$$
R_1,\quad R_2,\quad R_3
$$

разбивают множество всех неориентированных пар различных состояний $X_{\mathrm{adm}}$.

**Проверка.**
Для любых различных

$$
x,y\in X_{\mathrm{adm}}\subset Q_3
$$

расстояние $d_H(x,y)$ принимает одно из значений

$$
1,\quad 2,\quad 3.
$$

Других положительных Hamming-distance в $Q_3$ нет.

Пара $\lbrace x,y\rbrace$ принадлежит ровно одному relation $R_k$, поскольку значение $d_H(x,y)$ единственно. Значит, отношения $R_1, R_2, R_3$ попарно не пересекаются и вместе покрывают все пары различных состояний.

Контрольный подсчёт:

$$
\binom{|X_{\mathrm{adm}}|}{2} = \binom{6}{2} = 15.
$$

Из Утверждений 6.2–6.4:

$$
|E(R_1)|=6,
$$

$$
|E(R_2)|=6,
$$

$$
|E(R_3)|=3.
$$

Итого:

$$
6+6+3=15.
$$

Следовательно,

$$
\mathcal R_{\mathrm{adm}}^{(3)} = \lbrace R_1, R_2, R_3\rbrace
$$

является полной static Hamming relation-грамматикой $X_{\mathrm{adm}}$.


## §6.8. Emergence-order, shell-order и relation-order

В §5 emergence-order описывал, как $Q_3^*$ возникает из rank-lift-а

$$
Q_2\to Q_3.
$$

В §5 shell-order описывал роль состояний внутри уже собранного $Q_3$:

$$
S_1^{(3)},
\qquad
S_2^{(3)}.
$$
В §6 используется relation-order, задаваемый Hamming-distance:
$$
d_H=1,
\qquad
d_H=2,
\qquad
d_H=3.
$$
Relation $R_1$ чередует shell-и и даёт
$$
C_6.
$$
Relation $R_2$ читает каждый shell отдельно и даёт
$$
K_3\sqcup K_3.
$$
Relation $R_3$ связывает shell-и complement-парами и даёт
$$
3K_2.
$$

Emergence-order ранга $3$ остаётся фиксированным. §6 строит relation-readings на уже собранном carrier-е.


# §7. Октаэдральный relation-carrier

## §7.1. Complement-пары как блоки несмежности

По §6 relation $R_3$ задаёт три complement-пары:

$$
001\leftrightarrow110,
$$

$$
010\leftrightarrow101,
$$

$$
100\leftrightarrow011.
$$

Для различения с emergence-блоками $B_n$ из §3.6 обозначим эти пары через

$$
\beta_1,\quad \beta_2,\quad \beta_3.
$$

**Определение 7.1.**
Complement-pair partition carrier-а $X_{\mathrm{adm}}$ есть разбиение

$$
X_{\mathrm{adm}} = \beta_1\sqcup\beta_2\sqcup\beta_3,
$$

где

$$
\beta_1=\lbrace 001,110\rbrace,
$$

$$
\beta_2=\lbrace 010,101\rbrace,
$$

$$
\beta_3=\lbrace 100,011\rbrace.
$$

Каждая $\beta_i$ является одной компонентой graph-reading-а

$$
(X_{\mathrm{adm}},R_3)\cong 3K_2.
$$

В §7 эти пары задают доли complete tripartite graph-reading-а. В relation $R_{12}$ внутри каждой $\beta_i$ рёбра отсутствуют; между разными $\beta_i$ рёбра присутствуют.


## §7.2. Union-relation $R_{12}$

**Определение 7.2.**
На $X_{\mathrm{adm}}$ задаётся relation

$$
R_{12} = R_1\cup R_2.
$$

То есть для

$$
x,y\in X_{\mathrm{adm}},
\qquad
x\neq y,
$$
имеем
$$
(x,y)\in R_{12}
$$
тогда и только тогда, когда
$$
d_H(x,y)=1
$$
или
$$
d_H(x,y)=2.
$$

По Утверждению 6.5, отношения $R_1, R_2, R_3$ разбивают все пары различных состояний $X_{\mathrm{adm}}$. Поэтому $R_{12}$ можно читать как остаток относительно complement-отношения $R_3$: оно содержит ровно те пары, которые не являются complement-парами.

Эквивалентно, поскольку для $x\neq y$ в $Q_3$

$$
d_H(x,y)\in\lbrace 1,2,3\rbrace,
$$

а условие

$$
d_H(x,y)=3
$$

равносильно

$$
y=x+111,
$$

имеем:

$$
(x,y)\in R_{12}
\quad\Longleftrightarrow\quad
x\neq y \land y\neq x+111.
$$

Иными словами, $R_{12}$ соединяет все различные admissible-состояния, кроме complement-состояния данного $x$.


## §7.3. Presentation для $R_{12}$

На relation

$$
R_{12}
$$

задаётся identity graph-reading

$$
\Pi_{12} = \bigl( X_{\mathrm{adm}}, R_{12}, \mathrm{id}_{X_{\mathrm{adm}}}, \mathrm{rec}_{\mathrm{id}} \bigr).
$$

Отношения $R_1$ и $R_2$ симметричны и иррефлексивны. Поэтому их объединение

$$
R_{12}=R_1\cup R_2
$$

также симметрично и иррефлексивно.

По §4.3, для identity graph-reading-а с иррефлексивным отношением $R$ recovery datum имеет вид

$$
\mathrm{rec}_{\mathrm{id}}(x) = (\lbrace x\rbrace,\varnothing).
$$

Поскольку $R_{12}$ иррефлексивно, эта формула применима к $\Pi_{12}$. Поэтому $\Pi_{12}$ является exact identity graph-reading-ом.

Структурный объект §7 — presentation $\Pi_{12}$. Граф $K_{2,2,2}$ и октаэдральный $1$-скелет являются graph-readings этой presentation.

## §7.4. Граф $K_{2,2,2}$

Перед формулировкой утверждения зафиксируем целевой graph-reading.

**Определение 7.3.**
Граф

$$
K_{2,2,2}
$$

есть complete tripartite graph с тремя долями мощности $2$. Это означает, что множество вершин разложено как

$$
V = V_1\sqcup V_2\sqcup V_3, \qquad |V_1|=|V_2|=|V_3|=2,
$$

при этом внутри каждой $V_i$ рёбер нет, а любые две вершины из разных долей соединены ребром.


## §7.5. Проверка $R_{12}\cong K_{2,2,2}$

**Утверждение 7.4.**

$$
(X_{\mathrm{adm}},R_{12}) \cong K_{2,2,2}.
$$

**Проверка.**
Покажем, что complement-pair partition

$$
\beta_1,\beta_2,\beta_3
$$

играет роль долей

$$
V_1,V_2,V_3
$$

из Определения 7.3.

Используем разбиение

$$
X_{\mathrm{adm}} = \beta_1\sqcup\beta_2\sqcup\beta_3,
$$

где

$$
\beta_1=\lbrace 001,110\rbrace,
$$

$$
\beta_2=\lbrace 010,101\rbrace,
$$

$$
\beta_3=\lbrace 100,011\rbrace.
$$

Внутри каждой $\beta_i$ находится ровно одна пара состояний. Эта пара является complement-парой, поэтому её Hamming-distance равен $3$. Следовательно, она принадлежит $R_3$, но не принадлежит

$$
R_{12}=R_1\cup R_2.
$$

Значит, внутри каждой доли $\beta_i$ рёбер $R_{12}$ нет.

Теперь возьмём

$$
x\in \beta_i,
\qquad
y\in \beta_j,
\qquad
i\neq j.
$$
Тогда $y$ находится вне complement-пары $x$. Поэтому
$$
d_H(x,y)\neq 3.
$$
Так как
$$
x\neq y
$$
и оба состояния лежат в $Q_3$, остаются только два возможных значения:
$$
d_H(x,y)=1
$$
или
$$
d_H(x,y)=2.
$$
По определению $R_{12}$ это даёт
$$
(x,y)\in R_{12}.
$$
Следовательно, вершины из разных $\beta_i$ соединены всеми возможными рёбрами, а внутри одной $\beta_i$ рёбер нет. Это ровно структура
$$
K_{2,2,2}.
$$

**Контрольный подсчёт.**
Из §6:

$$
|E(R_1)|=6,
\qquad
|E(R_2)|=6.
$$
По Утверждению 6.5 отношения $R_1$ и $R_2$ не пересекаются. Поэтому
$$
|E(R_{12})| = |E(R_1)|+|E(R_2)| = 6+6 = 12.
$$
С другой стороны, в $K_{2,2,2}$ есть три пары долей, а между каждой парой долей проходит
$$
2\cdot2=4
$$
ребра. Поэтому
$$
|E(K_{2,2,2})| = 3\cdot4 = 12.
$$

Подсчёт согласуется со структурной проверкой.

<p align="center">
  <a href="../assets/figures/4.1-R_12-octahedron.png">
    <img src="../assets/figures/4.1-R_12-octahedron.png" width="500" alt="Union-relation $R_1\cup R_2$ как $K_{2,2,2}$">
  </a>
</p>


## §7.6. $K_{2,2,2}$ как $1$-скелет октаэдра

**Определение 7.5.**
Пусть

$$
O_3^{(1)}
$$

обозначает graph $1$-скелета стандартного октаэдра.

Его вершины можно записать как

$$
\lbrace +e_1,-e_1,+e_2,-e_2,+e_3,-e_3\rbrace.
$$

Две различные вершины соединены ребром тогда и только тогда, когда они не являются противоположными:

$$
u\sim v
\quad\Longleftrightarrow\quad
u\neq v \land u\neq -v.
$$
Противоположные пары:
$$
E_1=\lbrace +e_1,-e_1\rbrace,
$$

$$
E_2=\lbrace +e_2,-e_2\rbrace,
$$

$$
E_3=\lbrace +e_3,-e_3\rbrace.
$$

**Утверждение 7.6.**

$$
K_{2,2,2} \cong O_3^{(1)}.
$$

**Проверка.**
Разложим вершины $O_3^{(1)}$ на три противоположные пары:

$$
E_1=\lbrace +e_1,-e_1\rbrace,
$$

$$
E_2=\lbrace +e_2,-e_2\rbrace,
$$

$$
E_3=\lbrace +e_3,-e_3\rbrace.
$$

Внутри каждой пары $E_i$ вершины противоположны, поэтому ребра между ними нет.

Если две вершины лежат в разных парах $E_i$ и $E_j$, то они не противоположны. По определению $O_3^{(1)}$ между ними есть ребро.

Следовательно, $O_3^{(1)}$ является complete tripartite graph с тремя долями мощности $2$:

$$
O_3^{(1)} \cong K_{2,2,2}.
$$

**Следствие 7.7.**

$$
(X_{\mathrm{adm}},R_{12}) \cong O_3^{(1)}.
$$

**Проверка.**
По Утверждению 7.4:

$$
(X_{\mathrm{adm}},R_{12}) \cong K_{2,2,2}.
$$

По Утверждению 7.6:

$$
K_{2,2,2} \cong O_3^{(1)}.
$$

Транзитивность изоморфизма даёт

$$
(X_{\mathrm{adm}},R_{12}) \cong O_3^{(1)}.
$$


## §7.7. Octahedral graph-reading на $X_{\mathrm{adm}}$

**Определение 7.8.**
Octahedral graph-reading package на $X_{\mathrm{adm}}$ есть structure

$$
\mathcal O_{12} = \bigl( \Pi_{12}, [(X_{\mathrm{adm}},R_{12})\cong O_3^{(1)}] \bigr)
$$

где $\Pi_{12}$ — presentation из §7.3, а второй компонент означает изоморфный тип

$$
(X_{\mathrm{adm}},R_{12}) \cong O_3^{(1)}
$$

из Следствия 7.7.

$\mathcal O_{12}$ имеет статус package. Его presentation-компонента задаётся $\Pi_{12}^{O}$.

Конкретный рисунок октаэдра получается только после выбора изоморфизма

$$
\varphi:(X_{\mathrm{adm}},R_{12})\to O_3^{(1)}.
$$

Сам octahedral graph-reading не зависит от одного выбранного рисунка.

**Замечание.**
Изоморфизм графов сохраняет несмежность. Не-рёбра graph-reading-а

$$
(X_{\mathrm{adm}},R_{12})
$$

— это ровно complement-пары

$$
\beta_1,\quad \beta_2,\quad \beta_3.
$$

Не-рёбра $O_3^{(1)}$ — это ровно противоположные пары

$$
E_1,\quad E_2,\quad E_3.
$$

Поэтому любой изоморфизм

$$
\varphi:(X_{\mathrm{adm}},R_{12})\to O_3^{(1)}
$$

индуцирует биекцию

$$
\lbrace \beta_1,\beta_2,\beta_3\rbrace \to \lbrace E_1,E_2,E_3\rbrace.
$$

Один допустимый выбор изоморфизма:

$$
001\mapsto +e_1,
\qquad
110\mapsto -e_1,
$$

$$
010\mapsto +e_2,
\qquad
101\mapsto -e_2,
$$

$$
100\mapsto +e_3,
\qquad
011\mapsto -e_3.
$$
При этом
$$
\beta_1=\lbrace 001,110\rbrace
$$
переходит в
$$
E_1=\lbrace +e_1,-e_1\rbrace,
$$

$$
\beta_2=\lbrace 010,101\rbrace
$$

переходит в

$$
E_2=\lbrace +e_2,-e_2\rbrace,
$$

$$
\beta_3=\lbrace 100,011\rbrace
$$

переходит в

$$
E_3=\lbrace +e_3,-e_3\rbrace.
$$

Выбор конкретного изоморфизма содержит два независимых типа произвола.

Первый — блочный: можно выбрать любую биекцию

$$
\lbrace \beta_1,\beta_2,\beta_3\rbrace \to \lbrace E_1,E_2,E_3\rbrace.
$$

Второй — знаковый: внутри каждой пары можно поменять $+e_i$ и $-e_i$.

Эти два произвола дают

$$
3!\cdot 2^3=48
$$

графовых изоморфизмов такого типа. Обратно, любой изоморфизм обязан переводить не-рёбра в не-рёбра, значит он задаётся именно перестановкой трёх complement-пар и возможной перестановкой двух элементов внутри каждой пары.

Эти выборы задают конкретную координатную реализацию уже построенного octahedral graph-reading-а.


## §7.8. Различимость $R_1$ и $R_2$ внутри $R_{12}$

Octahedral graph-reading использует relation

$$
R_{12}=R_1\cup R_2.
$$

При этом различие между $R_1$ и $R_2$ сохраняется.

Relation $R_1$ остаётся одношаговым Hamming-отношением:

$$
(X_{\mathrm{adm}},R_1)\cong C_6.
$$

Relation $R_2$ остаётся двухшаговым Hamming-отношением:

$$
(X_{\mathrm{adm}},R_2)\cong K_3\sqcup K_3.
$$

Relation $R_{12}$ объединяет Hamming-distance $1$ и Hamming-distance $2$ в один graph-reading. В полной relation-грамматике §6 рёбра октаэдрального skeleton-а имеют два источника:

$$
d_H=1
$$

и

$$
d_H=2.
$$

Relation-грамматика §6 сохраняется. Graph-reading §7 собирает $R_1$ и $R_2$ в общий октаэдральный skeleton.


## §7.9. Shell-order и octahedral partition

В §7 используется ещё одно разложение уже собранного carrier-а.

Shell-order из §5 задаёт

$$
X_{\mathrm{adm}} = S_1^{(3)} \sqcup S_2^{(3)}.
$$

В §6 relation $R_2$ читала это shell-разложение напрямую:

$$
S_1^{(3)}\mapsto K_3,
\qquad
S_2^{(3)}\mapsto K_3.
$$
В §7 используется другое разложение:
$$
X_{\mathrm{adm}} = \beta_1\sqcup\beta_2\sqcup\beta_3.
$$

Это octahedral partition. Оно задаётся complement-парностью.

Каждая $\beta_i$ содержит одно состояние из $S_1^{(3)}$ и одно состояние из $S_2^{(3)}$. Например,

$$
\beta_1=\lbrace 001,110\rbrace,
$$

где

$$
001\in S_1^{(3)},
\qquad
110\in S_2^{(3)}.
$$

Значит, shell-order и octahedral partition — разные структуры на одном carrier-е.

Carrier §7:

$$
X_{\mathrm{adm}}.
$$

Новый слой состоит в выборе union-relation

$$
R_{12}=R_1\cup R_2
$$

и его graph-reading-е

$$
(X_{\mathrm{adm}},R_{12}) \cong O_3^{(1)}.
$$



# §8. Chamber layer октаэдра

## §8.1. Skeleton-данные из §7

По §7.1 admissible carrier разбит на complement-пары:

$$
X_{\mathrm{adm}} = \beta_1\sqcup\beta_2\sqcup\beta_3,
$$

где

$$
\beta_1=\lbrace 001,110\rbrace,
$$

$$
\beta_2=\lbrace 010,101\rbrace,
$$

$$
\beta_3=\lbrace 100,011\rbrace.
$$

По Утверждению 7.4 relation $R_{12}$ связывает две вершины тогда и только тогда, когда они принадлежат разным complement-парам. В octahedral graph-reading-е §7.7 каждая $\beta_i$ читается как пара противоположных вершин.

Иначе:

$$
x\in\beta_i,
\qquad
y\in\beta_j,
\qquad
i\neq j
$$
даёт
$$
(x,y)\in R_{12},
$$

а две разные вершины одной и той же $\beta_i$ не смежны в $R_{12}$.


## §8.2. Камеры как выборы из complement-пар

**Определение 8.1.**
Камерой chamber-layer-а $O_3$ называется подмножество

$$
C\subset X_{\mathrm{adm}}
$$

такое, что

$$
|C\cap \beta_i|=1
$$

для каждого

$$
i=1,2,3.
$$

Множество всех камер обозначается

$$
\mathrm{Cham}(O_3).
$$

Камера выбирает ровно одну вершину из каждой пары противоположных вершин:

$$
C=\lbrace x_1,x_2,x_3\rbrace,
\qquad
x_i\in\beta_i.
$$

В §8 камера и её vertex-support совпадают: vertex-support камеры $C$ есть само подмножество $C\subset X_{\mathrm{adm}}$. Определение §8 использует только finite chamber carrier.


## §8.3. Камеры и трёхвершинные clique-и

**Утверждение 8.2.**
Для подмножества

$$
C\subset X_{\mathrm{adm}},
\qquad
|C|=3,
$$
следующие условия эквивалентны:
$$
C\in \mathrm{Cham}(O_3);
$$

$$
C\subset X_{\mathrm{adm}}, \qquad |C|=3, \qquad C\ \mathrm{is\ a\ clique\ in}\ (X_{\mathrm{adm}},R_{12}).
$$

**Проверка.**
Пусть

$$
C\in \mathrm{Cham}(O_3).
$$

Тогда $C$ содержит ровно по одной вершине из каждой $\beta_i$. Поэтому любые две разные вершины $x,y\in C$ принадлежат разным complement-парам. По §8.1:

$$
(x,y)\in R_{12}.
$$

Значит, $C$ является трёхвершинным clique-ом.

Обратно, пусть

$$
C=\lbrace x,y,z\rbrace
$$

является трёхвершинным clique-ом в $R_{12}$. Две разные вершины одной complement-пары не смежны в $R_{12}$. Поэтому $C$ не может содержать две вершины одной $\beta_i$. Так как complement-пар ровно три и $|C|=3$, множество $C$ содержит ровно по одной вершине из каждой $\beta_i$. Следовательно,

$$
C\in\mathrm{Cham}(O_3).
$$

$$
\Box
$$


## §8.4. Число камер

**Утверждение 8.3.**

$$
|\mathrm{Cham}(O_3)|=8.
$$

**Проверка.**
Камера задаётся независимым выбором одного элемента в каждой из трёх complement-пар:

$$
\beta_1,
\quad
\beta_2,
\quad
\beta_3.
$$
В каждой паре есть два выбора. Поэтому
$$
|\mathrm{Cham}(O_3)| = 2\cdot 2\cdot 2 = 8.
$$

$$
\Box
$$

<p align="center">
  <a href="../assets/figures/4.8-chamber_code_projection_overview.png">
    <img src="../assets/figures/4.8-chamber_code_projection_overview.png" width="500" alt="Коды камер $C_\varepsilon$">
  </a>
</p>


## §8.5. Координатная запись камер

Зафиксируем порядок complement-пар:

$$
\beta_1,
\beta_2,
\beta_3.
$$
Внутри каждой пары выберем двоичную маркировку:
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

Эта маркировка реализует знаковый произвол §7.6: внутри каждой complement-пары можно поменять marker $0$ и marker $1$. Другой выбор даёт изоморфную координатную запись через независимые перестановки двух элементов внутри complement-пар.

Для

$$
\varepsilon=(\varepsilon_1,\varepsilon_2,\varepsilon_3)\in\lbrace 0,1\rbrace^3
$$

задаётся камера

$$
C_\varepsilon = \lbrace b_1^{\varepsilon_1},b_2^{\varepsilon_2},b_3^{\varepsilon_3}\rbrace.
$$

В согласии с bit-order §3.6 запись индекса камеры как трёхбитной строки идёт в порядке

$$
\varepsilon_3\,\varepsilon_2\,\varepsilon_1.
$$

То есть

$$
C_{\varepsilon_3\,\varepsilon_2\,\varepsilon_1} = \lbrace b_1^{\varepsilon_1},b_2^{\varepsilon_2},b_3^{\varepsilon_3}\rbrace.
$$

Получаем отображение

$$
\Phi:\mathrm{Cham}(O_3)\to Q_3
$$

по формуле

$$
\Phi(C_\varepsilon)=\varepsilon_3\,\varepsilon_2\,\varepsilon_1.
$$

Здесь $Q_3$ означает полный трёхбитный carrier из §5.1:

$$
Q_3=\lbrace 0,1\rbrace^3.
$$

Он содержит все восемь состояний, включая

$$
000
\qquad
\mathrm{and}
\qquad
111.
$$

**Утверждение 8.4.**
Отображение

$$
\Phi:\mathrm{Cham}(O_3)\to Q_3
$$

является биекцией.

**Проверка.**
Каждая камера содержит ровно один элемент из каждой пары $\beta_i$. Поэтому она однозначно задаёт тройку выборов

$$
(\varepsilon_1,\varepsilon_2,\varepsilon_3).
$$

Обратно, каждая тройка

$$
\varepsilon\in\lbrace 0,1\rbrace^3
$$

задаёт ровно одну камеру $C_\varepsilon$. Следовательно, $\Phi$ биективно.

$$
\Box
$$

В сжатой записи:

$$
\mathrm{Cham}(O_3)\cong Q_3.
$$

<p align="center">
  <a href="../assets/figures/4.10-chambers_two_octahedron_views.png">
    <img src="../assets/figures/4.10-chambers_two_octahedron_views.png" width="500" alt="Две октаэдральные проекции chamber-layer-а">
  </a>
</p>

Эта биекция кодирует камеры октаэдра элементами $Q_3$. Carrier вершин $X_{\mathrm{adm}}$ и carrier камер остаются разными типами объектов.


## §8.6. Chamber-adjacency и cube graph

**Определение 8.5.**
Для $n\geq 1$ graph-reading

$$
Q_n^{(1)}
$$

есть Hamming-one graph на полном carrier-е $Q_n$. Его relation задаётся правилом

$$
(x,y)\in R_{Q_n}^{(1)}
\quad\Longleftrightarrow\quad
x\neq y \land d_H(x,y)=1.
$$

Для $n=3$ graph $Q_3^{(1)}$ имеет $8$ вершин и $12$ рёбер. Для $n=2$ это тот же one-step Hamming graph-reading, который в §4 читался как $C_4$.

**Определение 8.6.**
Для

$$
C,D\in\mathrm{Cham}(O_3)
$$

положим

$$
(C,D)\in R_{\mathrm{ch}}
$$

тогда и только тогда, когда

$$
C\neq D
$$

и

$$
|C\cap D|=2.
$$

То есть две камеры смежны, если они имеют две общие вершины.

**Утверждение 8.7.**

$$
(\mathrm{Cham}(O_3),R_{\mathrm{ch}}) \cong Q_3^{(1)}.
$$

**Проверка.**
Пусть

$$
C_\varepsilon,
\qquad
C_\delta
$$

— две камеры.

Они имеют общую вершину из пары $\beta_i$ тогда и только тогда, когда

$$
\varepsilon_i=\delta_i.
$$

Поэтому

$$
|C_\varepsilon\cap C_\delta|=2
$$

тогда и только тогда, когда $\varepsilon$ и $\delta$ совпадают ровно в двух координатах и различаются ровно в одной координате:

$$
d_H(\varepsilon,\delta)=1.
$$

Это правило смежности в cube graph $Q_3^{(1)}$. Следовательно,

$$
(\mathrm{Cham}(O_3),R_{\mathrm{ch}}) \cong Q_3^{(1)}.
$$

$$
\Box
$$

Таким образом,

$$
\mathrm{Cham}(O_3)\cong Q_3
$$

как chamber carrier, а

$$
(\mathrm{Cham}(O_3),R_{\mathrm{ch}})
\cong Q_3^{(1)}
$$

как chamber graph-reading.




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
