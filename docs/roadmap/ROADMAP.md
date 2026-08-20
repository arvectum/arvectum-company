# Arvectum Company Canonical Roadmap

Status: `Active`
Version: `0.18.0`
Created: `2026-08-19`
Updated: `2026-08-20`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Current canonical action: `AC-206 — Company data/tool/credential access boundary baseline`

## 1. Canonical publication model

This `0.18.0` publication preserves the complete approved planning substance of roadmap `0.17.0` by immutable git-blob reference and applies only the explicit AC-205 closure / AC-206 transition delta below.

Incorporated prior roadmap:

- prior version: `0.17.0`;
- prior canonical path: `docs/roadmap/ROADMAP.md`;
- immutable blob SHA: `2ba6a29b0ac4ea5c60c60034a5e9a2f6e6ed6bf0`.

All Phase 0–8 planning, milestone definitions, business-first principles, repository boundaries, P0–P3 sequencing, AC-108 parallel discovery rules and AC-202–AC-204 governance/organization baseline from that incorporated version remain unchanged unless explicitly superseded below.

## 2. AC-205 closure delta

`AC-205 — Initial Assignments and executor classification` is now `Complete / PASS`.

Binding organizational publication:

- `docs/organization/INITIAL-ASSIGNMENTS-AND-EXECUTOR-CLASSIFICATION-v1.0.0.md` — `Approved 1.0.0`;
- approved reviewed proposal: `docs/organization/INITIAL-ASSIGNMENTS-AND-EXECUTOR-CLASSIFICATION.md` — `Proposed 0.9.0`, blob `b7ce232b460543423497176503b43ceea2a191ae`;
- cross-review: `docs/reviews/AC-205-INITIAL-ASSIGNMENTS-CROSS-REVIEW.md` — `9 of maximum 10`, PASS for Owner approval;
- Owner approval: `docs/governance/decisions/DECISION-2026-08-20-AC-205-APPROVAL.md`.

Approved initial realizations:

1. `POS-001 — Company Executive` — Hybrid: Owner human Position holder + AI advisory/preparation;
2. `POS-002 — Commercial & Customer Lead` — Hybrid: Owner accountable + AI search/research/qualification/drafting/bounded approved outreach + outsourced accounting support + conditional future human seller Assignments;
3. `POS-003 — Portfolio & Product Lead` — Hybrid: Owner judgment/direct proposals + AI synthesis/advice;
4. `POS-004 — Engineering & Release Lead` — AI-led for bounded admitted technical work;
5. `POS-005 — Finance & Obligation Control Lead` — Owner human Position holder + outsourced accounting/tax external-service interface;
6. `POS-006 — Security, Risk & Continuity Lead` — Hybrid: Owner bounded judgment/direct proposals + AI analysis/advice.

Assignments do not create technical access, new legal authority, customer authority, Product/OS authority, `ROD-*` authority, `AM-3` approval or `AM-4` automatic consequential execution.

## 3. Phase 2 current status

| ID | Work item | Status |
|---|---|---|
| `AC-201` | Minimal real organizational/function model | `Complete / PASS` |
| `AC-202` | Reserved Owner Decisions | `Complete / PASS` |
| `AC-203` | Delegated Position authority, approval and escalation model | `Complete / PASS` |
| `AC-204` | Initial Position Registry | `Complete / PASS` |
| `AC-205` | Initial Assignments and executor classification | `Complete / PASS` |
| `AC-206` | Company data/tool/credential access boundary baseline | `Current` |
| `AC-207` | Critical-function continuity, replacement and manual fallback baseline | `Planned` |
| `AC-208` | Reference-model transferability boundary and operating-model cross-review | `Planned` |

## 4. Current action — AC-206

### AC-206 — Company data/tool/credential access boundary baseline

Status: `Current`.

Objective: derive the least-privilege data/tool/credential access required by the approved six Positions and their AC-205 Assignments without turning possession of a credential or system role into Organizational Authority.

AC-206 must determine, proportionately to current evidence:

- which data classes, repositories, accounts, communication channels, customer systems, local environments, signing/payment/security tools and other resources each Position/Assignment actually needs;
- which access is Owner-only, human-Position, AI/software, external-service or shared under controlled conditions;
- how AI-led `POS-004` receives enough engineering access to operate without gaining commercial, financial, customer-acceptance or Owner-reserved authority;
- how AI search/outreach under `POS-002` is bounded by approved campaign scope, data purpose, sending identity, suppression/opt-out rules and commitment limits;
- how outsourced accounting access remains inside its valid professional/legal/service contour and separate from Company Organizational Authority;
- how finance (`POS-005`) and security/risk (`POS-006`) access remain distinct even where the same Owner Principal holds both Assignments;
- credential-holder, recovery, rotation, revocation and least-privilege requirements without placing secret values in the public Company repository;
- fail-closed behavior when required access, authority, customer rights or data-purpose evidence is absent or unclear;
- which access dependencies must pass to AC-207 for continuity/replacement/fallback proof.

AC-206 MUST NOT store reusable secrets, private keys, passwords, token values, bank details or unnecessary personal/customer-confidential payloads in the public repository. It must not create legal powers, customer consent, new Product/OS authority or broaden any approved Assignment/Position authority.

The bounded AC-108 discovery loop continues in parallel as previously authorized P1 market-evidence work.

The next Phase 2 handoff after AC-206 is `AC-207 — Critical-function continuity, replacement and manual fallback baseline`.

## 5. Authority reminder

Roadmap status coordinates planning only. It does not itself grant Organizational Authority, approve expenditure, authorize external effect, establish legal/corporate authority, create Product/OS obligations or prove business/customer/production readiness.
