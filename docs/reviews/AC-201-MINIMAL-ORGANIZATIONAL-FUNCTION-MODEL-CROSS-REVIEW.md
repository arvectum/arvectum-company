# AC-201 — Minimal Organizational / Function Model Cross-Review

Status: `Complete / PASS`
Review date: `2026-08-20`
Iterations completed: `9 of maximum 10`
Result: `PASS — the eight-function model is the smallest evidence-backed Company-level responsibility set that covers current value creation, commitments, portfolio/technical production, management economics, organizational state and continuity/control without inventing departments, Positions, delegations or AI headcount`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-201 — Minimal real organizational/function model`
Reviewed artifact: `docs/organization/MINIMAL-REAL-ORGANIZATIONAL-FUNCTION-MODEL.md`
Reviewed publication: `0.1.0`
Maximum review iterations authorized by Owner: `10`
Company baseline checked: Ratified Company Constitution, AC-101 through AC-108, AC-106 priority decision, portfolio and Company↔OS boundary
Arvectum OS main re-checked: `d26f9583393d4f3d9ef104f5408439da0471fd76`

## 1. Review purpose

This review tests whether AC-201 has derived a **minimal real function model** rather than a generic enterprise org chart, a copy of current Owner activities, a list of software agents or a prematurely productized customer blueprint.

The review must prevent six failure modes:

1. creating one department for every familiar corporate label;
2. turning current Owner concentration into permanent organizational design;
3. treating AI agents, repositories or runtimes as Positions/functions;
4. pulling product/customer/external/OS authority into the Company model merely because Company work depends on it;
5. splitting responsibilities so finely that the current small Company gains governance overhead rather than clarity;
6. using AC-201 to pre-decide AC-202 through AC-208.

## 2. Review lenses

The review uses fifteen functional perspectives:

1. Owner / Founder;
2. General Director / corporate authority;
3. Strategy;
4. Commercial / Market Discovery;
5. Customer Delivery / Acceptance;
6. Product / Portfolio;
7. Engineering / QA / Release;
8. Operations;
9. Finance / Obligation Management;
10. Organizational Design;
11. Governance / Evidence;
12. Security / Data / Customer Sovereignty;
13. Risk / Continuity;
14. Arvectum OS / Product Contract boundary;
15. Flagship Transferability / Customer Design.

These are review lenses only. They create no Positions, committees, departments or delegated authority.

## 3. Iteration 1 — derive functions from evidence, not from a standard org chart

**Primary lenses:** Organizational Design, Strategy, Owner, Operations.

**Criticism:** the M1 evidence can easily be mapped onto conventional labels such as CEO, Sales, Delivery, Product, Engineering, Finance, Legal, HR, Marketing, Security and PMO. Doing so would create fake organizational completeness before workload and accountability justify it.

**Reconciliation:** AC-201 uses a five-part minimality test: real value/obligation/control/workload; consequence if unowned; distinguishable accountable outcome; correct authority/repository boundary; and executor independence.

The resulting model is limited to eight durable Company-level responsibility domains rather than a complete corporate department inventory.

Marketing, Sales department, Customer Success, PMO, internal Legal, internal Accounting, HR, “AI Workforce department”, procurement-as-company-core and OS operations are explicitly rejected as separate functions at the current evidence level.

**Result:** PASS after minimality tightening.

## 4. Iteration 2 — corporate/legal authority must not be manufactured by the function model

**Primary lenses:** General Director, Owner, Governance, Risk.

**Criticism:** `F-01 — Company Direction, Corporate Governance & Material Control` could be misread as a newly created internal authority source or as a substitute for the participant/General Director/legal authority actually required for external and corporate acts.

**Reconciliation:** AC-201 treats F-01 as an **authority interface and durable responsibility domain**, not an authority grant. The artifact explicitly preserves distinctions among Owner, participant, General Director, Position, Principal and technical operator and states that applicable law/corporate acts/charter/authorized legal actors remain authoritative in their scope.

AC-202 is the next task specifically because AC-201 does not decide which decisions are Reserved Owner Decisions.

**Result:** PASS.

## 5. Iteration 3 — commercial discovery must not imply a mature Sales organization

**Primary lenses:** Commercial, Market Discovery, Owner, Evidence.

**Criticism:** AC-108 authorizes real market discovery, and current client work begins with opportunity/scoping. Calling this a Company function could drift into an invented sales funnel, CRM, sales headcount or mass-outbound operating model that current evidence does not support.

**Reconciliation:** `F-02` is bounded to commercial discovery, qualification and commitment preparation. Its minimum output is an evidence-backed scoped opportunity/discovery package, not a closed sale.

The artifact explicitly says:

- no binding authority arises from preparation;
- no repeatable acquisition engine is yet proven;
- no dedicated Sales/Marketing department is justified yet;
- AC-108 remains bounded high-information discovery, not mass outbound.

**Result:** PASS.

## 6. Iteration 4 — customer obligation ownership and product ownership must stay separate

**Primary lenses:** Customer Delivery, Product/Portfolio, Operations, Commercial.

**Criticism:** current bespoke delivery blurs customer context, product evolution, defect correction, acceptance and productization. A single broad “Product/Delivery” function would preserve the Owner's universal-interpreter bottleneck and make it unclear whether the Company is satisfying a customer obligation or investing in a reusable product.

**Reconciliation:** AC-201 separates:

- `F-03 — Customer Delivery, Acceptance & Support`, which owns engagement state and value realization from committed scope through closure; and
- `F-04 — Portfolio, Product & Workstream Stewardship / Reuse`, which owns why a product/workstream exists, its priority/status/boundary and its continue/change/stop/reuse question.

Product implementation truth remains in product repositories. A customer correction does not automatically become product investment, and a product idea does not automatically become customer scope.

**Result:** PASS.

## 7. Iteration 5 — technical strength and AI execution must not become authority or organization design

**Primary lenses:** Engineering, Organizational Design, Owner, Arvectum OS.

**Criticism:** engineering is currently the strongest and most automatable capability. Because AI/software already execute significant technical work, there is a risk of designing the Company around agents/repositories rather than durable responsibility.

**Reconciliation:** `F-05 — Engineering, Automation, QA & Release` exists because technical production is a real durable function, but:

- detailed implementation remains product-owned;
- no centralized codebase/engineering department follows by implication;
- AI/software are executor classes only;
- technical PASS creates no customer/commercial/capital/approval authority;
- current Owner bottlenecks are explicitly identified as sequencing/context/exception/release gates rather than lack of raw coding capacity.

The model remains compatible with later human, AI, software or hybrid Assignments.

**Result:** PASS.

## 8. Iteration 6 — management finance must not recreate accounting

**Primary lenses:** Finance, General Director, Operations, Owner.

**Criticism:** a conventional function model might add a Finance/Accounting department even though AC-102 explicitly corrected the Company boundary away from transaction-level bookkeeping.

**Reconciliation:** `F-06 — Management Finance, Cash & Obligation Control` owns decision-relevant economic visibility only. Outsourced accounting, banking systems, tax/statutory records and transaction truth remain external authoritative sources.

The artifact rejects a duplicated accounting function and makes AC-404 responsible for the later management-reporting interface.

**Result:** PASS.

## 9. Iteration 7 — security and continuity must be cross-cutting control, not a ceremonial department

**Primary lenses:** Security/Data, Risk/Continuity, Operations, Customer Sovereignty.

**Criticism:** AC-105 found real credential, local-device, repository, data, vendor and Owner/corporate continuity risks. A naïve response would create a broad Security/Risk department before the Company has enough scale or detailed access evidence.

**Reconciliation:** `F-08 — Security, Access, Risk & Continuity Assurance` is admitted because the control need is real, but AC-201 limits it to required outcomes and boundaries:

- access/data/risk/continuity requirements;
- fail-closed/escalation behavior;
- bounded replacement/degraded/recovery expectations;
- no secrets in the public repository;
- no invented RTO/RPO/SLA;
- no bypass of lawful authority/security/customer gates.

Detailed access and tested continuity remain AC-206/AC-207.

**Result:** PASS.

## 10. Iteration 8 — organizational state/evidence must create value, not governance theater

**Primary lenses:** Governance/Evidence, Owner, Operations, Arvectum OS.

**Criticism:** `F-07 — Organizational State, Evidence & Improvement` could become self-referential repository bureaucracy: the Company might create governance work merely because it has a governance repository.

**Reconciliation:** F-07 is justified by specific AC-104 evidence: state reconstruction, decision-preparation/publication coupling and cross-repository synchronization already consume scarce Owner attention.

The function is narrowly defined around reconstructable current state, canonical-source synchronization, decision/workflow/evidence references and governed improvement proposals. It explicitly excludes every runtime log/transient AI output and does not require Arvectum OS to become the Company's universal canonical runtime.

The value test is practical: reduce lost context and repeated reconstruction; do not maximize artifacts.

**Result:** PASS.

## 11. Iteration 9 — test minimal completeness, boundary integrity and flagship transferability

**Primary lenses:** Strategy, Organizational Design, Customer Design, Product/Portfolio, OS Boundary, Evidence.

**Criticism:** after avoiding over-modeling, the opposite risk is under-modeling: a missing function could leave customer value, commitments, economics, technical production, organizational state or continuity unowned. In addition, the resulting eight-function set could be mistaken for the standard customer blueprint sold by the flagship product.

**Reconciliation:** the review traced the complete current value/control loop:

```text
external need
→ F-02 qualification/scoping
→ F-01 authority when material
   + F-06 economic/obligation evidence
   + F-08 risk/data/access constraints
→ F-03 delivery/value realization
↔ F-04 product/workstream stewardship
↔ F-05 technical production
→ customer validation/acceptance/support
→ F-06 obligation/economic closure
→ F-07 organizational state/improvement evidence
```

The trace covers the current M1 value streams and material control needs without assigning executors.

External authority/service boundaries are also explicit: legal/corporate, accounting/banking, customer, suppliers/contractors, product repositories, Arvectum OS and technology vendors remain separate.

Finally, AC-201 states that the reusable flagship asset is the **derivation method**, not this particular eight-function result. A customer must be re-derived from its own business model, value streams, obligations, authority and bottlenecks.

**Result:** PASS.

## 12. Acceptance test

| Test | Result |
|---|---|
| functions derived from M1 evidence rather than generic corporate labels | PASS |
| minimality/admission test explicit | PASS |
| current Owner concentration treated as evidence, not permanent design | PASS |
| Company function distinct from Position, authority, Assignment and runtime | PASS |
| no Position or department created by AC-201 | PASS |
| no AI agent/runtime treated as function or authority source | PASS |
| commercial discovery covered without inventing repeatable Sales organization | PASS |
| customer delivery/acceptance separated from portfolio/product investment | PASS |
| engineering/QA/release covered while product implementation remains product-owned | PASS |
| management-finance need covered without duplicating accounting | PASS |
| organizational state/evidence function tied to a real Owner bottleneck | PASS |
| security/access/risk/continuity covered proportionately | PASS |
| legal/corporate authority remains external/higher authority where applicable | PASS |
| customer authority/data remain customer-scoped | PASS |
| Arvectum OS remains domain-neutral and no new OS reliance is created | PASS |
| current Provisional/Incubating OS maturity is not overstated | PASS |
| procurement remains a domain/business line, not the Company identity | PASS |
| external supplier/accounting/bank/tool dependencies are not converted into Company authority | PASS |
| eight functions cover the current end-to-end value/control loop | PASS |
| AC-202 through AC-208 remain genuinely open downstream work | PASS |
| function model is reference evidence, not a fixed customer template | PASS |

## 13. Why the review closes at iteration 9 of 10

The Owner authorized a **maximum** of ten cross-review iterations.

After iteration 9, the remaining material questions are deliberately outside AC-201 scope and require the next Phase 2 artifacts or real operating evidence:

- which exact decisions remain Reserved Owner Decisions;
- which bounded decisions may be delegated and under what limits;
- how many Positions the eight functions actually justify;
- whether one Position should span several functions or one function needs several Positions;
- which human/AI/software Assignments are economical and safe;
- the exact data/tool/credential access boundary;
- tested continuity/replacement behavior;
- which internal patterns prove transferable to customers after actual use;
- whether future workload creates a real Sales, Marketing, Support, HR, Legal or other standalone function.

A tenth AC-201 desk-review iteration cannot answer those questions without pre-empting AC-202–AC-208 or fabricating operational evidence.

Stopping at iteration 9 is therefore the evidence-disciplined result.

## 14. Final conclusion

`PASS — material consensus reached at 9 of maximum 10 iterations.`

AC-201 establishes eight Company-level function domains:

1. `F-01` Company Direction, Corporate Governance & Material Control;
2. `F-02` Commercial Discovery, Qualification & Commitment Preparation;
3. `F-03` Customer Delivery, Acceptance & Support;
4. `F-04` Portfolio, Product & Workstream Stewardship / Reuse;
5. `F-05` Engineering, Automation, QA & Release;
6. `F-06` Management Finance, Cash & Obligation Control;
7. `F-07` Organizational State, Evidence & Improvement;
8. `F-08` Security, Access, Risk & Continuity Assurance.

Recommended roadmap transition:

`AC-201 Complete / PASS → AC-202 Current`.
