# AC-104 — Owner Workload, Manual Work and Bottleneck Map Cross-Review

Status: `Complete / PASS`
Review date: `2026-08-20`
Iterations completed: `8 of maximum 10`
Result: `PASS — Owner control is separated from Owner execution; the dominant interpretation, exception, priority and local-gate bottlenecks are exposed without inventing future Positions or time-sheet data`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-104 — Owner workload, manual work and bottleneck map`
Reviewed artifact: `docs/business/OWNER-WORKLOAD-MANUAL-WORK-BOTTLENECK-MAP.md`
Reviewed publication: `0.1.0`
Maximum review iterations authorized by Owner: `10`

## 1. Review purpose

This cross-review tests whether AC-104 identifies real Owner workload and bottlenecks well enough to support continuity/risk work and Phase 2 operating-model design, while preserving Owner authority and avoiding false precision or premature organizational design.

## 2. Review lenses

The review uses twelve functional perspectives:

1. Owner / Founder;
2. General Director;
3. Commercial / Commitment Control;
4. Delivery / Operations;
5. Customer Success / Support;
6. Product / Portfolio;
7. Finance / Management Control;
8. Technology / Architecture;
9. Security / Data / Sovereignty;
10. Legal / Corporate Authority;
11. Risk / Continuity;
12. Organizational Design / AI Workforce.

These are review lenses only. They do not create Positions, delegation or independent authority.

## 3. Iteration 1 — False precision and workload evidence

**Primary lenses:** Owner, Finance, Organizational Design.

**Criticism:** A bottleneck map could become misleading if it assigns hours, percentages or utilization without a historical time-sheet or instrumentation baseline.

**Reconciliation:** The artifact explicitly refuses to fabricate quantitative workload. It uses evidence classes and qualitative workload categories (`Reserved`, `Owner-dependent`, `Owner-executed`, `Owner-gated`) and creates a prospective measurement baseline for future work.

**Result:** PASS after correction.

## 4. Iteration 2 — Owner control versus Owner execution

**Primary lenses:** Owner, General Director, Governance, Organizational Design.

**Criticism:** The initial conceptual map risked treating every task performed by the Owner as an automation target, which would conflict with the owner-operated governance model.

**Reconciliation:** The artifact separates residual/reserved authority from execution load. Strategy, capital allocation, material risk, material commitments and governance changes remain presumptively Owner-reserved until AC-202 or later explicit delegation says otherwise.

The optimization target is preparation, bounded execution and exception routing around the Owner decision — not removal of the decision authority itself.

**Result:** PASS.

## 5. Iteration 3 — Customer lifecycle workload

**Primary lenses:** Commercial, Delivery, Customer Success.

**Criticism:** AC-103 identified likely Owner dependency across scoping, customer communication, rework and acceptance, but AC-104 needed to show the specific workload mechanism rather than repeat the lifecycle map.

**Reconciliation:** The workload map now identifies semantic interpretation, defect/scope/change classification, customer-context continuity and acceptance judgment as distinct Owner dependencies. It also records that open-ended correction becomes a scale bottleneck when no explicit acceptance/change boundary exists.

**Result:** PASS.

## 6. Iteration 4 — Coding is not the main organizational bottleneck

**Primary lenses:** Technology, Product, Operations, Owner.

**Criticism:** Because Arvectum uses AI coding and repository automation heavily, AC-104 could incorrectly identify raw implementation capacity as the primary Owner problem.

**Reconciliation:** The artifact distinguishes implementation execution from work sequencing, technical/business interpretation, repository ownership decisions and exception acceptance. It concludes that the dominant structural constraint is the universal-interpreter/priority queue, not raw coding throughput.

This conclusion is qualitative and evidence-backed; no unsupported throughput number is claimed.

**Result:** PASS.

## 7. Iteration 5 — Local, credential and physical execution gates

**Primary lenses:** Operations, Security, Risk, Technology.

**Criticism:** The map needed to capture a recurring pattern where cloud/AI/repository work is complete but progress still waits for a local machine, physical token, user-device check, credential-bound environment or human external action.

**Reconciliation:** `MW-3` and `B-5` now treat local/credential-bound execution as a separate `Owner-gated` class. The artifact distinguishes justified security/authority gates from accidental technical dependence and hands continuity/access questions to AC-105, AC-206 and AC-207.

**Result:** PASS.

## 8. Iteration 6 — Portfolio and cross-repository context switching

**Primary lenses:** Product, Portfolio, Architecture, Owner.

**Criticism:** The Owner's workload spans Company, OS and multiple product repositories. A client-only analysis would understate the bottleneck created by repeated cross-repository prioritization and ownership reconciliation.

**Reconciliation:** The artifact adds the priority/portfolio switching bottleneck, repository orchestration workload and explicit boundary decisions around customer-specific logic, product capability, module candidate and OS responsibility.

It does not turn this into a centralized technical mega-role or invent a future CTO/Product department.

**Result:** PASS.

## 9. Iteration 7 — Reserved approval versus clerical synchronization

**Primary lenses:** Governance, Legal, Operations, Owner.

**Criticism:** Governance workflows can become Owner-heavy because the same Principal both approves the material decision and performs low-risk preparation/publication/status synchronization around it.

**Reconciliation:** `MW-5` separates Owner approval from evidence assembly, draft preparation, canonical publication mechanics and follow-through. The future direction is delegated/automated preparation around an explicit authorized Principal action, preserving the rule that AI execution is not Owner approval.

**Result:** PASS.

## 10. Iteration 8 — Delegation candidates without premature Positions

**Primary lenses:** Organizational Design, AI Workforce, Risk, all remaining lenses.

**Criticism:** A workload map is not complete if it merely says "delegate more", but naming a future org chart or AI agents now would violate the roadmap sequence and organization-first rule.

**Reconciliation:** The artifact identifies bounded candidate work classes — intake normalization, discovery preparation, evidence assembly, routine decomposition, QA, first-pass issue classification, state synchronization, draft customer updates, support triage, management-report preparation and runbook execution — while explicitly stating that they are not approved Assignments.

The later path remains:

`function → Position → authority/workflow/evidence → Assignment → runtime`.

**Result:** PASS.

## 11. Acceptance test

| Test | Result |
|---|---|
| distinguishes Owner control from Owner execution | PASS |
| separates presumptively reserved authority from current operational dependency | PASS |
| maps Owner workload across customer, product, portfolio, governance and local execution | PASS |
| identifies interpretation/priority/exception bottlenecks rather than blaming coding capacity alone | PASS |
| captures local/credential-bound blocking | PASS |
| captures customer-context continuity and open-ended rework risk | PASS |
| captures state reconstruction and context-switching overhead | PASS |
| does not fabricate historical hours, percentages or ROI | PASS |
| creates a prospective workload measurement baseline | PASS |
| identifies delegation/automation candidates without approving them | PASS |
| does not invent Positions, headcount or AI agents | PASS |
| preserves Company/Product/OS and customer-authority boundaries | PASS |
| creates actionable handoff to AC-105 | PASS |
| provides useful evidence for AC-201–AC-207 and later AC-601 selection | PASS |

## 12. Why the review closes at iteration 8 of 10

The Owner authorized a maximum of ten iterations, not a requirement to consume all ten.

After iteration 8, the remaining unanswered questions are intentionally owned by later roadmap items rather than defects in AC-104:

- exact material continuity/dependency/fallback risk → AC-105;
- flagship ICP and buyer → AC-107;
- market-validation operating burden → AC-108;
- final M1 priority decision → AC-106;
- actual functions/Positions → AC-201/AC-204;
- Reserved Owner Decisions and delegation limits → AC-202/AC-203;
- data/tool/credential access → AC-206;
- tested continuity/replacement paths → AC-207;
- operational registers and Owner Mission Control → AC-401–AC-406;
- first economically justified AI-held Position → AC-601–AC-607.

Iterations 9–10 would therefore either duplicate later tasks, invent unsupported quantitative data, or prematurely design the organization.

## 13. Final conclusion

`PASS — material consensus reached at 8 of maximum 10 iterations.`

AC-104 is complete as a qualitative Company-level workload/manual-work/bottleneck baseline.

Recommended roadmap transition:

`AC-104 Complete / PASS → AC-105 Current`.