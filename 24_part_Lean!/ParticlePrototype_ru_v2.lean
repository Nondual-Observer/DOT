import TnrFormal.L1
import TnrFormal.L1Bare
import TnrFormal.L1Reference

open TnrFormal

-- Repository: https://github.com/Nondual-Observer/DOT

def repoUrlRu : String :=
  "https://github.com/Nondual-Observer/DOT"

def freshnessNoteRu : String :=
  "Текущий импортированный snapshot пакета; при появлении более новых таблиц PDG слой нужно обновить."

def allParticlesRu : List ParticleName := [
  .electron, .muon, .tau,
  .upQuark, .downQuark, .strangeQuark, .charmQuark, .bottomQuark, .topQuark,
  .pionZero, .kaonPlus, .kaonZero, .dMesonZero, .dMesonPlus, .bMesonZero, .bsMesonZero,
  .proton, .neutron, .lambda, .sigmaPlus, .omegaMinus,
  .wBoson, .zBoson, .higgs
]

def highlightedParticlesRu : List ParticleName := [
  .electron, .muon, .downQuark, .strangeQuark, .sigmaPlus, .higgs
]

def bareSummaryLinesRu : List String := [
  "--- Сводка по bare-слою ---",
  "Грамматика коэффициентов: минимальные low-prime packets, с доминированием 2 и 3 и редкими расширениями через 7 и 17.",
  "Грамматика уровней: один общий спектральный инвариант γ = √6/9.",
  "Правило выбора: каждый показанный пакет — текущий минимальный bare-family packet, который использует реестр для своего семейства.",
  "Наибольшие bare-отклонения возникают в более глубоких γ^3-секторах и в составных baryon-секторах.",
  "То есть менее точные bare-случаи не случайны: они сидят глубже в иерархии или несут более составную структуру.",
  "Сводка bare-ошибок по всем 24 частицам: mean |error| = 1.6222%, median |error| = 0.6105%, max |error| = 8.5510%."
]

def introLinesRu : List String := [
  "--- DOTheory: русский Lean-вход по bare-формулам и reference-данным ---",
  s!"Репозиторий      : {repoUrlRu}",
  s!"Набор данных     : {l1ReferenceDataset}",
  s!"Актуальность     : {freshnessNoteRu}",
  "Что показывает этот файл:",
  "  1) bare-формулу, формализованную в Lean",
  "  2) сырую массу, которую даёт bare-носитель",
  "  3) финальное значение текущего пакета L1",
  "  4) reference-массу и uncertainty",
  ""
]

def psLinesRu : List String := [
  "P.S. Ещё одна забавная вещь: скрипт как будто всё время намекает, что там должен быть ещё один тяжёлый узел.",
  "Может, я просто вижу паттерны там, где их нет, но больше всего ему как будто нравится Ω_ccc^{++}.",
  ""
]

def categoryRu (s : String) : String :=
  match s with
  | "lepton" => "лептон"
  | "quark" => "кварк"
  | "meson" => "мезон"
  | "baryon" => "барион"
  | "gauge_boson" => "калибровочный бозон"
  | "scalar_boson" => "скалярный бозон"
  | _ => s

def particleLabelRu : ParticleName → String
  | .electron => "Электрон (e⁻)"
  | .muon => "Мюон (μ)"
  | .tau => "Тау (τ)"
  | .upQuark => "u-кварк"
  | .downQuark => "d-кварк"
  | .strangeQuark => "s-кварк"
  | .charmQuark => "c-кварк"
  | .bottomQuark => "b-кварк"
  | .topQuark => "t-кварк"
  | .pionZero => "Пион (π⁰)"
  | .kaonPlus => "Каон (K⁺)"
  | .kaonZero => "Каон (K⁰)"
  | .dMesonZero => "D⁰-мезон"
  | .dMesonPlus => "D⁺-мезон"
  | .bMesonZero => "B⁰-мезон"
  | .bsMesonZero => "B_s⁰-мезон"
  | .proton => "Протон (p)"
  | .neutron => "Нейтрон (n)"
  | .lambda => "Λ-барион"
  | .sigmaPlus => "Σ⁺-барион"
  | .omegaMinus => "Ω⁻-барион"
  | .wBoson => "W±-бозон"
  | .zBoson => "Z⁰-бозон"
  | .higgs => "Бозон Хиггса (H⁰)"

def baseMassStringRu (p : ParticleName) : String :=
  let fam := bareFamilyOf p
  let c := carrierCOf fam
  let k := gammaPowerOf fam
  if k = 0 then
    s!"C = {c}, глубина (k) = {k}  =>  M_bare = {c}·m_e"
  else if k > 0 then
    s!"C = {c}, глубина (k) = {k}  =>  M_bare = {c}·γ^{k}·m_e"
  else
    let absK : Nat := Int.natAbs k
    if absK = 1 then
      s!"C = {c}, глубина (k) = {k}  =>  M_bare = {c}/γ·m_e"
    else
      s!"C = {c}, глубина (k) = {k}  =>  M_bare = {c}/γ^{absK}·m_e"

def particleReportLinesRu (p : ParticleName) : List String :=
  let ref := l1ReferenceOf p
  let formula := baseMassStringRu p
  [ s!"{particleLabelRu p} [{categoryRu ref.category}]"
  , s!"  bare carrier : {formula}"
  , s!"  source law   : {ref.sourceFormula}"
  , s!"  bare mass    : {ref.bareMeV} MeV   (ошибка {ref.bareErrorPct} относительно reference)"
  , s!"  final L1     : {ref.finalMeV} MeV   (ошибка {ref.finalErrorPct} относительно reference)"
  , s!"  reference    : {ref.referenceMeV} ± {ref.referenceUncMeV} MeV"
  , s!"  dataset      : {l1ReferenceDataset}"
  , ""
  ]

def emitBlockRu (xs : List String) : IO Unit := do
  for x in xs do
    IO.println x

def emitParticleListRu (xs : List ParticleName) : IO Unit := do
  for p in xs do
    emitBlockRu (particleReportLinesRu p)

def main : IO Unit := do
  emitBlockRu introLinesRu
  emitBlockRu ["Короткие примеры:"]
  emitParticleListRu highlightedParticlesRu
  emitBlockRu psLinesRu
  emitBlockRu ["--- Полная таблица из 24 частиц ---"]
  emitParticleListRu allParticlesRu
  emitBlockRu bareSummaryLinesRu
  IO.println "--- Конец русской таблицы DOTheory ---"
