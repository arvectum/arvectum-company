# AC-304 — Разделение: самостоятельный продукт / эталонная реализация / кандидат в модуль / кандидат в возможность Arvectum OS

Статус: `Proposed`
Версия: `0.9.0`
Дата: `2026-08-21`
Владелец документа: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-304 — Standalone product / reference implementation / module candidate / Arvectum OS capability candidate classification`
Максимум итераций перекрёстной проверки: `10`

## 1. Цель и точная граница AC-304

AC-304 классифицирует текущую Company-level роль каждого portfolio node `PORT-001…PORT-007` и разделяет четыре понятия, которые нельзя использовать как синонимы:

1. **самостоятельный продукт**;
2. **эталонная / референсная реализация**;
3. **кандидат в повторно используемый Company/product-family module**;
4. **Company-side кандидат на рассмотрение как domain-neutral Platform Capability Arvectum OS**.

Задача отвечает на вопрос:

> Какую роль каждый существующий portfolio node играет сейчас: самостоятельную продуктовую, референсную, гипотезу общего Company-модуля или источник обоснованной OS-capability promotion hypothesis — без автоматического объединения репозиториев, без speculative platform gravity и без переноса domain semantics в Arvectum OS?

AC-304 **не**:

- меняет `PORT-*` identities или AC-301 dispositions;
- меняет AC-302 accountability mapping;
- меняет AC-303 investment envelope;
- переносит код, схемы, данные или историю между репозиториями;
- создаёт shared library/service/runtime;
- создаёт Product Contract или меняет существующий Product Contract Arvectum OS;
- переводит OS capability в lifecycle `Candidate`, `Incubating` или `Active`;
- утверждает budget, capital priority или relative portfolio ranking;
- объединяет продукты;
- создаёт legal/IP/data rights;
- считает техническое сходство, общий стек, repository reuse или факт существования кода достаточным доказательством повторного использования.

## 2. Каноническая основа и просмотренный evidence

Company-level основа:

- `docs/constitution/COMPANY-CONSTITUTION.md` — Ratified `1.0.0`, reviewed blob `181705c60a6135752cffeb38ccf475f815aa6185`;
- `docs/governance/COMPANY-OS-AUTHORITY-BOUNDARY.md` — Approved `1.0.0`, reviewed blob `90c7b6b6a53af827a0ae7e593a553e05fa848391`;
- `docs/portfolio/AC-301-PORTFOLIO-IDENTITY-BOUNDARY-OWNERSHIP-RECONCILIATION-v1.0.0.md` — Approved `1.0.0`, reviewed blob `96933e32263cbf1140ce257423eb5e9c16a49f07`;
- `docs/portfolio/AC-302-PORTFOLIO-ACCOUNTABLE-POSITION-MAPPING-v1.0.0.md` — Approved `1.0.0`, reviewed blob `1f62dcfea885e564c8cd43926c72a04d00821328`;
- `docs/portfolio/AC-303-PORTFOLIO-INVESTMENT-COST-RISK-BOUNDARIES-v1.0.0.md` — Approved `1.0.0`, reviewed blob `3f7af8bd9e5b9c5f64045a54a723f8db4eab63d0`;
- `docs/portfolio/PORTFOLIO.md` — Active `0.4.0`, reviewed blob `c8906a139833dfe76915f976260e2949a718f118`;
- `docs/roadmap/ROADMAP.md` — Active `0.25.0`, reviewed blob `e6d32d76c710b9956f7902ac838c429f32829358`.

Текущий product evidence snapshot:

| Portfolio ID | Product source | Reviewed blob |
|---|---|---|
| `PORT-001` | `arvectum/tender-agent/STATUS.md` | `8f9c3cfdb8e893d46d0898e252ecb2f86e5c5f2b` |
| `PORT-001 / PORT-005` | `arvectum/tender-agent/docs/product/tender_app_reuse_audit.md` | `9b43d08a960a89482e692b73bc54a49d2cb1dbdb` |
| `PORT-002` | `arvectum/discount-parser/README.md` | `7580d8112918c0be3381ff0073b7a481fa388434` |
| `PORT-003` | `arvectum/proxy-launcher/README.md` | `5113d6d768507be9f91a35436c8cc4eea00e7c99` |
| `PORT-004` | `arvectum/creative-test-agent/README.md` | `faf29045cbe57f46579743ca3d8b87995dc0e808` |
| `PORT-005` | `arvectum/tender-app/README.md` | `5065e0e1673da12b60128f7972efa6286938e034` |
| `PORT-006` | `arvectum/doors_parser/README.md` | `69c6d037f5812d9a1ae225c2b4ab46f6d8713f53` |
| `PORT-007` | `arvectum/data-platform/README.md` | `6d6a0afe1f4437c383626bad42355077d76d986e` |

Arvectum OS boundary evidence:

- `arvectum/arvectum-os/docs/constitution/CONSTITUTION.md` — Ratified `1.2.0`, reviewed blob `d54680919a0119ad4543df516a23dada23a48582`;
- `arvectum/arvectum-os/docs/rfc/RFC-0001-arvectum-os-architecture.md` — Accepted `1.0.0`, reviewed blob `1a8379e6626f2d8d5cc5517ad4f00ad32014ee73`;
- `arvectum/arvectum-os/docs/contracts/P6-02-FIRST-REAL-PRODUCT-CONTRACT.md` — Provisional `0.1.0`, reviewed blob `bdf098776399a003f2df542f3ab3cd48ef83b003`;
- `arvectum/arvectum-os/docs/contracts/P6-06-SECOND-REAL-PRODUCT-CONTRACT.md` — Provisional `0.1.0`, reviewed blob `23bbe792b81ddc5da736333d8a92580a718f920e`;
- `arvectum/arvectum-os/docs/contracts/P8-06-CREATIVE-TEST-AGENT-PROVISIONAL-PRODUCT-CONTRACT.md` — Provisional `0.1.0`, reviewed blob `0f8b8404b8b201d3aa29e88f146a7bf658c01d9b`.

Product repositories остаются canonical для product implementation/status. Arvectum OS repository остаётся canonical для OS contracts/capability lifecycle. Этот snapshot фиксирует только evidence, использованный для Company-level classification.

## 3. Семантика четырёх ролей

### 3.1 Самостоятельный продукт

`Standalone product` — portfolio node с самостоятельной продуктовой идентичностью и собственным customer/use outcome, product lifecycle, product-owned domain semantics и отдельной продуктовой ответственностью.

Признаки могут включать:

- отдельный customer/use problem;
- самостоятельный workflow/UX/package;
- собственный roadmap/release/support contour;
- способность продолжать product-specific развитие без превращения в shared implementation другого продукта.

Самостоятельный продукт **может одновременно быть референсной реализацией**. Это не противоречие: первая роль описывает product identity, вторая — reuse/evidence role.

### 3.2 Эталонная / референсная реализация

`Reference implementation` — точная существующая реализация или bounded product experiment, которую Компания намеренно сохраняет как evidence/reference для проверенного паттерна, границы, workflow или будущего reusable design.

Reference status не означает:

- что весь код является «золотым шаблоном»;
- что реализация становится shared library;
- что она получает indefinite growth funding;
- что её domain semantics становятся Company- или OS-wide standard;
- что код/данные можно копировать без IP/license/data review.

В AC-304 различаются два useful subtype:

- `RI-OS-CONSUMER` — реальная product-side consumer implementation, которой Arvectum OS уже пользуется как evidence для Product Contract / cross-repository validation;
- `RI-PRODUCT-FAMILY` — реализация, из которой подтверждённо извлекаются или могут извлекаться reusable product-family patterns без превращения всей реализации в shared module.

### 3.3 Кандидат в Company/product-family module

`Module candidate` — Company-level гипотеза повторно используемого механизма **выше отдельных продуктов, но ниже Arvectum OS**, когда общий смысл остаётся product-family/domain/integration-oriented и не должен становиться domain-neutral OS behavior.

Candidate status требует как минимум:

- сформулированный общий outcome/problem;
- конкретные source implementations или организационную need;
- минимум двух правдоподобных consumers либо одного реального consumer и credible near-term второго;
- понятную общую contract boundary;
- доказательство, что общий модуль потенциально дешевле/безопаснее duplication + later migration;
- отсутствие необходимости переносить customer/domain authority в shared layer;
- bounded promotion/containment/retirement criteria.

`Module candidate` **не равен реализованному module** и не разрешает material build автоматически.

### 3.4 Company-side кандидат в возможность Arvectum OS

`OS capability candidate` в AC-304 означает только **Company-side promotion hypothesis**: есть evidence, что reusable mechanism должен рассматриваться OS governance как возможная domain-neutral organizational ability.

Это не lifecycle status Arvectum OS `Candidate`.

RFC-0001 определяет Platform Capability как reusable, domain-neutral organizational ability и требует для OS `Candidate` отдельного organizational outcome, owner, rationale, domain-neutral boundary, expected consumers/strategic need, reuse hypothesis, review date и admission criteria. Только Arvectum OS governance может создать lifecycle `Candidate` и продвигать его дальше.

Поэтому Company artifact может сказать `OS promotion hypothesis: yes/no`, но не может присвоить OS lifecycle status.

## 4. Утверждаемая при approval классификационная матрица

`YES` означает Company-level role/classification в пределах AC-304. `NO` означает отсутствие достаточного текущего evidence для этой роли; это не вечный запрет.

| ID | Standalone product | Reference implementation | Company/product-family module candidate | Company-side OS capability candidate | Текущая основная роль AC-304 |
|---|---|---|---|---|---|
| `PORT-001` | `YES` | `YES — RI-OS-CONSUMER` | `NO` | `NO` | самостоятельный продукт + референсный consumer Arvectum OS |
| `PORT-002` | `YES` | `YES — RI-OS-CONSUMER + RI-PRODUCT-FAMILY` | `NO` | `NO` | самостоятельный продукт + референсная реализация для OS и parser/data-extraction family evidence |
| `PORT-003` | `YES` | `NO` | `NO` | `NO` | самостоятельный продукт |
| `PORT-004` | `YES` | `YES — RI-OS-CONSUMER` | `NO` | `NO` | самостоятельный продукт + референсный внешний consumer Arvectum OS |
| `PORT-005` | `NO` | `YES — RI-PRODUCT-FAMILY` | `NO` | `NO` | contained procurement reference implementation / evidence source |
| `PORT-006` | `NO` | `YES — RI-PRODUCT-FAMILY` | `NO` | `NO` | contained completed-delivery reference implementation / evidence source |
| `PORT-007` | `NO` | `NO` | `YES — clarification-only candidate` | `NO` | кандидат в Company/product-family data acquisition/extraction module; не platform status |

В текущем портфеле **ни один `PORT-*` node не классифицируется как Company-side кандидат в новую Platform Capability Arvectum OS**.

Это осознанный результат, а не пропуск: OS-level reusable needs, уже доказанные через продукты, представлены существующими OS capabilities/contracts внутри `arvectum/arvectum-os`, а не переводом целого product repository в Platform Capability.

## 5. Node-level rationale

### 5.1 `PORT-001 — Arvectum Tender Agent`

**Standalone: YES.**

AC-301 уже фиксирует самостоятельную product identity. Текущий product source показывает самостоятельный controlled tender workflow: intake, read-only document acquisition, extraction, RAG-assisted analysis, local-model integration и human-reviewed export.

**Reference: YES — `RI-OS-CONSUMER`.**

Arvectum OS P6.02 выбрал bounded tender/operator workflow как **первый реальный Product Contract validation target**, использующий CAP-001 и CAP-004. Это делает продукт референсным consumer implementation для проверки Company/Product/OS boundary, но не реализацией самих OS capabilities.

P6.02 всё ещё содержит старый repository locator `arutyunoveth/ai-corporation`. AC-301 уже запретил silent Company-side rewrite; exact locator/Product Contract reconciliation остаётся AC-305.

**Module candidate: NO.**

Product repository содержит несколько potentially reusable procurement mechanisms, однако текущий evidence не требует отдельного shared Company module. `tender_app_reuse_audit.md` показывает selective reuse архитектурных идей из старого Tender Small-Volume Calculator в Tender Agent без монолитного переноса кода. Это скорее доказательство reference-based reuse, чем необходимость общего runtime module.

**OS capability candidate: NO.**

Tender/domain semantics, risk rules, RFQ/TKP logic и product workflow остаются product-owned. Domain-neutral pressure уже выражено через существующие CAP-001/CAP-004, а не через promotion всего Tender Agent.

### 5.2 `PORT-002 — Discount Parser`

**Standalone: YES.**

Продукт имеет самостоятельный клиентский contour, установку/дистрибуцию, source adapters, normalization/deduplication, lifecycle, scheduler, Telegram control/publication и product-owned UI.

**Reference: YES — два subtype.**

`RI-OS-CONSUMER`: P6.06 прямо использует Discount Parser как **второй materially distinct real Product Contract target**, проверяющий scheduled/machine-initiated execution, external mutation, idempotency, uncertain outcome и reconstruction через CAP-004.

`RI-PRODUCT-FAMILY`: product source содержит Source SDK, пять adapters, normalization, provenance/run state, deduplication и failure isolation. Эти механизмы дают конкретное implementation evidence для будущей parser/data-acquisition module hypothesis вместе с PORT-006.

**Module candidate: NO на уровне целого node.**

Discount Parser не превращается в shared parser module. Offer taxonomy, publication workflow, Telegram integration, scheduler policy, classification и customer UX остаются его product semantics. Потенциально reusable subset относится к PORT-007 candidate boundary, а не меняет identity PORT-002.

**OS capability candidate: NO.**

P6.06 прямо исключает platform promotion source adapters, scheduler, Offer model, classification, deduplication, rule memory, Telegram integration и UI. Existing CAP-004 остаётся OS-owned shared capability; продукт является consumer/reference, а не capability candidate.

### 5.3 `PORT-003 — Arvectum Proxy Launcher`

**Standalone: YES.**

Текущий product source фиксирует самостоятельный Windows productization track с собственным release, installer/portable formats, state/recovery, DPAPI credential handling, update/repair/uninstall и supportability boundary.

**Reference: NO сейчас.**

Product implementation содержит потенциально полезные engineering patterns — release packaging, recovery, rollback, signing/productization discipline — но текущий Company/OS evidence не фиксирует независимого consumer или approved reuse boundary. Техническая полезность сама по себе не создаёт reference role.

**Module candidate: NO.**

Сходство release/packaging потребностей с другими desktop products может позже создать tooling/standard hypothesis, но AC-304 не создаёт новый portfolio node или module без consumer/economic evidence.

**OS capability candidate: NO.**

Proxy routing, Windows launcher behavior и desktop productization не являются доказанной domain-neutral organizational ability Arvectum OS. Если продукт позже начнёт использовать OS, это требует Product Contract/dependency path, а не переноса proxy semantics в платформу.

### 5.4 `PORT-004 — Creative Test Agent`

**Standalone: YES.**

Продукт имеет отдельный marketing-creative problem, local-first closed-loop architecture, creative/audience/rubric domain schemas, reports/exports, pilot package, projects/brandbooks/knowledge, local model/vision integrations и собственный product UX.

**Reference: YES — `RI-OS-CONSUMER`.**

Arvectum OS P8.06 создаёт отдельный Provisional Product Contract для optional external Creative Test Agent audit/reconstruction extension через CAP-004. Контракт специально доказывает cross-repository onboarding и сохраняет независимую работоспособность CTA без OS extension.

**Module candidate: NO.**

Prompt/model/evaluation/export/local-vision mechanisms могут выглядеть повторно используемыми, но текущий evidence не показывает отдельного shared Company module с двумя consumers и bounded contract. Они остаются product-owned до доказательства обратного.

**OS capability candidate: NO.**

P8.06 прямо сохраняет creative schemas, audience simulation, scoring, brand safety, rubric configuration, creative workflows, reports, recommendations, UX, model/prompt choices за продуктом. CAP-004 остаётся domain-neutral OS capability.

### 5.5 `PORT-005 — Tender Small-Volume Calculator`

**Standalone: NO как текущая Company portfolio role.**

Репозиторий остаётся самостоятельно запускаемым MVP, но AC-301/AC-303 уже установили `contain`: это не growth product mandate. Техническая самостоятельность runtime не равна Company classification `standalone product` для дальнейшего портфельного развития.

**Reference: YES — `RI-PRODUCT-FAMILY`.**

`arvectum/tender-agent/docs/product/tender_app_reuse_audit.md` является прямым reuse evidence: старый tender-app использован как reference для read-only procurement discovery, normalized result, attachment manifest, skip reasons и manual fallback. При этом code не переносился монолитно, а browser/auth/install/scheduler/price-search contours намеренно не переносились.

Это именно reference role: сохранять проверяемое implementation/history evidence и извлекать только пригодные patterns после product/security/legal review.

**Module candidate: NO.**

Selective reuse уже происходит через product-to-product reference и не доказывает необходимость общего procurement runtime module. Отдельный module candidate может появиться позже только при real multi-consumer need.

**OS capability candidate: NO.**

Закупки малого объёма, price search, margin/risk/evaluation и domain connectors являются procurement semantics. Они не должны переходить в domain-neutral OS по импликации.

### 5.6 `PORT-006 — Doors Parser`

**Standalone: NO как текущая Company portfolio role.**

Это завершённый contained client-delivery/product experiment. Repository остаётся valuable implementation/evidence asset, но AC-301/AC-303 не дают ему growth product mandate.

**Reference: YES — `RI-PRODUCT-FAMILY`.**

Implementation содержит конкретные reusable patterns для parser/data-extraction family: multi-site configuration, line/model extraction, deduplication, image-quality filtering/replacement, structured QA report, per-source behavior и explicit `needs_review` treatment.

AC-304 предлагает сохранять PORT-006 как reference implementation для PORT-007 module hypothesis. Это **не** означает автоматическое копирование customer data, domain fields, site-specific selectors или кода; reusable design/code требует отдельного IP/license/data и engineering review.

**Module candidate: NO на уровне целого node.**

Doors domain, manufacturer/line/model/material semantics и current client output не являются shared module contract. Reusable subset должен быть выделен отдельно только через PORT-007 candidate boundary.

**OS capability candidate: NO.**

Web/catalog extraction и door-domain QA не являются доказанной domain-neutral organizational ability Arvectum OS. Если extracted artifacts позже должны получать OS governance/provenance, продукт/module должен потреблять соответствующие OS capabilities по явному contract boundary.

### 5.7 `PORT-007 — Data Platform`

**Standalone: NO.**

Current canonical repository содержит только минимальный README `Data Platform`; нет product contract, customer outcome, product lifecycle или implementation evidence, достаточного для самостоятельного продукта.

**Reference: NO.**

Нет реализации, которую можно считать reference implementation.

**Module candidate: YES — `clarification-only`.**

AC-304 ограничивает смысл этого кандидата до **Company/product-family data acquisition & extraction module hypothesis**. Candidate существует ради проверки, можно ли вынести общие patterns из PORT-002 и PORT-006 в reusable layer с более низкой стоимостью поддержки и меньшим duplication.

Предлагаемая bounded hypothesis включает только потенциально общие механизмы:

- source/adapter contract;
- controlled fetch/intake envelope;
- extraction result envelope;
- normalization hooks;
- provenance/source reference;
- run/error/failure isolation;
- dedup/quality/review hooks;
- test fixtures/adapter conformance там, где это реально общее.

Она **не включает по умолчанию**:

- Offer/discount taxonomy и Telegram publication PORT-002;
- door/manufacturer/line/material schemas PORT-006;
- tender/procurement semantics PORT-001/005;
- generic enterprise data lake/warehouse;
- shared customer data store;
- vector database/search platform;
- OS Canonical Records, authority, Event, Execution Context, Memory/Knowledge или Document governance semantics;
- production infrastructure merely because node называется `Data Platform`.

AC-303 `clarify before investment` остаётся в силе. `Module candidate: YES` не разрешает material implementation, recurring infrastructure или production data ingestion.

**OS capability candidate: NO.**

Текущая module hypothesis — technical/product-family integration layer. Она не имеет доказанной domain-neutral organizational semantics, отличной от уже существующих OS capabilities. Возможная будущая OS promotion hypothesis возникает только после реального module evidence и отдельного OS admission analysis.

## 6. PORT-007 — критерии выхода из candidate state

PORT-007 не должен «становиться платформой» по инерции. До material build должны быть получены evidence и explicit decision по следующим вопросам:

1. **Consumers:** минимум два конкретных текущих/near-term consumer contours; не просто два старых репозитория.
2. **Common contract:** минимальный общий adapter/extraction/result/provenance contract без Offer/door/tender domain leakage.
3. **Economic case:** почему extraction в shared module дешевле/безопаснее, чем локальная реализация плюс selective reuse.
4. **Migration cost:** какую реально существующую дубликацию нужно убрать и сколько адаптации потребуется consumers.
5. **Rights/data:** можно ли законно повторно использовать код/patterns/fixtures; customer/source data не становятся shared asset автоматически.
6. **Sovereignty:** dependencies должны быть replaceable и не владеть единственной копией критического state/knowledge.
7. **Continuity:** модуль не должен превращаться в новый single point of failure без recovery/rollback path.
8. **Ownership:** accountable product-family/module owner и support responsibility должны быть явными до shared operational reliance.
9. **Exit:** если reuse value не подтверждается, PORT-007 должен быть contained/re-scoped/retired candidate без миграции продуктов ради сохранения идеи.

До выполнения этих условий допускаются discovery, contract sketch, evidence inventory и bounded proof, если они укладываются в действующие authority/investment limits. Production/shared operational reliance требует отдельного решения.

## 7. Почему в AC-304 нет новых OS capability candidates

Это важный boundary result.

Arvectum OS Constitution и RFC-0001 требуют validated reuse или стратегической/constitutional need и domain-neutral boundary. Портфель уже даёт реальные OS reuse evidence другим способом:

- Tender Agent — реальный Product Contract consumer CAP-001/CAP-004;
- Discount Parser — materially distinct consumer CAP-004 с external-effect/reconciliation pressure;
- Creative Test Agent — external consumer onboarding CAP-004.

То есть реальное межпродуктовое reuse evidence укрепляет **существующие OS capability contracts**. Из этого не следует, что Tender Agent, Discount Parser, Creative Test Agent, Parser Engine, Proxy Launcher или Data Platform должны сами стать Platform Capabilities.

Если позже появится новый domain-neutral need, Company может подготовить promotion hypothesis. OS-side `Candidate` создаётся только через Arvectum OS governance с требованиями RFC-0001.

## 8. Promotion/reuse evidence rules после AC-304

### 8.1 Reference implementation → module candidate

Reference implementation может стать источником module candidate только если есть:

- повторяемая problem/contract boundary;
- реальный второй consumer либо credible near-term второй;
- measurable reduction duplication/cost/risk;
- отсутствие cross-customer/domain authority leakage;
- explicit owner/support/exit path.

### 8.2 Module candidate → implemented shared module

Нужен отдельный Company/product decision с bounded scope, implementation owner, consumers, compatibility, migration, security/data/IP boundary, operational responsibility и stop/return-to-product criteria.

### 8.3 Product/module → OS promotion hypothesis

Нужно доказать, что общий outcome:

- domain-neutral;
- organizational, а не просто технически удобный;
- нужен нескольким products/capabilities или стратегически необходим;
- лучше принадлежит OS, чем Company/product-family layer;
- не дублирует уже существующий OS capability;
- имеет explicit governance/security/portability value.

После этого Company только передаёт evidence в OS governance; lifecycle решение остаётся за Arvectum OS.

## 9. Границы с AC-305 и AC-306

AC-304 специально **не** выполняет downstream work.

### AC-305 остаётся владельцем dependency/Product Contract reconciliation

В AC-305 должны быть проверены:

- точные current dependencies между PORT nodes;
- declared/hidden cross-product contracts;
- Product Contract/dependency status с Arvectum OS;
- stale P6.02 repository locator;
- отсутствующие или лишние OS dependencies;
- whether PORT-007 module hypothesis вообще требует OS dependency и какую именно.

AC-304 reference labels не являются dependency contracts.

### AC-306 остаётся владельцем relative priority

AC-304 не говорит, что reference implementation, module candidate или standalone product «важнее» другого node.

Capital/economics/Owner-attention priority остаётся AC-306. Reference status не является funding argument; module-candidate status не создаёт investment mandate; standalone status не гарантирует continuation beyond AC-303 envelope.

## 10. Authority, IP, data и external effect boundary

При approval AC-304 будет Company-level portfolio classification decision в пределах внутренней governance модели.

Он не:

- создаёт право копировать third-party/customer code/data/content;
- меняет исключительные права;
- создаёт customer permission или cross-customer reuse right;
- расширяет Position authority или access;
- разрешает новый spend;
- создаёт external commitment;
- меняет Product Contract;
- создаёт OS lifecycle status.

AI recommendation, repository similarity, common Python/FastAPI stack, наличие одинаковых библиотек или успешный CI не являются достаточным reuse/promotion evidence.

## 11. Decision effect при явном Owner approval

После явного approval exact reviewed proposal:

1. классификационная матрица раздела 4 становится binding Company-level AC-304 baseline;
2. `PORT-001/002/003/004` сохраняют самостоятельную product role в пределах AC-301/303;
3. `PORT-001/002/004` фиксируются как OS consumer reference implementations, не OS capabilities;
4. `PORT-005/006` фиксируются как contained product-family reference implementations/evidence sources, без growth mandate;
5. `PORT-007` фиксируется только как clarification-only Company/product-family module candidate;
6. Company-side новых OS capability candidates остаётся `0`;
7. `PORTFOLIO.md` должен быть синхронизирован с role classification без переписывания product truth;
8. дорожная карта должна закрыть AC-304 и перевести current action на AC-305.

До явного Owner approval этот документ остаётся proposal и не меняет canonical portfolio map.

## 12. Статус

`AC-304 — Proposed 0.9.0 / Pending cross-review and explicit Owner approval.`

Следующий canonical step после успешного cross-review и approval:

`AC-305 — Сверка межпродуктовых зависимостей и контрактов продуктов с Arvectum OS`.
