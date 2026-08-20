# AC-206 — Company Data / Tool / Credential Access Boundary Cross-Review

Status: `Complete / PASS for Owner approval`
Review date: `2026-08-20`
Iterations completed: `9 of maximum 10`
Result: `PASS — the proposal defines a deny-by-default least-privilege Company access boundary for the six approved Positions and AC-205 executor classes, keeps technical access separate from Organizational Authority, permits AI-led engineering and bounded commercial automation without exposing bank/signing/credential authority, preserves customer/product/OS boundaries, keeps outsourced accounting in its external professional contour, and exposes current credential/recovery gaps without storing secrets or claiming implementation readiness`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-206 — Company data/tool/credential access boundary baseline`
Reviewed artifact: `docs/security/COMPANY-DATA-TOOL-CREDENTIAL-ACCESS-BOUNDARY.md`
Reviewed publication: `Proposed 0.9.0`
Reviewed blob SHA: `TO_BE_VERIFIED_AFTER_READBACK`
Maximum review iterations: `10`
Approval status: `Pending explicit Owner approval of the exact reviewed proposal`
Arvectum OS main re-checked: `608a796be255f2b2d350f75fb2a72af411cb615d`
Relevant OS contract: RFC-0003 `Accepted 1.0.0`

## 1. Review purpose

The review tests whether AC-206 creates a practical access boundary for the AC-205 Assignment model without falling into one of the two common failures:

- **under-control** — AI/services receive Owner-wide credentials or broad technical access because they are capable of using them;
- **over-control** — every technical action requires the Owner, making AI-led engineering and bounded commercial automation impossible in practice.

The review also tests whether the public Company repository can safely hold the access-governance model without becoming a credential inventory or attack-surface disclosure.

## 2. Iteration 1 — access, authority and legal power must remain separate

**Criticism:** AC-205 now assigns the Owner to several Positions and makes POS-004 AI-led. If AC-206 equates account possession with Position authority, a GitHub token, mailbox credential or bank login could silently become a decision right.

**Reconciliation:** the proposal explicitly preserves:

```text
Principal identity
≠ Position Assignment
≠ Position decision authority
≠ technical authorization/access
≠ legal/corporate power
≠ customer/data rights
```

It also retains AC-203's intersection rule and defines technical capability markers (`R/W/X/P/K/E`) as orthogonal to authority modes.

**Result:** PASS.

## 3. Iteration 2 — the access model itself must be safe in a public repository

**Criticism:** an access baseline can accidentally become a high-value attack map by listing usernames, account identifiers, recovery channels, endpoints, token locations or credential details.

**Reconciliation:** AC-206 stores only resource classes, Position/Assignment boundaries and safe metadata schemas. It explicitly prohibits reusable secrets, keys, passwords, recovery codes, bank details and unnecessary sensitive access metadata in the public repository.

A future live access/credential inventory must reside in an owner-controlled restricted store. The proposal also states that the restricted register should reference secret storage without embedding the secret value.

**Result:** PASS.

## 4. Iteration 3 — current Owner concentration must not defeat capacity separation

**Criticism:** one natural person currently holds POS-001, POS-002, POS-003, POS-005 and POS-006 and may separately act as Owner/participant/General Director. Creating separate technical accounts per Position immediately may be artificial, but ignoring capacity separation would destroy auditability.

**Reconciliation:** AC-206 does not force fake account proliferation. Instead it requires material actions to identify the capacity/context in which the current human acted. Bank/signing/root-admin capability is not attributed to a Position merely because the current Owner possesses it.

This is compatible with later separation: a future Principal can receive only the access required by the Position Assignment rather than inheriting the current Owner's aggregate reach.

**Result:** PASS.

## 5. Iteration 4 — AI-led Engineering needs real write/execute access without Owner-wide privilege

**Criticism:** POS-004 cannot be meaningfully AI-led if the AI is restricted to read-only recommendations. Conversely, giving the AI the Owner's organization-wide GitHub/admin credentials, CI secrets, signing token or production controls would violate least privilege and AC-203.

**Reconciliation:** the proposal grants the AI engineering Principal/workload class:

- `R/W` to product repositories/worktrees in the active Assignment/workstream;
- `R/W/X` to approved engineering work directories and test environments;
- `R/X` plus bounded artifact/build operations in CI/CD;
- no default repository/org `P` administration;
- no raw `K` secret access;
- no bank/signing/commercial mailbox privilege;
- no ambient production/customer-system access;
- no consequential production release outside an already approved execution class.

Secret-bearing automation is modeled through controlled runtime injection so the workload can use a secret without exposing its raw value to the AI/model where possible.

Product-specific branch/release/security policy remains controlling within product scope; Company access eligibility does not override a stricter product path.

**Result:** PASS.

## 6. Iteration 5 — AI commercial search/outreach must not become an unrestricted sales mailbox or autonomous commitment engine

**Criticism:** POS-002 explicitly intends AI search and outbound. If the AI uses the Owner's general mailbox or can send arbitrary messages, technical sending capability can create privacy, reputation and commitment risk.

**Reconciliation:** AC-206 requires a dedicated/scoped commercial sending identity and campaign boundary. The AI may research, maintain scoped prospect state and send only inside an explicitly approved target/message/frequency/follow-up envelope. Recipient suppression/opt-out and unclear data-purpose cases stop or escalate.

The AI is denied bank/signing, product write, infrastructure admin and the Owner's unrestricted mailbox, and cannot invent price, SLA, warranty, scope or legal/data promises.

**Result:** PASS.

## 7. Iteration 6 — Finance/accounting access must not create payment authority or duplicate accounting truth

**Criticism:** POS-005 is Owner-led with outsourced accounting. A naive access model could either give the accounting provider Company-wide authority or let POS-005's management-finance role silently imply payment/signature authority.

**Reconciliation:** AC-206 distinguishes:

- POS-005 management visibility and interpretation;
- the external accounting/tax provider's professional/statutory contour;
- bank/payment and signature capability as separate high-consequence technical/legal gates.

No standing AI access to detailed bank/accounting data is created. The accounting provider receives no Company Organizational Authority or unrelated customer/security/repository privilege by implication.

**Result:** PASS.

## 8. Iteration 7 — Finance and Security must remain separate in access as well as in the Position Registry

**Criticism:** the Owner currently occupies both POS-005 and POS-006. If the same credential inventory or admin model treats them as one operational role, AC-204's Owner-requested separation would be cosmetic.

**Reconciliation:** AC-206 assigns different access purposes and evidence boundaries:

- POS-005 consumes accounting/bank/obligation evidence for management decisions;
- POS-006 consumes access/security/incident/recovery metadata and may hold legitimate security administration capability;
- POS-006 authority does not include financial approval;
- POS-005 does not receive security/IAM administration merely because the same human currently holds both Assignments.

A future reassignment can therefore split the two Positions without redesigning the access semantics.

**Result:** PASS.

## 9. Iteration 8 — customer isolation, secrets and machine identities need an explicit hard boundary

**Criticism:** a hybrid AI company is especially vulnerable to cross-customer data bleed, reused Owner tokens and shared anonymous machine accounts.

**Reconciliation:** AC-206 establishes:

- four data classes (`DC-0` through `DC-3`);
- `DC-3` secrets excluded from prompts/ordinary AI context;
- customer/workstream access scoped by purpose and organization;
- no ambient cross-customer access;
- service/workload identities preferred over shared Owner credentials;
- no shared anonymous machine identity for consequential work where attribution would be lost;
- revocation without deleting historical attribution.

This aligns with Accepted OS RFC-0003 without importing Company-specific roles into OS.

**Result:** PASS.

## 10. Iteration 9 — continuity, privileged access and current implementation gaps must be represented honestly

**Criticism:** an elegant matrix could falsely imply that least privilege, service identities, credential inventory, break-glass and recovery are already implemented and tested.

**Reconciliation:** AC-206 explicitly separates **access eligibility ceiling** from actual provisioning and records ten current gaps, including incomplete credential inventory, concentrated Owner credentials, non-uniform AI identities/tokens, unproven dedicated outreach identity, untested accounting replacement and untested Company-wide recovery/break-glass behavior.

Human-controlled high-consequence capabilities remain protected at the current baseline. The model does not claim that one human must remain the permanent recovery path; AC-207 must test how recovery/continuity can improve without transferring Organizational Authority to a machine or bypassing lawful/security gates.

The current lack of `AM-3` also prevents an AI/system from approving its own privileged access expansion. Routine access inside the approved Assignment ceiling can be provisioned only with attributable human provisioning/authorization under the current governance path; future delegation requires an explicit approved change.

**Result:** PASS.

## 11. Acceptance test

| Test | Result |
|---|---|
| access is separate from Organizational Authority | PASS |
| access is separate from legal/corporate power | PASS |
| deny-by-default and least privilege explicit | PASS |
| public repository contains no secret values | PASS |
| restricted credential-register architecture defined | PASS |
| data classes defined without claiming statutory classification | PASS |
| technical capability markers separated from AC-203 authority modes | PASS |
| AC-206 approval does not provision an account/credential | PASS |
| current Owner multi-Position concentration handled without merging capacities | PASS |
| POS-001 AI can perform bounded repository/state work without approval authority | PASS |
| POS-002 AI outreach gets dedicated bounded sending/data path | PASS |
| future seller access is scoped and not active before Assignment | PASS |
| POS-003 AI gets cross-product evidence read without product implementation authority | PASS |
| POS-004 AI-led Engineering receives meaningful code/build execution access | PASS |
| POS-004 denied Owner-wide admin/bank/signing/general-mailbox privilege | PASS |
| CI secret-use pattern avoids model exposure where possible | PASS |
| product-specific access/release rules may narrow Company ceiling | PASS |
| POS-005 management finance separated from bank/signature authority | PASS |
| outsourced accounting remains external professional contour | PASS |
| POS-005 and POS-006 remain separately reconstructable | PASS |
| POS-006 AI advice does not receive default raw secrets/admin privilege | PASS |
| customer isolation and purpose limitation explicit | PASS |
| no cross-customer learning/data reuse by default | PASS |
| service/workload identities preferred over shared Owner token | PASS |
| grant/review/revocation semantics explicit | PASS |
| break-glass creates no Organizational Authority | PASS |
| Product and OS boundaries preserved | PASS |
| no new OS dependency/lifecycle/readiness claim | PASS |
| current access/recovery gaps stated instead of hidden | PASS |
| AC-207 continuity handoff is concrete | PASS |

## 12. Why the review closes at iteration 9 of 10

The remaining material questions are implementation/recovery evidence rather than defects in the AC-206 semantic boundary:

- the actual current account/credential inventory;
- which current tokens are over-broad and can be replaced by scoped service identities;
- concrete sender/CRM implementation for AI commercial outreach;
- exact per-product GitHub/CI permissions and branch protections;
- restricted-store tool selection and migration of credential metadata;
- tested rotation/recovery/revocation procedures;
- tested signing-token/local-device continuity;
- tested customer-access expiry/handover;
- actual incident evidence showing whether the access model is too broad or too restrictive.

Those questions require AC-207 and/or concrete implementation work. A tenth desk-only iteration would either repeat the current controls or fabricate account/credential facts that have not been inventoried.

Stopping at iteration 9 is therefore evidence-disciplined.

## 13. Final conclusion

`PASS — material consensus reached at 9 of maximum 10 iterations.`

AC-206 `Proposed 0.9.0` is ready for explicit Owner approval after read-back verification of the reviewed blob SHA.

Approval is required because the baseline materially constrains Company access and future Principal provisioning, while the actual account/credential grants remain separate implementation records.

After approval, AC-206 may be published as binding Company access governance, registered canonically, closed as `Complete / PASS`, and the roadmap may advance to:

`AC-207 — Critical-function continuity, replacement and manual fallback baseline`.