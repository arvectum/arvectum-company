# AC-504 — Bounded Workflow Implementation — Cross-Review

Статус: `Complete`
Результат: `PASS for AC-505 transition`
Дата: `2026-08-21`
Максимум итераций: `10`
Выполнено итераций: `10 of 10`
Roadmap item: `AC-504 — Bounded workflow implementation`
Workflow: `WF-M5-001`
Implementation payload head reviewed: `8aa82ccfe49001063e8416c21bf673bfa3941b26`
Implementation evidence reviewed: `docs/operations/AC-504-BOUNDED-WORKFLOW-IMPLEMENTATION-EVIDENCE.md`, blob `ad3855fc08448dbb190b1d486f255e5592f59d71`

## 1. Review purpose

Cross-review проверяет, реализует ли AC-504 минимальный, обратимый и authority-safe operating mechanism, достаточный для одного supervised real customer case в AC-505, без premature platformization, скрытого Arvectum OS reliance, customer effect или новой Organizational Authority.

Review фиксирует вопросы, наблюдаемые факты, material findings и disposition. Private chain-of-thought не сохраняется.

## 2. Reviewed exact payload

Reviewed implementation payload:

- `tools/wf_m5_001_case.py` — blob `19373811e761226c3e418fa1b8086828c9caded6`;
- `tests/test_wf_m5_001_case.py` — blob `14e20464fd2aea2d0b85c5b286950ae7ac55f86a`;
- `.github/workflows/wf-m5-001-case.yml` — blob `f09e3969cb4e56cdc8cc59917439bb4ee32d493e`;
- `docs/operations/WF-M5-001-BOUNDED-IMPLEMENTATION-RUNBOOK.md` — blob `c51b522d66ce80ca4e2e46e5494fa32c3301ee27`;
- `docs/operations/WF-M5-001-CASE-TEMPLATE.json` — blob `b66fc43e1fa47e13c5f251588324a7a813bfd9fa`;
- `.gitignore` — blob `516cb25b279ec91757230e37242ecb3fbd38f060`.

Implementation evidence:

- `docs/operations/AC-504-BOUNDED-WORKFLOW-IMPLEMENTATION-EVIDENCE.md` — blob `ad3855fc08448dbb190b1d486f255e5592f59d71`.

Governing pins:

- AC-502 Approved publication blob `9b06e02a6d9afa8b6b4533d3a9f71690518c3ce1`;
- AC-502 reviewed proposal blob `b1df71839422e509cbfa76faec31bf788ca9842d`;
- AC-503 Approved publication blob `8984d4c094da87a2c9d201fd9cffcd617c641f8f`;
- Discount Parser baseline re-checked at `a8c1b29702a8ce40bd30b5d972ac2541367900e1`.

Executed local-equivalent test evidence recorded by AC-504:

`7 tests / 7 PASS / 0 failures / 0 errors`.

No remote GitHub Actions run is claimed as evidence in this review.

---

## 3. Iteration 1 — Scope and business minimality

### Review question

Does the implementation solve only the first supervised workflow-case need, or does it prematurely create a new platform/system?

### Finding

The implementation consists of one stdlib Python helper, JSON local storage, a runbook, a manual fallback template, bounded tests and a narrow regression workflow. It does not add a database, service, event bus, generic workflow DSL, queue, orchestration layer, CRM or Arvectum OS substitute.

### Disposition

`PASS`.

The implementation is materially smaller and more reversible than a generic workflow platform and is proportional to AC-504.

---

## 4. Iteration 2 — Workflow/state correctness

### Review question

Does the implementation preserve the approved AC-502 distinction among feedback intake, classification, technical correction, Candidate Ready, customer validation and closure?

### Finding

The helper represents W0…W11 and validates material transitions. The normal technical path requires CL-1; W7 requires technical verification/provenance; W8 requires a handoff evidence reference; W10 requires explicit customer validation evidence.

Candidate Ready is therefore not collapsed into handoff or acceptance.

### Bounded limitation

W11 is terminal in helper v1 and does not automate recovery/resume. This is deliberate: AC-506 owns actual incident/uncertain-outcome/recovery/fallback drill. AC-504 provides explicit fail-closed state plus manual fallback.

### Disposition

`PASS` for AC-504 scope.

---

## 5. Iteration 3 — Position and authority correctness

### Review question

Does implementation preserve the approved POS-002/POS-004 and AM boundary without creating authority from software?

### Finding

- W1/W2/W3/W4/W8/W10 require POS-002 attribution;
- W5/W6/W7 require POS-004 attribution;
- W3 classification requires AM-2;
- accepted authority modes are only AM-0/AM-1/AM-2;
- AM-3/AM-4 are rejected;
- the tool records `principal_ref` but does not independently authenticate legal identity or create authority.

### Disposition

`PASS`.

Software is an enforcement/evidence aid only. Existing Company authority remains the source of the allowed acts.

---

## 6. Iteration 4 — Customer external-effect and acceptance boundary

### Review question

Can technical execution or the helper itself silently create a customer-facing effect, promise or acceptance state?

### Finding

The helper has no send/deploy/payment/signing operation. `handoff` records a reference to an already authorized external act; it does not perform that act. W10 requires explicit customer validation evidence. Tests include a negative path proving closure cannot occur without a validation reference.

### Disposition

`PASS`.

`technical PASS ≠ customer-facing approval ≠ customer acceptance` remains operationally preserved.

---

## 7. Iteration 5 — Data, access and secret handling

### Review question

Does AC-504 avoid placing raw customer evidence or reusable secrets into the public repository or ordinary workflow record?

### Finding

- default real-case directory `.local/wf-m5-001/` is git-ignored;
- case records are reference-oriented;
- DC-3 storage through helper reference classification is rejected;
- common private-key/credential/token patterns are rejected;
- runbook requires protected opaque references and sanitized summaries.

### Bounded limitation

Secret-pattern detection is deliberately lightweight and is not DLP, legal-compliance or perfect PII detection. Sanitized free-text fields still depend on operator discipline.

### Disposition

`PASS with explicit bounded limitation`.

The limitation is acceptable for the supervised first proof and must not be represented as comprehensive security/compliance automation.

---

## 8. Iteration 6 — Evidence and reconstructability

### Review question

Can one case be reconstructed from exact governance/product/customer references without duplicating authoritative truth?

### Finding

The schema pins exact AC-502/AC-503 blobs, product repository/baseline, current state, transition history, classification history, Position/Principal/AM attribution, technical references, handoff/validation references, blockers and lightweight measurements.

Validation checks continuity of transition history and exact governance pins.

### Disposition

`PASS`.

This is sufficient evidence structure for AC-505 supervised proof without requiring OS shared execution history.

---

## 9. Iteration 7 — Product and source-of-truth boundary

### Review question

Does Company implementation improperly become the source of truth for Discount Parser technical state or customer truth?

### Finding

The helper stores only product/customer/control references plus sanitized Company interpretation. Discount Parser product code, issues, PRs, commits, tests/builds/releases remain in `arvectum/discount-parser`; raw customer feedback/validation remains outside the public Company repo.

No product repository mutation was made by AC-504.

### Disposition

`PASS`.

Company, Product and customer-source responsibilities remain separated.

---

## 10. Iteration 8 — Arvectum OS neutrality and sovereignty

### Review question

Does implementation respect approved AC-503 `NO-ADDITIONAL-OS-RELIANCE`, or does it recreate hidden OS/platform coupling?

### Finding

The implementation imports no Arvectum OS runtime/API, writes no OS canonical state/history, uses no CAP-004, does not alter P6.06 and creates no Product Contract or Platform Capability transition.

Runtime is Python stdlib + local JSON and can be replaced by manual operation using the same evidence fields.

### Disposition

`PASS`.

No hidden cross-repository OS commitment is created.

---

## 11. Iteration 9 — Continuity, fallback and operator burden

### Review question

Can the first case continue safely if the helper/runtime is unavailable, and is the implementation light enough not to create a new Owner bottleneck?

### Finding

Manual fallback is explicitly documented through the case template and runbook. The same minimum evidence model can be maintained without the helper. No service/database installation or credential setup is required. Owner-burden measurements are lightweight optional fields rather than a new timekeeping system.

Actual recovery effectiveness is not yet empirical evidence and remains AC-506 work.

### Disposition

`PASS` for implementation readiness.

---

## 12. Iteration 10 — Adversarial checks and AC-505 readiness

### Review question

Do implemented negative tests cover the most material ways this helper could falsely make the workflow look governed or complete, and is it ready for one real supervised case?

### Finding

Current tests cover:

- explicit customer result required for closure;
- new scope cannot enter normal correction path;
- Candidate Ready requires test/provenance;
- secret-like material rejection;
- explicit unknown fail-closed state;
- acceptance requires validation reference;
- persisted case preserves exact governance pins.

A real AC-505 case is still required to test actual customer evidence quality, actual Owner intervention burden, real product execution/verification links and real customer outcome. Those are empirical questions and must not be inferred from unit tests.

### Disposition

`PASS for AC-505 transition`.

---

## 13. Cross-review synthesis

All 10 review lenses are complete.

Blocking contradictions found: `0`.

Material bounded limitations retained:

1. secret detection is a guardrail, not comprehensive DLP/compliance;
2. W11 recovery/resume automation is intentionally deferred to AC-506;
3. remote GitHub Actions execution is not claimed as AC-504 evidence; executed local-equivalent tests are `7/7 PASS`;
4. no real customer case or customer acceptance has yet been proven;
5. no business-value/economic conclusion may be drawn before AC-505/AC-507 evidence.

None of these limitations blocks one supervised AC-505 case.

## 14. Governance disposition

AC-504 operates within already-approved AC-502/AC-503 scope and creates no new Reserved Owner Decision, AM-3/AM-4 delegation, budget, customer commitment, Product Contract or OS lifecycle transition.

Therefore repeating an Owner approval ceremony solely to publish the bounded implementation would add control overhead without changing authority.

Cross-review disposition:

**`AC-504 — PASS for AC-505 transition`.**

After final canonical merge/publication:

- AC-504 may be marked `Complete / PASS`;
- roadmap may advance to `AC-505 — Supervised real-operation proof`;
- AC-505 must use actual customer feedback/evidence and actual product technical evidence under the existing human customer/acceptance gates;
- technical/unit-test PASS must not be represented as AC-505 or M5 proof.
