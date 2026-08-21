# AC-303 — Границы инвестиций, затрат и рисков; критерии продолжить / изменить / ограничить / предложить остановку

Статус: `Proposed`
Версия: `0.9.0`
Дата: `2026-08-21`
Владелец документа: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-303 — Investment, cost and risk boundaries; continue/change/stop criteria`
Максимум итераций перекрёстной проверки: `10`

## 1. Цель и точная граница AC-303

AC-303 определяет Company-level investment envelope для каждого действующего portfolio node `PORT-001…PORT-007` и единый evidence-based способ подготовить решение `continue / change / contain / stop-retire candidate`.

Задача отвечает на вопрос:

> В каких пределах Компания может продолжать уже допущенную работу по каждому portfolio node, какие виды затрат, Owner attention и downside должны становиться видимыми, и при каких evidence/review triggers работа должна быть пересмотрена, ограничена или вынесена собственнику как material continue/change/stop/investment decision?

AC-303 **не**:

- создаёт или утверждает денежный бюджет;
- устанавливает выдуманные рублёвые, часовые, процентные или иные числовые лимиты при отсутствии подтверждённых данных;
- разрешает конкретный расход, договор, найм, подписку, customer commitment, production deployment или доступ;
- меняет AC-301 identity/disposition baseline или AC-302 accountable-Position mapping молча;
- выполняет AC-304 classification `standalone product / reference implementation / module candidate / Arvectum OS capability candidate`;
- выполняет AC-305 reconciliation межпродуктовых зависимостей и Product Contracts Arvectum OS;
- выполняет AC-306 относительную приоритизацию портфеля по капиталу, экономике и Owner attention;
- переносит product implementation truth из product repositories в Company repository;
- доказывает юридические/IP/data rights;
- превращает technical `PASS`, активность репозитория, sunk cost или AI recommendation в business/investment approval.

## 2. Каноническая основа

AC-303 опирается на:

- `docs/constitution/COMPANY-CONSTITUTION.md` — business-first, Owner authority, proportional governance, technology sovereignty;
- `docs/governance/RESERVED-OWNER-DECISIONS-v1.0.0.md` — `ROD-01…ROD-09`;
- `docs/governance/DELEGATED-POSITION-AUTHORITY-MODEL-v1.0.0.md` — deny-by-default и `AM-0…AM-4`;
- `docs/organization/INITIAL-POSITION-REGISTRY-v1.0.0.md` — `POS-001…POS-006`;
- `docs/portfolio/AC-301-PORTFOLIO-IDENTITY-BOUNDARY-OWNERSHIP-RECONCILIATION-v1.0.0.md` — утверждённые `PORT-*` identities и dispositions;
- `docs/portfolio/AC-302-PORTFOLIO-ACCOUNTABLE-POSITION-MAPPING-v1.0.0.md` — primary Company-level accountability `PORT-* → POS-003`;
- `docs/portfolio/PORTFOLIO.md` — текущая каноническая карта портфеля;
- `docs/roadmap/ROADMAP.md` — AC-303 как текущий канонический Phase 3 step.

Product-specific implementation/status evidence остаётся product-owned. Для AC-303 использован следующий bounded snapshot текущих product sources; blob reference фиксирует именно прочитанную редакцию и не превращает Company artifact в product source of truth:

| Portfolio ID | Product source | Reviewed blob |
|---|---|---|
| `PORT-001` | `arvectum/tender-agent/STATUS.md` | `8f9c3cfdb8e893d46d0898e252ecb2f86e5c5f2b` |
| `PORT-002` | `arvectum/discount-parser/README.md` | `7580d8112918c0be3381ff0073b7a481fa388434` |
| `PORT-003` | `arvectum/proxy-launcher/README.md` | `5113d6d768507be9f91a35436c8cc4eea00e7c99` |
| `PORT-004` | `arvectum/creative-test-agent/README.md` | `faf29045cbe57f46579743ca3d8b87995dc0e808` |
| `PORT-005` | `arvectum/tender-app/README.md` | `5065e0e1673da12b60128f7972efa6286938e034` |
| `PORT-006` | `arvectum/doors_parser/README.md` | `69c6d037f5812d9a1ae225c2b4ab46f6d8713f53` |
| `PORT-007` | `arvectum/data-platform/README.md` | `6d6a0afe1f4437c383626bad42355077d76d986e` |

Если после этого snapshot product source изменился materially, POS-003 MUST refresh decision-relevant evidence before consequential reliance.

## 3. Главный принцип: investment envelope, а не фиктивный бюджет

До появления подтверждённых финансовых и operating данных AC-303 использует **границы по типам воздействия и decision triggers**, а не произвольные денежные пороги.

`Unknown` означает `evidence required`, а не `zero`.

Для каждого node должны быть видимы, если применимы:

1. **Direct cash exposure** — разовые покупки, подрядчики, hardware, сертификаты, регистрационные/юридические расходы, иные прямые денежные траты.
2. **Recurring cost** — hosting/VPS, подписки, лицензии, домены, внешние API/сервисы, support tooling, постоянно работающая инфраструктура.
3. **Engineering / delivery effort** — разработка, QA, packaging, migration, customer-specific adaptation, release/support work.
4. **Owner attention exposure** — необходимость регулярного ручного решения, контроля, debugging, customer handling или approval, создающая bottleneck.
5. **Customer / obligation exposure** — SLA, support, срок поставки, исправления, acceptance, обещания, штрафной/репутационный downside.
6. **Security / data / privacy exposure** — credentials, real customer data, production access, cross-customer reuse, leakage, privileged execution.
7. **Legal / IP / compliance exposure** — исключительные права, лицензии, signing, реестры, договорные ограничения, обязательная правовая форма действия.
8. **Dependency / sovereignty exposure** — критические внешние сервисы, юрисдикция, доступность из России, vendor lock-in, отсутствие self-host/offline/replacement path.
9. **Operational continuity exposure** — single machine/runtime/operator, recovery, backup, update/rollback, source fragility, external-site drift.
10. **Opportunity cost** — вытеснение более ценной работы, даже если прямой cash spend мал.

Фактические суммы, часы, recurring invoices и commitments SHOULD записываться из надёжного evidence, когда они появляются. До этого нельзя подменять неизвестность оценкой «почти бесплатно».

## 4. Семантика portfolio decision states

### `continue within envelope`

Существующий disposition может продолжаться **только в уже допущенном bounded scope** и при наличии достаточного evidence для следующего шага. Это не вечное финансирование и не разрешение на material expansion.

### `change / re-scope`

Evidence показывает, что цель может оставаться ценной, но текущая форма, workflow, architecture, delivery model, dependency или cost structure требует изменения до дальнейшего material investment.

### `contain`

Growth/scope expansion прекращаются. Разрешённый предмет — сохранение необходимого состояния/evidence, исполнение уже существующих обязательств в законном/утверждённом scope, bounded maintenance, safety/security containment и подготовка reuse/retire decision.

### `stop / retire candidate`

Это **proposal for decision**, а не автоматическое удаление repository, данных, сервиса, продукта, contractual obligation или organizational asset. Material stop/retire/merge/abandonment попадает в применимый Owner/corporate/legal gate, включая `ROD-04` и при необходимости другие `ROD-*`.

### `clarify before investment`

Допустимы discovery и evidence-building. Material implementation, production data, recurring infrastructure или внешний commitment до clarification/admission decision не должны возникать по инерции.

## 5. Общий evidence packet перед material continue/change/stop/investment decision

`POS-003 — Portfolio & Product Lead` отвечает за сбор decision-ready packet, но не подменяет functional Positions.

Минимальный packet:

1. **Identity/current state** — `PORT-*`, действующий disposition, product canonical source и его точная current/version reference.
2. **Business outcome** — какая клиентская/внутренняя проблема решается и какой следующий проверяемый outcome нужен.
3. **Demand / use evidence** — customer/pilot/use evidence, если применимо; отсутствие evidence фиксируется явно.
4. **Obligations** — уже существующие customer/legal/support commitments и consequences of non-performance.
5. **Cost map** — известные direct/recurring costs, engineering/delivery effort, Owner attention, unknowns и источник каждого materially relied-upon факта.
6. **Economics** — revenue/cash/unit-economics evidence там, где оно реально существует; отсутствие цифр не заменяется предположением.
7. **Risk map** — security/data/legal/IP/reputational/operational/dependency/sovereignty downside, reversibility и time-to-recover.
8. **Alternatives** — keep current, change, contain, stop/retire candidate, buy/use external solution, reuse existing Company/Product/OS capability where such option is already evidenced.
9. **Opportunity cost** — что не будет сделано или потребует Owner attention из-за продолжения этого node.
10. **Recommendation** — один recommended disposition, альтернативы, missing evidence, next review trigger и applicable authority gate.

Functional evidence routing:

- `POS-002` — customer/demand/commitment/delivery evidence;
- `POS-004` — engineering/release/technical feasibility/maintenance evidence;
- `POS-005` — cash, recurring cost, economics, obligations and financial exposure evidence;
- `POS-006` — security, data, risk, critical dependency, sovereignty and continuity evidence;
- `POS-001` — cross-Position integration, decision routing and Company-level escalation;
- `POS-003` — node-level synthesis and stewardship.

## 6. Универсальные review triggers

Независимо от node, decision MUST be refreshed or escalated before/when появляется одно из следующего:

- новый material cash commitment или recurring spend;
- новый contractor/hire/vendor commitment;
- обязательство перед новым customer или существенное расширение существующего promise/SLA/support scope;
- production deployment или внешняя mutation/commitment, которой раньше не было;
- обработка нового класса real/sensitive/customer data;
- security/privacy/data/rights exception;
- новая critical dependency либо зависимость без приемлемого replacement path;
- technology-sovereignty exception;
- material cross-repository, Company↔Product или Company/Product↔Arvectum OS commitment;
- изменение product identity, target market, business model или material product scope;
- переход от controlled pilot/experiment к production/scale;
- заметно повторяющийся Owner/manual intervention, превращающий node в bottleneck;
- существенное расхождение между ожидаемой и фактической support/maintenance/engineering нагрузкой;
- отсутствие ожидаемого customer/use/economic evidence к согласованному milestone/gate;
- incident, loss, data leakage, material defect или source/dependency failure, меняющий downside;
- появление более дешёвой/безопасной/заменяемой альтернативы, делающей текущую траекторию экономически сомнительной.

Срабатывание trigger не означает автоматический `stop`; оно означает, что прежняя envelope больше не должна считаться достаточной без review.

## 7. Node-specific investment envelopes

### 7.1 `PORT-001 — Arvectum Tender Agent`

Текущий AC-301 disposition: `continue`.

Product evidence snapshot: `R0_CLOSED_FUNCTIONALLY`; следующий заявленный product milestone ограничен extraction quality, analysis quality, report structure и evidence coverage; массовый внешний pilot текущим product status не разрешён.

**Допустимый Company envelope сейчас:**

- продолжать bounded quality/evidence/product-readiness work, уже находящееся в approved/assigned scope;
- готовить controlled pilot/business-quality evidence без превращения preparation в customer commitment;
- сохранять human review и manual external-action boundary, пока отдельный product/governance decision не утверждает иное;
- не считать временную публичную инфраструктуру или technical functional closure доказательством production reliability/business readiness.

**Material review/escalation triggers:** массовый внешний pilot; production/public reliability commitment; новый recurring infra/service spend; binding customer promise; автоматизированные внешние procurement actions; material real-customer data expansion; новая critical external dependency; material OS/Product Contract/cross-repo change.

**Continue evidence:** измеримая полезность/качество анализа и отчёта; evidence controlled-pilot demand/use; приемлемая operator/Owner нагрузка; реконструируемая reliability/continuity; отсутствие unresolved material security/data/sovereignty gap.

**Change/contain evidence:** повторяющиеся quality/reliability failures, manual burden выше разумной product value, неподтверждённая economics при росте затрат, необходимость material external commitment только для продолжения, неуправляемая dependency/sovereignty проблема.

**Stop/retire candidate evidence:** после bounded validation отсутствует credible customer/use/economic path и отсутствует достаточная reusable/strategic value, либо material downside не имеет пропорционального mitigation path.

### 7.2 `PORT-002 — Discount Parser`

Текущий AC-301 disposition: `continue`.

Product evidence snapshot: MVP functional/delivery contour реализован; live acceptance зависит от target machine, реального доступа к источникам и Telegram credentials; CI green не заявлен.

**Допустимый Company envelope сейчас:**

- завершать bounded client acceptance/correction/delivery work в существующем scope;
- поддерживать source-specific adapters и installation/runtime path, когда это необходимо для принятого delivery scope;
- не финансировать generic scraping platform/module rewrite только потому, что несколько parser projects существуют;
- не превращать local client solution в 24/7 managed service/SLA по импликации.

**Material review/escalation triggers:** новый customer/paid productization contour; постоянный hosted/VPS operation; новый внешний autopublishing commitment; credential/data exposure; существенное расширение числа/класса источников; повторяющийся source-drift maintenance; generic engine/platformization proposal.

**Continue evidence:** client acceptance/use evidence; стабильность extraction/normalization на declared sources; support effort остаётся bounded; release/install path воспроизводим; recurring operating cost и credential risk понятны.

**Change/contain evidence:** поддержка превращается в непрерывную ручную подстройку, source-specific complexity разрушает unit economics/maintainability, delivery acceptance остаётся недостижимой, либо 24/7/credential/support burden требует иной product/service model.

**Stop/retire candidate evidence:** нет оставшегося customer obligation/value, нет validated reusable value и дальнейшая поддержка создаёт несоразмерную recurring/Owner burden.

### 7.3 `PORT-003 — Arvectum Proxy Launcher`

Текущий AC-301 disposition: `continue`.

Product evidence snapshot: Windows `0.2.3` — verified productization track; production embedded code signing ещё не активирован; macOS/Linux не должны представляться production-ready.

**Допустимый Company envelope сейчас:**

- продолжать Windows productization, release evidence, Russia-first signing path, security/supportability и IP/dependency evidence в уже approved scope;
- не считать unsigned branding/metadata цифровой подписью;
- не расширять macOS/Linux production commitment только ради feature parity до отдельного evidence/priority decision;
- не принимать critical foreign signing/distribution dependency как неизбежную без sovereignty review.

**Material review/escalation triggers:** новый production signing/certificate/hardware/service spend; государственный/реестровый/legal commitment; customer-facing production release/SLA; новый privileged/network control; macOS/Linux productization; critical vendor dependency; material security exception.

**Continue evidence:** проверяемый Windows release path; customer/use evidence; supportability/rollback/recovery; acceptable signing/distribution path для первичного рынка; dependency replaceability; отсутствие material network/security risk.

**Change/contain evidence:** signing/distribution/support model блокирует practical delivery, security/privilege risk требует redesign, cross-platform expansion резко увеличивает support cost без demand evidence, critical dependency становится неприемлемой.

**Stop/retire candidate evidence:** нет validated market/internal use и нет достаточно ценной reusable capability, а безопасная поддержка/distribution требует несоразмерного постоянного ресурса.

### 7.4 `PORT-004 — Creative Test Agent`

Текущий AC-301 disposition: `continue`.

Product evidence snapshot: local-first closed-loop product с demo/pilot pack и server deployment foundation; cloud LLM disabled by default.

**Допустимый Company envelope сейчас:**

- продолжать controlled-pilot quality/usefulness evidence, local model/closed-loop validation и bounded client-pilot packaging;
- не превращать server foundation в production/SaaS readiness по импликации;
- не разрешать cloud-model/customer-data/cross-client learning expansion без отдельного data/rights/risk decision.

**Material review/escalation triggers:** real client data; external production hosting; cloud LLM/VLM/provider; customer SLA/support commitment; cross-client knowledge reuse; new recurring compute/hosting cost; broad SaaS productization.

**Continue evidence:** pilot/customer usefulness; acceptable creative-analysis quality; local closed-loop controls; bounded compute/support effort; clear customer data handling and no unresolved material rights/security issue.

**Change/contain evidence:** model/output quality не поддерживает customer value, manual review/support cost несоразмерен, local compute/runtime fragility блокирует delivery, либо scale требует существенно иной security/operations model.

**Stop/retire candidate evidence:** controlled pilots не подтверждают устойчивый customer/use/economic path и отдельная reusable value не оправдывает дальнейшую поддержку.

### 7.5 `PORT-005 — Tender Small-Volume Calculator`

Текущий AC-301 disposition: `contain`.

Product evidence snapshot: локальный procurement MVP с demo/production paths, real-source/price-search limitations и manual fallback; AC-301 отдельно запретил автоматическое объединение с Tender Agent.

**Допустимый Company envelope сейчас:**

- сохранять работоспособный contained state, documentation/evidence и только необходимое bounded maintenance;
- исполнять фактически существующее обязательство, если оно будет подтверждено applicable source;
- готовить evidence для дальнейшего reuse/merge/retire question без фактического merge;
- не инвестировать в новый production rollout, новые источники, масштабирование или самостоятельную productization траекторию без Owner gate.

**Material review/escalation triggers:** новый customer/pilot; production deployment; существенная новая feature/source/integration; предложение объединить с PORT-001; material OS/dependency coupling; recurring infra/support commitment.

**Retain-contained evidence:** существует конкретная preservation/reuse/obligation value, превосходящая bounded cost хранения/поддержки.

**Change evidence:** полезная функция требует иного ownership/boundary или дальнейшее существование как отдельного node создаёт явное duplication burden — classification/merge implication при этом остаётся предметом AC-304/последующего Owner decision.

**Stop/retire candidate evidence:** нет действующих obligations, нет distinct customer/use case и не подтверждена reusable value, после чего retirement всё равно должен сохранить required history/data/rights/rollback obligations.

### 7.6 `PORT-006 — Doors Parser`

Текущий AC-301 disposition: `contain`.

Product evidence snapshot: завершённый client-delivery parser с зафиксированным результатом/QA и известными manual-review limitations.

**Допустимый Company envelope сейчас:**

- сохранять delivery evidence/history и исполнять только реально существующие bounded correction/support obligations;
- выполнять security/safety preservation и минимальное maintenance, если оно необходимо для обязательства или сохранения организационного актива;
- не расширять количество сайтов, функциональность или generic-parser productization без нового business evidence;
- не объявлять его автоматически частью Discount Parser/Data Platform/generic parsing module.

**Material review/escalation triggers:** новый customer; новая крупная source scope; существенная переработка движка; длительный support/maintenance contour; generic parser/module initiative; изменение data/IP/source rights assumptions.

**Retain-contained evidence:** есть непогашенное обязательство, доказанная повторная полезность или недорогая preservation value.

**Change evidence:** repeated reuse подтверждает отдельную reusable hypothesis, но classification остаётся AC-304, а investment — отдельным Owner decision.

**Stop/retire candidate evidence:** obligations закрыты, reuse не подтверждён, а дальнейшее поддержание создаёт лишнюю support/attention нагрузку; retirement не должен уничтожать required delivery evidence/history.

### 7.7 `PORT-007 — Data Platform`

Текущий AC-301 disposition: `clarify`.

Product evidence snapshot: canonical repository пока содержит только минимальное описание `Data Platform`; business problem, consumers, product/module/platform boundary и economics не определены.

**Допустимый Company envelope сейчас:**

- только clarification/discovery: конкретная business problem, consumers, required data flows, strategic/economic hypothesis, boundary и measurable evidence plan;
- архитектурное сравнение с уже существующими product-owned capabilities и Arvectum OS только на уровне подготовки вопроса; AC-305 остаётся отдельным formal reconciliation gate;
- не создавать production data lake/platform, recurring infrastructure, customer data ingestion или broad shared schemas до admission decision;
- не выводить platform status из имени repository.

**Material review/escalation triggers:** начало существенной implementation; data ingestion; database/warehouse/vector/search infrastructure; recurring cloud/hosting spend; cross-product data contract; customer data centralization; новый OS/platform boundary; critical dependency.

**Continue-clarify evidence:** выявлен конкретный consumer/problem и минимальный bounded use case; есть credible economic/operational benefit hypothesis; ясно, почему это не дублирование product logic или Arvectum OS; определены data/rights/security/sovereignty constraints.

**Change/contain evidence:** hypothesis распадается на product-local задачи, пересекается с существующей OS responsibility или требует слишком широкого speculative platform build до наличия consumers.

**Stop/retire candidate evidence:** конкретный consumer/problem/economic hypothesis не появляется после bounded clarification либо value можно получить существенно проще существующим product/OS/external solution без создания отдельной инициативы.

## 8. Reserved Owner Decisions и authority boundary

AC-303 особенно близок к следующим hard gates:

- `ROD-02 — Capital allocation and material financial exposure`;
- `ROD-04 — Major portfolio, initiative and investment decisions`;
- `ROD-06 — Risk appetite and material exception acceptance`;
- `ROD-08 — Core IP, critical dependency and technology-sovereignty exceptions`;
- `ROD-09 — Material Company↔Product↔Arvectum OS boundary and cross-repository commitments`.

Также по фактам могут применяться:

- `ROD-01` — strategy/business-model identity;
- `ROD-03` — material external/customer commitments;
- `ROD-07` — customer/data sovereignty/reuse/disclosure exception;
- `ROD-05` — если investment decision требует material organizational/authority change.

Поэтому AC-303 устанавливает **decision preparation and bounded execution envelope**, а не делегирует material investment authority POS-003 или AI.

`POS-003` может в approved `AM-0/1/2` scope собирать evidence, вести bounded stewardship, синхронизировать уже утверждённые states и готовить recommendation. Финальное material capital/portfolio/risk/boundary решение остаётся у применимой authority.

## 9. Technical PASS, repository activity, sunk cost и AI recommendation

Следующие факты **не являются достаточными continue/invest evidence сами по себе**:

- tests/CI/build/release PASS;
- большое количество кода, commits или уже затраченного времени;
- наличие работающего demo;
- наличие repository/branch/package;
- субъективная техническая привлекательность;
- утверждение AI, что продукт перспективен;
- факт, что на node уже потрачены деньги/время (`sunk cost`).

Они могут быть входным evidence, но business decision должен учитывать future value, future cost, obligations, downside, reversibility, opportunity cost и Owner workload.

## 10. Decision rule

Для каждого material gate применяется последовательность:

```text
Current PORT identity/disposition
→ current product source evidence
→ obligations/customer/use evidence
→ cost + Owner-attention evidence
→ risk/data/legal/dependency/sovereignty evidence
→ alternatives + opportunity cost
→ recommended continue/change/contain/stop-retire candidate
→ applicable authority gate
→ explicit decision
→ bounded execution
→ new evidence / review trigger
```

Если materially required evidence отсутствует, правильный результат — `evidence incomplete / do not expand`, а не оптимистичное продолжение по умолчанию.

## 11. Reconciliation register

| Вопрос | AC-303 результат | Дальнейший owner/source |
|---|---|---|
| сколько конкретно рублей/часов выделить каждому node | не устанавливается без evidence/approval | конкретный budget/capital decision + AC-306 priority context |
| какой node важнее остальных | не ранжируется | `AC-306` |
| является ли node продуктом, reference implementation или module/OS candidate | не классифицируется | `AC-304` |
| какие cross-product/OS dependencies должны быть изменены | не изменяются | `AC-305` + applicable product/OS governance |
| кто primary accountable за node | сохраняется `POS-003` | Approved AC-302 |
| кто даёт finance/risk/customer/technical evidence | сохраняется functional Position split | Approved M2 model |
| может ли AI одобрить material investment | нет | AC-202/203 + Owner/legal authority |
| можно ли автоматически удалить contained/stopped node | нет | explicit retirement/data/history/obligation decision |

## 12. Acceptance criteria AC-303

AC-303 готов к Owner approval только если подтверждено всё следующее:

- для всех `PORT-001…PORT-007` есть bounded investment treatment;
- cost categories включают cash, recurring, engineering/delivery, Owner attention и opportunity cost;
- risk categories включают customer, security/data, legal/IP, dependency/sovereignty и continuity;
- неизвестные суммы не превращены в нули или invented thresholds;
- existing AC-301 dispositions сохранены;
- existing AC-302 `PORT-* → POS-003` mapping сохранён;
- functional Positions не поглощены POS-003;
- `ROD-*` hard gates сохранены;
- `continue` не означает automatic funding/scope growth;
- `contain` не означает silent deletion или refusal of existing obligations;
- `clarify` не означает implementation/platform admission;
- technical PASS/activity/sunk cost не равны business value;
- stop/retire остаётся proposal до competent decision;
- product source remains canonical for product implementation/status;
- legal/IP/customer/OS authority не присваивается Company artifact;
- AC-304/305/306 scopes не выполнены заранее;
- next canonical action после approval остаётся `AC-304`.

## 13. Approval boundary

До явного Owner approval этот документ остаётся `Proposed 0.9.0`.

Его наличие в `main` не создаёт бюджет, не меняет portfolio disposition, не санкционирует расход или stop/retire, не меняет Product/OS/customer state и не обновляет канонический `PORTFOLIO.md`/`ROADMAP.md` как будто AC-303 уже утверждён.
