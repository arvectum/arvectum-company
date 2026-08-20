# AC-201 — Minimal Real Organizational / Function Model

Status: `Complete / PASS`
Version: `0.1.0`
Created: `2026-08-20`
Updated: `2026-08-20`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-201 — Minimal real organizational/function model`
Review: `docs/reviews/AC-201-MINIMAL-ORGANIZATIONAL-FUNCTION-MODEL-CROSS-REVIEW.md`
Depends on: `AC-101` through `AC-108`, with `AC-106` as the M1 synthesis/priority handoff

## 1. Purpose

AC-201 derives the **minimum real Company-level function model** of Arvectum from the evidence already established in M1.

The task exists to answer a narrow organizational question before creating Positions, delegations, Assignments or AI Workforce:

> What durable business responsibilities must exist inside Arvectum Company because real value streams, obligations, control needs, recurring workload, continuity needs or economic responsibility already require them — regardless of which human, AI, software or external service currently performs the work?

The model must improve the real operation of ООО «Арвектум» and provide reference evidence for the flagship `«ИИ-компания под ключ»` method. It must not become a generic enterprise org chart or an invented list of future departments.

This publication is intentionally executor-neutral.

It does **not** create a Position, appoint a Principal, delegate authority, grant access, choose a runtime, create headcount, approve a department, approve a module, change an Arvectum OS Product Contract, or create a customer-facing commitment.

## 2. Governing and evidence boundary

AC-201 is subordinate to:

1. applicable law and valid legal/corporate authority of ООО «Арвектум»;
2. `docs/constitution/COMPANY-CONSTITUTION.md`;
3. approved Company governance and Owner decisions;
4. `docs/governance/COMPANY-OS-AUTHORITY-BOUNDARY.md`;
5. product-specific canonical repositories within their product/domain scope;
6. applicable Arvectum OS Constitution, Accepted RFC/ADR, approved governance and Product Contracts where Company work actually relies on Arvectum OS.

The main Company evidence inputs are:

- `docs/business/CURRENT-BUSINESS-MODEL-AND-VALUE-PROPOSITION.md`;
- `docs/business/REVENUE-CASH-COST-OBLIGATION-BASELINE.md`;
- `docs/business/CURRENT-CUSTOMER-LIFECYCLE-AND-VALUE-STREAM.md`;
- `docs/business/OWNER-WORKLOAD-MANUAL-WORK-BOTTLENECK-MAP.md`;
- `docs/business/MATERIAL-RISK-DEPENDENCY-CONTINUITY-FALLBACK-BASELINE.md`;
- `docs/business/FLAGSHIP-ICP-BUYER-JTBD-OUTCOME-HYPOTHESES.md`;
- `docs/business/DESIGN-PARTNER-DISCOVERY-AND-MARKET-VALIDATION-PLAN.md`;
- `docs/business/M1-BUSINESS-BASELINE-REVIEW-AND-PRIORITY.md`;
- `docs/portfolio/PORTFOLIO.md`;
- the approved flagship and M1 closure/priority decisions.

The current legal/corporate source registry supports a minimal safe fact pattern sufficient for this organizational model: the Company is currently owner-operated, one General Director is registered as the person entitled to act without a power of attorney at the evidenced baseline, and the Company operates under standard charter No. 23. AC-201 does not reproduce personal identifiers, signatures, addresses, banking details or other unnecessary source payloads.

Arvectum OS `main` was re-checked for AC-201 at `d26f9583393d4f3d9ef104f5408439da0471fd76`. The Company-relevant baseline remains unchanged from AC-106: Constitution `1.2.0` Ratified, RFC-0001 through RFC-0008 Accepted `1.0.0`, OS Decision Authority Policy still Proposed `0.2.1`, CAP-001 through CAP-004 Incubating/Provisional and the current Product Contracts relevant to existing product slices still Provisional. AC-201 therefore creates no new OS reliance or platform-lifecycle claim.

## 3. Modeling rules

### 3.1 Function before Position

AC-201 uses the following sequence:

```text
real value / obligation / workload / control need
→ durable function
→ accountable outcomes and handoffs
→ AC-202/AC-203 authority boundaries
→ AC-204 Position design
→ AC-205 Assignment/executor design
→ AC-206 access boundary
→ AC-207 continuity/fallback
```

A function is not a job title. A function may later be carried by:

- one Position;
- part of one Position;
- several Positions;
- an external professional service under an explicit interface;
- or a combination of human, AI and software execution under one accountable organizational boundary.

### 3.2 Minimality test

A Company-level function is admitted here only when all of the following are true:

1. a real current value stream, obligation, control need, recurring workload or material continuity requirement depends on it;
2. failure to own the responsibility would create material ambiguity, bottleneck, economic loss, customer harm, governance gap or continuity risk;
3. it has a distinguishable accountable outcome or control result;
4. its Company-level meaning is not already owned canonically by a product, customer, legal/corporate authority, accounting/banking contour or Arvectum OS;
5. the function remains meaningful if the current executor, model, agent, device or vendor is replaced.

A separate department, Position or software component is **not** required merely because a function exists.

### 3.3 Current executor concentration is evidence, not design

The Owner currently carries many materially different responsibilities. That concentration is a fact used to reveal durable functions; it is not evidence that those functions should remain permanently fused into one Position.

Conversely, the existence of several AI tools, coding agents, repositories or product runtimes is not evidence of several organizational functions or Positions.

## 4. Current operating reality

M1 establishes a distinctive current pattern:

- the Company already creates real customer value through bespoke automation, controlled pilot/product work and procurement/domain activity;
- technical implementation and QA are comparatively strong and increasingly executable by AI/software;
- acquisition, scoping, commitment framing, customer-context continuity, exception classification, acceptance, portfolio prioritization and organizational-state reconstruction remain highly Owner-dependent;
- material strategy, capital, risk and external commitments legitimately require competent authority and must not be “automated away” merely to reduce Owner involvement;
- accounting/statutory execution is professionally externalized, while management visibility and commitment decisions remain Company responsibilities;
- security, credentials, local environments, repositories, customer data and external services create real continuity/control requirements;
- the flagship market-discovery loop is authorized as bounded evidence work but a repeatable sales/onboarding engine is not yet proven.

The resulting organizational problem is therefore not “create departments for everything”. It is:

```text
preserve material Owner/corporate control
+ make durable functions explicit
+ separate value creation from authority/control
+ move repeatable preparation/execution out of Owner memory over time
+ keep product/customer/OS/external authority boundaries intact
```

## 5. Minimal Company-level function model

AC-201 admits **eight** Company-level function domains.

They are responsibility domains, not departments and not Positions.

| ID | Function domain | Primary class | Why it exists now | Minimum accountable outcome |
|---|---|---|---|---|
| `F-01` | Company Direction, Corporate Governance & Material Control | control / authority interface | the Company needs strategy, priority, capital/risk/commitment control and a lawful corporate decision/representation path | material Company decisions are framed, decided through the proper authority path, recorded proportionately and converted into bounded next actions without confusing technical access with authority |
| `F-02` | Commercial Discovery, Qualification & Commitment Preparation | value acquisition | real work begins with opportunity/request interpretation; flagship AC-108 discovery is now an active evidence loop; scoping and commercial meaning are major Owner bottlenecks | a qualified opportunity/discovery package states the real problem, desired outcome, inputs, constraints, scope/exclusions, uncertainties and the evidence needed before any binding commitment |
| `F-03` | Customer Delivery, Acceptance & Support | value realization | current customer value is realized through scoped delivery, validation, correction, acceptance, handover and bounded support; customer context continuity is currently fragile | each committed engagement has reconstructable state from scope through delivery/validation/acceptance/support, with defects vs changes vs customer-blocked states distinguishable and closure evidence explicit |
| `F-04` | Portfolio, Product & Workstream Stewardship / Reuse | portfolio / value orchestration | Arvectum has multiple products, client workstreams and module candidates competing for Owner attention; productization/reuse decisions are real but not yet systematically governed | each material workstream/product has a clear business purpose, priority/status, responsibility boundary and continue/change/stop/reuse question without copying product implementation truth into the Company repository |
| `F-05` | Engineering, Automation, QA & Release | production / execution | implementation, testing, packaging and technical correction are the strongest current production capability and already use substantial AI/software execution | produce verified technical artifacts/releases/automations with adequate tests, limitations, reproducibility and handoff evidence for the declared workstream, without creating customer/commercial authority by technical success |
| `F-06` | Management Finance, Cash & Obligation Control | management / economic control | material commitments require decision-relevant liquidity, cost, working-capital and obligation visibility; transaction/statutory accounting is external but management responsibility is not | decision-makers receive sufficient current cash/commitment/economic/obligation evidence for material choices while accounting/banking systems remain authoritative for transaction/statutory truth |
| `F-07` | Organizational State, Evidence & Improvement | coordination / learning | the Owner currently reconstructs current state across chats/repos/decisions; the flagship thesis requires durable organizational meaning and governed learning rather than transient AI output | Company functions, decisions, workflow/evidence references, current planning state and validated improvement proposals remain reconstructable, synchronized with their canonical sources and promoted only through the proper governance path |
| `F-08` | Security, Access, Risk & Continuity Assurance | assurance / continuity | credentials, local devices, customer data, repositories, vendors and external systems create real control and recovery needs; AC-105 found unresolved single points and deliberate gates | material work has explicit data/access/risk/continuity requirements, fail-closed/escalation behavior and a bounded replacement/degraded/recovery expectation without storing secrets or weakening authority/security gates |

These eight functions are the smallest current set that covers the M1 evidence without inventing a future enterprise structure.

## 6. Function details and boundaries

### F-01 — Company Direction, Corporate Governance & Material Control

**Owns at Company level:**

- strategy and flagship-direction coherence;
- material portfolio priority and capital/risk decision framing;
- material commitment and exception decision path;
- corporate/legal authority interface for actions that require a valid corporate form or authorized representative;
- approval/publication boundary for material Company governance changes;
- explicit distinction between Owner, participant, General Director, Position, Principal and technical operator.

**Does not own:**

- automatic technical permission merely because a decision exists;
- product implementation decisions within product scope;
- Arvectum OS governance;
- customer corporate authority;
- routine preparation/clerical work that can later be delegated safely.

**Current evidence:** strongly Owner/General-Director concentrated. AC-202 must now define what is actually reserved rather than leaving every difficult choice here by default.

### F-02 — Commercial Discovery, Qualification & Commitment Preparation

**Owns at Company level:**

- opportunity/request intake meaning;
- problem and recent-case discovery;
- qualification against business/economic/fit constraints;
- scope/exclusion and acceptance-outcome preparation;
- customer-input/readiness questions;
- pricing/commitment proposal preparation when applicable;
- bounded flagship market discovery under AC-108.

**Does not own:**

- authority to bind the Company merely because a proposal was prepared;
- mass-outbound, CRM or sales-funnel machinery that current evidence does not justify;
- customer-side buying authority;
- product implementation.

**Current evidence:** real but highly Owner-dependent and not standardized Company-wide. There is not yet evidence for a separate Sales department or a repeatable acquisition engine.

### F-03 — Customer Delivery, Acceptance & Support

**Owns at Company level:**

- engagement/workstream state from committed scope to closure;
- customer-context continuity needed to deliver the promised result;
- delivery coordination across product/technical work;
- customer validation and acceptance evidence;
- defect vs agreed-scope vs change-request classification;
- blocked-customer-input state;
- support/follow-up state and closure boundary;
- customer outcome/usefulness evidence where available.

**Does not own:**

- product roadmap or product-domain implementation truth;
- authority to promise new scope/support without the applicable commitment path;
- customer confidential payload in this public repository;
- a separate Customer Success department without later workload/economic evidence.

**Current evidence:** real and central to value realization, but the coordination/exception path remains highly Owner-dependent.

### F-04 — Portfolio, Product & Workstream Stewardship / Reuse

**Owns at Company level:**

- the reason a product/workstream exists in the Company portfolio;
- priority and investment/attention proposal within approved bounds;
- status and responsibility boundary across Company/Product/OS;
- stop/continue/change questions;
- productization and reuse-candidate evidence;
- separation among standalone product, client-specific solution, reference implementation, module candidate, supporting capability and possible OS candidate.

**Does not own:**

- product code, schemas, product-specific prompts/workflows or release truth;
- automatic promotion of a product into a reusable module;
- automatic promotion of a shared pattern into Arvectum OS;
- final Phase 3 investment/module decisions before their evidence and authority path.

**Current evidence:** real and strongly Owner-centered because multiple repositories/workstreams compete for one priority context.

### F-05 — Engineering, Automation, QA & Release

**Owns at Company level only at the functional level:**

- technical decomposition and implementation execution needed by accepted workstreams;
- automated/manual tests proportionate to risk;
- packaging/build/release preparation;
- defect correction and technical evidence;
- reproducibility/re-bootstrap information where needed;
- handoff of tested artifacts and known limitations back to the customer/product/workstream owner.

**Product boundary:** detailed product implementation remains canonical in the corresponding product repository. This Company function describes the durable need for technical production; it does not create one centralized codebase or “engineering department” by implication.

**AI boundary:** AI/software may execute substantial portions of this function. Technical competence or repository permission does not create authority to approve material business commitments, customer acceptance, capital expenditure or other Reserved Owner Decisions.

**Current evidence:** strongest and most automatable current function; the Owner bottleneck is increasingly around sequencing, context, exception handling and acceptance rather than raw coding alone.

### F-06 — Management Finance, Cash & Obligation Control

**Owns at Company level:**

- management interpretation of revenue/cost/obligation classes;
- decision-relevant current liquidity/commitment visibility;
- material receivable/payable/mandatory-payment exceptions reaching management;
- project/product economic evidence for material decisions;
- procurement working-capital/cash-gap visibility where relevant;
- recurring-cost and material new-spend awareness.

**External accounting boundary:** bookkeeping, transaction classification, bank reconciliation, tax calculation, statutory reporting and transaction truth remain with the professional accounting/banking contour unless a later competent decision changes that architecture.

**Does not own:** a duplicate bookkeeping system or a “Finance department” created for organizational symmetry.

**Current evidence:** the function is necessary, but the management-reporting interface is still immature and is intentionally completed later through AC-404.

### F-07 — Organizational State, Evidence & Improvement

**Owns at Company level:**

- one-current-source awareness for Company governance/planning/organizational assets;
- roadmap/decision/review synchronization and read-after-write consistency where material;
- durable function/workflow/decision/evidence references;
- reconstruction of current Company state without relying on one chat or one person's memory;
- evidence capture for Owner interventions, exceptions and reusable-learning candidates;
- proposal of improvements and governed promotion after review/approval.

**Does not own:**

- every runtime log, trace or transient AI output;
- automatic promotion of observations into policy/workflow/knowledge;
- a requirement that Arvectum OS already be the canonical runtime for the Company;
- authority to make a decision simply because the evidence was assembled.

**Current evidence:** real because state reconstruction and clerical synchronization already consume Owner attention. The function is admitted to remove coordination loss, not to create governance ceremony.

### F-08 — Security, Access, Risk & Continuity Assurance

**Owns at Company level:**

- requirements for who/what may access material Company/customer data/tools;
- separation of technical authorization from Organizational Authority;
- credential and privileged-access governance requirements without storing secrets;
- data/customer sovereignty and purpose boundary;
- risk/exception escalation criteria;
- continuity requirements for critical functions, repositories, local environments and vendors;
- fail-closed/degraded/manual/recovery expectations;
- technology-sovereignty/replacement implications for material dependencies.

**Does not own:**

- the secret values, keys or private credential inventory in this public repository;
- product-specific security implementation that belongs in a product repository;
- OS-domain-neutral security semantics owned by Arvectum OS;
- invented Company-wide RTO/RPO/SLA values;
- bypass of a lawful corporate, customer or security gate in the name of continuity.

**Current evidence:** necessary because AC-105 found real single points and control gates; detailed access and tested continuity remain AC-206/AC-207.

## 7. Company function flow

The minimum value flow is:

```text
external need / market evidence / current obligation
                ↓
F-02 Commercial Discovery & Qualification
                ↓
scoped opportunity / commitment proposal
                ↓
F-01 material authority path when required
       + F-06 economic/obligation evidence
       + F-08 risk/data/access constraints
                ↓
accepted bounded work
                ↓
F-03 Customer Delivery & Outcome coordination
                ↕
F-04 Product / Workstream Stewardship
                ↕
F-05 Engineering / Automation / QA / Release
                ↓
customer validation / acceptance / support state
                ↓
F-06 economic/obligation closure where applicable
F-07 evidence / state / improvement capture
                ↓
continue / change / stop / reuse proposal
```

`F-08` constrains every material path where data, privileged access, external dependency, security or continuity is relevant.

`F-01` remains the material control/authority interface; AC-201 does not yet decide which specific decisions may bypass Owner review through later delegation.

## 8. Current realization map — without creating Positions

The current Company is functionally real but organizationally concentrated.

| Function | Current execution pattern | Main current weakness |
|---|---|---|
| `F-01` | Owner / General Director performs the material strategic, corporate and commitment control work | lawful/material control and low-risk preparation/mechanics are still too coupled around one Principal |
| `F-02` | primarily Owner-led; AI/software may assist with research, extraction, drafts and evidence preparation | customer/problem meaning and scope are reconstructed centrally; repeatable commercial process is not proven |
| `F-03` | Owner coordinates customer context, feedback, exception and acceptance; product/AI/software execute pieces | customer history and defect/scope/acceptance judgment can remain in Owner memory |
| `F-04` | Owner is the shared portfolio/product/workstream interpreter across several repositories | priority switching and productization/reuse judgment form a central queue |
| `F-05` | substantial AI/software/local-agent execution plus Owner sequencing/review and environment gates | automated production can still wait for Owner context, local access, exception handling or release acceptance |
| `F-06` | accounting/bank professionals/systems own transaction/statutory work; Owner consumes or reconstructs management meaning | decision-relevant management reporting is not yet a routine exception-driven interface |
| `F-07` | Owner + AI-assisted repository/governance work | current state can still require cross-chat/repository reconstruction and manual synchronization |
| `F-08` | Owner + product-specific controls + external providers/runtime controls | detailed access map, credential recovery and tested continuity are not yet Company-wide |

This table is evidence about current concentration only. It is **not** the Initial Position Registry and creates no Assignment.

## 9. External and non-Company authority/service interfaces

Several essential activities influence the Company but should not be converted into internal Company functions with competing authority.

| Interface | External/current authority or responsibility | Company function that consumes the interface | Boundary |
|---|---|---|---|
| legal/corporate registry, charter and formal authority | applicable law, corporate acts, charter, registry and authorized legal actors | `F-01` | Company artifacts may reference/implement internal governance but cannot manufacture legal authority |
| accounting/tax/statutory records | outsourced accounting and authoritative accounting/banking systems | `F-06` | Company consumes decision-relevant summaries/exceptions; no parallel bookkeeping |
| banking/payment execution | bank and properly authorized Company Principal | `F-06` / `F-01` | bank access is technical/financial capability, not independent Organizational Authority |
| customer authority, data and acceptance | customer and its authorized systems/Principals | `F-02`, `F-03`, `F-08` | customer data/authority remain customer-scoped; no automatic cross-customer reuse |
| suppliers/contractors | supplier/contractor plus the applicable contract/workstream | `F-03`, `F-04`, `F-06` | supplier performance does not become generic Company truth; substitution/downside is workstream-specific |
| product repositories | corresponding product governance/repository | `F-04`, `F-05`, `F-03` | Company owns portfolio meaning; product owns implementation/domain semantics |
| Arvectum OS | canonical OS repository/governance/contracts | functions only where an admitted OS reliance later exists | OS may represent/enforce Company semantics but does not create Company authority or Company-specific meaning |
| AI/model/runtime/tool vendors | replaceable technology provider/runtime | primarily `F-05`, `F-07`, `F-08` | technology executes work; it must not own the only copy of authority/history/critical meaning |

## 10. What is deliberately **not** a separate Company function now

AC-201 rejects the following as separate Company functions/departments **at the current evidence level**:

### 10.1 Dedicated Sales department

The Company has real opportunity/scoping work and now has a bounded flagship discovery instrument, but it does not yet have evidence of a repeatable acquisition funnel, sales capacity model or workload requiring an independent Sales department. The current need is covered by `F-02`.

### 10.2 Separate Marketing department

Positioning and discovery support real commercial work, but current evidence does not establish a standalone marketing operating function with independent accountable output sufficient to justify separate organizational treatment. Market learning remains inside `F-02` and later commercial evidence may change this.

### 10.3 Separate Customer Success / Support department

Support and acceptance are real, but their current business meaning is inseparable from delivery, feedback and closure. They remain within `F-03` until workload/economics justify separation.

### 10.4 Separate Project Management / PMO department

Coordination is real, but the current need is workstream/customer delivery state plus portfolio/product stewardship, not an independent PMO bureaucracy. It is covered by `F-03`, `F-04` and `F-07`.

### 10.5 Internal Accounting department

Transaction/statutory accounting is professionally outsourced. The Company requires `F-06` management finance, not duplicated bookkeeping headcount.

### 10.6 Separate Legal department

The Company has legal/corporate obligations and requires a valid authority/legal interface through `F-01`, but current evidence does not justify dedicated internal legal headcount. External professional/legal authority remains external where applicable.

### 10.7 HR / People function

No current evidence supports a distinct personnel/hiring workload requiring a separate Company-level function. Future real hiring, employment, contractor or capacity needs may justify one later; AC-201 does not create it in advance.

### 10.8 “AI Workforce”, “Agent Department” or model-specific function

AI is an executor class, not a business function or authority source. A model/provider/agent framework must never become a department merely because many tasks use it.

### 10.9 Procurement as the Company-wide core department

Procurement remains a real business/domain line and potential module, but the approved flagship correction explicitly rejects procurement as the highest-level Company identity. Procurement-specific operations remain product/workstream/domain semantics under the applicable product/business line and may later justify their own Position/module design without becoming a universal Company function.

### 10.10 Arvectum OS platform operations as a Company department

Arvectum OS is a separate canonical platform repository/governance scope. Company reliance may later require an operating responsibility, but AC-201 does not create a Company OS department or make current Provisional/Incubating platform state a Company-critical universal dependency.

## 11. Function criticality and continuity handoff

AC-201 does not set RTO/RPO or final criticality tiers, but it identifies which functions cannot remain dependent on one current executor without a later continuity decision.

| Function | Consequence if unowned or unavailable | AC-207 focus |
|---|---|---|
| `F-01` | Company may lose strategic/corporate/material-decision ability | preserve lawful authority gates; prepare/queue bounded work; distinguish short absence from legal/corporate continuity |
| `F-02` | growth/qualification stops and new work may be mis-scoped | preserve discovery/scoping state; another executor should be able to reconstruct what is known/unknown |
| `F-03` | existing customer obligations, acceptance and support may stall | reconstruct scope, current state, customer inputs, exceptions and next commitment-safe action |
| `F-04` | portfolio priorities/workstreams drift and Owner switching load rises | preserve current purpose/status/priority/stop criteria and product-repo pointers |
| `F-05` | technical delivery can stop | reproducible build/test/release/re-bootstrap and replacement-runtime paths where material |
| `F-06` | material spending/commitment decisions may proceed without sufficient economic evidence or must stop | ensure decision-relevant cash/obligation exceptions can reach management even if one tool/provider is unavailable |
| `F-07` | current organizational state/history may become difficult to reconstruct | independent recoverable canonical history and clear reconciliation after outages |
| `F-08` | unsafe access, data exposure or unrecoverable dependency can turn a workstream problem into Company risk | recovery/rotation/revocation/degraded-mode evidence proportional to criticality |

Detailed continuity ownership remains AC-207 after authority, Position, Assignment and access design have progressed.

## 12. Downstream Phase 2 handoff

### AC-202 — Reserved Owner Decisions

AC-202 must use this function model to decide which decisions within `F-01` and which material gates across `F-02`, `F-03`, `F-04`, `F-06`, `F-07` and `F-08` remain reserved to the Owner rather than treating entire functions as Owner-reserved.

The important distinction is:

```text
function responsibility ≠ decision authority ≠ execution assignment
```

### AC-203 — Delegated Position authority, approval and escalation model

AC-203 must define how bounded authority can flow to future Positions while material limits, escalation and approval remain explicit.

### AC-204 — Initial Position Registry

AC-204 may derive Positions only where the eight functions show enough distinct responsibility, workload, control need or economic value. It must not mechanically create one Position per function.

### AC-205 — Initial Assignments and executor classification

Only after Positions exist may current/future human, AI, software or hybrid execution be represented as Assignments. Current AI/software usage does not prejudge the result.

### AC-206 — Company data/tool/credential access boundary baseline

AC-206 should derive minimum access needs from function/Position responsibilities and keep least privilege, customer sovereignty and credential recovery explicit.

### AC-207 — Critical-function continuity, replacement and manual fallback baseline

AC-207 must prove that function meaning survives executor/runtime/device/vendor replacement and that deliberate authority/security gates are not bypassed for convenience.

### AC-208 — Transferability boundary and operating-model cross-review

AC-208 must determine which aspects of this eight-function Arvectum model are reusable method/pattern evidence and which are Arvectum-specific facts that a customer organization must not copy blindly.

## 13. Reference-implementation learning for the flagship

AC-201 produces one important flagship lesson already supported by internal evidence:

> The reusable commercial method is **not** an Arvectum org chart. The reusable method is the derivation procedure that starts from value streams, obligations, workload, control needs and risks and only then creates functions, authority, Positions and executor Assignments.

The Arvectum function set is therefore reference evidence, not a customer template.

A customer diagnostic should use the same sequence:

```text
customer value streams / obligations / bottlenecks
→ minimal customer functions
→ reserved/delegated authority
→ Positions
→ workflows / evidence / data / tools
→ human | AI | software Assignments
→ governed execution / fallback
```

The customer may end with fewer, more or entirely different functions.

## 14. Prospective evidence to capture

Before M2 closes, real work should begin capturing lightweight evidence that tests whether the function boundaries are correct:

- material Owner interventions by function;
- handoff failures or duplicated responsibility between functions;
- customer rework caused by missing F-02/F-03 state;
- technical work blocked because F-04 priority or F-03 acceptance meaning is unclear;
- material commitment blocked because F-06/F-08 evidence is missing;
- state reconstruction work attributable to F-07 gaps;
- repeated work that suggests one function needs a distinct Position;
- functions that remain too broad or prove unnecessary;
- cases where product/customer/external authority was accidentally pulled into Company scope;
- internal patterns that appear transferable only after real operating evidence.

This evidence should inform AC-204 through AC-208. It does not require a heavyweight workflow suite or dashboard at AC-201.

## 15. Completion boundary

AC-201 is complete when the Company can explain, from M1 evidence:

- the smallest current set of durable Company-level functions;
- why each function exists in business/obligation/control terms;
- the accountable outcome and major boundary of each function;
- the current Owner/executor concentration without converting it into a final org chart;
- the distinction between Company function, product/domain responsibility, external professional/authority interface and OS responsibility;
- which familiar enterprise departments are **not** justified yet;
- the major function handoffs that later authority/Position/workflow design must make explicit;
- why AI/software are executor choices rather than functions/authority sources;
- how the model informs the flagship method without becoming a fixed customer template.

This publication satisfies that boundary with eight Company-level function domains and without inventing Positions, delegation, headcount, access grants, customer organization design, module admission or Arvectum OS lifecycle effects.

Cross-review result: `PASS at iteration 9 of maximum 10`.

Next roadmap action: `AC-202 — Reserved Owner Decisions`.
