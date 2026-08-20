# AC-204 — Initial Position Registry Cross-Review

Status: `Complete / PASS for Owner approval`
Review date: `2026-08-20`
Iterations completed: `9 of maximum 10`
Result: `PASS — the proposal defines five evidence-backed executor-neutral Company Positions that cover all eight AC-201 functions while preserving AC-202 Reserved Owner Decisions, AC-203 delegation semantics, legal/corporate/customer/Product/OS boundaries and current-scale minimality without turning Positions into employees, AI-agent slots or conventional departments`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-204 — Initial Position Registry`
Reviewed artifact: `docs/organization/INITIAL-POSITION-REGISTRY.md`
Reviewed publication: `Proposed 0.9.0`
Reviewed blob SHA: `623a3b407d99dad8244629307a57b41bb423e8fa`
Maximum review iterations: `10`
Approval status: `Pending explicit Owner approval of the exact reviewed proposal`
Arvectum OS main re-checked: `dff9591a9897743c48c56bbe2320260c2e0a071c`

## 1. Review purpose

This review tests whether AC-204 creates the **minimum useful Position structure** for the real current Company rather than:

- mechanically creating one Position per AC-201 function;
- turning familiar department labels into fake headcount;
- preserving the Owner as universal operator under a new title;
- confusing Owner/participant/General Director legal capacities with an internal Position;
- making AI agents, products, repositories or runtimes into Positions;
- granting authority that AC-202/AC-203 do not support;
- or over-bundling responsibilities until accountability becomes meaningless.

Review lenses:

1. Owner / Founder;
2. legal/corporate authority / General Director;
3. Company Executive / operating integration;
4. Commercial / market discovery;
5. Customer Delivery / acceptance;
6. Portfolio / Product;
7. Engineering / QA / Release;
8. Finance / obligations;
9. Organizational Operations / evidence;
10. Security / Data / Customer Sovereignty;
11. Risk / Continuity;
12. Organizational Design;
13. Product-repository boundary;
14. Arvectum OS boundary;
15. Flagship transferability / customer organization design.

These are review perspectives only and do not create extra Positions.

## 2. Iteration 1 — reject one-function-one-Position modeling

**Criticism:** AC-201 contains eight functions. The easiest AC-204 implementation would create eight Positions, but that would convert an analytical function map into headcount-shaped organization without evidence.

**Reconciliation:** the proposal applies a separate Position admission test and bundles functions only where current scale and shared accountability make the bundle more useful than extra handoffs.

The resulting initial registry contains five Positions:

1. `POS-001 — Company Executive`;
2. `POS-002 — Commercial & Customer Lead`;
3. `POS-003 — Portfolio & Product Lead`;
4. `POS-004 — Engineering & Release Lead`;
5. `POS-005 — Company Operations & Assurance Lead`.

All eight AC-201 functions are covered, but Sales, Customer Success, CFO, CISO, PMO and other familiar labels are not created merely for completeness.

**Result:** PASS after minimality test.

## 3. Iteration 2 — Owner, participant, General Director and Company Executive must not collapse into one authority source

**Criticism:** `POS-001 — Company Executive` could be read as equivalent to Owner or General Director and accidentally manufacture legal/corporate authority from an internal Position.

**Reconciliation:** the proposal explicitly records Owner, participant/general-meeting competence and General Director legal office as **non-Position authority anchors**. `POS-001` owns delegated operating integration only.

The Position title does not create:

- General Director powers;
- participant competence;
- bank/signature authority;
- `ROD-*` authority;
- or external representation rights.

A later AC-205 Assignment may place the same natural person in several capacities, but the authority sources remain distinct.

**Result:** PASS.

## 4. Iteration 3 — Commercial and Customer Delivery: split or bundle?

**Criticism:** `F-02` Commercial Discovery and `F-03` Customer Delivery have different lifecycle stages and could be represented by separate Sales and Delivery/Customer Success Positions. Combining them might blur commitment and acceptance.

**Counter-criticism:** current evidence shows that customer context itself is a major single point: discovery meaning, scope, defect-vs-change classification and acceptance live in one fragile context. Creating a handoff before there is a repeatable acquisition engine would add coordination overhead and risk.

**Reconciliation:** `POS-002 — Commercial & Customer Lead` combines `F-02` and `F-03` for the current scale but is bounded by authority rather than by title:

- it may prepare scope, qualify and coordinate accepted delivery;
- it cannot create material/non-standard commitments (`ROD-03`);
- it cannot accept customer/data/risk exceptions (`ROD-06`/`ROD-07`);
- it cannot approve on behalf of the customer.

Explicit split triggers are recorded for repeatable acquisition volume, customer concurrency, incentive conflict and support becoming a distinct capability.

**Result:** PASS.

## 5. Iteration 4 — Portfolio/Product accountability must be distinct from Engineering

**Criticism:** at current scale the same executor often decides what to build and then builds it. A minimal model could merge `F-04` and `F-05` into one Product/Engineering Position.

**Risk:** that would preserve two major AC-104 failure modes: the Owner/universal interpreter remains the shared product-priority context, and implementation sunk cost can silently become portfolio priority.

**Reconciliation:** the proposal creates separate `POS-003 — Portfolio & Product Lead` and `POS-004 — Engineering & Release Lead`.

The first owns Company-level purpose/status/priority/reuse evidence; the second owns technical production and verification. Product repositories remain canonical for detailed implementation.

Major investment/start/stop/reclassification remains `ROD-02`/`ROD-04`; technical success does not become portfolio authority.

**Result:** PASS.

## 6. Iteration 5 — bundling Finance, Organizational State and Security/Risk could create an oversized control Position

**Criticism:** `POS-005 — Company Operations & Assurance Lead` combines `F-06`, `F-07` and `F-08`. Finance, governance/evidence and security/risk are materially different disciplines; combining them can create weak independence or a future bottleneck.

**Counter-evidence:** current Company evidence does not justify separate CFO, PMO/Governance, CISO or Risk Positions. Transaction/statutory accounting is already external. The immediate durable need is preparation/visibility/exception-routing and continuity/access assurance, not three management departments.

**Reconciliation:** the bundle is admitted with four controls:

1. the Position has no initial `AM-3` material approval authority;
2. material finance/risk/data/sovereignty decisions remain `ROD-*` or other competent approval;
3. external accounting/banking truth remains external;
4. explicit split triggers require separation if independent approval, regulatory specialization, workload or assurance conflict becomes material.

Thus one Position gathers/maintains control evidence but cannot become the sole approver of its own material exception.

**Result:** PASS after independence rule.

## 7. Iteration 6 — authority model must not outrun available evidence

**Criticism:** AC-203 defines `AM-0` through `AM-4`. A Position Registry that immediately grants delegated approvals or automatic consequential execution would pre-empt AC-205 Principal eligibility, AC-206 access and concrete workflow evidence.

**Reconciliation:** all five initial Positions receive only an initial **design ceiling** of `AM-0`, `AM-1` and `AM-2` by declared action classes.

No Position receives `AM-3` or `AM-4` initially.

This does not negate AC-203. It means the Company has not yet produced evidence for:

- concrete consequential delegated approval classes;
- eligible approver Principal classes;
- automatic consequential workflows with approved limits/data/failure/rollback semantics.

`AM-3`/`AM-4` may be added later through explicit approved changes rather than inferred from Assignment or capability.

**Result:** PASS.

## 8. Iteration 7 — product, customer, external service and Arvectum OS boundaries

**Criticism:** Positions spanning products and Company controls could accidentally pull external authority into the Company organization. In particular, a Portfolio/Product Lead could become product implementation authority, an Engineering Lead could become OS governance authority, or a Company Operations Lead could become accounting/customer-data authority.

**Reconciliation:** the proposal explicitly preserves:

- product repositories as canonical for product implementation/domain truth;
- customer Principals as customer authority;
- outsourced accounting/banking systems as transaction/statutory authority;
- legal/corporate actors as legal authority;
- Arvectum OS as separate platform governance.

The registry creates no Product Contract, OS Position, customer role, accounting department or cross-repository commitment.

Current Arvectum OS `main` was re-checked at `dff9591a9897743c48c56bbe2320260c2e0a071c`; the OS Constitution remains `1.2.0` Ratified and the Decision Authority Policy remains Proposed `0.2.1`. No AC-204 design depends on treating that Proposed policy as binding.

**Result:** PASS.

## 9. Iteration 8 — Positions must not become AI-agent slots or a five-person staffing plan

**Criticism:** once five Positions are named, later AI Workforce work could mechanically create one agent per Position, or the registry could be read as requiring five employees.

**Reconciliation:** the proposal makes the executor-neutral rule explicit:

- five Positions are five durable accountability boundaries, not five people;
- one Principal may hold several Assignments initially;
- one Position may be realized by a human/AI/software hybrid;
- AI/software may execute permitted work but do not become authority sources;
- external services may provide inputs without becoming Positions;
- executor replacement does not change Position meaning.

The proposal also records conflict-of-context cautions when the same Principal holds several Positions so temporary concentration does not erase organizational boundaries.

**Result:** PASS.

## 10. Iteration 9 — end-to-end completeness, handoffs and future adaptability

**Criticism:** after aggressive minimality, the model could still fail by leaving one function ownerless, preserving a hidden universal coordinator, or becoming too rigid for future scale.

**Reconciliation:** the review traced all eight functions and the end-to-end current value/control loop.

Coverage:

- `F-01` → `POS-001`;
- `F-02` + `F-03` → `POS-002`;
- `F-04` → `POS-003`;
- `F-05` → `POS-004`;
- `F-06` + `F-07` + `F-08` → `POS-005`.

The major handoffs are explicit:

```text
customer/market need
→ POS-002 scope/customer state
→ POS-005 economics/risk/data evidence
→ POS-001 routine integration or Owner/legal gate
→ POS-003 portfolio/product context
↔ POS-004 technical production
→ POS-002 validation/acceptance state
→ POS-005 closure/evidence/assurance
→ POS-003 recommendation
→ POS-001 / Owner as authority requires
```

No Position is allowed to convert a handoff into ambient authority.

Each Position also contains evidence-based split/merge triggers, so the registry is a current operating design rather than a permanent five-box org chart.

**Result:** PASS.

## 11. Acceptance test

| Test | Result |
|---|---|
| Positions derived from real AC-201 functions/workload/control needs | PASS |
| one-function-one-Position rule rejected | PASS |
| all eight AC-201 functions have primary Position accountability | PASS |
| five Positions are the current minimum after bundling review | PASS |
| Owner is not modeled as a Position | PASS |
| participant/general meeting and General Director legal competence remain separate | PASS |
| Company Executive title creates no legal/corporate authority | PASS |
| Commercial + Customer bundle justified by current context continuity | PASS |
| no invented Sales/Marketing/Customer Success departments | PASS |
| Portfolio/Product separated from Engineering | PASS |
| product implementation remains product-repository canonical | PASS |
| Operations/Assurance bundle has explicit no-self-material-approval control | PASS |
| no internal Accounting/CFO/CISO/PMO fake headcount | PASS |
| AC-202 `ROD-*` remains hard negative boundary | PASS |
| AC-203 `AM-*` semantics preserved | PASS |
| initial modes limited to AM-0/AM-1/AM-2 | PASS |
| AM-3/AM-4 not fabricated without downstream evidence | PASS |
| no named human/AI/software Principal assigned | PASS |
| Position count not treated as employee/agent count | PASS |
| customer authority/data rights remain external/customer-scoped | PASS |
| legal/accounting/banking authority not internalized | PASS |
| Arvectum OS governance remains separate | PASS |
| no Product Contract/capability lifecycle effect created | PASS |
| split/merge/retirement triggers explicit | PASS |
| AC-205 handoff is concrete without pre-assigning executors/access | PASS |
| flagship transferability remains method-level, not a fixed customer org chart | PASS |

## 12. Why the review closes at iteration 9 of 10

The remaining material questions belong to downstream work or operating evidence:

- which current Principal(s) should hold each Position Assignment;
- where one human should temporarily carry multiple Positions;
- which work is best executed by AI, software or hybrid Assignments;
- Assignment-specific narrowing of Position authority;
- concrete data/tool/credential access;
- exact workflow-level `AM-4` automation eligibility;
- tested continuity and replacement behavior;
- whether live workload later justifies splitting Commercial/Customer, Operations/Assurance or product-specific accountability;
- actual escalation and cross-Position conflict frequency.

A tenth AC-204 desk-review iteration cannot answer those questions without pre-empting AC-205–AC-207 or fabricating operating evidence.

Stopping at iteration 9 is therefore the evidence-disciplined result.

## 13. Final conclusion

`PASS — material consensus reached at 9 of maximum 10 iterations.`

AC-204 `Proposed 0.9.0`, blob `623a3b407d99dad8244629307a57b41bb423e8fa`, is ready for explicit Owner approval.

Approval is required because the registry creates material Company accountability structure under AC-202 `ROD-05`.

After approval, the unchanged substance may be published as the binding Initial Position Registry, registered canonically, AC-204 may close as `Complete / PASS`, and the roadmap may advance to:

`AC-205 — Initial Assignments and executor classification`.
