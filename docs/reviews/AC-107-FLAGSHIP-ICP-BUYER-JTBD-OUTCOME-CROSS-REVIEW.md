# AC-107 — Flagship ICP, Buyer, JTBD and Outcome Hypotheses Cross-Review

Status: `Complete / PASS`
Review date: `2026-08-20`
Iterations completed: `9 of maximum 10`
Result: `PASS — the first flagship market hypothesis is narrowed to a behavior-based owner-led B2B ICP, the likely buyer and JTBD are explicit, the first deployment is bounded to one measurable function, and value is defined through paired operating/economic outcomes without inventing demand, pricing, ROI, maturity or customer authority`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-107 — Flagship ICP, buyer, job-to-be-done and measurable outcome hypotheses`
Reviewed artifact: `docs/business/FLAGSHIP-ICP-BUYER-JTBD-OUTCOME-HYPOTHESES.md`
Reviewed publication: `0.1.0`
Maximum review iterations authorized by Owner: `10`
Company baseline checked: AC-101 through AC-105, current Company roadmap and approved flagship decision
Arvectum OS main re-checked: `d26f9583393d4f3d9ef104f5408439da0471fd76`

## 1. Review purpose

This review tests whether AC-107 narrows the first market hypothesis enough for design-partner discovery while preserving the evidence boundary established by M1.

The review must prevent two opposite errors:

1. remaining so broad that “SMEs that want AI” provides no useful discovery target; and
2. inventing market validation, ROI, headcount ranges, pricing, deployment duration, production readiness or customer authority that current evidence does not support.

The result must also avoid regressing to the superseded procurement-centered Company strategy merely because procurement currently has strong domain/product evidence.

## 2. Review lenses

The review uses thirteen functional perspectives:

1. Owner / Founder;
2. CEO / General Director / economic buyer;
3. Operations;
4. Commercial / Customer Discovery;
5. Customer Success / Adoption;
6. Finance / Unit Economics;
7. Product / Portfolio;
8. Organizational Design;
9. Technology / Architecture;
10. Arvectum OS / Product Contract Boundary;
11. Security / Data / Customer Sovereignty;
12. Risk / Continuity;
13. Evidence / Experiment Design.

These are review lenses only. They create no Positions, customer authority, committee or delegation.

## 3. Iteration 1 — “SME” is not an ICP

**Primary lenses:** Commercial, Owner, Operations, Evidence.

**Criticism:** A segment such as “SMEs that want AI” is too broad to drive discovery. Employee count or industry labels alone do not explain why the customer needs Arvectum's organization-first model.

**Reconciliation:** The artifact defines the primary ICP behaviorally:

- owner-led B2B business;
- recurring case/workflow operation;
- senior-management interpretation/coordination/exception bottleneck;
- fragmented digital context/tools and possibly ad-hoc AI;
- at least one measurable bounded function;
- willingness to preserve explicit authority while delegating bounded execution.

Industry becomes a secondary sourcing clue rather than the core segmentation variable.

**Result:** PASS after correction.

## 4. Iteration 2 — The buyer must be able to change the organization, not just buy software

**Primary lenses:** CEO/General Director, Commercial, Organizational Design.

**Criticism:** The flagship offer changes responsibility, workflow, approval boundaries, information flow and executor assignments. Treating IT or an innovation manager as the universal buyer would confuse technical sponsorship with Organizational Authority and budget/operating responsibility.

**Reconciliation:** The primary buyer hypothesis is Owner / Founder / CEO / General Director or equivalent top executive who both experiences the bottleneck and can sponsor a bounded operating-model change.

The artifact separately identifies an operational champion and possible IT/security/legal/finance veto or assurance roles. No universal customer RACI is invented.

A larger business-unit leader remains an adjacent secondary case when that Principal actually holds the required budget and operating authority.

**Result:** PASS.

## 5. Iteration 3 — The JTBD must be business progress, not “install AI”

**Primary lenses:** Customer Discovery, Product, Owner, Operations.

**Criticism:** “Deploy an AI-native company” is Arvectum language, not necessarily the customer's job. Customers may care about management overload, slow case handling, rework, fragmented context and inability to scale rather than about organizational-model terminology.

**Reconciliation:** The JTBD is rewritten around customer progress:

> turn one material recurring function from person-dependent coordination into an explicit operating model that produces accepted outcomes with less scarce management attention, faster and more consistently, while keeping authority/control with the proper people.

AI, Arvectum OS and modules are execution/substrate choices beneath that job rather than the job itself.

**Result:** PASS.

## 6. Iteration 4 — “ИИ-компания под ключ” is too large for the first proof

**Primary lenses:** Operations, Finance, Risk, Product.

**Criticism:** Attempting a whole-company transformation in the first design-partner engagement would make value, failure cause and unit economics impossible to isolate. It would also create unbounded customization/support obligations before any repeatability evidence exists.

**Reconciliation:** AC-107 introduces the smallest credible wedge:

- one recurring information/coordination-heavy function or value-stream slice;
- observable input and accepted output;
- explicit authority and data/tool boundary;
- enough real cases to observe the pattern;
- bounded fallback/manual contour;
- baseline measurement before broad automation.

The flagship remains company-level in long-term direction, but the first proof is function-level and reversible.

**Result:** PASS.

## 7. Iteration 5 — A single “hours saved” metric can reward bad automation

**Primary lenses:** Operations, Customer Success, Risk, Evidence.

**Criticism:** Reducing owner time alone could simply shift effort to staff, hidden rework, support incidents or quality loss. Throughput alone could reward unsafe external effects or ignored exceptions.

**Reconciliation:** The north-star hypothesis becomes **scarce owner/senior-manager attention per accepted unit of work**, paired with cycle time, throughput, quality, rework, exception, reconstructability, continuity and adoption/friction evidence.

Mandatory guardrails prevent a PASS when performance improves by weakening approval, authority, source truth, customer isolation, quality or replaceability.

No arbitrary percentage target is set before a real baseline exists.

**Result:** PASS.

## 8. Iteration 6 — Customer value is not Arvectum profitability

**Primary lenses:** Finance, Commercial, Owner.

**Criticism:** Even a real customer outcome can produce a bad business if Arvectum requires excessive discovery, customization, integration, support or Owner attention. Conversely, an implementation can be cheap to deliver but not valuable enough for the customer to pay.

**Reconciliation:** The artifact separates a customer operating-value equation from later commercial evidence. It explicitly subtracts implementation, runtime/support and change/adoption burden and requires future discovery to test both sides:

- customer value pool;
- Arvectum cost-to-deploy/support and ability to capture value.

Pricing, margin and ROI remain unknown rather than inferred from technical capability.

**Result:** PASS.

## 9. Iteration 7 — Procurement evidence must not re-center Company strategy

**Primary lenses:** Product/Portfolio, Owner, Commercial.

**Criticism:** Tender Agent/Tender Operator is currently one of the strongest domain examples and could tempt AC-107 to define the flagship buyer as “tender companies” by default. That would recreate the strategic error corrected in AC-101.

**Reconciliation:** Procurement/tender-oriented B2B suppliers are listed only as one strong first **subsegment/wedge candidate** alongside digital-service/automation businesses and data-heavy operations.

The primary ICP remains the operating pattern: owner-led B2B business with a measurable senior-management coordination bottleneck.

The artifact states explicitly that naming a tender-analysis/RFQ example does not make procurement the flagship identity or automatically promote a module.

**Result:** PASS.

## 10. Iteration 8 — Governance, sovereignty and OS maturity cannot be sold by implication

**Primary lenses:** Security/Data, Arvectum OS, Architecture, Risk, General Director.

**Criticism:** The flagship positioning could accidentally imply that Arvectum or an AI executor receives customer authority, that customer information becomes reusable Company knowledge, or that current Arvectum OS maturity supports production/SLA claims.

**Canonical re-check:** Arvectum OS `main` was re-checked during AC-107 at `d26f9583393d4f3d9ef104f5408439da0471fd76`. The Company-relevant baseline remains the one already recorded by AC-105: no Stable Product Contract, Active customer-facing capability or production/SLA claim is inferred by this Company artifact.

**Reconciliation:** AC-107 includes mandatory guardrails:

- customer Organizational Authority remains with authorized customer Principals;
- bounded AI/software execution does not create independent authority;
- no hidden cross-customer reuse;
- external authority and uncertainty remain explicit;
- safe authority/security controls are not removed to improve metrics;
- organizational meaning/history must not depend irreversibly on one runtime/vendor.

The artifact treats OS/module packaging as an unknown for later commercial/product-contract work rather than an already sold platform guarantee.

**Result:** PASS.

## 11. Iteration 9 — Hypotheses must be falsifiable and handed cleanly to AC-108

**Primary lenses:** Evidence/Experiment Design, Commercial, Owner, all remaining lenses.

**Criticism:** A polished ICP/JTBD statement can become self-confirming unless the Company records what evidence would reject it. AC-107 also risks drifting into AC-108 by inventing an interview sample, outreach plan or external commitment.

**Reconciliation:** The final artifact records nine explicit hypotheses (`ICP-H1` through `SOV-H1`) with supporting and rejecting evidence.

It also defines:

- fit and anti-ICP signals;
- a commercial evidence ladder from problem → workflow → outcome → adoption → economics → willingness to pay → repeatability;
- explicit unknowns;
- AC-108 handoff requirements for criteria, discovery questions, evidence fields, candidate prioritization and continue/change/stop logic.

No exact interview count, price, outreach commitment, pilot promise or production term is created by AC-107.

**Result:** PASS.

## 12. Acceptance test

| Test | Result |
|---|---|
| identifies one primary flagship ICP pattern rather than “all SMEs” | PASS |
| preserves Russia-first sequencing without making market-size/legal claims | PASS |
| identifies likely economic/authority buyer | PASS |
| separates buyer, champion, users and veto/assurance roles | PASS |
| states a concrete customer JTBD rather than an AI-installation description | PASS |
| defines a bounded first function/value-stream wedge | PASS |
| does not require whole-company transformation for first proof | PASS |
| defines senior-management attention per accepted outcome as a primary measurable hypothesis | PASS |
| pairs time/throughput metrics with quality/rework/adoption/control evidence | PASS |
| defines mandatory authority/security/data/source/replaceability guardrails | PASS |
| separates customer value from Arvectum implementation/support economics | PASS |
| does not invent pricing, ROI, headcount ranges, implementation duration or SLA | PASS |
| keeps procurement as one subsegment/module wedge rather than Company identity | PASS |
| does not automatically classify existing products as reusable modules | PASS |
| preserves customer Organizational Authority and customer sovereignty | PASS |
| does not infer Stable/Active/production Arvectum OS maturity | PASS |
| contains fit and anti-ICP signals | PASS |
| contains falsifiable hypotheses and reject evidence | PASS |
| leaves discovery sample/outreach/external commitment to AC-108 | PASS |
| creates a clear roadmap handoff to AC-108 | PASS |

## 13. Why the review closes at iteration 9 of 10

The Owner authorized a **maximum** of ten review iterations, not a requirement to consume all ten.

After iteration 9, the remaining uncertainties are intentionally empirical market questions:

- which subsegment responds most strongly;
- whether the hypothesized Owner/CEO buyer actually purchases;
- customer language for the problem;
- willingness to engage and pay;
- achievable magnitude of outcome improvement;
- integration/change/support burden;
- module contribution to deployment economics;
- preferred OS/runtime packaging;
- repeatability across later customers.

These are not defects that another desk review can resolve. They are the purpose of AC-108 and later real design-partner evidence.

A tenth iteration would therefore either repeat already passed conceptual lenses or manufacture “market evidence” without a market interaction.

## 14. Final conclusion

`PASS — material consensus reached at 9 of maximum 10 iterations.`

AC-107 is complete as a hypothesis baseline.

The canonical first-market position is now deliberately narrow enough to test:

> **Start with an owner-led B2B company where one recurring business function materially depends on owner/senior-manager interpretation and exception handling; sell the progress of producing accepted outcomes with less scarce management attention and preserved control; prove it first on one bounded function before attempting a whole-company transformation.**

This is not yet a validated ICP or customer promise.

Recommended roadmap transition:

`AC-107 Complete / PASS → AC-108 Current`.