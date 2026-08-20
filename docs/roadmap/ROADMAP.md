# Arvectum Company Canonical Roadmap

Status: `Active`
Version: `0.19.0`
Created: `2026-08-19`
Updated: `2026-08-21`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Current canonical action: `AC-207 — Critical-function continuity, replacement and manual fallback baseline`

## 1. Canonical publication model

This `0.19.0` publication preserves the complete approved planning substance of roadmap `0.18.0` by immutable git-blob reference and applies only the explicit AC-206 closure / AC-207 transition delta below.

Incorporated prior roadmap:

- prior version: `0.18.0`;
- prior canonical path: `docs/roadmap/ROADMAP.md`;
- immutable blob SHA: `763268dc5d017c30d5978335d73d5017fbd230a1`.

All Phase 0–8 planning, milestone definitions, business-first principles, repository boundaries, P0–P3 sequencing, AC-108 parallel discovery rules and AC-202–AC-205 governance/organization baseline from that incorporated version remain unchanged unless explicitly superseded below.

## 2. AC-206 closure delta

`AC-206 — Company data/tool/credential access boundary baseline` is now `Complete / PASS`.

Binding access-governance publication:

- `docs/security/COMPANY-DATA-TOOL-CREDENTIAL-ACCESS-BOUNDARY-v1.0.0.md` — `Approved 1.0.0`;
- approved reviewed proposal: `docs/security/COMPANY-DATA-TOOL-CREDENTIAL-ACCESS-BOUNDARY.md` — `Proposed 0.9.0`, blob `0588ab2736e5aa5c2782c572f8e10adf4c65de1e`;
- cross-review: `docs/reviews/AC-206-COMPANY-ACCESS-BOUNDARY-CROSS-REVIEW.md` — `9 of maximum 10`, PASS for Owner approval;
- Owner approval: `docs/governance/decisions/DECISION-2026-08-21-AC-206-APPROVAL.md`.

AC-206 establishes:

- deny-by-default / least-privilege access governance;
- `DC-0` through `DC-3` Company access-governance data classes;
- `R/W/X/P/K/E` technical capability markers, distinct from Organizational Authority and AC-203 authority modes;
- `RA-01` through `RA-18` Company resource classes;
- Position/Assignment-specific access eligibility ceilings for the AC-205 executor model;
- meaningful bounded code/build/test access for AI-led Engineering without Owner-wide admin/bank/signing/commercial privilege;
- scoped commercial research/outreach access with dedicated sending identity requirements rather than Owner-general-mailbox access;
- separation of Finance and Security access purposes even where the same human Principal currently holds both Positions;
- prohibition on storing reusable credentials/secrets in the public Company repository or ordinary AI/model context;
- restricted-store metadata, grant/review/revocation/recovery and fail-closed requirements.

AC-206 approval does not itself provision accounts/credentials, create legal/customer authority, activate `AM-3`/`AM-4`, or prove that the target access/recovery model is already implemented.

## 3. Phase 2 current status

| ID | Work item | Status |
|---|---|---|
| `AC-201` | Minimal real organizational/function model | `Complete / PASS` |
| `AC-202` | Reserved Owner Decisions | `Complete / PASS` |
| `AC-203` | Delegated Position authority, approval and escalation model | `Complete / PASS` |
| `AC-204` | Initial Position Registry | `Complete / PASS` |
| `AC-205` | Initial Assignments and executor classification | `Complete / PASS` |
| `AC-206` | Company data/tool/credential access boundary baseline | `Complete / PASS` |
| `AC-207` | Critical-function continuity, replacement and manual fallback baseline | `Current` |
| `AC-208` | Reference-model transferability boundary and operating-model cross-review | `Planned` |

## 4. Current action — AC-207

### AC-207 — Critical-function continuity, replacement and manual fallback baseline

Status: `Current`.

Objective: prove, at a proportionate Company baseline, that the six approved Positions and their critical workflows can survive executor/runtime/device/vendor/service unavailability without inventing authority, bypassing security controls or losing reconstructable organizational meaning.

AC-207 must determine, proportionately to current evidence:

- continuity expectations for each approved Position and the most material Company/workstream dependencies;
- what may continue automatically, what must degrade to a bounded mode and what must stop/fail closed;
- how `POS-004` AI-led Engineering can move between AI models/agents/runtimes or temporarily to human execution without losing workstream state;
- how hybrid Positions preserve decision/evidence state if the current AI adviser/runtime is unavailable;
- how future human sellers or replacement commercial operators can receive reconstructable scoped state rather than relying on Owner memory;
- how outsourced accounting/provider replacement can occur while Company management meaning and source-document access remain recoverable;
- how GitHub/GitVerse/local copies, product repositories and canonical source rules behave during outage/recovery without silently changing authority;
- how credential rotation/recovery/revocation, privileged service identities, local machines/VMs, signing mechanisms and other deliberate gates behave under failure;
- how customer/workstream data and rights remain isolated and reconstructable during replacement/recovery;
- what happens during short Owner unavailability versus materially longer Owner/legal-representation unavailability, without AI or technical operators inheriting `ROD-*` or legal powers;
- which continuity/fallback paths are already evidenced, which are plausible but untested, and which remain unresolved risks requiring later implementation/tests.

AC-207 MUST distinguish continuity from bypass. A deliberate Owner/legal/customer/security gate may legitimately stop an action. Recovery must preserve authority and security rather than granting broader access or decision rights for convenience.

AC-207 MUST NOT fabricate RTO/RPO/SLA values, legal succession instruments, powers of attorney, tested recovery evidence or alternate providers that do not actually exist.

The bounded AC-108 discovery loop continues in parallel as previously authorized P1 market-evidence work.

The next Phase 2 handoff after AC-207 is `AC-208 — Reference-model transferability boundary and operating-model cross-review`.

## 5. Authority reminder

Roadmap status coordinates planning only. It does not itself grant Organizational Authority, approve expenditure, authorize external effect, establish legal/corporate authority, create Product/OS obligations or prove business/customer/production readiness.
