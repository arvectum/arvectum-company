# Arvectum Company Canonical Roadmap

Status: `Active`
Version: `0.3.0`
Created: `2026-08-19`
Updated: `2026-08-20`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Task classification: `company_planning` with `governance`, `operations`, `portfolio` and `ai_workforce`
Current canonical action: `AC-003 — Canonical repository structure and artifact map`

## 1. Purpose

This document is the canonical planning source for Arvectum Company development and organizational sequencing.

Arvectum Company is the concrete AI-native organization of ООО «Арвектум». The roadmap coordinates how that organization is founded, modeled, operated and progressively automated. It is not the roadmap of Arvectum OS and it does not replace product roadmaps.

The roadmap serves the business. Its objective is not to maximize organizational modeling, governance ceremony, software layers or AI headcount. Its objective is to help build a viable, profitable and governable company in which the owner retains ultimate control while repeatable work is progressively delegated to governed human, AI and software executors.

Roadmap status does not by itself create Organizational Authority, approve expenditure, authorize an external effect, establish legal or contractual authority, promote an Arvectum OS capability, change a Product Contract, or prove business/customer/production readiness.

Future roadmap items are planning hypotheses until activated. Explicit owner priority may reorder work when obligations, risk, client value, cash, continuity or other business evidence requires it; material sequencing changes must be reflected back into this roadmap.

## 2. Authority and source hierarchy

For Company matters, applicable law, legal/corporate authority, approved Company governance artifacts and explicit owner decisions have priority over this roadmap.

Where Company relies on Arvectum OS, applicable Arvectum OS Constitution, Accepted RFC/ADR, approved governance, Product Contracts and implementation/operational evidence remain binding within their declared scope.

Product-specific implementation remains governed by the corresponding product repository and roadmap.

Chat history, model memory and historical discussions are context, not independent canonical authority unless explicitly promoted through an approved path.

## 3. Planning principles

The roadmap follows these rules:

1. **Business first.** Prioritize obligations/risk, operational continuity, client value/revenue, unit economics, scalability and owner workload.
2. **Owner control without owner bottleneck.** Reserved decisions stay with the owner; bounded repeatable work should move to accountable Positions and governed execution.
3. **Organization before executor.** Define the function, accountable Position, authority, workflow and evidence before choosing human, AI or software runtime.
4. **No fake headcount.** Separate agents are not separate Positions unless responsibilities, authority and accountable outputs are materially distinct.
5. **Evidence before scaling.** Technical PASS does not prove business readiness, profitability, compliance or customer readiness.
6. **Reversible evolution.** Prefer the smallest sufficient step with an explicit fallback, replacement or stop path.
7. **Repository boundaries matter.** Company owns organization and portfolio semantics; products own product implementation; OS owns domain-neutral platform contracts/capabilities.
8. **Technology sovereignty by design.** External dependencies must be replaceable and must not own Company authority, canonical history or the only copy of critical organizational knowledge/data.
9. **Learning is governed.** Work produces evidence; evidence may produce an approved improvement. Incidents, customer feedback or AI suggestions do not silently change production behavior.
10. **Client work does not wait for organizational perfection.** Real obligations and product delivery may continue in parallel with Company founding work under their existing authority and repositories.

## 4. Status model

Company roadmap work items use:

- `Current` — active Company-level work;
- `Planned` — accepted sequencing target, not yet active;
- `Future` — directional item requiring later validation;
- `Complete / PASS` — declared scope completed with sufficient evidence;
- `Blocked` — cannot proceed until an explicit blocker is resolved;
- `Stopped` — deliberately discontinued.

By default there is one primary `Current` Company action. Parallel product/client work is tracked in the relevant product roadmap and portfolio, not duplicated here.

Completion requires evidence proportionate to consequence and an update of the applicable canonical source. Percent-complete estimates are avoided unless they have operational meaning.

## 5. Milestone map

| Milestone | Meaning |
|---|---|
| `M0` | Company canonically founded |
| `M1` | Business reality and economics captured |
| `M2` | Initial operating model and authority established |
| `M3` | Portfolio governed as Company assets/investments |
| `M4` | Owner management and core control system established |
| `M5` | First real governed Company operating contour proven |
| `M6` | First real AI-held Position proven economically and operationally |
| `M7` | Multiple Positions operate as one governed organization |
| `M8` | Evidence-driven AI-native Company scaling |

## 6. Phase 0 — Founding and canonical boundary

**Milestone:** `M0 — Company canonically founded`

Purpose: establish the minimum authoritative foundation before detailed organizational design.

| ID | Work item | Status |
|---|---|---|
| `AC-001` | Company Constitution / Founding Charter | `Complete / PASS` |
| `AC-002` | Company ↔ Arvectum OS authority and responsibility boundary | `Complete / PASS` |
| `AC-003` | Canonical repository structure and artifact map | `Current` |
| `AC-004` | Initial `docs/portfolio/PORTFOLIO.md` | `Planned` |
| `AC-005` | Founding baseline cross-review and closure | `Planned` |

AC-001 completion evidence:

- `docs/constitution/COMPANY-CONSTITUTION.md` — `Ratified 1.0.0`;
- `docs/reviews/AC-001-COMPANY-CONSTITUTION-CROSS-REVIEW.md` — `PASS`, 6/10 iterations, material consensus reached;
- `docs/governance/decisions/DECISION-2026-08-19-AC-001-RATIFICATION.md` — explicit Owner approval and amendment reservation.

AC-002 completion evidence:

- `docs/governance/COMPANY-OS-AUTHORITY-BOUNDARY.md` — `Approved 1.0.0`;
- `docs/reviews/AC-002-COMPANY-OS-AUTHORITY-BOUNDARY-CROSS-REVIEW.md` — `PASS`, 7/10 iterations, material consensus reached;
- `docs/governance/decisions/DECISION-2026-08-20-AC-002-APPROVAL.md` — explicit Owner approval of exact Proposed `0.9.0` blob and publication authority for `1.0.0`.

### M0 exit criteria

- Company Constitution / Founding Charter is explicitly approved and canonical;
- corporate/legal authority is not confused with OS governance;
- Company ↔ OS ↔ Product ownership boundaries are explicit;
- repository structure identifies canonical homes for durable Company assets;
- initial portfolio map exists without copying product roadmaps;
- no unresolved material founding conflict remains.

## 7. Phase 1 — Business reality and economic baseline

**Milestone:** `M1 — Business reality and economics captured`

Purpose: model the Company that actually exists before designing departments or AI workforce.

| ID | Work item | Status |
|---|---|---|
| `AC-101` | Current business model and value proposition baseline | `Planned` |
| `AC-102` | Revenue, cash, recurring cost and obligation baseline | `Planned` |
| `AC-103` | Customer/client lifecycle and real value-stream map | `Planned` |
| `AC-104` | Owner workload, manual work and bottleneck map | `Planned` |
| `AC-105` | Material risk, dependency, continuity and fallback baseline | `Planned` |
| `AC-106` | Business baseline review and owner priority decision | `Planned` |

### M1 exit criteria

The owner can answer from canonical evidence:

- how the Company currently creates and captures value;
- where revenue/cash enters and material cost/cash commitments arise;
- what obligations exist and which workflows are operationally critical;
- where owner time is consumed or blocks scale;
- which risks/dependencies can materially interrupt delivery;
- which near-term improvements have the strongest business case.

## 8. Phase 2 — Initial operating model and authority

**Milestone:** `M2 — Initial operating model and authority established`

Purpose: derive the minimum organization from real work rather than from a speculative org chart.

| ID | Work item | Status |
|---|---|---|
| `AC-201` | Minimal organizational/function model | `Planned` |
| `AC-202` | Reserved Owner Decisions | `Planned` |
| `AC-203` | Delegated Position authority, approval and escalation model | `Planned` |
| `AC-204` | Initial Position Registry | `Planned` |
| `AC-205` | Initial Assignments and executor classification | `Planned` |
| `AC-206` | Company data/tool/credential access boundary baseline | `Planned` |
| `AC-207` | Critical-function continuity, replacement and manual fallback baseline | `Planned` |
| `AC-208` | Initial operating model cross-review and closure | `Planned` |

### M2 exit criteria

- every modeled Position exists because of real business responsibility, workload, control need or economic value;
- accountable outputs and authority boundaries are explicit;
- owner-reserved decisions are distinguishable from delegated and automatic execution;
- humans, AI and software are Assignments/executors rather than sources of authority;
- sensitive access and critical fallback paths are bounded;
- replacing an executor does not destroy the Position or its history.

## 9. Phase 3 — Portfolio governance

**Milestone:** `M3 — Portfolio governed as Company assets/investments`

Purpose: turn repositories/products into explicit Company-owned portfolio nodes without moving product implementation into the Company repository.

| ID | Work item | Status |
|---|---|---|
| `AC-301` | Portfolio product/node identity and ownership reconciliation | `Planned` |
| `AC-302` | Accountable Position for each active product/initiative | `Planned` |
| `AC-303` | Investment, cost/risk boundary and stop/continue criteria | `Planned` |
| `AC-304` | Cross-product dependencies and Product Contract reconciliation | `Planned` |
| `AC-305` | Portfolio prioritization and capital/owner-attention model | `Planned` |
| `AC-306` | Portfolio governance review and closure | `Planned` |

### M3 exit criteria

For every active material product/initiative, Company knows its purpose, accountable owner/Position, strategic or economic hypothesis, investment boundary, material dependencies, current milestone source and continue/change/stop criteria.

Product roadmaps remain canonical for product implementation details.

## 10. Phase 4 — Owner management and core controls

**Milestone:** `M4 — Owner management and core control system established`

Purpose: let the owner understand and direct the Company without reconstructing state from chats, repositories and personal memory.

| ID | Work item | Status |
|---|---|---|
| `AC-401` | Company work/obligation register model | `Planned` |
| `AC-402` | Decision, approval and escalation register model | `Planned` |
| `AC-403` | Risk, exception and incident register model | `Planned` |
| `AC-404` | Cash, commitment and management reporting baseline | `Planned` |
| `AC-405` | Portfolio/priority review cadence | `Planned` |
| `AC-406` | Owner Mission Control / unified management view | `Planned` |
| `AC-407` | Management operating cadence and control review | `Planned` |

Implementation may initially be simple. A software dashboard is not required until evidence shows that it creates enough value.

### M4 exit criteria

The owner has a reliable view of material work, obligations, cash/commitments, risks/exceptions, decisions awaiting authority, product priorities and operational health, with canonical drill-down to supporting evidence where appropriate.

## 11. Phase 5 — First governed Company operating contour

**Milestone:** `M5 — First real governed Company operating contour proven`

Purpose: connect the organizational model to real work through the smallest high-value repeatable workflow.

The first workflow is **not predetermined**. It must be selected from M1/M2 evidence using business value, workload, repeatability, risk, reversibility, evidence quality and owner-time reduction.

| ID | Work item | Status |
|---|---|---|
| `AC-501` | First governed workflow candidate selection | `Planned` |
| `AC-502` | Workflow, accountable Position, authority/data/evidence contract | `Planned` |
| `AC-503` | Arvectum OS reliance/admission mapping where applicable | `Planned` |
| `AC-504` | Bounded workflow implementation | `Planned` |
| `AC-505` | Supervised real-operation proof | `Planned` |
| `AC-506` | Incident, uncertain-outcome, recovery and fallback drill | `Planned` |
| `AC-507` | Business-value/economic review and continue/change/stop decision | `Planned` |

### M5 exit criteria

- a real recurring Company workflow runs through explicit Position/authority semantics;
- consequential effects remain within approved authority;
- material actions/evidence can be reconstructed;
- failure has an explicit safe fallback/recovery path;
- owner workload, quality, cost or risk shows sufficient benefit to justify continuation;
- no broader OS/Product lifecycle or readiness claim is inferred from the proof.

## 12. Phase 6 — First real AI-held Position

**Milestone:** `M6 — First real AI-held Position proven economically and operationally`

Purpose: delegate a real Company responsibility to AI only after the function and authority boundary are proven.

| ID | Work item | Status |
|---|---|---|
| `AC-601` | AI delegation candidate selection from real workload | `Planned` |
| `AC-602` | Position business case and unit-economics/workload evidence | `Planned` |
| `AC-603` | Assignment, authority, runtime, tools and data boundary | `Planned` |
| `AC-604` | Quality/evaluation, cost and risk gates | `Planned` |
| `AC-605` | Supervised AI Position pilot | `Planned` |
| `AC-606` | Human/software fallback and executor-replacement proof | `Planned` |
| `AC-607` | Value, owner-workload and risk review | `Planned` |

### M6 exit criteria

A real Position is predominantly executed by AI with measurable value, bounded authority, attributable work, acceptable quality/cost/risk, and a proven replacement/fallback path. AI recommendation, execution or output does not become owner approval by implication.

## 13. Phase 7 — Multi-Position AI-native operation

**Milestone:** `M7 — Multiple Positions operate as one governed organization`

Purpose: scale from one successful delegation to coordinated human/AI/software execution without creating fake organizational complexity.

| ID | Work item | Status |
|---|---|---|
| `AC-701` | Select additional delegations from evidence | `Future` |
| `AC-702` | Cross-Position workflow and handoff model | `Future` |
| `AC-703` | Workforce/Assignment directory and continuity history | `Future` |
| `AC-704` | Coordination, supervision and approval handling where justified | `Future` |
| `AC-705` | Workforce resource/budget governance | `Future` |
| `AC-706` | Multi-executor continuity and replacement drills | `Future` |
| `AC-707` | Multi-Position operating review | `Future` |

### M7 exit criteria

Multiple real Positions execute coordinated workflows with clear accountability, authority, evidence and resource boundaries while the owner retains effective control and does not become the routine execution bottleneck.

## 14. Phase 8 — Evidence-driven scale

**Milestone:** `M8 — Evidence-driven AI-native Company scaling`

Status: `Future`.

Scaling is driven by business capacity and economics, not a target number of agents. A trajectory such as 10 → 25 → 50 → 100 Positions is directional only and must not become a vanity KPI or fake headcount target.

Future scaling may include:

- broader delegation where workload/economics justify it;
- stronger cross-functional coordination and quality control;
- resource/model/tool routing where complexity makes it valuable;
- resilience, portability and disaster-recovery hardening;
- security/privacy/compliance hardening proportionate to customers and data;
- readiness for regulated or public-sector use only after current official requirements are verified;
- additional products, markets and organizational units when supported by strategy and economics.

M8 has no fixed end state. The Company should stop adding organizational or technical complexity whenever marginal business value no longer justifies cost, risk or owner attention.

## 15. Parallel work and repository boundaries

Company founding work does not suspend real product/client obligations.

The following may proceed in parallel when separately authorized and economically justified:

- client delivery and fixes in product repositories;
- Data Platform development;
- Tender Agent product evolution;
- Marketing Agent/product evolution;
- Arvectum OS roadmap work;
- Company founding and operating-model work.

This roadmap records Company-level dependencies and decisions only. It must not duplicate detailed tasks from product or OS roadmaps.

A cross-repository dependency becomes a commitment only through the applicable repository/governance path. Mentioning a future OS capability or product change here does not authorize that change.

## 16. Current action — AC-003

### AC-003 — Canonical repository structure and artifact map

Status: `Current`.

Objective: define the smallest durable Company repository structure and artifact map so each significant Company information class has an explicit canonical home without duplicating product repositories or prematurely forcing Company state into Arvectum OS.

Minimum scope:

- identify durable Company artifact classes needed for the current roadmap;
- assign canonical repository paths/homes for Constitution, governance decisions, authority artifacts, roadmap, portfolio, reviews and later organizational/operational assets;
- distinguish canonical artifacts, evidence/reviews, convenience snapshots and generated/transient outputs;
- identify which future artifact classes remain repository-first, which may later become OS-native, and which remain external/product-owned;
- define naming/version/status conventions only to the extent needed for reliable navigation and change control;
- preserve the AC-002 rule that migration of a Company artifact into OS canonical state is a separate governed change;
- avoid creating empty departments, fake Positions or speculative policy trees merely to make the repository look complete.

Acceptance requires an explicit repository/artifact map sufficient to support AC-004 and later Company governance without conflicting canonical homes or hidden Company↔OS/Product ownership changes.
