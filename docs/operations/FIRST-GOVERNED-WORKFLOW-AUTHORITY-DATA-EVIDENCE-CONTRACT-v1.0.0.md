# AC-502 — First Governed Workflow: Position, Authority, Data and Evidence Contract

Статус: `Approved`
Версия: `1.0.0`
Утверждено: `2026-08-21`
Опубликовано: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-502 — Workflow, accountable Position, authority/data/evidence contract`
Milestone: `M5 — First real governed Company operating contour proven`
Selected workflow: `WF-M5-001 — Customer Feedback → Classified Correction → Verified Candidate → Customer Validation / Acceptance`
First application contour: `PORT-002 — Discount Parser`
Решение: `docs/governance/decisions/DECISION-2026-08-21-AC-502-APPROVAL.md`
Cross-review: `docs/reviews/AC-502-FIRST-GOVERNED-WORKFLOW-CONTRACT-CROSS-REVIEW.md`
Approved proposal: `Proposed 0.9.0`, blob `b1df71839422e509cbfa76faec31bf788ca9842d`

## 1. Approval publication

Этот документ является канонической Approved publication AC-502 `1.0.0`.

Утверждённое собственником нормативное содержание — полная проверенная редакция:

`docs/operations/FIRST-GOVERNED-WORKFLOW-AUTHORITY-DATA-EVIDENCE-CONTRACT.md`

с immutable git blob SHA:

`b1df71839422e509cbfa76faec31bf788ca9842d`.

Proposal включён в эту publication **целиком по immutable content reference**. Настоящая publication не меняет нормативное содержание проверенной редакции.

Owner approval зафиксирован в:

`docs/governance/decisions/DECISION-2026-08-21-AC-502-APPROVAL.md`, immutable blob `08db32414f9f19c99b281d936a5eccaa0f456ede`.

## 2. Approved workflow contract

AC-502 `1.0.0` устанавливает binding Company workflow governance contract для `WF-M5-001` в первом real-operation contour `PORT-002 — Discount Parser`.

Утверждены:

- bounded workflow entry/exit and states `W0…W11`;
- classification taxonomy `CL-1…CL-7`;
- `POS-002 — Commercial & Customer Lead` как единственный end-to-end accountable Position;
- `POS-004 — Engineering & Release Lead` как accountable Position технического сегмента `W4 → W7`;
- explicit authority, data, access, evidence, escalation, failure, continuity and measurement boundaries;
- separation customer meaning/acceptance from technical completion;
- source-of-truth separation между Company, Product, customer/legal contours и M4 control registers.

## 3. Authority and Assignment boundary

Workflow использует только already-approved authority/Assignment semantics.

Initial operating rule:

- current human POS-002 Assignment performs attributable routine `W3 — Classified` decisions within admitted `AM-2` scope;
- AI-led POS-004 may perform admitted `AM-0/AM-1/AM-2` technical work after `W4` admission;
- `W7 — Candidate Ready` is a technical handoff only;
- `AM-3` and `AM-4` are not activated;
- no AI/software executor acquires customer/commercial/Owner authority by workflow participation or technical access.

All applicable `ROD-01…ROD-09`, legal/corporate/customer/Product/OS gates remain unchanged.

## 4. Customer acceptance boundary

The workflow preserves:

`technical PASS ≠ release/customer approval ≠ customer acceptance`.

A correction case closes as accepted only when applicable explicit customer/authorized-source validation/acceptance evidence exists.

Customer silence does not constitute acceptance unless a stronger authoritative source explicitly defines that rule for the case.

A successful correction case does not by itself prove full Discount Parser production acceptance/readiness.

## 5. Data and access boundary

AC-502 applies approved AC-206 `DC-0…DC-3` and least-privilege/access ceilings.

Binding expectations include:

- raw customer `DC-2` remains in the appropriate protected contour by default;
- public Company artifacts store sanitized references/meaning rather than confidential payload;
- POS-004 receives a minimized engineering packet sufficient for technical work;
- reusable `DC-3` secrets do not enter ordinary model context;
- need for broader confidential access becomes an explicit rights/access gate;
- AC-502 itself provisions no credentials/accounts/access.

## 6. Evidence and source-of-truth boundary

The workflow does not create a universal duplicate bug/acceptance register.

- product issues/code/tests/build/release truth remains in `arvectum/discount-parser`;
- raw customer feedback/validation remains in its authorized customer/workstream source contour;
- Company workflow state represents bounded operating interpretation and public-safe references;
- `WORK/OBL/DEC/APR/ESC/RSK/EXC/INC` controls are used only where existing AC-401/402/403 material qualification gates require them.

`technical task closed ≠ Company/customer obligation satisfied`.

## 7. Failure, continuity and fallback

Approved contract requires fail-closed behavior for missing/ambiguous/stale authority, evidence, rights, access or uncertain consequential external effect.

POS-002/Owner unavailability does not transfer customer/Owner authority to AI.

POS-004 runtime replacement may preserve Position meaning only within valid Assignment/access boundaries; if no eligible executor exists, technical work pauses or is explicitly reassigned.

Actual incident/recovery/fallback drill remains empirical work for AC-506 and is not claimed by AC-502 approval.

## 8. Arvectum OS boundary

AC-502 creates no Arvectum OS reliance, Product Contract or platform lifecycle transition.

Exact reliance/admission mapping is the next action `AC-503`.

`AC-503` may validly conclude `no additional OS reliance required`; the Company must not force OS integration merely for dogfooding completeness.

## 9. Review and approval evidence

Cross-review:

- `docs/reviews/AC-502-FIRST-GOVERNED-WORKFLOW-CONTRACT-CROSS-REVIEW.md`;
- iterations: `10 of maximum 10`;
- result: `Complete / PASS for explicit Owner approval`;
- immutable review blob SHA: `7c457c2b3145b0f2becb3b6e289d9496e02e2d15`.

Approved proposal:

- `docs/operations/FIRST-GOVERNED-WORKFLOW-AUTHORITY-DATA-EVIDENCE-CONTRACT.md`;
- status/version: `Proposed 0.9.0`;
- immutable proposal blob SHA: `b1df71839422e509cbfa76faec31bf788ca9842d`.

Owner decision:

- `docs/governance/decisions/DECISION-2026-08-21-AC-502-APPROVAL.md` — `Approved`;
- immutable decision blob SHA: `08db32414f9f19c99b281d936a5eccaa0f456ede`;
- explicit Owner wording at the pending approval gate: `делай`.

## 10. Non-effects

AC-502 approval does **not** itself:

- create/change a customer contract, promise, SLA, price, discount or warranty;
- create budget/spend/payment/signing authority;
- create a new Position/Principal/Assignment/access grant;
- activate `AM-3`/`AM-4`;
- authorize autonomous consequential customer communication or production deployment;
- prove full product production/business/legal/customer readiness;
- prove profitability, market validation or M5 completion;
- create an Arvectum OS Product Contract/Stable Product Contract/Active Platform Capability.

## 11. Approval result and handoff

`AC-502 — Workflow, accountable Position, authority/data/evidence contract` получает статус:

`Complete / PASS`.

Следующее каноническое действие:

`AC-503 — Arvectum OS reliance/admission mapping where applicable`.

AC-503 должен проверить current canonical Arvectum OS state и установить, требует ли `WF-M5-001` реального OS reliance/admission для AC-504/AC-505; если нет, это должно быть зафиксировано явно без искусственной cross-repository dependency.