# AC-503 — First Governed Workflow: Arvectum OS Reliance / Admission Mapping

Статус: `Approved`
Версия: `1.0.0`
Утверждено: `2026-08-21`
Опубликовано: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-503 — Arvectum OS reliance/admission mapping where applicable`
Milestone: `M5 — First real governed Company operating contour proven`
Workflow: `WF-M5-001 — Customer Feedback → Classified Correction → Verified Candidate → Customer Validation / Acceptance`
First application contour: `PORT-002 — Discount Parser`

## 1. Approval publication

Это canonical Approved publication AC-503 `1.0.0`.

Утверждённая нормативная сущность — exact reviewed proposal:

- path: `docs/operations/FIRST-GOVERNED-WORKFLOW-ARVECTUM-OS-RELIANCE-ADMISSION-MAPPING.md`;
- status/version: `Proposed 0.9.0`;
- immutable proposal blob SHA: `3b7bef8f227d17990ced164aa0de16874bb2ec61`.

Proposal incorporated into this publication by immutable content reference without изменения его reviewed normative substance.

Cross-review:

- `docs/reviews/AC-503-FIRST-GOVERNED-WORKFLOW-ARVECTUM-OS-RELIANCE-CROSS-REVIEW.md`;
- `10 of 10`;
- `Complete / PASS for explicit Owner approval`;
- immutable blob SHA: `67623301fbc2a370433d94952ee3ed6c2f0ef608`.

Owner approval:

- `docs/governance/decisions/DECISION-2026-08-21-AC-503-APPROVAL.md`;
- immutable decision blob SHA: `5197aa78a48d5d4373f6bf24e887bf58607d2d75`;
- exact Owner wording: `AC-503 утверждаю`.

## 2. Approved result

Для первого M5 proof утверждён результат:

**`NO-ADDITIONAL-OS-RELIANCE — no additional Arvectum OS reliance required for the first M5 proof of WF-M5-001`.**

Это означает, что AC-504 может реализовать первый bounded real workflow contour без обязательной записи execution state/history в Arvectum OS и без нового/изменённого OS Product Contract, пока фактическая реализация не пересекает trigger governed OS reliance.

Этот result ограничен первым M5 proof и не является общим решением «Company не использует Arvectum OS».

## 3. Exact Company / Product / OS boundary

Company owns:

- business meaning и governance `WF-M5-001`;
- workflow states `W0…W11`;
- classifications `CL-1…CL-7`;
- Position accountability and Company authority/escalation semantics;
- customer-feedback/scope/acceptance interpretation;
- M5 Owner-burden/business-value evidence requirements.

`arvectum/discount-parser` owns canonical product implementation/status/domain truth, including code, product technical tasks, tests, build/release-candidate evidence and product-specific behavior.

Authorized customer/workstream sources remain authoritative evidence sources for raw customer feedback and customer validation/acceptance/rejection/change request.

Arvectum OS owns its domain-neutral Constitution/RFC/ADR/Product Contract/Platform Capability semantics and governed platform state where actually relied upon.

No source-of-truth or authority transfers merely because one repository references another.

## 4. Current Arvectum OS state used for this decision

AC-503 re-checked `arvectum/arvectum-os` at commit:

`76504766353028540891ac1dfdbf1e5dc331a4af`.

Material current state at the decision point:

- Constitution `1.2.0` — `Ratified`;
- RFC-0001…RFC-0008 — `Accepted 1.0.0`;
- OS roadmap `2.81.0`, current `P9.07`;
- CAP-001…CAP-004 — `Incubating / Provisional`;
- existing `P6.06` Discount Parser Product Contract — `Provisional 0.1.0` within its exact scope;
- no Platform Capability is `Active` merely because prior product validation or M9-alpha exists.

This reference records the checked decision baseline. Future reliance must use then-current OS canonical state.

## 5. Existing P6.06 is not enlarged

Existing `P6.06 — Second Real Product / Workflow Product Contract Boundary` concerns a materially different operation:

`eligible publication candidate → controlled Telegram publication attempt → external-effect evidence/reconstruction`.

WF-M5-001 concerns:

`customer feedback → classification → admitted correction → technical verification → customer validation/acceptance evidence`.

Therefore P6.06 `0.1.0` is neither revoked nor extended by AC-503. Its existing CAP-004 reliance does not become WF-M5-001 reliance by implication.

## 6. No Product Contract or capability transition created

AC-503 does not create:

- new OS Product Contract;
- changed P6.06 Product Contract;
- Stable Product Contract status;
- new Platform Capability;
- CAP-004 dependency for WF-M5-001;
- Platform Capability `Active` transition;
- OS RFC/ADR change;
- hidden cross-repository commitment.

If AC-504 later requires governed OS reliance, the applicable OS governance path must be opened before consequential reliance.

## 7. AC-504 implementation boundary

AC-504 is authorized to implement the smallest reversible OS-neutral mechanics sufficient to operate and reconstruct a real WF-M5-001 case.

Minimum evidence shape should preserve, proportionate to the case:

1. exact workflow identity/version reference;
2. safe case identifier;
3. protected customer feedback source reference and receive time;
4. customer/workstream/product/build context;
5. data classification/sanitization state;
6. current and material prior `W*` states;
7. current `CL-*` classification and attributable Position/Principal act;
8. admitted technical scope and exclusions;
9. product issue/PR/commit/test/build/release-candidate references;
10. known limitations and candidate-ready result;
11. customer-facing handoff evidence where validly authorized/performed;
12. explicit customer validation/acceptance/rework/change evidence;
13. AC-401/402/403 control references when their qualification triggers;
14. Owner intervention, cycle/blocking, rework and reconstruction measurements required by AC-502;
15. explicit unknown/stale/blocked/uncertain states instead of inferred success.

The evidence format must remain OS-neutral and portable enough to admit later platform reliance without rewriting Company business semantics or losing history.

AC-504 must not build a generic workflow engine, event bus, Company-wide database/platform abstraction, CAP-004 substitute or local “mini Arvectum OS” merely to avoid using OS.

## 8. Re-admission triggers

Re-open Company↔OS reliance mapping before consequential use if actual implementation establishes that any of the following becomes necessary:

- shared OS canonical state read/write;
- OS Execution Context / Governed Execution;
- CAP-004 or another Platform Capability as material control dependency;
- Productive Workspace as actual admitted operating surface;
- OS-held Organization/Actor/authorization enforcement;
- shared OS event/provenance history for trustworthy reconciliation;
- stronger governed enforcement for later AM-4/autonomous execution;
- deliberate migration of product/customer evidence into an OS canonical/replica model;
- validated cross-product reuse demonstrating genuine domain-neutral platform demand.

The required sequence remains:

`Company need/evidence → ownership classification → current OS contract/capability check → exact existing admitted boundary OR new Product Contract/capability/RFC/ADR path → explicit approval/admission → only then governed reliance`.

## 9. Authority, security, continuity and sovereignty

Existing AC-202…AC-207 and AC-401…AC-407 remain controlling.

AC-503 creates no Organizational Authority, access grant or autonomous customer effect. Technical access never substitutes for authority. AI/software does not become a Principal. Technical PASS does not create customer-facing approval or acceptance.

Raw customer-confidential material remains protected in its authorized contour by default. `DC-3` reusable secrets stay outside ordinary model context.

The first proof remains replaceable and recoverable through current Company/product/customer sources. If automation/runtime fails, workflow may fall back to the existing human-led correction loop without transferring authority to the failed/replacement executor.

## 10. Non-effects

Approval of AC-503 does not:

- implement AC-504;
- prove AC-505 supervised real operation;
- complete M5;
- create customer obligation, contract, price, SLA, warranty, promise or acceptance;
- create budget/spend/payment/signing authority;
- create Position/Principal/Assignment/access;
- activate AM-3/AM-4;
- approve autonomous external communication/deployment;
- establish Discount Parser production, profitability, legal/compliance or commercial readiness;
- establish OS production/stable/public readiness;
- make OS unnecessary for future Company operations.

## 11. AC-503 completion

`AC-503 — Complete / PASS`.

Next canonical action after publication synchronization:

`AC-504 — Bounded workflow implementation`.

AC-504 must convert the approved design into the smallest actually usable and reconstructable workflow implementation without pre-empting AC-505 empirical proof or AC-506 recovery drill.