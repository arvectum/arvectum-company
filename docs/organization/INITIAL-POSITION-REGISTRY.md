# AC-204 — Initial Position Registry

Status: `Proposed`
Version: `0.9.0`
Created: `2026-08-20`
Updated: `2026-08-20`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-204 — Initial Position Registry`
Review: `docs/reviews/AC-204-INITIAL-POSITION-REGISTRY-CROSS-REVIEW.md`
Depends on: AC-201 function model; AC-202 Reserved Owner Decisions `1.0.0`; AC-203 Delegated Position Authority Model `1.0.0`; M1 business/workload/risk evidence
Approval required: explicit Owner approval before these Positions become binding Company organizational state

## 1. Purpose

AC-204 defines the **smallest evidence-backed initial set of durable Arvectum Company Positions** needed to carry the real Company functions established by AC-201 without creating fake headcount, conventional departments or AI-agent job slots.

The task answers:

> Which durable accountability units must exist now so the Company can separate responsibility, authority, execution and continuity — even if one person, several AI/software executors or a hybrid arrangement later carries several of them?

The governing sequence remains:

```text
real business responsibility
→ Company function
→ Position
→ Position authority envelope
→ Assignment of Principal
→ technical/data/tool access
→ governed execution / evidence / continuity
```

This artifact creates **Position definitions only after Owner approval**. It does not assign any named human, AI, software service or runtime; does not create employment/headcount; does not grant credentials or legal authority; and does not make one Position equal to one employee.

## 2. Governing and evidence boundary

AC-204 is subordinate to:

1. applicable law and valid legal/corporate authority of ООО «Арвектум»;
2. the acting charter and valid corporate decisions;
3. the Ratified Company Constitution `1.0.0`;
4. Approved AC-202 Reserved Owner Decisions `1.0.0`;
5. Approved AC-203 Delegated Position Authority Model `1.0.0`;
6. the AC-201 minimal real function model;
7. approved Company governance and explicit Owner decisions;
8. product-specific canonical authority in product scope;
9. customer authority and rights in customer scope;
10. applicable Arvectum OS governance/contracts where Company work actually relies on OS.

The main evidence inputs are AC-104 Owner-workload/bottleneck evidence, AC-105 dependency/continuity evidence, AC-201's eight functions and the current portfolio map with multiple active product/workstream nodes.

Arvectum OS `main` was re-checked for AC-204 at `dff9591a9897743c48c56bbe2320260c2e0a071c`. The OS Constitution remains Ratified `1.2.0`; the OS Decision Authority Policy remains Proposed `0.2.1`. AC-204 creates no OS Position, Product Contract, capability lifecycle change or platform authority claim.

## 3. Position admission test

A separate Position is admitted only when all of the following are satisfied:

1. there is a durable current business responsibility, recurring workload, accountability need or material control need;
2. the responsibility has a distinguishable accountable outcome and handoff;
3. leaving the responsibility implicit would preserve a material Owner bottleneck, ambiguity, control gap or continuity risk;
4. the Position remains meaningful if today's human/AI/software executor changes;
5. the responsibility is Company-owned rather than customer-, product-, legal/corporate-, accounting/banking- or OS-owned;
6. creating a separate Position reduces more ambiguity/control risk than organizational overhead;
7. the Position can be described without inventing a department, future staffing plan or unsupported authority.

A function does not automatically become a Position. Several functions may be bundled when current scale, context continuity and control design make one accountability boundary more useful than multiple handoffs.

## 4. Non-Position authority and service anchors

The following are important to Company operation but are **not created as Positions by AC-204**:

| Anchor | Status in this model | Boundary |
|---|---|---|
| Owner | Authority Principal/capacity, not a Position | retains AC-202 `ROD-*` final decisions and residual authority where no valid delegation exists |
| participant/general meeting competence | legal/corporate authority, not an internal Position | determined by law/charter/corporate acts |
| General Director legal office | legal/corporate capacity, not created by this registry | a later Assignment may coincide with an internal Position, but Position title never creates General Director powers |
| outsourced accounting/tax service | external professional interface | transaction/statutory truth remains outside Company Position semantics |
| bank/payment system and authorized bank actors | external/legal/technical interface | technical payment ability does not create Company Organizational Authority |
| customer authorized Principals | external customer authority | Company Positions cannot approve on behalf of the customer |
| Arvectum OS governance actors | separate OS governance scope | Company Position does not approve OS RFC/ADR/Product Contract/capability changes by implication |

This separation is particularly important because the same natural person may currently carry Owner, participant, General Director and one or more future Position Assignments. Their authority sources remain distinct.

## 5. Initial Position Registry

AC-204 admits **five** current Company Positions.

They cover the eight AC-201 functions without creating eight jobs or conventional departments.

| ID | Position | Current lifecycle state | Primary AC-201 coverage | Why a distinct Position exists |
|---|---|---|---|---|
| `POS-001` | Company Executive | `Required / Defined — Unassigned` | `F-01`, with integration interfaces to `F-04`, `F-06`, `F-07`, `F-08` | the Company needs one durable operating integration/accountability boundary that converts valid Owner/corporate decisions into coordinated Company action, resolves non-reserved cross-function conflicts and escalates material decisions without making the Owner the scheduler of every routine action |
| `POS-002` | Commercial & Customer Lead | `Required / Defined — Unassigned` | `F-02` + `F-03` | discovery/scoping and delivery/acceptance currently depend on the same fragile customer context; at present scale one end-to-end customer accountability boundary reduces context loss better than separate Sales/Customer Success Positions |
| `POS-003` | Portfolio & Product Lead | `Required / Defined — Unassigned` | `F-04` | multiple products/workstreams compete for priority and reuse/productization interpretation; this responsibility must be separated from both Owner-reserved portfolio decisions and raw engineering execution |
| `POS-004` | Engineering & Release Lead | `Required / Defined — Unassigned` | `F-05` | technical decomposition, implementation, QA, packaging and release evidence form a durable production accountability boundary that is already highly automatable but must remain subordinate to business scope and acceptance |
| `POS-005` | Company Operations & Assurance Lead | `Required / Defined — Unassigned` | `F-06` + `F-07` + `F-08` | management finance evidence, organizational state, access/risk/continuity assurance are real but individually do not yet justify CFO/CISO/PMO/Governance headcount; one control/evidence Position is the minimum current boundary so long as it does not receive self-approving material authority |

`Unassigned` means AC-205 has not yet mapped Principals/executor classes. It does **not** mean the work is currently undone; it means current execution concentration is intentionally not converted into canonical Assignment until AC-205.

## 6. `POS-001 — Company Executive`

### 6.1 Purpose

Provide the durable Company-level operating integration boundary between Owner/corporate authority and the Company's delegated routine work.

This Position exists so that preserving Owner control does not require the Owner personally to perform every coordination, evidence-routing, publication or non-reserved sequencing action.

### 6.2 Accountable outcomes

The Position is accountable for ensuring that:

- approved Company strategy/priorities are translated into bounded current operating direction;
- decisions requiring Owner or legal/corporate authority arrive as decision-ready escalations rather than raw context;
- non-reserved cross-Position conflicts are resolved within approved bounds or escalated;
- approved decisions are converted into explicit accountable next actions and state changes;
- material external/corporate actions are routed to the proper legally authorized Principal rather than inferred from Position title;
- Company-level priorities and material exceptions remain reconstructable.

### 6.3 Boundary

The Position does not own:

- `ROD-01` through `ROD-09` final decisions;
- participant/general-meeting or General Director legal competence merely because it is named `Company Executive`;
- product implementation truth;
- customer authority;
- OS governance;
- accounting transaction truth.

### 6.4 Initial authority envelope

Permitted Position modes after approval and valid Assignment:

- `AM-0` — prepare/recommend Company decisions and options;
- `AM-1` — execute/publish/synchronize already approved Company decisions and routine governance mechanics;
- `AM-2` — make routine internal sequencing/coordination decisions inside already approved strategy, workstream, budget/risk/commitment boundaries.

Not admitted initially:

- `AM-3` delegated consequential approval;
- `AM-4` automatic consequential execution.

Those modes require later explicit evidence, eligibility/workflow and authority changes; their absence is deliberate, not a permanent prohibition.

### 6.5 Escalation

Escalate to the Owner for any `ROD-*`, material exception or absent/ambiguous envelope; to the legally competent actor for corporate/legal acts; and to customer/Product/OS authority where the affected scope belongs there.

### 6.6 Split/merge evidence triggers

Review this Position if:

- routine Company operations become large enough for a separate COO-like Position;
- portfolio stewardship becomes a full operating load independent of Company integration;
- management finance/control volume requires a separate finance-control Position;
- the Position becomes a new universal-interpreter bottleneck rather than an integration boundary.

## 7. `POS-002 — Commercial & Customer Lead`

### 7.1 Purpose

Own the reconstructable customer value path from discovery/qualification through committed delivery, acceptance and bounded support while separating customer context from Owner memory.

The Position intentionally combines AC-201 `F-02` and `F-03` at the current scale.

### 7.2 Why discovery and delivery are bundled now

Current evidence does not justify separate Sales, Account Management, Customer Success or Support Positions. Splitting them now would create additional handoffs around the very customer context that AC-104/AC-105 identify as fragile.

The Position may split later when a repeatable acquisition engine, customer volume, independent workload or control conflict produces evidence for separation.

### 7.3 Accountable outcomes

- each qualified opportunity has an evidence-backed problem/outcome/scope/readiness package;
- commitment preparation states inclusions, exclusions, uncertainties and required customer inputs;
- committed engagements have reconstructable current state;
- defect vs agreed scope vs change request vs customer-blocked state is classified explicitly;
- customer validation/acceptance/support state is visible and bounded;
- no routine customer communication silently creates a new promise or authority.

### 7.4 Initial authority envelope

Permitted after valid Assignment:

- `AM-0` — discovery, research, qualification evidence, proposal/scope drafts;
- `AM-1` — execute already committed delivery/customer-process steps;
- `AM-2` — routine qualification, issue classification, customer follow-up, scheduling and delivery coordination inside accepted scope and approved criteria.

Not admitted initially:

- `AM-3` consequential commercial/customer approval;
- `AM-4` automatic customer-facing consequential effect.

Hard exclusions include material/non-standard commitments under `ROD-03`, material risk exceptions under `ROD-06`, data-rights/sovereignty exceptions under `ROD-07`, and any strategic/business-model case entering `ROD-01`.

The Position cannot approve on behalf of a customer.

### 7.5 Major handoffs

- to `POS-001` / Owner for material commitment or exception;
- to `POS-003` when customer evidence raises productization/reuse/portfolio questions;
- to `POS-004` for technical decomposition and delivery;
- to `POS-005` for management-finance, data, access, risk or continuity constraints.

### 7.6 Split evidence triggers

Consider separate Commercial and Customer Delivery/Success Positions when one or more are observed:

- repeatable acquisition pipeline with independently measurable workload;
- multiple concurrent customers causing context queues;
- acquisition incentives materially conflict with delivery/acceptance control;
- support load becomes a durable business capability rather than extension of delivery;
- customer handoff can be made reliably without reintroducing Owner interpretation.

## 8. `POS-003 — Portfolio & Product Lead`

### 8.1 Purpose

Own Company-level portfolio/product/workstream interpretation and routine stewardship without becoming the canonical owner of product implementation.

### 8.2 Accountable outcomes

- each material portfolio node has current purpose, lifecycle/status reference and accountable question;
- routine priority proposals are coherent with approved Company strategy and P0–P3 sequencing;
- product/workstream state points to the actual product canonical source;
- continue/change/stop/reuse/module-candidate evidence is assembled before material Owner decisions;
- customer-specific corrections are not silently promoted into reusable product investment;
- reusable patterns are not silently promoted into Arvectum OS.

### 8.3 Initial authority envelope

Permitted after valid Assignment:

- `AM-0` — portfolio/product analysis, investment/reuse recommendations;
- `AM-1` — synchronize approved portfolio decisions and status references;
- `AM-2` — routine prioritization/status coordination inside an already approved portfolio/workstream envelope.

Not admitted initially:

- `AM-3` approval of major portfolio/product investment changes;
- `AM-4` automatic portfolio stop/start/reclassification.

Hard exclusions include `ROD-02`, `ROD-04`, material `ROD-09` and any strategy change under `ROD-01`.

The Position does not grant product-local implementation authority merely because a product is in the Company portfolio.

### 8.4 Major handoffs

- `POS-001` / Owner for material investment, stop/continue or cross-boundary decision;
- `POS-002` for market/customer evidence;
- `POS-004` for technical/release feasibility and evidence;
- `POS-005` for economics, dependency, risk and continuity evidence.

### 8.5 Split evidence triggers

Phase 3 may justify product-specific Positions when individual products have enough independent revenue, customer obligations, roadmap complexity, investment or domain accountability. AC-204 does not create one Product Manager per repository merely because seven portfolio nodes exist.

## 9. `POS-004 — Engineering & Release Lead`

### 9.1 Purpose

Own the durable technical-production accountability boundary for accepted workstreams while keeping technical success separate from business/customer authority.

### 9.2 Accountable outcomes

- accepted work is decomposed into implementable technical work;
- implementation has proportionate automated/manual verification;
- releases/artifacts are reproducible enough for their declared criticality;
- known limitations and test evidence are explicit;
- technical defects are corrected or escalated;
- release readiness is handed back to the business/customer/product authority that owns acceptance/commitment.

### 9.3 Initial authority envelope

Permitted after valid Assignment:

- `AM-0` — technical analysis/design recommendations;
- `AM-1` — execute approved implementation, QA, packaging and release mechanics;
- `AM-2` — routine reversible engineering/tool/testing choices inside accepted workstream, architecture/risk/data constraints and product scope.

Not admitted initially:

- `AM-3` consequential release/business approval;
- `AM-4` Company-level automatic consequential execution.

Build/test automation may later use `AM-4` only when a concrete workflow has been pre-authorized under AC-203; AC-204 does not activate that automation class.

Hard exclusions include customer/commercial commitments, capital decisions, material risk/data exceptions and any `ROD-*` boundary case.

### 9.4 Product boundary

This Position does not make the Company repository canonical for product code or detailed product architecture. Product-specific technical authority remains in the corresponding product canonical scope.

### 9.5 Major handoffs

- `POS-002` for exact customer scope, validation and acceptance meaning;
- `POS-003` for product/workstream priority and reuse decisions;
- `POS-005` for security/access/dependency/continuity constraints;
- `POS-001` / Owner where a technical option changes material business/risk/commitment state.

### 9.6 Split evidence triggers

Review for product/domain-specific engineering Positions when technical workload, independent release accountability, specialized risk or product scale makes one Company technical boundary a bottleneck or obscures product ownership.

## 10. `POS-005 — Company Operations & Assurance Lead`

### 10.1 Purpose

Provide the minimum current control/evidence Position for management economics, organizational state, access/risk/continuity assurance without prematurely creating separate Finance, PMO/Governance, Security or Risk departments.

This Position combines `F-06`, `F-07` and `F-08` because each is real today, but current evidence supports one shared preparation/monitoring/control boundary rather than three separate executive positions.

### 10.2 Accountable outcomes

- decision-makers receive decision-relevant cash/cost/obligation/economic evidence without duplicating statutory accounting;
- material due/receivable/payable/mandatory-payment exceptions are surfaced to the appropriate authority;
- Company roadmap/decision/review/organizational state remains reconstructable and synchronized with canonical sources;
- access/data/risk/continuity requirements are explicit for material work;
- incident, dependency and continuity exceptions are classified/escalated;
- approved safe containment/recovery mechanics can be executed without inventing risk-acceptance authority;
- external accounting/banking/customer/product/OS source authority is preserved rather than copied into Company truth.

### 10.3 Initial authority envelope

Permitted after valid Assignment:

- `AM-0` — management reporting, risk/dependency analysis, evidence/review preparation;
- `AM-1` — execute approved state synchronization, reporting mechanics, access revocation/rotation or continuity procedures where a valid policy/workflow exists;
- `AM-2` — routine classification, exception routing and reversible control/operational choices within approved policy/data/risk boundaries.

Not admitted initially:

- `AM-3` material finance/risk/security approval;
- `AM-4` Company-level automatic consequential effect.

Pre-authorized monitoring/containment/recovery automation may later be admitted through a concrete `AM-4` workflow after AC-206/AC-207 evidence.

Hard exclusions include `ROD-02`, `ROD-05`, `ROD-06`, `ROD-07`, `ROD-08` and material `ROD-09` cases.

### 10.4 Independence rule

Because this Position combines preparation/monitoring across finance, evidence, security and continuity, it must not become the sole approver of its own material exceptions.

The initial absence of `AM-3` is an intentional control. If future scale requires independent assurance or delegated consequential approval, the Company should split the relevant responsibility or introduce an independent approval path rather than grant self-review authority for convenience.

### 10.5 Split evidence triggers

Review for separate Positions if:

- management finance becomes a sustained independent workload with delegated spending/approval needs;
- security/privacy/customer-data exposure requires independent assurance or regulated specialization;
- organizational state/work coordination becomes a large operating function rather than lightweight evidence management;
- continuity/incident workload becomes independently material;
- combining preparation and assurance creates repeated independence conflicts.

## 11. Function-to-Position coverage matrix

| AC-201 function | Primary Position | Secondary interfaces | Coverage decision |
|---|---|---|---|
| `F-01` Company Direction / Governance / Material Control | `POS-001` | `POS-003`, `POS-005` | non-reserved operating integration is a Position; Owner/corporate reserved authority stays outside the Position |
| `F-02` Commercial Discovery / Qualification / Commitment Preparation | `POS-002` | `POS-001`, `POS-005` | bundled with F-03 to preserve customer context at current scale |
| `F-03` Customer Delivery / Acceptance / Support | `POS-002` | `POS-004`, `POS-003`, `POS-005` | bundled with F-02 until workload/control evidence justifies a customer handoff split |
| `F-04` Portfolio / Product / Workstream Stewardship / Reuse | `POS-003` | `POS-001`, `POS-002`, `POS-004`, `POS-005` | separate Position because portfolio switching/reuse interpretation is a distinct Owner bottleneck and should not be fused into engineering |
| `F-05` Engineering / Automation / QA / Release | `POS-004` | `POS-002`, `POS-003`, `POS-005` | separate production accountability because execution is high-volume/automatable and must remain distinct from acceptance/investment authority |
| `F-06` Management Finance / Cash / Obligation Control | `POS-005` | `POS-001`, `POS-003` | bundled into Operations & Assurance; no internal Accounting Position |
| `F-07` Organizational State / Evidence / Improvement | `POS-005` | all Positions | bundled into Operations & Assurance to eliminate state reconstruction without creating a PMO/governance department |
| `F-08` Security / Access / Risk / Continuity Assurance | `POS-005` | all Positions | bundled into Operations & Assurance with no material self-approval; detailed access/continuity remains AC-206/AC-207 |

All eight functions have one primary Position accountability boundary; no function is left ownerless and no Position is created merely to mirror a function label.

## 12. Initial authority-mode matrix

This matrix defines the **Position design ceiling** for the initial registry. Actual executable authority still requires valid AC-205 Assignment, AC-206 technical access where needed and all current workflow/data/risk conditions.

| Position | `AM-0` | `AM-1` | `AM-2` | `AM-3` initial | `AM-4` initial |
|---|---:|---:|---:|---:|---:|
| `POS-001` Company Executive | yes | yes | yes | no | no |
| `POS-002` Commercial & Customer Lead | yes | yes | yes | no | no |
| `POS-003` Portfolio & Product Lead | yes | yes | yes | no | no |
| `POS-004` Engineering & Release Lead | yes | yes | yes | no | no |
| `POS-005` Company Operations & Assurance Lead | yes | yes | yes | no | no |

This is intentionally conservative. AC-203 makes `AM-3` and `AM-4` possible, but current AC-204 evidence does not yet identify Principal eligibility, concrete consequential approval classes or sufficiently specified automatic workflows to activate them safely.

A future amendment may add them with evidence; title or Assignment alone cannot.

## 13. Company value/control flow through Positions

```text
external need / current obligation
        ↓
POS-002 Commercial & Customer Lead
        ↓ qualified scope / commitment preparation
POS-005 economics / risk / data evidence
        ↓
POS-001 Company Executive
        ↓ routine delegated coordination
        └→ Owner / legal-corporate gate when ROD/material act required
        ↓ accepted bounded work
POS-002 customer/delivery state
        ↕
POS-003 portfolio/product stewardship
        ↕
POS-004 engineering / QA / release
        ↓
customer validation / acceptance state
        ↓
POS-005 economic closure / evidence / risk / organizational state
        ↓
POS-003 continue/change/stop/reuse recommendation
        ↓
POS-001 / Owner as required by authority class
```

`POS-005` also constrains material paths with access/data/risk/continuity requirements.

The flow deliberately prevents `POS-004` technical success from becoming customer acceptance, portfolio investment or Owner approval by implication.

## 14. Positions deliberately not admitted now

The initial registry does **not** create separate Positions for:

- Sales;
- Marketing;
- Customer Success / Support;
- Project Manager / PMO;
- CFO / internal Accountant;
- Legal Counsel;
- HR / People;
- CISO / Security Officer;
- Risk Officer;
- Knowledge Manager / Governance Officer;
- AI Workforce Manager / Agent Manager;
- Arvectum OS Operator;
- Procurement Director as a Company-wide role;
- one Product Manager/Product Owner per portfolio repository.

Some may become justified later. Their familiar corporate labels are not evidence of current business need.

## 15. One Position is not one person or one agent

This registry contains five Positions, not a five-person staffing plan.

AC-205 may find that:

- one human Principal temporarily holds several Position Assignments;
- one Position is executed by a hybrid human + AI/software Assignment pattern;
- AI/software performs substantial `AM-0`/`AM-1`/`AM-2` work while a human remains responsible for bounded approval/escalation;
- an external professional service provides inputs to a Position without becoming the Position or Company authority;
- one Position eventually needs several Principals or a rotation for continuity.

The important invariant is that Position meaning, accountable outputs, authority boundary and history survive executor replacement.

## 16. Position conflict and separation rules

AC-205 may assign the same Principal to several Positions initially, but the Company should preserve their distinct decision contexts and evidence where conflicts matter.

The following combinations require explicit caution if held by one Principal:

- `POS-002` commercial/customer commitment preparation + `POS-004` technical readiness: technical optimism must not silently broaden customer scope;
- `POS-003` investment/priority recommendation + `POS-004` engineering execution: implementation sunk cost must not become portfolio authority;
- `POS-005` assurance evidence + any Position whose exception is being reviewed: no material self-approval;
- `POS-001` operating integration + Owner capacity: routine Company Executive work should not be reclassified as Owner-reserved merely because the same person currently holds both capacities.

These are separation-of-context rules, not mandatory current headcount separation.

## 17. Position lifecycle and change triggers

Position lifecycle states are:

- `Proposed` — designed but not approved;
- `Defined — Unassigned` — approved Position exists, no canonical Assignment yet;
- `Assigned` — one or more active AC-205 Assignments exist;
- `Suspended` — Position remains meaningful but execution is intentionally paused;
- `Retiring` — responsibilities are being transferred;
- `Retired` — Position no longer exists as active organizational accountability, with history preserved.

A Position should be reviewed for split, merge or retirement when operating evidence shows:

- repeated handoff failure or accountability ambiguity;
- persistent workload queue or excessive context switching;
- material conflict of duties;
- a function becomes unnecessary or externalized;
- a new function/accountability becomes materially distinct;
- one Position repeatedly escalates work that a stable delegated envelope could own;
- customer/product scale creates durable product/domain-specific responsibility;
- the economic value of maintaining the Position no longer exceeds its governance/coordination cost.

Changing the executor does not by itself justify changing the Position.

## 18. Handoff to AC-205

AC-205 must classify the current/future executor realization for each approved Position without changing the Position merely to fit a preferred model or agent.

For each Position AC-205 should determine:

- assigned Principal(s) or current unfilled state;
- executor class: human / AI / software / external-service interface / hybrid;
- Assignment scope relative to the Position authority ceiling;
- accountability and supervision model;
- duration/review condition;
- known executor-specific limitations;
- replacement/fallback expectations handed onward to AC-207.

AC-205 MUST NOT infer technical access from Assignment. AC-206 owns the actual data/tool/credential access boundary.

## 19. Completion and approval boundary

AC-204 is substantively complete when the Company can explain:

- why each initial Position exists from real business evidence;
- why five Positions are enough to cover the current eight functions without fake headcount;
- why some functions are bundled and others separated;
- which outcomes each Position owns;
- the initial AC-203 authority-mode ceiling and AC-202 exclusions;
- the principal handoffs/escalation paths;
- which familiar Positions are deliberately not justified yet;
- how Positions remain independent of current human/AI/software execution;
- what evidence would cause split, merge or retirement;
- how AC-205 can assign executors without redesigning the organization around technology.

This `0.9.0` publication is a **proposal only**.

Because approving the initial Position Registry materially changes Company organizational accountability under `ROD-05`, it requires an explicit Owner approval of the exact reviewed proposal before the Positions become binding Company state.
