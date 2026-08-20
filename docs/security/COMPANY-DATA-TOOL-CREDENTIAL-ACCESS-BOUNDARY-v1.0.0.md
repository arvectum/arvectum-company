# AC-206 — Company Data / Tool / Credential Access Boundary Baseline

Status: `Approved`
Version: `1.0.0`
Approved: `2026-08-21`
Published: `2026-08-21`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-206 — Company data/tool/credential access boundary baseline`
Approval: `docs/governance/decisions/DECISION-2026-08-21-AC-206-APPROVAL.md`
Cross-review: `docs/reviews/AC-206-COMPANY-ACCESS-BOUNDARY-CROSS-REVIEW.md`
Approved proposal: `Proposed 0.9.0`, blob `0588ab2736e5aa5c2782c572f8e10adf4c65de1e`

## 1. Approval publication

This document is the canonical Approved publication of AC-206 `1.0.0`.

The Owner-approved normative substance is the complete reviewed proposal preserved at:

`docs/security/COMPANY-DATA-TOOL-CREDENTIAL-ACCESS-BOUNDARY.md`

and identified immutably by git blob SHA:

`0588ab2736e5aa5c2782c572f8e10adf4c65de1e`

The proposal is incorporated into this Approved publication **in full by immutable content reference**. No normative substance of the reviewed proposal is changed by this publication.

Owner approval is recorded in:

`docs/governance/decisions/DECISION-2026-08-21-AC-206-APPROVAL.md`.

## 2. Approved access baseline

AC-206 `1.0.0` establishes the binding Company-level access-governance baseline for the six approved Positions and AC-205 executor realizations.

The approved model is deny-by-default and least-privilege. Technical access is explicitly distinct from Organizational Authority, legal/corporate power, Assignment, customer/data rights and AC-203 authority modes.

The binding data classes are:

- `DC-0 — Public`;
- `DC-1 — Internal`;
- `DC-2 — Confidential`;
- `DC-3 — Restricted`.

The binding technical capability markers are:

- `R` — read/observe;
- `W` — create/update ordinary content;
- `X` — execute approved technical operation;
- `P` — privileged administration/access-management capability;
- `K` — access to reusable secret/key material itself;
- `E` — technical capability to cause an external effect.

These markers describe technical reach only; they do not themselves grant decision or approval authority.

## 3. Position / executor access boundary

The approved access ceilings preserve the AC-205 realization:

- `POS-001` hybrid Company Executive: AI may read Company/product evidence and perform bounded Company-repository drafting/state-publication mechanics, but receives no default Owner-wide admin, secret, bank, signing, general-mailbox or unrelated customer access;
- `POS-002` hybrid Commercial & Customer: AI may perform public research, scoped prospect/CRM work and bounded approved outreach through a dedicated/scoped commercial identity; it receives no autonomous commitment, bank/signing, product-write or Owner-general-mailbox access;
- `POS-003` hybrid Portfolio & Product: AI may read relevant product/CI evidence and prepare/synchronize Company portfolio proposals/state without thereby gaining product implementation, production, secret or investment authority;
- `POS-004` AI-led Engineering & Release: AI may receive meaningful bounded repository/worktree/build/test execution access required for `AM-0`/`AM-1`/`AM-2` technical work, but no default organization-wide admin, raw reusable secret access, bank/signing/commercial privilege or ambient production/customer-system access;
- `POS-005` Finance & Obligation Control: management-finance access remains distinct from bank/payment/signature authority; detailed statutory/accounting work remains in the outsourced accounting contour and no standing AI access to detailed bank/accounting data is created by AC-206;
- `POS-006` Security, Risk & Continuity: the human Assignment may hold justified security/admin/recovery capability in the proper capacity, while AI receives minimized evidence/configuration for analysis and no default raw-secret or privileged-admin reach.

Finance and Security remain separate access purposes and evidence boundaries even while the same current human Principal holds both Assignments.

## 4. Secret and restricted-data boundary

Reusable passwords, API tokens, private keys, recovery codes, e-signature PIN/key material, bank authentication/signing secrets and equivalent `DC-3` material MUST NOT be stored in the public Company repository or ordinary AI/model context.

Where a future machine workflow legitimately requires secret use, the preferred design is controlled runtime injection or another protected mechanism that allows the workload to use the credential without exposing its reusable value to the model/operator where feasible.

A restricted owner-controlled access/credential register may record safe operational metadata and a reference to the secret-storage location, but should not duplicate the secret value merely for convenience.

## 5. Provisioning boundary

Approval of AC-206 establishes an access-eligibility ceiling. It does **not** itself:

- create an account or service identity;
- issue a token or password;
- add repository collaboration rights;
- authorize a mailbox or CRM sender;
- grant bank/payment/signing access;
- expose customer-confidential data;
- install a secret on a runtime/device;
- create customer consent or legal authority;
- broaden a Position or Assignment;
- activate `AM-3` or `AM-4`.

Actual provisioning must remain attributable, inside the approved ceiling, justified by the current Assignment/workflow, and revocable/recoverable proportionate to consequence.

## 6. Current implementation-state honesty

This approval does not claim that the target access model is already fully implemented.

Current gaps preserved for downstream implementation/AC-207 include incomplete credential inventory, concentration of some Owner-held credentials, non-uniform AI/service identities, unproven dedicated commercial sender/CRM implementation, untested Company-wide rotation/recovery/revocation and break-glass behavior, and unresolved continuity for physical signing/local-device gates.

These gaps are evidence requirements, not permission to weaken the approved access boundary.

## 7. Company / Product / Arvectum OS boundary

Product-specific repository/branch/release/security rules may narrow the Company ceiling and remain canonical within product scope.

Customer-system rights and data-purpose rules remain customer-scoped.

Arvectum OS RFC-0003 remains the applicable domain-neutral platform security contract where Company workflows rely on OS, but AC-206 creates no OS-specific Company role, Product Contract, capability lifecycle change or platform authority.

## 8. Cross-review and approval evidence

Cross-review:

- `docs/reviews/AC-206-COMPANY-ACCESS-BOUNDARY-CROSS-REVIEW.md`;
- iterations: `9 of maximum 10`;
- result: `Complete / PASS for Owner approval`.

Approved proposal:

- `docs/security/COMPANY-DATA-TOOL-CREDENTIAL-ACCESS-BOUNDARY.md`;
- status/version: `Proposed 0.9.0`;
- immutable blob SHA: `0588ab2736e5aa5c2782c572f8e10adf4c65de1e`.

Owner approval:

- `docs/governance/decisions/DECISION-2026-08-21-AC-206-APPROVAL.md` — `Approved`.

## 9. Approval result

`AC-206 — Company data/tool/credential access boundary baseline` is `Complete / PASS` and binding as Company access governance within its declared scope.

The next canonical Company action is:

`AC-207 — Critical-function continuity, replacement and manual fallback baseline`.
