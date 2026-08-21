# Решение собственника — утверждение AC-501

Статус: `Approved`
Дата: `2026-08-21`
Владелец решения: собственник ООО «Арвектум»
Репозиторий: `arvectum/arvectum-company`
Решение: `AC-501 — First governed workflow candidate selection`
Milestone: `M5 — First real governed Company operating contour proven`

## 1. Явное решение

После представления exact reviewed proposal AC-501 и прямого запроса на Owner approval собственник дал явное распоряжение:

> `делай`

В контексте непосредственно предшествующего approval gate это распоряжение означает явное утверждение AC-501 и разрешение выполнить предусмотренную post-approval publication/synchronization механику.

Утверждение относится к точной проверенной редакции:

- proposal: `docs/operations/FIRST-GOVERNED-WORKFLOW-CANDIDATE-SELECTION.md`;
- proposal status/version: `Proposed 0.9.0`;
- immutable proposal blob SHA: `f6cbebfea1c2e6a56a0fd03c38b68a7211c6bbde`;
- cross-review: `docs/reviews/AC-501-FIRST-GOVERNED-WORKFLOW-CANDIDATE-SELECTION-CROSS-REVIEW.md`;
- cross-review result: `10 of 10`, `Complete / PASS for explicit Owner approval`;
- immutable cross-review blob SHA: `10924469f889d9e97d6a6d11b61d57a70b69e22a`.

Эти immutable references фиксируют exact proposal/review set, представленный собственнику перед решением.

## 2. Утверждённый выбор

Для M5 выбирается один первый governed Company workflow candidate:

`WF-M5-001 — Customer Feedback → Classified Correction → Verified Candidate → Customer Validation / Acceptance`.

Первый реальный контур применения:

`PORT-002 — Discount Parser`.

Selection основан на текущем evidence, а не на формальном portfolio rank или технической зрелости как таковой.

Утверждённая rationale включает:

1. workflow уже проявляется как реальный повторяющийся customer-facing цикл;
2. он напрямую связан с текущей клиентской ценностью, обязательствами по корректировке результата и quality/acceptance evidence;
3. он адресует выявленные AC-104 Owner bottlenecks: customer-context continuity, exception classification, rework routing, acceptance judgment и state reconstruction;
4. техническая часть может быть bounded и largely delegated через существующие Position/Assignment semantics без делегирования material customer/commitment authority;
5. риск ограничим, изменения в основном обратимы, а safe human/manual fallback практически достижим;
6. результат каждой итерации может быть реконструирован через customer evidence, classification, implementation/test evidence, candidate delivery и validation/acceptance outcome;
7. для самого selection не требуется создавать новый Arvectum OS dependency, Product Contract или platform lifecycle claim;
8. текущий Discount Parser evidence содержит серию реальных customer-feedback → correction → re-delivery циклов, а не один изолированный тестовый пример.

## 3. Альтернативы и граница выбора

AC-501 сравнивал и не уничтожает следующие alternative candidate classes:

- flagship discovery / AC-108 evidence loop;
- Tender Agent supervised pre-bid contour;
- finance/obligation decision-preparation contour;
- M4 governance proposal/review/approval/publication contour.

Они остаются действующими или потенциальными workflows в своих scope. Настоящее решение означает только, что `WF-M5-001` является первым workflow для последовательного AC-502…AC-507 M5 proof.

Выбор `PORT-002` как first application contour не меняет portfolio disposition/budget и не создаёт exclusive strategic priority поверх AC-106 `P0…P3` или действующего PORTFOLIO order.

Реальное `P0` обязательство, material risk или cash condition по-прежнему может preempt M5 sequencing.

## 4. Authority boundary

Настоящее решение утверждает durable Company operating-contour selection, но само по себе не создаёт новую Organizational Authority.

Продолжают действовать:

- AC-202 `ROD-01…ROD-09`;
- AC-203 `AM-0…AM-4` semantics;
- AC-204 Position boundaries;
- AC-205 Assignments;
- AC-206 access ceilings;
- AC-207 continuity/fail-closed semantics;
- AC-401…AC-407 M4 control baseline.

Selection не является автоматическим `ROD-04` portfolio reallocation, не является `ROD-03` external commitment и не делегирует такие решения. Если downstream AC-502…AC-507 создаст material portfolio, capital, customer, data, risk или Company↔Product↔OS effect, соответствующий отдельный authority gate обязателен.

## 5. Company / Product / Arvectum OS boundary

Company владеет выбором workflow, accountability/authority/evidence semantics и M5 proof.

`arvectum/discount-parser` остаётся canonical source для product implementation/status/domain semantics.

`arvectum/arvectum-os` остаётся canonical source для OS Product Contracts/platform capabilities/governance. AC-501 не создаёт OS reliance. Exact reliance/admission mapping выполняется только в `AC-503` после того, как `AC-502` определит workflow contract достаточно точно.

## 6. Non-effects

Настоящее решение не:

- утверждает новый customer promise, contract, SLA, price, discount или support term;
- создаёт budget, spend/payment/signing authority;
- изменяет `PORT-002` disposition или portfolio investment treatment;
- утверждает production readiness, profitability, market validation или legal compliance Discount Parser;
- создаёт новый Position, Principal или Assignment;
- выдаёт credential/access/customer-data permission;
- активирует `AM-3` или `AM-4`;
- утверждает конкретную automated customer communication или autonomous external effect;
- создаёт Product Contract, Stable Product Contract или Active Platform Capability Arvectum OS;
- доказывает M5 completion.

M5 остаётся открытым до AC-502…AC-507 и actual supervised real-operation evidence.

## 7. Publication authorization and next action

Решение разрешает:

- публикацию `AC-501 — Approved 1.0.0` с immutable reference на reviewed proposal;
- синхронизацию `docs/roadmap/ROADMAP.md`, `docs/CANONICAL-SOURCES.md` и `README.md`;
- перевод `AC-501` в `Complete / PASS`;
- перевод current canonical action на:

`AC-502 — Workflow, accountable Position, authority/data/evidence contract`.

AC-502 должен формализовать `WF-M5-001` как bounded governed workflow: exact scope/states, accountable Position(s), permitted/excluded authority, customer/Company/product data boundary, evidence contract, approval/escalation gates, safe failure behavior и measurable M5 proof inputs — не предрешая AC-503 OS reliance.