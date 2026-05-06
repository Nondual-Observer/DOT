#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clean verifier for the finite DOT core.

What this script checks:
1. The axiom-level triad `Z_D, Z_F, Z_C` is operationally irreducible in the canonical model family.
2. The 3-bit admissible core has exactly six states.
3. On those six states there are two different exact graphs:
   - primitive one-bit process: C_6
   - residual non-complement carrier: K(2,2,2)
4. The octahedron/chamber package produces Q_3 and the canonical incidence matrix B.
5. The exact Laplacian spectra and edge resistances match theory.
6. The composite graph (octahedron + cube) has exact spectrum
   {0^1, 4^3, 7^4, 9^4, 10^2}, hence lambda_2 = 4.
7. The slow eigenspace has the exact energy ratio 4:1 between chambers and poles.
8. The twisted transport law on the selected cycle has gauge-invariant holonomy.
9. The 4D shell ladder separates the outer 8-vertex carrier from the 14-vertex nontrivial package.
10. The general n-dimensional shell law separates V_n from U_n.
11. The minimal path-category layer is compatible with chamber coding and reduction.
12. Shell apertures form an exact banded decomposition of hypercube dynamics.
13. The natural presentation symmetry class exhausts the color-preserving automorphisms
    of the 3-bit relation core, and the axial incidence map has normalized
    coupling coefficient 2 whose square gives the 3D ratio 4.

Dependency policy:
- NumPy only.
- No SciPy required.

Evidence policy:
- This file is a clean numeric/regression verifier for the frozen corpus.
- This file is the canonical code-level source of truth for finite-core checks.
- External tools should import exported helpers from here rather than re-implement
  finite-core verification logic, except for compatibility fallbacks.
- The Markov block is illustrative only and is not part of the [Д]-layer.
"""

from itertools import permutations, product
from math import comb

import numpy as np

TOL = 1e-10


CORE_CHECK_CATALOG = (
    {
        "ref": "0.1.A / 8.12.D1-D3",
        "claim": "Preparatory binary pre-core F_2^1/F_2^2 with its canonical local graph readings and the local square corridor.",
        "functions": ("precore_binary_layer_test",),
    },
    {
        "ref": "1.4-1.5",
        "claim": "Operational irreducibility of the triad Z_D, Z_F, Z_C in the canonical model class.",
        "functions": ("axiomatic_level_test",),
    },
    {
        "ref": "2.0.4-2.0.7",
        "claim": "Minimality and uniqueness of the six-state carrier inside the axis-transport model class.",
        "functions": ("minimal_active_carrier_test",),
    },
    {
        "ref": "2.2-2.6",
        "claim": "Three-bit admissible core with C_6 cyclic process and K(2,2,2) residual graph.",
        "functions": ("build_admissible_core", "combinatorial_core_test"),
    },
    {
        "ref": "2.6.6-2.6.9",
        "claim": "Exact relation scheme and finite relation-core signature on X_adm.",
        "functions": ("relation_scheme_test", "compute_core_bridge_signature", "core_bridge_signature_test"),
    },
    {
        "ref": "2.6.9a / 3.3.9",
        "claim": "Shell face grammar, pure/transition chambers, and Kuhn-sector incidence law.",
        "functions": ("shell_face_kuhn_transition_test",),
    },
    {
        "ref": "3-4",
        "claim": "Canonical carriers, octahedral realization, chamber cube, and incidence identities.",
        "functions": ("build_C6", "build_K222", "build_Q3", "build_incidence_matrix", "stanley_reisner_check"),
    },
    {
        "ref": "5-6",
        "claim": "Exact Laplacian spectra, effective resistances, and the 3D slow-mode 4:1 law.",
        "functions": ("spectral_test", "block_operator_spectral_test"),
    },
    {
        "ref": "7",
        "claim": "Gauge-invariant Z_2 holonomy and transport layer.",
        "functions": ("holonomy_test_exact",),
    },
    {
        "ref": "7.8",
        "claim": "Presentation stability and the axial incidence coefficient.",
        "functions": ("presentation_and_intertwiner_test",),
    },
    {
        "ref": "8.1-8.6",
        "claim": "Higher-dimensional shell laws, chamber laws, and reduction statements.",
        "functions": (
            "higher_4d_graph_test",
            "hamming_shell_ladder_test_4d",
            "general_dimension_shell_law_test",
            "general_chamber_block_law_test",
            "general_dimension_reduction_test",
            "strong_geometric_reduction_test",
        ),
    },
    {
        "ref": "8.8-8.13",
        "claim": "Minimal categorical layer on chamber coding and reduction.",
        "functions": ("minimal_category_layer_test",),
    },
    {
        "ref": "8.15-8.27",
        "claim": "Aperture algebra, strengthened shell operators, and sl2-compatible structure.",
        "functions": ("aperture_algebra_test", "strengthened_aperture_algebra_test"),
    },
    {
        "ref": "8.28.2-8.28.4",
        "claim": "Operator-combinatorial interface sl2 -> Sigma_core.",
        "functions": ("compute_sl2_sigma_core_signature", "sl2_sigma_core_bridge_test"),
    },
)


def get_core_check_catalog():
    """Return the theorem-to-function map used by the finite-core verifier."""
    return [dict(item) for item in CORE_CHECK_CATALOG]


# ============================================================================
# Admissible-state builders
# ============================================================================

def build_raw_cube_states(n):
    return list(product([0, 1], repeat=n))


def build_admissible_states_by_filter(n):
    """
    Strict admissibility used in the clean core:
    - for n = 3: remove only 000 and 111;
    - for n >= 4 in the higher-layer graph program: keep weights 1 and n-1.
    """
    raw_states = build_raw_cube_states(n)
    if n == 3:
        admissible = [state for state in raw_states if state not in {(0, 0, 0), (1, 1, 1)}]
        removed = [state for state in raw_states if state not in admissible]
    else:
        admissible = [state for state in raw_states if sum(state) in {1, n - 1}]
        removed = [state for state in raw_states if state not in admissible]
    return raw_states, admissible, removed


def build_hamming_shells(n):
    raw_states = build_raw_cube_states(n)
    shells = {k: [] for k in range(n + 1)}
    for state in raw_states:
        shells[sum(state)].append(state)
    return shells


def build_binary_precore_states():
    return [(0, 0), (0, 1), (1, 0), (1, 1)]


def build_binary_precore_graphs():
    states = build_binary_precore_states()
    size = len(states)
    index = {state: i for i, state in enumerate(states)}

    c4 = np.zeros((size, size), dtype=int)
    two_k2 = np.zeros((size, size), dtype=int)
    k4_minus_e = np.zeros((size, size), dtype=int)
    k4 = np.ones((size, size), dtype=int) - np.eye(size, dtype=int)

    for i, a in enumerate(states):
        for j in range(i + 1, size):
            b = states[j]
            dist = hamming_distance(a, b)
            xor = tuple(x ^ y for x, y in zip(a, b))

            if dist == 1:
                c4[i, j] = c4[j, i] = 1
            if xor == (1, 1):
                two_k2[i, j] = two_k2[j, i] = 1

    missing_edge = (index[(0, 0)], index[(1, 1)])
    for i in range(size):
        for j in range(i + 1, size):
            if (i, j) != missing_edge:
                k4_minus_e[i, j] = k4_minus_e[j, i] = 1

    simplex_sector = [index[(0, 1)], index[(1, 0)], index[(1, 1)]]

    return {
        "states": states,
        "labels": ["".join(str(bit) for bit in state) for state in states],
        "C4": c4,
        "2K2": two_k2,
        "K4_minus_e": k4_minus_e,
        "K4": k4,
        "simplex_sector": simplex_sector,
    }


def pairwise_complement_order(states):
    """
    Reorder states so that each complement pair is adjacent in the list.
    Within each pair, the state with first differing bit = 1 comes first.
    """
    state_set = set(states)
    seen = set()
    ordered = []
    for state in states:
        if state in seen:
            continue
        comp = tuple(1 - bit for bit in state)
        if comp not in state_set:
            raise ValueError("Complement pair is missing from admissible set.")
        if state > comp:
            first, second = state, comp
        else:
            first, second = comp, state
        ordered.extend([first, second])
        seen.add(first)
        seen.add(second)
    return ordered


def build_noncomplement_graph_on_states(states):
    """
    Build the residual graph on any finite state family closed under complement.
    """
    states = pairwise_complement_order(states)
    labels = ["".join(str(bit) for bit in state) for state in states]
    index = {state: i for i, state in enumerate(states)}

    complement = {}
    for i, state in enumerate(states):
        complement[i] = index[tuple(1 - bit for bit in state)]

    A_res = np.zeros((len(states), len(states)), dtype=int)
    for i in range(len(states)):
        for j in range(len(states)):
            if i != j and j != complement[i]:
                A_res[i, j] = 1

    return {
        "states": states,
        "labels": labels,
        "complement": complement,
        "A_res": A_res,
    }


# ============================================================================
# Linear algebra utilities
# ============================================================================

def eigh_sorted(matrix):
    """Return sorted eigenvalues and corresponding eigenvectors."""
    values, vectors = np.linalg.eigh(matrix.astype(float))
    order = np.argsort(values)
    return values[order], vectors[:, order]


def laplacian(adjacency):
    degrees = np.sum(adjacency, axis=1)
    return np.diag(degrees) - adjacency


def pseudoinverse_laplacian(L):
    """
    Hermitian Moore-Penrose pseudoinverse for symmetric graph Laplacians.

    Using pinv(..., hermitian=True) avoids hand-written zero-eigenvalue masking
    and is numerically more robust on larger block systems.
    """
    return np.linalg.pinv(L.astype(float), hermitian=True, rcond=TOL)


def effective_resistance(L_pseudo, u, v):
    return L_pseudo[u, u] + L_pseudo[v, v] - 2.0 * L_pseudo[u, v]


def foster_theorem_check(adjacency, tolerance=TOL):
    """Check sum_{edges} R_eff = |V| - 1."""
    L = laplacian(adjacency)
    L_pseudo = pseudoinverse_laplacian(L)
    n = adjacency.shape[0]
    edges = [(i, j) for i in range(n) for j in range(i + 1, n) if adjacency[i, j] > 0]
    total = sum(effective_resistance(L_pseudo, i, j) for i, j in edges)
    expected = n - 1
    return abs(total - expected) < tolerance, total, expected


def edge_resistance_mean(adjacency):
    L_pseudo = pseudoinverse_laplacian(laplacian(adjacency))
    n = adjacency.shape[0]
    edges = [(i, j) for i in range(n) for j in range(i + 1, n) if adjacency[i, j] > 0]
    values = [effective_resistance(L_pseudo, i, j) for i, j in edges]
    return float(np.mean(values))


def connected_components(adjacency):
    """Return list of components of an undirected graph."""
    n = adjacency.shape[0]
    unseen = set(range(n))
    components = []

    while unseen:
        start = unseen.pop()
        stack = [start]
        comp = [start]
        while stack:
            v = stack.pop()
            neighbors = [u for u in range(n) if adjacency[v, u] > 0 and u in unseen]
            for u in neighbors:
                unseen.remove(u)
                stack.append(u)
                comp.append(u)
        components.append(sorted(comp))

    return components


# ============================================================================
# Axiomatic layer: canonical weakening countermodels
# ============================================================================

def axiomatic_level_test():
    print("\n[Тест] Аксиоматический уровень [А] через канонические контрмодели")
    print("-" * 50)

    # ¬Z_D: keep the full raw 3-cube and use non-complement residual adjacency.
    raw_states = build_raw_cube_states(3)
    negD = build_noncomplement_graph_on_states(raw_states)
    A_negD = negD["A_res"]
    A_k2222, _ = build_complete_multipartite([2, 2, 2, 2])
    negD_graph_ok = np.array_equal(A_negD, A_k2222)
    eigenvalues_negD, _ = eigh_sorted(laplacian(A_negD))
    lambda2_negD = float(eigenvalues_negD[1])
    negD_lambda_ok = abs(lambda2_negD - 6.0) < 1e-8
    negD_core_breaks = A_negD.shape[0] == 8 and abs(lambda2_negD - 4.0) > 1e-8

    # ¬Z_F: keep the canonical cycle but force trivial holonomy +1.
    trivial_epsilon = np.ones(6, dtype=int)
    all_holonomies = set()
    negF_ok = True
    for g in product([-1, 1], repeat=6):
        g = np.array(g, dtype=int)
        transformed = np.array(
            [trivial_epsilon[i] * g[(i + 1) % 6] * g[i] for i in range(6)],
            dtype=int,
        )
        value = int(np.prod(transformed))
        all_holonomies.add(value)
        if value != 1:
            negF_ok = False
            break
    negF_ok = negF_ok and all_holonomies == {1}

    # ¬Z_C: duplicate the strict carrier by an external flag and gate adjacency by that flag.
    core = build_admissible_core()
    A_res = core["A_res"]
    A_negC = np.zeros((12, 12), dtype=int)
    A_negC[:6, :6] = A_res
    A_negC[6:, 6:] = A_res
    components = connected_components(A_negC)
    component_sizes = sorted(len(comp) for comp in components)
    negC_ok = (
        len(components) == 2
        and component_sizes == [6, 6]
        and np.array_equal(A_negC[:6, :6], A_res)
        and np.array_equal(A_negC[6:, 6:], A_res)
        and not np.any(A_negC[:6, 6:])
        and not np.any(A_negC[6:, :6])
    )

    print(
        f"  ¬Z_D: residual graph = K(2,2,2,2): {'✓' if negD_graph_ok else '✗'}, "
        f"λ₂ = {lambda2_negD:.1f}"
    )
    print(
        f"  ¬Z_F: голономии после всех 64 калибровок = {sorted(all_holonomies)}, "
        f"тривиальный класс: {'✓' if negF_ok else '✗'}"
    )
    print(
        f"  ¬Z_C: число компонент = {len(components)}, размеры = {component_sizes}, "
        f"внешнее расщепление: {'✓' if negC_ok else '✗'}"
    )

    overall = negD_graph_ok and negD_lambda_ok and negD_core_breaks and negF_ok and negC_ok
    print(f"  Результат: {'[Д|мод] ПРОЙДЕН' if overall else '✗ НЕСОВПАДЕНИЕ'}")

    return {
        "negD_graph_ok": negD_graph_ok,
        "negD_lambda_ok": negD_lambda_ok,
        "negF_ok": negF_ok,
        "negC_ok": negC_ok,
        "status": "[Д|мод]",
        "passed": overall,
    }


# ============================================================================
# Three-bit admissible core
# ============================================================================

def build_admissible_core():
    """
    Canonical order groups complement pairs together:
    0: 100, 1: 011
    2: 010, 3: 101
    4: 001, 5: 110
    """
    raw_states, admissible, removed = build_admissible_states_by_filter(3)
    states = [
        (1, 0, 0),
        (0, 1, 1),
        (0, 1, 0),
        (1, 0, 1),
        (0, 0, 1),
        (1, 1, 0),
    ]
    if set(states) != set(admissible):
        raise ValueError("3D admissible filter no longer matches the canonical 6-state core.")
    labels = ["100", "011", "010", "101", "001", "110"]
    index = {state: i for i, state in enumerate(states)}

    complement = {}
    for i, state in enumerate(states):
        comp = tuple(1 - bit for bit in state)
        complement[i] = index[comp]

    # Primitive graph: admissible one-bit flips.
    A_prim = np.zeros((6, 6), dtype=int)
    for i, state in enumerate(states):
        for axis in range(3):
            nxt = list(state)
            nxt[axis] = 1 - nxt[axis]
            nxt = tuple(nxt)
            if nxt in index:
                A_prim[i, index[nxt]] = 1

    # Residual graph: all pairs except complements.
    A_res = np.zeros((6, 6), dtype=int)
    for i in range(6):
        for j in range(6):
            if i != j and j != complement[i]:
                A_res[i, j] = 1

    # Cycle order that makes A_prim identical to the standard C_6 adjacency.
    cycle_order = [0, 5, 2, 1, 4, 3]  # 100 -> 110 -> 010 -> 011 -> 001 -> 101 -> 100

    return {
        "raw_states": raw_states,
        "removed_states": removed,
        "states": states,
        "labels": labels,
        "index": index,
        "complement": complement,
        "A_prim": A_prim,
        "A_res": A_res,
        "cycle_order": cycle_order,
    }


def build_C6():
    n = 6
    A = np.zeros((n, n), dtype=int)
    for i in range(n):
        j = (i + 1) % n
        A[i, j] = A[j, i] = 1
    return A, "C_6"


def build_K222():
    n = 6
    A = np.zeros((n, n), dtype=int)
    parts = [{0, 1}, {2, 3}, {4, 5}]
    for i in range(n):
        for j in range(i + 1, n):
            same_part = any(i in part and j in part for part in parts)
            if not same_part:
                A[i, j] = A[j, i] = 1
    return A, "K(2,2,2)", parts


def build_residual_graph_n(n):
    raw_states, admissible, removed = build_admissible_states_by_filter(n)
    data = build_noncomplement_graph_on_states(admissible)

    return {
        "n": n,
        "raw_states": raw_states,
        "removed_states": removed,
        "states": data["states"],
        "labels": data["labels"],
        "complement": data["complement"],
        "A_res": data["A_res"],
    }


def build_complete_multipartite(part_sizes):
    n = sum(part_sizes)
    A = np.zeros((n, n), dtype=int)
    start = 0
    parts = []
    for size in part_sizes:
        part = list(range(start, start + size))
        parts.append(part)
        start += size
    for i in range(n):
        for j in range(i + 1, n):
            same_part = any(i in part and j in part for part in parts)
            if not same_part:
                A[i, j] = A[j, i] = 1
    return A, parts


def build_axis_transport_model(rank):
    """
    Abstract flag-free axis-transport model of rank `rank`.

    Vertices are ordered by complement pairs:
    +1,-1,+2,-2,...,+rank,-rank.
    Residual adjacency connects all vertices from different axes and no
    vertices inside the same complement pair.
    """
    labels = []
    for axis in range(1, rank + 1):
        labels.extend([f"+{axis}", f"-{axis}"])

    n = 2 * rank
    complement = {}
    for axis in range(rank):
        i = 2 * axis
        complement[i] = i + 1
        complement[i + 1] = i

    A_res = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(i + 1, n):
            if complement[i] != j:
                A_res[i, j] = A_res[j, i] = 1

    parts = [{2 * axis, 2 * axis + 1} for axis in range(rank)]
    return {
        "rank": rank,
        "labels": labels,
        "complement": complement,
        "A_res": A_res,
        "parts": parts,
    }


def build_Q3():
    vertices = list(product([0, 1], repeat=3))
    A = np.zeros((8, 8), dtype=int)
    for i, v in enumerate(vertices):
        for j, u in enumerate(vertices):
            if i < j and sum(a != b for a, b in zip(v, u)) == 1:
                A[i, j] = A[j, i] = 1
    return A, "Q_3", vertices


def hamming_distance(u, v):
    return sum(a != b for a, b in zip(u, v))


def permute_adjacency(A, order):
    P = np.eye(A.shape[0], dtype=int)[order]
    return P @ A @ P.T


def graph_isomorphic(A, B):
    """Brute-force graph isomorphism for very small graphs."""
    if A.shape != B.shape:
        return False
    n = A.shape[0]
    if np.sum(A, axis=0).tolist() != np.sum(B, axis=0).tolist():
        return False
    for perm in permutations(range(n)):
        P = np.eye(n, dtype=int)[list(perm)]
        if np.array_equal(P @ A @ P.T, B):
            return True
    return False


def minimal_active_carrier_test():
    print("\n[Тест] Минимальность и единственность шестисостояного носителя")
    print("-" * 50)

    checked_ranks = [3, 4, 5, 6]
    lower_bound_ok = True
    minimality_ok = True
    residual_ok = True

    for rank in checked_ranks:
        model = build_axis_transport_model(rank)
        n_vertices = len(model["labels"])
        lower_bound_ok = lower_bound_ok and (n_vertices == 2 * rank) and (n_vertices >= 6)
        minimality_ok = minimality_ok and ((n_vertices == 6) == (rank == 3))
        if rank == 3:
            A_k222, _, _ = build_K222()
            residual_ok = residual_ok and np.array_equal(model["A_res"], A_k222)

    model3 = build_axis_transport_model(3)
    A_res = model3["A_res"]
    A_c6, _ = build_C6()

    edges = [(i, j) for i in range(6) for j in range(i + 1, 6) if A_res[i, j] == 1]
    cycle_like_count = 0
    all_cycle_like_are_c6 = True

    from itertools import combinations

    for edge_subset in combinations(edges, 6):
        A = np.zeros((6, 6), dtype=int)
        for i, j in edge_subset:
            A[i, j] = A[j, i] = 1
        degrees = np.sum(A, axis=1)
        if not np.all(degrees == 2):
            continue
        if len(connected_components(A)) != 1:
            continue
        cycle_like_count += 1
        all_cycle_like_are_c6 = all_cycle_like_are_c6 and graph_isomorphic(A, A_c6)

    core = build_admissible_core()
    canonical_realization_ok = np.array_equal(core["A_res"], A_res)
    canonical_process_ok = np.array_equal(
        permute_adjacency(core["A_prim"], core["cycle_order"]),
        A_c6,
    )

    print(f"  Проверенные ранги осей: {checked_ranks}")
    print(f"  Нижняя граница |V| = 2m >= 6: {'✓' if lower_bound_ok else '✗'}")
    print(f"  Минимальный случай возникает ровно при m=3: {'✓' if minimality_ok else '✗'}")
    print(f"  Остаточный граф минимального случая = K(2,2,2): {'✓' if residual_ok else '✗'}")
    print(f"  Число связных 2-регулярных остовных подграфов в K(2,2,2): {cycle_like_count}")
    print(f"  Любой такой подграф изоморфен C_6: {'✓' if all_cycle_like_are_c6 else '✗'}")
    print(f"  Канонический трёхбитовый носитель реализует абстрактную минимальную модель: {'✓' if canonical_realization_ok else '✗'}")
    print(f"  Канонический циклический процесс лежит в этом классе моделей: {'✓' if canonical_process_ok else '✗'}")

    overall = (
        lower_bound_ok
        and minimality_ok
        and residual_ok
        and cycle_like_count > 0
        and all_cycle_like_are_c6
        and canonical_realization_ok
        and canonical_process_ok
    )
    print(f"  Результат: {'[Д|К] ПРОЙДЕН' if overall else '✗ НЕСОВПАДЕНИЕ'}")

    return {
        "checked_ranks": checked_ranks,
        "lower_bound_ok": lower_bound_ok,
        "minimality_ok": minimality_ok,
        "residual_ok": residual_ok,
        "cycle_like_count": cycle_like_count,
        "all_cycle_like_are_c6": all_cycle_like_are_c6,
        "canonical_realization_ok": canonical_realization_ok,
        "canonical_process_ok": canonical_process_ok,
        "status": "[Д|К]",
        "passed": overall,
    }


def precore_binary_layer_test():
    print("\n[Тест] Доядерный бинарный слой F_2^1 / F_2^2")
    print("-" * 50)

    dipole = build_raw_cube_states(1)
    binary = build_binary_precore_graphs()
    states = binary["states"]
    labels = binary["labels"]
    c4 = binary["C4"]
    two_k2 = binary["2K2"]
    k4_minus_e = binary["K4_minus_e"]
    k4 = binary["K4"]
    simplex_sector = binary["simplex_sector"]

    dipole_ok = dipole == [(0,), (1,)]
    state_count_ok = len(states) == 4
    manifest_ok = np.all(c4.sum(axis=1) == 2)
    opposition_ok = np.array_equal(two_k2.sum(axis=1), np.ones(4, dtype=int))
    partial_ok = int(np.sum(k4_minus_e) // 2) == 5
    closure_ok = int(np.sum(k4) // 2) == 6
    simplex_triangle_ok = np.array_equal(
        k4[np.ix_(simplex_sector, simplex_sector)],
        np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]], dtype=int),
    )

    q3_states = list(product([0, 1], repeat=3))
    q3_index = {state: i for i, state in enumerate(q3_states)}
    face_states = [(0,) + state for state in states]
    face_indices = [q3_index[state] for state in face_states]
    A_q3, _, _ = build_Q3()
    face_graph = A_q3[np.ix_(face_indices, face_indices)]
    face_ok = np.array_equal(face_graph, c4)

    edge_list = [(i, j) for i in range(8) for j in range(i + 1, 8) if A_q3[i, j] == 1]
    edge_index = {edge: k for k, edge in enumerate(edge_list)}
    line_graph = np.zeros((len(edge_list), len(edge_list)), dtype=int)
    for i, (a, b) in enumerate(edge_list):
        for j in range(i + 1, len(edge_list)):
            c, d = edge_list[j]
            if len({a, b, c, d}) < 4:
                line_graph[i, j] = line_graph[j, i] = 1

    face_state_set = set(face_indices)
    face_edges = [
        edge_index[edge]
        for edge in edge_list
        if edge[0] in face_state_set and edge[1] in face_state_set
    ]
    line_face_graph = line_graph[np.ix_(face_edges, face_edges)]
    line_face_ok = np.array_equal(line_face_graph, c4)

    print(f"  F_2^1 = {{0,1}}: {'✓' if dipole_ok else '✗'}")
    print(f"  F_2^2 имеет 4 состояния: {'✓' if state_count_ok else '✗'} -> {labels}")
    print(f"  Циклическое чтение = C_4: {'✓' if manifest_ok else '✗'}")
    print(f"  Чтение комплементарных пар = 2K_2: {'✓' if opposition_ok else '✗'}")
    print(f"  Неполное замыкание = K_4-e: {'✓' if partial_ok else '✗'}")
    print(f"  Полное графовое замыкание = K_4: {'✓' if closure_ok else '✗'}")
    print(f"  Симплексный сектор {{01,10,11}} как K_3 в полном замыкании: {'✓' if simplex_triangle_ok else '✗'}")
    print(f"  Локальное вложение F_2^2 -> грань Q_3 даёт C_4: {'✓' if face_ok else '✗'}")
    print(f"  Та же грань в L(Q_3) даёт C_4: {'✓' if line_face_ok else '✗'}")

    overall = (
        dipole_ok
        and state_count_ok
        and manifest_ok
        and opposition_ok
        and partial_ok
        and closure_ok
        and simplex_triangle_ok
        and face_ok
        and line_face_ok
    )
    print(f"  Результат: {'[Д|К] ПРОЙДЕН' if overall else '✗ НЕСОВПАДЕНИЕ'}")

    return {
        "labels": labels,
        "status": "[Д|К]",
        "passed": overall,
    }


def combinatorial_core_test():
    print("\n[Тест] Строгое 3-битное ядро")
    print("-" * 50)

    core = build_admissible_core()
    raw_states = core["raw_states"]
    removed_states = core["removed_states"]
    states = core["states"]
    labels = core["labels"]
    complement = core["complement"]
    A_prim = core["A_prim"]
    A_res = core["A_res"]
    cycle_order = core["cycle_order"]

    print(f"  Сырые состояния: {len(raw_states)}")
    print(f"  Удалённые состояния: {[ ''.join(map(str, s)) for s in removed_states ]}")
    print(f"  Допустимые состояния: {labels}")

    weights = [sum(state) for state in states]
    class_1 = [labels[i] for i, w in enumerate(weights) if w == 1]
    class_2 = [labels[i] for i, w in enumerate(weights) if w == 2]
    print(f"  Класс веса 1: {class_1}")
    print(f"  Класс веса 2: {class_2}")

    complement_pairs = sorted(
        (labels[i], labels[j]) for i, j in complement.items() if i < j
    )
    print(f"  Комплементарные пары: {complement_pairs}")

    counts = {1: 0, 2: 0, 3: 0}
    for i in range(6):
        for j in range(i + 1, 6):
            counts[hamming_distance(states[i], states[j])] += 1
    print(f"  Разбиение пар по Хэммингу: {counts}")

    counts_ok = counts == {1: 6, 2: 6, 3: 3}

    # Primitive graph must be C_6 up to the stored cycle order.
    A_c6, _ = build_C6()
    A_prim_cycle = permute_adjacency(A_prim, cycle_order)
    primitive_ok = np.array_equal(A_prim_cycle, A_c6)

    # Residual graph must be exactly K(2,2,2) in the canonical order.
    A_k222, _, _ = build_K222()
    residual_ok = np.array_equal(A_res, A_k222)

    print(f"  Циклическое отношение R1 = C_6: {'✓' if primitive_ok else '✗'}")
    print(f"  Остаточный граф R1 ∪ R2 = K(2,2,2): {'✓' if residual_ok else '✗'}")

    overall = counts_ok and primitive_ok and residual_ok
    print(f"  Результат: {'[Д] ПРОЙДЕН' if overall else '✗ НЕСОВПАДЕНИЕ'}")

    return {
        "pair_counts_ok": counts_ok,
        "primitive_ok": primitive_ok,
        "residual_ok": residual_ok,
        "passed": overall,
    }


def relation_scheme_test():
    print("\n[Тест] Каноническая схема отношений на X_adm")
    print("-" * 50)

    core = build_admissible_core()
    states = core["states"]
    labels = core["labels"]
    A_prim = core["A_prim"]
    A_res = core["A_res"]
    complement = core["complement"]

    A_r1 = np.zeros((6, 6), dtype=int)
    A_r2 = np.zeros((6, 6), dtype=int)
    A_r3 = np.zeros((6, 6), dtype=int)

    for i in range(6):
        for j in range(i + 1, 6):
            dist = hamming_distance(states[i], states[j])
            if dist == 1:
                A_r1[i, j] = A_r1[j, i] = 1
            elif dist == 2:
                A_r2[i, j] = A_r2[j, i] = 1
            elif dist == 3:
                A_r3[i, j] = A_r3[j, i] = 1

    r1_ok = np.array_equal(A_r1, A_prim)

    expected_r2 = np.zeros((6, 6), dtype=int)
    for tri in ([0, 2, 4], [1, 3, 5]):
        for a in range(3):
            for b in range(a + 1, 3):
                i, j = tri[a], tri[b]
                expected_r2[i, j] = expected_r2[j, i] = 1
    r2_ok = np.array_equal(A_r2, expected_r2)

    expected_r3 = np.zeros((6, 6), dtype=int)
    for i, j in complement.items():
        expected_r3[i, j] = 1
    r3_ok = np.array_equal(A_r3, expected_r3)

    residual_decomp_ok = np.array_equal(A_res, A_r1 + A_r2)
    complete_decomp_ok = np.array_equal(
        np.ones((6, 6), dtype=int) - np.eye(6, dtype=int),
        A_r1 + A_r2 + A_r3,
    )

    spectrum_r2_ok = np.allclose(
        eigh_sorted(laplacian(A_r2))[0],
        np.array([0, 0, 3, 3, 3, 3], dtype=float),
        atol=TOL,
    )
    spectrum_r3_ok = np.allclose(
        eigh_sorted(laplacian(A_r3))[0],
        np.array([0, 0, 0, 2, 2, 2], dtype=float),
        atol=TOL,
    )

    class1 = [0, 2, 4]
    class2 = [1, 3, 5]

    def quotient_matrix(A, partition):
        q = np.zeros((len(partition), len(partition)), dtype=int)
        for i, block_i in enumerate(partition):
            base = block_i[0]
            for j, block_j in enumerate(partition):
                q[i, j] = int(np.sum(A[base, block_j]))
        return q

    partition = [class1, class2]
    q_r1 = quotient_matrix(A_r1, partition)
    q_r2 = quotient_matrix(A_r2, partition)
    q_r3 = quotient_matrix(A_r3, partition)
    q_res = quotient_matrix(A_res, partition)

    q_r1_ok = np.array_equal(q_r1, np.array([[0, 2], [2, 0]], dtype=int))
    q_r2_ok = np.array_equal(q_r2, np.array([[2, 0], [0, 2]], dtype=int))
    q_r3_ok = np.array_equal(q_r3, np.array([[0, 1], [1, 0]], dtype=int))
    q_res_ok = np.array_equal(q_res, np.array([[2, 2], [2, 2]], dtype=int))

    r3_pairs = sorted((labels[i], labels[j]) for i in range(6) for j in range(i + 1, 6) if A_r3[i, j] == 1)
    print(f"  R1 = граф расстояния 1 = C_6: {'✓' if r1_ok else '✗'}")
    print(f"  R2 = граф расстояния 2 = K_3 ⊔ K_3: {'✓' if r2_ok else '✗'}")
    print(f"  R3 = граф расстояния 3 = 3K_2: {'✓' if r3_ok else '✗'}")
    print(f"  Комплементарные оси R3: {r3_pairs}")
    print(f"  A_res = R1 ∪ R2: {'✓' if residual_decomp_ok else '✗'}")
    print(f"  K_6 = R1 ⊔ R2 ⊔ R3: {'✓' if complete_decomp_ok else '✗'}")
    print(f"  Quot(R1) = [[0,2],[2,0]]: {'✓' if q_r1_ok else '✗'}")
    print(f"  Quot(R2) = [[2,0],[0,2]]: {'✓' if q_r2_ok else '✗'}")
    print(f"  Quot(R3) = [[0,1],[1,0]]: {'✓' if q_r3_ok else '✗'}")
    print(f"  Quot(A_res) = [[2,2],[2,2]]: {'✓' if q_res_ok else '✗'}")
    print(f"  Spec(L(R2)) = {{0,0,3,3,3,3}}: {'✓' if spectrum_r2_ok else '✗'}")
    print(f"  Spec(L(R3)) = {{0,0,0,2,2,2}}: {'✓' if spectrum_r3_ok else '✗'}")

    overall = (
        r1_ok and r2_ok and r3_ok and residual_decomp_ok
        and complete_decomp_ok and q_r1_ok and q_r2_ok and q_r3_ok
        and q_res_ok and spectrum_r2_ok and spectrum_r3_ok
    )
    print(f"  Результат: {'[Д] ПРОЙДЕН' if overall else '✗ НЕСОВПАДЕНИЕ'}")

    return {
        "r1_ok": r1_ok,
        "r2_ok": r2_ok,
        "r3_ok": r3_ok,
        "residual_decomp_ok": residual_decomp_ok,
        "complete_decomp_ok": complete_decomp_ok,
        "passed": overall,
    }


def shell_face_kuhn_transition_test():
    print("\n[Тест] Грамматика граней оболочки и секторы Куна")
    print("-" * 50)

    axes = {
        "A": {"+": "100", "-": "011"},
        "B": {"+": "010", "-": "101"},
        "C": {"+": "001", "-": "110"},
    }
    triad_plus = {"100", "010", "001"}
    triad_minus = {"011", "101", "110"}
    kuhn_edges = {
        tuple(sorted(("100", "110"))),
        tuple(sorted(("110", "010"))),
        tuple(sorted(("010", "011"))),
        tuple(sorted(("011", "001"))),
        tuple(sorted(("001", "101"))),
        tuple(sorted(("101", "100"))),
    }

    def face(signs):
        sa, sb, sc = signs
        return (axes["A"][sa], axes["B"][sb], axes["C"][sc])

    def edge_type(a, b):
        d = hamming_distance(a, b)
        if d == 1:
            return "R1"
        if d == 2:
            return "R2"
        if d == 3:
            return "R3"
        raise ValueError(f"Unexpected Hamming distance for {a}, {b}: {d}")

    def edge_signature(face_vertices):
        a, b, c = face_vertices
        counts = {"R1": 0, "R2": 0, "R3": 0}
        for x, y in ((a, b), (a, c), (b, c)):
            counts[edge_type(x, y)] += 1
        return counts

    def classify_face(face_vertices):
        face_set = set(face_vertices)
        if face_set == triad_plus:
            return "pure_plus"
        if face_set == triad_minus:
            return "pure_minus"
        return "transition"

    faces = [face(signs) for signs in product("+-", repeat=3)]
    faces_ok = len(faces) == 8 and len({tuple(sorted(f)) for f in faces}) == 8

    pure_faces = []
    transition_faces = []
    for f in faces:
        kind = classify_face(f)
        sig = edge_signature(f)
        if kind.startswith("pure"):
            pure_faces.append((f, sig))
        else:
            transition_faces.append((f, sig))

    pure_faces_ok = len(pure_faces) == 2 and {
        frozenset(f) for f, _ in pure_faces
    } == {frozenset(triad_plus), frozenset(triad_minus)}
    pure_signatures_ok = all(sig == {"R1": 0, "R2": 3, "R3": 0} for _, sig in pure_faces)
    transition_faces_ok = len(transition_faces) == 6
    transition_signatures_ok = all(
        sig == {"R1": 2, "R2": 1, "R3": 0} for _, sig in transition_faces
    )

    chambers = [("000*",) + f for f in faces]
    chamber_count_ok = len(chambers) == 8
    pure_chambers = [("000*",) + f for f, _ in pure_faces]
    pure_chambers_ok = len(pure_chambers) == 2

    host_count = {edge: 0 for edge in kuhn_edges}
    all_r1_edges = set()
    for f, _ in transition_faces:
        edges_r1 = []
        vs = list(f)
        for i in range(3):
            for j in range(i + 1, 3):
                e = tuple(sorted((vs[i], vs[j])))
                if hamming_distance(*e) == 1:
                    edges_r1.append(e)
        if len(edges_r1) != 2:
            transition_signatures_ok = False
        for e in edges_r1:
            if e not in kuhn_edges:
                transition_signatures_ok = False
            else:
                all_r1_edges.add(e)
                host_count[e] += 1

    kuhn_edge_cover_ok = all_r1_edges == kuhn_edges
    kuhn_host_ok = all(count == 2 for count in host_count.values())

    print(f"  8 конфигураций граней: {'✓' if faces_ok else '✗'}")
    print(f"  2 чистые триадные грани: {'✓' if pure_faces_ok else '✗'}")
    print(f"  Сигнатура чистой грани = 3*R2: {'✓' if pure_signatures_ok else '✗'}")
    print(f"  6 переходных граней: {'✓' if transition_faces_ok else '✗'}")
    print(f"  Сигнатура переходной грани = 2*R1 + 1*R2: {'✓' if transition_signatures_ok else '✗'}")
    print(f"  8 тетраэдральных камер оболочки: {'✓' if chamber_count_ok else '✗'}")
    print(f"  2 чистые триадные камеры: {'✓' if pure_chambers_ok else '✗'}")
    print(f"  6 рёбер Куна покрываются переходными гранями: {'✓' if kuhn_edge_cover_ok else '✗'}")
    print(f"  Каждое ребро Куна входит ровно в две переходные грани: {'✓' if kuhn_host_ok else '✗'}")

    overall = (
        faces_ok and pure_faces_ok and pure_signatures_ok and transition_faces_ok
        and transition_signatures_ok and chamber_count_ok and pure_chambers_ok
        and kuhn_edge_cover_ok and kuhn_host_ok
    )
    print(f"  Результат: {'[Д] ПРОЙДЕН' if overall else '✗ НЕСОВПАДЕНИЕ'}")

    return {
        "faces_ok": faces_ok,
        "pure_faces_ok": pure_faces_ok,
        "transition_faces_ok": transition_faces_ok,
        "kuhn_edge_cover_ok": kuhn_edge_cover_ok,
        "kuhn_host_ok": kuhn_host_ok,
        "passed": overall,
    }


def compute_core_bridge_signature():
    """
    Finite AMR-facing signature exported by the three-bit relation core.

    The AMR layer should read this signature from the core verifier itself,
    rather than reconstructing it independently.
    """
    bridge = compute_sl2_sigma_core_signature()

    return {
        "relation_counts": bridge["relation_counts"],
        "chamber_support": bridge["chamber_support"],
        "shell_types": bridge["shell_types"],
        "primitive_ok": bridge["primitive_ok"],
        "residual_decomp_ok": bridge["residual_decomp_ok"],
    }


def restrict_to_core_order(matrix):
    raw_states = build_raw_cube_states(3)
    state_to_idx = {state: i for i, state in enumerate(raw_states)}
    core = build_admissible_core()
    admissible_idx = [state_to_idx[state] for state in core["states"]]
    return matrix[np.ix_(admissible_idx, admissible_idx)]


def edge_pairs_from_adjacency(adjacency):
    return [
        (i, j)
        for i in range(adjacency.shape[0])
        for j in range(i + 1, adjacency.shape[0])
        if adjacency[i, j]
    ]


def build_clique_incidence_from_R3(A_R3):
    parts = []
    used = set()
    for i in range(A_R3.shape[0]):
        if i in used:
            continue
        for j in range(i + 1, A_R3.shape[1]):
            if A_R3[i, j] == 1:
                parts.append((i, j))
                used.add(i)
                used.add(j)
                break

    cliques = list(product(*parts))
    B = np.zeros((A_R3.shape[0], len(cliques)), dtype=int)
    for ci, clique in enumerate(cliques):
        for vi in clique:
            B[vi, ci] = 1
    return B


def compute_sl2_sigma_core_signature():
    """
    Exact operator-to-core interface for n=3.

    It reconstructs R1, R2, R3 from the sl2/aperture layer and then recovers
    the finite relation-core signature through clique incidence of K(2,2,2).
    """
    projectors, E, F, H, C, A_q3 = build_aperture_transition_operators(3)
    core = build_admissible_core()
    A_prim = core["A_prim"]
    A_res = core["A_res"]

    P = projectors[1] + projectors[2]
    A1_full = P @ (E + F) @ P
    A3_full = P @ C @ P
    A2_full = A1_full @ A1_full - 2 * P

    A1 = restrict_to_core_order(A1_full).astype(int)
    A2 = restrict_to_core_order(A2_full).astype(int)
    A3 = restrict_to_core_order(A3_full).astype(int)

    relation_matrices = {"R1": A1, "R2": A2, "R3": A3}
    relation_edges = {
        name: edge_pairs_from_adjacency(adj) for name, adj in relation_matrices.items()
    }
    relation_counts = {name: len(pairs) for name, pairs in relation_edges.items()}

    Pi1 = restrict_to_core_order(projectors[1]).astype(int)
    Pi2 = restrict_to_core_order(projectors[2]).astype(int)
    shell_types = {}
    for name, adj in relation_matrices.items():
        diag_mass = int(np.sum(np.abs(Pi1 @ adj @ Pi1)) + np.sum(np.abs(Pi2 @ adj @ Pi2)))
        offdiag_mass = int(np.sum(np.abs(Pi1 @ adj @ Pi2)) + np.sum(np.abs(Pi2 @ adj @ Pi1)))
        if name == "R2":
            shell_types[name] = "within" if offdiag_mass == 0 else "mixed"
        elif diag_mass == 0 and name == "R3":
            shell_types[name] = "axial"
        elif diag_mass == 0:
            shell_types[name] = "between"
        else:
            shell_types[name] = "mixed"

    B_clique = build_clique_incidence_from_R3(A3)
    BBt = B_clique @ B_clique.T
    chamber_support = {}
    for name, pairs in relation_edges.items():
        chamber_support[name] = sorted({int(BBt[i, j]) for i, j in pairs})[0]

    B_geom, _ = build_incidence_matrix()
    geom_cols = {tuple(B_geom[:, j]) for j in range(B_geom.shape[1])}
    clique_cols = {tuple(B_clique[:, j]) for j in range(B_clique.shape[1])}

    return {
        "P_rank": int(round(np.trace(P))),
        "relation_matrices": relation_matrices,
        "relation_counts": relation_counts,
        "chamber_support": chamber_support,
        "shell_types": shell_types,
        "primitive_ok": np.array_equal(A_prim, A1),
        "residual_decomp_ok": np.array_equal(A_res, A1 + A2),
        "clique_B_matches_geometric": clique_cols == geom_cols,
        "BBt_formula_ok": np.array_equal(BBt, 4 * np.eye(6, dtype=int) + 2 * (A1 + A2)),
    }


def core_bridge_signature_test():
    print("\n[Тест] Конечная сигнатура отношенческого ядра и внешний интерфейс")
    print("-" * 50)

    signature = compute_core_bridge_signature()
    relation_counts = signature["relation_counts"]
    chamber_support = signature["chamber_support"]
    shell_types = signature["shell_types"]

    counts_ok = relation_counts == {"R1": 6, "R2": 6, "R3": 3}
    chambers_ok = chamber_support == {"R1": 2, "R2": 2, "R3": 0}
    shells_ok = shell_types == {"R1": "between", "R2": "within", "R3": "axial"}
    supported_pair_ok = (
        relation_counts["R1"] == relation_counts["R2"] == 6
        and chamber_support["R1"] == chamber_support["R2"] == 2
        and shell_types["R1"] == "between"
        and shell_types["R2"] == "within"
    )
    axial_block_ok = (
        relation_counts["R3"] == 3
        and chamber_support["R3"] == 0
        and shell_types["R3"] == "axial"
    )

    overall = (
        counts_ok
        and chambers_ok
        and shells_ok
        and signature["primitive_ok"]
        and signature["residual_decomp_ok"]
        and supported_pair_ok
        and axial_block_ok
    )

    print(f"  relation_counts : {relation_counts}")
    print(f"  chamber_support : {chamber_support}")
    print(f"  shell_types     : {shell_types}")
    print(f"  A_prim = R1     : {'✓' if signature['primitive_ok'] else '✗'}")
    print(f"  A_res = R1 + R2 : {'✓' if signature['residual_decomp_ok'] else '✗'}")
    print(f"  balanced pair   : {'✓' if supported_pair_ok else '✗'}")
    print(f"  axial layer     : {'✓' if axial_block_ok else '✗'}")
    print(f"  Результат: {'[Д] ПРОЙДЕН' if overall else '✗ НЕСОВПАДЕНИЕ'}")

    return {
        "counts_ok": counts_ok,
        "chambers_ok": chambers_ok,
        "shells_ok": shells_ok,
        "supported_pair_ok": supported_pair_ok,
        "axial_block_ok": axial_block_ok,
        "status": "[Д]",
        "passed": overall,
    }


def sl2_sigma_core_bridge_test():
    print("\n[Тест] Операторно-комбинаторный интерфейс sl2 -> Sigma_core")
    print("-" * 50)

    bridge = compute_sl2_sigma_core_signature()
    counts_ok = bridge["relation_counts"] == {"R1": 6, "R2": 6, "R3": 3}
    chambers_ok = bridge["chamber_support"] == {"R1": 2, "R2": 2, "R3": 0}
    shells_ok = bridge["shell_types"] == {
        "R1": "between",
        "R2": "within",
        "R3": "axial",
    }
    rank_ok = bridge["P_rank"] == 6
    clique_ok = bridge["clique_B_matches_geometric"]
    bbt_ok = bridge["BBt_formula_ok"]
    overall = (
        rank_ok
        and counts_ok
        and chambers_ok
        and shells_ok
        and bridge["primitive_ok"]
        and bridge["residual_decomp_ok"]
        and clique_ok
        and bbt_ok
    )

    print(f"  rank(P)=6       : {'✓' if rank_ok else '✗'}")
    print(f"  relation_counts : {bridge['relation_counts']}")
    print(f"  chamber_support : {bridge['chamber_support']}")
    print(f"  shell_types     : {bridge['shell_types']}")
    print(f"  A_R1 = P(E+F)P  : {'✓' if bridge['primitive_ok'] else '✗'}")
    print(f"  A_R1+A_R2=A_res : {'✓' if bridge['residual_decomp_ok'] else '✗'}")
    print(f"  B from cliques  : {'✓' if clique_ok else '✗'}")
    print(f"  BB^T law        : {'✓' if bbt_ok else '✗'}")
    print(f"  Результат: {'[Д|alg] ПРОЙДЕН' if overall else '✗ НЕСОВПАДЕНИЕ'}")

    return {
        "rank_ok": rank_ok,
        "counts_ok": counts_ok,
        "chambers_ok": chambers_ok,
        "shells_ok": shells_ok,
        "clique_ok": clique_ok,
        "bbt_ok": bbt_ok,
        "status": "[Д|alg]",
        "passed": overall,
    }


def relation_algebra_test():
    print("\n[Тест] Алгебра отношений на X_adm")
    print("-" * 50)

    core = build_admissible_core()
    states = core["states"]

    A = {0: np.eye(6, dtype=int), 1: np.zeros((6, 6), dtype=int), 2: np.zeros((6, 6), dtype=int), 3: np.zeros((6, 6), dtype=int)}
    for i in range(6):
        for j in range(6):
            if i == j:
                continue
            d = hamming_distance(states[i], states[j])
            A[d][i, j] = 1

    sum_ok = np.array_equal(A[0] + A[1] + A[2] + A[3], np.ones((6, 6), dtype=int))
    symm_ok = all(np.array_equal(A[k], A[k].T) for k in range(4))
    valencies_ok = (
        np.all(A[1].sum(axis=1) == 2)
        and np.all(A[2].sum(axis=1) == 2)
        and np.all(A[3].sum(axis=1) == 1)
    )

    mult_ok = (
        np.array_equal(A[1] @ A[1], 2 * A[0] + A[2])
        and np.array_equal(A[2] @ A[2], 2 * A[0] + A[2])
        and np.array_equal(A[3] @ A[3], A[0])
        and np.array_equal(A[1] @ A[2], A[1] + 2 * A[3])
        and np.array_equal(A[2] @ A[1], A[1] + 2 * A[3])
        and np.array_equal(A[1] @ A[3], A[2])
        and np.array_equal(A[3] @ A[1], A[2])
        and np.array_equal(A[2] @ A[3], A[1])
        and np.array_equal(A[3] @ A[2], A[1])
    )

    intersection_ok = True
    for i in (1, 2, 3):
        for j in (1, 2, 3):
            for k in (0, 1, 2, 3):
                values = set()
                for x in range(6):
                    for y in range(6):
                        if A[k][x, y] == 1:
                            c = int(sum(A[i][x, z] * A[j][z, y] for z in range(6)))
                            values.add(c)
                if len(values) != 1:
                    intersection_ok = False

    print(f"  A0+A1+A2+A3 = J: {'✓' if sum_ok else '✗'}")
    print(f"  Симметричность отношений: {'✓' if symm_ok else '✗'}")
    print(f"  Валентности (2,2,1): {'✓' if valencies_ok else '✗'}")
    print(f"  Замкнутость алгебры отношений: {'✓' if mult_ok else '✗'}")
    print(f"  Постоянство intersection numbers: {'✓' if intersection_ok else '✗'}")

    overall = sum_ok and symm_ok and valencies_ok and mult_ok and intersection_ok
    print(f"  Результат: {'[Д] ПРОЙДЕН' if overall else '✗ НЕСОВПАДЕНИЕ'}")

    return {
        "sum_ok": sum_ok,
        "symm_ok": symm_ok,
        "valencies_ok": valencies_ok,
        "mult_ok": mult_ok,
        "intersection_ok": intersection_ok,
        "passed": overall,
    }


def higher_4d_graph_test():
    print("\n[Тест] 4D-графовый слой без смешения множеств вершин")
    print("-" * 50)

    data = build_residual_graph_n(4)
    labels = data["labels"]
    A_res = data["A_res"]

    expected_graph, parts = build_complete_multipartite([2, 2, 2, 2])
    graph_ok = np.array_equal(A_res, expected_graph)

    eigenvalues, _ = eigh_sorted(laplacian(A_res))
    expected_spectrum = np.array([0, 6, 6, 6, 6, 8, 8, 8], dtype=float)
    spectrum_ok = np.allclose(eigenvalues, expected_spectrum, atol=1e-8)

    induced = A_res[:6, :6]
    expected_k222, _, _ = build_K222()
    reduction_ok = np.array_equal(induced, expected_k222)

    print(f"  Полный 4D-куб: {len(data['raw_states'])} вершин")
    print(f"  Допустимое множество V4: {len(data['states'])} вершин")
    print(f"  Удалённые вершины: {len(data['removed_states'])}")
    print(f"  V4 = {labels}")
    print(f"  Остаточный граф = K(2,2,2,2): {'✓' if graph_ok else '✗'}")
    print(f"  Спектр L(V4): {np.round(eigenvalues, 6)}")
    print(f"  Спектр совпал: {'✓' if spectrum_ok else '✗'}")
    print(f"  Удаление одной комплементарной пары даёт K(2,2,2): {'✓' if reduction_ok else '✗'}")

    overall = graph_ok and spectrum_ok and reduction_ok
    print(f"  Результат: {'[Д] ПРОЙДЕН' if overall else '✗ НЕСОВПАДЕНИЕ'}")

    return {
        "graph_ok": graph_ok,
        "spectrum_ok": spectrum_ok,
        "reduction_ok": reduction_ok,
        "passed": overall,
    }


def hamming_shell_ladder_test_4d():
    print("\n[Тест] 4D-лестница оболочек без смешения слоёв")
    print("-" * 50)

    shells = build_hamming_shells(4)
    counts = {k: len(v) for k, v in shells.items()}
    expected_counts = {k: comb(4, k) for k in range(5)}
    counts_ok = counts == expected_counts

    outer_shell = shells[1] + shells[3]
    equatorial_shell = shells[2]
    nontrivial_package = outer_shell + equatorial_shell

    outer_ok = len(outer_shell) == 8
    equatorial_ok = len(equatorial_shell) == 6
    package_ok = len(nontrivial_package) == 14

    admissible_labels = {
        "".join(str(bit) for bit in state)
        for state in build_residual_graph_n(4)["states"]
    }
    outer_labels = {
        "".join(str(bit) for bit in state)
        for state in outer_shell
    }
    identification_ok = admissible_labels == outer_labels

    print(f"  Размеры оболочек S_k^(4): {counts}")
    print(f"  Биномиальный закон: {'✓' if counts_ok else '✗'}")
    print(f"  Внешний слой S_1 ∪ S_3 имеет 8 вершин: {'✓' if outer_ok else '✗'}")
    print(f"  Экваториальный слой S_2 имеет 6 вершин: {'✓' if equatorial_ok else '✗'}")
    print(f"  Нетривиальный пакет U4 = S_1 ∪ S_2 ∪ S_3 имеет 14 вершин: {'✓' if package_ok else '✗'}")
    print(f"  Текущий носитель V4 совпадает с внешним слоем: {'✓' if identification_ok else '✗'}")

    overall = counts_ok and outer_ok and equatorial_ok and package_ok and identification_ok
    print(f"  Результат: {'[Д] ПРОЙДЕН' if overall else '✗ НЕСОВПАДЕНИЕ'}")

    return {
        "counts_ok": counts_ok,
        "outer_ok": outer_ok,
        "equatorial_ok": equatorial_ok,
        "package_ok": package_ok,
        "identification_ok": identification_ok,
        "passed": overall,
    }


def general_dimension_shell_law_test():
    print("\n[Тест] Общий n-мерный закон для V_n и U_n")
    print("-" * 50)

    all_ok = True
    checked_ns = [3, 4, 5, 6]

    for n in checked_ns:
        shells = build_hamming_shells(n)
        shell_counts = {k: len(v) for k, v in shells.items()}
        expected_counts = {k: comb(n, k) for k in range(n + 1)}
        counts_ok = shell_counts == expected_counts

        V_n = shells[1] + shells[n - 1]
        U_n = [state for k in range(1, n) for state in shells[k]]
        outer_ok = len(V_n) == 2 * n
        package_ok = len(U_n) == (2 ** n - 2)

        data = build_residual_graph_n(n)
        A_expected, parts = build_complete_multipartite([2] * n)
        graph_ok = np.array_equal(data["A_res"], A_expected)

        print(f"  n={n}: |V_n|={len(V_n)} (ожидалось {2*n}), |U_n|={len(U_n)} (ожидалось {2**n-2}), K_{{2,...,2}}: {'✓' if graph_ok else '✗'}")

        all_ok = all_ok and counts_ok and outer_ok and package_ok and graph_ok

    print(f"  Проверенные размерности: {checked_ns}")
    print(f"  Результат: {'[Д] ПРОЙДЕН' if all_ok else '✗ НЕСОВПАДЕНИЕ'}")

    return {
        "checked_ns": checked_ns,
        "passed": all_ok,
    }


# ============================================================================
# Geometry and incidence
# ============================================================================

def build_incidence_matrix():
    """
    Canonical pole ordering:
    0: D+, 1: D-, 2: F+, 3: F-, 4: C+, 5: C-
    Chambers are sign triples sigma in {±1}^3.
    """
    vertex_signs = [
        (+1, 0, 0),
        (-1, 0, 0),
        (0, +1, 0),
        (0, -1, 0),
        (0, 0, +1),
        (0, 0, -1),
    ]
    chamber_signs = list(product([-1, +1], repeat=3))

    B = np.zeros((6, 8), dtype=int)
    for v in range(6):
        for s, sigma in enumerate(chamber_signs):
            belongs = True
            for axis in range(3):
                pole_sign = vertex_signs[v][axis]
                if pole_sign != 0 and pole_sign != sigma[axis]:
                    belongs = False
                    break
            if belongs:
                B[v, s] = 1

    return B, chamber_signs


def build_Qn(n):
    vertices = list(product([0, 1], repeat=n))
    A = np.zeros((2 ** n, 2 ** n), dtype=int)
    for i in range(2 ** n):
        for j in range(i + 1, 2 ** n):
            if hamming_distance(vertices[i], vertices[j]) == 1:
                A[i, j] = A[j, i] = 1
    return A, vertices


def build_incidence_matrix_n(n):
    pole_data = []
    for axis in range(n):
        pole_data.append((axis, +1))
        pole_data.append((axis, -1))

    chamber_signs = list(product([-1, +1], repeat=n))
    B = np.zeros((2 * n, 2 ** n), dtype=int)
    for v, (axis, sign) in enumerate(pole_data):
        for s, sigma in enumerate(chamber_signs):
            if sigma[axis] == sign:
                B[v, s] = 1
    return B, pole_data, chamber_signs


def build_general_block_graph(n):
    A_cross, _ = build_complete_multipartite([2] * n)
    A_cube, cube_vertices = build_Qn(n)
    B, pole_data, chamber_signs = build_incidence_matrix_n(n)

    m = 2 * n + 2 ** n
    A_block = np.zeros((m, m), dtype=int)
    A_block[: 2 * n, : 2 * n] = A_cross
    A_block[2 * n :, 2 * n :] = A_cube
    A_block[: 2 * n, 2 * n :] = B
    A_block[2 * n :, : 2 * n] = B.T
    return A_block, A_cross, A_cube, B, pole_data, chamber_signs, cube_vertices


def expected_general_block_spectrum(n):
    a = 2 ** (n - 1) + n - 4
    delta = np.sqrt(a * a + 2 ** (n + 1))
    lambda_minus = 0.5 * (3 * n + 2 ** (n - 1) - delta)
    lambda_plus = 0.5 * (3 * n + 2 ** (n - 1) + delta)

    values = [0.0, float(n + 2 ** (n - 1))]
    values.extend([float(lambda_minus)] * n)
    values.extend([float(lambda_plus)] * n)
    for k in range(2, n + 1):
        values.extend([float(n + 2 * k)] * comb(n, k))
    values.extend([float(2 * n + 2 ** (n - 1))] * (n - 1))
    return np.array(sorted(values), dtype=float), float(lambda_minus), float(lambda_plus)


def build_block_graph():
    A_oct, _, _ = build_K222()
    A_cube, _, _ = build_Q3()
    B, chamber_signs = build_incidence_matrix()

    A_block = np.zeros((14, 14), dtype=int)
    A_block[:6, :6] = A_oct
    A_block[6:, 6:] = A_cube
    A_block[:6, 6:] = B
    A_block[6:, :6] = B.T
    return A_block, A_oct, A_cube, B, chamber_signs


# ============================================================================
# Spectral tests
# ============================================================================

def spectral_test(adjacency, name, expected_spectrum, expected_reff):
    print(f"\n[Тест] {name}")
    print("-" * 50)

    L = laplacian(adjacency)
    eigenvalues, _ = eigh_sorted(L)
    spec_ok = np.allclose(eigenvalues, np.array(expected_spectrum, dtype=float), atol=1e-8)

    lambda2_computed = float(eigenvalues[1])
    reff_computed = edge_resistance_mean(adjacency)
    reff_ok = abs(reff_computed - expected_reff) < 1e-8

    foster_ok, foster_sum, foster_expected = foster_theorem_check(adjacency)

    print(f"  Спектр L: {np.round(eigenvalues, 6)}")
    print(f"  λ₂: {lambda2_computed:.10f}")
    print(f"  Ср. R_eff(по рёбрам): {reff_computed:.10f}")
    print(f"  Теорема Фостера: {'✓' if foster_ok else '✗'} (ΣR_eff = {foster_sum:.6f}, ожидалось {foster_expected})")
    print(f"  Спектр совпал: {'✓' if spec_ok else '✗'}")
    print(f"  R_eff совпало: {'✓' if reff_ok else '✗'}")

    overall = spec_ok and reff_ok and foster_ok
    print(f"  Результат: {'[Д] ПРОЙДЕН' if overall else '✗ НЕСОВПАДЕНИЕ'}")

    return {
        "lambda2": lambda2_computed,
        "reff": reff_computed,
        "foster_ok": foster_ok,
        "spectrum_ok": spec_ok,
        "passed": overall,
    }


# ============================================================================
# Statistical illustration on the residual carrier
# ============================================================================

def markov_simulation_k222(n_steps=50000, burn_in=5000, seed=0):
    """
    Numerical illustration only.

    This function checks the statistical tail on K(2,2,2).
    It does not attempt to encode the topological Z_2 holonomy class, which
    belongs to the selected cycle test below.
    """
    print("\n[Симуляция] Статистический хвост на K(2,2,2)")
    print("-" * 50)

    rng = np.random.default_rng(seed)
    A, _, _ = build_K222()
    P = A / A.sum(axis=1, keepdims=True)

    state = int(rng.integers(6))
    visit_counts = np.zeros(6, dtype=int)
    target = 0
    last_visit = -1
    return_times = []

    for step in range(n_steps + burn_in):
        if step >= burn_in:
            visit_counts[state] += 1
            if state == target:
                if last_visit != -1:
                    return_times.append(step - last_visit)
                last_visit = step
        state = int(rng.choice(6, p=P[state]))

    pi_emp = visit_counts / visit_counts.sum()
    pi_unif = np.ones(6) / 6.0
    uniformity_error = float(np.max(np.abs(pi_emp - pi_unif)))
    tail_l1 = float(np.linalg.norm(pi_emp - pi_unif, ord=1))
    mean_return = float(np.mean(return_times))

    print(f"  Эмпирическое распределение: {np.round(pi_emp, 4)}")
    print(f"  Равномерное распределение:  {np.round(pi_unif, 4)}")
    print(f"  Макс. отклонение: {uniformity_error:.4e}")
    print(f"  L¹-хвост: {tail_l1:.4e}")
    print(f"  Среднее время возврата в вершину 0: {mean_return:.4f} (теория: 6)")

    uniformity_ok = uniformity_error < 1e-2
    return_ok = abs(mean_return - 6.0) < 0.6
    overall = uniformity_ok and return_ok

    print(f"  Результат: {'[Д] ПРОЙДЕН' if overall else '[Г1] НУЖНО БОЛЬШЕ ШАГОВ'}")

    return {
        "uniformity_error": uniformity_error,
        "tail_l1": tail_l1,
        "mean_return": mean_return,
        "passed": overall,
    }


# ============================================================================
# Exact holonomy test on the selected cycle
# ============================================================================

def holonomy_test_exact():
    print("\n[Тест] Точный Z₂-транспорт на каноническом цикле C_6")
    print("-" * 50)

    core = build_admissible_core()
    labels = core["labels"]
    cycle_order = core["cycle_order"]
    cycle_labels = [labels[i] for i in cycle_order]

    epsilon = np.array([1, 1, 1, 1, 1, -1], dtype=int)
    holonomy = int(np.prod(epsilon))

    all_values = set()
    exhaustive_ok = True

    # Exhaustive check on C_6. Analytically, gauge invariance is immediate:
    # product_i (g_{i+1} * eps_i * g_i^{-1}) = (product_i eps_i),
    # because every g_i appears once upstairs and once downstairs.
    for g in product([-1, 1], repeat=6):
        g = np.array(g, dtype=int)
        transformed = np.array(
            [epsilon[i] * g[(i + 1) % 6] * g[i] for i in range(6)],
            dtype=int,
        )
        value = int(np.prod(transformed))
        all_values.add(value)
        if value != holonomy:
            exhaustive_ok = False
            break

    nontrivial_ok = holonomy == -1

    print(f"  Канонический цикл: {' -> '.join(cycle_labels + [cycle_labels[0]])}")
    print(f"  Исходная голономия: {holonomy}")
    print(f"  Уникальные значения после всех 64 калибровок: {sorted(all_values)}")
    print(f"  Нетривиальный класс: {'✓' if nontrivial_ok else '✗'}")
    print(f"  Полная калибровочная инвариантность: {'✓' if exhaustive_ok else '✗'}")

    overall = nontrivial_ok and exhaustive_ok and all_values == {-1}
    print(f"  Результат: {'[Д] ПРОЙДЕН' if overall else '✗ НЕСОВПАДЕНИЕ'}")

    return {
        "cycle_labels": cycle_labels,
        "holonomy": holonomy,
        "all_values": all_values,
        "passed": overall,
    }


# ============================================================================
# Cross-checks on the residual octahedral carrier
# ============================================================================

def stanley_reisner_check(adjacency, name):
    print(f"\n[Проверка] Комплементарные пары для {name}")
    print("-" * 50)

    n = adjacency.shape[0]
    forbidden = [(i, j) for i in range(n) for j in range(i + 1, n) if adjacency[i, j] == 0]

    print(f"  Несмежные пары: {forbidden}")

    expected = [(0, 1), (2, 3), (4, 5)]
    ok = forbidden == expected

    print(f"  Совпадение с комплементарными парами: {'✓' if ok else '✗'}")
    return ok


# ============================================================================
# Block graph: exact spectrum and exact slow eigenspace
# ============================================================================

def build_axis_harmonics(chamber_signs):
    """
    Return the three explicit eigenvectors d_i ⊕ chi_i for lambda = 4.
    """
    pole_vectors = [
        np.array([1, -1, 0, 0, 0, 0], dtype=float),
        np.array([0, 0, 1, -1, 0, 0], dtype=float),
        np.array([0, 0, 0, 0, 1, -1], dtype=float),
    ]
    chamber_vectors = []
    for axis in range(3):
        chamber_vectors.append(
            np.array([sigma[axis] for sigma in chamber_signs], dtype=float)
        )

    basis = []
    for pole_vec, chamber_vec in zip(pole_vectors, chamber_vectors):
        basis.append(np.concatenate([pole_vec, chamber_vec]))
    return basis


def block_operator_spectral_test():
    print("\n[Тест] Составной граф (октаэдр + куб)")
    print("-" * 50)

    A_block, A_oct, A_cube, B, chamber_signs = build_block_graph()
    L_block = laplacian(A_block)

    row_sums = B.sum(axis=1)
    col_sums = B.sum(axis=0)
    bbt_identity = np.array_equal(B @ B.T, 4 * np.eye(6, dtype=int) + 2 * A_oct)

    eigenvalues, _ = eigh_sorted(L_block)
    expected_spectrum = np.array([0, 4, 4, 4, 7, 7, 7, 7, 9, 9, 9, 9, 10, 10], dtype=float)
    spectrum_ok = np.allclose(eigenvalues, expected_spectrum, atol=1e-8)

    basis = build_axis_harmonics(chamber_signs)
    harmonic_ok = True
    for vec in basis:
        if not np.allclose(L_block @ vec, 4.0 * vec, atol=1e-8):
            harmonic_ok = False
            break

    basis_matrix = np.column_stack(basis)
    rank_ok = np.linalg.matrix_rank(basis_matrix) == 3
    orthogonal_ok = np.allclose(basis_matrix.T @ basis_matrix, np.diag([10.0, 10.0, 10.0]), atol=1e-8)

    X = basis_matrix[:6, :]
    Y = basis_matrix[6:, :]
    ratio_identity_ok = np.allclose(Y.T @ Y, 4.0 * (X.T @ X), atol=1e-8)

    lambda4_mult = int(np.sum(np.isclose(eigenvalues, 4.0, atol=1e-8)))
    multiplicity_ok = lambda4_mult == 3

    print(f"  Суммы по строкам B: {row_sums} (ожидалось [4 4 4 4 4 4])")
    print(f"  Суммы по столбцам B: {col_sums} (ожидалось [3 3 3 3 3 3 3 3])")
    print(f"  BB^T = 4I + 2A_oct: {'✓' if bbt_identity else '✗'}")
    print(f"  Спектр L_block: {np.round(eigenvalues, 6)}")
    print(f"  Спектр совпал: {'✓' if spectrum_ok else '✗'}")
    print(f"  Кратность λ=4: {lambda4_mult} (ожидалось 3)")
    print(f"  Явные осевые гармоники: {'✓' if harmonic_ok else '✗'}")
    print(f"  Ранг slow-базиса: {'✓' if rank_ok else '✗'}")
    print(f"  Ортогональность slow-базиса: {'✓' if orthogonal_ok else '✗'}")
    print(f"  Тождество энергии Y^T Y = 4 X^T X: {'✓' if ratio_identity_ok else '✗'}")

    ratio_sample = np.sum(basis[0][6:] ** 2) / np.sum(basis[0][:6] ** 2)
    print(f"  Отношение энергий на базисной моде: {ratio_sample:.2f}")

    overall = (
        np.all(row_sums == 4)
        and np.all(col_sums == 3)
        and bbt_identity
        and spectrum_ok
        and multiplicity_ok
        and harmonic_ok
        and rank_ok
        and orthogonal_ok
        and ratio_identity_ok
    )
    print(f"  Результат: {'[Д] ПРОЙДЕН' if overall else '✗ НЕСОВПАДЕНИЕ'}")

    return {
        "spectrum_ok": spectrum_ok,
        "multiplicity_ok": multiplicity_ok,
        "ratio_identity_ok": ratio_identity_ok,
        "passed": overall,
    }


def presentation_and_intertwiner_test():
    print("\n[Тест] Устойчивость presentation и осевое сплетение")
    print("-" * 50)

    core = build_admissible_core()
    states = core["states"]
    index = core["index"]
    A_prim = core["A_prim"]
    A_res = core["A_res"]

    shell1 = {0, 2, 4}
    shell2 = {1, 3, 5}

    # Relation matrices R_0, R_1, R_2, R_3 on X_adm.
    A_rel = {
        0: np.eye(6, dtype=int),
        1: np.zeros((6, 6), dtype=int),
        2: np.zeros((6, 6), dtype=int),
        3: np.zeros((6, 6), dtype=int),
    }
    for i in range(6):
        for j in range(6):
            if i == j:
                continue
            A_rel[hamming_distance(states[i], states[j])][i, j] = 1

    B, chamber_signs = build_incidence_matrix()
    chamber_index = {sigma: i for i, sigma in enumerate(chamber_signs)}

    def apply_state_symmetry(state, coord_perm, use_global_complement):
        transformed = tuple(state[coord_perm[i]] for i in range(3))
        if use_global_complement:
            transformed = tuple(1 - bit for bit in transformed)
        return transformed

    def apply_chamber_symmetry(sigma, coord_perm, use_global_complement):
        transformed = tuple(sigma[coord_perm[i]] for i in range(3))
        if use_global_complement:
            transformed = tuple(-bit for bit in transformed)
        return transformed

    generated_state_perms = set()
    group_ok = True
    incidence_ok = True
    shell_pair_ok = True

    for coord_perm in permutations(range(3)):
        for use_global_complement in (False, True):
            state_perm = tuple(
                index[apply_state_symmetry(state, coord_perm, use_global_complement)]
                for state in states
            )
            chamber_perm = tuple(
                chamber_index[apply_chamber_symmetry(sigma, coord_perm, use_global_complement)]
                for sigma in chamber_signs
            )
            generated_state_perms.add(state_perm)

            P_state = np.eye(6, dtype=int)[list(state_perm)]
            P_chamber = np.eye(8, dtype=int)[list(chamber_perm)]

            rel_ok = all(
                np.array_equal(P_state @ A_rel[k] @ P_state.T, A_rel[k])
                for k in range(4)
            )
            carrier_ok = np.array_equal(P_state @ A_prim @ P_state.T, A_prim) and np.array_equal(
                P_state @ A_res @ P_state.T, A_res
            )
            inc_ok = np.array_equal(P_state @ B @ P_chamber.T, B)

            image_shell1 = {state_perm[i] for i in shell1}
            image_shell2 = {state_perm[i] for i in shell2}
            shells_as_pair_ok = (
                (image_shell1 == shell1 and image_shell2 == shell2)
                or (image_shell1 == shell2 and image_shell2 == shell1)
            )

            group_ok = group_ok and rel_ok and carrier_ok
            incidence_ok = incidence_ok and inc_ok
            shell_pair_ok = shell_pair_ok and shells_as_pair_ok

    generated_count_ok = len(generated_state_perms) == 12

    all_relation_automorphisms = set()
    shell_preserving_automorphisms = set()
    for perm in permutations(range(6)):
        P = np.eye(6, dtype=int)[list(perm)]
        if all(np.array_equal(P @ A_rel[k] @ P.T, A_rel[k]) for k in range(4)):
            all_relation_automorphisms.add(perm)
            image_shell1 = {perm[i] for i in shell1}
            image_shell2 = {perm[i] for i in shell2}
            if image_shell1 == shell1 and image_shell2 == shell2:
                shell_preserving_automorphisms.add(perm)

    full_group_ok = (
        generated_count_ok
        and len(all_relation_automorphisms) == 12
        and generated_state_perms == all_relation_automorphisms
    )
    shell_subgroup_ok = len(shell_preserving_automorphisms) == 6

    # Axial intertwiner: D = span(d_i), Xi = span(chi_i).
    basis = build_axis_harmonics(chamber_signs)
    D = np.column_stack([vec[:6] for vec in basis])
    Xi = np.column_stack([vec[6:] for vec in basis])

    intertwiner_ok = np.array_equal(B.T @ D, Xi) and np.array_equal(B @ Xi, 4 * D)

    D_hat = D / np.sqrt(2.0)
    Xi_hat = Xi / np.sqrt(8.0)
    normalized_factor_ok = np.allclose(B.T @ D_hat, 2.0 * Xi_hat, atol=1e-8) and np.allclose(
        B @ Xi_hat, 2.0 * D_hat, atol=1e-8
    )

    axial_matrix = D_hat.T @ B @ Xi_hat
    axial_scalar_ok = np.allclose(axial_matrix, 2.0 * np.eye(3), atol=1e-8)
    ratio_from_axial_ok = np.allclose(4.0, 2.0 ** 2, atol=1e-8)

    print(f"  Сгенерированных симметрий Γ_3: {len(generated_state_perms)} (ожидалось 12)")
    print(f"  Все элементы Γ_3 сохраняют R_0..R_3, A_prim, A_res: {'✓' if group_ok else '✗'}")
    print(f"  Все элементы Γ_3 сохраняют shell-pair и B: {'✓' if shell_pair_ok and incidence_ok else '✗'}")
    print(
        f"  Полная цветосохраняющая группа отношенческого ядра имеет размер 12: "
        f"{'✓' if full_group_ok else '✗'}"
    )
    print(
        f"  Подгруппа, сохраняющая оболочки по отдельности, имеет размер 6: "
        f"{'✓' if shell_subgroup_ok else '✗'}"
    )
    print(f"  B^T D = Xi и B Xi = 4D: {'✓' if intertwiner_ok else '✗'}")
    print(f"  На нормированном осевом секторе коэффициент связи равен 2: {'✓' if normalized_factor_ok else '✗'}")
    print(f"  Матрица осевого сплетения в нормированном базисе = 2I: {'✓' if axial_scalar_ok else '✗'}")
    print(f"  Коэффициент 4 = 2^2: {'✓' if ratio_from_axial_ok else '✗'}")

    overall = (
        group_ok
        and incidence_ok
        and shell_pair_ok
        and full_group_ok
        and shell_subgroup_ok
        and intertwiner_ok
        and normalized_factor_ok
        and axial_scalar_ok
        and ratio_from_axial_ok
    )
    print(f"  Результат: {'[Д|К] ПРОЙДЕН' if overall else '✗ НЕСОВПАДЕНИЕ'}")

    return {
        "gamma3_generated": len(generated_state_perms),
        "full_group_ok": full_group_ok,
        "shell_subgroup_ok": shell_subgroup_ok,
        "normalized_factor_ok": normalized_factor_ok,
        "status": "[Д|К]",
        "passed": overall,
    }


def general_chamber_block_law_test():
    print("\n[Тест] Общий камерный слой и блочный спектр")
    print("-" * 50)

    checked_ns = [3, 4, 5, 6]
    all_ok = True

    for n in checked_ns:
        A_block, A_cross, A_cube, B, pole_data, chamber_signs, _ = build_general_block_graph(n)
        L_block = laplacian(A_block)

        row_ok = np.all(B.sum(axis=1) == 2 ** (n - 1))
        col_ok = np.all(B.sum(axis=0) == n)
        bbt_ok = np.array_equal(
            B @ B.T,
            (2 ** (n - 1)) * np.eye(2 * n, dtype=int) + (2 ** (n - 2)) * A_cross,
        )

        expected_spectrum, lambda_minus, lambda_plus = expected_general_block_spectrum(n)
        eigenvalues, _ = eigh_sorted(L_block)
        spectrum_ok = np.allclose(eigenvalues, expected_spectrum, atol=1e-8)

        pole_basis = []
        chamber_basis = []
        alpha = (2 * n - 2) + 2 ** (n - 1)
        t_minus = (alpha - lambda_minus) / (2 ** (n - 1))
        for axis in range(n):
            d_i = np.zeros(2 * n, dtype=float)
            d_i[2 * axis] = 1.0
            d_i[2 * axis + 1] = -1.0
            chi_i = np.array([sigma[axis] for sigma in chamber_signs], dtype=float)
            pole_basis.append(d_i)
            chamber_basis.append(chi_i)

        basis = [
            np.concatenate([d_i, t_minus * chi_i])
            for d_i, chi_i in zip(pole_basis, chamber_basis)
        ]
        harmonic_ok = all(
            np.allclose(L_block @ vec, lambda_minus * vec, atol=1e-8)
            for vec in basis
        )

        basis_matrix = np.column_stack(basis)
        X = basis_matrix[: 2 * n, :]
        Y = basis_matrix[2 * n :, :]
        rank_ok = np.linalg.matrix_rank(basis_matrix) == n
        orthogonal_ok = np.allclose(basis_matrix.T @ basis_matrix, np.diag(np.diag(basis_matrix.T @ basis_matrix)), atol=1e-8)
        ratio_n = (2 ** (n - 1)) * (t_minus ** 2)
        ratio_identity_ok = np.allclose(Y.T @ Y, ratio_n * (X.T @ X), atol=1e-8)
        slow_mult_ok = int(np.sum(np.isclose(eigenvalues, lambda_minus, atol=1e-8))) == n

        print(
            f"  n={n}: Q_n={2**n} камер, row={2**(n-1)}, col={n}, "
            f"λ_-={lambda_minus:.6f}, ratio={ratio_n:.6f}"
        )
        print(
            f"       BB^T: {'✓' if bbt_ok else '✗'}, "
            f"Spec: {'✓' if spectrum_ok else '✗'}, "
            f"slow mult={n}: {'✓' if slow_mult_ok else '✗'}"
        )

        all_ok = all_ok and row_ok and col_ok and bbt_ok and spectrum_ok and harmonic_ok and rank_ok and orthogonal_ok and ratio_identity_ok and slow_mult_ok

    print(f"  Проверенные размерности: {checked_ns}")
    print(f"  Результат: {'[Д] ПРОЙДЕН' if all_ok else '✗ НЕСОВПАДЕНИЕ'}")

    return {
        "checked_ns": checked_ns,
        "passed": all_ok,
    }


def general_dimension_reduction_test():
    print("\n[Тест] Общий закон редукции n -> n-1")
    print("-" * 50)

    checked_ns = [4, 5, 6]
    all_ok = True

    for n in checked_ns:
        axis = n - 1
        data_n = build_residual_graph_n(n)
        states_n = data_n["states"]
        A_n = data_n["A_res"]

        p = tuple(1 if i == axis else 0 for i in range(n))
        p_bar = tuple(1 - bit for bit in p)
        keep_indices = [i for i, state in enumerate(states_n) if state not in {p, p_bar}]
        kept_states = [states_n[i] for i in keep_indices]

        projected = [state[:axis] + state[axis + 1 :] for state in kept_states]
        projected_set = set(projected)

        data_prev = build_residual_graph_n(n - 1)
        prev_states = data_prev["states"]
        prev_index = {state: i for i, state in enumerate(prev_states)}
        projection_bijection_ok = projected_set == set(prev_states) and len(projected) == len(prev_states)

        A_restricted = A_n[np.ix_(keep_indices, keep_indices)]
        perm = [prev_index[state] for state in projected]
        A_prev_in_projected_order = data_prev["A_res"][np.ix_(perm, perm)]
        graph_reduction_ok = np.array_equal(A_restricted, A_prev_in_projected_order)

        chamber_signs_n = list(product([-1, +1], repeat=n))
        chamber_signs_prev = list(product([-1, +1], repeat=n - 1))
        fibers = {
            sigma_prev: [sigma_prev + (-1,), sigma_prev + (+1,)]
            for sigma_prev in chamber_signs_prev
        }
        fiber_sizes_ok = all(len(fiber) == 2 for fiber in fibers.values())

        A_q_prev_sign = np.zeros((2 ** (n - 1), 2 ** (n - 1)), dtype=int)
        for i, a in enumerate(chamber_signs_prev):
            for j in range(i + 1, len(chamber_signs_prev)):
                b = chamber_signs_prev[j]
                exists_edge = any(
                    sum(u_t != v_t for u_t, v_t in zip(u, v)) == 1
                    for u in fibers[a]
                    for v in fibers[b]
                )
                if exists_edge:
                    A_q_prev_sign[i, j] = A_q_prev_sign[j, i] = 1

        expected_q_prev_sign = np.zeros_like(A_q_prev_sign)
        for i, a in enumerate(chamber_signs_prev):
            for j in range(i + 1, len(chamber_signs_prev)):
                b = chamber_signs_prev[j]
                if sum(x != y for x, y in zip(a, b)) == 1:
                    expected_q_prev_sign[i, j] = expected_q_prev_sign[j, i] = 1
        chamber_quotient_ok = np.array_equal(A_q_prev_sign, expected_q_prev_sign)

        B_n, _, chamber_signs_full = build_incidence_matrix_n(n)
        B_prev, _, _ = build_incidence_matrix_n(n - 1)
        remaining_rows = list(range(2 * (n - 1)))
        row_restricted = B_n[np.ix_(remaining_rows, np.arange(2 ** n))]

        factor_cols = []
        incidence_constant_ok = True
        sign_to_index = {sigma: i for i, sigma in enumerate(chamber_signs_full)}
        for sigma_prev in chamber_signs_prev:
            col_minus = row_restricted[:, sign_to_index[sigma_prev + (-1,)]]
            col_plus = row_restricted[:, sign_to_index[sigma_prev + (+1,)]]
            if not np.array_equal(col_minus, col_plus):
                incidence_constant_ok = False
            factor_cols.append(col_minus)
        B_factor = np.column_stack(factor_cols)
        incidence_descent_ok = incidence_constant_ok and np.array_equal(B_factor, B_prev)

        print(
            f"  n={n}: V_n -> V_{n-1}: {'✓' if projection_bijection_ok and graph_reduction_ok else '✗'}, "
            f"Q_n -> Q_{n-1}: {'✓' if fiber_sizes_ok and chamber_quotient_ok else '✗'}, "
            f"B_n -> B_{n-1}: {'✓' if incidence_descent_ok else '✗'}"
        )

        all_ok = all_ok and projection_bijection_ok and graph_reduction_ok and fiber_sizes_ok and chamber_quotient_ok and incidence_descent_ok

    print(f"  Проверенные размерности: {checked_ns}")
    print(f"  Результат: {'[Д] ПРОЙДЕН' if all_ok else '✗ НЕСОВПАДЕНИЕ'}")

    return {
        "checked_ns": checked_ns,
        "passed": all_ok,
    }


def minimal_category_layer_test():
    print("\n[Тест] Минимальный категориальный слой")
    print("-" * 50)

    checked_ns = [3, 4, 5, 6]
    all_ok = True

    for n in checked_ns:
        chamber_signs = list(product([-1, +1], repeat=n))
        phi_images = [tuple((1 + s) // 2 for s in sigma) for sigma in chamber_signs]
        phi_bijection_ok = len(set(phi_images)) == 2 ** n

        adjacency_ok = True
        for i, sigma in enumerate(chamber_signs):
            for j in range(i + 1, len(chamber_signs)):
                tau = chamber_signs[j]
                sign_edge = sum(a != b for a, b in zip(sigma, tau)) == 1
                bit_edge = hamming_distance(phi_images[i], phi_images[j]) == 1
                if sign_edge != bit_edge:
                    adjacency_ok = False
                    break
            if not adjacency_ok:
                break

        k = n - 1
        reduction_ok = True
        for i, sigma in enumerate(chamber_signs):
            for j in range(i + 1, len(chamber_signs)):
                tau = chamber_signs[j]
                if sum(a != b for a, b in zip(sigma, tau)) != 1:
                    continue
                sigma_red = sigma[:k] + sigma[k + 1 :]
                tau_red = tau[:k] + tau[k + 1 :]
                dist = sum(a != b for a, b in zip(sigma_red, tau_red))
                if dist not in {0, 1}:
                    reduction_ok = False
                    break
            if not reduction_ok:
                break

        incidence_size = 2 ** (n - 1) * (2 * n)
        B_n, _, _ = build_incidence_matrix_n(n)
        incidence_ok = int(B_n.sum()) == incidence_size

        print(
            f"  n={n}: Φ_n bijection: {'✓' if phi_bijection_ok else '✗'}, "
            f"adjacency: {'✓' if adjacency_ok else '✗'}, "
            f"T_k on edges: {'✓' if reduction_ok else '✗'}, "
            f"|I_n|={incidence_size}: {'✓' if incidence_ok else '✗'}"
        )

        all_ok = all_ok and phi_bijection_ok and adjacency_ok and reduction_ok and incidence_ok

    print(f"  Проверенные размерности: {checked_ns}")
    print(f"  Результат: {'[Д] ПРОЙДЕН' if all_ok else '✗ НЕСОВПАДЕНИЕ'}")

    return {
        "checked_ns": checked_ns,
        "passed": all_ok,
    }


def build_shell_projectors(n):
    states = build_raw_cube_states(n)
    projectors = {}
    for k in range(n + 1):
        diag = np.array([1 if sum(state) == k else 0 for state in states], dtype=int)
        projectors[k] = np.diag(diag)
    return projectors


def build_complement_matrix(n):
    states = build_raw_cube_states(n)
    index = {state: i for i, state in enumerate(states)}
    C = np.zeros((2 ** n, 2 ** n), dtype=int)
    for i, state in enumerate(states):
        comp = tuple(1 - bit for bit in state)
        C[index[comp], i] = 1
    return C


def embed_with_zero(y, k):
    return tuple(list(y[:k]) + [0.0] + list(y[k:]))


def project_delete_coord(x, k):
    return tuple(list(x[:k]) + list(x[k + 1 :]))


def in_cross_polytope(x, tol=TOL):
    return sum(abs(t) for t in x) <= 1.0 + tol


def in_sign_chamber(x, sigma, tol=TOL):
    return all(s * t >= -tol for s, t in zip(sigma, x))


def build_aperture_transition_operators(n):
    A_qn, _ = build_Qn(n)
    projectors = build_shell_projectors(n)
    E = sum(projectors[k - 1] @ A_qn @ projectors[k] for k in range(1, n + 1))
    F = sum(projectors[k + 1] @ A_qn @ projectors[k] for k in range(0, n))
    H = sum((n - 2 * k) * projectors[k] for k in range(0, n + 1))
    C = build_complement_matrix(n)
    return projectors, E, F, H, C, A_qn


def spectral_projector_from_H(H, n, k):
    lam_k = n - 2 * k
    result = np.eye(H.shape[0], dtype=float)
    for j in range(n + 1):
        if j == k:
            continue
        lam_j = n - 2 * j
        result = result @ ((H - lam_j * np.eye(H.shape[0])) / (lam_k - lam_j))
    return result


def aperture_algebra_test():
    print("\n[Тест] Оболочечные апертуры и примитивная полосатость")
    print("-" * 50)

    checked_ns = [3, 4, 5, 6]
    all_ok = True

    for n in checked_ns:
        A_qn, _ = build_Qn(n)
        projectors = build_shell_projectors(n)
        identity = np.eye(2 ** n, dtype=int)

        orthogonal_ok = True
        for j in range(n + 1):
            for k in range(n + 1):
                lhs = projectors[j] @ projectors[k]
                rhs = projectors[k] if j == k else np.zeros_like(lhs)
                if not np.array_equal(lhs, rhs):
                    orthogonal_ok = False
                    break
            if not orthogonal_ok:
                break
        resolution_ok = np.array_equal(sum(projectors.values()), identity)

        banded_ok = True
        for j in range(n + 1):
            for k in range(n + 1):
                block = projectors[j] @ A_qn @ projectors[k]
                if abs(j - k) != 1 and np.any(block):
                    banded_ok = False
                    break
            if not banded_ok:
                break

        ext = projectors[1] + projectors[n - 1]
        compressed = ext @ A_qn @ ext
        if n == 3:
            # Compare with the canonical C_6 order on the admissible package.
            raw_states = build_raw_cube_states(3)
            state_to_idx = {state: i for i, state in enumerate(raw_states)}
            core = build_admissible_core()
            admissible_idx = [state_to_idx[state] for state in core["states"]]
            induced = A_qn[np.ix_(admissible_idx, admissible_idx)]
            induced_cycle = permute_adjacency(induced, core["cycle_order"])
            ext_ok = np.array_equal(induced_cycle, build_C6()[0])
        else:
            ext_ok = not np.any(compressed)

        print(
            f"  n={n}: Π_jΠ_k: {'✓' if orthogonal_ok else '✗'}, "
            f"ΣΠ_k=I: {'✓' if resolution_ok else '✗'}, "
            f"banded: {'✓' if banded_ok else '✗'}, "
            f"ext compression: {'✓' if ext_ok else '✗'}"
        )

        all_ok = all_ok and orthogonal_ok and resolution_ok and banded_ok and ext_ok

    print(f"  Проверенные размерности: {checked_ns}")
    print(f"  Результат: {'[Д] ПРОЙДЕН' if all_ok else '✗ НЕСОВПАДЕНИЕ'}")

    return {
        "checked_ns": checked_ns,
        "passed": all_ok,
    }


def strengthened_aperture_algebra_test():
    print("\n[Тест] Усиленная апертурная алгебра")
    print("-" * 50)

    checked_ns = [3, 4, 5, 6]
    all_ok = True

    for n in checked_ns:
        projectors, E, F, H, C, A_qn = build_aperture_transition_operators(n)

        split_ok = np.array_equal(E + F, A_qn)
        sl2_ok = (
            np.allclose(H @ E - E @ H, 2.0 * E, atol=1e-8)
            and np.allclose(H @ F - F @ H, -2.0 * F, atol=1e-8)
            and np.allclose(E @ F - F @ E, H, atol=1e-8)
        )
        complement_ok = (
            np.array_equal(C @ C, np.eye(2 ** n, dtype=int))
            and np.allclose(C @ H + H @ C, 0.0, atol=1e-8)
            and np.allclose(C @ E - F @ C, 0.0, atol=1e-8)
            and np.allclose(C @ F - E @ C, 0.0, atol=1e-8)
        )

        projectors_from_H_ok = True
        for k in range(n + 1):
            recovered = spectral_projector_from_H(H.astype(float), n, k)
            if not np.allclose(recovered, projectors[k], atol=1e-8):
                projectors_from_H_ok = False
                break

        print(
            f"  n={n}: A=E+F: {'✓' if split_ok else '✗'}, "
            f"sl2: {'✓' if sl2_ok else '✗'}, "
            f"complement: {'✓' if complement_ok else '✗'}, "
            f"Π_k from H: {'✓' if projectors_from_H_ok else '✗'}"
        )

        all_ok = all_ok and split_ok and sl2_ok and complement_ok and projectors_from_H_ok

    print(f"  Проверенные размерности: {checked_ns}")
    print(f"  Результат: {'[Д] ПРОЙДЕН' if all_ok else '✗ НЕСОВПАДЕНИЕ'}")

    return {
        "checked_ns": checked_ns,
        "passed": all_ok,
    }


def strong_geometric_reduction_test():
    print("\n[Тест] Сильная геометрическая редукция через сечение и проекцию")
    print("-" * 50)

    checked_ns = [4, 5, 6]
    all_ok = True

    for n in checked_ns:
        k = n - 1

        section_vertices = set()
        for axis in range(n):
            if axis == k:
                continue
            for sign in (-1.0, 1.0):
                v = [0.0] * n
                v[axis] = sign
                section_vertices.add(tuple(v))

        embedded_lower_vertices = set()
        for axis in range(n - 1):
            for sign in (-1.0, 1.0):
                y = [0.0] * (n - 1)
                y[axis] = sign
                embedded_lower_vertices.add(embed_with_zero(tuple(y), k))

        vertices_ok = section_vertices == embedded_lower_vertices

        chamber_pair_ok = True
        for sigma_prev in product([-1.0, 1.0], repeat=n - 1):
            y = tuple(s / (2.0 * n) for s in sigma_prev)
            x = embed_with_zero(y, k)
            containing = []
            for sigma in product([-1.0, 1.0], repeat=n):
                if in_sign_chamber(x, sigma):
                    containing.append(tuple(int(s) for s in sigma))
            expected = [
                tuple(list(tuple(int(s) for s in sigma_prev[:k])) + [-1] + list(tuple(int(s) for s in sigma_prev[k:]))),
                tuple(list(tuple(int(s) for s in sigma_prev[:k])) + [+1] + list(tuple(int(s) for s in sigma_prev[k:]))),
            ]
            if set(containing) != set(expected):
                chamber_pair_ok = False
                break

        fiber_ok = True
        sample_points = [tuple(0.0 for _ in range(n - 1))]
        for axis in range(n - 1):
            y = [0.0] * (n - 1)
            y[axis] = 0.5
            sample_points.append(tuple(y))
        sample_points.extend(
            tuple(s / (2.0 * n) for s in sigma_prev)
            for sigma_prev in product([-1.0, 1.0], repeat=n - 1)
        )

        for y in sample_points:
            norm_y = sum(abs(t) for t in y)
            tmax = 1.0 - norm_y
            x_mid = embed_with_zero(y, k)
            x_top = list(x_mid)
            x_top[k] = tmax
            x_bot = list(x_mid)
            x_bot[k] = -tmax
            if (
                not in_cross_polytope(x_mid)
                or not in_cross_polytope(tuple(x_top))
                or not in_cross_polytope(tuple(x_bot))
                or project_delete_coord(x_mid, k) != y
            ):
                fiber_ok = False
                break
            if tmax > 1e-9:
                x_out = list(x_mid)
                x_out[k] = tmax + 0.1
                if in_cross_polytope(tuple(x_out)):
                    fiber_ok = False
                    break

        print(
            f"  n={n}: section vertices: {'✓' if vertices_ok else '✗'}, "
            f"chamber pairing: {'✓' if chamber_pair_ok else '✗'}, "
            f"fiber formula: {'✓' if fiber_ok else '✗'}"
        )

        all_ok = all_ok and vertices_ok and chamber_pair_ok and fiber_ok

    print(f"  Проверенные размерности: {checked_ns}")
    print(f"  Результат: {'[Д] ПРОЙДЕН' if all_ok else '✗ НЕСОВПАДЕНИЕ'}")

    return {
        "checked_ns": checked_ns,
        "passed": all_ok,
    }


# ============================================================================
# Main entry point
# ============================================================================

def main():
    print("=" * 72)
    print("ЧИСТОВОЙ ВЕРИФИКАТОР DOT")
    print("Область: аксиоматический, комбинаторный, спектральный и Z₂-транспортный каркас")
    print("=" * 72)

    results = {}

    print("\n" + "█" * 72)
    print("РАЗДЕЛ P: ДОЯДЕРНЫЙ БИНАРНЫЙ СЛОЙ")
    print("█" * 72)
    results["precore_binary"] = precore_binary_layer_test()

    print("\n" + "█" * 72)
    print("РАЗДЕЛ 0: АКСИОМАТИЧЕСКИЙ УРОВЕНЬ [А]")
    print("█" * 72)
    results["axioms"] = axiomatic_level_test()

    print("\n" + "█" * 72)
    print("РАЗДЕЛ 0A: МИНИМАЛЬНЫЙ АКТИВНЫЙ НОСИТЕЛЬ")
    print("█" * 72)
    results["minimal_active_carrier"] = minimal_active_carrier_test()

    print("\n" + "█" * 72)
    print("РАЗДЕЛ 1: КОМБИНАТОРНОЕ ЯДРО")
    print("█" * 72)
    results["core"] = combinatorial_core_test()

    print("\n" + "█" * 72)
    print("РАЗДЕЛ 2: СХЕМА ОТНОШЕНИЙ НА X_adm")
    print("█" * 72)
    results["relations"] = relation_scheme_test()

    print("\n" + "█" * 72)
    print("РАЗДЕЛ 2A: ГРАММАТИКА ГРАНЕЙ И СЕКТОРЫ КУНА")
    print("█" * 72)
    results["shell_face_kuhn"] = shell_face_kuhn_transition_test()

    print("\n" + "█" * 72)
    print("РАЗДЕЛ 3: АЛГЕБРА ОТНОШЕНИЙ")
    print("█" * 72)
    results["relation_algebra"] = relation_algebra_test()

    print("\n" + "█" * 72)
    print("РАЗДЕЛ 4: СПЕКТРЫ БАЗОВЫХ НОСИТЕЛЕЙ")
    print("█" * 72)
    A_c6, name_c6 = build_C6()
    results["C6"] = spectral_test(A_c6, name_c6, [0, 1, 1, 3, 3, 4], 5.0 / 6.0)

    A_q3, name_q3, _ = build_Q3()
    results["Q3"] = spectral_test(A_q3, name_q3, [0, 2, 2, 2, 4, 4, 4, 6], 7.0 / 12.0)

    A_oct, name_oct, _ = build_K222()
    results["octahedron"] = spectral_test(
        A_oct,
        name_oct,
        [0, 4, 4, 4, 6, 6],
        5.0 / 12.0,
    )

    print("\n" + "█" * 72)
    print("РАЗДЕЛ 5: СТАТИСТИЧЕСКАЯ ИЛЛЮСТРАЦИЯ")
    print("█" * 72)
    results["markov"] = markov_simulation_k222()

    print("\n" + "█" * 72)
    print("РАЗДЕЛ 6: ТОЧНЫЙ Z₂-ТРАНСПОРТ НА ЦИКЛЕ")
    print("█" * 72)
    results["holonomy"] = holonomy_test_exact()

    print("\n" + "█" * 72)
    print("РАЗДЕЛ 7: ОКТАЭДРАЛЬНЫЕ КОМПЛЕМЕНТАРНЫЕ ПАРЫ")
    print("█" * 72)
    sr_ok = stanley_reisner_check(A_oct, "K(2,2,2)")
    results["complement_pairs"] = {"passed": sr_ok}

    print("\n" + "█" * 72)
    print("РАЗДЕЛ 8: СОСТАВНОЙ ГРАФ")
    print("█" * 72)
    results["block"] = block_operator_spectral_test()

    print("\n" + "█" * 72)
    print("РАЗДЕЛ 9: 4D-ГРАФОВЫЙ СЛОЙ")
    print("█" * 72)
    results["4d_graph"] = higher_4d_graph_test()

    print("\n" + "█" * 72)
    print("РАЗДЕЛ 10: 4D-ЛЕСТНИЦА ОБОЛОЧЕК")
    print("█" * 72)
    results["4d_shells"] = hamming_shell_ladder_test_4d()

    print("\n" + "█" * 72)
    print("РАЗДЕЛ 11: ОБЩИЙ n-МЕРНЫЙ ЗАКОН")
    print("█" * 72)
    results["n_shell_law"] = general_dimension_shell_law_test()

    print("\n" + "█" * 72)
    print("РАЗДЕЛ 12: ОБЩИЙ КАМЕРНЫЙ СЛОЙ")
    print("█" * 72)
    results["n_chambers"] = general_chamber_block_law_test()

    print("\n" + "█" * 72)
    print("РАЗДЕЛ 13: ОБЩАЯ РЕДУКЦИЯ n -> n-1")
    print("█" * 72)
    results["n_reduction"] = general_dimension_reduction_test()

    print("\n" + "█" * 72)
    print("РАЗДЕЛ 14: МИНИМАЛЬНЫЙ КАТЕГОРИАЛЬНЫЙ СЛОЙ")
    print("█" * 72)
    results["category_layer"] = minimal_category_layer_test()

    print("\n" + "█" * 72)
    print("РАЗДЕЛ 15: АПЕРТУРНЫЙ СЛОЙ")
    print("█" * 72)
    results["apertures"] = aperture_algebra_test()

    print("\n" + "█" * 72)
    print("РАЗДЕЛ 16: УСИЛЕННАЯ АПЕРТУРНАЯ АЛГЕБРА")
    print("█" * 72)
    results["aperture_algebra_strong"] = strengthened_aperture_algebra_test()

    print("\n" + "█" * 72)
    print("РАЗДЕЛ 17: СИЛЬНАЯ ГЕОМЕТРИЧЕСКАЯ РЕДУКЦИЯ")
    print("█" * 72)
    results["strong_geometry"] = strong_geometric_reduction_test()

    print("\n" + "█" * 72)
    print("РАЗДЕЛ 18: УСТОЙЧИВОСТЬ PRESENTATION И ОСЕВОЕ СПЛЕТЕНИЕ")
    print("█" * 72)
    results["presentation_stability"] = presentation_and_intertwiner_test()

    print("\n" + "█" * 72)
    print("РАЗДЕЛ 19: КОНЕЧНАЯ СИГНАТУРА ОТНОШЕНЧЕСКОГО ЯДРА")
    print("█" * 72)
    results["core_bridge_signature"] = core_bridge_signature_test()

    print("\n" + "█" * 72)
    print("РАЗДЕЛ 20: ОПЕРАТОРНО-КОМБИНАТОРНЫЙ ИНТЕРФЕЙС sl2 -> Σ_core")
    print("█" * 72)
    results["sl2_sigma_core_bridge"] = sl2_sigma_core_bridge_test()

    print("\n" + "=" * 72)
    print("СВОДНЫЙ ОТЧЁТ")
    print("=" * 72)

    passed_count = sum(result.get("passed", False) for result in results.values())
    total = len(results)
    print(f"\nПройдено разделов: {passed_count} / {total}")
    summary_labels = {
        "precore_binary": "precore binary",
        "minimal_active_carrier": "minimal six-state carrier",
        "shell_face_kuhn": "shell face / Kuhn",
        "relation_algebra": "relation algebra",
        "complement_pairs": "complement pairs",
        "4d_graph": "4D graph layer",
        "4d_shells": "4D shell layer",
        "n_shell_law": "n-shell law",
        "n_chambers": "n-chamber law",
        "n_reduction": "n-reduction",
        "category_layer": "category layer",
        "aperture_algebra_strong": "strong aperture algebra",
        "strong_geometry": "strong geometry",
        "presentation_stability": "presentation stability",
        "core_bridge_signature": "core interface signature",
        "sl2_sigma_core_bridge": "sl2/Sigma interface",
    }
    for name, result in results.items():
        status = result.get("status")
        if status is None:
            status = "[Д]" if result.get("passed", False) else "[Г1/✗]"
        label = summary_labels.get(name, name)
        print(f"  {label:28s} : {status}")

    if passed_count == total:
        print("\n✓ Чистовой строгий каркас полностью верифицирован.")
    else:
        print("\n✗ Обнаружены несогласованные разделы.")

    print("=" * 72)
    return results


if __name__ == "__main__":
    main()
