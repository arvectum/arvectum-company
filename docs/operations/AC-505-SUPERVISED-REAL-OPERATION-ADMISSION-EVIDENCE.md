# AC-505 — Supervised Real-Operation Admission Evidence

Статус: `In Progress`
Результат текущего admission check: `REAL CASE CANDIDATE FOUND — POS-002 CLASSIFICATION GATE`
Версия: `0.2.0`
Дата: `2026-08-21`
Roadmap item: `AC-505 — Supervised real-operation proof`
Workflow: `WF-M5-001 — Customer Feedback → Classified Correction → Verified Candidate → Customer Validation / Acceptance`
Первый contour: `PORT-002 — Discount Parser`

## 1. Purpose

Этот artifact фиксирует фактический старт AC-505 и admission check перед первым real supervised case.

Он не является доказательством завершения AC-505, customer acceptance, production readiness или M5 closure.

Главное правило:

**pre-AC-504 product work нельзя задним числом выдать за supervised execution, но реально существующий unresolved feedback item можно взять в работу prospectively после появления AC-504 implementation, если chronology и unknowns сохранены честно.**

## 2. Governing baseline re-check

Company main содержит AC-504 `Complete / PASS` и roadmap `0.40.0`, где AC-505 является `Current`.

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

PR #74/#75 являются product implementation/provenance evidence. Они **не являются сами по себе customer acceptance evidence** и не будут ретроспективно маркироваться как AC-505 W4→W7 execution.

## 4. Real customer evidence candidate

Connected Gmail re-check обнаружил реальную Kwork notification от customer workstream `An1480`:

- timestamp: `2026-08-20T13:44:29Z`;
- protected source class: customer/Kwork evidence;
- sanitized meaning: customer reports that parsing does not work with the configured settings;
- public-safe protected reference: `protected-gmail:kwork:2026-08-20:discount-parser-settings-feedback`.

Raw email/message body and unnecessary customer identifiers are not copied into the public repository.

This item is real, non-synthetic and customer-derived.

## 5. Chronology rule

The feedback event predates AC-504 implementation. That does **not** authorize a retrospective claim that earlier engineering work was governed by AC-504.

However, AC-505 roadmap requires an `актуальный реальный feedback item`, not necessarily a feedback item received only after AC-504 publication.

Therefore an unresolved/uncertain historical real feedback item may be opened **now** as a prospective supervised case if all of the following remain explicit:

1. original `received_at` remains the historical customer timestamp;
2. case creation/supervision starts only after AC-504 exists;
3. earlier PR/commit/build evidence remains historical context, not fabricated W4→W7 transitions;
4. current product baseline is pinned separately;
5. current reproduction, affected version and resolution state are treated as unknown until evidenced;
6. POS-002 classification is performed now and attributable to the current human Principal.

This preserves temporal integrity while avoiding the opposite error of discarding a still-relevant real customer problem solely because governance was implemented later.

## 6. Current evidence gaps

For the Gmail feedback item, the following are not yet established from authoritative current evidence:

- exact application/installer version used when the customer observed the problem;
- exact source/configuration/settings state that produced the failure;
- whether the same failure reproduces on current product main / synchronized version `0.1.11`;
- whether the customer-side environment changed after the report;
- whether a later Kwork reply resolved/superseded the complaint outside the available connected evidence;
- whether current accepted-scope basis is sufficient to classify the observed symptom as an in-scope defect rather than evidence-insufficient/configuration/product-design issue.

Gmail search found no newer Kwork notification from the same customer in the currently available mailbox window that supplies explicit post-handoff acceptance/rework evidence.

## 7. Classification recommendation

Current **recommendation only**:

`CL-3 — Evidence insufficient / not reproduced`.

Reason:

- the customer symptom is real;
- the message is too terse to establish current reproducibility or affected build;
- current main exists and contains related source-mapping work, but that does not prove the present symptom is fixed or still present;
- forcing `CL-1` would require assuming accepted scope and defect causality that current evidence does not establish.

This recommendation is `AM-0` preparation. It is **not** the required POS-002 human `AM-2` classification decision.

## 8. Prepared case identity

Reserved public-safe case identifier for the live supervised contour:

`WF-M5-001-20260821-AC505001`.

Expected product baseline pin:

`a8c1b29702a8ce40bd30b5d972ac2541367900e1`.

Expected source ref:

`protected-gmail:kwork:2026-08-20:discount-parser-settings-feedback`.

No W3 classification is recorded until the current human POS-002 Principal explicitly confirms the classification.

## 9. Next live gate

The immediate governance gate is:

**POS-002 human classification of `WF-M5-001-20260821-AC505001`.**

Recommended decision:

`CL-3 — Evidence insufficient / not reproduced`.

If confirmed, the supervised case should record the classification and then exit the ordinary CL-1 technical path into an explicit blocked/unknown follow-up state until authoritative reproduction/customer evidence exists.

If POS-002 instead classifies `CL-1`, an accepted-scope basis reference and bounded technical admission are required before POS-004 work may begin.

## 10. Delivery/validation evidence status

Protected prior workstream evidence records that installer `DiscountParser-Setup-0.1.11.exe` was sent, but available connected evidence still does not establish customer download/install/test/acceptance.

Silence/non-download uncertainty remains pending evidence and cannot be converted into acceptance.

## 11. Explicit non-effects

This artifact does not:

- claim customer acceptance;
- claim the customer downloaded or installed 0.1.11;
- claim PR #74/#75 were executed under AC-504 governance;
- classify the case on behalf of POS-002;
- create/widen customer scope, SLA, price, obligation or legal commitment;
- create new Assignment, access or credential rights;
- activate AM-3/AM-4;
- authorize automatic customer messaging/deployment;
- create Arvectum OS reliance or Product Contract change;
- close AC-505 or M5.

## 12. Current AC-505 state

`AC-505 — In Progress / REAL CASE CANDIDATE FOUND / POS-002 CLASSIFICATION REQUIRED`.

The canonical roadmap action remains `AC-505 — Supervised real-operation proof`.
