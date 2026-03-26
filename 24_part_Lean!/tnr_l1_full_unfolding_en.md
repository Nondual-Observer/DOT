# DOT: Full `L1` Unfolding Without Formal Proofs

This document provides a direct unfolding of the current `L1` without formal
proofs and without additional explanatory text. Only the carrier basis, assembly
path, `δ₀`, `Ω`, `T`, and the final scheme for all `24` particles are recorded
here.

## General Law

```text
M = B
M = B · exp(δ₀ + Ω)
M = B · exp(δ₀ + Ω) · T
```

where:

- `B` — carrier basis;
- `δ₀ + Ω` — shift grammar;
- `T` — tail grammar.

Below, particles are unfolded by `5` superpaths and `15` operator paths exactly
as currently implemented in the engine.

## I. Base Identity

| Particle | Path | Basis | `δ₀` | `Ω` | `T` | Assembly |
| --- | --- | --- | --- | --- | --- | --- |
| `e⁻` | `anchor.identity.direct` | `e` | `0` | `0` | `0` | `M = B` |

### e⁻

- source: `1·mₑ`
- carrier family: `electron_anchor`
- state: `default`
- variant: `electron_anchor`
- basis: `B = e`
- `δ₀ = 0`
- `Ω = 0`
- `T = 0`
- full assembly: `M = e`

## II. Single Lift

| Particle | Path | Basis | `δ₀` | `Ω` | `T` | Assembly |
| --- | --- | --- | --- | --- | --- | --- |
| `Muon (μ)` | `lepton.bridge.single` | `56/γ` | `0` | `1·BB5·α·γ^-1 + 1·BB7·α^2·γ^-1 / (56 · 24) + 1·BB11·α^2·γ^-1 / (56 · 120)` | `0` | `M = B · exp(δ₀ + Ω)` |
| `Proton (p)` | `baryon.proton.single_lift` | `136/γ^2` | `-1·BB7·α / (7) + -1·BB5·α^2 / (120 · 17) + 1·BB3·α^2 / (47 · 252) + 1·BB10·α^2 / (47 · 1728)` | `0` | `0` | `M = B · exp(δ₀ + Ω)` |

### Muon (μ)

- source: `56/γ · exp(δ₀+Ω)`
- carrier family: `muon_bridge`
- state: `default`
- variant: `muon_mode`
- basis: `B = 56/γ`
- `δ₀ = 0`
- `Ω = 1·BB5·α·γ^-1 + 1·BB7·α^2·γ^-1 / (56 · 24) + 1·BB11·α^2·γ^-1 / (56 · 120)`
- `T = 0`
- full assembly: `M = 56/γ · exp(δ₀ + Ω)`

### Proton (p)

- source: `136/γ² bb7+bb5`
- carrier family: `nucleon_seed`
- state: `proton`
- variant: `proton_mode`
- basis: `B = 136/γ^2`
- `δ₀ = -1·BB7·α / (7) + -1·BB5·α^2 / (120 · 17) + 1·BB3·α^2 / (47 · 252) + 1·BB10·α^2 / (47 · 1728)`
- `Ω = 0`
- `T = 0`
- full assembly: `M = 136/γ^2 · exp(δ₀ + Ω)`

## III. Dual-Shift Family

| Particle | Path | Basis | `δ₀` | `Ω` | `T` | Assembly |
| --- | --- | --- | --- | --- | --- | --- |
| `Tau (τ)` | `lepton.bulk.dual` | `3456` | `2/3 / (110)` | `3 / (110 · 432)` | `0` | `M = B · exp(δ₀ + Ω)` |
| `u-quark` | `quark.seed.dual` | `56·γ^2` | `1 / (3136)` | `3 / (162)` | `0` | `M = B · exp(δ₀ + Ω)` |
| `d-quark` | `quark.seed.dual` | `6528·γ^5` | `-1/4 / (39)` | `-1·π / (54)` | `0` | `M = B · exp(δ₀ + Ω)` |
| `s-quark` | `quark.seed.dual` | `4/γ^3` | `-1 / (12)` | `4 / (3136)` | `0` | `M = B · exp(δ₀ + Ω)` |
| `c-quark` | `quark.seed.dual` | `48/γ^3` | `-1 / (162)` | `1·π / (64)` | `0` | `M = B · exp(δ₀ + Ω)` |
| `b-quark` | `quark.seed.dual` | `162/γ^3` | `1 / (56)` | `-2 / (59319)` | `0` | `M = B · exp(δ₀ + Ω)` |
| `Top (t)` | `quark.seed.dual` | `1872/γ^4` | `-1 / (110)` | `-1·r_avg·γ / (81)` | `0` | `M = B · exp(δ₀ + Ω)` |
| `Baryon Σ⁺` | `baryon.sigma.dual_lift` | `162/γ^2` | `3 / (48)` | `-1/3 / (1521)` | `0` | `M = B · exp(δ₀ + Ω)` |
| `Baryon Ω⁻` | `baryon.bulk.dual` | `18/γ^4` | `-1 / (432)` | `-2/3 / (186624)` | `0` | `M = B · exp(δ₀ + Ω)` |
| `Boson W±` | `boson.gauge.dual` | `64/γ^6` | `-1/3 / (162)` | `4 / (4096)` | `0` | `M = B · exp(δ₀ + Ω)` |
| `Higgs Boson (H⁰)` | `boson.scalar.dual` | `27/γ^7` | `1·√6 / (576)` | `-1·γ-tail·γ^2 / (1521)` | `0` | `M = B · exp(δ₀ + Ω)` |

### Tau (τ)

- source: `3456 · exp(δ₀+Ω)`
- carrier family: `tau_bulk`
- state: `default`
- variant: `tau_mode`
- basis: `B = 3456`
- `δ₀ = 2/3 / (110)`
- `Ω = 3 / (110 · 432)`
- `T = 0`
- full assembly: `M = 3456 · exp(δ₀ + Ω)`

### u-quark

- source: `56·γ²`
- carrier family: `u_seed`
- state: `default`
- variant: `u_mode`
- basis: `B = 56·γ^2`
- `δ₀ = 1 / (3136)`
- `Ω = 3 / (162)`
- `T = 0`
- full assembly: `M = 56·γ^2 · exp(δ₀ + Ω)`

### d-quark

- source: `6528·γ⁵`
- carrier family: `d_seed`
- state: `default`
- variant: `d_mode`
- basis: `B = 6528·γ^5`
- `δ₀ = -1/4 / (39)`
- `Ω = -1·π / (54)`
- `T = 0`
- full assembly: `M = 6528·γ^5 · exp(δ₀ + Ω)`

### s-quark

- source: `4/γ³`
- carrier family: `s_seed`
- state: `default`
- variant: `s_mode`
- basis: `B = 4/γ^3`
- `δ₀ = -1 / (12)`
- `Ω = 4 / (3136)`
- `T = 0`
- full assembly: `M = 4/γ^3 · exp(δ₀ + Ω)`

### c-quark

- source: `48/γ³`
- carrier family: `c_seed`
- state: `default`
- variant: `c_mode`
- basis: `B = 48/γ^3`
- `δ₀ = -1 / (162)`
- `Ω = 1·π / (64)`
- `T = 0`
- full assembly: `M = 48/γ^3 · exp(δ₀ + Ω)`

### b-quark

- source: `162/γ³`
- carrier family: `b_seed`
- state: `default`
- variant: `b_mode`
- basis: `B = 162/γ^3`
- `δ₀ = 1 / (56)`
- `Ω = -2 / (59319)`
- `T = 0`
- full assembly: `M = 162/γ^3 · exp(δ₀ + Ω)`

### Top (t)

- source: `1872/γ⁴`
- carrier family: `t_seed`
- state: `default`
- variant: `t_mode`
- basis: `B = 1872/γ^4`
- `δ₀ = -1 / (110)`
- `Ω = -1·r_avg·γ / (81)`
- `T = 0`
- full assembly: `M = 1872/γ^4 · exp(δ₀ + Ω)`

### Baryon Σ⁺

- source: `162/γ²`
- carrier family: `lambda_sigma_seed`
- state: `sigma`
- variant: `sigma_mode`
- basis: `B = 162/γ^2`
- `δ₀ = 3 / (48)`
- `Ω = -1/3 / (1521)`
- `T = 0`
- full assembly: `M = 162/γ^2 · exp(δ₀ + Ω)`

### Baryon Ω⁻

- source: `18/γ⁴`
- carrier family: `omega_seed`
- state: `default`
- variant: `omega_mode`
- basis: `B = 18/γ^4`
- `δ₀ = -1 / (432)`
- `Ω = -2/3 / (186624)`
- `T = 0`
- full assembly: `M = 18/γ^4 · exp(δ₀ + Ω)`

### Boson W±

- source: `64/γ⁶`
- carrier family: `w_seed`
- state: `default`
- variant: `w_mode`
- basis: `B = 64/γ^6`
- `δ₀ = -1/3 / (162)`
- `Ω = 4 / (4096)`
- `T = 0`
- full assembly: `M = 64/γ^6 · exp(δ₀ + Ω)`

### Higgs Boson (H⁰)

- source: `27/γ⁷`
- carrier family: `higgs_seed`
- state: `default`
- variant: `higgs_mode`
- basis: `B = 27/γ^7`
- `δ₀ = 1·√6 / (576)`
- `Ω = -1·γ-tail·γ^2 / (1521)`
- `T = 0`
- full assembly: `M = 27/γ^7 · exp(δ₀ + Ω)`

## IV. Tail Closure Family

| Particle | Path | Basis | `δ₀` | `Ω` | `T` | Assembly |
| --- | --- | --- | --- | --- | --- | --- |
| `Pion (π⁰)` | `meson.neutral.tail_closure` | `72/γ` | `-2/3 / (432)` | `1/3 / (136 · 110)` | `1·BB6·γ^3 / (12 · 119)` | `M = B · exp(δ₀ + Ω) · T` |
| `Kaon (K⁺)` | `meson.charged.tail_closure` | `72/γ^2` | `-2/3 / (110)` | `-1/2·α_coupling²` | `-1·BB19·γ / (240 · 353)` | `M = B · exp(δ₀ + Ω) · T` |
| `Kaon (K⁰)` | `meson.neutral.tail_closure` | `72/γ^2` | `1/4 / (136)` | `1/4 / (48 · 432)` | `1·BB11·α / (120 · 55)` | `M = B · exp(δ₀ + Ω) · T` |
| `Meson D⁰` | `meson.neutral.tail_closure` | `272/γ^2` | `-2/3 / (110)` | `-2/3·γ-tail·γ^2 / (432)` | `1·BB15·γ / (120 · 221)` | `M = B · exp(δ₀ + Ω) · T` |
| `Meson D⁺` | `meson.charged.tail_closure` | `272/γ^2` | `-1/2 / (136)` | `4 / (110 · 432)` | `1·BB22·γ^3 / (252 · 412)` | `M = B · exp(δ₀ + Ω) · T` |
| `Meson B⁰` | `meson.neutral.tail_closure` | `56/γ^4` | `1 / (81)` | `-1/6 / (2304)` | `1·γ-tail·α·γ / (6176)` | `M = B · exp(δ₀ + Ω) · T` |
| `Meson Bs⁰` | `meson.strange.tail_closure` | `56/γ^4` | `1·π / (110)` | `2·α_coupling²` | `1·BB14·γ^2 / (120 · 273)` | `M = B · exp(δ₀ + Ω) · T` |
| `Baryon Λ` | `baryon.lambda.tail_closure` | `162/γ^2` | `-2/3 / (432)` | `-1·√6 / (18496)` | `1·BB3·γ^3 / (12 · 224)` | `M = B · exp(δ₀ + Ω) · T` |
| `Boson Z⁰` | `boson.gauge.tail_closure` | `72/γ^6` | `1 / (136)` | `-1/2·α_coupling²` | `1·BB14·γ^3 / (252 · 58)` | `M = B · exp(δ₀ + Ω) · T` |

### Pion (π⁰)

- source: `72/γ · 3-layer + ζ-tail`
- carrier family: `pion_seed`
- state: `default`
- variant: `pion_mode`
- basis: `B = 72/γ`
- `δ₀ = -2/3 / (432)`
- `Ω = 1/3 / (136 · 110)`
- `T = 1·BB6·γ^3 / (12 · 119)`
- full assembly: `M = 72/γ · exp(δ₀ + Ω) · T`

### Kaon (K⁺)

- source: `72/γ² + ζ-tail`
- carrier family: `kaon_seed`
- state: `plus`
- variant: `kaon_plus_mode`
- basis: `B = 72/γ^2`
- `δ₀ = -2/3 / (110)`
- `Ω = -1/2·α_coupling²`
- `T = -1·BB19·γ / (240 · 353)`
- full assembly: `M = 72/γ^2 · exp(δ₀ + Ω) · T`

### Kaon (K⁰)

- source: `72/γ² + ζ-tail`
- carrier family: `kaon_seed`
- state: `zero`
- variant: `kaon_zero_mode`
- basis: `B = 72/γ^2`
- `δ₀ = 1/4 / (136)`
- `Ω = 1/4 / (48 · 432)`
- `T = 1·BB11·α / (120 · 55)`
- full assembly: `M = 72/γ^2 · exp(δ₀ + Ω) · T`

### Meson D⁰

- source: `272/γ² + ζ-tail`
- carrier family: `d_meson_seed`
- state: `zero`
- variant: `d0_mode`
- basis: `B = 272/γ^2`
- `δ₀ = -2/3 / (110)`
- `Ω = -2/3·γ-tail·γ^2 / (432)`
- `T = 1·BB15·γ / (120 · 221)`
- full assembly: `M = 272/γ^2 · exp(δ₀ + Ω) · T`

### Meson D⁺

- source: `272/γ² + ζ-tail`
- carrier family: `d_meson_seed`
- state: `plus`
- variant: `dplus_mode`
- basis: `B = 272/γ^2`
- `δ₀ = -1/2 / (136)`
- `Ω = 4 / (110 · 432)`
- `T = 1·BB22·γ^3 / (252 · 412)`
- full assembly: `M = 272/γ^2 · exp(δ₀ + Ω) · T`

### Meson B⁰

- source: `56/γ⁴ + ζ-tail`
- carrier family: `b_meson_seed`
- state: `zero`
- variant: `b0_mode`
- basis: `B = 56/γ^4`
- `δ₀ = 1 / (81)`
- `Ω = -1/6 / (2304)`
- `T = 1·γ-tail·α·γ / (6176)`
- full assembly: `M = 56/γ^4 · exp(δ₀ + Ω) · T`

### Meson Bs⁰

- source: `56/γ⁴ + ζ-tail`
- carrier family: `b_meson_seed`
- state: `strange`
- variant: `bs_mode`
- basis: `B = 56/γ^4`
- `δ₀ = 1·π / (110)`
- `Ω = 2·α_coupling²`
- `T = 1·BB14·γ^2 / (120 · 273)`
- full assembly: `M = 56/γ^4 · exp(δ₀ + Ω) · T`

### Baryon Λ

- source: `162/γ² + ζ-tail`
- carrier family: `lambda_sigma_seed`
- state: `lambda`
- variant: `lambda_mode`
- basis: `B = 162/γ^2`
- `δ₀ = -2/3 / (432)`
- `Ω = -1·√6 / (18496)`
- `T = 1·BB3·γ^3 / (12 · 224)`
- full assembly: `M = 162/γ^2 · exp(δ₀ + Ω) · T`

### Boson Z⁰

- source: `72/γ⁶ + ζ-tail`
- carrier family: `z_seed`
- state: `default`
- variant: `z_mode`
- basis: `B = 72/γ^6`
- `δ₀ = 1 / (136)`
- `Ω = -1/2·α_coupling²`
- `T = 1·BB14·γ^3 / (252 · 58)`
- full assembly: `M = 72/γ^6 · exp(δ₀ + Ω) · T`

## V. Shadow Tail Family

| Particle | Path | Basis | `δ₀` | `Ω` | `T` | Assembly |
| --- | --- | --- | --- | --- | --- | --- |
| `Neutron (n)` | `baryon.neutron.shadow_tail` | `136/γ^2` | `1 / (684) + -1·BB2·α / (120 · 9)` | `0` | `-1·BB4·α^2 / (1080 · 1098)` | `M = B · exp(δ₀ + Ω) · T` |

### Neutron (n)

- source: `136/γ² bb2 + 3rd-layer`
- carrier family: `nucleon_seed`
- state: `neutron`
- variant: `neutron_mode`
- basis: `B = 136/γ^2`
- `δ₀ = 1 / (684) + -1·BB2·α / (120 · 9)`
- `Ω = 0`
- `T = -1·BB4·α^2 / (1080 · 1098)`
- full assembly: `M = 136/γ^2 · exp(δ₀ + Ω) · T`

## Structural Summary

- particles: `24`
- operator paths: `15`
- superpaths: `5`
- the layer is now unfolded not as a mass catalogue, but as a finite fabric of
  `carrier basis -> path -> assembly`.
