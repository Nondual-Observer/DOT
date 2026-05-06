# Приложение C. Мост Hopf/Borromean

Статус: мостовой документ / протокол топологических прообразов.

Этот документ фиксирует место чтений типа Möbius, Hopf и Borromean относительно строгого конечного ядра. Источник конечен: \(Q_3\), \(X_{\mathrm{adm}}\), отношения \(R_1,R_2,R_3\), транспорт \(T\), осевое разложение и точные осевые представления. Топологические прообразы получают отдельный мостовой статус.

---

## C.0. Аннотация и ход документа

Мост Hopf/Borromean связывает три конечные структуры ранга \(3\) с тремя топологическими чтениями.

Первая структура — осевая пара

\[
H_i=\{I_i^-,I_i^+\}.
\]

Она даёт двухполюсный носитель одной оси. В топологическом чтении такая пара может быть сопоставлена паре связанных окружностей типа Hopf, но только после задания отдельного топологического носителя и вложения.

Вторая структура — полуоборот транспорта

\[
T^3(I_i^\eta)=I_i^{-\eta}.
\]

Он является конечной \(Z_2\)-голономией на \(X_{\mathrm{adm}}\). В топологическом чтении этот полуоборот соответствует мотиву Möbius-монодромии: обход меняет знак в двухточечном волокне.

Третья структура — разбиение всего шестипозиционного носителя на три осевые пары:

\[
X_{\mathrm{adm}}=H_1\sqcup H_2\sqcup H_3.
\]

В топологическом чтении эта тройка может быть сопоставлена борромеевской триаде блоков. Такое чтение не утверждает наличие буквальных борромеевских колец внутри конечного ядра. Оно фиксирует только схему: три блока удерживают общий мотив, который не сводится к одной выбранной паре.

Ход документа:

\[
\text{строгий rank-3 источник}
\to
\text{осевые пары}
\to
\text{точные осевые представления}
\to
\text{конечная }Z_2\text{-голономия}
\to
\text{Hopf/Möbius/Borromean-чтения}
\to
\text{граница статусов}.
\]

Главная граница: \(R_3=3K_2\), \(T^3\) и \(X_{\mathrm{adm}}\cong I_3\times\Sigma\) являются объектами строгого конечного ядра. Лента Мёбиуса, связка Hopf и борромеевская связка не входят в это ядро. Они становятся собственными объектами только в отдельном топологическом слое с заданными носителями, вложениями и инвариантами.

---

## C.1. Исходный strict-слой

Rank \(3\) задаёт полный carrier:

\[
Q_3=\mathbb F_2^3.
\]

Admissible carrier:

\[
X_{\mathrm{adm}}=Q_3\setminus\{000,111\}.
\]

На \(X_{\mathrm{adm}}\) заданы Hamming relations:

\[
R_k=\{(x,y)\in X_{\mathrm{adm}}\times X_{\mathrm{adm}}:
x\neq y,\ d_H(x,y)=k\},
\qquad
k=1,2,3.
\]

Graph-readings:

\[
(X_{\mathrm{adm}},R_1)\cong C_6,
\]

\[
(X_{\mathrm{adm}},R_2)\cong K_3\sqcup K_3,
\]

\[
(X_{\mathrm{adm}},R_3)\cong 3K_2.
\]

Union relation:

\[
R_{12}=R_1\cup R_2,
\qquad
(X_{\mathrm{adm}},R_{12})\cong K_{2,2,2}.
\]

Strict-источник для Hopf/Borromean bridge — relation \(R_3\) и axial factorization:

\[
X_{\mathrm{adm}}\cong I_3\times\Sigma,
\qquad
I_3=\{I_1,I_2,I_3\},
\qquad
\Sigma=\{-,+\}.
\]

---

## C.2. Axial pairs

Для \(i\in\{1,2,3\}\):

\[
H_i=\{I_i^-,I_i^+\}\subset X_{\mathrm{adm}}.
\]

Три axial pairs разбивают carrier:

\[
X_{\mathrm{adm}}=H_1\sqcup H_2\sqcup H_3.
\]

Relation \(R_3\) ограничивается на каждую pair как \(K_2\):

\[
(H_i,R_3|_{H_i})\cong K_2.
\]

Вся \(R_3\)-структура:

\[
(X_{\mathrm{adm}},R_3)
\cong
H_1\sqcup H_2\sqcup H_3
\cong
3K_2.
\]

Это native finite layer. Hopf-термин к этому слою не добавляет нового strict-объекта.

---

## C.3. Axial presentations

Для каждой axial pair задаётся reading:

\[
\pi_i:H_i\to\{I_i\},
\]

\[
\pi_i(I_i^-)=I_i,
\qquad
\pi_i(I_i^+)=I_i.
\]

Recovery datum:

\[
\operatorname{rec}_i(I_i)
=
(H_i,R_3|_{H_i}).
\]

Axial presentation:

\[
\Pi_i^{\operatorname{ax},(3)}
=
(H_i,R_3|_{H_i},\pi_i,\operatorname{rec}_i).
\]

Эта presentation exact: единственное волокно reading-а равно \(H_i\), а recovery возвращает это волокно вместе с induced relation.

Содержательная формула strict layer:

\[
\text{one axial invariant}
\quad
\longmapsto
\quad
\text{two polar manifestations}.
\]

---

## C.4. Finite holonomy

Transport \(T\) на \(X_{\mathrm{adm}}\) строится после выбора orientation на \(C_6\)-reading relation \(R_1\):

\[
T:X_{\mathrm{adm}}\to X_{\mathrm{adm}},
\qquad
T^6=\operatorname{id}_{X_{\mathrm{adm}}}.
\]

Half-return:

\[
T^3(x)=x+111.
\]

В axial notation:

\[
T^3(I_i^\eta)=I_i^{-\eta}.
\]

Strict-статус:

\[
T^3
\]

является finite \(Z_2\)-holonomy на \(X_{\mathrm{adm}}\).

Bridge-reading:

\[
T^3
\quad
\text{читается как}
\quad
\text{Möbius-type monodromy}.
\]

Literal Möbius band требует собственного topological carrier:

\[
p:E\to S^1,
\qquad
p^{-1}(\theta)\cong\Sigma,
\]

с monodromy swap после одного обхода. Этот carrier имеет bridge-статус.

---

## C.5. Hopf-type reading

Для каждой strict axial pair:

\[
H_i=\{I_i^-,I_i^+\},
\]

bridge-target задаётся как two-component topological pair:

\[
\mathcal H_i=(L_i^-,L_i^+),
\]

где \(L_i^-\) и \(L_i^+\) — ориентированные closed curves в ambient \(3\)-manifold, например в \(S^3\).

Literal Hopf condition:

\[
\operatorname{lk}(L_i^-,L_i^+)=\pm1.
\]

Bridge-handoff:

\[
I_i^-\mapsto L_i^-,
\qquad
I_i^+\mapsto L_i^+,
\]

\[
R_3|_{H_i}
\quad
\mapsto
\quad
\text{linked two-component relation}.
\]

Статус:

\[
(H_i,R_3|_{H_i})\cong K_2
\]

является native strict data.

\[
\mathcal H_i
\]

является Hopf-target data после задания embedding model.

Hopf-type reading задаётся bridge-формулой:

\[
\text{one axial invariant in two polar manifestations}
\quad
\leadsto
\quad
\text{two linked boundary components}.
\]

---

## C.6. Borromean block-triad

Strict finite source:

\[
\mathcal B_3=\{H_1,H_2,H_3\}.
\]

Каждый \(H_i\) является two-point axial block. Триада blocks фиксируется после factorization:

\[
X_{\mathrm{adm}}\cong I_3\times\Sigma.
\]

Borromean-type bridge reading:

\[
(H_1,H_2,H_3)
\quad
\leadsto
\quad
\text{three block-components held as one triadic dependency}.
\]

Literal Borromean rings состоят из трёх topological components с nontrivial triple linking и trivial pairwise linking. Strict finite source задаёт другие данные:

\[
3\text{ axial blocks},
\qquad
2\text{ polar states in each block}.
\]

Совместимый topological target имеет block-level форму:

\[
\mathcal L_{\operatorname{block}}
=
(\mathcal H_1,\mathcal H_2,\mathcal H_3),
\]

где каждый \(\mathcal H_i\) может иметь Hopf-type structure.

Статус:

\[
\mathcal B_3
\]

является native finite block data.

\[
\text{Borromean block-triad}
\]

имеет bridge-readable status.

\[
\text{literal six-component topological link}
\]

имеет not-yet status до задания explicit curves, ambient space и linking invariants.

---

## C.7. Möbius, Hopf-band, Hopf pair

Три topological names имеют разные роли.

Möbius avatar:

\[
\text{one circuit}
\quad
\mapsto
\quad
\text{fiber swap}.
\]

Strict source:

\[
T^3(I_i^\eta)=I_i^{-\eta}.
\]

Hopf-band avatar:

\[
\text{annular/twisted surface with two boundary components}.
\]

Bridge-role:

\[
I_i^-,
\ I_i^+
\]

читаются как two boundary components одного axial block.

Hopf pair:

\[
\operatorname{lk}(L_i^-,L_i^+)=\pm1.
\]

Bridge-role:

\[
H_i
\]

реализуется как linked pair после задания embedding.

Status discipline:

\[
\text{finite }Z_2\text{-holonomy}
\]

имеет native status.

\[
\text{Möbius/Hopf/Hopf-band}
\]

имеют bridge-target status.

---

## C.8. Legacy labels

В ранних заметках использовались labels:

\[
D,\quad F,\quad C.
\]

В текущей strict architecture эти labels не являются native names axial carrier-а. Native carrier:

\[
I_3=\{I_1,I_2,I_3\}.
\]

В диаграммах может использоваться label map:

\[
\lambda:I_3\to\{D,F,C\}.
\]

Такая map имеет readable status. В proofs она используется только после того, как target layer задаёт \(D,F,C\) как собственные carrier labels.

---

## C.9. Таблица статусов

| Объект / claim | Strict core status | Hopf/Borromean bridge status |
|---|---:|---:|
| \(X_{\mathrm{adm}}\) | native | source carrier |
| \(R_3=3K_2\) | native | source relation for axial pairs |
| \(H_i=\{I_i^-,I_i^+\}\) | native | source block |
| \(\Pi_i^{\operatorname{ax},(3)}\) | native exact presentation | source presentation |
| \(T^3(I_i^\eta)=I_i^{-\eta}\) | native finite holonomy | Möbius-readable monodromy |
| \(p:E\to S^1\) with swap monodromy | вне strict core | Möbius bridge carrier |
| Hopf link \((L_i^-,L_i^+)\) | вне strict core | bridge target после embedding |
| \(\operatorname{lk}(L_i^-,L_i^+)=\pm1\) | вне strict core | topological verification |
| \((H_1,H_2,H_3)\) | native finite block triad | Borromean-readable source |
| literal six-component link | not-yet | требует explicit construction |
| physical interpretation | вне strict core | downstream interpretation |

---

## C.10. Необходимые рисунки

### Рисунок C1. \(R_3=3K_2\)

Показать три disjoint \(K_2\)-pairs:

\[
H_1,\quad H_2,\quad H_3.
\]

Назначение: strict finite source для Hopf-type reading.

### Рисунок C2. Axial factorization

Показать:

\[
X_{\mathrm{adm}}\cong I_3\times\Sigma.
\]

Строки: \(I_1,I_2,I_3\). Колонки: \(-,+\).

Назначение: показать, что Hopf-type pair относится к одному axial invariant.

### Рисунок C3. Half-return \(T^3\)

Показать \(C_6\)-cycle и три antipodal jumps:

\[
I_i^-\leftrightarrow I_i^+.
\]

Назначение: finite \(Z_2\)-holonomy before Möbius reading.

### Рисунок C4. Möbius target schema

Показать base circle \(S^1\), two-point fiber \(\Sigma\), monodromy swap после одного обхода.

Назначение: bridge carrier for Möbius-readable \(T^3\).

### Рисунок C5. Hopf pair per axis

Показать две linked curves \(L_i^-,L_i^+\) с label:

\[
\operatorname{lk}=\pm1.
\]

Назначение: topological target одной axial pair.

### Рисунок C6. Borromean block-triad

Показать три blocks:

\[
\mathcal H_1,\quad\mathcal H_2,\quad\mathcal H_3.
\]

Каждый block содержит две polar components. Block-level dependency показывается отдельно от internal Hopf-pair linking.

Назначение: отделить ordinary Borromean rings от \(3\) two-component blocks.

### Рисунок C7. Status boundary

Показать:

\[
\text{strict finite core}
\to
\text{Möbius/Hopf bridge}
\to
\text{literal topological link model}.
\]

Назначение: сохранить boundary между finite relations и topological embedding.

---

## C.11. Что зафиксировано

Hopf/Borromean layer имеет корректный bridge-статус.

Strict finite source:

\[
(X_{\mathrm{adm}},R_3)\cong 3K_2,
\qquad
X_{\mathrm{adm}}\cong I_3\times\Sigma.
\]

Exact axial presentations:

\[
\Pi_i^{\operatorname{ax},(3)}
=
(H_i,R_3|_{H_i},\pi_i,\operatorname{rec}_i).
\]

Finite holonomy:

\[
T^3(I_i^\eta)=I_i^{-\eta}.
\]

Bridge readings:

\[
T^3
\leadsto
\text{Möbius-type monodromy},
\]

\[
H_i
\leadsto
\text{Hopf-type axial pair},
\]

\[
(H_1,H_2,H_3)
\leadsto
\text{Borromean block-triad}.
\]

Literal topological models требуют explicit carriers, embeddings и linking invariants. До задания этих данных они остаются вне strict finite core.
