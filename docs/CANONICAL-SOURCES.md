# Arvectum Company Canonical Sources Registry

Status: `Active`
Version: `2.4.0`
Updated: `2026-08-21`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`

## 1. Canonical publication model

This registry publication preserves the complete source registry `2.3.0` by immutable git-blob reference and applies the AC-207 registration delta below.

Incorporated prior registry:

- version: `2.3.0`;
- path: `docs/CANONICAL-SOURCES.md`;
- immutable blob SHA: `f8b67bc1ef5cf5067f4760f7510a19e7f670e108`.

All source hierarchy, Company/OS/Product authority rules, M0/M1/AC-201–AC-206 registrations, external-source boundaries and Project Source provenance from that incorporated registry remain unchanged unless explicitly superseded here.

Authority remains:

1. applicable law and valid legal/corporate authority within their scope;
2. approved Company governance artifacts and explicit Owner decisions for Company-specific internal matters;
3. applicable canonical Arvectum OS governance where Company relies on OS;
4. product-specific canonical repositories/decisions within product scope;
5. roadmaps as planning coordination rather than independent authority;
6. chats, model memory, generated packs and local copies as non-canonical context unless explicitly promoted.

## 2. AC-207 canonical registration

The following artifacts are added to the active Company canonical/evidence set:

| Source | Status | Role |
|---|---|---|
| `docs/operations/CRITICAL-FUNCTION-CONTINUITY-REPLACEMENT-FALLBACK-BASELINE-v1.0.0.md` | Approved `1.0.0` | Binding Company critical-function continuity, replacement, degraded/manual fallback and recovery/reconciliation baseline; incorporates the exact reviewed `0.9.0` proposal by immutable blob reference |
| `docs/governance/decisions/DECISION-2026-08-21-AC-207-APPROVAL.md` | Approved | Explicit Owner approval record for AC-207 and publication authority for `1.0.0` |
| `docs/operations/CRITICAL-FUNCTION-CONTINUITY-REPLACEMENT-FALLBACK-BASELINE.md` | Historical reviewed proposal `0.9.0` | Exact reviewed proposal preserved at blob `425ab4d83098aa3dbc73925305aa5d9981512818`; incorporated in full by the Approved `1.0.0` publication |
| `docs/reviews/AC-207-CRITICAL-FUNCTION-CONTINUITY-CROSS-REVIEW.md` | Complete / PASS | AC-207 cross-review, `9 of maximum 10`, validating continuity/degraded/fail-closed/recovery semantics without authority transfer or fabricated readiness |
| `docs/roadmap/ROADMAP.md` | Active `0.20.0` | Canonical Company planning publication; AC-207 Complete / PASS and AC-208 Current |

## 3. Approved continuity baseline

AC-207 establishes:

- continuity modes `CM-0 — Normal`, `CM-1 — Bounded Continuity`, `CM-2 — Degraded`, `CM-3 — Fail Closed`, `CM-4 — Recovery / Reconciliation`;
- evidence states `CE-0` through `CE-3`, distinguishing unresolved, defined/untested, operationally evidenced and tested/reviewed fallback;
- a strict distinction among runtime, Principal, external-provider, device and legal/corporate replacement;
- minimum continuity-packet requirements so material workstream state is reconstructable without one Owner memory, one AI session or one device;
- Position-specific continuity behavior for all six approved Positions;
- replaceability of the AI-led `POS-004` runtime without making a particular model/agent/vendor the Position or automatically transferring Assignment/access/authority;
- degraded/manual continuation for hybrid Positions when AI is unavailable and explicit stop/fail-closed behavior when Owner/legal/customer/security gates are unavailable;
- GitHub/GitVerse/local-copy recovery semantics that preserve canonical authority and require explicit reconciliation;
- explicit unresolved/untested continuity gaps instead of a false disaster-recovery readiness claim.

## 4. Authority / continuity boundary

Continuity is not a source of Organizational Authority.

A runtime, mirror, device, service provider, technical administrator or replacement Principal does not inherit authority merely because the normal executor or dependency is unavailable.

Approved AC-202 `ROD-01` through `ROD-09`, AC-203 delegation/approval semantics, AC-204 Position definitions, AC-205 Assignments and AC-206 access ceilings remain controlling during degraded/recovery operation.

Signing, payment, legal/corporate, customer-rights, trusted-state and security gates may legitimately force `CM-3 — Fail Closed`.

AC-207 creates no legal succession instrument, alternate representative, alternate provider, new credential, `AM-3`/`AM-4` authority, customer consent, RTO/RPO/SLA or tested recovery evidence by implication.

## 5. Current evidence boundary

The approved baseline deliberately preserves multiple `CE-0` and `CE-1` states. Material unresolved or untested areas include extended Owner/legal-representation absence, replacement humans for Owner-held Positions, Company-wide credential recovery/rotation, GitHub/GitVerse restore/reconciliation, actual POS-004 runtime failover, local-device re-bootstrap, commercial operator handoff, accounting-provider replacement, signing-token replacement and customer-data restore/expiry behavior.

These are future implementation/test requirements and do not invalidate the governance baseline; they do prevent stronger continuity/readiness claims.

## 6. Company / Product / Arvectum OS boundary

Product-specific recovery/release evidence remains product-owned. The Company repository does not become a substitute for product implementation truth during outage.

Arvectum OS remains a domain-neutral platform dependency only where an admitted Company/product workflow actually relies on its contracts. OS unavailability does not invalidate Company governance, and product-local/manual fallback must not be mislabeled as OS-governed execution.

Customer/data rights and purpose limitations survive recovery, migration and replacement.

## 7. Current Company planning state

`AC-207 — Critical-function continuity, replacement and manual fallback baseline` is `Complete / PASS`.

Current canonical Company action:

`AC-208 — Reference-model transferability boundary and operating-model cross-review`.

AC-208 must close Phase 2 by reviewing the combined AC-201–AC-207 operating model for internal coherence, business usefulness and transferability as a derivation method/reference pattern rather than treating Arvectum Company's exact organization instance as a universal customer template.
