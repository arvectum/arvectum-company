# Решение собственника — утверждение AC-502

Статус: `Approved`
Дата: `2026-08-21`
Владелец решения: собственник ООО «Арвектум»
Репозиторий: `arvectum/arvectum-company`
Решение: `AC-502 — Workflow, accountable Position, authority/data/evidence contract`
Milestone: `M5 — First real governed Company operating contour proven`

## 1. Явное решение

После представления exact reviewed proposal AC-502 и прямого Owner approval gate собственник дал явное распоряжение:

> `делай`

В непосредственном контексте pending approval gate это распоряжение означает явное утверждение AC-502 и разрешение выполнить post-approval publication/synchronization mechanics.

Утверждение относится к точной проверенной редакции:

- proposal: `docs/operations/FIRST-GOVERNED-WORKFLOW-AUTHORITY-DATA-EVIDENCE-CONTRACT.md`;
- proposal status/version: `Proposed 0.9.0`;
- immutable proposal blob SHA: `b1df71839422e509cbfa76faec31bf788ca9842d`;
- cross-review: `docs/reviews/AC-502-FIRST-GOVERNED-WORKFLOW-CONTRACT-CROSS-REVIEW.md`;
- cross-review result: `10 of 10`, `Complete / PASS for explicit Owner approval`;
- immutable cross-review blob SHA: `7c457c2b3145b0f2becb3b6e289d9496e02e2d15`.

Эти immutable references фиксируют exact proposal/review set, представленный собственнику перед решением.

## 2. Утверждённый workflow contract

Утверждается Company workflow governance contract для:

`WF-M5-001 — Customer Feedback → Classified Correction → Verified Candidate → Customer Validation / Acceptance`.

Первый application contour:

`PORT-002 — Discount Parser`.

Binding contract включает:

1. bounded entry/exit and state model `W0…W11`;
2. classification taxonomy `CL-1…CL-7`;
3. `POS-002 — Commercial & Customer Lead` как один end-to-end accountable Position;
4. `POS-004 — Engineering & Release Lead` как accountable Position технического сегмента `W4 → W7`;
5. существующие `AM-0/AM-1/AM-2` boundaries без новой Organizational Authority;
6. human-attributable initial `W3 — Classified` через current POS-002 Assignment;
7. AI-led bounded technical execution через POS-004 внутри existing Assignment/access ceilings;
8. отсутствие `AM-3`/`AM-4` activation;
9. separation `Candidate Ready ≠ customer-facing approval ≠ customer acceptance`;
10. explicit customer validation/acceptance evidence; silence не является acceptance без отдельного authoritative rule;
11. `DC-0…DC-3` data handling и minimized engineering packet;
12. запрет на обычное AI/model handling `DC-3` reusable secrets;
13. Company/Product/customer/legal/control-register source-of-truth separation;
14. fail-closed behavior при missing/ambiguous/stale authority, evidence, rights, access или uncertain external effect;
15. continuity/replacement/manual fallback semantics без ложного утверждения, что drills уже выполнены;
16. lightweight M5 evidence/measurement inputs для AC-505/AC-507;
17. отсутствие обязательной Arvectum OS reliance по импликации.

## 3. Authority boundary

AC-502 не создаёт и не расширяет Organizational Authority.

Продолжают действовать:

- AC-202 `ROD-01…ROD-09`;
- AC-203 `AM-0…AM-4`;
- AC-204 Position definitions;
- AC-205 Assignments/executor classes;
- AC-206 access/data boundaries;
- AC-207 continuity/fail-closed baseline;
- AC-401…AC-407 operating-control models.

Особенно:

- POS-002 не получает новый autonomous AI classification/commitment authority;
- POS-004 technical PASS не создаёт customer/commercial authority;
- possession of credentials/access does not create authority;
- customer acceptance remains customer/authoritative-source evidence;
- material scope, commitment, capital, risk, data, sovereignty and Company↔Product↔OS questions continue through applicable `ROD-*`/legal/customer/Product/OS gates.

## 4. Data and source-of-truth boundary

Raw customer-confidential evidence remains in the applicable protected customer/workstream contour by default.

Public Company repository stores only public-safe references/sanitized workflow meaning. `DC-3` credentials/secrets do not enter ordinary AI/model context.

`arvectum/discount-parser` remains canonical for product implementation/status/domain semantics.

Customer messages/validation remain evidence from the customer/source contour.

Company control registers are used only where AC-401/402/403 material qualification requires them; AC-502 does not create a duplicate universal bug/acceptance register.

## 5. Arvectum OS boundary

AC-502 does not create Arvectum OS reliance, Product Contract or platform lifecycle transition.

Exact reliance/admission mapping is the separate next task `AC-503` and may validly conclude that no additional OS reliance is required.

Any actual Company↔OS commitment remains subject to applicable Company authority and OS governance.

## 6. Non-effects

Настоящее решение не:

- создаёт или изменяет customer contract, SLA, price, discount, warranty or promise;
- создаёт budget/spend/payment/signing authority;
- создаёт new Position/Principal/Assignment/access grant;
- активирует `AM-3` или `AM-4`;
- разрешает autonomous consequential customer communication/deployment;
- утверждает full Discount Parser production acceptance/readiness;
- доказывает profitability, market validation, legal compliance или M5 completion;
- создаёт Arvectum OS Product Contract/Stable Product Contract/Active Platform Capability.

## 7. Publication authorization and next action

Решение разрешает:

- публикацию `AC-502 — Approved 1.0.0` с immutable reference на exact reviewed proposal;
- перевод AC-502 в `Complete / PASS`;
- синхронизацию `docs/roadmap/ROADMAP.md`, `docs/CANONICAL-SOURCES.md` и `README.md`;
- перевод current canonical action на:

`AC-503 — Arvectum OS reliance/admission mapping where applicable`.

AC-503 должен проверить реальную необходимость/ценность OS reliance для `WF-M5-001`, current OS canonical state, existing correspondence/admission artifacts и ownership boundary. Он не должен внедрять OS ради dogfooding; `no additional OS reliance required` является допустимым результатом.