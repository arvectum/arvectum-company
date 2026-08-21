# Решение собственника — утверждение AC-503

Статус: `Approved`
Дата: `2026-08-21`
Владелец решения: собственник ООО «Арвектум»
Репозиторий: `arvectum/arvectum-company`
Решение: `AC-503 — Arvectum OS reliance/admission mapping where applicable`
Milestone: `M5 — First real governed Company operating contour proven`

## 1. Явное решение

После представления exact reviewed proposal AC-503 и прямого Owner approval gate собственник дал явное решение:

> `AC-503 утверждаю`

Это является explicit Owner approval exact reviewed AC-503 proposal и разрешает только post-approval publication/synchronization mechanics, прямо перечисленные в этом решении.

Утверждение относится к точной проверенной редакции:

- proposal: `docs/operations/FIRST-GOVERNED-WORKFLOW-ARVECTUM-OS-RELIANCE-ADMISSION-MAPPING.md`;
- proposal status/version: `Proposed 0.9.0`;
- immutable proposal blob SHA: `3b7bef8f227d17990ced164aa0de16874bb2ec61`;
- cross-review: `docs/reviews/AC-503-FIRST-GOVERNED-WORKFLOW-ARVECTUM-OS-RELIANCE-CROSS-REVIEW.md`;
- cross-review result: `10 of 10`, `Complete / PASS for explicit Owner approval`;
- immutable cross-review blob SHA: `67623301fbc2a370433d94952ee3ed6c2f0ef608`.

Эти immutable references фиксируют exact proposal/review set, представленный собственнику перед утверждением.

## 2. Утверждённый AC-503 result

Для первого M5 proof workflow:

`WF-M5-001 — Customer Feedback → Classified Correction → Verified Candidate → Customer Validation / Acceptance`

в application contour:

`PORT-002 — Discount Parser`

утверждается результат:

**`NO-ADDITIONAL-OS-RELIANCE — no additional Arvectum OS reliance required for the first M5 proof of WF-M5-001`.**

Это означает:

1. первый AC-504 bounded implementation MAY operate through Company/product/customer-owned sources and current authorized tools without making Arvectum OS canonical runtime/history mandatory;
2. новый или изменённый Arvectum OS Product Contract не требуется до первого M5 proof только потому, что workflow принадлежит Company или связан с Discount Parser;
3. существующий `P6.06 — Second Real Product / Workflow Product Contract Boundary` не расширяется и остаётся применим только в своём exact governed Telegram-publication/reconstruction scope;
4. `CAP-004 — Audit / Reconstruction Support` не становится dependency WF-M5-001 по импликации;
5. никакой Platform Capability lifecycle transition этим Company decision не создаётся;
6. никакой Arvectum OS repository change этим решением не считается approved или committed;
7. AC-504 должен сохранить OS-neutral exact references/version/evidence boundary, достаточную для последующей governed migration/admission при возникновении реальной необходимости.

Это решение не является стратегическим отказом от Arvectum OS и не запрещает его последующую фактическую опору. Оно ограничено первым M5 proof выбранного workflow.

## 3. Current OS baseline acknowledged

AC-503 был выполнен после повторной проверки current `arvectum/arvectum-os` state на commit:

`76504766353028540891ac1dfdbf1e5dc331a4af`.

На этой точке были проверены, в применимом scope:

- Constitution `1.2.0` — `Ratified`;
- RFC-0001…RFC-0008 — `Accepted 1.0.0`;
- canonical OS roadmap `2.81.0`, current `P9.07`;
- CAP-001…CAP-004 — `Incubating / Provisional`;
- existing P6.06 Product Contract — `Provisional 0.1.0`;
- absence of an implication that M9-alpha, technical usability or past product validation promotes capabilities/contracts or authorizes broader reliance.

Future Company work must re-check then-current OS state if a re-admission trigger occurs; this decision does not freeze OS at that commit.

## 4. Company / Product / OS ownership boundary

AC-503 preserves the approved AC-002 and AC-502 separation.

Company-owned semantics remain Company-owned, including:

- WF-M5-001 purpose and state model `W0…W11`;
- classification taxonomy `CL-1…CL-7`;
- `POS-002` end-to-end accountability;
- `POS-004` technical-segment accountability;
- Company `ROD-*` / `AM-*` application;
- customer feedback/classification/scope/acceptance/escalation meaning;
- M5 Owner-burden/business-value measurements.

`arvectum/discount-parser` remains canonical for product code, product implementation/status, tests/build/release-candidate evidence and product-domain behavior.

Authorized customer/workstream sources remain authoritative evidence sources for raw customer feedback and explicit customer validation/acceptance/rejection/change request.

Arvectum OS remains canonical for its own domain-neutral architecture, Product Contract semantics, Platform Capability lifecycle and governed platform state where actually relied upon.

No repository acquires another repository's authority merely because it references its artifacts.

## 5. Authority, data and access boundary

AC-503 does not create or broaden Organizational Authority, legal authority, technical authorization or access.

Continue to apply:

- AC-202 `ROD-01…ROD-09`;
- AC-203 `AM-0…AM-4`;
- AC-204 Position definitions;
- AC-205 Assignments/executor classes;
- AC-206 data/tool/credential/access boundaries;
- AC-207 continuity/fail-closed baseline;
- AC-401…AC-407 control models;
- AC-502 workflow contract.

In particular:

- technical access or repository write ability does not create authority;
- AI/software classification/recommendation does not create customer/commercial approval;
- POS-004 technical PASS does not create permission to send/deploy/promise;
- raw customer confidential data must remain in its authorized protected contour unless an approved need allows otherwise;
- `DC-3` reusable secrets do not enter ordinary model context;
- missing/ambiguous/stale authority, rights, evidence, access or external-effect certainty must fail closed/escalate under existing rules.

## 6. Re-admission triggers

Company↔OS reliance mapping must be re-opened before consequential reliance if AC-504/AC-505 establishes that one of the following is actually necessary rather than merely convenient:

1. WF-M5-001 must read/write shared Arvectum OS canonical state;
2. OS Execution Context / Governed Execution is required for a consequential action;
3. CAP-004 or another Platform Capability becomes materially necessary for reconstruction/control quality;
4. Productive Workspace becomes the actual operating surface and requires an admitted Company/product composition boundary;
5. OS-held Organization/Actor/authorization enforcement becomes necessary;
6. shared OS event/provenance history is required for trustworthy reconciliation or uncertainty handling;
7. a later AM-4/autonomous proposal requires stronger governed enforcement;
8. product/customer evidence is intentionally migrated into an OS-admitted canonical/replica model;
9. validated cross-product reuse creates a genuine domain-neutral platform need.

When such trigger exists, the Company must use the applicable Product Contract/capability/RFC/ADR/governance path in `arvectum/arvectum-os` before reliance. Hidden coupling is prohibited.

## 7. Non-effects

Настоящее решение не:

- реализует AC-504;
- доказывает supervised real-operation proof AC-505;
- закрывает M5;
- создаёт customer contract, SLA, price, discount, warranty, promise or acceptance;
- создаёт budget/spend/payment/signing authority;
- создаёт new Position/Principal/Assignment/access grant;
- активирует `AM-3` или `AM-4`;
- разрешает autonomous consequential customer communication/deployment;
- утверждает Discount Parser production/commercial/legal readiness;
- переводит любой Arvectum OS Product Contract в `Stable`;
- переводит любой Platform Capability в `Active`;
- изменяет P6.06 scope;
- утверждает новый OS Product Contract, RFC, ADR, capability admission или cross-repository implementation commitment;
- означает, что Arvectum OS не будет использоваться Company в будущем.

## 8. Publication authorization and next action

Решение разрешает:

- публикацию `AC-503 — Approved 1.0.0` с immutable reference на exact reviewed proposal;
- перевод AC-503 в `Complete / PASS`;
- синхронизацию `docs/roadmap/ROADMAP.md`, `docs/CANONICAL-SOURCES.md` и `README.md`;
- перевод current canonical action на:

`AC-504 — Bounded workflow implementation`.

AC-504 должен реализовать минимально достаточную, обратимую, OS-neutral механику WF-M5-001 для реальной работы и evidence capture. Он не должен строить generic workflow engine, event bus, Company-wide platform abstraction или локальный substitute Arvectum OS без доказанной необходимости.