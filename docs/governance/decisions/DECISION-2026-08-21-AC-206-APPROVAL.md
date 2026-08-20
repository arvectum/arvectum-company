# DECISION-2026-08-21 — AC-206 Company Access Boundary Approval

Status: `Approved`
Decision date: `2026-08-21`
Decision time: `00:08 +03:00`
Decision class: `Company Governance / Data, Tool and Credential Access Boundary`
Decision authority: `Owner of Arvectum Company`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-206 — Company data/tool/credential access boundary baseline`

## Decision

The Owner explicitly approved the reviewed AC-206 proposal identified as:

- proposal artifact: `docs/security/COMPANY-DATA-TOOL-CREDENTIAL-ACCESS-BOUNDARY.md`;
- proposal status/version: `Proposed 0.9.0`;
- reviewed proposal blob SHA: `0588ab2736e5aa5c2782c572f8e10adf4c65de1e`;
- cross-review: `docs/reviews/AC-206-COMPANY-ACCESS-BOUNDARY-CROSS-REVIEW.md`;
- cross-review result: `PASS — material consensus reached at 9 of maximum 10 iterations`.

Owner approval statement in the project conversation:

> Принято AC-206

The statement is treated as explicit approval of the exact reviewed `Proposed 0.9.0` publication identified above.

## Approved access-governance baseline

The Owner approves the AC-206 Company-level deny-by-default / least-privilege access model, including:

1. separation of identity, Assignment, Organizational Authority, technical access, legal/corporate power and customer/data rights;
2. `DC-0` through `DC-3` Company access-governance data classes;
3. `R/W/X/P/K/E` technical capability markers, explicitly distinct from AC-203 authority modes;
4. the `RA-01` through `RA-18` Company resource-class model;
5. Position/Assignment-specific access eligibility ceilings for the approved AC-205 executor realizations;
6. meaningful bounded repository/build/test access for AI-led `POS-004` without Owner-wide admin, bank, signing or unrelated customer/commercial privilege;
7. dedicated/scoped commercial sending and prospect-state access for AI work under `POS-002`, subject to campaign/data-purpose/message/frequency/suppression boundaries;
8. separation of `POS-005` finance/obligation access from `POS-006` security/risk/continuity access even while the same human Principal currently occupies both Positions;
9. external accounting/tax access remaining in its professional/legal/service contour;
10. prohibition on storing reusable secrets or restricted credential values in the public Company repository or ordinary AI/model context;
11. use of a restricted owner-controlled access/credential register for live sensitive metadata and secret-location references;
12. attributable grant/review/revocation/recovery semantics and fail-closed behavior when authority, access basis, customer rights or data purpose are unclear.

## Authority and implementation boundary

This decision approves the access-governance **eligibility ceiling and control model**. It does not itself provision technical access.

It does not:

- issue, disclose or rotate any password, API token, private key, recovery code or signing material;
- grant a bank/payment permission, qualified electronic-signature power or legal/corporate representation right;
- create customer consent or customer-system rights;
- broaden any AC-204 Position or AC-205 Assignment;
- create any AC-202 `ROD-01` through `ROD-09` authority;
- activate AC-203 `AM-3` or `AM-4`;
- turn a repository/admin credential into Organizational Authority;
- authorize cross-customer data reuse or ambient cross-organization access;
- create a new Arvectum OS Product Contract, capability lifecycle change or platform authority;
- claim that the current credential inventory, service identities, recovery, rotation, break-glass or continuity controls are already fully implemented/tested.

Actual provisioning remains a separate attributable action inside this approved ceiling and applicable product/customer/legal/security controls. Continuity, replacement and recovery proof remains AC-207.

## Publication actions authorized

1. Publish the unchanged approved normative substance as `docs/security/COMPANY-DATA-TOOL-CREDENTIAL-ACCESS-BOUNDARY-v1.0.0.md` — `Approved 1.0.0`, incorporating the exact reviewed `0.9.0` proposal by immutable blob reference.
2. Preserve `docs/security/COMPANY-DATA-TOOL-CREDENTIAL-ACCESS-BOUNDARY.md` as the historical reviewed proposal.
3. Register the approved publication, this approval decision and AC-206 cross-review in the Company canonical-source registry.
4. Close `AC-206` as `Complete / PASS` in the canonical roadmap.
5. Advance the current Company action to `AC-207 — Critical-function continuity, replacement and manual fallback baseline`.
6. Refresh repository navigation/state summaries where useful.

## Approval result

`APPROVED — AC-206 Company Data / Tool / Credential Access Boundary Baseline`
