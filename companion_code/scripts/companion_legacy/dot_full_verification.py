#!/usr/bin/env python3
"""
===========================================================================
DOT FULL VERIFICATION: One Script, All Predictions
===========================================================================

Run this single script to reproduce every claim in the DOT paper.
No external data files needed — all constants derived from first principles.

INPUTS (from geometry):
  γ  = √6/9           (observer anisotropy)
  j  = 1728           (j-invariant)
  |2O| = 48           (binary octahedral group order)
  D  = 39             (cascade depth: 1+10+28)

OUTPUTS:
  - 9 particle masses (compared to PDG/CODATA)
  - 4 coupling constants
  - 4 cosmological fractions
  - g-2 of the electron
  - Fine structure splitting
  - Bethe logarithm
  - Total: 21 observables

STATUS RULE:
  This script mixes three layers:
    1. exact structural identities,
    2. baseline numerical predictions,
    3. candidate correction layers.

It therefore serves as a unified verifier/dashboard, not as a single closed proof.
===========================================================================
"""

import math


# ==========================================================================
#  SECTION 0: FUNDAMENTAL INVARIANTS (from octahedron + observer)
# ==========================================================================

gamma = math.sqrt(6) / 9.0
gamma2 = gamma ** 2
gamma3 = gamma ** 3

j_inv = 1728
group_2O = 48
N_faces = 8
N_vert = 6
D_cascade = 39

# Derived
alpha_inv = j_inv / (4 * math.pi) - (group_2O - 1) * gamma3 / 2
alpha = 1.0 / alpha_inv

M_e = 0.510998950  # electron mass (MeV) — unit anchor


# ==========================================================================
#  SECTION 1: CARRIER FUNCTIONS
# ==========================================================================

def partition_coeffs(n_max):
    p = [0] * (n_max + 1)
    p[0] = 1
    for k in range(1, n_max + 1):
        for n in range(k, n_max + 1):
            p[n] += p[n - k]
    return p

def sigma1_coeffs(n_max):
    out = [0] * (n_max + 1)
    for d in range(1, n_max + 1):
        for n in range(d, n_max + 1, d):
            out[n] += d
    return out

def backbone_excess(carrier, p):
    all_abs = [abs(carrier[n]) for n in range(1, len(carrier)) if abs(carrier[n]) > 1e-12]
    g = sum(all_abs) / len(all_abs) if all_abs else 1.0
    bk = [abs(carrier[n]) for n in range(1, len(carrier)) if n % p == 0]
    return (sum(bk) / len(bk) / g - 1.0) if bk else 0.0

def balance_deviation(carrier, p, ann):
    all_abs = [abs(carrier[n]) for n in range(1, len(carrier)) if abs(carrier[n]) > 1e-12]
    g = sum(all_abs) / len(all_abs) if all_abs else 1.0
    loads = {}
    for r in range(p):
        bk = [abs(carrier[n]) for n in range(1, len(carrier)) if n % p == r]
        loads[r] = (sum(bk) / len(bk) / g) if bk else 0.0
    pairs = [(a, p - a) for a in range(1, p // 2 + 1)]
    intact = [(a, b) for a, b in pairs if ann not in (a, b)]
    bals = [loads[a] / (loads[a] + loads[b]) for a, b in intact
            if loads[a] + loads[b] > 1e-12]
    return (sum(bals) / len(bals) - 0.5) if bals else 0.0

N_CARRIER = 200
pq = partition_coeffs(N_CARRIER)
s1 = sigma1_coeffs(N_CARRIER)
e2 = [0] + [-24 * s1[n] for n in range(1, N_CARRIER + 1)]

bb5 = backbone_excess(pq, 5)
bb7 = backbone_excess(pq, 7)
bb9 = backbone_excess(pq, 9)
bb11 = backbone_excess(pq, 11)
bd5 = balance_deviation(e2, 5, 4)


# ==========================================================================
#  SECTION 2: MASS PREDICTIONS
# ==========================================================================

def predict_mass(bare_ratio, correction):
    return bare_ratio * M_e * (1.0 + correction)

results = []
candidate_results = []

def add(name, pred, exp, unc=0.0):
    err_pct = abs(pred - exp) / exp * 100
    sigma = abs(pred - exp) / unc if unc > 0 else float('inf')
    results.append((name, pred, exp, unc, err_pct, sigma))

def add_candidate(name, pred, exp, unc=0.0, note="candidate"):
    err_pct = abs(pred - exp) / exp * 100
    sigma = abs(pred - exp) / unc if unc > 0 else float('inf')
    candidate_results.append((name, pred, exp, unc, err_pct, sigma, note))

# Leptons
mu_pred = predict_mass(56.0 / gamma, alpha * bb5 / gamma)
add("Muon (μ)", mu_pred, 105.6583755, 0.0000023)

tau_pred = predict_mass(70.0 / gamma3, -alpha * backbone_excess(pq, 9))
add("Tau (τ)", tau_pred, 1776.930, 0.09)

# Baryons
p_pred = predict_mass(136.0 / gamma2, -alpha * bb7 / 7.0)
add("Proton (p)", p_pred, 938.2720894, 0.00000029)

n_pred_l1 = predict_mass(136.0 / gamma2, -alpha * backbone_excess(pq, 9))
g_abs9 = sum(abs(pq[n]) for n in range(1, N_CARRIER+1)) / N_CARRIER
loads9 = {}
for r in range(9):
    bk = [abs(pq[n]) for n in range(1, N_CARRIER+1) if n % 9 == r]
    loads9[r] = sum(bk)/len(bk)/g_abs9 if bk else 0.0
s27 = loads9[2] + loads9[7]
bd27 = (loads9[2] / s27 - 0.5) if s27 > 1e-12 else 0.0
delta_l2 = abs(alpha * backbone_excess(pq, 7) * backbone_excess(e2, 2) * bd27 / (2/3))
n_pred = n_pred_l1 * math.exp(-delta_l2)
add("Neutron (n)", n_pred, 939.5654219, 0.00000048)

# Mesons
pi_pred = predict_mass(72.0 / gamma, bd5 * gamma / (2/3))
add("Pion (π⁰)", pi_pred, 134.9768, 0.0005)

k_pred = predict_mass(72.0 / gamma2, gamma2 / 40.0)
add("Kaon (K⁰)", k_pred, 497.611, 0.013)

# Heavy sector
Z_pred = 3.0 * D_cascade**3 * M_e
add("Z boson", Z_pred, 91188.0, 2.0)

W_pred = Z_pred * math.sqrt(1.0 - 2.0/9.0)
add("W boson", W_pred, 80369.2, 13.3)

t_pred = (group_2O * D_cascade) / gamma**4 * M_e
add("Top quark", t_pred, 172520.0, 330.0)


# ==========================================================================
#  SECTION 3: COUPLING CONSTANTS
# ==========================================================================

add("α⁻¹", alpha_inv, 137.035999206, 0.000000011)

koide = 2.0 / 3.0
add("Koide K₄", koide, 0.666667, 0.0)

sin2w = 2.0 / 9.0
add("sin²θ_W (bare)", sin2w, 0.22320, 0.0)

alpha_s = 35.0 / 297.0
add("α_s(M_Z)", alpha_s, 0.1179, 0.0010)


# ==========================================================================
#  SECTION 4: COSMOLOGICAL FRACTIONS
# ==========================================================================

omega_b = 4.0 / 81.0
omega_c = 21.0 / 81.0
omega_l = 56.0 / 81.0
omega_c_transfer = omega_c + alpha * omega_l

add("Ω_b (baryonic)", omega_b, 0.04930, 0.0)
add("Ω_c (dark matter)", omega_c, 0.26450, 0.0)
add("Ω_Λ (dark energy)", omega_l, 0.68620, 0.0)
add("Σ (closure)", omega_b + omega_c + omega_l, 1.0, 0.0)


# ==========================================================================
#  SECTION 5: PRECISION OBSERVABLES
# ==========================================================================

a_qed = (0.5 * (alpha/math.pi)
         - 0.3284789 * (alpha/math.pi)**2
         + 1.1812415 * (alpha/math.pi)**3
         - 1.9114 * (alpha/math.pi)**4
         + 7.606 * (alpha/math.pi)**5)
add("(g−2)/2 electron", a_qed, 0.00115965218128, 0.0)

Ry_MHZ = 3.28984e9
E1_dot = gamma2 * N_faces
K_mhz = Ry_MHZ / E1_dot
fs_mhz = E1_dot * alpha**2 / 16 * K_mhz
add("Fine structure (MHz)", fs_mhz, 10969.0, 0.0)

bethe_dot = D_cascade / 4.0
bethe_exp = math.log(alpha_inv**2)
add("Bethe log (D/4)", bethe_dot, bethe_exp, 0.0)

bridge = (2.0/9.0)**2
add("Ω_b = (sin²θ_W)²", bridge, omega_b, 0.0)


# ==========================================================================
#  SECTION 6: CANDIDATE EXTENSIONS (not counted in main score)
# ==========================================================================

omega_c_transfer_ref = 0.26450
add_candidate("Ω_c transfer", omega_c + alpha * omega_l, omega_c_transfer_ref, 0.0,
              "sector transfer: 21/81 + α·56/81")

z_transfer = Z_pred * (1.0 + alpha * (gamma + 1.0/11.0))
w_transfer = W_pred * (1.0 + alpha * gamma)
t_transfer = t_pred * math.exp(-0.455211005 / 48.0)

add_candidate("Z boson transfer", z_transfer, 91188.0, 2.0,
              "electroweak transfer + neutral surcharge 1/11")
add_candidate("W boson transfer", w_transfer, 80369.2, 13.3,
              "electroweak transfer αγ")
add_candidate("Top damping (old scheme)", t_transfer, 172520.0, 330.0,
              "deep damping exp(-R_avg/48), old reference")
add_candidate("Top damping (new scheme)", t_transfer, 172690.0, 300.0,
              "deep damping exp(-R_avg/48), new reference")


# ==========================================================================
#  OUTPUT
# ==========================================================================

print("=" * 115)
print("  DOT FULL VERIFICATION — 21 Observables, 1 Unit Anchor")
print("=" * 115)
print(f"\n  Inputs: γ = √6/9 = {gamma:.10f}")
print(f"          j(i) = {j_inv}")
print(f"          |2O| = {group_2O}")
print(f"          D = {D_cascade}")
print(f"          α = 1/(j/(4π) − (|2O|−1)·γ³/2) = {alpha:.14f}")
print(f"          M_e = {M_e} MeV (unit anchor)")
print(f"          Status = exact identities + baseline numerics + candidate extensions")
print(f"\n  Carrier diagnostics:")
print(f"          bb5  = backbone_excess(P(q), 5)          = {bb5:.15f}")
print(f"          bb7  = backbone_excess(P(q), 7)          = {bb7:.15f}")
print(f"          bb9  = backbone_excess(P(q), 9)          = {bb9:.15f}")
print(f"          bb11 = backbone_excess(P(q), 11)         = {bb11:.15f}")
print(f"          bd5  = balance_deviation(E₂, 5, ann = 4) = {bd5:.15f}")
print()

categories = [
    ("PARTICLE MASSES", 0, 9),
    ("COUPLING CONSTANTS", 9, 13),
    ("COSMOLOGICAL FRACTIONS", 13, 17),
    ("PRECISION OBSERVABLES", 17, None),
]

total_count = 0
inside_sigma = 0
sub_01_pct = 0
sub_1_pct = 0

for cat_name, start, end in categories:
    subset = results[start:end]
    print(f"\n  {'─'*50}")
    print(f"  {cat_name}")
    print(f"  {'─'*50}")
    print(f"  {'Observable':<25s} {'DOT':>15s} {'Reference':>15s} {'Error %':>10s} {'σ':>8s} {'':>10s}")
    print(f"  {'-'*90}")
    
    for name, pred, exp, unc, err, sigma in subset:
        total_count += 1
        if exp > 1000:
            p_s, e_s = f"{pred:.1f}", f"{exp:.1f}"
        elif exp > 1:
            p_s, e_s = f"{pred:.7f}", f"{exp:.7f}"
        else:
            p_s, e_s = f"{pred:.11f}", f"{exp:.11f}"
        
        if unc > 0 and sigma < 3:
            v = "✅ in σ"; inside_sigma += 1
        elif err < 0.01:
            v = "✅ <0.01%"; sub_01_pct += 1
        elif err < 1.0:
            v = "⬜ <1%"; sub_1_pct += 1
        else:
            v = "🔶 >1%"
        
        s_s = f"{sigma:.1f}" if sigma < 1e6 else "—"
        print(f"  {name:<25s} {p_s:>15s} {e_s:>15s} {err:>10.5f} {s_s:>8s} {v:>10s}")

rest = total_count - inside_sigma - sub_01_pct - sub_1_pct
print(f"\n  {'='*90}")
print(f"  SUMMARY: {total_count} observables | {inside_sigma} in σ | "
      f"{sub_01_pct} <0.01% | {sub_1_pct} <1% | {rest} >1% | 1 unit anchor")
print(f"  {'='*90}")
print(f"\n  EXACT IDENTITIES:")
print(f"    Koide K₄ = 2/3 = 9γ²")
print(f"    sin²θ_W = 2/9 = 3γ²")
print(f"    Ω_b = 4/81 = (sin²θ_W)²")
print(f"    Σ Ω_i = 1 (exact closure)")
print(f"\n  DERIVED:  α⁻¹ = 432/π − 47γ/27 = {alpha_inv:.10f} (err {abs(alpha_inv-137.035999206)/137.035999206*100:.7f}%)")
omega_c_ref = 0.26450
omega_c_residual = omega_c - omega_c_ref
omega_c_cand_1 = omega_c + alpha**2 * bb11
omega_c_cand_2 = omega_c + alpha * gamma3 * bb11
print(f"\n  RESIDUAL DIAGNOSTICS:")
print(f"    Ω_c baseline residual         = {omega_c_residual:+.12f}")
print(f"    Ω_c + α²·bb11                = {omega_c_cand_1:.12f} (Δ={omega_c_cand_1 - omega_c_ref:+.12f})")
print(f"    Ω_c + α·γ³·bb11              = {omega_c_cand_2:.12f} (Δ={omega_c_cand_2 - omega_c_ref:+.12f})")
print(f"    Ω_c + α·Ω_Λ  [transfer]      = {omega_c_transfer:.12f} (Δ={omega_c_transfer - omega_c_ref:+.12f})")
print(f"\n  HEAVY TRANSFER CANDIDATES:")
print(f"    Z · (1 + α(γ + 1/11))        = {z_transfer:.6f} (err {abs(z_transfer - 91188.0)/91188.0*100:.6f}%)")
print(f"    W · (1 + αγ)                 = {w_transfer:.6f} (err {abs(w_transfer - 80369.2)/80369.2*100:.6f}%)")
print(f"    t · exp(-R_avg/48)           = {t_transfer:.6f} (err old-ref {abs(t_transfer - 172520.0)/172520.0*100:.6f}%, new-ref {abs(t_transfer - 172690.0)/172690.0*100:.6f}%)")
print(f"\n  CANDIDATE EXTENSIONS:")
print(f"  {'Observable':<25s} {'Candidate':>15s} {'Reference':>15s} {'Error %':>10s} {'σ':>8s} {'note':>20s}")
print(f"  {'-'*110}")
for name, pred, exp, unc, err, sigma, note in candidate_results:
    if exp > 1000:
        p_s, e_s = f'{pred:.1f}', f'{exp:.1f}'
    elif exp > 1:
        p_s, e_s = f'{pred:.7f}', f'{exp:.7f}'
    else:
        p_s, e_s = f'{pred:.11f}', f'{exp:.11f}'
    s_s = f"{sigma:.1f}" if sigma < 1e6 else "—"
    print(f"  {name:<25s} {p_s:>15s} {e_s:>15s} {err:>10.5f} {s_s:>8s} {note:>20s}")
print(f"\n  ARCHITECTURE:")
print(f"    Fermion mass = (8k/γⁿ) × (1 + α·backbone(P,gate)/scale) × m_e")
print(f"    Meson mass   = (8k/γⁿ) × (1 + baldev(E₂,gate)·γ/(2/3)) × m_e")
print(f"    Heavy        = f(D³, |2O|, γ) × m_e")
print(f"    Constants    = rational(octahedron) / irrational(π, γ)")
