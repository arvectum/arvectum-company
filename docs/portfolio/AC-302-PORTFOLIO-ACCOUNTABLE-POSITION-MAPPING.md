# AC-302 — Закрепление ответственной организационной позиции за продуктами и инициативами портфеля

Статус: `Proposed`
Версия: `0.9.0`
Дата: `2026-08-21`
Владелец документа: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-302 — Assign accountable Position to each active product/initiative`
Максимум итераций перекрёстной проверки: `10`

## 1. Цель и граница AC-302

AC-302 связывает утверждённые Company-level portfolio identities `PORT-001…PORT-007` с уже утверждённой M2 Position model так, чтобы каждый активный или materially retained узел имел однозначную организационную accountability.

Задача не создаёт по одной должности на продукт. Она отвечает на более узкий вопрос:

> Какая существующая долговременная Position отвечает на уровне Arvectum Company за то, чтобы конкретный portfolio node имел актуальную Company-level идентичность, понятную роль, корректный статус/источник, подготовленный continue/change/stop/reuse вопрос и своевременную эскалацию — при том что коммерческая, техническая, финансовая и security accountability остаётся у своих функциональных Positions?

AC-302 **не**:

- создаёт новые Positions, departments или product-manager headcount;
- изменяет AC-205 Principal-to-Position Assignments;
- превращает текущего Principal, GitHub owner/admin или AI runtime в источник authority;
- утверждает budget, capital allocation, цену, profitability, investment priority или stop/continue decision — это AC-303/AC-306;
- классифицирует узел как reusable module/reference implementation/OS capability — это AC-304;
- изменяет Product Contract или dependency Arvectum OS — это AC-305 и применимый OS governance path;
- изменяет product implementation truth, legal/IP ownership, customer authority, SLA или production readiness;
- активирует `AM-3` или `AM-4`.

## 2. Каноническая основа

AC-302 опирается на следующие действующие Company artifacts:

- `docs/portfolio/PORTFOLIO.md` — `Active 0.2.0`, baseline `AC-301 Approved 1.0.0`;
- `docs/portfolio/AC-301-PORTFOLIO-IDENTITY-BOUNDARY-OWNERSHIP-RECONCILIATION-v1.0.0.md` — семь стабильных identities и bounded dispositions;
- `docs/organization/INITIAL-POSITION-REGISTRY-v1.0.0.md` — шесть утверждённых Positions;
- `docs/organization/INITIAL-ASSIGNMENTS-AND-EXECUTOR-CLASSIFICATION-v1.0.0.md` — текущая executor realization;
- `docs/governance/RESERVED-OWNER-DECISIONS-v1.0.0.md` — `ROD-01…ROD-09`;
- `docs/governance/DELEGATED-POSITION-AUTHORITY-MODEL-v1.0.0.md` — `AM-0…AM-4`, deny-by-default и escalation semantics;
- `docs/security/COMPANY-DATA-TOOL-CREDENTIAL-ACCESS-BOUNDARY-v1.0.0.md` — access ceiling;
- `docs/operations/CRITICAL-FUNCTION-CONTINUITY-REPLACEMENT-FALLBACK-BASELINE-v1.0.0.md` — continuity/replacement boundary;
- `docs/constitution/COMPANY-CONSTITUTION.md` — Company authority and organizational model;
- `docs/roadmap/ROADMAP.md` — AC-302 как текущий канонический шаг.

Применимые product repositories остаются каноническими для product-specific implementation/status/roadmaps. Arvectum OS остаётся каноническим для OS Product Contracts и platform semantics.

## 3. Главный вывод

### 3.1. Primary accountable Position

Для **всех семи текущих portfolio nodes** primary Company-level accountable Position устанавливается как:

`POS-003 — Portfolio & Product Lead`.

Это не случайное объединение и не универсальное правило «всеми продуктами управляет один Product Lead». Оно прямо следует из утверждённого AC-204 scope `F-04 — Portfolio / Product / Workstream Stewardship / Reuse` и accountable outcomes `POS-003`:

- каждый material portfolio node должен иметь current purpose, lifecycle/status reference и accountable question;
- continue/change/stop/reuse/module-candidate evidence должно быть собрано до material Owner decision;
- product/workstream state должен указывать на реальный product canonical source;
- product-specific implementation не переносится в Company scope;
- reusable patterns не продвигаются молча в Arvectum OS.

AC-204 отдельно предусматривает, что Phase 3 **может** позднее обосновать product-specific Positions при достаточной независимой выручке, customer obligations, roadmap complexity, investment или domain accountability. Текущая evidence base пока не требует такого split.

### 3.2. Что означает primary accountability

Связь `PORT-* → POS-003` означает accountability за Company-level stewardship portfolio node:

- актуальность Company-level identity, aliases и canonical repository/status-source locator;
- корректность portfolio role и bounded lifecycle/disposition state;
- видимость главного product/initiative question и следующего governance gate;
- сбор evidence для continue/change/stop/reuse/investment решений;
- эскалацию при выходе за `AM-0/1/2`, попадании в `ROD-*`, изменении Company↔Product↔OS boundary или существенном customer/risk/financial effect;
- недопущение тихого scope creep, stale status и competing Company-level product identities.

Эта accountability **не** означает end-to-end владение всеми функциями продукта.

## 4. Утверждаемая после approval accountability map

| Portfolio ID | Узел | AC-301 disposition | Primary accountable Position | Обоснование текущего mapping | Ключевые обязательные interfaces |
|---|---|---|---|---|---|
| `PORT-001` | Arvectum Tender Agent | `continue` | `POS-003 — Portfolio & Product Lead` | самостоятельная procurement product line требует Company-level lifecycle/priority/reuse stewardship; stale P6.02 locator и будущие product-family вопросы должны оставаться явными governance questions | `POS-002` customer/commercial; `POS-004` engineering/release; `POS-005` economics/obligations; `POS-006` security/risk/continuity; `POS-001` + Owner при ROD/material cases |
| `PORT-002` | Discount Parser | `continue` | `POS-003` | productized client solution остаётся самостоятельным node; Company должна удерживать product role, client-solution vs reusable-engine boundary и дальнейший investment/reuse question | `POS-002` customer/delivery; `POS-004` technical/release; `POS-005`; `POS-006`; `POS-001`/Owner при material commitment/change |
| `PORT-003` | Arvectum Proxy Launcher | `continue` | `POS-003` | самостоятельный productization track требует portfolio stewardship без превращения Engineering в product-investment authority | `POS-004` productization/release; `POS-006` security/dependency/sovereignty; `POS-005` economics; `POS-002` при external commercial contour; `POS-001`/Owner для ROD |
| `PORT-004` | Creative Test Agent | `continue` | `POS-003` | отдельный controlled-pilot product; Company-level Position должна удерживать границу Creative Test Agent vs broader Marketing Agent hypothesis и investment/productization question | `POS-002` customer/commercial/pilot; `POS-004` engineering; `POS-005`; `POS-006`; `POS-001`/Owner при material changes |
| `PORT-005` | Tender Small-Volume Calculator | `contain` | `POS-003` | contained product experiment всё равно требует владельца Company-level question: сохранить, включить в procurement family, извлечь полезное, продолжить или предложить retirement; отдельный Product Position сейчас был бы fake headcount | `POS-004` только bounded maintenance/evidence; `POS-002` при наличии customer evidence; `POS-005/006` по необходимости; Owner через ROD при material continue/merge/stop investment decision |
| `PORT-006` | Doors Parser | `contain` | `POS-003` | завершённый client-delivery experiment должен иметь portfolio custodian для reuse/maintenance/archive question, но не оправдывает отдельную постоянную product Position | `POS-002` customer/history/scope; `POS-004` bounded maintenance/reuse evidence; `POS-006` data/dependency concerns; `POS-005` при cost/obligation; Owner при material reuse/investment decision |
| `PORT-007` | Data Platform | `clarify` | `POS-003` | неопределённая инициатива нуждается прежде всего в accountable clarification: business problem, consumers, boundary и strategic/economic hypothesis; создание отдельной Position до этого усилило бы неопределённость | `POS-002` consumer/problem evidence; `POS-004` feasibility only after scope; `POS-005` cost/economics; `POS-006` sovereignty/dependency/data; `POS-001`/Owner при admission/material investment/boundary decision |

## 5. Почему не создаются product-specific Positions сейчас

AC-204 уже содержит прямой safeguard: не создавать один Product Manager/Product Owner на каждый repository лишь потому, что существует несколько portfolio nodes.

По состоянию AC-302 нет доказательств, что для любого одного `PORT-*` одновременно возникла достаточно самостоятельная долговременная accountability boundary, превосходящая стоимость нового Position. В частности, текущие evidence не доказывают для отдельного узла такой совокупности факторов, как:

- устойчивый независимый revenue/P&L contour;
- отдельный существенный поток customer obligations;
- постоянный product-roadmap workload, который POS-003 уже не может вести как portfolio stewardship;
- domain-specific authority, которую нельзя корректно выразить через существующие functional Positions;
- материальный conflict of duties, требующий отдельной Position;
- повторяющийся queue/bottleneck, обусловленный именно общей `POS-003`, а не текущей концентрацией Principal/Owner workload.

Поэтому изменение Initial Position Registry в AC-302 не требуется.

## 6. Разделение node accountability и functional accountability

Primary `POS-003` mapping **не поглощает** другие Positions.

### `POS-002 — Commercial & Customer Lead`

Остаётся accountable за discovery, qualification, commitment preparation, customer delivery/acceptance/support в своём approved scope. `POS-003` не может принять customer acceptance или создать commercial promise лишь потому, что отвечает за portfolio node.

### `POS-004 — Engineering & Release Lead`

Остаётся accountable за technical decomposition, implementation, QA, packaging и release evidence для accepted work. Technical PASS не становится portfolio continue decision. Engineering не получает product-investment authority.

### `POS-005 — Finance & Obligation Control Lead`

Остаётся accountable за decision-relevant economics/cash/obligation evidence. `POS-003` не может заменить finance evidence собственным product judgment.

### `POS-006 — Security, Risk & Continuity Lead`

Остаётся accountable за access/data/security/dependency/continuity assurance. `POS-003` не может принять material risk/security/data exception.

### `POS-001 — Company Executive`

Остаётся Company-level operating integration boundary: decision-ready escalation, cross-Position coordination, publication/state mechanics и routing к Owner/legal/corporate authority. `POS-003` не становится универсальным Company Executive для product matters.

## 7. Principal / Assignment boundary

AC-205 уже устанавливает текущую realization `POS-003` как `Hybrid`: текущий Owner Principal выполняет routine portfolio judgment/direct proposals, AI — synthesis/evidence/options/review.

AC-302 **не создаёт нового Assignment** и не утверждает Owner как product owner в юридическом или персонально-незаменимом смысле.

Действует цепочка:

`PORT node → accountable Position POS-003 → current valid Assignment(s) → runtime/access → execution`.

Если Principal или AI runtime заменяется, `PORT-* → POS-003` сохраняется, пока отдельное approved Position-model change не установит иное.

Текущая концентрация Owner Principal в нескольких Positions остаётся operational gap/constraint, а не основание превращать Owner capacity в постоянную продуктовую должность.

## 8. Authority и escalation

`POS-003` действует только в approved initial ceiling `AM-0`, `AM-1`, `AM-2`.

### Внутри bounded scope

Position может:

- анализировать product/initiative state;
- готовить options и recommendations;
- синхронизировать уже approved portfolio decisions/status references;
- выполнять routine prioritization/status coordination внутри уже approved portfolio/workstream envelope;
- инициировать evidence collection и handoffs к другим Positions.

### Обязательная эскалация

Position должна остановиться/эскалировать, когда case затрагивает, в частности:

- `ROD-01` — strategy/business model;
- `ROD-02` — material capital allocation/exposure;
- `ROD-03` — material/non-standard external commitment;
- `ROD-04` — major portfolio/initiative/investment decision;
- `ROD-05` — material authority/organizational-model change;
- `ROD-06` — material risk acceptance;
- `ROD-07` — customer/data sovereignty/reuse exception;
- `ROD-08` — core IP/critical dependency/technology-sovereignty exception;
- `ROD-09` — material Company↔Product↔Arvectum OS or cross-repository commitment;
- создание/изменение юридически значимого обязательства;
- customer approval outside Company authority;
- отсутствие достаточных financial/security/customer/technical evidence от соответствующей Position/source.

Эскалация идёт через `POS-001` и/или непосредственно к Owner/компетентному legal/corporate Principal в соответствии с применимым workflow и authority source. Product/OS/customer scope также требует соответствующей product/OS/customer authority, а не Company Position title.

## 9. Access и continuity

AC-302 не меняет AC-206 access ceilings. `POS-003` может получать evidence/read access и bounded Company portfolio publication capability, но mapping узла не создаёт product repository write/admin, production, secret, customer-system или financial access.

AC-207 continuity также сохраняется без изменений:

- при недоступности AI `POS-003` может деградировать к human execution в рамках существующего Assignment;
- при недоступности Owner human AI может продолжать evidence preparation, но не получает human `AM-2`, `ROD-*` или юридическую authority;
- product repository остаётся source of product implementation truth;
- replacement runtime не меняет `PORT-* → POS-003` accountability.

## 10. Node-specific accountable questions после AC-302

`POS-003` должно поддерживать для каждого узла как минимум один явный portfolio question до следующих gates:

| Node | Обязательный текущий accountable question |
|---|---|
| `PORT-001` | Как закрыть identity/dependency lineage с P6.02 и каков следующий bounded investment/productization contour без преждевременного merge с PORT-005? |
| `PORT-002` | Какая часть остаётся конкретным client solution/product, а какая потенциально заслуживает reusable-module consideration только после AC-304 evidence? |
| `PORT-003` | Каков экономически оправданный standalone/internal role и какие technology-sovereignty/security constraints materially влияют на investment decision? |
| `PORT-004` | Остаётся ли scope Creative Test Agent самостоятельным продуктом или появятся evidence для более широкой marketing product family — без rename-by-aspiration? |
| `PORT-005` | Сохранить как contained experiment, интегрировать часть в procurement family, использовать как reference evidence или предложить retirement — после AC-303/304/306 evidence? |
| `PORT-006` | Какую ценность имеет сохранение/maintenance/reuse зрелого client-delivery parser asset и есть ли evidence для module candidate без автоматической universalization? |
| `PORT-007` | Какой конкретный business problem, consumer, cost/risk boundary и Company/Product/OS ownership hypothesis оправдывают существование Data Platform до material development? |

Эти questions не являются ответами и не предрешают AC-303…AC-306.

## 11. Position-model change triggers

Отдельный product-specific Position или split `POS-003` должен рассматриваться только через явный change proposal, если появляется evidence одного или нескольких факторов:

1. отдельный продукт имеет устойчивую независимую revenue/customer-obligation accountability;
2. product roadmap/release/customer complexity создаёт постоянный workload, который нельзя безопасно вести в общей portfolio Position;
3. один Principal/Position становится повторяющимся cross-product bottleneck несмотря на нормальную automation/delegation;
4. product-specific regulatory/security/domain risk требует самостоятельной accountable authority boundary;
5. конфликт между portfolio investment recommendation и product operating responsibility становится материальным;
6. продукт получает самостоятельную команду/несколько Principals и им требуется единый durable product operating boundary;
7. доказана экономическая ценность нового Position выше governance/coordination overhead.

До такого evidence создание отдельного Product Lead на каждый node считается premature organizational complexity.

## 12. Reconciliation register

| ID | Вопрос | Решение AC-302 | Следующий gate |
|---|---|---|---|
| `R-302-01` | кто primary accountable за все семь Company portfolio identities | `POS-003` | binding после Owner approval AC-302 |
| `R-302-02` | нужен ли отдельный Product Position для каждого `continue` node | нет текущего evidence; registry не меняется | future Position-model change только по evidence |
| `R-302-03` | кто отвечает за `contain` nodes | `POS-003` как portfolio custodian; scope expansion запрещён без следующего решения | AC-303/304/306 |
| `R-302-04` | кто отвечает за `clarify` Data Platform | `POS-003` за clarification/admission package, не за автоматическое развитие | AC-303/304/306 |
| `R-302-05` | заменяет ли POS-003 Engineering/Commercial/Finance/Security | нет, functional accountability остаётся разделённой | ongoing M2 model |
| `R-302-06` | создаёт ли mapping новый Principal Assignment/access | нет | AC-205/206 остаются controlling |
| `R-302-07` | меняет ли mapping Owner-reserved authority | нет | AC-202/203 controlling |
| `R-302-08` | изменяет ли mapping Product/OS canonical ownership | нет | product repositories / AC-305 / OS governance |
| `R-302-09` | когда нужен product-specific Position | только при evidence triggers из §11 и отдельном approved change | future governance |

## 13. Acceptance criteria

AC-302 может быть утверждён, если одновременно подтверждено:

1. каждый `PORT-001…PORT-007` имеет один primary Company accountable Position;
2. mapping выведен из существующей M2 Position model, а не из repository names;
3. не создано fake headcount и не применён принцип «один продукт — одна должность»;
4. node accountability не поглотила commercial, engineering, finance, security или Company-executive accountability;
5. current Principal/AI runtime не стал источником authority;
6. `ROD-01…ROD-09` и `AM-0/1/2` ceiling сохранены;
7. contained/clarify nodes имеют owner of the question без автоматического scope expansion;
8. product implementation, customer authority и OS governance остаются вне Company Position title;
9. access и continuity boundaries не расширены;
10. AC-303 остаётся следующим каноническим Phase 3 action после approval.

## 14. Предлагаемый результат

После Owner approval:

- `POS-003 — Portfolio & Product Lead` становится primary Company-level accountable Position для `PORT-001…PORT-007`;
- остальные Positions сохраняют свою functional accountability и обязательные interfaces;
- Initial Position Registry не изменяется;
- AC-205 Assignments не изменяются;
- отдельные product-specific Positions не создаются;
- roadmap может закрыть AC-302 как `Complete / PASS` и перейти к `AC-303 — Investment, cost and risk boundaries; continue/change/stop criteria`.

До явного Owner approval этот документ остаётся proposal и не изменяет binding portfolio/Position state.
