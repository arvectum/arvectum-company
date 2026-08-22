# AC-506 — Incident, Uncertain-Outcome, Recovery and Fallback Drill Evidence

Статус: `Complete`
Результат: `PASS`
Версия: `1.0.0`
Дата: `2026-08-22`
Roadmap item: `AC-506 — Incident, uncertain-outcome, recovery and fallback drill`
Workflow: `WF-M5-001 / 1.0.0`
First contour: `PORT-002 — Discount Parser`

## 1. Objective

AC-506 проверяет, что первый governed workflow не теряет authority/data/evidence boundaries при недостаточных данных, неизвестном внешнем outcome, потере helper/runtime и последующем появлении нового evidence.

Drill не должен создавать выдуманный customer outcome или ретроспективно изменять реальный AC-505 case.

Граничные принципы:

```text
recovery ≠ rewrite
uncertain outcome ≠ success
runtime replacement ≠ authority transfer
manual fallback ≠ weaker controls
synthetic drill evidence ≠ customer evidence
```

## 2. Canonical baseline re-check

Перед drill повторно проверены:

- Company main before AC-506 implementation: `2433a9aae78a9415d1dbdc2b6a9f11d2e256c307`;
- AC-207 Approved continuity baseline `1.0.0`;
- AC-502 Approved workflow contract `1.0.0`;
- AC-503 `NO-ADDITIONAL-OS-RELIANCE` decision for the first M5 proof;
- AC-504 bounded helper/runbook/manual fallback;
- AC-505 real case evidence `WF-M5-001-20260821-AC505001`.

AC-207 requires designed fallback to remain distinct from tested fallback and defines `CM-0…CM-4` / `CE-0…CE-3` semantics. In particular, runtime replacement does not transfer authority and missing/uncertain customer state may legitimately force fail-closed behavior.

## 3. Real case used for uncertainty drill

Real AC-505 case:

`WF-M5-001-20260821-AC505001`.

Observed governed state:

`W3 — CL-3 Evidence insufficient / not reproduced`
→
`W11 — unknown / customer-evidence follow-up required`.

Real protected source:

`protected-gmail:kwork:2026-08-20:discount-parser-settings-feedback`.

The case has no authoritative evidence of customer download/install/test/acceptance for the delivered 0.1.11 candidate and no current reproduction basis sufficient for CL-1.

### Drill D1 — unknown external/customer outcome

Expected behavior:

- do not infer acceptance;
- do not admit POS-004 technical correction;
- preserve original case and blocker;
- wait for new attributable evidence.

Observed result:

**PASS.** The real case remains W11; no customer effect or technical admission was created solely to move the milestone.

This is actual operating evidence, not synthetic evidence.

## 4. Recovery design implemented

New implementation:

`tools/wf_m5_001_recovery.py`.

Recovery strategy:

**immutable predecessor + linked successor**.

A W11 case is never silently reopened. New evidence creates a new case with:

- explicit new source ref;
- exact current product baseline supplied by operator;
- safe predecessor control link;
- predecessor blocker kind;
- fresh intake;
- no automatic classification;
- no automatic W4 technical admission.

This resolves the AC-504 bounded limitation that W11 recovery/resume mechanics were intentionally deferred to AC-506 without weakening the terminal history of the original case.

## 5. Deterministic recovery tests

New test artifact:

`tests/test_wf_m5_001_recovery.py`.

Recovery tests cover:

1. W11 successor preserves predecessor byte-for-byte;
2. non-W11 predecessor is rejected;
3. predecessor feedback ref cannot be reused as purported new evidence;
4. recovery does not auto-classify or auto-admit;
5. recovered CL-3 still cannot enter technical correction;
6. secret-like recovery evidence is rejected;
7. duplicate successor case id is rejected rather than overwriting state.

Existing 7 AC-504 tests remain active.

## 6. Fresh runtime/process execution evidence

GitHub Actions PR validation:

- PR: `#8 — AC-506 — recovery drill validation`;
- tested head commit: `931853edbf5e162c103091539b55f8b7068db4fb`;
- workflow: `WF-M5-001 Case Helper`;
- run id: `32555014701`;
- job id: `96987697988`;
- runner: GitHub-hosted Ubuntu 24.04;
- Python: CPython `3.12.14`;
- command: `python -m unittest discover -s tests -p 'test_wf_m5_001_*.py' -v`;
- result: **14 tests / 14 PASS / 0 failures / 0 errors**.

This is a fresh checkout/process with no dependency on the active ChatGPT session or local `.local/wf-m5-001` state.

### Evidence interpretation

This upgrades only the narrow **WF-M5-001 helper/recovery runtime-process portability** evidence to `CE-3 — Tested and Reviewed` after cross-review.

It does **not** prove:

- actual POS-004 AI-model/agent runtime swap;
- replacement Principal Assignment;
- Owner-independent Company operation;
- disaster recovery of customer systems;
- production deployment/signing continuity.

Those AC-207 gaps remain unchanged.

## 7. Manual fallback reconstruction drill

The drill intentionally treated the live helper/local case store as unavailable and reconstructed the next-safe-action packet from canonical/public-safe artifacts only:

- workflow id/version and governance pins — available from AC-504 runbook/helper;
- case id — available;
- accountable Position — POS-002 available;
- product/repository/current baseline — available;
- protected customer-source pointer — available;
- classification and attributable human decision — available;
- blocker kind/reason/target — available;
- next safe action — wait for new authoritative evidence; no POS-004 admission;
- customer acceptance state — explicitly unknown/not evidenced;
- stop condition — no technical/customer consequence without new evidence/authority.

Raw customer payload and secrets were not required for reconstructing the safe governance state.

Result:

**PASS for bounded case-state reconstruction/manual fallback.**

Narrow evidence state after cross-review:

`WF-M5-001 case-state/manual fallback → CE-3`.

This does not upgrade Company-wide customer continuity packet readiness or Owner/legal succession readiness.

## 8. Incident-like security/data drill

AC-506 includes a deliberate synthetic guardrail scenario: a recovery evidence reference contains secret-like token material.

Expected behavior:

- reject the evidence from ordinary case storage;
- do not downgrade it to DC-1/DC-2 merely to continue work;
- do not create customer/technical effect;
- route real security/material-risk facts through applicable AC-403 / POS-006 semantics if such facts actually occur.

Test result:

**PASS — secret-like recovery evidence is rejected.**

This is a synthetic incident-like drill only. It does **not** assert that a real security incident occurred and does not create an `INC-*` record.

## 9. Duplicate/retry uncertainty drill

A recovery attempt using an already-existing successor case id is rejected.

Result:

**PASS.** The tool does not overwrite the first successor and therefore does not erase provenance under retry/uncertain operator outcome.

This specifically protects against a common recovery failure mode: treating an uncertain prior attempt as if it definitely never happened.

## 10. Continuity modes exercised

The drill exercised the following AC-207 semantics:

- `CM-3 — Fail Closed`: real CL-3/W11 case with insufficient evidence;
- `CM-2 — Degraded`: evidence preparation/reconstruction can continue while consequential work cannot;
- `CM-4 — Recovery / Reconciliation`: new evidence is represented by a linked successor rather than rewriting predecessor state;
- `CM-1 — Bounded Continuity`: deterministic helper/recovery mechanics execute in a fresh hosted process without authority expansion.

## 11. Evidence-state result

After successful cross-review, AC-506 supports these narrow evidence-state changes:

| Scope | Before | After AC-506 | Boundary |
|---|---|---|---|
| WF-M5-001 W11 successor recovery mechanics | deferred / untested | `CE-3` | synthetic deliberate recovery test; no fake customer recovery |
| WF-M5-001 case-state manual reconstruction | `CE-1` design | `CE-3` | bounded workflow case only |
| WF-M5-001 helper/process portability | bounded implementation evidence | `CE-3` | fresh GitHub-hosted checkout/process |
| real insufficient-evidence fail-closed behavior | limited | `CE-2` | actual AC-505 W11 operating evidence |
| actual POS-004 AI runtime/model swap | `CE-1` | unchanged `CE-1` | not exercised |
| Owner-independent commercial continuity | `CE-0/CE-1` | unchanged | not exercised |
| Company-wide DR / credential / signing / provider replacement | mixed `CE-0/CE-1` | unchanged | not exercised |

No Company-wide continuity claim is made from a workflow-level drill.

## 12. Business/Owner burden observation

The real W11 case demonstrated a useful control property: the Company can stop rather than spend engineering effort on an unsupported defect hypothesis.

The current evidence does not yet support a quantified economic saving. That belongs in AC-507 and must not be fabricated.

Observed governance cost for this drill includes additional case/evidence handling and one explicit human classification. Whether that overhead is justified by avoided rework/risk remains an AC-507 question.

## 13. Arvectum OS boundary

No new actual OS governed reliance was needed.

AC-503 `NO-ADDITIONAL-OS-RELIANCE` remains intact for this first proof/drill contour.

AC-506 creates no Product Contract, capability lifecycle transition or OS repository commitment.

## 14. Approval / authority boundary

AC-506 does not change ROD, Assignment, access ceiling, AM authority, customer promise, budget, Product Contract or external obligation.

The work is bounded implementation/testing/reconciliation under already-approved AC-207/AC-502/AC-503/AC-504 semantics. No separate Owner approval ceremony is required for AC-506 completion unless cross-review discovers a material governance change.

## 15. Completion result

`AC-506 — Complete / PASS` subject to final cross-review and canonical roadmap synchronization.

AC-505 remains open independently because the real customer case is still W11 pending authoritative evidence.

AC-507 may proceed with its preparatory economic/business-value evidence collection, but final M5 closure still requires the evidence demanded by the roadmap.
