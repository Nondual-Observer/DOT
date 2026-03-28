import TnrFormal.L1
import TnrFormal.L1Bare
import TnrFormal.L1Reference

open TnrFormal

-- Repository: https://github.com/Nondual-Observer/DOT

/-- URL репозитория для заголовка отчёта. -/
def repoUrlRu : String :=
  "https://github.com/Nondual-Observer/DOT"

/-- Русская локальная формулировка свежести reference-слоя. -/
def freshnessNoteRu : String :=
  "Текущий импортированный snapshot пакета; при появлении более новых таблиц PDG слой нужно обновить."

/-- Полный список 24 канонических частиц слоя `L1`. -/
def allParticlesRu : List ParticleName := [
  .electron, .muon, .tau,
  .upQuark, .downQuark, .strangeQuark, .charmQuark, .bottomQuark, .topQuark,
  .pionZero, .kaonPlus, .kaonZero, .dMesonZero, .dMesonPlus, .bMesonZero, .bsMesonZero,
  .proton, .neutron, .lambda, .sigmaPlus, .omegaMinus,
  .wBoson, .zBoson, .higgs
]

/--
Небольшой набор частиц, который показывается сначала.
Он нужен для быстрого входа:
- якорный точный случай;
- хороший bridge-case;
- кваark-узлы с заметной bare-ошибкой;
- тяжёлый baryon-case;
- high-energy boson-case.
-/
def highlightedParticlesRu : List ParticleName := [
  .electron, .muon, .downQuark, .strangeQuark, .sigmaPlus, .higgs
]

/-- Русская подпись для particle category. -/
def categoryRu (s : String) : String :=
  match s with
  | "lepton" => "лептон"
  | "quark" => "кварк"
  | "meson" => "мезон"
  | "baryon" => "барион"
  | "gauge_boson" => "калибровочный бозон"
  | "scalar_boson" => "скалярный бозон"
  | _ => s

/-- Русская подпись частицы для читаемого отчёта. -/
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

/-- Строка bare-представления массы для частицы. -/
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

/-- Читаемый русский многострочный отчёт по одной частице. -/
def particleReportStringRu (p : ParticleName) : String :=
  let ref := l1ReferenceOf p
  let formula := baseMassStringRu p
  String.intercalate "\n"
    [ s!"{particleLabelRu p} [{categoryRu ref.category}]"
    , s!"  bare carrier : {formula}"
    , s!"  source law   : {ref.sourceFormula}"
    , s!"  bare mass    : {ref.bareMeV} MeV   (ошибка {ref.bareErrorPct} относительно reference)"
    , s!"  final L1     : {ref.finalMeV} MeV   (ошибка {ref.finalErrorPct} относительно reference)"
    , s!"  reference    : {ref.referenceMeV} ± {ref.referenceUncMeV} MeV"
    , s!"  dataset      : {l1ReferenceDataset}"
    ]

def main : IO Unit := do
  IO.println "--- DOTheory: русский Lean-вход по bare-формулам и reference-данным ---"
  IO.println s!"Репозиторий      : {repoUrlRu}"
  IO.println s!"Набор данных     : {l1ReferenceDataset}"
  IO.println s!"Актуальность     : {freshnessNoteRu}"
  IO.println "Что показывает этот файл:"
  IO.println "  1) bare-формулу, формализованную в Lean"
  IO.println "  2) сырую массу, которую даёт bare-носитель"
  IO.println "  3) финальное значение текущего пакета L1"
  IO.println "  4) reference-массу и uncertainty"
  IO.println ""
  IO.println "Короткие примеры:"
  for p in highlightedParticlesRu do
    IO.println (particleReportStringRu p)
    IO.println ""
  IO.println "P.S. Ещё одна забавная вещь: скрипт как будто всё время намекает, что там должен быть ещё один тяжёлый узел."
  IO.println "Может, я просто вижу паттерны там, где их нет, но больше всего ему как будто нравится Ω_ccc^{++}."
  IO.println ""
  IO.println "--- Полная таблица из 24 частиц ---"
  for p in allParticlesRu do
    IO.println (particleReportStringRu p)
    IO.println ""
  IO.println "--- Конец русской таблицы DOTheory ---"
