# DECISION-2026-08-21 — AC-207 Critical-Function Continuity Baseline Approval

Status: `Approved`
Decision date: `2026-08-21`
Decision time: `06:29 +03:00`
Decision class: `Company Governance / Continuity, Replacement and Fallback`
Decision authority: `Owner of Arvectum Company`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-207 — Critical-function continuity, replacement and manual fallback baseline`

## Decision

The Owner explicitly approved the reviewed AC-207 proposal identified as:

- proposal artifact: `docs/operations/CRITICAL-FUNCTION-CONTINUITY-REPLACEMENT-FALLBACK-BASELINE.md`;
- proposal status/version: `Proposed 0.9.0`;
- reviewed proposal blob SHA: `425ab4d83098aa3dbc73925305aa5d9981512818`;
- cross-review: `docs/reviews/AC-207-CRITICAL-FUNCTION-CONTINUITY-CROSS-REVIEW.md`;
- cross-review result: `PASS — material consensus reached at 9 of maximum 10 iterations`.

Owner approval statement in the project conversation:

> Принято AC-207

The statement is treated as explicit approval of the exact reviewed `Proposed 0.9.0` publication identified above.

## Approved continuity baseline

The Owner approves the AC-207 Company-wide continuity model, including:

1. the rule that continuity does not create or transfer Organizational Authority;
2. five continuity modes `CM-0` through `CM-4`: Normal, Bounded Continuity, Degraded, Fail Closed, Recovery / Reconciliation;
3. four continuity-evidence states `CE-0` through `CE-3`, distinguishing unresolved, defined/untested, operationally evidenced and tested/reviewed fallback;
4. explicit separation of runtime replacement, Principal replacement, external-provider replacement, device replacement and legal/corporate succession;
5. minimum continuity-packet requirements for material workstreams;
6. Position-specific continuity behavior for all six approved Positions;
7. bounded AI/runtime replacement for `POS-004 — Engineering & Release Lead` without automatic inheritance of identity, Assignment, access or authority;
8. degraded/manual behavior for hybrid Positions when AI is unavailable and fail-closed behavior where the current human/Owner authority is unavailable;
9. preservation of GitHub canonicality during GitVerse/local-copy fallback and explicit reconciliation after outage;
10. fail-closed treatment of missing signing, payment, legal, customer-rights, trusted-state and security gates;
11. preservation of customer/data isolation and purpose limitations through recovery and replacement;
12. explicit representation of unresolved continuity risks rather than fabricated readiness.

## Authority and readiness boundary

This approval establishes Company continuity-governance semantics and expectations only.

It does not:

- create an alternate Owner, participant, General Director or other legal/corporate representative;
- create a power of attorney, succession instrument or legal-signature right;
- transfer any AC-202 `ROD-01` through `ROD-09` authority to AI, software, another Principal or a technical administrator;
- activate AC-203 `AM-3` or `AM-4`;
- provision credentials, service identities, bank/payment access, signing material or customer-system rights;
- make GitVerse or a local clone canonical automatically;
- create or approve an alternate bank, accountant, hosting provider, supplier or other external provider;
- claim tested RTO/RPO/SLA, disaster recovery, failover readiness or CE-2/CE-3 evidence where none exists;
- override stricter Product, customer, legal or Arvectum OS recovery requirements.

Current `CE-0`/`CE-1` gaps remain real evidence requirements for later implementation and testing.

## Publication actions authorized

1. Publish the unchanged approved normative substance as `docs/operations/CRITICAL-FUNCTION-CONTINUITY-REPLACEMENT-FALLBACK-BASELINE-v1.0.0.md` — `Approved 1.0.0`, incorporating the exact reviewed `0.9.0` proposal by immutable blob reference.
2. Preserve `docs/operations/CRITICAL-FUNCTION-CONTINUITY-REPLACEMENT-FALLBACK-BASELINE.md` as the historical reviewed proposal.
3. Register the approved publication, this approval decision and AC-207 cross-review in the Company canonical-source registry.
4. Close `AC-207` as `Complete / PASS` in the canonical roadmap.
5. Advance the current Company action to `AC-208 — Reference-model transferability boundary and operating-model cross-review`.
6. Refresh repository navigation/state summaries where useful.

## Approval result

`APPROVED — AC-207 Critical-Function Continuity, Replacement and Manual Fallback Baseline`
