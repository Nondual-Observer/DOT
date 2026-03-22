"""
ПОЛНЫЙ КАЛЬКУЛЯТОР ХВОСТОВ ВСЕХ ЧАСТИЦ ТНР
Берёт формулы из tnr_modular_algebra_analysis.md (Раздел 5)
и вычисляет: Bare → δ₀ → Ω → Total → PDG → Error
"""
import math

# ═══════════════════════════════════════════════════════════
# ФУНДАМЕНТАЛЬНЫЕ КОНСТАНТЫ ТНР
# ═══════════════════════════════════════════════════════════
gamma = math.sqrt(6) / 9       # γ = √6/9
gamma2 = gamma**2               # γ² = 2/27
m_e = 0.51099895                # МэВ (масса электрона)
alpha_bare = 1 / (432/math.pi - 47*gamma/27)  # α_TNR
R_av = 2/3                      # Средний радиус (рабочая оценка)
R_pole = 1/4                    # Полюсной радиус 

print("=" * 100)
print("  ПОЛНЫЙ КАЛЬКУЛЯТОР ХВОСТОВ ВСЕХ ЧАСТИЦ ТНР")
print(f"  γ = {gamma:.8f},  γ² = {gamma2:.8f},  α_bare = {alpha_bare:.8f},  α⁻¹ = {1/alpha_bare:.4f}")
print("=" * 100)

# ═══════════════════════════════════════════════════════════
# ТАБЛИЦА ЧАСТИЦ
# Каждая запись: (Имя, Класс, C_bare, k_depth, δ₀, Ω, PDG_MeV)
# C_bare: числовой множитель перед 1/γ^k
# k_depth: степень 1/γ^k (0 = электрон, 1 = мюон/пион, ...)
# δ₀, Ω: Mellin-поправки (относительные, умножаются на bare)
# ═══════════════════════════════════════════════════════════

particles = []

# --- ЛЕПТОНЫ ---
# Мюон: (2³·7)/γ = 56/γ, δ₀ = +(2/3)/(2³·17) = (2/3)/136
particles.append({
    'name': 'Muon (μ)',
    'class': 'Lepton',
    'C': 2**3 * 7,           # 56
    'k': 1,
    'delta0': +(2/3) / (2**3 * 17),   # (2/3)/136
    'omega': 0,
    'pdg': 105.6583755
})

# Тау: (2⁷·3³) = 3456, k=0 (прямое!), δ₀ = +(2/3)/(2·5·11), Ω = +3/((110)·(432))
particles.append({
    'name': 'Tau (τ)',
    'class': 'Lepton',
    'C': 2**7 * 3**3,         # 3456
    'k': 0,
    'delta0': +(2/3) / (2 * 5 * 11),
    'omega': +3 / ((2 * 5 * 11) * (2**4 * 3**3)),
    'pdg': 1776.86
})

# --- КВАРКИ ---
# u-кварк: (2³·7)·γ² = 56·γ², δ₀ = +R_av·γ/(2³·3)
particles.append({
    'name': 'Up (u)',
    'class': 'Quark',
    'C': 2**3 * 7,            # 56
    'k': -2,                  # умножаем на γ², т.е. «отрицательная глубина»
    'delta0': +R_av * gamma / (2**3 * 3),
    'omega': 0,
    'pdg': 2.16  # МэВ (current mass)
})

# d-кварк: (2⁷·3·17)·γ⁵ = 6528·γ⁵
particles.append({
    'name': 'Down (d)',
    'class': 'Quark',
    'C': 2**7 * 3 * 17,       # 6528
    'k': -5,
    'delta0': -math.pi / (2**4 * 3),
    'omega': 0,
    'pdg': 4.67
})

# s-кварк: (2²)/γ³ = 4/γ³
particles.append({
    'name': 'Strange (s)',
    'class': 'Quark',
    'C': 2**2,                # 4
    'k': 3,
    'delta0': -math.pi / (3 * 13),
    'omega': 0,
    'pdg': 93.4
})

# c-кварк: (2⁴·3)/γ³ = 48/γ³
particles.append({
    'name': 'Charm (c)',
    'class': 'Quark',
    'C': 2**4 * 3,            # 48
    'k': 3,
    'delta0': +math.sqrt(2*3) / (2**3 * 7),
    'omega': 0,
    'pdg': 1270.0
})

# b-кварк: (2·3⁴)/γ³ = 162/γ³
particles.append({
    'name': 'Bottom (b)',
    'class': 'Quark',
    'C': 2 * 3**4,            # 162
    'k': 3,
    'delta0': +1 / (2**3 * 7),
    'omega': 0,
    'pdg': 4180.0
})

# t-кварк: (2⁴·3)·(3·13)/γ⁴ = 48·39/γ⁴ = 1872/γ⁴
particles.append({
    'name': 'Top (t)',
    'class': 'Quark',
    'C': 2**4 * 3 * 3 * 13,   # 1872
    'k': 4,
    'delta0': -R_av * gamma / (2**4 * 3),
    'omega': -(1/math.pi) / (2**3 * 17)**2,
    'pdg': 172760.0
})

# --- МЕЗОНЫ ---
# Пион π⁰: (2³·3²)/γ = 72/γ
particles.append({
    'name': 'Pion (π⁰)',
    'class': 'Meson',
    'C': 2**3 * 3**2,         # 72
    'k': 1,
    'delta0': -(2/3) / (2**4 * 3**3),
    'omega': +(1/3) / ((2**3 * 17) * (2 * 5 * 11)),
    'pdg': 134.9768
})

# Каон K⁺: (2³·3²)/γ² = 72/γ²
particles.append({
    'name': 'Kaon (K⁺)',
    'class': 'Meson',
    'C': 2**3 * 3**2,         # 72
    'k': 2,
    'delta0': -(2/3) / (2 * 5 * 11),
    'omega': -(1/2) * alpha_bare**2,
    'pdg': 493.677
})

# Каон K⁰: (2³·3²)/γ² = 72/γ²
particles.append({
    'name': 'Kaon (K⁰)',
    'class': 'Meson',
    'C': 2**3 * 3**2,         # 72
    'k': 2,
    'delta0': +(1/4) / (2**3 * 17),
    'omega': +(1/4) / ((2**4 * 3) * (2**4 * 3**3)),
    'pdg': 497.611
})

# D⁰ мезон: (2⁴·17)/γ² = 272/γ²
particles.append({
    'name': 'D-Meson (D⁰)',
    'class': 'Meson',
    'C': 2**4 * 17,           # 272
    'k': 2,
    'delta0': -(2/3) / (2 * 5 * 11),
    'omega': -(2/3) * gamma2 / (2**4 * 3**3),
    'pdg': 1864.84
})

# D⁺ мезон: (2⁴·17)/γ² = 272/γ²
particles.append({
    'name': 'D-Meson (D⁺)',
    'class': 'Meson',
    'C': 2**4 * 17,           # 272
    'k': 2,
    'delta0': -(1/2) / (2**3 * 17),
    'omega': +(4) / ((2 * 5 * 11) * (2**4 * 3**3)),
    'pdg': 1869.66
})

# B⁰ мезон: (2³·7)/γ⁴ = 56/γ⁴
particles.append({
    'name': 'B-Meson (B⁰)',
    'class': 'Meson',
    'C': 2**3 * 7,            # 56
    'k': 4,
    'delta0': +(2/3) / (2**3 * 7),
    'omega': +2 * gamma2 / (2**4 * 3**3),
    'pdg': 5279.66
})

# Bs⁰ мезон: (2³·7)/γ⁴ = 56/γ⁴
particles.append({
    'name': 'B-Meson (Bs⁰)',
    'class': 'Meson',
    'C': 2**3 * 7,            # 56
    'k': 4,
    'delta0': +math.pi / (2 * 5 * 11),
    'omega': +2 * alpha_bare**2,
    'pdg': 5366.93
})

# --- БАРИОНЫ ---
# Протон: (2³·17)/γ² = 136/γ²
particles.append({
    'name': 'Proton (p)',
    'class': 'Baryon',
    'C': 2**3 * 17,           # 136
    'k': 2,
    'delta0': +R_pole / (2 * 5 * 11),
    'omega': +(1/4) * R_av * gamma / (2**4 * 3**3)**2,
    'pdg': 938.272089
})

# Лямбда: (2·3⁴)/γ² = 162/γ²
particles.append({
    'name': 'Lambda (Λ)',
    'class': 'Baryon',
    'C': 2 * 3**4,            # 162
    'k': 2,
    'delta0': -(2/3) / (2**4 * 3**3),
    'omega': -math.sqrt(2*3) / (2**3 * 17)**2,
    'pdg': 1115.683
})

# Сигма: (2·3⁴)/γ² = 162/γ²
particles.append({
    'name': 'Sigma (Σ⁺)',
    'class': 'Baryon',
    'C': 2 * 3**4,            # 162
    'k': 2,
    'delta0': +math.sqrt(2*3) / (3 * 13),
    'omega': -math.pi * gamma2 / (2**4 * 3**3),
    'pdg': 1189.37
})

# Омега: (2·3²)/γ⁴ = 18/γ⁴
particles.append({
    'name': 'Omega (Ω⁻)',
    'class': 'Baryon',
    'C': 2 * 3**2,            # 18
    'k': 4,
    'delta0': -1 / (2**4 * 3**3),
    'omega': -(2/3) / (2**4 * 3**3)**2,
    'pdg': 1672.45
})

# --- БОЗОНЫ ---
# W: (2⁶)/γ⁶ = 64/γ⁶
particles.append({
    'name': 'W Boson',
    'class': 'Boson',
    'C': 2**6,                # 64
    'k': 6,
    'delta0': -R_av * gamma / (2**4 * 3**3),
    'omega': -(2/3) / ((2**3 * 7) * (2**4 * 3**3)),
    'pdg': 80360.0
})

# Z: (2³·3²)/γ⁶ = 72/γ⁶
particles.append({
    'name': 'Z Boson',
    'class': 'Boson',
    'C': 2**3 * 3**2,         # 72
    'k': 6,
    'delta0': +1 / (2**3 * 17),
    'omega': -(1/2) * alpha_bare**2,
    'pdg': 91188.0
})

# Хиггс: (3³)/γ⁷ = 27/γ⁷
particles.append({
    'name': 'Higgs (H⁰)',
    'class': 'Boson',
    'C': 3**3,                # 27
    'k': 7,
    'delta0': +R_av * gamma / (2 * 5 * 11),
    'omega': +math.pi / ((2 * 5 * 11) * (2**4 * 3**3)),
    'pdg': 125250.0
})

# ═══════════════════════════════════════════════════════════
# ВЫЧИСЛЕНИЕ
# ═══════════════════════════════════════════════════════════
print(f"\n{'Частица':<20} {'Класс':<8} {'C':>6} {'k':>3} {'Bare m/me':>12} {'Bare MeV':>12} "
      f"{'δ₀':>12} {'Ω':>12} {'Corrected':>12} {'PDG':>12} {'Err%':>8} {'Δ MeV':>10}")
print("-" * 140)

results = []
for p in particles:
    C = p['C']
    k = p['k']
    
    # Bare mass в единицах m_e
    if k >= 0:
        bare_me = C / gamma**k
    else:
        bare_me = C * gamma**(-k)  # отрицательная глубина = умножение на γ
    
    bare_mev = bare_me * m_e
    
    # Corrected = bare * (1 + δ₀ + Ω)
    d0 = p['delta0']
    om = p['omega']
    corrected_me = bare_me * (1 + d0 + om)
    corrected_mev = corrected_me * m_e
    
    pdg = p['pdg']
    err = (corrected_mev - pdg) / pdg * 100
    delta = corrected_mev - pdg
    
    results.append({
        'name': p['name'], 'class': p['class'], 'C': C, 'k': k,
        'bare_me': bare_me, 'bare_mev': bare_mev,
        'd0': d0, 'om': om,
        'corrected_mev': corrected_mev, 'pdg': pdg,
        'err': err, 'delta': delta
    })
    
    print(f"{p['name']:<20} {p['class']:<8} {C:>6} {k:>3} {bare_me:>12.3f} {bare_mev:>12.4f} "
          f"{d0:>+12.8f} {om:>+12.10f} {corrected_mev:>12.4f} {pdg:>12.4f} {err:>+8.4f}% {delta:>+10.4f}")

# ═══════════════════════════════════════════════════════════
# СТАТИСТИКА
# ═══════════════════════════════════════════════════════════
print(f"\n{'='*100}")
print("  СТАТИСТИКА")
print(f"{'='*100}")

# Фильтруем кварки (неточные экспериментальные данные)
leptons_mesons_baryons = [r for r in results if r['class'] != 'Quark']
quarks = [r for r in results if r['class'] == 'Quark']

print(f"\n  Лептоны + Мезоны + Барионы + Бозоны ({len(leptons_mesons_baryons)} частиц):")
for r in sorted(leptons_mesons_baryons, key=lambda x: abs(x['err'])):
    print(f"    {r['name']:<20} err = {r['err']:>+10.5f}%  Δ = {r['delta']:>+12.4f} МэВ")

avg_err = sum(abs(r['err']) for r in leptons_mesons_baryons) / len(leptons_mesons_baryons)
print(f"\n  Средняя |ошибка|: {avg_err:.5f}%")

print(f"\n  Кварки ({len(quarks)} частиц) — оценки current mass:")
for r in sorted(quarks, key=lambda x: abs(x['err'])):
    print(f"    {r['name']:<20} err = {r['err']:>+10.4f}%  Δ = {r['delta']:>+12.2f} МэВ")

# ═══════════════════════════════════════════════════════════
# АНАТОМИЯ ХВОСТОВ: δ₀ + Ω в процентах
# ═══════════════════════════════════════════════════════════
print(f"\n{'='*100}")
print("  АНАТОМИЯ ХВОСТОВ (в % от bare)")
print(f"{'='*100}")
print(f"{'Частица':<20} {'δ₀ (%)':>12} {'Ω (%)':>12} {'Суммарный хвост (%)':>20} {'Хвост в МэВ':>14}")
print("-" * 80)
for p, r in zip(particles, results):
    d0_pct = p['delta0'] * 100
    om_pct = p['omega'] * 100
    tail_pct = (p['delta0'] + p['omega']) * 100
    tail_mev = r['bare_mev'] * (p['delta0'] + p['omega'])
    print(f"{p['name']:<20} {d0_pct:>+12.6f}% {om_pct:>+12.8f}% {tail_pct:>+20.6f}% {tail_mev:>+14.4f} МэВ")
