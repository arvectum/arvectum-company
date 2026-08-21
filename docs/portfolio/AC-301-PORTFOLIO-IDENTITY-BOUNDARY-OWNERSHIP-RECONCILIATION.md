# AC-301 — Сверка идентичности, границ и владения продуктами и инициативами портфеля

Статус: `Proposed`
Версия: `0.9.0`
Дата: `2026-08-21`
Владелец документа: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-301 — Portfolio product/node identity and ownership reconciliation`
Максимум итераций перекрёстной проверки: `10`

## 1. Цель и предел решения

AC-301 приводит начальную карту портфеля к однозначному Company-level состоянию перед распределением ответственных организационных позиций, установлением инвестиционных границ и классификацией кандидатов в повторно используемые модули.

Документ устанавливает для каждого существенного узла:

- устойчивую Company-level идентичность и точное основное имя;
- допустимые исторические/контрактные aliases без создания второй идентичности;
- канонический репозиторий реализации и источник текущего продуктового состояния;
- текущий тип узла;
- границу `Company ↔ Product ↔ Arvectum OS`;
- организационное владение и sponsorship без создания нового Assignment;
- состояние `continue / clarify / contain / retire candidate`;
- обязательные последующие reconciliation actions.

AC-301 **не**:

- утверждает бюджет, цену, прибыльность, SLA или промышленную готовность;
- создаёт или меняет организационные позиции и назначения — это AC-302;
- объединяет и не удаляет репозитории;
- передаёт legal title, исключительные права или договорные права;
- признаёт продукт повторно используемым модулем — это AC-304;
- меняет Product Contract или lifecycle Arvectum OS — это применимый OS governance path и Company-side AC-305;
- превращает факт размещения репозитория в доказательство принадлежности исключительных прав.

В этом документе **организационное владение продуктом** означает Company-level ответственность за то, что продукт существует в портфеле ООО «Арвектум», за решение о его направлении/сохранении/изменении в пределах утверждённых полномочий и за целостность его границ. Это понятие не заменяет юридическую квалификацию прав на код, данные, товарные знаки, результаты работ или клиентские материалы.

## 2. Источники и правило authority

Проверка выполнена против актуального `main` следующих канонических источников:

- `arvectum/arvectum-company` — Company Constitution, roadmap, initial portfolio, approved M2 operating-model artifacts;
- `arvectum/tender-agent` — `STATUS.md` и продуктовые документы;
- `arvectum/discount-parser` — `README.md` и product docs;
- `arvectum/proxy-launcher` — `README.md`, release/productization docs;
- `arvectum/creative-test-agent` — `README.md` и product roadmap/docs;
- `arvectum/tender-app` — `README.md` и roadmap/docs;
- `arvectum/doors_parser` — `README.md` и delivery evidence;
- `arvectum/data-platform` — `README.md` и repository state;
- `arvectum/arvectum-os` — действующие Product Contracts и Accepted OS governance/architecture.

Юридически значимые и корпоративные факты остаются подчинены применимым юридическим/корпоративным источникам. Product repositories остаются каноническими для product-specific semantics, implementation, roadmap и release/operational evidence. Arvectum OS остаётся каноническим для OS Product Contracts, capability lifecycle и platform semantics.

## 3. Стабильная Company-level модель идентичности

### 3.1. Portfolio ID

`PORT-001` … `PORT-007` сохраняются как стабильные Company-level идентификаторы узлов портфеля.

Переименование продукта, репозитория или маркетингового названия **не должно** создавать новый `PORT-*`, пока семантический продукт/инициатива остаётся тем же. Новый `PORT-*` требуется, если создаётся действительно новый самостоятельный объект инвестирования и ответственности.

### 3.2. Repository identity

Репозиторий является каноническим locator реализации, но не самой продуктовой идентичностью. Репозиторий может быть переименован, перенесён или разделён без автоматического изменения Product Identity.

### 3.3. Aliases

Историческое имя, старый repository locator, Product Contract identity или маркетинговое имя могут быть записаны как alias/reference. Alias:

- не создаёт второго продукта;
- не переносит authority между Company, Product и OS;
- не становится доказательством legal/IP ownership;
- должен быть явно reconciled, если способен направить исполнение в неверный repository/contract boundary.

## 4. Утверждаемая после approval карта идентичности и границ

| ID | Основное Company-level имя | Текущий тип | Канонический repository | Канонический источник текущего состояния | Организационное владение | Company ↔ Product ↔ OS boundary | Disposition |
|---|---|---|---|---|---|---|---|
| `PORT-001` | `Arvectum Tender Agent` | самостоятельный продукт | `arvectum/tender-agent` | `STATUS.md` + product docs | ООО «Арвектум» как portfolio sponsor/product organizational owner; конкретная accountable Position определяется AC-302 | Company владеет portfolio/investment direction; продукт владеет procurement-domain semantics, workflows, UX и implementation; OS владеет только явно принятым platform boundary/Product Contract | `continue` |
| `PORT-002` | `Discount Parser` | productized client solution / продукт с клиентским delivery contour | `arvectum/discount-parser` | `README.md` + `docs/` | ООО «Арвектум» как portfolio sponsor/product organizational owner; AC-302 должен закрепить Position | Company владеет обязательствами/portfolio decision; продукт владеет source adapters, normalization, dedup, taxonomy, client UX/delivery; OS contract не поглощает parser semantics | `continue` |
| `PORT-003` | `Arvectum Proxy Launcher` | самостоятельный продукт | `arvectum/proxy-launcher` | `README.md` + `RELEASE_POLICY.md` + productization evidence | ООО «Арвектум» как portfolio sponsor/product organizational owner; AC-302 должен закрепить Position | Company владеет продуктовым направлением/риском/коммерческими решениями; продукт владеет proxy-routing/release semantics; отсутствие Product Contract означает отсутствие OS reliance по умолчанию | `continue` |
| `PORT-004` | `Creative Test Agent` | самостоятельный продукт / controlled-pilot solution | `arvectum/creative-test-agent` | `README.md` + canonical product roadmap/docs | ООО «Арвектум» как portfolio sponsor/product organizational owner; AC-302 должен закрепить Position | Company владеет portfolio role и коммерческим направлением; продукт владеет creative-testing domain semantics, local-first workflow и client pilot implementation; OS relation не выводится без Product Contract | `continue` |
| `PORT-005` | `Tender Small-Volume Calculator` | product experiment / локальный procurement MVP | `arvectum/tender-app` | `README.md` + `docs/ROADMAP.md` | ООО «Арвектум» как sponsor существующего experiment asset; отдельное product-owner Assignment не создаётся AC-301 | Company хранит инвестиционную/семейную границу; experiment владеет своим small-volume workflow/implementation; он не является модулем Tender Agent и не является OS capability без отдельного решения | `contain` |
| `PORT-006` | `Doors Parser` | client-delivery solution / завершённый product experiment | `arvectum/doors_parser` | `README.md` + delivery/QA outputs | ООО «Арвектум» как sponsor/holder of the portfolio node в организационном смысле; конкретные правовые/IP границы определяются отдельными источниками | Company хранит клиентскую/портфельную историю и решение о повторном использовании; репозиторий владеет door-domain extraction implementation; никакой generic parser/module/OS capability из него автоматически не возникает | `contain` |
| `PORT-007` | `Data Platform` | внутренняя инициатива на стадии определения | `arvectum/data-platform` | `README.md` + repository history | ООО «Арвектум» как initiative sponsor; отдельная product/Position authority ещё не выводится | Company должна сначала определить business hypothesis, consumers и boundary; Product/OS ownership нельзя назначить из названия `platform`; domain-neutral OS capability не возникает автоматически | `clarify` |

### Значение disposition

- `continue` — идентичность и текущая граница достаточны для продолжения bounded work; дальнейшие инвестиции всё равно подчиняются AC-303/AC-306.
- `clarify` — следующий существенный инвестиционный шаг должен сначала устранить неопределённость identity/business boundary.
- `contain` — существующий asset сохраняется, но его scope не расширяется и он не получает автоматически статус самостоятельного strategic growth product до отдельного решения.
- `retire candidate` — узел является кандидатом на прекращение/архивацию, но фактическое прекращение требует отдельного authority/investment decision.

В AC-301 ни один узел не переводится в `retire candidate`: текущих доказательств недостаточно, чтобы делать материальное stop decision без AC-303/AC-306.

## 5. Узел PORT-001 — Arvectum Tender Agent

### 5.1. Идентичность

Каноническое Company-level имя: `Arvectum Tender Agent`.

Канонический repository locator: `arvectum/tender-agent`.

Исторические/контрактные references:

- прежний repository/product context `ai-corporation` / `arutyunoveth/ai-corporation`;
- OS P6.02 wording `Arvectum procurement/tender AI operator`;
- OS Product Identity `product/arvectum-tender-operator@<organization>` для конкретной bounded Product Contract lineage.

Эти references относятся к той же продуктовой линии/конкретному OS interaction contour, но **не заменяют** Company-level Product Identity `PORT-001` и не должны использоваться как текущий repository locator.

### 5.2. Граница

`arvectum/tender-agent` остаётся владельцем product-specific procurement semantics: tender intake, extraction/analysis, product workflows, procurement risk/decision-support logic, UI/export и product roadmap.

Company определяет portfolio role, investment priority, commercial/risk boundaries и accountable organizational ownership.

Arvectum OS получает authority только над явно объявленной platform-owned частью. P6.02 `Provisional 0.1.0` остаётся OS artifact и не превращает Tender Agent в OS capability.

### 5.3. Reconciliation defect

P6.02 на текущем `main` Arvectum OS всё ещё указывает `Product repository: arutyunoveth/ai-corporation`.

Company-side решение AC-301: считать это **stale OS contract locator**, а не второй текущий canonical repository. Исправление самого Product Contract должно происходить через OS governance / AC-305, с сохранением contract lineage и без silent rewrite.

Disposition: `continue`.

## 6. Узел PORT-002 — Discount Parser

Каноническое имя и repository уже однозначны: `Discount Parser`, `arvectum/discount-parser`.

Текущая product identity включает клиентский installer/web UI, source-specific adapters, normalisation/dedup/classification, Telegram control/publication contour и клиентскую поставку. Эти product-domain обязанности не передаются в OS из-за наличия P6.06 Product Contract.

`Discount Parser` **не** переименовывается в `Arvectum Parser`, `Universal Parser` или `Data Platform`. Возможное извлечение reusable parsing engine является отдельным будущим решением AC-304 и/или соответствующего product repository.

Disposition: `continue`.

## 7. Узел PORT-003 — Arvectum Proxy Launcher

Каноническое имя: `Arvectum Proxy Launcher`.

Канонический repository: `arvectum/proxy-launcher`.

Продукт имеет собственный release/productization lifecycle и не является ни инфраструктурной службой Arvectum OS, ни Company authority component только потому, что может использоваться другими продуктами.

Если Company позднее использует его как shared internal dependency, это создаст dependency relation, а не автоматически новый Product Identity или OS capability.

Disposition: `continue`.

## 8. Узел PORT-004 — Creative Test Agent

Каноническое имя: `Creative Test Agent`.

Канонический repository: `arvectum/creative-test-agent`.

Историческое/обобщающее название `Marketing Agent` **не считается текущей product identity** и сохраняется только как historical concept/possible future product-family direction.

Текущий продукт — локальный/closed-loop creative pre-testing product with controlled client pilot contour. Расширение в общий Marketing Agent требует отдельного product-scope decision и не происходит через Company naming convention.

Disposition: `continue`.

## 9. Узел PORT-005 — Tender Small-Volume Calculator

Каноническое Company-level имя уточняется до `Tender Small-Volume Calculator`, поскольку repository README сам идентифицирует продукт как `tender-small-volume-calculator`, а имя `Tender App` является прежде всего repository/short-name locator.

Repository: `arvectum/tender-app`.

Этот узел **не объединяется** с `PORT-001`. На текущем evidence он является отдельным локальным MVP/product experiment, сфокусированным на закупках малого объёма, импорте, расчёте маржи/рисков, decisioning и dashboard/export.

Одновременно он имеет достаточный domain overlap с Tender Agent, чтобы дальнейшее независимое расширение без family/boundary decision создавать риск дублирования.

Поэтому disposition: `contain`.

До AC-303/AC-304/AC-306 допустимы сохранение, исправление критических дефектов и extraction of evidence; не следует молча развивать его как второй равноправный procurement strategic product или переносить его код в Tender Agent без отдельного решения.

## 10. Узел PORT-006 — Doors Parser

Каноническое имя: `Doors Parser`.

Канонический repository: `arvectum/doors_parser`.

Текущий evidence отражает зрелый клиентский delivery snapshot, а не активную универсальную parser platform. Он остаётся отдельным product/client-solution identity для истории, обязательств, provenance и возможного повторного использования.

Общие идеи visual/source-specific extraction могут быть evidence для будущего reusable module, но не создают generic parser identity в AC-301.

Disposition: `contain`.

## 11. Узел PORT-007 — Data Platform

Каноническое временное имя: `Data Platform`.

Канонический repository: `arvectum/data-platform`.

Текущее содержимое repository не подтверждает достаточную business/product boundary: README содержит только базовое название, отсутствуют утверждённые consumers, economic hypothesis, product roadmap, Product Contract и явная ответственность за reusable capability.

Само слово `Platform` не является архитектурным решением.

Disposition: `clarify`.

Перед существенной разработкой необходимо определить как минимум:

1. business problem и expected value;
2. первых реальных consumers;
3. границу с Discount Parser/Doors Parser/Tender products;
4. почему это Company/product capability, отдельный product или candidate for OS rather than duplicate;
5. cost/risk/sovereignty boundary;
6. canonical product owner Position после AC-302;
7. stop/continue criteria по AC-303.

## 12. Семейства и потенциальные дубли

### 12.1. Procurement family

`PORT-001` и `PORT-005` образуют **portfolio family hypothesis**, но не одну product identity.

До отдельного решения:

- `PORT-001` — основной продолжаемый procurement product;
- `PORT-005` — contained small-volume experiment;
- cross-repo code/data/schema merge запрещён как неявное архитектурное решение;
- reusable pieces должны проходить AC-304/product-specific review.

### 12.2. Parsing/data family

`PORT-002`, `PORT-006`, `PORT-007` имеют потенциальную связь по extraction/data processing, но остаются тремя разными identities:

- Discount Parser — текущий client/productized solution;
- Doors Parser — contained client-delivery solution;
- Data Platform — clarify-stage internal initiative.

Никакого `Universal Parser` или shared platform identity AC-301 не создаёт.

### 12.3. Marketing family

`Creative Test Agent` остаётся отдельным product identity. `Marketing Agent` не создаётся как отдельный узел без repository/business boundary/economic hypothesis.

## 13. Организационное владение и AC-302

На уровне AC-301 все семь узлов принадлежат портфелю ООО «Арвектум» в **организационном** смысле: Company является sponsor и authority source для Company-level portfolio decisions в пределах применимых юридических/корпоративных полномочий.

Это не означает, что Owner human Principal лично должен исполнять product-management work.

AC-301 намеренно не создаёт Assignments. AC-302 должен взять эту карту и для каждого `continue`, `contain` и при необходимости `clarify` узла закрепить реально существующую accountable Position из утверждённой M2-модели либо обосновать необходимость изменения Position registry отдельным governance decision.

Repository account ownership, GitHub admin permission и техническая возможность push **не равны** Organizational Authority или legal ownership.

## 14. Arvectum OS boundary

Arvectum OS не является `PORT-*` product node в этой карте. Это отдельная domain-neutral platform foundation.

Текущие явные Product Contract relations:

- Tender Agent ↔ P6.02 `Provisional 0.1.0`;
- Discount Parser ↔ P6.06 `Provisional 0.1.0`.

Для остальных узлов отсутствие Product Contract означает отсутствие декларируемой governed OS reliance в AC-301.

Company sponsorship of Arvectum OS не позволяет Company artifact переписывать Product Contract; Product Contract не позволяет OS владеть product-domain semantics; техническая интеграция не создаёт Company authority.

## 15. Reconciliation register

| ID | Дефект/неопределённость | AC-301 resolution | Следующий owner |
|---|---|---|---|
| `REC-301-01` | P6.02 указывает predecessor repository `arutyunoveth/ai-corporation` | текущий canonical product repo = `arvectum/tender-agent`; старый locator признан stale reference | AC-305 + OS governance |
| `REC-301-02` | Tender Agent vs Tender App overlap | identities остаются отдельными; Tender App = contained experiment | AC-304/AC-306 |
| `REC-301-03` | `Marketing Agent` vs Creative Test Agent | текущий product identity = Creative Test Agent; Marketing Agent не admitted | future product decision if needed |
| `REC-301-04` | Discount/Doors reuse может быть ошибочно названо universal parser | generic parser identity не создана | AC-304 |
| `REC-301-05` | Doors Parser не имеет текущего strategic lifecycle | сохраняется как contained client-delivery/product experiment asset | AC-303/AC-306 |
| `REC-301-06` | Data Platform boundary не определена | `clarify`; дальнейшая material investment требует business/consumer boundary | AC-303/AC-304/AC-306 |
| `REC-301-07` | GitHub repository ownership может быть принят за legal/IP ownership | явное non-equivalence правило | legal/IP evidence path where needed |
| `REC-301-08` | Product accountability пока не привязана к Position | не исправляется созданием fake Assignment в AC-301 | AC-302 |

## 16. Acceptance criteria

AC-301 может быть утверждён только если перекрёстная проверка подтверждает:

1. все семь текущих material nodes имеют одну Company-level identity;
2. repository locator отделён от Product Identity;
3. historical aliases не создают competing canonical products;
4. Company/Product/OS responsibilities разделены;
5. legal/IP ownership не выведено из GitHub/repository placement;
6. Tender Agent/Tender App не объединены молча;
7. parser/data nodes не превращены молча в universal platform;
8. Creative Test Agent не переименован молча в Marketing Agent;
9. Data Platform не получает platform status из названия;
10. для каждого узла задан disposition;
11. disposition не подменяет AC-303/AC-306 инвестиционное решение;
12. AC-302 остаётся следующим шагом и не получает заранее выдуманные Assignments;
13. P6.02 stale locator выявлен без изменения OS artifact из Company repository;
14. никакой новый Product Contract, OS capability, budget, SLA или customer commitment не создан.

## 17. Результат после утверждения

После Owner approval эта редакция должна стать канонической Company-level базой AC-301 и синхронизировать `docs/portfolio/PORTFOLIO.md`.

Следующее действие дорожной карты:

`AC-302 — Закрепление ответственной организационной позиции за каждым активным продуктом/инициативой`.

До approval данный документ остаётся reviewed proposal и не заменяет действующий `PORTFOLIO.md`.