# DOT: finite-rank theory and bridges

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/Theory-CC%20BY--NC--SA%204.0-blue.svg)](LICENSE-THEORY.md)
[![License: Apache-2.0](https://img.shields.io/badge/Code-Apache--2.0-yellow.svg)](LICENSE)

[Русская версия](README_RU.md)

The **Theory of Observable Distinction** is a finite combinatorial theory organized around one principle: **distinction is the primary structural fact, and objects arise as stable forms of held and presented distinction**. DOT starts from the conditions under which distinctions can be held and observed, and then shows which finite structures appear when these conditions are successively strengthened.

The guiding intuition is that observation participates in how a distinction becomes accessible, stable, and checkable. In quantum physics, artificial-intelligence architectures, logic, information theory, cognitive science, and complex systems, this appears as one broad question: which states are distinguishable, which relations hold their distinguishability, which maps make it observable, and what data are preserved under such a passage?

The strict part of DOT is finite combinatorics. Each claim is grounded in an explicitly given finite carrier, a relation on it, a reading of that relation, and recovery data for what remains available after the reading.

The objects of the theory are finite sets with fixed relations. Distinguishing between them is a finite check. Growth is a finite procedure: a new binary coordinate is added to an already constructed domain. This makes DOT constructive from the ground up, finitely checkable, and open to external projections through separately marked bridge constructions.

## Main Principle

Simple inequality only says that two positions are different. In DOT, distinction is not reduced to the statement "one is not equal to the other." A distinction must be **held** by a structure, **presented** in some description, and retain a **recoverable** part when passing between descriptions.

Four roles are used for this: **carrier**, **relation**, **reading**, and **recovery**. The carrier gives the finite domain of positions. The relation specifies which positions are connected and how their distinguishability is held. The reading presents the distinction in another domain of description. Recovery specifies which part of the original positions and relations remains available after the reading.

These four roles define a way to record finite data, not an external interpretation. The formal unit of this record is a **representation**.

$$
(X, R, q, \mathrm{rec}).
$$

A representation gives every distinction a checkable finite form. Every statement in the theory reduces to checking properties of such a tuple on a finite carrier.

Held distinction passes through three levels of closure. At the **pair level**, a position receives its role only together with its opposite. At the **cycle level**, several such distinctions are linked by transitions; when the traversal returns to the beginning, a cycle appears, and opposition can be read as the position reached halfway around the cycle. At the **whole-scene level**, several distinctions are held as one scene: admissible joint configurations, chambers, incidence relations, and a Borromean intuition of mutual three-axis holding appear.

The minimal complete scene contains three opposite pairs: six positions forming the first complete geometric configuration of the theory.

![Rank-3 octahedral shell](assets/figures/4.1-R_12-octahedron.png)

## Tools and Result

The basic tools remain finite at every step. Carriers are given by binary strings; relations are built from coordinate differences, weight, complement, incidence, and finite transitions. Every object is introduced through explicit data, so it can be checked by finite enumeration or finite proof.

The point is not to collect familiar graphs. Cycles, the octahedron, the Petersen graph, multipartite graphs, and Singer cycles appear as different readings of one growing system of distinctions. One carrier can support several relations, and one relation can acquire a new role at the next rank.

At the end of the strict part one obtains a finite core up to rank 5. It contains constructed carriers, relations, readings, recoveries, chambers, incidence relations, cycles, and transition operators. This core is closed as a coherent finite-rank package:

$$
\mathfrak{R}_{\leq 5}^{\mathrm{fin}}=(\Pi_1,\mathfrak{C}_2,\mathfrak{C}_3,\mathfrak{C}_4,\mathfrak{A}_5).
$$

The general growth law is then stated: the passage from rank $n$ to rank $n+1$ is given by adding a new binary coordinate. The construction up to rank 5 is therefore not just an example; it fixes a checkable finite pattern for how distinctions grow, are repackaged, and are read again inside larger structures.

## Main Manuscript

- [Main manuscript, English](00_Theory/DOT_main_EN.md)

The main manuscript is the central document of the package. It builds DOT as a finite theory in which each object is specified by a carrier, relation, reading, and recovery. Rank $1$ introduces the polar pair. Rank $2$ builds the binary carrier $Q_2$ and several readings of it: a cycle, opposite pairs, complete connectivity, and partial closure.

Rank $3$ gives the first complete scene: two homogeneous positions are removed from $Q_3$, leaving the six-point carrier $X_{\mathrm{adm}}$. The relations $R_1, R_2, R_3$, the octahedral shell, chambers, incidence, and a six-step transport appear on this carrier. These constructions provide the basic form of later growth.

Ranks $4$ and $5$ develop the same scheme on larger carriers. In rank $4$, the rank-3 octahedral structure reappears inside the middle layer of a fifteen-position carrier. In rank $5$, a thirty-one-position carrier is built with shell decomposition $5+10+10+5+1$, middle layers, an outer layer, the Petersen graph, selected cycles, and a Singer cycle. The final part states the general rank-growth law and the universal outer layer.

![Rank-4 middle-layer octahedral structure](assets/figures/5.4-S2_rank4_octahedral_graph.png)

## Mathematical Start

- [01A. Mathematical bridge to the strict core](01_Mathematical_Start/01A_DOT_Mathematical_Bridge_EN.md)

  Introductory mathematical text for the passage from the idea of distinction to strict notation. The basic unit is given by four data: carrier, relation, reading, and recovery. The document moves from a polar pair and a two-bit carrier to the six-point rank-3 structure.

- [02A. Core foundation and theorems](01_Mathematical_Start/02A_DOT_Core_Foundation_And_Theorems_EN.md)

  The first strict block of the theory. It fixes definitions and restrictions, then analyzes the rank-3 six-point structure as a finite object: a cycle, three complement pairs, two triangular components, an octahedron, chambers, spectra, and transport.

- [02B. Shell extension and categorical/operator packaging](01_Mathematical_Start/02B_DOT_Shell_Extension_And_Categorical_Packaging_EN.md)

  Continuation of the strict core toward rank $4$. The already built six-point scene appears inside a larger carrier through weight layers, the middle layer, the outer layer, and operator readings. The document fixes how previous structures are preserved, change role, and enter a wider layer.

- [03A. AMR-SR: scale/residue line](01_Mathematical_Start/03A_DOT_AMR_Scale_Residue_Line_EN.md)

  The first arithmetic AMR branch. Its carrier is the plane of pairs $\mathcal R=\mathbb N_{>0}^2$. The document analyzes a pair $(a,b)$ through the decomposition $(a,b)=g(p,q)$, where $g=\gcd(a,b)$ and $(p,q)$ is the primitive direction. This gives difference layers, primitive rays, local cells, and the scalar residue $\mathrm{Res}_{\mathrm{sr}}=(g-1)|p-q|$.

  The role of 03A is to fix the scale/residue line and its partial bridge to the strict core: the arrows $\beta_3,\beta_4$ connect selected arithmetic cases with rank-3 relations. After 03B is separated, this document should not be read as the whole AMR package. It is the AMR-SR branch, not the divisor-carrier theory.

- [03B. AMR-DC: divisor carrier and chain extension](01_Mathematical_Start/03B_AMR_Divisor_Carrier_and_Chain_Extension.md)

  The second arithmetic AMR branch. Its carrier is the finite divisor lattice $D(N)=\{d:d\mid N\}$. The document shows that if $N=p_1^{a_1}\cdots p_r^{a_r}$, then $D(N)$ is read as the product of finite chains $\prod_i\{0,\ldots,a_i\}$. For square-free numbers this gives the Boolean carrier $Q_n$; after the lower and upper poles are removed, the proper carrier $D^\circ(N)\cong U_n$ appears.

  The central example of 03B is $30=2\cdot3\cdot5$. Its proper carrier $D^\circ(30)=\{2,3,5,6,10,15\}$ is an arithmetic avatar of the six-point scene $X_{\mathrm{adm}}$. On the same carrier one builds the relations $C_6$, $K_3\sqcup K_3$, $3K_2$, and $K_{2,2,2}$. The document then develops chain extension, recovery discipline, the residue carrier connection, and bridge readings toward $A_2/\mathfrak{sl}_3/\mathfrak{su}(3)$, the Hopf/Borromean layer, and the Möbius function.

  The boundary between 03A and 03B is essential: $\mathrm{Res}_{\mathrm{sr}}$ from AMR-SR is not the relation $R_{\mathrm{oct}}$ in AMR-DC, and the carriers $\mathbb N_{>0}^2$ and $D(N)$ are not identified without a separate bridge map.

## Bridge Notes

- [RGB / CMY / Kuhn / HSV color bridge](02_Bridges/01_Color_RGB_Kuhn/DOT_RGB_Kuhn_Color_Bridge_EN.md)

  A color projection of rank $3$. The carrier $Q_3$ is read as an RGB/CMY cube, while the six-point layer $X_{\mathrm{adm}}$ is read as the chromatic carrier without the black and white poles. The relations $R_1, R_2, R_3$ receive color forms: a cycle, two triads, and three complementary axes. The octahedral shell and the decomposition of the RGB cube into Kuhn sectors are fixed separately.

  ![DOT chambers on the color octahedron](assets/figures/B7c_DOT_chambers_two_octahedron_views.png)

  Figure from the color bridge: DOT chambers on the color octahedron and the two RGB/CMY sides.

- [Binarity as a growth principle of DOT](02_Bridges/02_Binary_Growth/DOT_Binary_Growth_Principle_EN.md)

  A note on the binary mechanism of growth. A new rank is introduced by adding a new leading bit; previous states receive new positions, layers are lifted by weight, and complement connects opposite regions of the carrier. This is the general transition principle between ranks in the main manuscript.

- [Binary coordinates in DOT](02_Bridges/02_Binary_Growth/DOT_Binary_Coordinate_Note_EN.md)

  A technical coordinate note. It gathers conventions for binary carriers, string weight, layers, Hamming relations, complement, and rank growth. The file serves as a reference layer for consistent notation.

- [Six-state A2 / sl3 / su(3) bridge](02_Bridges/03_A2_sl3_su3/DOT_Six_State_A2_sl3_su3_EN.md)

  An algebraic reading of the rank-3 six-point structure. The document connects the $3+3$ split, triangular relations, and opposite pairs with $A_2$ root data, the Cartan matrix, Chevalley realization, and action on a six-position module.

- [Hopf / Borromean bridge](02_Bridges/04_Hopf_Borromean/DOT_Principles_Hopf_2x3_Full_2026-04-24_EN.md)

  A topological bridge for pairing, cyclic transport, and triple connectivity. It introduces axial pairs, finite holonomy, Hopf-type reading, the Borromean block triad, and the related name-status discipline. This is a separate map of topological readings for the already constructed finite layer.

- [Cryptographic spectral block](02_Bridges/05_Cryptographic_Spectral_Block/DOT_Cryptographic_Spectral_Block.md)

  A theorem package for the cross-polytope--hypercube composite graph. It computes the spectrum of a fixed block Laplacian and reads correlation immunity, balancedness, and resilience of Boolean functions as vanishing on explicit spectral sectors.

## Appendix, Figures, and Glossary

- [Appendix AF. Object atlas and glossary](03_Appendix/DOT_Appendix_AF_Atlas_And_Glossary_EN.md) collects the main carriers, layers, relations, graphs, cycles, packages, term statuses, and figure map.
- [Figure folder](assets/figures) contains diagrams used in the main manuscript and bridge notes.

The appendix is useful as a navigation layer: it helps check notation, formulas on figures, and object statuses.

## Verification

Python dependencies are listed in [requirements.txt](requirements.txt).

```bash
python3 -m pip install -r requirements.txt
```

Available verification scripts:

```bash
python3 01_Mathematical_Start/DOT_Core_verifier.py
python3 01_Mathematical_Start/DOT_AMR_verifier.py
python3 02_Bridges/03_A2_sl3_su3/verify_six_state_a2_sl3_su3.py
python3 02_Bridges/05_Cryptographic_Spectral_Block/verify_cryptographic_spectral_block.py
```

These scripts check selected constructions from the finite core, AMR, the representation bridge, and the spectral block.

## Licenses

Theoretical texts, manuscripts, figures, and documentation are distributed under [CC BY-NC-SA 4.0](LICENSE-THEORY.md), unless a specific file states otherwise.

Executable source code is distributed under the [Apache License 2.0](LICENSE).

---

© 2026 Igor M. Zhuk. Theory and documentation are distributed under the corresponding licenses listed above.
