# AC-205 — Initial Assignments and Executor Classification

Status: `Proposed`
Version: `0.9.0`
Created: `2026-08-20`
Updated: `2026-08-20`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-205 — Initial Assignments and executor classification`
Review: `docs/reviews/AC-205-INITIAL-ASSIGNMENTS-CROSS-REVIEW.md`
Depends on: AC-204 Initial Position Registry `1.0.0`; AC-203 Delegated Position Authority Model `1.0.0`; AC-202 Reserved Owner Decisions `1.0.0`
Approval required: explicit Owner approval before these Assignments become binding Company organizational state

## 1. Purpose

AC-205 maps the **initial executor realization** of the six approved Company Positions without changing their meaning to fit today's Owner concentration, a preferred AI model, a software tool or an external service.

The governing distinction remains:

```text
Position = durable accountability / authority boundary
Principal / Assignment = who or what currently carries the Position
Runtime / tool = replaceable execution mechanism
```

An Assignment does not create authority beyond the Position ceiling and does not imply technical access. Effective execution remains bounded by AC-203:

```text
Position authority envelope
∩ Assignment scope
∩ technical authorization/access
∩ current workflow/data/risk conditions
= maximum executable action
```

AC-205 does not grant credentials or data/tool access (AC-206), create new legal/corporate powers, amend `ROD-*`, activate `AM-3`/`AM-4`, create employment contracts or hire people.

## 2. Owner capacities remain distinct

The current Owner Principal may hold one or more Position Assignments while also acting in separate Owner, participant and General Director capacities.

These capacities MUST remain distinguishable:

- routine delegated Position decisions inside `AM-0`/`AM-1`/`AM-2` are Position acts;
- `ROD-01` through `ROD-09` final decisions are Owner acts;
- participant/general-meeting and General Director acts remain legally/corporately sourced acts;
- the fact that the same natural person currently performs several capacities does not merge their authority sources.

The Owner may originate a proposal or decision subject directly. AI recommendation is not a prerequisite to Owner action.

## 3. Executor classes used in this baseline

AC-205 uses the following executor classifications:

- `Human-led` — a human Principal is the primary Position holder/executor;
- `AI-led` — AI is the primary executor for the Position's admitted work classes, with mandatory escalation at authority/business/customer/risk boundaries;
- `Hybrid` — human and AI/software execution are intentionally combined while authority remains attributable to the applicable Position/Principal capacity;
- `External-service interface` — a professional/service provider supplies authoritative or specialist inputs/execution under its own contract/system boundary without becoming a source of Company Organizational Authority;
- `Conditional future human capacity` — no Principal is assigned yet, but a future scoped Assignment class is reserved once hiring/engagement and an explicit Assignment record exist.

## 4. Initial Assignment map

| Position | Initial realization | Human / authority role | AI / software role | External / future capacity |
|---|---|---|---|---|
| `POS-001 — Company Executive` | `Hybrid` | Current Owner Principal carries the human Position Assignment for routine Company integration and may also act separately in Owner/legal capacities when the matter requires it; Owner may originate direct proposals/decisions | AI acts as adviser, analyst, cross-reviewer, decision-packet preparer and approved state/publication assistant; no independent `ROD-*` authority | none initially |
| `POS-002 — Commercial & Customer Lead` | `Hybrid + future human sales capacity` | Current Owner Principal is the initial accountable human Position holder for customer/commercial meaning, commitment boundaries and exception handling | AI performs prospect discovery, research, enrichment, qualification preparation, message drafting and bounded outreach execution only inside an explicitly approved campaign/scope; no autonomous material commitment | outsourced accounting is a supporting external-service interface where commercial/payment/accounting facts are needed; future human sellers are reserved as scoped additional Assignments to this Position, not yet active Principals |
| `POS-003 — Portfolio & Product Lead` | `Hybrid` | Current Owner Principal carries the human Position Assignment for routine portfolio/product judgment and may make direct proposals; material `ROD-02`/`ROD-04`/`ROD-09` decisions remain Owner-capacity acts | AI performs portfolio synthesis, evidence gathering, cross-repository status analysis, option generation, productization/reuse analysis and decision preparation | none initially |
| `POS-004 — Engineering & Release Lead` | `AI-led` | no routine human co-holder is required for bounded engineering execution; Owner/customer/product authority remains outside the Position where business acceptance, material exception or reserved decision is required | AI is the primary executor for technical decomposition, implementation, testing, defect correction, packaging and routine reversible engineering decisions inside the approved workstream/product/risk/data boundary | product-specific tools/runtimes are replaceable execution mechanisms, not authority sources |
| `POS-005 — Finance & Obligation Control Lead` | `Human-led + external-service interface` | Current Owner Principal is the initial accountable Position holder for management-finance interpretation, cash/commitment awareness and obligation escalation | no standing AI co-holder is created by this baseline | outsourced accounting/tax service supplies transaction/statutory/accounting facts and professional execution under its own authoritative contour; it does not become Company Organizational Authority |
| `POS-006 — Security, Risk & Continuity Lead` | `Hybrid` | Current Owner Principal carries the human Position Assignment for bounded security/risk/continuity judgment and may originate direct proposals; material risk acceptance and sovereignty exceptions remain Owner-capacity `ROD-*` acts | AI advises, checks evidence, performs threat/dependency/continuity analysis, prepares options and reviews controls; AI does not independently accept material risk | product/runtime/security providers remain external/tool interfaces rather than Position authority |

## 5. Assignment details

### 5.1 `POS-001 — Company Executive`

**Human Assignment:** Current Owner Principal.

**Executor model:** Hybrid — `human decision/coordination + AI advisory/preparation`.

Human Position scope initially includes:

- routine Company sequencing and coordination within approved priorities;
- conversion of approved decisions into accountable next actions;
- resolving non-reserved cross-Position conflicts inside approved limits;
- maintaining the Company current-state boundary with AI assistance;
- originating direct operating/governance proposals without waiting for AI recommendation.

AI scope initially includes:

- `AM-0`: evidence assembly, analysis, alternatives, criticism/cross-review and decision packet preparation;
- bounded `AM-1`: publication/state synchronization after a valid decision and within AC-206 access;
- no independent `AM-2` Company Executive decision by this initial Assignment.

The Owner human Assignment may exercise `AM-0`/`AM-1`/`AM-2` within POS-001's approved non-reserved envelope. When the subject enters a `ROD-*` class, the same person acts in Owner capacity, not because POS-001 received reserved authority.

### 5.2 `POS-002 — Commercial & Customer Lead`

**Primary human Assignment:** Current Owner Principal.

**Executor model:** Hybrid with planned human sales capacity.

Owner scope initially includes:

- customer/problem interpretation;
- routine qualification and scope coordination;
- customer-context continuity;
- routine delivery/acceptance coordination;
- direct commercial proposals within the applicable authority boundary;
- escalation/decision for non-standard or material commitment cases through the proper Owner/legal path.

**AI commercial support Assignment class:**

AI/software may perform:

- prospect/company search and list building;
- public-source research and enrichment;
- first-pass ICP/qualification analysis;
- message and proposal drafting;
- outreach queue preparation;
- bounded sending/follow-up only where the campaign, target criteria, message class, frequency, opt-out/suppression rules and commitment boundary have been explicitly approved and AC-206 grants the necessary technical access.

AI outreach MUST NOT:

- create or imply a material/non-standard customer commitment;
- invent price, discount, SLA, warranty, scope or legal/data promise outside an approved envelope;
- continue when recipient/customer rights, suppression/opt-out state or data-processing purpose are unclear;
- infer authorization from possession of an email/CRM/API credential.

**Future human seller capacity:**

AC-205 reserves a `Conditional future human capacity` under POS-002. Future live sellers may become additional scoped human Assignments once actually engaged and explicitly recorded.

This reservation does **not** create employees or separate Sales Positions today. Initial seller scope should normally be limited to prospecting, approved outreach, qualification/follow-up and preparation inside bounded commercial rules. Authority to create material commitments remains excluded.

If seller workload later develops distinct durable accountability, incentive conflict or management structure, the Company should amend AC-204 and create a dedicated Sales Position class rather than pretending an Assignment has become a new Position by habit.

**Outsourced accounting interface:**

The accounting provider may supply payment, invoice, tax/accounting-status or other authoritative accounting facts needed for customer/commercial work, but does not occupy POS-002 and has no customer-commitment authority merely by providing those facts.

### 5.3 `POS-003 — Portfolio & Product Lead`

**Human Assignment:** Current Owner Principal.

**Executor model:** Hybrid — `human portfolio judgment + AI synthesis/advice`.

AI scope:

- portfolio/repository evidence gathering;
- status and dependency synthesis;
- option generation and critique;
- continue/change/stop/reuse/module-candidate preparation;
- approved portfolio-state synchronization.

Owner human Position scope:

- routine `AM-2` prioritization/status coordination inside the approved portfolio envelope;
- direct portfolio/product proposals;
- escalation into Owner capacity for `ROD-02`, `ROD-04`, material `ROD-09` or strategy decisions.

AI does not independently start/stop products, allocate material capital or change Company↔Product↔OS responsibility.

### 5.4 `POS-004 — Engineering & Release Lead`

**Primary Assignment:** AI-led.

The initial design deliberately makes this the first Position whose routine operating realization is predominantly AI rather than Owner-led.

AI scope may include:

- `AM-0`: technical analysis, design alternatives, implementation/release recommendations;
- `AM-1`: implementation, testing, defect correction, packaging and already-approved release mechanics;
- `AM-2`: routine reversible engineering, testing, tooling and implementation decisions inside accepted product/workstream architecture, data, security and risk bounds.

The AI-led Position MUST escalate when:

- product/customer scope or acceptance meaning is unclear;
- technical work would create a new commercial/customer commitment;
- a material security/data/dependency/risk exception is required;
- release has a consequential external effect outside an already approved execution class;
- the action enters any `ROD-*` class;
- authority/access is missing or the external effect has an uncertain outcome.

No `AM-3` or `AM-4` is activated by AC-205. Technical automation remains execution under the admitted `AM-0`/`AM-1`/`AM-2` envelope until a later explicit workflow-level approval changes that state.

AI model, coding agent, local runtime or vendor is **not** named as the Position itself and may be replaced without changing POS-004.

### 5.5 `POS-005 — Finance & Obligation Control Lead`

**Human Assignment:** Current Owner Principal.

**Supporting interface:** outsourced accounting/tax service.

The Owner Position Assignment owns management interpretation, not duplicate statutory accounting:

- decision-relevant cash/cost/commitment awareness;
- obligation and material due-date exception awareness;
- project/product economics interpretation where needed for decisions;
- preparation/escalation of material spend/capital/commitment questions.

The outsourced accounting provider remains authoritative for the professional/statutory/accounting work in its existing contour and supplies facts/reports required by POS-005.

The external accounting service:

- is not granted `ROD-*` authority;
- does not become the Company Position merely because it performs accounting work;
- does not receive customer/product/security authority by this interface;
- may only perform external effects through its valid legal/contractual/technical authority.

No standing AI Assignment is added to POS-005 in this baseline because the Owner direction specifies Owner + outsourced accounting as the initial realization. AI assistance may be added later if a real management-finance workflow and evidence justify it.

### 5.6 `POS-006 — Security, Risk & Continuity Lead`

**Human Assignment:** Current Owner Principal.

**Executor model:** Hybrid — `AI advisory/analysis + human judgment/decision`.

AI scope initially includes:

- threat/dependency/security review;
- access/risk/continuity evidence checks;
- alternative/mitigation preparation;
- technology-sovereignty and replacement-path analysis;
- incident/exception classification proposals;
- runbook/recovery critique and decision packets.

The Owner human Position Assignment may make bounded `AM-2` operational/risk-treatment decisions inside approved controls and may originate direct proposals.

Material risk acceptance, data-sovereignty exception, critical dependency exception or similar `ROD-06`/`ROD-07`/`ROD-08`/material `ROD-09` matter is decided by the same person in Owner capacity through the applicable explicit gate.

AI MUST NOT independently accept material risk, weaken mandatory controls, broaden data purpose, waive customer rights or treat technical admin permission as authority.

## 6. Current concentration map

The initial operating reality deliberately contains concentration:

- the current Owner Principal is the human holder of POS-001, POS-002, POS-003, POS-005 and POS-006;
- POS-004 is AI-led;
- outsourced accounting supports POS-005 and may provide bounded factual support to POS-002;
- future human sales capacity is reserved under POS-002 but not yet active.

This concentration is a **transition state**, not the target proof of an AI-native company.

The organizational value of AC-204/AC-205 is that the capacities are now distinguishable even while one person carries several of them. Later reassignment can therefore occur without redefining the Company each time.

## 7. Conflict-of-capacity controls

Because one human currently holds several Assignments, the following contexts must remain distinguishable:

- POS-002 commercial enthusiasm must not become POS-005 financial approval or POS-006 risk acceptance by implication;
- POS-003 portfolio sunk-cost preference must not become POS-004 technical evidence or Owner investment approval;
- POS-006 assurance criticism must remain reconstructable even when the same human ultimately decides an Owner-reserved risk case;
- POS-001 routine coordination must not be reclassified as Owner-reserved merely because the same person holds both capacities;
- the external accounting provider supplies accounting truth but does not approve commercial scope, portfolio priority or security exceptions.

For material decisions, the durable record should identify the capacity in which the human acted.

## 8. Supervision and escalation model

### Hybrid Positions (`POS-001`, `POS-003`, `POS-006`)

AI prepares, challenges and advises. The current Owner Principal performs the human Position decision work and separately performs Owner-reserved decisions when required.

### Commercial hybrid (`POS-002`)

AI may search, research, draft and later execute bounded approved outreach. Human seller Assignments may later perform scoped prospecting/outreach/qualification. The current Owner Principal remains the initial accountable Position holder and material commitment gate.

### AI-led Engineering (`POS-004`)

AI should not require Owner per-task approval for routine admitted `AM-1`/`AM-2` technical work. The design objective is autonomous bounded engineering execution with escalation only at scope, acceptance, risk, access, consequential external-effect or reserved-decision boundaries.

### Finance (`POS-005`)

The Owner performs management judgment; outsourced accounting supplies authoritative accounting/statutory inputs/execution. The two scopes must not be collapsed.

## 9. Assignment does not imply access

AC-205 makes **no claim** that the assigned executor already has every required repository, bank, email, CRM, customer, signing, local-device, security or other credential.

AC-206 must derive actual access from the approved Position/Assignment needs and apply least privilege.

In particular:

- AI commercial outreach is not operational until the approved outreach boundary and technical account access are explicit;
- AI engineering execution is limited by actual product/repository/runtime access;
- outsourced accounting access remains governed by its external/legal/service contour;
- Owner possession of a credential does not convert a Position or AI into the authority holder.

## 10. Continuity / replacement handoff to AC-207

AC-207 must test at least the following replacement questions:

- can POS-001/003/006 AI advisory execution be replaced without losing decision history or Position meaning;
- can POS-004 move between AI models/agents/runtimes or temporarily to human execution without losing engineering state;
- can another human later take a seller Assignment under POS-002 without reconstructing all customer/commercial meaning from Owner memory;
- can the accounting provider be changed while POS-005 management meaning and Company source documents remain recoverable;
- can the Owner be temporarily unavailable without AI or other executors inferring `ROD-*` authority;
- can the Finance and Security Position boundaries remain distinct even while the same human currently holds both.

## 11. Review / reassignment triggers

Review an Assignment when:

- workload becomes sufficient to move a Position away from the Owner;
- AI quality/cost/risk evidence supports broader or narrower scope;
- repeated escalation shows the Assignment scope is poorly calibrated;
- a new human seller is hired/engaged;
- an AI/runtime/provider is replaced;
- a security/finance conflict requires independent human separation;
- customer/portfolio scale creates a durable specialized Position need;
- an executor dependency becomes a material continuity risk.

Changing the executor should normally change the Assignment, not the Position.

## 12. Completion and approval boundary

AC-205 is substantively complete when the Company has an explicit initial realization for every approved Position, distinguishes Owner/Position/legal capacities, classifies AI/human/external execution, preserves accounting/customer/Product/OS boundaries, reserves future human seller capacity without fake hiring, and hands concrete access/continuity questions to AC-206/AC-207.

This `0.9.0` publication is a proposal only.

Because AC-205 creates real Position Assignments and determines where AI is the primary executor of a Company Position, binding publication requires explicit Owner approval of the exact reviewed proposal.