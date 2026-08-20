# AC-203 — Delegated Position Authority Cross-Review

Status: `Complete / PASS for Owner approval`
Review date: `2026-08-20`
Iterations completed: `9 of maximum 10`
Result: `PASS — the proposal defines a bounded Position-level delegation model that reduces unnecessary Owner involvement while preserving AC-202 Reserved Owner Decisions, legal/corporate competence, customer authority, Product/OS boundaries, explicit approval semantics, fail-closed escalation and executor/runtime replaceability without creating concrete Positions or invented numeric thresholds`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-203 — Delegated Position authority, approval and escalation model`
Reviewed artifact: `docs/governance/DELEGATED-POSITION-AUTHORITY-MODEL.md`
Reviewed publication: `Proposed 0.9.0`
Reviewed blob SHA: `ba89771f7b3ead7f70b0482f06d7d04bc68df2ea`
Maximum review iterations: `10`
Approval status: `Pending explicit Owner approval of the exact reviewed proposal`

## 1. Review purpose

The review tests whether AC-203 creates a practical delegation model rather than either:

- a disguised return to Owner approval for everything;
- an unsafe transfer of material authority to Positions, AI or technical operators;
- a premature Position Registry;
- or an abstract governance model with no usable escalation semantics.

The review uses AC-201 functions and AC-202 Reserved Owner Decisions as hard upstream constraints.

## 2. Iteration 1 — delegation must attach to Position, not executor

**Criticism:** a model that grants authority directly to today's human, AI agent or service would make authority unstable when the executor changes and would contradict the organization-first sequence.

**Reconciliation:** AC-203 makes the Position authority envelope primary. An Assignment may narrow that envelope for a particular Principal but cannot broaden it. Runtime/tool replacement does not alter Position authority by implication.

**Result:** PASS.

## 3. Iteration 2 — one generic “delegated authority” category is too coarse

**Criticism:** preparation, execution, bounded decision, approval and automatic execution have materially different consequences. Treating them as one permission class would recreate ambiguity around technical ability versus organizational authority.

**Reconciliation:** AC-203 introduces five explicit modes:

- `AM-0` Prepare / Recommend;
- `AM-1` Execute Pre-Decided Work;
- `AM-2` Bounded Decision;
- `AM-3` Delegated Approval;
- `AM-4` Pre-Authorized Automatic Execution.

This keeps approval distinct from analysis and allows automatic execution to be modeled as a pre-authorized class rather than fictitious software discretion.

**Result:** PASS.

## 4. Iteration 3 — AC-202 must remain a hard negative boundary

**Criticism:** AC-203 could silently erode Owner control by defining broad Position authority that functionally includes a `ROD-*` decision even if the document nominally says otherwise.

**Reconciliation:** every delegation envelope must carry explicit excluded decisions, including applicable `ROD-01` through `ROD-09`. Mandatory escalation is triggered whenever a case enters a ROD class. `AM-3` cannot absorb a ROD final decision unless AC-202 itself is explicitly amended and approved.

**Result:** PASS.

## 5. Iteration 4 — numeric thresholds must not be fabricated

**Criticism:** practical delegation often requires ruble, duration, liability, data or risk thresholds, but current Company evidence does not justify universal numbers. Inventing them now would create false precision and potentially unsafe authority.

**Reconciliation:** AC-203 defines required **limit dimensions** but leaves concrete values to later Position/delegation records when business evidence exists. Where a reliable threshold does not exist, the matter remains residual Owner authority or escalates.

**Result:** PASS.

## 6. Iteration 5 — AI/software approval semantics need stronger separation

**Criticism:** because future Positions may be AI-held, `AM-3 — Delegated Approval` could be read as granting an AI independent Organizational Authority.

**Reconciliation:** the model states that AI/software are not authority sources; consequential `AM-3` requires explicit approver eligibility and by default AI/software are not sole approvers merely because assigned to a Position. Where no per-instance human approval is intended, the correct design is normally `AM-4` pre-authorized automatic execution approved by competent authority.

This is consistent with the Company Constitution and AC-202.

**Result:** PASS after clarification.

## 7. Iteration 6 — technical access and organizational authority must intersect, not substitute

**Criticism:** later AC-206 access grants may be broader or narrower than Position authority. Without an explicit rule, a privileged credential or admin role could become de facto authority.

**Reconciliation:** AC-203 defines effective executable scope as the intersection:

```text
Position authority envelope
∩ Assignment scope
∩ technical authorization/access
∩ current workflow/data/risk conditions
= maximum executable action
```

Neither technical permission nor organizational delegation alone is sufficient when the other required gate is absent.

**Result:** PASS.

## 8. Iteration 7 — escalation must be an accountable output, not an exception to the model

**Criticism:** delegated operators often fail in practice when ambiguity is treated as an invitation to improvise. A useful model needs explicit mandatory escalation triggers.

**Reconciliation:** AC-203 enumerates triggers covering ROD entry, absent/expired authority, exceeded limits, stale evidence, non-standard commitments, unclear customer rights, risk exceptions, cross-repository obligations, irreversible consequence, technical/authority mismatch and uncertain external-effect outcomes.

Correct escalation is explicitly treated as successful fulfillment of the Position boundary, not as operator failure.

**Result:** PASS.

## 9. Iteration 8 — emergency containment must not wait for Owner while risk acceptance remains reserved

**Criticism:** a strict authority model could make urgent defensive action impossible when the Owner is unavailable, while an overly broad emergency exception could become a back door for continuing unsafe operations.

**Reconciliation:** AC-203 permits later pre-authorized reversible containment such as revocation, isolation, safe shutdown, evidence preservation, degraded mode and tested restoration. Resumption with an unresolved material gap, new liability or changed risk appetite still escalates to the applicable ROD authority.

**Result:** PASS.

## 10. Iteration 9 — boundary completeness and AC-204 handoff

**Criticism:** the model must be useful enough for AC-204 to create real Positions while not pre-creating those Positions or copying the model into customer organizations.

**Reconciliation:** the review traced the downstream sequence:

```text
AC-201 functions
→ AC-202 Reserved Owner boundary
→ AC-203 reusable authority/delegation semantics
→ AC-204 concrete Positions
→ AC-205 Assignments
→ AC-206 access
→ AC-207 continuity
```

AC-203 supplies authority modes, delegation fields, limit dimensions, approval semantics, AI/human eligibility rules, escalation, revocation and evidence requirements, but names no concrete Position and assigns no executor.

Company/Product/OS/customer authority boundaries remain separate. A customer must derive its own delegation model from its authority sources and business rather than copy Arvectum's concrete future Position matrix.

**Result:** PASS.

## 11. Acceptance test

| Test | Result |
|---|---|
| Position authority separated from Principal/Assignment/runtime | PASS |
| five authority modes distinguish preparation, execution, decision, approval and automatic execution | PASS |
| AC-202 ROD catalog is hard negative boundary | PASS |
| no concrete Position created | PASS |
| no Assignment or access grant created | PASS |
| no invented ruble/SLA/data-volume thresholds | PASS |
| delegation envelope fields sufficient for later concrete records | PASS |
| default-deny / no ambient authority explicit | PASS |
| technical authorization cannot substitute for Organizational Authority | PASS |
| approval distinct from recommendation/workflow completion | PASS |
| AI/software not independent authority source | PASS |
| consequential AI path modeled through bounded decision or pre-authorized automatic execution rather than fictitious approval | PASS |
| mandatory escalation triggers explicit | PASS |
| uncertain external-effect retry handled through escalation/reconciliation | PASS |
| emergency containment possible without delegating material risk acceptance | PASS |
| delegation revocation/expiry/staleness handled | PASS |
| parent/child tasks receive no ambient authority inheritance | PASS |
| legal/corporate competence preserved | PASS |
| customer authority/data rights preserved | PASS |
| Product and Arvectum OS governance boundaries preserved | PASS |
| sufficient AC-204 handoff without pre-empting Position Registry | PASS |

## 12. Why the review closes at iteration 9 of 10

The remaining unresolved questions require AC-204–AC-207 or real operating evidence, not another abstract AC-203 iteration:

- what concrete Positions Arvectum actually needs;
- which Positions receive which `AM-*` modes;
- actual financial/customer/risk/data thresholds;
- which Principal class is eligible for which Position/approval class;
- exact technical access grants;
- tested continuity/replacement behavior;
- observed escalation frequency and delegation failure modes.

A tenth desk-review iteration would either repeat the established semantics or fabricate downstream facts.

Stopping at iteration 9 is therefore the evidence-disciplined result.

## 13. Final conclusion

`PASS — material consensus reached at 9 of maximum 10 iterations.`

AC-203 `Proposed 0.9.0` is ready for explicit Owner approval.

Required next governance act:

> explicit Owner approval of the exact reviewed proposal blob `ba89771f7b3ead7f70b0482f06d7d04bc68df2ea`.

After approval, AC-203 may be published as binding Company governance, registered canonically, closed as `Complete / PASS`, and the roadmap may advance to `AC-204 — Initial Position Registry`.
