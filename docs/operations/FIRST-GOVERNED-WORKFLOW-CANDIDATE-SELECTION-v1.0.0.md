# AC-501 — First Governed Workflow Candidate Selection

Статус: `Approved`
Версия: `1.0.0`
Утверждено: `2026-08-21`
Опубликовано: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-501 — First governed workflow candidate selection`
Milestone: `M5 — First real governed Company operating contour proven`
Решение: `docs/governance/decisions/DECISION-2026-08-21-AC-501-APPROVAL.md`
Cross-review: `docs/reviews/AC-501-FIRST-GOVERNED-WORKFLOW-CANDIDATE-SELECTION-CROSS-REVIEW.md`
Approved proposal: `Proposed 0.9.0`, blob `f6cbebfea1c2e6a56a0fd03c38b68a7211c6bbde`

## 1. Approval publication

Этот документ является канонической Approved publication AC-501 `1.0.0`.

Утверждённое собственником нормативное содержание — полная проверенная редакция:

`docs/operations/FIRST-GOVERNED-WORKFLOW-CANDIDATE-SELECTION.md`

с immutable git blob SHA:

`f6cbebfea1c2e6a56a0fd03c38b68a7211c6bbde`.

Proposal включён в настоящую publication **целиком по immutable content reference**. Публикация не меняет нормативное содержание проверенной редакции.

Явное Owner решение зафиксировано в:

`docs/governance/decisions/DECISION-2026-08-21-AC-501-APPROVAL.md`.

## 2. Approved selection

AC-501 `1.0.0` устанавливает первый выбранный governed Company workflow candidate для M5:

`WF-M5-001 — Customer Feedback → Classified Correction → Verified Candidate → Customer Validation / Acceptance`.

Первый real-operation contour:

`PORT-002 — Discount Parser`.

Выбор основан на aggregate Company/product evidence и критериях business value, Owner burden, repeatability, bounded authority feasibility, access/data readiness, risk/reversibility, evidence/reconstructability, continuity/fallback и ожидаемой operational/economic value относительно control/implementation cost.

## 3. Approved rationale

Binding selection rationale из incorporated proposal включает следующие выводы:

1. `WF-M5-001` уже существует как реальный customer-facing operating pattern, а не только как design hypothesis;
2. current Discount Parser evidence содержит повторяющуюся последовательность customer feedback → interpretation/classification → technical correction → verification → re-delivery/customer validation;
3. workflow непосредственно связан с клиентской ценностью, fulfillment/acceptance evidence и риском unbounded rework;
4. workflow адресует выявленные Owner bottlenecks: customer-context continuity, exception classification, rework routing, acceptance judgment и state reconstruction;
5. bounded technical execution может быть delegated/AI-led в существующем Position/Assignment envelope, не превращая AI в customer/commercial/Owner authority;
6. customer scope/commitment/acceptance и material exceptions остаются отдельными authority gates;
7. workflow достаточно обратим и допускает practical human/manual fallback;
8. workflow создаёт сильный reconstruction path через source customer evidence, classification decision, implementation/test evidence, candidate delivery и validation/acceptance outcome;
9. first M5 proof не требует искусственного создания новой Arvectum OS dependency;
10. выбранный contour позволяет проверить реальную организационную модель Company на business work, а не повторять уже доказанный только governance-publication workflow M4.

## 4. Alternative candidates

AC-501 сравнивал, но не отменяет:

- flagship discovery / AC-108 evidence loop;
- Tender Agent supervised pre-bid contour;
- finance/obligation decision-preparation contour;
- M4 governance proposal/review/approval/publication contour.

Их дальнейшая работа определяется собственными roadmap/authority/evidence основаниями.

Selection `WF-M5-001` означает только первый M5 workflow для последовательного AC-502…AC-507 proof.

## 5. Portfolio and priority boundary

Выбор `PORT-002` не изменяет сам по себе:

- portfolio disposition;
- investment treatment;
- budget;
- Product roadmap;
- permanent Company priority;
- customer obligation scope.

AC-106 hierarchy сохраняется:

`P0 obligations/cash/material risk → P1 flagship evidence + real operating model → P2 revenue/obligation/evidence-linked product/OS work → P3 speculative expansion`.

Действующий portfolio order также сохраняется как decision-attention baseline, а не spending authorization.

Реальный `P0` condition может preempt M5 execution.

## 6. Authority, Assignment and access boundary

AC-501 не создаёт Organizational Authority.

Binding boundaries сохраняются:

- AC-202 `ROD-01…ROD-09`;
- AC-203 `AM-0…AM-4`;
- AC-204 Position meanings;
- AC-205 Assignments/executor realizations;
- AC-206 least-privilege access ceilings;
- AC-207 continuity/replacement/fail-closed semantics;
- AC-401…AC-407 M4 operating-control baseline.

`WF-M5-001` должен быть детализирован в AC-502 так, чтобы technical execution, recommendation, customer communication, acceptance, commitment и approval не смешивались.

## 7. Company / Product / Arvectum OS boundary

Company repository владеет:

- выбором workflow;
- accountable organizational semantics;
- Company authority/evidence/escalation contract;
- M5 proof/continue-change-stop decision.

`arvectum/discount-parser` владеет product implementation/status/domain semantics.

`arvectum/arvectum-os` владеет OS Product Contracts/platform capability/governance semantics.

AC-501 не создаёт OS reliance. Exact Arvectum OS reliance/admission mapping, если оно реально потребуется после определения workflow contract, принадлежит `AC-503`.

## 8. Evidence and review

Cross-review:

- `docs/reviews/AC-501-FIRST-GOVERNED-WORKFLOW-CANDIDATE-SELECTION-CROSS-REVIEW.md`;
- iterations: `10 of maximum 10`;
- result: `Complete / PASS for explicit Owner approval`;
- immutable review blob SHA: `10924469f889d9e97d6a6d11b61d57a70b69e22a`.

Approved proposal:

- `docs/operations/FIRST-GOVERNED-WORKFLOW-CANDIDATE-SELECTION.md`;
- status/version: `Proposed 0.9.0`;
- immutable proposal blob SHA: `f6cbebfea1c2e6a56a0fd03c38b68a7211c6bbde`.

Owner approval:

- `docs/governance/decisions/DECISION-2026-08-21-AC-501-APPROVAL.md` — `Approved`;
- immutable decision blob SHA: `04d42d227c74c779e58d4298ad542e458821837b`;
- explicit Owner wording: `делай`, given directly at the pending AC-501 approval gate.

## 9. Non-effect boundary

AC-501 approval does **not** itself:

- create/modify customer contract, promise, SLA, price, discount or support obligation;
- authorize spend/payment/signing;
- prove Discount Parser production/business/legal/customer readiness;
- create new Position/Principal/Assignment;
- grant credentials/customer-data rights;
- activate `AM-3` or `AM-4`;
- authorize autonomous external customer effects;
- create Product Contract or Arvectum OS lifecycle transition;
- prove M5 complete.

M5 remains open until AC-502…AC-507 produce actual governed-operation evidence.

## 10. Approval result and handoff

`AC-501 — First governed workflow candidate selection` получает статус:

`Complete / PASS`.

Следующее каноническое действие:

`AC-502 — Workflow, accountable Position, authority/data/evidence contract`.

AC-502 должен формализовать `WF-M5-001` без premature implementation: workflow scope/states, accountable Position(s), exact authority modes and exclusions, customer/Company/product data boundary, required source/evidence contract, approval/escalation gates, stale/unknown/failure behavior, continuity/manual fallback и M5 measurement inputs.

Arvectum OS reliance остаётся отдельным AC-503 decision/admission mapping после AC-502.