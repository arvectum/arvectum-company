# AC-207 — Critical-Function Continuity, Replacement and Manual Fallback Cross-Review

Status: `Complete / PASS for Owner approval`
Review date: `2026-08-21`
Iterations completed: `9 of maximum 10`
Result: `PASS — the proposal defines conservative continuity/degraded/fail-closed/recovery semantics for all six approved Positions, preserves Owner/legal/customer/security gates, makes AI and runtime replacement possible without authority inheritance, distinguishes mirror availability from canonical promotion, exposes current Owner/legal/signing/bank/credential continuity gaps, and avoids claiming tested disaster recovery or fabricated alternate providers`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-207 — Critical-function continuity, replacement and manual fallback baseline`
Reviewed artifact: `docs/operations/CRITICAL-FUNCTION-CONTINUITY-REPLACEMENT-FALLBACK-BASELINE.md`
Reviewed publication: `Proposed 0.9.0`
Reviewed blob SHA: `425ab4d83098aa3dbc73925305aa5d9981512818`
Maximum review iterations: `10`
Approval status: `Pending explicit Owner approval of the exact reviewed proposal`
Arvectum OS main re-checked: `d7c70355c0bd13148c493500990f83b522805831`

## 1. Review purpose

The review tests whether AC-207 makes Arvectum Company more resilient without converting continuity into a mechanism for bypassing authority, security, customer rights or legal gates.

The principal failure modes tested are:

- treating urgency or outage as a source of authority;
- automatically transferring a Position's authority to an AI model, replacement runtime or technical administrator;
- assuming any human can take over AI-led Engineering without Assignment/competence/access evidence;
- silently promoting GitVerse or a local copy into canonical authority because GitHub is unavailable;
- inventing alternate signing/payment/legal-representation paths;
- calling an untested fallback “ready”;
- losing customer/commercial/engineering state in one Owner memory or one AI session;
- letting recovery broaden customer/data access;
- preserving uptime by weakening least privilege.

## 2. Iteration 1 — continuity must not mean bypass

**Criticism:** A continuity plan often optimizes for “keep operating”, which is unsafe in an authority-governed Company. Owner, legal, customer, bank, signature or security gates may be deliberately blocking.

**Reconciliation:** the proposal makes the primary invariant explicit:

```text
continuity ≠ bypass
replacement ≠ authority transfer
technical recovery ≠ business approval
```

It defines `CM-0` through `CM-4`, including explicit `CM-3 — Fail Closed`, and states that an unavailable legitimate gate may stop the affected action.

**Result:** PASS.

## 3. Iteration 2 — current Owner concentration must be represented as a real continuity gap

**Criticism:** AC-205 assigns the current Owner human Principal to POS-001, POS-002, POS-003, POS-005 and POS-006. A superficial continuity baseline could claim AI support makes these Positions Owner-independent.

**Reconciliation:** the proposal does the opposite. During Owner absence:

- AI in POS-001/003/006 remains preparation/advisory and does not inherit human AM-2 or Owner ROD authority;
- POS-002 may only preserve already-approved bounded mechanics; material commitments/ambiguous customer decisions stop;
- POS-005 accounting may continue in its contracted external contour but does not inherit management/spending authority;
- POS-004 bounded AI-led Engineering is the principal function that can continue materially without the Owner while its scope/access/risk remain clear.

Extended Owner/legal-authority absence is explicitly `CE-0 — Unresolved`, not hidden behind a workflow workaround.

**Result:** PASS.

## 4. Iteration 3 — AI-led Engineering must be replaceable without making a specific model the Position

**Criticism:** POS-004 is AI-led. If its current model/agent is unavailable, either engineering stops completely or a replacement model is implicitly granted the prior agent's identity/access/authority.

**Reconciliation:** the proposal distinguishes runtime replacement from Principal replacement.

A runtime may be swapped while preserving a valid governed workload identity/Assignment where the architecture supports it. If a genuinely different Principal is introduced, an explicit Assignment/access change is required.

Replacement requires reconstructable repo/commit/task/tests/constraints/limitations/toolchain/access state and cannot rely on hidden model memory.

Manual human fallback is not assumed: a human must be explicitly assigned and provisioned before taking over POS-004.

**Result:** PASS.

## 5. Iteration 4 — GitHub/GitVerse/local continuity must preserve canonical authority

**Criticism:** because GitVerse is a resilience mirror, an outage of GitHub could tempt the Company to treat the mirror as automatically canonical or create two divergent authorities.

**Reconciliation:** GitHub remains canonical under the current approved repository model. During outage, GitVerse/local clones may preserve work/history and support bounded internal work, but no automatic canonical promotion occurs.

Divergence is handled through `CM-4` recovery: identify pre-outage authoritative head, inspect divergent history, reconcile explicitly, then resume canonical publication. A canonical-remote change requires an explicit applicable Company decision.

**Result:** PASS.

## 6. Iteration 5 — credential, device, signing and bank continuity must fail closed where necessary

**Criticism:** credential loss, physical token failure or bank outage can create pressure to share Owner credentials, bypass signing controls or use an improvised payment route.

**Reconciliation:** the proposal requires revocation/rotation/recovery through the authoritative provider/control path, least-privilege re-provisioning and trusted-state verification.

Qualified electronic signature/physical signing mechanisms remain deliberate technical/legal gates. If the valid token/certificate/signer is unavailable, the signing action stops. Bank/payment outage similarly does not authorize an improvised substitute.

Local device replacement requires trusted re-bootstrap, scoped access and secure secret rehydration rather than copying unrestricted Owner state.

**Result:** PASS.

## 7. Iteration 6 — customer/commercial continuity must preserve commitments, rights and isolation

**Criticism:** customer continuity can fail in two opposite ways: all work stops because context lives in Owner memory, or recovery proceeds by using stale/incorrect/cross-customer information.

**Reconciliation:** the proposal introduces a minimum continuity packet containing scope/exclusions, last authority/decision reference, commitments, acceptance state, canonical references, data-rights/classification, required access, risks, stop conditions and pending decisions.

Customer data recovery remains purpose- and organization-scoped. A recovery copy does not broaden rights. Customer silence does not become acceptance. Unavailable/uncertain customer truth produces blocked/degraded state instead of invented state.

Future sellers remain conditional until actually engaged/assigned/provisioned.

**Result:** PASS.

## 8. Iteration 7 — outsourced accounting continuity must not recreate bookkeeping or payment authority inside the Company model

**Criticism:** provider replacement could either make the Company dependent on an opaque accounting provider state or drive the Company to duplicate statutory accounting in the public Company repository.

**Reconciliation:** the proposal requires recoverable source documents, management obligation visibility and transition metadata, while preserving the external accounting/statutory contour as authoritative.

If the provider is unavailable, unverifiable statutory/accounting facts are marked unavailable/uncertain; they are not fabricated. A replacement provider requires an actual service/legal/access transition. The provider never inherits Company management/spending authority.

**Result:** PASS.

## 9. Iteration 8 — evidence maturity must distinguish “specified” from “tested”

**Criticism:** a detailed continuity matrix can look operationally mature even when no restore/failover exercise has occurred.

**Reconciliation:** AC-207 defines `CE-0` through `CE-3` evidence states and explicitly refuses to upgrade a fallback without evidence.

The current matrix intentionally contains multiple `CE-0` and `CE-1` items: replacement human Positions, legal representation continuity, signing continuity, alternate bank path, complete credential recovery, customer-data recovery and independent security/risk decision continuity.

Repository history itself is evidenced as durable current state, but mirror restore/reconciliation is separately only `CE-1`; the proposal does not equate ordinary Git use with a tested disaster-recovery exercise.

**Result:** PASS.

## 10. Iteration 9 — end-to-end recovery/reconciliation and Company↔Product↔OS boundaries

**Criticism:** individual fallbacks can still create inconsistent state after recovery, especially across Company governance, product repositories, customer systems and OS-governed workflows.

**Reconciliation:** the proposal defines a ten-step `CM-4` recovery sequence: scope → authority → contain ambiguity → establish trusted source → restore least-privilege environment → compare divergent state → reconcile explicitly → verify controls → resume bounded work → promote validated learning.

It also preserves repository ownership:

- Company does not recreate product implementation truth;
- product-specific recovery remains product-owned;
- Company governance does not become unavailable merely because OS is unavailable;
- a product-local fallback is not mislabeled OS-governed execution;
- customer/data rights survive migration/recovery.

The handoff to AC-208 is methodological rather than copying Arvectum's exact fallback matrix into customer organizations.

**Result:** PASS.

## 11. Acceptance test

| Test | Result |
|---|---|
| continuity is explicitly distinct from bypass | PASS |
| five continuity modes defined | PASS |
| evidence maturity distinguishes unresolved/untested/operational/tested | PASS |
| replacement runtime is distinct from replacement Principal | PASS |
| legal/corporate succession is not invented | PASS |
| minimum continuity packet removes dependence on one memory/session | PASS |
| POS-001 AI does not inherit human AM-2 or ROD authority | PASS |
| POS-002 preserves bounded outreach without autonomous commitment | PASS |
| future sellers do not activate automatically | PASS |
| POS-003 AI cannot make material portfolio decisions during Owner absence | PASS |
| POS-004 model/runtime can be replaced in principle without changing Position meaning | PASS |
| POS-004 human fallback requires explicit Assignment/access | PASS |
| release/deploy/signing gates remain separate from engineering continuity | PASS |
| POS-005 accounting provider remains external professional contour | PASS |
| bank/payment outage does not authorize substitute route | PASS |
| POS-006 AI does not inherit material risk acceptance/security admin | PASS |
| GitVerse/local copies do not become canonical automatically | PASS |
| recovery explicitly reconciles divergent state | PASS |
| product implementation remains product-owned | PASS |
| OS outage does not invalidate Company governance | PASS |
| customer-data recovery preserves purpose/isolation/rights | PASS |
| credential compromise causes revoke/rotate/reverify rather than privilege broadening | PASS |
| signing/token failure fails closed | PASS |
| current Owner concentration is stated as unresolved continuity risk | PASS |
| no fabricated RTO/RPO/SLA or redundant provider claims | PASS |
| no claim of full continuity/DR readiness | PASS |
| downstream implementation evidence is explicit | PASS |
| AC-208 transferability handoff is method-level | PASS |

## 12. Why the review closes at iteration 9 of 10

The remaining material questions require real implementation or live failure/recovery evidence:

- complete credential inventory and rotation/recovery exercise;
- controlled GitHub/GitVerse/local restore and reconciliation exercise;
- a real POS-004 AI-runtime swap;
- local machine re-bootstrap test;
- actual customer continuity packet and seller/operator handoff;
- accounting provider transition evidence;
- dedicated commercial sender/CRM failover evidence;
- legal review/instrument for extended Owner/authorized-representative absence;
- signing certificate/token replacement evidence;
- customer-data backup/restore/expiry tests.

A tenth desk-only review would either repeat the current rules or fabricate evidence that does not exist.

Stopping at iteration 9 is therefore evidence-disciplined.

## 13. Final conclusion

`PASS — material consensus reached at 9 of maximum 10 iterations.`

AC-207 `Proposed 0.9.0`, blob `425ab4d83098aa3dbc73925305aa5d9981512818`, is ready for explicit Owner approval.

Approval is required because the baseline establishes Company-wide continue/degrade/fail-closed/recovery expectations for material function and dependency failures.

After approval, the unchanged substance may be published as the binding AC-207 continuity baseline, registered canonically, AC-207 may close as `Complete / PASS`, and the roadmap may advance to:

`AC-208 — Reference-model transferability boundary and operating-model cross-review`.