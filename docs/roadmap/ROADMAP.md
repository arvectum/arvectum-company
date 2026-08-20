# Arvectum Company Canonical Roadmap

Status: `Active`
Version: `0.8.3`
Created: `2026-08-19`
Updated: `2026-08-20`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Task classification: `company_planning` with `business`, `governance`, `operations`, `portfolio`, `productization` and `ai_workforce`
Current canonical action: `AC-104 — Owner workload, manual work and bottleneck map`
Strategic decision: `docs/governance/decisions/DECISION-2026-08-20-FLAGSHIP-AI-COMPANY-BUILDER.md`

## 1. Purpose

This document is the canonical planning source for Arvectum Company development and organizational sequencing.

Arvectum Company is the concrete AI-native organization of ООО «Арвектум». It is also the first real reference implementation / dogfooding environment for the Company's flagship commercial direction: **customer-specific AI-native company / «ИИ-компания под ключ»**.

The roadmap therefore has two coupled purposes:

1. build ООО «Арвектум» itself as a viable, profitable, governable AI-native company; and
2. turn validated organizational patterns, workflows and modules into a reproducible customer solution without confusing Arvectum Company, Arvectum OS and customer organizations.

The roadmap serves the business. It does not maximize organizational modeling, governance ceremony, software layers, module count or AI headcount as goals in themselves.

Roadmap status does not by itself create Organizational Authority, approve expenditure, authorize an external effect, establish legal or contractual authority, promote an Arvectum OS capability, change a Product Contract, approve a module, or prove business/customer/production readiness.

## 2. Strategic North Star — «ИИ-компания под ключ»

The flagship direction fixed by the Owner is:

> Arvectum designs and deploys an organization-specific AI-native operating model for a customer on top of Arvectum OS: business functions, Positions, authority boundaries, workflows, knowledge, controls and human/AI/software execution, adapted to the customer's real business model and populated with reusable or customer-specific functional modules where justified.

The target transformation is:

```text
Customer business model
→ value streams / obligations / risks
→ functions
→ Positions / authority / escalation
→ workflows / knowledge / evidence
→ reusable + customer-specific modules
→ human | AI | software Assignments
→ Governed Execution on Arvectum OS where admitted
→ measurable operating value
→ governed learning and improvement
```

The organization-first law remains:

`Position → Principal → Assignment → Runtime → Governed Execution`

### 2.1 What is reusable and what is not

Arvectum Company is a **reference implementation**, not a literal customer template.

Potentially reusable:

- organizational modeling method;
- authority/delegation patterns;
- workflow and evidence patterns;
- module contracts and validated functional implementations;
- deployment/configuration methods;
- continuity, portability and replacement patterns;
- Arvectum OS domain-neutral capabilities/contracts.

Not reusable by default:

- Arvectum-specific departments or Positions;
- Owner powers or legal/corporate authority;
- customer/company data, decisions, history or confidential knowledge;
- product-domain rules merely because Arvectum uses them internally;
- technical access as a substitute for Organizational Authority.

### 2.2 Product/module rule

Current products are **not automatically modules**.

A product, workflow or component may become:

- a standalone product;
- a reference implementation;
- a reusable functional module;
- a supporting capability;
- an incubating OS capability where the OS admission rules are satisfied;
- or a contained/retired experiment.

That classification requires evidence and a Company/Product/OS decision in the proper scope.

## 3. Authority and source hierarchy

For Company matters, applicable law, legal/corporate authority, approved Company governance artifacts and explicit Owner decisions have priority over this roadmap.

Where Company relies on Arvectum OS, applicable Arvectum OS Constitution, Accepted RFC/ADR, approved governance, Product Contracts and implementation/operational evidence remain binding within their declared scope.

Product-specific implementation remains governed by the corresponding product repository and roadmap.

Customer organizational authority remains with the customer's authorized Principals/governance. Arvectum OS technical permission, Arvectum Company expertise or a deployed AI executor does not create customer corporate authority by implication.

Chat history, model memory and historical discussions are context, not independent canonical authority unless explicitly promoted through an approved path.

## 4. Planning principles

1. **Business first.** Prioritize obligations/risk, operational continuity, client value/revenue, unit economics, scalability and Owner workload.
2. **Reference implementation, not architecture theater.** Internal Company work must improve the real Company and/or produce evidence useful for the flagship product.
3. **Market evidence early.** Do not wait for a “finished” internal company before testing ICP, customer jobs, willingness to engage and the implementation/support burden.
4. **Owner control without Owner bottleneck.** Reserved decisions stay with the Owner; bounded repeatable work moves toward accountable Positions and governed execution.
5. **Organization before executor.** Define function, Position, authority, workflow and evidence before selecting a human, AI or software runtime.
6. **No fake headcount or fake modules.** Separate agents are not Positions, and separate repositories are not reusable modules, without distinct responsibility/value and evidence.
7. **Evidence before productization.** Technical PASS does not prove customer value, repeatability, profitability, compliance or module readiness.
8. **Reversible evolution.** Prefer the smallest sufficient step with fallback, replacement and stop paths.
9. **Repository boundaries matter.** Company owns organization/portfolio semantics; products own product implementation/domain logic; OS owns domain-neutral platform contracts/capabilities.
10. **Technology sovereignty by design.** Critical dependencies must be replaceable and must not own authority, canonical history or the only copy of critical organizational/customer data.
11. **Customer sovereignty by design.** Customer data, knowledge, decisions and authority remain isolated and governed for that customer unless explicit rights permit otherwise.
12. **Learning is governed.** Work produces evidence; approved evidence may improve reusable organizational assets. Customer or internal incidents do not silently change production behavior.
13. **Internal and external loops stay coupled.** Arvectum Company proves the method; customer discovery and deployments test whether the method is commercially valuable and transferable.

## 5. Status model

Company roadmap work items use:

- `Current` — active Company-level work;
- `Planned` — accepted sequencing target, not yet active;
- `Future` — directional item requiring later validation;
- `Complete / PASS` — declared scope completed with sufficient evidence;
- `Blocked` — cannot proceed until an explicit blocker is resolved;
- `Stopped` — deliberately discontinued.

By default there is one primary `Current` Company action. Parallel product, OS and client work remains in the relevant repository and is referenced rather than duplicated.

Completion requires evidence proportionate to consequence and an update of the applicable canonical source.

## 6. Milestone map

| Milestone | Meaning |
|---|---|
| `M0` | Company canonically founded |
| `M1` | Business/economic reality and first market-validation plan captured |
| `M2` | Arvectum Company reference operating model and authority established |
| `M3` | Product/module-candidate portfolio governed as investments |
| `M4` | Owner control and reference-implementation observability established |
| `M5` | First reusable governed internal operating module proven |
| `M6` | First AI-held Position proven economically, operationally and replaceably |
| `M7` | First external AI-company design-partner deployment proven |
| `M8` | Repeatable multi-customer AI-company product proven and scalable |

## 7. Phase 0 — Founding and canonical boundary

**Milestone:** `M0 — Company canonically founded`

**Milestone status:** `Complete / PASS`

| ID | Work item | Status |
|---|---|---|
| `AC-001` | Company Constitution / Founding Charter | `Complete / PASS` |
| `AC-002` | Company ↔ Arvectum OS authority and responsibility boundary | `Complete / PASS` |
| `AC-003` | Canonical repository structure and artifact map | `Complete / PASS` |
| `AC-004` | Initial `docs/portfolio/PORTFOLIO.md` | `Complete / PASS` |
| `AC-005` | Founding baseline cross-review and closure | `Complete / PASS` |

**M0 result:** `COMPLETE / PASS — achieved 2026-08-20`.

Completion evidence remains in the corresponding canonical artifacts, review files and approval records. M0 does not imply a completed operating model, financial baseline, profitable portfolio, production-ready AI workforce or customer-ready flagship product.

## 8. Phase 1 — Business reality, economics and early market evidence

**Milestone:** `M1 — Business/economic reality and first market-validation plan captured`

Purpose: understand the real Company, economic runway and first credible market path before designing a large internal organization or a customer product from assumptions.

| ID | Work item | Status |
|---|---|---|
| `AC-101` | Current business model and value proposition baseline | `Complete / PASS` |
| `AC-102` | Revenue, cash, recurring cost and obligation baseline | `Complete / PASS` |
| `AC-103` | Current customer/client lifecycle and real value-stream map | `Complete / PASS` |
| `AC-104` | Owner workload, manual work and bottleneck map | `Current` |
| `AC-105` | Material risk, dependency, continuity and fallback baseline | `Planned` |
| `AC-107` | Flagship ICP, buyer, job-to-be-done and measurable outcome hypotheses | `Planned` |
| `AC-108` | First design-partner criteria, discovery script and market-validation plan | `Planned` |
| `AC-106` | M1 business baseline review and Owner priority decision | `Planned` |

AC-101 establishes the corrected flagship direction under `DECISION-2026-08-20-FLAGSHIP-AI-COMPANY-BUILDER` and `docs/business/CURRENT-BUSINESS-MODEL-AND-VALUE-PROPOSITION.md` `0.2.0`.

AC-102 publication `0.3.0` establishes the Company-level revenue/cash/cost/obligation architecture and the boundary between management finance and outsourced accounting. Its cross-review closed at `7 of maximum 10` after the Owner corrected the task scope: transaction-level bookkeeping, bank reconciliation, tax calculation and receipt inspection are not Company-design work and do not block progression.

AC-103 publication `0.1.0` establishes the current Company-level customer lifecycle and five value streams, separating real bespoke client delivery and controlled-pilot evidence from the future flagship lifecycle. Its cross-review closed at `7 of maximum 10`; the key handoff is that acquisition/scoping/commitment, customer iteration and acceptance are strongly Owner-dependent and must be measured rather than assumed in AC-104.

### M1 exit criteria

The Owner can answer from evidence:

- what business Arvectum is building and how current business lines create/capture value;
- where structurally revenue/cash enters and material cost/cash commitments arise;
- what obligation classes and continuity risks exist;
- where Owner time is consumed or blocks scale;
- what investment burden the flagship direction structurally creates;
- who the first plausible flagship buyer/ICP is and what measurable outcome the offer should create;
- what evidence would make a first external design-partner engagement worth pursuing;
- which near-term improvements and productization work have the strongest business case.

## 9. Phase 2 — Arvectum Company reference operating model

**Milestone:** `M2 — Arvectum Company reference operating model and authority established`

Purpose: derive the minimum real organization from M1 evidence and make it useful both for operating ООО «Арвектум» and for learning what is transferable to customer organizations.

| ID | Work item | Status |
|---|---|---|
| `AC-201` | Minimal real organizational/function model | `Planned` |
| `AC-202` | Reserved Owner Decisions | `Planned` |
| `AC-203` | Delegated Position authority, approval and escalation model | `Planned` |
| `AC-204` | Initial Position Registry | `Planned` |
| `AC-205` | Initial Assignments and executor classification | `Planned` |
| `AC-206` | Company data/tool/credential access boundary baseline | `Planned` |
| `AC-207` | Critical-function continuity, replacement and manual fallback baseline | `Planned` |
| `AC-208` | Reference-model transferability boundary and operating-model cross-review | `Planned` |

AC-208 must explicitly separate:

- Arvectum-specific organizational facts;
- reusable organization-design patterns;
- reusable workflow/authority patterns;
- product/module candidates;
- OS-domain-neutral semantics;
- customer-specific semantics that must be re-derived for each customer.

### M2 exit criteria

- every modeled Position exists because of real business responsibility, workload, control need or economic value;
- authority and escalation boundaries are explicit;
- humans, AI and software remain Assignments/executors rather than authority sources;
- sensitive access and critical fallback paths are bounded;
- replacing an executor does not destroy Position meaning/history;
- the Company can explain what parts of its operating model are evidence for the flagship method and what parts must **not** be copied into a customer organization.

## 10. Phase 3 — Product and reusable module-candidate governance

**Milestone:** `M3 — Product/module-candidate portfolio governed as investments`

Purpose: decide how existing products and initiatives relate to the flagship offer without turning every repository into a module or every reusable component into Arvectum OS.

| ID | Work item | Status |
|---|---|---|
| `AC-301` | Portfolio product/node identity and ownership reconciliation | `Planned` |
| `AC-302` | Accountable Position for each active product/initiative | `Planned` |
| `AC-303` | Investment, cost/risk boundary and stop/continue criteria | `Planned` |
| `AC-304` | Standalone product vs reference implementation vs module-candidate vs OS-capability boundary | `Planned` |
| `AC-305` | Cross-product/module dependencies and Product Contract reconciliation | `Planned` |
| `AC-306` | Portfolio/module prioritization and capital/Owner-attention model | `Planned` |
| `AC-307` | Portfolio/module governance review and closure | `Planned` |

A reusable module must eventually have, proportionate to risk and maturity:

- a concrete organizational function/job;
- accountable ownership;
- defined inputs/outputs and authority assumptions;
- data/tool boundaries;
- workflow/evidence semantics;
- configuration versus customer-specific customization boundary;
- quality/cost/risk evidence;
- dependencies and OS reliance where applicable;
- version/upgrade/retirement path;
- replacement/fallback path.

### M3 exit criteria

For every material node, Company knows whether it is being treated as a standalone product, reference implementation, module candidate, supporting capability, experiment or retirement candidate; knows its investment boundary and accountable Position; and does not confuse product-domain reuse with OS platform admission.

## 11. Phase 4 — Owner control and reference observability

**Milestone:** `M4 — Owner control and reference-implementation observability established`

Purpose: let the Owner run Arvectum without reconstructing state from chats/repositories and create observable evidence about whether the AI-native organizational model actually works.

| ID | Work item | Status |
|---|---|---|
| `AC-401` | Company work/obligation register model | `Planned` |
| `AC-402` | Decision, approval and escalation register model | `Planned` |
| `AC-403` | Risk, exception and incident register model | `Planned` |
| `AC-404` | Cash, commitment and management reporting baseline | `Planned` |
| `AC-405` | Portfolio/module/priority review cadence | `Planned` |
| `AC-406` | Owner Mission Control / reference-implementation evidence view | `Planned` |
| `AC-407` | Management operating cadence and control review | `Planned` |

Software dashboards are not required until they create sufficient value. Manual/simpler controls are acceptable when reliable and proportionate.

### M4 exit criteria

The Owner can see material work, obligations, cash/commitments, risks/exceptions, pending decisions, product/module priorities, operational health and evidence needed to evaluate the internal reference implementation.

## 12. Phase 5 — First reusable governed internal operating module

**Milestone:** `M5 — First reusable governed internal operating module proven`

Purpose: connect the organizational model to one real recurring Company workflow selected for both internal business value and useful flagship-product learning.

The first workflow/module is **not predetermined**. Selection uses M1/M2/M3 evidence: business value, workload, repeatability, transferability, risk, reversibility, evidence quality and Owner-time reduction.

| ID | Work item | Status |
|---|---|---|
| `AC-501` | First governed workflow/module candidate selection | `Planned` |
| `AC-502` | Workflow, Position, authority/data/evidence contract | `Planned` |
| `AC-503` | Arvectum OS reliance/admission mapping where applicable | `Planned` |
| `AC-504` | Bounded internal implementation | `Planned` |
| `AC-505` | Supervised real-operation proof | `Planned` |
| `AC-506` | Incident, uncertain-outcome, recovery and fallback drill | `Planned` |
| `AC-507` | Business-value, transferability and economics review | `Planned` |
| `AC-508` | Reusable module candidate package or explicit non-reuse decision | `Planned` |

### M5 exit criteria

- a real recurring Company workflow runs through explicit Position/authority semantics;
- consequential effects remain within approved authority;
- material execution/evidence is reconstructable;
- failure has a safe fallback/recovery path;
- internal value is measurable enough to justify continuation;
- reusable versus Arvectum-specific semantics are explicit;
- the result is either promoted to a governed module candidate through the proper scope or explicitly retained as Company-specific work;
- no OS Active/customer-ready claim is inferred from internal success.

## 13. Phase 6 — First real AI-held Position

**Milestone:** `M6 — First AI-held Position proven economically, operationally and replaceably`

Purpose: prove that a real organizational responsibility can be predominantly executed by AI without making AI the source of authority or organizational continuity.

| ID | Work item | Status |
|---|---|---|
| `AC-601` | AI delegation candidate selection from real workload | `Planned` |
| `AC-602` | Position business case and unit-economics/workload evidence | `Planned` |
| `AC-603` | Assignment, authority, runtime, tools and data boundary | `Planned` |
| `AC-604` | Quality/evaluation, cost and risk gates | `Planned` |
| `AC-605` | Supervised AI Position pilot | `Planned` |
| `AC-606` | Human/software fallback and executor-replacement proof | `Planned` |
| `AC-607` | Value, Owner-workload, module-reuse and risk review | `Planned` |

### M6 exit criteria

A real Position is predominantly executed by AI with measurable value, bounded authority, attributable work, acceptable quality/cost/risk and proven replacement/fallback. The result provides credible evidence for customer module design but does not imply external readiness automatically.

## 14. Phase 7 — First external AI-company design-partner deployment

**Milestone:** `M7 — First external AI-company design-partner deployment proven`

Purpose: test whether the organization-first method transfers from Arvectum Company to a real external organization and creates customer value without creating uncontrolled customization, authority, security or support obligations.

| ID | Work item | Status |
|---|---|---|
| `AC-701` | Select first design partner from AC-108 evidence | `Future` |
| `AC-702` | Customer business/value-stream/obligation discovery | `Future` |
| `AC-703` | Customer functions, Positions, authority and escalation model | `Future` |
| `AC-704` | Customer data/security/sovereignty/access boundary | `Future` |
| `AC-705` | Module configuration, gap analysis and customer-specific module scope | `Future` |
| `AC-706` | Arvectum OS Product Contract/reliance/admission mapping | `Future` |
| `AC-707` | Bounded supervised customer deployment | `Future` |
| `AC-708` | Acceptance, support, continuity, replacement and portability proof | `Future` |
| `AC-709` | Customer-value, implementation-economics and continue/change/stop review | `Future` |

### M7 exit criteria

- one real customer organization is modeled from its own business rather than cloned from Arvectum;
- customer Organizational Authority remains with authorized customer Principals;
- reused modules and customer-specific extensions have explicit boundaries;
- customer data/knowledge/history remain isolated and portable;
- deployment can be supported, recovered and exited without hidden vendor lock-in;
- measurable customer value and implementation/support effort are recorded;
- the Owner has an evidence-backed decision whether the flagship should continue, change scope or stop.

## 15. Phase 8 — Repeatable multi-customer AI-company product

**Milestone:** `M8 — Repeatable multi-customer AI-company product proven and scalable`

Status: `Future`.

Purpose: turn one successful external deployment into a repeatable product rather than a consultancy project that must be reinvented from scratch for every customer.

| ID | Work item | Status |
|---|---|---|
| `AC-801` | Standard discovery and organization-configuration methodology | `Future` |
| `AC-802` | Reusable organizational pattern/blueprint library without fixed org-chart cloning | `Future` |
| `AC-803` | Governed module catalog, versioning, compatibility and retirement model | `Future` |
| `AC-804` | Packaging, pricing, implementation and support unit economics | `Future` |
| `AC-805` | Deployment, upgrade, migration, backup, exit and portability path | `Future` |
| `AC-806` | Multi-customer isolation, security, privacy and rights model | `Future` |
| `AC-807` | Sales/onboarding/implementation capacity model | `Future` |
| `AC-808` | Second/third customer repeatability evidence | `Future` |
| `AC-809` | Scale review and capital/organization decision | `Future` |

Scaling is driven by customer value, repeatability, economics, support burden, risk and Owner capacity — not by a target number of agents or customer organizations.

### M8 exit criteria

The Company can repeatedly configure and deploy customer-specific AI-native organizations with substantially less reinvention than the first deployment, while preserving customer authority/sovereignty, module/OS boundaries, portability, acceptable implementation/support economics and measurable value.

## 16. Coupled internal ↔ external learning loop

The flagship product should compound through this loop:

```text
Arvectum Company real work
→ governed execution and evidence
→ validated organizational pattern/module candidate
→ product/module review
→ external customer discovery/deployment
→ customer value/support/economic evidence
→ validated improvement
→ improved method/module/Company operation
```

Customer feedback or internal convenience does not automatically change reusable modules, OS contracts, Company governance or production behavior. Promotion remains governed.

## 17. Parallel work and repository boundaries

The following may proceed in parallel when separately authorized and economically justified:

- current client delivery and fixes in product repositories;
- Tender Agent and procurement-domain evolution;
- Creative Test Agent / marketing-domain evolution;
- parser/product work;
- Data Platform investigation;
- Proxy Launcher productization;
- Arvectum OS roadmap work;
- early flagship customer discovery after AC-107/AC-108;
- Arvectum Company operating-model work.

This roadmap records Company-level dependencies and decisions only. Product/OS implementation roadmaps remain canonical in their repositories.

A cross-repository dependency becomes a commitment only through the applicable governance path. Mentioning a future module or OS capability here does not authorize or promote it.

## 18. Current action — AC-104

### AC-104 — Owner workload, manual work and bottleneck map

Status: `Current`.

Objective: map where the Owner currently performs, reviews, approves, coordinates or reconstructs work across the real Company lifecycle and portfolio, distinguish genuinely reserved authority from avoidable execution load, and identify the highest-value delegation/automation candidates without designing Positions prematurely.

AC-103 provides the customer/value-stream skeleton for this analysis. AC-104 should test actual Owner concentration across opportunity judgment, discovery/scoping, commitment, delivery coordination, exception handling, acceptance, support and productization/reuse decisions.

The output must distinguish work that should remain Owner-reserved from work that can later move to an accountable Position, AI/software Assignment or simpler process control.