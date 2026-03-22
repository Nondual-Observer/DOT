# Теория Наблюдаемого Различения: Code Availability

**Статус:** editorial reproducibility note  
**Дата:** 22.03.2026  
**Назначение:** зафиксировать, какие companion scripts существуют для проверки численных результатов ТНР и каков их статус по отношению к main manuscript.

---

К этому manuscript bundle приложен companion code layer. Его задача — **воспроизводимость численных результатов**, а не замена формальных derivation-блоков.

Код покрывает три класса задач:

1. **Проверка численных таблиц микрофизики**
   - bare-address calculations;
   - tail evaluations;
   - audit tables для частиц и констант.

2. **Проверка отдельных макро-вычислений**
   - arithmetic shell factors;
   - gravity-bridge numerics;
   - horizon-fraction checks.

3. **Exploratory ТНР chemistry**
   - атомные и гидридные readout-модели;
   - bond-domain / lone-pair / aperture logic;
   - ограниченная multi-center ветка для углеводородов $C_2H_n$ (разложение $C\!-\!C$ на $\sigma/\pi$ и hybridization-readout на инвариантах $2/3$ и $\gamma^2$);
   - проверка воспроизводимости для ограниченного класса молекул.

Важно различать:

- **main manuscript** — формальные derivations, статус которых фиксируется маркерами `[Д] / [Г1] / [Г2]`;
- **companion code** — инструменты проверки численных следствий и exploratory-модели.

Следовательно:

- совпадение чисел в коде **не заменяет** строгого доказательства;
- но оно является существенным элементом **reproducibility**;
- и позволяет отдельно тестировать устойчивость ТНР-readout’ов на новых данных.

Для publishable версии рекомендуется сопровождать manuscript:

- либо публичным репозиторием со snapshot/tag;
- либо архивным слепком (например, Zenodo);
- либо отдельной project page с замороженной версией скриптов.

Код не должен внедряться в основное тело статей как длинные листинги. Достаточно:

- краткой ссылки на code archive;
- указания, какие таблицы и главы проверяются какими скриптами;
- явного разграничения между formal derivation и numerical verification.

В текущем корпусе companion scripts следует понимать именно в этом смысле:  
**как слой воспроизводимости, контроля и расширения, но не как отдельный источник аксиом.**

---

*Companion code note for the ТНР draft manuscript*  
*22 марта 2026*

## Числовой snapshot (chemistry, draft)

Ниже приведён **проверочный** snapshot для “атомно-гидридной” и ограниченной multi-center ветки. Это **черновой** уровень: модель не претендует на универсальность по всей химии; при замыкании многоцентровой phase-selection логики точность потенциально может быть существенно повышена.

**Скрипт:** `scripts/tnr_hydrogen_dynamic_v10.py`  
**Внутренние константы, используемые моделью:**

- $\gamma = \sqrt{6}/9 \approx 0.27216553$, $\gamma^2 = 2/27 \approx 0.07407407$
- $\alpha^{-1} \approx 137.036101$
- $Ry \approx 13.605673$ eV, $E_{\text{bond}} = Ry/3 \approx 4.535224$ eV

Скрипт также печатает **внутреннюю декомпозицию** для каждого кейса (например, $E_{\text{radial}}$, $E_{\text{ortho}}$, period/aperture-факторы для гидридов; $E_{CH}$ и $E_{CC,\sigma/\pi}$ для $C_2H_n$), что позволяет проверять не только итоговую энергию, но и “внутренние каналы” модели.

**Точность (на текущем benchmark-наборе):**

- Mean $|\%|$ error (resolved) $\approx 0.34\%$.
- $H_2$ (точная ветка) $\approx 0.03\%$.
- Multi-center $C_2H_n$ (ограниченная ветка) сейчас даёт: $C_2H_6 \approx 0.36\%$, $C_2H_4 \approx 0.03\%$.
- Ветка `candidate-s-block` (например, `LiH`) помечена как **не замкнутая** и не считается “resolved”.

| Молекула | Mode | ТНР (eV) | Ref (eV) | Err% |
|---|---|---:|---:|---:|
| $H_2$ | exact-h2 | 4.4792 | 4.4780 | +0.03 |
| LiH | candidate-s-block | 2.5196 | 2.5150 | +0.18 |
| HF | bond-domain | 5.8308 | 5.8700 | -0.67 |
| $H_2O$ | bond-domain | 9.5744 | 9.5100 | +0.68 |
| $NH_3$ | bond-domain | 11.9260 | 11.9500 | -0.20 |
| $CH_4$ | bond-domain | 17.0045 | 17.0200 | -0.09 |
| $SiH_4$ | bond-domain | 13.0638 | 13.0700 | -0.05 |
| $PH_3$ | bond-domain | 9.9145 | 10.0000 | -0.86 |
| $H_2S$ | bond-domain | 7.5260 | 7.5700 | -0.58 |
| HCl | bond-domain | 4.4134 | 4.4300 | -0.38 |
| HBr | bond-domain | 3.7573 | 3.7600 | -0.07 |
| HI | bond-domain | 3.0717 | 3.0600 | +0.38 |
| $C_2H_6$ | multi-center-2c | 29.7060 | 29.6000 | +0.36 |
| $C_2H_4$ | multi-center-2c | 24.6918 | 24.7000 | -0.03 |

## Единая точка входа (companion dashboard)

Чтобы не разводить десятки скриптов в тексте, в репозитории companion‑кода есть **один entrypoint**, который оркестрирует расчёты:

- `scripts/dot_companion_verify.py --chem` (exploratory chemistry, v10)
- `scripts/dot_companion_verify.py --full` (legacy unified verification dashboard)
- `scripts/dot_companion_verify.py --tails` (legacy tail calculator)
- `scripts/dot_companion_verify.py --vacuum64` (legacy 64-state engine)
- `scripts/dot_companion_verify.py --all` (прогон всего набора по порядку)
- `scripts/dot_companion_verify.py --hydrogen-dyn` (legacy динамика водорода: evolution состояния, популяции возбуждённого/основного уровня, энтропия, нагрузки каналов)

Важно: ветки `legacy:*` зафиксированы как snapshot/дашборд (там смешаны exact identities, baseline predictions и candidate layers). Они полезны для воспроизводимости и диагностики, но не заменяют статусы `[Д]/[Г1]/[Г2]` в основном корпусе.
