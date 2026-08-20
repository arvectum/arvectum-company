# Arvectum Company Canonical Roadmap

Status: `Active`
Version: `0.16.0`
Created: `2026-08-19`
Updated: `2026-08-20`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Current canonical action: `AC-204 — Initial Position Registry`

## 1. Canonical publication model

This `0.16.0` publication preserves the complete approved planning substance of roadmap `0.15.0` by immutable git-blob reference and applies only the explicit AC-203 closure / AC-204 transition delta below.

Incorporated prior roadmap:

- prior version: `0.15.0`;
- prior canonical path: `docs/roadmap/ROADMAP.md`;
- immutable blob SHA: `51c0cf4577993d4416d708265383a9bbe098b224`.

All Phase 0–8 planning, milestone definitions, business-first principles, repository boundaries, P0–P3 sequencing, AC-108 parallel discovery rules and AC-202 governance baseline from that incorporated version remain unchanged unless explicitly superseded below.

## 2. AC-203 closure delta

`AC-203 — Delegated Position authority, approval and escalation model` is now `Complete / PASS`.

Binding governance publication:

- `docs/governance/DELEGATED-POSITION-AUTHORITY-MODEL-v1.0.0.md` — `Approved 1.0.0`;
- approved reviewed proposal: `docs/governance/DELEGATED-POSITION-AUTHORITY-MODEL.md` — `Proposed 0.9.0`, blob `ba89771f7b3ead7f70b0482f06d7d04bc68df2ea`;
- cross-review: `docs/reviews/AC-203-DELEGATED-POSITION-AUTHORITY-CROSS-REVIEW.md` — `9 of maximum 10`, PASS for Owner approval;
- Owner approval: `docs/governance/decisions/DECISION-2026-08-20-AC-203-APPROVAL.md`.

AC-203 establishes five authority modes (`AM-0` through `AM-4`), executor-neutral Position authority, deny-by-default delegation, explicit approval semantics, fail-closed/escalation behavior and the rule that effective execution is bounded by the intersection of Position authority, Assignment scope, technical access and current workflow/data/risk conditions.

Approved AC-202 `ROD-01` through `ROD-09` remain a hard negative boundary. AC-203 creates no concrete Position, Assignment, access grant, numeric threshold, legal power, customer authority or Arvectum OS lifecycle effect.

## 3. Phase 2 current status

| ID | Work item | Status |
|---|---|---|
| `AC-201` | Minimal real organizational/function model | `Complete / PASS` |
| `AC-202` | Reserved Owner Decisions | `Complete / PASS` |
| `AC-203` | Delegated Position authority, approval and escalation model | `Complete / PASS` |
| `AC-204` | Initial Position Registry | `Current` |
| `AC-205` | Initial Assignments and executor classification | `Planned` |
| `AC-206` | Company data/tool/credential access boundary baseline | `Planned` |
| `AC-207` | Critical-function continuity, replacement and manual fallback baseline | `Planned` |
| `AC-208` | Reference-model transferability boundary and operating-model cross-review | `Planned` |

## 4. Current action — AC-204

### AC-204 — Initial Position Registry

Status: `Current`.

Objective: derive the smallest evidence-backed set of durable Company Positions from the AC-201 function model, current workload/accountability/control needs and approved AC-202/AC-203 authority boundaries.

AC-204 must determine, proportionately to current evidence:

- which AC-201 responsibilities require a distinct durable Position rather than remaining bundled;
- where one Position may legitimately span several functions at the Company's current scale;
- where one function requires more than one Position because accountability, authority, workload or control separation genuinely differs;
- each Position's purpose and business reason for existence;
- accountable outputs/outcomes;
- function/responsibility coverage;
- authority modes available to the Position under AC-203 and explicit exclusions under AC-202;
- major handoffs and escalation destinations;
- whether the Position is currently required, conditional/future or not justified;
- what evidence would justify later splitting, merging or retiring the Position.

AC-204 MUST NOT mechanically create one Position per AC-201 function and MUST NOT create familiar departments or fake headcount for organizational completeness.

AC-204 must remain executor-neutral. It MUST NOT assign named humans, AI agents, software services or runtimes. Those remain AC-205 Assignments. It also must not create credentials or technical access; those remain AC-206.

The bounded AC-108 discovery loop continues in parallel as previously authorized P1 market-evidence work.

The next Phase 2 handoff after AC-204 is `AC-205 — Initial Assignments and executor classification`.

## 5. Authority reminder

Roadmap status coordinates planning only. It does not itself grant Organizational Authority, approve expenditure, authorize external effect, establish legal/corporate authority, create Product/OS obligations or prove business/customer/production readiness.
