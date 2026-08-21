# AC-504 — Bounded Workflow Implementation Evidence

Статус: `Complete`
Результат: `PASS`
Версия: `1.0.0`
Дата: `2026-08-21`
Roadmap item: `AC-504 — Bounded workflow implementation`
Workflow: `WF-M5-001 — Customer Feedback → Classified Correction → Verified Candidate → Customer Validation / Acceptance`
First contour: `PORT-002 — Discount Parser`
Implementation branch: `ac-504-bounded-workflow-implementation`
Implementation payload head: `8aa82ccfe49001063e8416c21bf673bfa3941b26`

## 1. Purpose

AC-504 реализует smallest sufficient, reversible и OS-neutral механику, необходимую для следующего supervised real-operation proof `AC-505`.

Результат AC-504 — **implementation readiness for one supervised workflow case**, а не доказательство того, что реальный customer case уже выполнен.

AC-504 не создаёт customer commitment, customer acceptance, production approval, новый Product Contract, Arvectum OS reliance, новую Organizational Authority или M5 completion.

## 2. Governing baseline

Implementation создана внутри уже утверждённых границ:

- AC-502 Approved workflow publication blob: `9b06e02a6d9afa8b6b4533d3a9f71690518c3ce1`;
- AC-502 exact reviewed proposal blob: `b1df71839422e509cbfa76faec31bf788ca9842d`;
- AC-503 Approved reliance/admission publication blob: `8984d4c094da87a2c9d201fd9cffcd617c641f8f`;
- binding AC-503 result: `NO-ADDITIONAL-OS-RELIANCE` for the first M5 proof;
- `POS-002` remains end-to-end accountable and human-attributable for Company/customer gates;
- `POS-004` remains accountable for bounded technical execution through Candidate Ready;
- only existing `AM-0/AM-1/AM-2` are used; `AM-3/AM-4` are not activated.

Product implementation truth remains in `arvectum/discount-parser`.

Product main was re-checked before implementation and remained at:

`a8c1b29702a8ce40bd30b5d972ac2541367900e1`.

No Discount Parser product change was made by AC-504.

## 3. Implementation home and payload

Company-level case/evidence mechanics live in `arvectum/arvectum-company`. Product code/issues/PRs/commits/tests/builds/releases remain product-owned and cross the boundary only by references.

Exact implementation payload at branch head `8aa82ccfe49001063e8416c21bf673bfa3941b26`:

| Artifact | Purpose | Immutable blob SHA |
|---|---|---|
| `tools/wf_m5_001_case.py` | OS-neutral case/evidence helper | `19373811e761226c3e418fa1b8086828c9caded6` |
| `tests/test_wf_m5_001_case.py` | bounded invariant/regression tests | `14e20464fd2aea2d0b85c5b286950ae7ac55f86a` |
| `.github/workflows/wf-m5-001-case.yml` | repeatable GitHub Actions regression command | `f09e3969cb4e56cdc8cc59917439bb4ee32d493e` |
| `docs/operations/WF-M5-001-BOUNDED-IMPLEMENTATION-RUNBOOK.md` | operator runbook and acceptance checks | `c51b522d66ce80ca4e2e46e5494fa32c3301ee27` |
| `docs/operations/WF-M5-001-CASE-TEMPLATE.json` | manual fallback case template | `b66fc43e1fa47e13c5f251588324a7a813bfd9fa` |
| `.gitignore` | prevents default local case evidence from entering git | `516cb25b279ec91757230e37242ecb3fbd38f060` |

The implementation uses Python standard library only and introduces no new runtime/vendor dependency.

## 4. Case/evidence representation

The helper uses schema:

`wf-m5-001.case.v1`.

A case pins:

- `WF-M5-001 / 1.0.0`;
- exact AC-502 Approved/reviewed blobs;
- exact AC-503 Approved reliance decision blob;
- `PORT-002` and `arvectum/discount-parser`;
- exact product baseline used by the case;
- current `W*` state and material transition history;
- current and historical `CL-*` classification evidence;
- Position, Principal reference and `AM-*` attribution;
- sanitized/protected source references;
- technical issue/PR/commit/test/build/release-candidate references;
- customer handoff/validation references;
- explicit blocker state;
- lightweight Owner-intervention/rework measurements.

Default real-case storage is:

`.local/wf-m5-001/`.

That path is git-ignored. Public repository artifacts contain implementation/schema/runbook only, not real raw customer case payloads.

## 5. Enforced authority and state gates

The helper enforces the following bounded controls:

1. only `AM-0`, `AM-1`, `AM-2` are accepted;
2. Company/customer gates `W1/W2/W3/W4/W8/W10` require `POS-002` attribution;
3. technical gates `W5/W6/W7` require `POS-004` attribution;
4. `W3` requires attributable `POS-002 / AM-2` classification;
5. only `CL-1 — In-scope defect` can enter the ordinary `W4→W9` technical correction path;
6. `CL-1` requires an accepted-scope basis reference;
7. `W7 — Candidate Ready` requires passed verification, at least one test reference, candidate provenance and a known-limitations statement;
8. `W8` requires a recorded customer handoff reference but the tool does not perform the handoff;
9. `W10` requires explicit customer validation evidence and cannot be inferred from technical PASS or silence;
10. `W11` requires an explicit `blocked / unknown / stale / uncertain` reason and target control point.

The helper performs no customer message send, product deployment, payment, signing, acceptance, commitment or other consequential external effect.

## 6. Data and security boundary

The implementation is reference-oriented.

Allowed stored reference classifications are `DC-0`, `DC-1`, `DC-2`. `DC-3` payload/reference storage through the helper is rejected.

The helper additionally rejects several common secret-like patterns, including private-key material and credential/token assignment patterns. This is a bounded guardrail, **not** a comprehensive DLP/compliance claim.

Operators remain responsible for sanitizing summaries and using protected opaque references instead of raw customer messages, screenshots, private commercial terms, credentials or unnecessary PII.

Raw customer evidence remains in the applicable authorized customer/workstream source contour.

## 7. Reconstructability and source-of-truth separation

The implementation records material transition history and exact references sufficient to reconstruct one supervised case without duplicating product/customer canonical truth.

Source ownership remains:

- Company: workflow/accountability/authority/evidence semantics and sanitized case control metadata;
- Discount Parser repository: product implementation, issue, PR, commit, test/build/release evidence;
- customer/workstream source: raw feedback, customer environment evidence and explicit validation/acceptance result;
- AC-401/402/403 control models: material work/obligation/decision/escalation/risk/incident records when their qualification gates are triggered;
- Arvectum OS: no additional reliance for the first M5 proof under AC-503.

No Product Contract scope is expanded by this implementation.

## 8. Test evidence

Local-equivalent regression command executed against the implementation source:

```text
python -m unittest discover -s tests -p 'test_wf_m5_001_case.py' -v
```

Result:

`7 tests / 7 PASS / 0 failures / 0 errors`.

Covered behaviors:

1. happy path cannot reach acceptance without explicit customer result;
2. `CL-4` new scope cannot be admitted as ordinary correction;
3. Candidate Ready fails without test + candidate provenance;
4. secret-like material is rejected;
5. unknown evidence can fail closed explicitly to `W11`;
6. customer acceptance cannot close without validation reference;
7. persisted case round-trip preserves exact workflow governance pins.

A GitHub Actions workflow containing the same test command is committed for repeatable regression. At AC-504 evidence publication time no remote workflow run is claimed as evidence; local-equivalent 7/7 PASS is the executed test evidence.

## 9. Continuity and fallback

Primary runtime is replaceable Python 3.11+ stdlib code with JSON files; no database/service/vendor is required.

Manual fallback is provided by:

`docs/operations/WF-M5-001-CASE-TEMPLATE.json`.

The runbook defines the same minimum evidence fields for manual operation. Runtime unavailability therefore does not transfer authority or require abandoning the workflow.

`W11` recovery/resume automation is intentionally **not** implemented in AC-504. Actual incident/uncertain-outcome/recovery/fallback drill and recovery evidence belong to AC-506. AC-504 provides fail-closed representation and manual fallback only.

## 10. AC-504 acceptance result

Against ROADMAP `0.39.0` expected evidence:

- sanitized case creation/persistence: `PASS`;
- exact workflow/version/current-state recording: `PASS`;
- attributable classification: `PASS`;
- bounded technical work/verification linking: `PASS`;
- Candidate Ready / handoff / customer acceptance separation: `PASS`;
- explicit blocked/unknown/stale/uncertain state: `PASS`;
- no required raw DC-2/DC-3 payload in public repo: `PASS`;
- manual fallback/runtime replacement: `PASS`;
- minimal implementation, no generic workflow engine/OS substitute: `PASS`;
- ready for one supervised AC-505 case: `PASS`.

Therefore:

**`AC-504 — Complete / PASS`**, subject to cross-review of this exact implementation payload and final canonical publication/merge.

## 11. Explicit non-effects

AC-504 PASS does not establish:

- successful real customer workflow execution;
- customer acceptance;
- Discount Parser production readiness;
- profitability or customer willingness to pay;
- legal/compliance readiness;
- Arvectum OS reliance or capability lifecycle change;
- `AM-3/AM-4` authority;
- M5 closure.

Those empirical/control questions remain AC-505…AC-507.
