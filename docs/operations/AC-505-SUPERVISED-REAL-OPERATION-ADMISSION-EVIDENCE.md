# AC-505 — Supervised Real-Operation Admission Evidence

Статус: `In Progress`
Результат текущего admission check: `WAIT — ELIGIBLE EXTERNAL CUSTOMER EVIDENCE REQUIRED`
Версия: `0.1.0`
Дата: `2026-08-21`
Roadmap item: `AC-505 — Supervised real-operation proof`
Workflow: `WF-M5-001 — Customer Feedback → Classified Correction → Verified Candidate → Customer Validation / Acceptance`
Первый contour: `PORT-002 — Discount Parser`

## 1. Purpose

Этот artifact фиксирует фактический старт AC-505 и fail-closed admission check перед первым real supervised case.

Он не является доказательством завершения AC-505, customer acceptance, production readiness или M5 closure.

Главное правило этого шага:

**pre-governance historical product work нельзя задним числом выдать за supervised execution AC-505.**

## 2. Governing baseline re-check

Перед admission check повторно проверены текущие canonical/product refs.

Company main на момент старта AC-505 содержит AC-504 `Complete / PASS` и текущий roadmap `0.40.0`, где AC-505 является `Current`.

AC-504 implementation boundary остаётся:

- `tools/wf_m5_001_case.py` — bounded OS-neutral case/evidence helper;
- real case storage по умолчанию `.local/wf-m5-001/`, исключён из git;
- `technical PASS ≠ customer handoff ≠ customer acceptance`;
- customer silence не является acceptance;
- AM-3/AM-4 не активированы;
- AC-503 result остаётся `NO-ADDITIONAL-OS-RELIANCE` для первого M5 proof.

## 3. Discount Parser product state re-check

Canonical product repository:

`arvectum/discount-parser`.

Re-checked product main:

`a8c1b29702a8ce40bd30b5d972ac2541367900e1`.

Этот commit — merge PR #75 `DP-REL-VER: synchronize application and installer version to 0.1.11`.

Relevant historical customer-derived product work:

- PR #74 — `DP-CUST-012: assisted source mapping with confirm-only customer UX`;
- merge commit: `87e427dec8cdc21645f220a089b0ad5ffe5d6671`;
- PR body фиксирует intended interaction: customer supplies source URL, inspects automatic proposal/preview and confirms it; low-confidence schema is not silently guessed;
- PR #75 subsequently synchronized package/installer version to `0.1.11` and merged as current product main.

PR #74/#75 являются product implementation/provenance evidence. Они **не являются сами по себе customer acceptance evidence**.

## 4. Real customer evidence available before AC-505

Protected project-chat evidence contains a real customer report from `2026-08-19` that Discount Parser opened but collected information incorrectly on a real source and that per-site mapping behavior needed correction. The same workstream then constrained customer participation to verification/confirmation of an automatic proposal rather than technical selector work.

Raw customer message is intentionally not copied into this public repository. Public-safe reference:

`protected-project-chat:discount-parser:2026-08-19:customer-feedback-source-mapping`

The public example source associated with that feedback was:

`https://promokood.ru/o/vseinstrumenti`

This evidence is historically useful for scope/reconstruction, but the implementation response to it occurred before AC-504 was established as the Company bounded workflow runtime/evidence mechanism.

Therefore the historical sequence cannot be relabelled as though W0→W7 had been supervised under AC-504 at the time it happened.

## 5. Delivery/validation evidence status

Protected project-chat evidence from `2026-08-20` records that installer `DiscountParser-Setup-0.1.11.exe` had been sent, but there was **no confirmed evidence that the customer had downloaded, installed, run or validated it** at that point.

Public-safe handoff reference:

`protected-project-chat:discount-parser:2026-08-20:installer-0.1.11-handoff`

A subsequent retrieval for post-handoff customer evidence found no later explicit customer message confirming download/install/test/acceptance, rejecting the candidate, or supplying a new rework result.

Consequently:

- handoff/reporting evidence exists;
- explicit customer validation evidence does not currently exist;
- silence/non-download uncertainty cannot be converted into acceptance;
- AC-505 cannot be closed honestly at this time.

## 6. Admission decision

The current historical feedback/correction chain is admissible as **context and historical product evidence**, but not sufficient by itself as the first supervised AC-505 proof.

No synthetic/demo workflow case will be created to fill the gap.

No retrospective helper transitions will be manufactured to make pre-AC-504 work look supervised.

The first AC-505 supervised case must begin from an eligible real external event captured after the governed implementation is available, for example:

1. a new real customer feedback item concerning Discount Parser behavior; or
2. an explicit customer validation/rework result for the already-delivered `0.1.11` candidate that can be attributed to the real customer source.

## 7. Exact next execution path once evidence arrives

For an eligible real event the operator must use `WF-M5-001 / 1.0.0` and the AC-504 helper/runbook, keeping the real case record outside git.

Required live sequence:

`real protected customer evidence`
→ `POS-002 intake/data-boundary assessment`
→ `POS-002 AM-2 classification`
→ `CL-1 only: bounded POS-002 technical admission`
→ `POS-004 bounded implementation/verification`
→ `W7 Candidate Ready`
→ `authorized human customer handoff`
→ `explicit customer validation / rework / block`
→ `measurement and AC-505 evidence publication`.

If the event is CL-4/CL-5/CL-6, ambiguous, unsupported by accepted scope, or needs unavailable access/authority, the workflow must route/escalate/fail closed rather than forcing it into CL-1.

## 8. Current AC-505 state

`AC-505 — In Progress / WAITING FOR ELIGIBLE EXTERNAL CUSTOMER EVIDENCE`.

This wait state is a governed outcome, not a failure of the implementation.

The current blocker is external evidence availability, not missing Company authority, missing OS capability, or a known technical defect in the AC-504 helper.

## 9. Explicit non-effects

This artifact does not:

- claim customer acceptance;
- claim the customer downloaded or installed 0.1.11;
- claim that PR #74/#75 were executed under AC-504 governance;
- create or widen customer scope, SLA, price, obligation or legal commitment;
- create new Assignment, access or credential rights;
- activate AM-3/AM-4;
- authorize automatic customer messaging/deployment;
- create Arvectum OS reliance or Product Contract change;
- close AC-505 or M5.

## 10. Next canonical action

The canonical roadmap action remains:

`AC-505 — Supervised real-operation proof`.

Execution resumes immediately when a qualifying real customer event is available. Until then the correct behavior is to preserve the wait state rather than manufacture empirical evidence.
