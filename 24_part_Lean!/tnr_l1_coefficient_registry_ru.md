# Теоретическая карта Lean4-пакета `L1`

## Роль документа

Этот документ нужен не для популяризации слоя частиц, а для чтения Lean4-пакета
как теоретического объекта. Его задача — зафиксировать:

1. какие файлы Lean4 входят в пакет;
2. какую роль выполняет каждый файл;
3. на какие разделы базовой теории он должен опираться;
4. где находится честная граница между уже формализованной grammar и ещё не
   реализованным first-principles выводом.

Документ следует читать вместе с тремя базовыми файлами теории:

- [DOT_machine_architecture_overview_en.md](../en/DOT_machine_architecture_overview_en.md)
- [DOT_mathematical_framework_en.md](../en/DOT_mathematical_framework_en.md)
- [DOT_physical_realization_en.md](../en/DOT_physical_realization_en.md)

Именно на эти три файла должны ссылаться комментарии внутри Lean-кода.

## Главная граница current package

Текущий Lean4-пакет **не** выводит слой частиц из явного комбинаторного объекта
`K(2,2,2)` внутри proof layer. Он делает другое:

- фиксирует словарь слоя `L1`;
- фиксирует bare families и `γ`-глубины как канонический импортированный
  реестр;
- фиксирует operator paths, `δ₀`, `Ω`, `T`;
- собирает полный symbolic bundle для каждой из 24 частиц;
- доказывает внутреннюю согласованность этого symbolic слоя.

То есть пакет формализует **текущий закон слоя частиц**, но ещё не содержит
полного моста:

```text
K(2,2,2) -> lower floor -> packets -> γ -> bare numerators C -> L1
```

Эта граница должна быть названа прямо, иначе код выглядит как набор констант
без объяснения их статуса.

## Файлы пакета и их роль

### Корневая сборка

- `TnrFormal.lean`
  - точка входа пакета;
  - импортирует все подмодули и задаёт внешний контур formalization.

### Основание vocabulary

- `TnrFormal/Prelude.lean`
  - минимальный словарь нижнего слоя;
  - `Layer`, `FloorNode`, `StructuralPacket`;
  - это vocabulary lower floor, а не доказательство его происхождения.
  - теория:
    - `DOT_machine_architecture_overview_en.md`, разделы про lower floor и
      visible/shadow packets;
    - `DOT_mathematical_framework_en.md`, разделы про floor ladder.

- `TnrFormal/Octahedron.lean`
  - словарь октаэдрального reading:
    - `OctahedralPort`
    - `TopologyRegime`
    - `visibleShadowSeed`
  - explicit graph `K(2,2,2)` здесь пока **не** построен.
  - теория:
    - `DOT_machine_architecture_overview_en.md`, разделы про carrier и shell;
    - `DOT_mathematical_framework_en.md`, разделы про spectral octahedron.

- `TnrFormal/Constants.lean`
  - только символические имена `γ`, `α`, `Ry`, `Ry/3`;
  - numerical derivation в Lean не реализована.
  - теория:
    - `DOT_mathematical_framework_en.md`, разделы про `γ` и bare law;
    - `DOT_physical_realization_en.md`, разделы про `α`, `Ry`, `E_bond`.

- `TnrFormal/Axioms.lean`
  - локальный аксиоматический vocabulary proof layer;
  - это место для честного отделения imported assumptions от доказанной grammar.

- `TnrFormal/Carriers.lean`
  - перечисление `BareFamily`;
  - не вывод bare families, а их канонический список.
  - теория:
    - `DOT_physical_realization_en.md`, каталог реализованных баз;
    - `DOT_mathematical_framework_en.md`, bare mass law.

- `TnrFormal/Paths.lean`
  - `OperatorPath` и path-class layer;
  - описывает типы assembly-маршрутов, а не numerical readout.
  - теория:
    - `DOT_machine_architecture_overview_en.md`, части про structure / act /
      observation и particle layer;
    - `DOT_physical_realization_en.md`, path families.

### Центральный symbolic layer `L1`

- `TnrFormal/L1.lean`
  - центральный registry current particle layer;
  - фиксирует:
    - 24 частицы,
    - superpaths,
    - operator paths,
    - bare-family assignment.
  - это symbolic ontology слоя `L1`.

- `TnrFormal/L1Assembly.lean`
  - вводит `AssemblyShape`:
    - `identity`
    - `shifted`
    - `tailed`
  - это coarse operator reading.

- `TnrFormal/L1Registry.lean`
  - группирует частицы по assembly-family;
  - нужен для считывания структуры слоя и простых proof-of-count.

- `TnrFormal/L1Profiles.lean`
  - даёт semantic classifier path-ов:
    - `baseAlphabet`
    - `duplicationTransfer`
    - `continuationMellin`
    - `twistClosure`
  - это уже bridge между кодом и теоретическими ролями.

- `TnrFormal/L1Grammar.lean`
  - grammar-level описание допустимых series modes и special factors;
  - не содержит коэффициентов, а задаёт допустимую форму термов.

- `TnrFormal/L1Terms.lean`
  - finite alphabet `BB_k` и coarse term categories;
  - это vocabulary symbolic terms.

### Bare layer

- `TnrFormal/L1Bare.lean`
  - bare numerators `carrierCOf`
  - gamma-depth `gammaPowerOf`
  - честная граница:
    - эти величины **импортированы как canonical registry**;
    - внутри Lean они пока не выводятся из `K(2,2,2)`.
  - это ключевой boundary file всего пакета.

### Post-basis grammar

- `TnrFormal/L1Delta.lean`
  - symbolic terms для `δ₀` и `Ω`;
  - helper constructors:
    - `ratio`
    - `bbRatio`
    - `piRatio`
    - `sqrt6Ratio`
    - `ravgGammaRatio`
    - `alphaCouplingSq`
  - здесь лежит основная grammar shift/closure-layer.

- `TnrFormal/L1Tail.lean`
  - explicit tail registry `T`;
  - это узкий и редкий operator layer, который включается только там, где без
    него packet не замыкается.

- `TnrFormal/L1Unfolding.lean`
  - собирает full symbolic bundle частицы:
    - bare family
    - path
    - superpath
    - assembly
    - `δ₀`
    - `Ω`
    - `T`
  - это самый близкий к “полной формуле слоя” файл внутри Lean.

## Параметры и функции: что откуда берётся

### `carrierCOf`

Функция:

```lean
carrierCOf : BareFamily → Nat
```

Она задаёт bare numerator `C` каждой family. Сейчас это canonical imported
registry.

Примеры с factorization:

- `56 = 2^3 · 7`
- `72 = 2^3 · 3^2`
- `136 = 2^3 · 17`
- `162 = 2 · 3^4`
- `272 = 2^4 · 17`
- `3456 = 2^7 · 3^3`
- `6528 = 2^7 · 3 · 17`
- `1872 = 2^4 · 3^2 · 13`
- `18 = 2 · 3^2`
- `64 = 2^6`
- `27 = 3^3`

Теоретически этот слой должен в будущем опираться на:

- `DOT_mathematical_framework_en.md`
  - bare law
  - packet structure
  - spectral/metric section;
- `DOT_physical_realization_en.md`
  - catalogue of realized bases.

Но в current Lean-package это **не derivation**, а **registry**.

### `gammaPowerOf`

Функция:

```lean
gammaPowerOf : BareFamily → Int
```

Она задаёт tier-depth в bare law.

Это уже прямой entry point к claim-у:

```text
M_bare = C / γ^k * m_e
```

Но в current package:
- `γ` символически назван;
- `k` задан registry-слоем;
- proof of origin of `γ` is not yet inside Lean.

### `superpathOf`, `operatorPathOf`, `assemblyShapeOfSuperpath`

Это основной symbolic skeleton current `L1`.

Он отвечает на вопрос:
- **как собирается частица**

а не на вопрос:
- **почему именно такой bare numerator появляется у носителя**.

То есть здесь formalization уже сильная:
- path-grammar закреплена;
- path/superpath/assembly relations доказуемы `rfl`-уровнем;
- слой не разваливается на ad hoc terms.

### `d0TermsOfParticle`

Это registry локального shift layer `δ₀`.

Здесь важно:
- коэффициенты уже factorized inline;
- допускаются только конечные типы term-ов;
- это не raw expression soup, а finite symbolic grammar.

Теория:
- `DOT_mathematical_framework_en.md`
  - sections on `δ₀`
  - post-basis law
- `DOT_physical_realization_en.md`
  - particle layer deployment

### `omegaTermsOfParticle`

Это closure field `Ω`.

Его правильный статус в теории:
- continuation / closure layer
- аналитическое поле замыкания
- модовый / резонансный слой

Но важно:
- current Lean still stores it symbolically;
- rare heavy denominators не выводятся, а только перечисляются.

### `tailTermsOfParticle`

Это explicit tail `T`.

Его статус:
- не общая судьба всех частиц;
- редкий operator layer;
- включается только у части packet-ов.

Именно поэтому этот слой должен быть документирован отдельно, а не смешан с
`δ₀` и `Ω`.

### `bundleOf`

Это главный assembly-point current package.

Функция:

```lean
bundleOf : ParticleName → L1Bundle
```

собирает:
- bare family,
- path,
- superpath,
- assembly,
- `δ₀`,
- `Ω`,
- `T`.

Если смотреть на пакет целиком, именно `bundleOf` — это current formal analogue
of the statement:

> каждая частица есть конечная assembled packet-конфигурация, а не отдельная
> произвольная формула.

## Что в Lean уже доказано, а что нет

### Уже зафиксировано

- vocabulary lower floor и carrier layer;
- список bare families;
- symbolic particle registry;
- path and superpath grammar;
- assembly classification;
- symbolic `δ₀`, `Ω`, `T`;
- полный unfolding bundle для каждой частицы;
- локальная согласованность этих слоёв.

### Пока не реализовано

- explicit graph object `K(2,2,2)` как working structure;
- spectral theorem inside Lean;
- derivation of `γ = √6 / 9` inside Lean;
- derivation of `24 / 48 / 23 / 47` inside Lean;
- bridge theorem:
  - `octahedral floor -> packets -> bare numerators C`.

То есть current package formalizes:

```text
canonical L1 symbolic law
```

но ещё не formalizes:

```text
full octahedral first-principles derivation of that law
```

## Почему factorization важна

Если оставить bare numerators и rare denominators просто как голые числа,
Lean-пакет читается как opaque registry.

Если разложить их на простые множители, сразу видно:

- конечный alphabet prime packets;
- повторяющиеся packet families;
- короткие numerator motifs:
  - `2^3 · 7`
  - `2^3 · 17`
  - `2 · 3^4`
  - `2^3 · 3^2`

Это ещё не вывод из октаэдра, но это уже промежуточный мост:

```text
opaque integer -> prime packet -> carrier alphabet -> topology claim
```

Именно поэтому factorization layer — обязательная часть читаемого Lean-пакета.

## Практический verdict

Текущий Lean4-комплект уже полезен и силён как:
- formalization of the current symbolic `L1` law;
- registry of packet families and paths;
- proof that assembly grammar is internally coherent.

Но он ещё не является:
- formal derivation of `L1` from octahedral first principles.

Поэтому правильный способ читать пакет сейчас такой:

1. сначала overview и mathematical framework;
2. затем `L1`, `L1Bare`, `L1Grammar`, `L1Delta`, `L1Tail`;
3. затем `L1Unfolding` как итоговый assembled layer.

Именно в этом порядке становится видно, что в пакете уже доказано, а что пока
остаётся импортированной канонической основой.
