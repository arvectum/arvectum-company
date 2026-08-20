# AC-202 — Reserved Owner Decisions

Status: `Proposed`
Version: `0.9.0`
Created: `2026-08-20`
Updated: `2026-08-20`
Owner: `Owner of Arvectum Company`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-202 — Reserved Owner Decisions`
Review: `docs/reviews/AC-202-RESERVED-OWNER-DECISIONS-CROSS-REVIEW.md`
Depends on: Ratified Company Constitution `1.0.0`, AC-002 Company↔OS authority boundary, AC-104 Owner-workload baseline, AC-105 continuity/risk baseline, AC-201 minimal function model and AC-106 M1 priority decision
Approval required: explicit Owner approval of the exact reviewed proposal before this artifact becomes binding Company governance

## 1. Purpose

AC-202 defines the **smallest durable set of internal decision classes whose final Company decision remains reserved to the Owner** even after later Positions, delegations and human/AI/software Assignments are introduced.

The task exists to remove two opposite risks:

1. **loss of Owner control** — material strategy, capital, risk, authority or commitment changes occurring because a Position, AI, software service or technical operator can execute them; and
2. **Owner bottleneck by default** — every difficult, ambiguous or merely important task escalating to the Owner because the Company never distinguished a truly reserved decision from work that is only temporarily Owner-dependent.

The intended operating rule is:

```text
reserved final decision
→ Owner

bounded preparation / recommendation / routine decision / execution
→ accountable Position under AC-203 authority envelope
→ escalation only when the envelope is exceeded or authority is unclear
```

This artifact defines **decision authority**, not execution headcount. It does not create a Position, Assignment, system permission, bank mandate, power of attorney, customer commitment, Product Contract or Arvectum OS authority.

## 2. Governing and legal/corporate boundary

AC-202 is subordinate to:

1. applicable law and valid legal/corporate authority of ООО «Арвектум»;
2. the acting legal charter / standard charter and valid corporate decisions;
3. `docs/constitution/COMPANY-CONSTITUTION.md`;
4. approved Company governance and explicit Owner decisions;
5. `docs/governance/COMPANY-OS-AUTHORITY-BOUNDARY.md`;
6. product-specific canonical authority in product repositories within product scope;
7. applicable Arvectum OS canonical governance where Company work actually relies on OS.

The current Company source baseline evidences one participant, one General Director entitled to act without power of attorney and operation under standard charter No. 23. The standard charter identifies the general meeting of participants as the highest corporate body and the General Director as the sole executive body for current management, with competence determined by applicable law. AC-202 deliberately does not reproduce personal identifiers, signatures, address, banking details or other unnecessary source payload.

The current legal frame was re-checked for AC-202 against the Company-provided corporate sources and the current Federal Law No. 14-FZ framework. The legal/corporate competence list is **not duplicated here as an exhaustive static table** because applicable law and corporate facts may change and must be re-checked when a legal act is actually performed.

### 2.1 Owner, participant and General Director remain different capacities

The Company Constitution already requires these concepts to remain distinct even when the same natural person currently holds several capacities.

Therefore:

- an internal `Reserved Owner Decision` is an Organizational Authority act under Company governance;
- a matter legally reserved to the participant/general meeting remains a corporate matter and must use the applicable corporate form;
- an act requiring the General Director, power of attorney, bank authorization, electronic signature or another legally effective actor must still be executed by that actor;
- Owner approval **does not substitute** for the legally required act;
- legal capacity to sign or technically execute **does not substitute** for an internal Owner approval when this artifact reserves the Company decision.

If the Owner, participant and General Director cease to be the same Principal, this distinction becomes operationally mandatory rather than merely conceptual.

### 2.2 Corporate/statutory matters are higher-authority reservations

Questions that applicable law, the acting charter or another valid corporate source assigns to the participant/general meeting, General Director or another legally competent actor remain governed by that source.

AC-202 does not narrow, enlarge or transfer that competence.

Where a corporate/statutory question also falls into a Reserved Owner Decision class below, both gates apply:

```text
internal Owner decision
+ required corporate/legal act
+ required technical/execution authorization
```

No one gate implies the others.

## 3. Three authority buckets

AC-202 separates Company work into three buckets.

| Bucket | Meaning | Long-term rule |
|---|---|---|
| `A — Reserved Owner Decision` | final internal decision is intentionally retained by the Owner because it changes fundamental strategy, capital/risk, material commitments, authority architecture or similarly consequential Company state | AC-203 MUST NOT delegate the final decision unless AC-202 is explicitly amended and approved |
| `B — Delegable decision/action` | a decision or action may be performed by a Position inside explicit limits, evidence, approval and escalation rules | AC-203 should place it as close as practical to the accountable Position |
| `C — Temporary residual Owner authority` | a matter is not inherently reserved, but no approved delegation exists yet or the present facts exceed/leave unclear the current envelope | remains with Owner only until AC-203 or a later approved delegation makes the boundary explicit |

This distinction is essential.

`material` does **not** mean `permanently Owner-only`.

Until AC-203 is approved, the Company Constitution's residual-authority rule continues to apply to material matters not yet delegated. That is a **transition state**, not the target operating model.

## 4. Reserved Owner Decision admission test

A decision should remain Owner-reserved only when at least one of the following is true and the consequence is material to the Company:

1. it changes Company mission, strategic identity or a fundamental business-model direction;
2. it establishes or materially changes capital allocation, risk appetite or a major financial exposure boundary;
3. it creates a material external commitment or exception beyond an already approved bounded commercial/operational envelope;
4. it starts, stops or materially redirects a strategically significant portfolio initiative or investment;
5. it changes the constitutional/governance model, Reserved Owner Decision set or material delegation/authority architecture;
6. it accepts a material legal, security, privacy, data, reputational, continuity or sovereignty risk outside approved limits;
7. it materially changes ownership/control of critical Company IP, organizational assets or technology/data sovereignty;
8. it materially changes Company↔Product↔Arvectum OS responsibility or creates a new cross-repository/shared-platform obligation for the Company;
9. it changes the Owner's own residual authority or the mechanism by which that authority may be delegated or removed.

A decision **must not** be made Owner-reserved merely because it:

- is intellectually difficult;
- requires judgment;
- uses AI;
- involves a customer;
- touches code or production;
- has no existing playbook yet;
- is currently performed by the Owner;
- requires a privileged credential or local device;
- or feels important.

Those facts may require stronger evidence, approval or escalation, but they do not by themselves justify permanent Owner exclusivity.

## 5. Reserved Owner Decision catalog

### `ROD-01 — Mission, strategic direction and business-model identity`

**Owner-reserved final decisions:**

- adopt or materially change Company mission or the flagship commercial direction;
- enter, exit or fundamentally reposition a material business line when the decision changes the Company's strategic identity or capital/risk profile;
- materially change the Company-wide business-model architecture, including a shift in how the Company creates/captures value that is not already inside an approved strategy envelope;
- approve a strategic priority reversal that materially overrides the currently approved Company priority model rather than merely sequencing work inside it.

**Not reserved by this class:**

- market research, ICP research, discovery interviews and evidence collection;
- preparation of strategy options;
- routine prioritization inside approved portfolio/workstream bounds;
- product backlog decisions that do not change Company strategy.

### `ROD-02 — Capital allocation and material financial exposure`

**Owner-reserved final decisions:**

- establish or materially change Company capital-allocation principles and material spend/commitment limits;
- approve material capital deployment, recurring-cost exposure, financing or financial obligations outside an approved delegated/budget envelope;
- approve a material shift of Company capital/attention among major portfolio investments when it changes the accepted risk or strategic exposure;
- accept a material economics exception where expected value, downside, cash exposure or reversibility falls outside approved limits.

Where a financing, distribution, capital, guarantee, major transaction or similar act is governed by applicable law/corporate competence, the required legal/corporate act remains separate and controlling in its scope.

**Not reserved by this class:**

- preparation of cash/economic evidence;
- bookkeeping, tax calculation or bank reconciliation in the outsourced accounting contour;
- routine payment mechanics for already approved obligations where a valid authorization path exists;
- bounded spending inside a later approved AC-203 budget/authority envelope.

AC-202 deliberately invents **no ruble thresholds**. AC-203 and later financial governance must set bounded limits only from actual economics, risk and operating evidence.

### `ROD-03 — Material external commitments and non-standard commercial exposure`

**Owner-reserved final decisions:**

- approve a material customer, partner, supplier or public commitment outside already approved standard/bounded terms;
- approve a material exception involving liability, SLA/support burden, warranty, exclusivity, IP rights, data rights, confidentiality, indemnity, termination exposure or other non-standard obligation;
- approve the first or materially expanded design-partner/pilot commitment where the arrangement creates production, privileged-access, material support, liability or other consequential exposure not already governed by an approved envelope;
- knowingly accept a material customer dispute, concession or scope/acceptance exception that creates new Company exposure outside approved limits.

**Not reserved by this class:**

- discovery, qualification, proposal drafting and evidence preparation;
- routine customer status communication that creates no new promise;
- delivery of already committed scope;
- bounded commercial decisions later delegated under AC-203.

Customer authority remains customer authority. Owner approval cannot approve on behalf of a customer or create rights the customer has not granted.

### `ROD-04 — Major portfolio, initiative and investment decisions`

**Owner-reserved final decisions:**

- start, stop, sell, abandon or materially redirect a strategically significant Company product/initiative when the decision changes material capital, risk, obligations or strategic positioning;
- approve continuation of a major initiative despite evidence crossing an approved stop criterion or material downside limit;
- approve material reclassification where a workstream becomes a Company flagship, a strategic standalone product, a major reusable module investment or another classification that materially changes Company obligations/investment;
- approve material portfolio exceptions that override the governing investment/priority model.

**Not reserved by this class:**

- product backlog sequencing;
- implementation architecture inside product scope;
- routine release planning;
- detection and preparation of reuse/module candidates;
- stop/continue recommendations inside a delegated portfolio envelope.

A Company portfolio decision does not make the Company repository canonical for product implementation.

### `ROD-05 — Company constitutional governance, authority architecture and material delegation`

**Owner-reserved final decisions:**

- amend, ratify, supersede or retire the Company Constitution / Founding Charter;
- approve, amend or retire this Reserved Owner Decision policy;
- create or materially change the Company-wide authority/delegation model in a way that changes who may make material decisions;
- grant, broaden, revoke or materially alter a delegation that itself carries material Organizational Authority;
- approve a material organizational-model change that changes accountability or authority boundaries rather than merely assigning an executor;
- approve any mechanism that would allow another Principal, Position, AI/software system or workflow to make a decision currently classified as Reserved Owner Decision.

**Not reserved by this class:**

- preparation/publication mechanics after an approved decision;
- low-risk workflow/document changes inside an approved governance envelope;
- routine Assignment changes that do not change Position authority;
- evidence collection and cross-review.

AC-203 may define delegated authority. It **must not** silently delegate `ROD-*` final decisions.

### `ROD-06 — Risk appetite and material exception acceptance`

**Owner-reserved final decisions:**

- define or materially change Company risk appetite;
- accept a material legal, security, privacy, data, reputational, operational or continuity gap outside approved limits;
- continue/resume a material activity while a known consequential control gap remains unresolved and no existing approved degraded-mode rule authorizes continuation;
- approve a material exception to a mandatory Company control where the higher-authority legal/constitutional/contractual source actually permits an exception.

**Non-waiver rule:** Owner authority cannot legalize an unlawful act, waive a customer's rights, weaken an Arvectum OS constitutional invariant, override a binding Product Contract or create authority the Company does not possess. Where the higher-authority rule permits no exception, the decision must stop or follow that rule's amendment/approval path.

**Not reserved by this class:**

- routine risk assessment;
- evidence gathering;
- security containment, credential rotation, fail-closed action or safe shutdown under an approved incident/runbook envelope;
- routine recovery inside an approved continuity plan.

### `ROD-07 — Customer/data sovereignty and material reuse/disclosure exceptions`

**Owner-reserved final decisions:**

- approve Company-side participation in a material cross-customer reuse, disclosure or shared-learning arrangement when valid rights/purpose/legal bases have first been established through the proper source;
- approve a material expansion of customer/partner data processing beyond the currently approved purpose, classification or external-processing boundary;
- accept a material data-sovereignty or retention exception outside approved Company/customer/contract limits;
- approve a material external data-processing dependency that changes the accepted customer/data risk envelope.

**Required higher-authority basis:** Owner approval is necessary where this class applies but is never sufficient to manufacture customer consent, legal basis, contractual rights or cross-organization permission.

**Not reserved by this class:**

- least-privilege access administration inside an approved boundary;
- data minimization and deletion execution required by existing policy/contract;
- routine customer-scoped processing already authorized by applicable rights and workflow.

### `ROD-08 — Core IP, critical dependency and technology-sovereignty exceptions`

**Owner-reserved final decisions:**

- approve sale, exclusive transfer, encumbrance or other material loss of control over critical Company IP or organizational assets, subject to the required legal/corporate process;
- approve a material technology-sovereignty exception that creates hard lock-in, removes a credible replacement path or places the only usable copy of critical Company history/knowledge/data with an external provider;
- approve adoption of a critical external dependency when sanctions/export/availability, jurisdiction, telemetry/data, licensing, forkability or replacement risk materially exceeds approved limits;
- approve abandonment of a critical replacement/portability path where the resulting dependency is materially irreversible.

**Not reserved by this class:**

- routine dependency upgrades;
- ordinary tool selection inside an approved architecture/risk envelope;
- reversible experiments with declared scope and exit path;
- technical evaluation of Russian or foreign alternatives.

### `ROD-09 — Material Company↔Product↔Arvectum OS boundary and cross-repository commitments`

**Owner-reserved final decisions:**

- approve a Company-side material responsibility transfer that changes what the Company, a product or Arvectum OS is expected to own or support;
- approve a Company commitment that would create a new stable cross-repository dependency, compatibility/support promise, data/authority reliance or shared-platform obligation outside existing approved contracts;
- approve material Company adoption, de-platformization or dependency on Arvectum OS where the change materially affects continuity, obligations, customer commitments or organizational authority implementation;
- approve a Company-specific semantic change that would require an OS governance proposal because current OS contracts do not admit the required behavior.

**Scope rule:** the Owner may approve the **Company side** of such a proposal or commitment. That does not approve an Arvectum OS RFC/ADR/capability lifecycle change or a product implementation change that belongs to another canonical governance path.

**Not reserved by this class:**

- normal use of already approved Product Contracts/capabilities within their admitted scope;
- repository synchronization and references;
- product-local implementation changes that create no Company/OS cross-boundary obligation.

## 6. Decisions deliberately **not** Owner-reserved by default

After AC-203 defines safe authority envelopes, the following classes should normally move away from Owner final approval unless a specific case exceeds a material limit or enters a `ROD-*` class:

- opportunity intake normalization and discovery preparation;
- routine qualification against approved criteria;
- evidence assembly, research and option preparation;
- standard scoping/proposal preparation;
- routine customer communications that add no commitment;
- defect / scope / change-request first-pass classification;
- delivery coordination inside accepted scope;
- technical decomposition and implementation inside an accepted workstream;
- routine QA, regression, packaging and release execution inside an approved release envelope;
- reversible engineering/tool choices inside accepted architecture/risk limits;
- management-finance reporting preparation and exception surfacing;
- portfolio status synchronization and routine prioritization inside approved bounds;
- canonical-source/roadmap/review synchronization after an authorized decision;
- security access administration, revocation, rotation and incident containment under approved rules;
- tested restore/re-bootstrap/degraded-mode actions under approved continuity rules;
- AI/software execution inside an explicitly approved bounded workflow and authority envelope.

The fact that the Owner performs one of these today does not make it a Reserved Owner Decision.

## 7. Function-level mapping from AC-201

AC-202 reserves **decision gates**, not whole functions.

| AC-201 function | Reserved Owner boundary | Expected delegable core after AC-203 |
|---|---|---|
| `F-01` Company Direction / Governance / Material Control | `ROD-01`, `ROD-02`, `ROD-05`, material portions of `ROD-06`/`ROD-09` | decision preparation, evidence assembly, routine governance mechanics and non-reserved operational control |
| `F-02` Commercial Discovery / Qualification / Commitment Preparation | material/non-standard commitment gate under `ROD-03`; strategy exception under `ROD-01` | intake, discovery, qualification, proposal/scoping preparation and bounded commercial decisions |
| `F-03` Customer Delivery / Acceptance / Support | material scope/acceptance/concession exposure outside limits under `ROD-03`/`ROD-06` | delivery coordination, routine acceptance evidence, issue classification and support inside committed bounds |
| `F-04` Portfolio / Product / Workstream Stewardship | major start/stop/reclassification/overrun decisions under `ROD-04`; cross-boundary changes under `ROD-09` | status, evidence, routine priority and continue/change/stop recommendation inside approved portfolio envelope |
| `F-05` Engineering / Automation / QA / Release | no whole-function reservation; only cases entering a material `ROD-*` class | technical execution, QA, packaging, routine release and reversible engineering decisions inside bounds |
| `F-06` Management Finance / Cash / Obligation Control | `ROD-02` financial-exposure decisions; material commitment/risk exceptions | reporting, forecasts, exception surfacing and bounded spend/payment decisions under later limits |
| `F-07` Organizational State / Evidence / Improvement | constitutional/authority changes under `ROD-05`; material cross-boundary governance under `ROD-09` | state synchronization, evidence, review preparation and approved publication mechanics |
| `F-08` Security / Access / Risk / Continuity Assurance | risk appetite/material exceptions `ROD-06`, data-sovereignty `ROD-07`, critical dependency exceptions `ROD-08` | access control, monitoring, containment, recovery and ordinary risk treatment under approved policies |

This mapping directly addresses the AC-201 handoff requirement: **function responsibility ≠ decision authority ≠ execution assignment**.

## 8. Materiality without invented numeric thresholds

AC-202 needs a consequence test but current evidence does not justify Company-wide ruble, duration, data-volume, SLA or percentage thresholds.

A case should be treated as potentially material when one or more of the following is true:

- it can meaningfully alter Company strategy or a major portfolio allocation;
- it can create a non-routine legal/commercial obligation or liability;
- it can create a cash/recurring-cost/working-capital exposure large enough that decision quality depends on explicit management evidence;
- it can cause material customer harm, reputation loss or delivery/support burden;
- it can expose sensitive/customer data beyond an approved purpose or boundary;
- it can create a material security or continuity gap;
- it can lock the Company into an external dependency or impair replacement/portability;
- it can change who holds material Organizational Authority;
- it can create a stable cross-repository/platform obligation;
- it is difficult or costly to reverse relative to the Company's current scale.

AC-203 must convert these consequence dimensions into practical delegation limits where evidence supports doing so.

Until then, ambiguity about whether a case is material must produce **escalation or fail-closed behavior**, not silent expansion of delegated authority.

## 9. Reserved Owner Decision preparation packet

The Owner should decide from a prepared bounded packet rather than reconstructing raw context.

For a material `ROD-*` decision, the accountable preparer should provide proportionately:

1. **decision subject and requested act**;
2. **why Owner authority is required** — exact `ROD-*` class and any legal/corporate gate;
3. **current canonical state / facts** and material source references;
4. **options**, including `do nothing / defer / stop` where meaningful;
5. **expected value / customer / strategic consequence**;
6. **cash, recurring cost and obligation impact** where relevant;
7. **risk/downside, reversibility and time-to-recover**;
8. **data/security/sovereignty implications** where relevant;
9. **dependencies and cross-repository/OS impact** where relevant;
10. **recommended decision and uncertainty**;
11. **execution plan after approval**, including owner, bounds, rollback/compensation and evidence;
12. **expiry/review trigger** where the decision should not remain valid indefinitely.

The packet is preparation, not approval.

## 10. Approval semantics

A Reserved Owner Decision is valid internally only after an **explicit attributable Owner act**.

The following do **not** constitute approval:

- AI recommendation;
- favorable score;
- prepared draft;
- silence or absence of objection;
- technical execution;
- repository write permission;
- completion of a workflow stage;
- the Owner reading a notification;
- prior approval of a similar but materially different case.

A durable decision record should identify, proportionately:

- `ROD-*` class;
- exact subject/scope;
- approving Owner Principal/capacity;
- evidence/version relied upon where material;
- decision: approve / reject / defer / approve-with-conditions;
- constraints and excluded effects;
- effective date;
- expiry/review/supersession trigger where applicable;
- required corporate/legal act if separate;
- execution owner/path after approval.

Chat may carry the explicit Owner act, but a material durable decision must be **promoted into the canonical Company decision record** rather than left only in chat history.

## 11. Execution after Owner approval

Owner approval should be a **thin decision gate**, not an instruction for the Owner to perform all mechanics.

After a Reserved Owner Decision is explicitly approved, a later accountable Position/workflow MAY, within the exact approved scope:

- publish/synchronize governance records;
- update roadmap/portfolio state;
- create bounded implementation work;
- perform technical configuration;
- execute already authorized operational steps;
- prepare or execute a legal/corporate action through the properly authorized Principal;
- notify affected operators;
- capture evidence and verify completion.

The execution path MUST stop/escalate when:

- material facts changed after approval;
- the requested external effect exceeds the approved scope;
- required legal/corporate authority is absent;
- data/security/risk conditions differ materially;
- the implementation would create a new cross-repository or OS commitment not in the approval;
- the result is uncertain and retry could duplicate a consequential effect.

## 12. AI and software boundary

AI/software may support every `ROD-*` class by:

- gathering evidence;
- checking completeness/freshness;
- identifying relevant policy/contract constraints;
- generating options;
- estimating bounded scenarios;
- challenging assumptions through cross-review;
- preparing the decision packet;
- executing authorized post-decision mechanics;
- monitoring whether approved limits are exceeded.

AI/software MUST NOT:

- approve a `ROD-*` decision;
- infer approval from context, behavior or silence;
- create a new delegation to itself;
- broaden Organization/customer scope;
- accept material risk on behalf of the Owner;
- convert technical permission into Company authority;
- silently amend this artifact or the Company Constitution.

## 13. Emergency and incident rule

Reserved authority must not make safe emergency containment impossible.

A later approved incident/continuity workflow MAY pre-authorize bounded reversible actions such as:

- revoke/disable access;
- rotate or disable credentials through the proper secure mechanism;
- isolate a service or workload;
- stop an automated external effect;
- preserve evidence;
- switch to an approved degraded/manual mode;
- restore from an approved recovery path.

Such containment is **not** a material risk-acceptance decision merely because the Owner is unavailable.

However, the following remain Owner-reserved when material and outside an already approved envelope:

- knowingly resume operation with an unresolved consequential gap;
- accept a new material liability/data/security/continuity exposure;
- waive a material Company control where waiver is legally/governance-permitted;
- materially change risk appetite because of the incident.

Where higher-authority law/contract/security rules require a different actor or prohibit continuation, those rules prevail.

## 14. Company / Product / OS / customer boundary

### Company

AC-202 governs internal Arvectum Company Owner-reserved decision classes.

### Product

A Company portfolio decision may fund, prioritize, continue or stop a product. Product implementation/domain semantics remain governed by the product repository.

### Arvectum OS

Arvectum OS may later represent/enforce the approved Company authority model. It does not create that authority.

The current canonical Arvectum OS `main` was re-checked for AC-202 at `d26f9583393d4f3d9ef104f5408439da0471fd76`. Constitution `1.2.0` remains Ratified and RFC-0001 through RFC-0008 remain Accepted `1.0.0`. The OS Decision Authority Policy remains Proposed `0.2.1`; it is therefore design reference only, not binding Company or OS authority for this artifact. AC-202 creates no new Product Contract, capability lifecycle or production-conformance claim.

### Customer

A customer organization's reserved decisions must be derived from its own owners, legal/corporate authority, business model, risk, commitments and governance.

Arvectum's `ROD-*` catalog is **reference evidence, not a customer template**.

## 15. Transferability lesson for the flagship

The reusable method is:

```text
customer/company value + obligations + risk + authority sources
→ identify consequential decision classes
→ separate legally/corporately reserved matters
→ select the smallest internal owner-reserved set
→ delegate the remainder through Position authority envelopes
→ give AI/software execution only after authority/data/tool/fallback boundaries exist
→ measure owner attention, exceptions and operating outcomes
```

A customer may reserve more, fewer or different decisions.

The commercial objective of the flagship is not to remove the owner from control. It is to preserve high-value control while moving preparation, routine decisions and execution out of the owner's personal attention queue.

## 16. Prospective operating evidence

Phase 2 and later operating work should capture, proportionately:

- count/class of Owner interventions by `ROD-*`, delegated decision or escalation;
- whether an escalation was genuinely reserved or caused by a missing/unclear delegation;
- Owner decision preparation time/blocking where material;
- decisions delayed because evidence was incomplete;
- cases where a delegated decision unnecessarily escalated;
- cases where a decision should have escalated but did not;
- Owner approval followed by excessive manual publication/execution work;
- repeated exception classes that justify a new AC-203 rule rather than more Owner involvement;
- emergency containment performed safely without bypassing material risk acceptance;
- any Company/Product/OS/customer authority confusion.

The target is not `zero Owner decisions`. The target is **high information per Owner decision and low Owner involvement in non-reserved work**.

## 17. Handoff to AC-203

AC-203 must use this artifact as a negative boundary: define what Positions **may** decide, approve or execute without Owner involvement while never crossing a `ROD-*` final-decision class.

AC-203 should define, where evidence supports it:

- Position authority scope;
- decision/action classes;
- financial/budget limits;
- customer/external commitment limits;
- data/classification scope;
- maximum risk/consequence;
- duration/review;
- excluded decisions, including the `ROD-*` catalog;
- escalation path;
- automatic execution rules after valid approval;
- canonical delegation reference.

AC-203 must also distinguish:

```text
routine delegated decision
vs
bounded automatic execution
vs
approval-required consequential action
vs
Reserved Owner Decision
```

No Position title, system role or AI Assignment may be treated as authority merely because it exists.

## 18. Completion and approval boundary

The reviewed AC-202 proposal is substantively complete when it:

- separates legal/corporate authority from internal Owner authority;
- identifies the smallest durable Owner-reserved decision classes rather than reserving whole functions;
- identifies major non-reserved/delegable work so Owner control does not become an Owner bottleneck;
- defines explicit approval semantics;
- preserves Company/Product/OS/customer authority boundaries;
- supports bounded AI/software preparation/execution without granting AI authority;
- defines emergency containment without delegating material risk acceptance;
- gives AC-203 a clear negative boundary for future delegated Position authority;
- avoids invented numeric thresholds and customer-template claims.

This `0.9.0` publication is a **proposal only**.

Because AC-202 itself defines material Company Organizational Authority, it MUST NOT become binding merely because AI drafted it, cross-review passed, or it was committed to the repository.

Required next governance act:

> explicit Owner approval of the exact reviewed `Proposed 0.9.0` content.

After that approval, publication may promote the unchanged approved substance to `Approved 1.0.0`, register the approval record/canonical source, close AC-202 and advance the roadmap to AC-203.
