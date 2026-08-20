# Arvectum Company Canonical Sources Registry

Status: `Active`
Version: `2.3.0`
Updated: `2026-08-21`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`

## 1. Canonical publication model

This registry publication preserves the complete source registry `2.2.0` by immutable git-blob reference and applies the AC-206 registration delta below.

Incorporated prior registry:

- version: `2.2.0`;
- path: `docs/CANONICAL-SOURCES.md`;
- immutable blob SHA: `5373766dd5ecebd1c9d007eb2201be4c8cd24327`.

All source hierarchy, Company/OS/Product authority rules, M0/M1/AC-201–AC-205 registrations, external-source boundaries and Project Source provenance from that incorporated registry remain unchanged unless explicitly superseded here.

Authority remains:

1. applicable law and valid legal/corporate authority within their scope;
2. approved Company governance artifacts and explicit Owner decisions for Company-specific internal matters;
3. applicable canonical Arvectum OS governance where Company relies on OS;
4. product-specific canonical repositories/decisions within product scope;
5. roadmaps as planning coordination rather than independent authority;
6. chats, model memory, generated packs and local copies as non-canonical context unless explicitly promoted.

## 2. AC-206 canonical registration

The following artifacts are added to the active Company canonical/evidence set:

| Source | Status | Role |
|---|---|---|
| `docs/security/COMPANY-DATA-TOOL-CREDENTIAL-ACCESS-BOUNDARY-v1.0.0.md` | Approved `1.0.0` | Binding Company data/tool/credential access-governance baseline; incorporates the exact reviewed `0.9.0` proposal by immutable blob reference |
| `docs/governance/decisions/DECISION-2026-08-21-AC-206-APPROVAL.md` | Approved | Explicit Owner approval record for AC-206 and publication authority for `1.0.0` |
| `docs/security/COMPANY-DATA-TOOL-CREDENTIAL-ACCESS-BOUNDARY.md` | Historical reviewed proposal `0.9.0` | Exact reviewed proposal preserved at blob `0588ab2736e5aa5c2782c572f8e10adf4c65de1e`; incorporated in full by the Approved `1.0.0` publication |
| `docs/reviews/AC-206-COMPANY-ACCESS-BOUNDARY-CROSS-REVIEW.md` | Complete / PASS | AC-206 cross-review, `9 of maximum 10`, validating deny-by-default / least-privilege access, AI-led engineering/commercial bounds, finance/security separation, restricted secret handling and the AC-207 continuity handoff |
| `docs/roadmap/ROADMAP.md` | Active `0.19.0` | Canonical Company planning publication; AC-206 Complete / PASS and AC-207 Current |

## 3. Approved access baseline

AC-206 establishes the Company-level access-governance model for the approved Positions/Assignments:

- data classes `DC-0 — Public`, `DC-1 — Internal`, `DC-2 — Confidential`, `DC-3 — Restricted`;
- technical capability markers `R/W/X/P/K/E` distinct from AC-203 authority modes;
- Company resource classes `RA-01` through `RA-18`;
- deny-by-default and multi-dimensional least privilege;
- Position/Assignment-specific access eligibility ceilings rather than ambient Owner-wide access inheritance;
- meaningful bounded code/build/test access for AI-led `POS-004` without organization-wide admin, bank, signing or unrelated commercial privilege;
- dedicated/scoped sending and prospect-state access for AI commercial work under `POS-002` rather than unrestricted Owner mailbox access;
- separate Finance (`POS-005`) and Security/Risk/Continuity (`POS-006`) access purposes even while the same human Principal currently holds both Assignments;
- restricted handling of reusable secrets and recovery/signing/bank credential material outside public Git and ordinary AI/model context.

## 4. Authority / access / provisioning boundary

Technical access remains distinct from Organizational Authority, legal/corporate power, customer rights and Position/Assignment meaning.

Approval of AC-206 establishes an access-eligibility ceiling and governance rules. It does not itself create an account, issue a credential, authorize a sender, grant bank/signing access, expose customer data, activate `AM-3`/`AM-4` or create an AC-202 `ROD-*` decision right.

Actual provisioning must be attributable, inside the approved ceiling, justified by current Assignment/workflow/data purpose and revocable/recoverable proportionate to consequence.

A restricted owner-controlled operational access/credential register may hold sensitive metadata and secret-location references; secret values themselves are not admitted to the public Company repository and should not be duplicated merely for convenience.

## 5. Current implementation-state boundary

AC-206 does not claim full implementation/readiness. The approved baseline explicitly carries forward unresolved evidence such as incomplete credential inventory, some concentrated Owner-held access, non-uniform service identities for AI, unproven dedicated commercial sender/CRM implementation, untested Company-wide rotation/recovery/revocation and break-glass behavior, and unresolved continuity for signing/local-device gates.

These are downstream implementation/AC-207 evidence requirements, not permission to weaken the access model.

## 6. Current Arvectum OS relevance

Arvectum OS RFC-0003 `Identity, Security, Privacy, Tenant Sovereignty and Portability` remains Accepted `1.0.0` and is compatible with the Company access boundary. It preserves separation among identity, authentication, authorization, Organizational Authority and data governance, deny-by-default/least-privilege behavior and explicit cross-organization access.

AC-206 creates no new Arvectum OS Product Contract, Company-specific platform role, capability lifecycle change or platform authority.

## 7. Current Company planning state

`AC-206 — Company data/tool/credential access boundary baseline` is `Complete / PASS`.

Current canonical Company action:

`AC-207 — Critical-function continuity, replacement and manual fallback baseline`.

AC-207 must test/reason about replacement, recovery, degraded/manual operation and deliberate stop behavior from the approved Position/Assignment/access baseline without transferring Owner/legal/customer authority to a machine or bypassing security controls.
