# AC-404 — Cash, Commitment and Management Reporting Baseline

Статус: `Proposed`
Версия: `0.9.0`
Создано: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-404 — Cash, commitment and management reporting baseline`
Предшественники: `AC-401 — Approved 1.0.0`; `AC-402 — Approved 1.0.0`; `AC-403 — Approved 1.0.0`
Статус утверждения: `Pending explicit Owner approval of the exact reviewed proposal`

## 1. Назначение

AC-404 определяет минимальную Company-level модель **управленческой видимости денег, обязательств и финансово значимых сигналов**, достаточную для Owner/Position decisions и последующих AC-405…AC-407.

Цель AC-404 — дать собственнику возможность без ручной реконструкции бухгалтерии понимать:

- есть ли decision-relevant liquidity evidence для материального решения;
- какие material cash outflows/obligations приближаются, просрочены или неопределённы;
- какие material receivables/inflows ожидаются и насколько они подтверждены;
- какие recurring costs и approved commitments создают будущую нагрузку;
- где есть procurement/project cash gap либо иная liquidity exposure;
- какие финансовые facts являются source truth, какие — management interpretation, а какие — forecast/hypothesis;
- какие decision/approval/risk/incident items требуют действия Owner или другой authority;
- насколько свежи и полны источники, на которых основан management view.

AC-404 **не** создаёт вторую бухгалтерию, банк, налоговый регистр, платёжный workflow, treasury system или spend authority.

Главный принцип:

```text
bank/accounting fact
≠ management interpretation
≠ forecast
≠ budget/limit
≠ planned spend
≠ approved internal commitment
≠ incurred obligation
≠ actual payment
```

## 2. Governing baseline

AC-404 подчинён применимым юридическим/корпоративным источникам, Ratified Company Constitution и Approved Company governance.

### 2.1 AC-102 financial boundary

AC-102 уже установил три разных слоя:

1. **statutory/accounting layer** — outsourced accounting, bank/accounting systems, tax/legal records; authoritative external truth;
2. **management-finance layer** — Company-level interpretation для Owner decisions, budgets, commitments, portfolio и risk;
3. **product/project economics** — product/project revenue, direct cost, implementation/support burden и unit-economics evidence.

AC-102 прямо запрещает превращать Company repository в transaction ledger и определяет required accounting→management interface: available cash/material liquidity issue, mandatory payments requiring attention, material receivables/payables, material new/overdue obligations, unusual material cash movements и periodic management summary.

### 2.2 M4 control layers

AC-404 строится поверх уже Approved:

- `AC-401`: `WORK-*` / `OBL-*`;
- `AC-402`: `DEC-*` / `APR-*` / `ESC-*`;
- `AC-403`: `RSK-*` / `EXC-*` / `INC-*`.

AC-404 не создаёт дублирующие финансовые identities для тех же obligations/decisions/risks.

### 2.3 Authority baseline

Сохраняются:

- `ROD-02 — Capital allocation and material financial exposure`;
- `ROD-03 — Material external commitments and non-standard commercial exposure`;
- применимые `ROD-04`, `ROD-06` и иные `ROD-*`;
- `AM-0…AM-4` и deny-by-default AC-203;
- Position/Assignment/access intersection;
- отдельность Owner, participant/general-meeting, General Director, bank/signature actor и internal Position capacity.

Наличие денег, видимость отчёта, доступ в интернет-банк или подготовленный payment draft не создают Organizational Authority или legal/payment authority.

### 2.4 Accountability baseline

`POS-005 — Finance & Obligation Control Lead` является primary Company Position для management-finance, cash/commitment visibility и obligation control.

Current AC-205 realization — `Human-led + external-service interface`: management-finance judgment остаётся у текущего human/Owner Principal в Position capacity; outsourced accounting/tax service поставляет professional/statutory/accounting facts в своём contour.

Это не делает POS-005 бухгалтерией и не передаёт ей по умолчанию payment/signature/spend approval authority.

## 3. Current Arvectum OS boundary

Перед AC-404 проверен current `arvectum/arvectum-os` `main` на commit:

`76504766353028540891ac1dfdbf1e5dc331a4af`.

Current OS roadmap `2.81.0` фиксирует `M9-alpha — Usable Internal Workspace` как `Achieved / PASS` в exact private internal scope и переводит current action на `P9.07 — Product-owned workspace surfaces / composition`.

Это полезно как будущий presentation/composition substrate, но:

- current OS `Decision Authority Policy` остаётся `Proposed 0.2.1`;
- OS workspace visibility не создаёт Company financial authority;
- M9-alpha не создаёт public/stable financial surface, Stable Product Contract или Active Platform Capability;
- Company-specific cash/commitment semantics не переносятся в OS по импликации.

AC-404 не создаёт OS Product Contract, finance capability, banking integration или payment execution path.

## 4. Source-of-truth architecture

AC-404 использует **reference-over-copy** и разделяет три уровня.

### 4.1 Authoritative fact sources

В зависимости от предмета source truth остаётся в соответствующем contour:

- bank balance / actual payment / bank availability — bank/payment source;
- accounting balance, receivable/payable, tax/accounting classification — professional accounting system/provider;
- legal/customer/vendor obligation — applicable contract/legal/customer/vendor source;
- corporate act — applicable corporate source;
- product/project economics evidence — product/project source;
- portfolio identity/disposition — `docs/portfolio/PORTFOLIO.md`;
- Company control identity/state — AC-401…AC-403 registers/models.

### 4.2 Company management interpretation

Company MAY быть authoritative для bounded management interpretation, например:

- что факт materially значим для Company decision;
- какой `OBL-*`/`RSK-*`/`DEC-*` с ним связан;
- какой `POS-*` отвечает за management control;
- какой current attention/priority context применяется;
- какой next control point нужен;
- какая uncertainty/freshness limitation должна быть показана.

Management interpretation не переписывает source fact.

### 4.3 Management report / snapshot

Management report является **derived decision-support projection** над current sources и Company control state.

Он не является:

- ledger;
- bank statement;
- tax register;
- legal proof of obligation;
- proof of payment;
- spend authorization;
- budget approval;
- proof of profitability.

Если report расходится с authoritative source, source fact имеет приоритет в своей области, а report должен быть reconciled либо marked stale/uncertain.

## 5. AC-404 не создаёт отдельный financial transaction namespace

AC-404 намеренно **не** вводит `FIN-*`, `PAY-*`, `TX-*` или иной универсальный Company ledger namespace.

Причины:

1. transaction/payment truth уже принадлежит банку/accounting contour;
2. material obligations уже имеют `OBL-*` control identities;
3. material decisions/approvals — `DEC-*`/`APR-*`;
4. financial risks/incidents/exceptions — `RSK-*`/`INC-*`/`EXC-*`;
5. новый transaction namespace создал бы competing source of truth и Owner/admin burden.

Отдельный report instance MAY позже иметь технический identifier в реализации, но это не новый класс financial authority или transaction identity и не является обязательной частью AC-404 semantics.

## 6. Финансовые состояния, которые нельзя смешивать

### 6.1 `cash fact`

Подтверждённый денежный факт из bank/accounting source на explicit `as_of`.

Примеры: доступный остаток, исполненный платёж, поступившие деньги — только если source действительно подтверждает факт.

### 6.2 `budget / limit`

Утверждённый внутренний предел допустимого расхода/экспозиции.

Budget/limit:

- не является obligation;
- не означает, что деньги существуют или зарезервированы;
- не требует потратить сумму;
- не отменяет отдельные approval/legal/payment gates;
- не создаётся AC-404.

### 6.3 `planned spend`

Намерение/forecast будущего расхода, ещё не ставшее binding obligation.

Planned spend не равен approval и не равен payable.

### 6.4 `approved internal commitment`

Внутреннее Company decision/approval, разрешающее exact bounded course of action в пределах existing authority.

Такое решение MAY быть необходимым, но не всегда достаточным для создания external obligation. Если требуется договор, заказ, корпоративный акт, подпись, bank action или customer/vendor acceptance, соответствующий external/legal gate остаётся отдельным.

### 6.5 `incurred obligation`

Реальное обязательство уже возникло на основании authoritative source.

Если оно material для Company control, оно должно быть связано с `OBL-*`. Internal intent или roadmap не создают incurred obligation.

### 6.6 `actual payment`

Фактически совершённое движение денег, подтверждённое bank/accounting source.

`approved` или `payment prepared` не означает `paid`.

### 6.7 `receivable / expected inflow`

Подтверждённая receivable и ожидаемое поступление — разные вещи.

Management view MUST различать как минимум:

- authoritative receivable/source-backed amount/date/condition;
- forecasted receipt timing;
- speculative/conditional inflow.

Forecast receipt не считается cash до фактического поступления.

## 7. Minimal management-finance view

AC-404 определяет минимальный management view, а не экран или software schema.

Для decision-relevant snapshot SHOULD быть возможно восстановить следующие поля напрямую или по references:

| Поле | Смысл |
|---|---|
| `report_as_of` | момент, к которому относится management view |
| `source_freshness` | свежесть/полнота ключевых bank/accounting/contract sources |
| `available_cash_fact_ref` | ссылка на authoritative available-cash evidence; exact value может оставаться private |
| `liquidity_status` | `sufficient_for_known_case`, `potential_issue`, `insufficient`, `unknown`, `not_assessed`; management interpretation, не bank fact |
| `material_due_outflows` | material due/triggered `OBL-*` и authoritative refs |
| `material_receivables` | material receivable refs + due/condition/freshness |
| `material_payables` | material payable/obligation refs + due/condition/freshness |
| `recurring_cost_signal` | material recurring burden/renewal signal без полного subscription ledger |
| `expected_inflows` | material forecast inflows с source/basis/condition/confidence class |
| `expected_outflows` | material forecast outflows, ещё не обязательно incurred obligations |
| `approved_not_yet_incurred_exposure` | material approved internal spend/commitment decisions, не ставшие external obligations |
| `procurement_cash_gap_cases` | material procurement/financing gaps/uncertainty refs |
| `portfolio_project_economic_signals` | relevant `PORT-*`/project economics exceptions or decision inputs |
| `mandatory_payment_attention` | tax/statutory/other mandatory items, которые accounting/legal contour пометил material/attention-worthy |
| `risk_exception_incident_refs` | связанные `RSK-*`/`EXC-*`/`INC-*` |
| `decision_approval_escalation_refs` | связанные `DEC-*`/`APR-*`/`ESC-*` |
| `unknowns_and_gaps` | missing/stale/incomplete source facts |
| `next_control_point` | следующий management checkpoint/event |

Не каждое поле обязано иметь число. `unknown` предпочтительнее fabricated precision.

## 8. Liquidity and cash-gap logic

### 8.1 No fabricated liquidity confidence

AC-404 не вводит автоматический `green/yellow/red`, runway, burn rate, probability или cash forecast без достаточного evidence.

Если source completeness, timing или obligation scope неизвестны, management view должен показывать uncertainty.

### 8.2 Confirmed outflows versus uncertain inflows

Подтверждённое material near-term обязательство **не должно автоматически считаться покрытым** speculative/conditional/uncertain inflow.

Любая liquidity margin формула MAY использоваться только если:

- explicit source set известен;
- as-of одинаково понятен;
- inclusion/exclusion rules указаны;
- receivable/forecast certainty не маскируется;
- result помечен management projection, а не bank/accounting fact.

### 8.3 Procurement cash gap

Для material procurement case management view SHOULD показывать по references:

```text
customer payment timing/condition
→ supplier payment timing/condition
→ working-capital gap
→ financing/security/direct-cost exposure
→ linked OBL/RSK/DEC/approval state
```

Если gap magnitude/timing нельзя подтвердить, он остаётся `unknown`/decision-blocking пропорционально consequence.

## 9. P0 and attention discipline

AC-106 остаётся governing priority model:

`P0 — protect current obligations, cash and material risk`.

AC-404 не делает любой invoice, overdue item или accounting question P0.

P0 SHOULD возникать только при реальном material/time-sensitive condition, например:

- due/near-due material obligation, для которого decision-relevant liquidity insufficient или unknown;
- mandatory/tax/corporate payment at material risk of non-performance;
- material commitment decision при отсутствии current liquidity/obligation evidence;
- material overdue receivable/payable, который угрожает existing obligation, customer delivery или continuity;
- procurement cash gap, который может materially нарушить исполнение/ликвидность;
- unexpected material cash movement, bank/access failure или accounting gap, требующий bounded decision/risk/incident response.

Owner attention должна быть **exception/decision driven**. Routine bookkeeping, bank reconciliation, ordinary invoice matching и receipt classification не становятся Owner work.

## 10. Freshness, reconciliation and uncertainty

### 10.1 Freshness

Любой dynamic financial statement в management view MUST иметь `as_of`/freshness evidence пропорционально consequence.

Stale data не превращается в current truth лишь потому, что была последняя известная цифра.

### 10.2 Reconciliation

Reconciliation в AC-404 означает не transaction-level bank reconciliation, а management-control reconciliation:

- source reference всё ещё доступен/актуален;
- Company interpretation соответствует source state;
- linked `OBL-*`/`DEC-*`/`RSK-*` не противоречат известным facts;
- changed facts вызывают review нужных decisions/forecasts.

### 10.3 Unknown is first-class

Допустимые states включают:

- `current/verified`;
- `stale`;
- `incomplete`;
- `conflicting`;
- `unknown`.

Material unknown MUST либо блокировать consequential decision/effect, либо создавать `needs_attention`/`ESC-*` в соответствии с действующей authority/risk моделью.

## 11. Accounting-provider interface

Outsourced accounting/tax service остаётся external professional function и source of professional/statutory/accounting facts.

Минимальный management interface SHOULD уметь выдавать или позволять получить:

- current cash/balance evidence, когда требуется decision;
- material receivables/payables;
- material mandatory/tax payment attention;
- material overdue/new obligations within its competence;
- unusual/material transaction context requiring management review;
- source references sufficient for current management interpretation.

AC-404 не требует, чтобы provider использовал Company IDs или Arvectum OS.

Если provider недоступен или evidence stale, Company не должна реконструировать accounting truth из памяти. Material decision выполняет fail-closed/escalation behavior пропорционально consequence.

## 12. Position accountability and separation of duties

### 12.1 POS-005

`POS-005 — Finance & Obligation Control Lead` accountable за:

- получение/проверку достаточности management-finance inputs;
- mapping material financial facts к `OBL-*`, `DEC-*`, `RSK-*`, portfolio/project decisions;
- краткую management interpretation и uncertainty;
- preparation финансовой части decision packet;
- своевременную escalation при material evidence gap.

POS-005 не получает payment/spend approval authority по факту этой ответственности.

### 12.2 POS-001 / POS-003 / POS-006

- `POS-001` использует finance evidence для Company coordination/decision routing;
- `POS-003` использует product/project economics для portfolio stewardship;
- `POS-006` независимо рассматривает material financial continuity/risk dependencies там, где они становятся risk/incident subject.

Если один физический Principal выполняет несколько Position capacities, records/authority context всё равно должны различаться. Proposer of material spend/commitment не становится sole approver из-за того, что тот же человек умеет собрать finance evidence.

## 13. Decision and commitment control sequence

Для material spend/commitment типовая semantic sequence:

```text
need / proposal / forecast
        ↓
management finance evidence
        ↓
DEC-* / APR-* if authority gate required
        ↓
internal approval within exact scope
        ↓
external/legal/corporate/vendor/bank act if required
        ↓
OBL-* once a material obligation actually exists
        ↓
actual payment only when bank/accounting source confirms it
        ↓
reconciliation / satisfaction evidence
```

Ни один шаг не выводится автоматически из предыдущего.

Особенно:

- budget ≠ approval;
- approval ≠ external obligation;
- obligation ≠ payment;
- payment ≠ obligation satisfaction in every case;
- technical bank access ≠ spend authority.

## 14. Forecast and hypothesis semantics

Forecasts полезны для decisions, но MUST сохранять происхождение и uncertainty.

Для material expected inflow/outflow SHOULD быть видно:

- source/basis;
- amount or range only if evidence supports it;
- expected timing/condition;
- confidence semantics: `contractual/source-backed`, `reasonably_expected`, `conditional`, `speculative/unknown` либо более precise approved taxonomy later;
- `as_of`;
- linked decision/obligation/risk.

Forecast MUST NOT автоматически изменять accounting/cash truth.

## 15. Minimum Owner management report

До AC-406 Owner Mission Control достаточно **одного короткого management packet**, который отвечает на вопросы:

1. Есть ли material liquidity issue или ключевой source gap сейчас?
2. Какие material cash obligations требуют внимания раньше остальных?
3. Какие material receivables/inflows materially влияют на decisions и насколько они подтверждены?
4. Какие recurring commitments создают decision-relevant будущую нагрузку?
5. Есть ли procurement/project cash gaps?
6. Какие financial risks/incidents/exceptions активны?
7. Какие decisions/approvals/escalations требуют Owner/other authority?
8. Что неизвестно/stale и что нельзя безопасно заключить?
9. Какой next control point?

Report MAY быть Markdown, private sheet/export, approved tool projection или позже OS-backed presentation. AC-404 не выбирает software implementation.

## 16. Cadence boundary

AC-404 намеренно **не устанавливает произвольный weekly/monthly reporting ritual** без operating evidence. Cadence принадлежит AC-407.

До AC-407 минимальные mandatory refresh triggers:

- перед material capital allocation / spend / external commitment decision;
- перед material portfolio/investment decision, если finance evidence materially relevant;
- при near-due material obligation;
- при material new/changed obligation, receivable/payable или procurement cash-gap fact;
- при material bank/accounting availability/freshness incident;
- при material changed fact, который может invalidate prior decision/forecast.

Recurring periodic summary MAY использоваться operationally, но AC-404 не превращает конкретную частоту в binding rule.

## 17. Confidentiality and public-repository boundary

Current `arvectum/arvectum-company` repository публичный.

В нём MUST NOT храниться ради management convenience:

- bank account numbers/payment credentials;
- detailed bank statements/transaction exports;
- signatures, keys, tokens, banking authorization artifacts;
- tax returns/ledgers/source documents с unnecessary sensitive data;
- customer/vendor confidential invoices/contracts, если можно использовать reference;
- salary/PII payloads;
- exact confidential cash balances, если их публикация не нужна и не одобрена;
- privileged fraud/security/payment incident details;
- chain-of-thought.

Public repo хранит model, safe metadata, references и governance evidence. Exact operational values должны находиться в подходящем restricted/authoritative contour.

## 18. Portfolio / product economics boundary

AC-404 не создаёт Company-wide fictitious unit economics для `PORT-*` nodes.

Portfolio view MAY ссылаться на:

- actual revenue evidence;
- direct/project cost evidence;
- recurring burden;
- owner workload/non-cash investment where decision relevant;
- approved/actual investment;
- current obligations/support burden;
- profitability/unit-economics evidence when реально available.

Missing CAC/LTV/ROI/margin data остаётся missing evidence, а не автоматически `0` или positive/negative value.

AC-405 later определит, как эти signals участвуют в portfolio review cadence.

## 19. Owner Mission Control / Arvectum OS handoff

AC-406 MAY представить AC-404 management signals в Owner Mission Control, но presentation остаётся derived.

Если Arvectum OS будет использоваться для persistence/projection/composition:

- Company-specific semantics остаются Company-owned;
- bank/accounting facts остаются source-owned;
- OS visibility не создаёт spend/approval authority;
- data minimization/Organization scope/access controls применяются;
- integration требует explicit admitted boundary/Product Contract where applicable.

M9-alpha/P9.07 progress в OS сам по себе не создаёт этот boundary.

## 20. Implementation sufficiency

Минимально достаточная реализация после approval MAY быть:

- short private management report + references;
- structured Markdown/YAML/JSON metadata без sensitive values;
- spreadsheet/export from professional accounting contour;
- light script generating a derived snapshot;
- later governed OS projection.

Выбор реализации должен быть replaceable и не создавать parallel ledger.

Software dashboard не является AC-404 completion criterion.

## 21. Evidence and validation after adoption

Реальная полезность AC-404 должна позже проверяться operational evidence, например:

- Owner может принять material commitment decision без ручного восстановления bank/accounting context;
- due material obligations не теряются;
- speculative inflow не маскируется под cash;
- stale/unknown finance evidence действительно блокирует unsafe decision;
- routine accounting не создаёт Owner workload;
- portfolio decisions получают relevant economics evidence, а не repo activity proxies;
- no unauthorized payment/spend occurs because visibility/access was mistaken for authority.

Technical/model PASS не доказывает, что current cash data complete или management reporting работает в реальной эксплуатации.

## 22. Handoff to AC-405…AC-407

### AC-405

Получает finance/economics signals для portfolio/module/priority review, но не право автоматически stop/start/fund products.

### AC-406

Получает minimal management packet semantics для Owner Mission Control. Presentation не становится source of truth/authority.

### AC-407

Определяет management operating cadence, refresh/review responsibilities, recurring control cycle и evidence of actual use. AC-404 intentionally leaves cadence unresolved except for material event/decision triggers.

## 23. Explicit non-effects

Даже после Owner approval AC-404 **не**:

- создаёт бухгалтерскую, tax или bank ledger system;
- доказывает текущий остаток денег;
- доказывает completeness/accuracy of accounting;
- доказывает отсутствие unpaid/unknown obligations;
- создаёт budget или изменяет budget;
- утверждает spend, payment, borrowing, financing, guarantee или investment;
- создаёт customer/vendor/legal obligation;
- создаёт payment/signing/bank authority;
- меняет `ROD-*`, `AM-*`, Position/Assignment/access boundary;
- создаёт new financial transaction namespace;
- создаёт live accounting/bank integration;
- доказывает profitability, runway, unit economics, tax/legal compliance;
- создаёт Product Contract или Platform Capability Arvectum OS;
- создаёт dashboard или automation;
- закрывает AC-405…AC-407.

Actual current values и completeness требуют отдельного current authoritative evidence.

## 24. Completion / approval boundary

AC-404 substantive design считается готовым к Owner approval, если модель:

- сохраняет accounting/bank/source truth вне Company management projection;
- не создаёт parallel ledger;
- отличает cash, budget, plan, approval, incurred obligation и payment;
- использует AC-401…AC-403 identities вместо дублирования;
- даёт minimum decision-relevant cash/commitment view;
- делает freshness/unknown явными;
- сохраняет P0 и exception-driven Owner attention;
- закрепляет POS-005 accountability без создания spend authority;
- защищает sensitive financial data;
- оставляет software/cadence AC-406/AC-407;
- сохраняет Company↔Product↔Arvectum OS boundaries.

Поскольку модель влияет на material financial governance и будущую Owner visibility, `Proposed 0.9.0` не становится binding только потому, что подготовлен AI или прошёл cross-review.

Required gate:

> explicit Owner approval of the exact reviewed proposal.
