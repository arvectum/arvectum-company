# AC-103 — Current Customer/Client Lifecycle and Real Value-Stream Map

Status: `Complete / PASS`
Version: `0.1.0`
Created: `2026-08-20`
Updated: `2026-08-20`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-103 — Current customer/client lifecycle and real value-stream map`
Review: `docs/reviews/AC-103-CUSTOMER-LIFECYCLE-CROSS-REVIEW.md`

## 1. Purpose

This baseline maps how Arvectum currently creates value for real clients/customers and where the current lifecycle is strong, weak, manual or not yet evidenced.

The purpose is not to invent a future sales department. It is to expose the real Company-level value streams that should shape later organizational design, Owner-workload analysis, risk/continuity work and flagship market validation.

Product repositories remain authoritative for product-specific delivery mechanics. Contract, banking, accounting and customer-confidential facts remain in their own authoritative systems. This public Company artifact records only the minimum Company-level operating meaning needed for planning.

## 2. Evidence classes

Statements use four evidence classes:

- **Repository-evidenced current fact** — directly supported by current product/Company repositories;
- **Promoted operating-context fact** — recurring real operating practice established in project history and promoted here at Company level;
- **Working hypothesis** — plausible interpretation requiring later market/operational evidence;
- **Unknown / deferred** — not sufficiently evidenced and assigned to a later roadmap item.

The most important evidence boundary is that current delivered client work must not be confused with the future flagship `«ИИ-компания под ключ»` lifecycle.

## 3. Current customer/client reality

Arvectum currently has three materially different customer-facing contours.

### 3.1 Bespoke client automation / productized client solution

**Evidence class:** `Repository-evidenced current fact` + `Promoted operating-context fact`.

This is the clearest real end-to-end client lifecycle today.

Examples include Discount Parser and Doors Parser. Product repositories show customer-specific requirements, iterative implementation, packaging/delivery artifacts, QA outputs and customer-facing installation/operation paths.

The practical lifecycle is:

```text
client problem / request
→ clarify required outcome and source/data boundary
→ agree scope / delivery expectation
→ build or adapt solution
→ test against real/synthetic cases
→ deliver build/data/artifacts
→ client verifies real use
→ defects / mismatches / change requests
→ targeted correction and re-delivery
→ acceptance / usable state
→ bounded support or later enhancement
```

This contour creates value by replacing repetitive manual work with a usable client-specific system or structured deliverable.

### 3.2 Controlled pilot / product proof with a prospective customer or design partner

**Evidence class:** `Repository-evidenced current fact` for prepared pilot mechanics; actual recurring commercial conversion is `not yet evidenced`.

Creative Test Agent contains explicit demo, onboarding, pilot-profile, success-criteria, commercial-outline and client-pilot packaging. Tender Agent / Tender Operator contains a bounded human-reviewed pre-bid operating contour and OS Product Contract evidence.

The evidenced pilot pattern is:

```text
candidate customer/problem
→ demo / discovery / onboarding questions
→ bounded pilot scope and success criteria
→ customer-specific inputs/configuration
→ supervised execution
→ human review / customer-facing result
→ evaluate usefulness, quality, friction and safety
→ continue / change / stop decision
```

This is stronger than an unstructured demo, but it is not yet evidence of a repeatable Company-wide sales/onboarding/customer-success engine.

### 3.3 Standalone product / utility path

**Evidence class:** `Working hypothesis with product evidence`.

Proxy Launcher and some other portfolio nodes can plausibly create value as standalone software without a large bespoke implementation.

The product repositories provide delivery/productization evidence, but AC-103 does not yet have sufficient Company-level evidence for a repeatable external lifecycle such as acquisition → purchase → onboarding → renewal/support.

Therefore this path remains a distinct value-stream candidate rather than an established current customer lifecycle.

## 4. The real common lifecycle across current client work

Despite product differences, current operating evidence converges on one Company-level lifecycle:

| Stage | Current operating meaning | Main value created | Current maturity |
|---|---|---|---|
| 1. Opportunity / request | a client problem, order, product interest or pilot candidate appears | converts external need into potential work | real but largely opportunistic/manual |
| 2. Discovery / scoping | clarify desired result, inputs, sources, constraints and acceptance expectations | prevents building the wrong thing | real, mostly Owner-led and not standardized Company-wide |
| 3. Commitment | decide whether to take the work and what will be delivered | converts opportunity into an obligation and expected revenue/value | real, but Company-wide qualification/commitment gates are not yet formalized |
| 4. Build / configure | implement, adapt, parse, analyze, package or configure the solution | primary technical value creation | strongest current capability; product-specific |
| 5. Internal verification | tests, QA, smoke checks, review, packaging and evidence | reduces defects before client exposure | comparatively mature in several repositories |
| 6. Customer validation | customer checks output on real machine/data/use case | establishes whether technical output solves the real job | real and essential; often produces new corrective information |
| 7. Correction / iteration | fix mismatch, source behavior, UX, packaging or interpretation | turns initial delivery into usable accepted value | highly visible current operating pattern |
| 8. Acceptance / handover | client receives working build/data/artifact and operating instructions where relevant | realizes client value and closes the delivery loop | evidenced, but acceptance semantics vary by project |
| 9. Support / continuation | resolve defects, update source-specific behavior, ship new build or continue pilot | preserves delivered value | present but mostly reactive and product-specific |
| 10. Learning / reuse | retain generalizable engineering, workflow and module evidence without leaking customer data/authority | lowers future delivery cost and improves products | strategically important but not yet a standardized Company lifecycle |

## 5. Current real value streams

### VS-1 — Bespoke automation delivery

```text
external client problem
→ scoped technical/business requirement
→ implementation/adaptation
→ verified deliverable
→ client acceptance/use
→ payment/value realization
```

Typical value: less manual work, faster data processing, fewer repetitive actions, a usable local application or structured output.

Current evidence: strongest in parser/client-delivery work.

### VS-2 — Iterative correction to accepted outcome

```text
client uses real result
→ discovers mismatch/edge case
→ sends evidence/feedback
→ Arvectum diagnoses
→ targeted correction
→ re-test/re-deliver
→ client confirms
```

This is not merely “support overhead”. In current bespoke work it is part of value creation because real websites, environments and user expectations reveal facts unavailable in the initial specification.

The weakness is that the loop is Owner-coordinated and can become unbounded unless scope, acceptance and change boundaries improve.

### VS-3 — Controlled pilot / decision-support proof

```text
candidate customer
→ bounded problem and success criteria
→ configure product/context
→ supervised run
→ reviewed output
→ customer/usefulness evidence
→ continue/change/stop
```

Typical value: prove usefulness before a broader deployment or commitment.

Current evidence: prepared strongly in Creative Test Agent and bounded Tender Agent operating contours; repeatable conversion to paid recurring engagements remains unknown.

### VS-4 — Productization from client work

```text
one-off/client-specific solution
→ repeated patterns observed
→ separate customer-specific from reusable logic
→ harden packaging/QA/update path
→ reusable product/module candidate
→ lower future delivery effort
```

Current evidence: Discount Parser moved materially toward installer/web-UI/cross-platform delivery; Doors Parser supplies mature extraction/QA evidence; other portfolio nodes show similar productization attempts.

This stream creates Company value only when reuse actually lowers future cost/risk or creates revenue. Repository existence alone is not proof of reusable-module economics.

### VS-5 — Flagship AI-company transformation

**Status:** `future flagship value stream, not current lifecycle evidence`.

The intended future stream is:

```text
customer business discovery
→ value streams / obligations / bottlenecks
→ functions / Positions / authority
→ workflows / data / controls
→ module selection + customer-specific gaps
→ bounded deployment
→ supervised operation and measurable outcome
→ acceptance / transfer / support
→ governed improvement
```

AC-103 records this only to identify the gap between current delivery capability and the future offer. AC-107/AC-108 must still establish ICP, buyer, job-to-be-done, measurable outcome and first design-partner plan.

## 6. What currently works well

1. **Rapid conversion of concrete requirements into working software/data outputs.** The Company repeatedly produces operational artifacts rather than only concepts.
2. **Strong implementation feedback loop.** Real user remarks lead to targeted corrections and new evidence.
3. **QA/productization discipline is emerging.** Several repositories contain regression tests, smoke checks, packaging, delivery guides or acceptance evidence.
4. **Local/controlled deployment is a recurring strength.** Customer delivery can avoid unnecessary cloud dependence and can preserve customer control.
5. **Human review remains available at consequential boundaries.** Product evidence does not require broad autonomous external action.
6. **Reusable patterns are already visible.** Parsing, controlled pilots, local packaging, project histories, reports and governed evidence provide candidate building blocks.

## 7. Current structural weaknesses

### 7.1 Acquisition is not yet a repeatable Company engine

Current evidence supports real client work but not a canonical funnel with lead source, qualification, conversion, cost of acquisition and predictable pipeline.

AC-103 therefore does not invent sales Positions or funnel KPIs.

### 7.2 Scoping and acceptance are too Owner-dependent

Discovery, interpretation of ambiguous requests, trade-offs and acceptance corrections frequently require direct Owner involvement.

This is a likely scale bottleneck and is carried directly into AC-104.

### 7.3 Technical delivery is more mature than commercial lifecycle management

Repositories often contain detailed implementation/QA/delivery mechanics while Company-level evidence for qualification, proposal discipline, formal acceptance, support tiers, renewal/expansion and customer-health management is sparse.

### 7.4 Iteration can become open-ended

The correction loop creates value, but without explicit change/acceptance boundaries it can absorb disproportionate Owner/engineering time and destroy project economics.

### 7.5 Post-delivery value realization is weakly measured

Current evidence often proves “works / delivered / accepted” better than it proves hours saved, revenue created, error reduction, decision quality, adoption rate or willingness to pay more.

This is critical for the flagship direction: technical PASS cannot substitute for measurable customer outcome.

### 7.6 Reuse is not yet a governed commercial loop

Technical patterns are reused informally or through product evolution, but there is not yet one Company process that decides:

- what remains customer-specific;
- what becomes product capability;
- what becomes a reusable module candidate;
- what, if anything, belongs in Arvectum OS;
- what rights permit reuse;
- whether reuse actually improves unit economics.

Phase 3 remains responsible for this governance.

## 8. Customer authority, data and external-effect boundary

Current and future customer work must preserve these boundaries:

1. customer instructions, data and business authority remain customer-scoped;
2. technical access or AI capability does not create authority to bind the customer;
3. customer-specific data/knowledge/history do not become reusable Company or cross-customer knowledge automatically;
4. externally consequential actions require the applicable human/organizational authority and approved workflow;
5. product-specific integrations remain governed in the product repository and, where Arvectum OS is relied upon, through the applicable Product Contract;
6. public Company planning must not contain raw customer-confidential payloads.

## 9. Lifecycle control points that the later operating model must own

The later organization should create accountability for these control points rather than copy product teams mechanically:

| Control point | Required organizational question |
|---|---|
| opportunity qualification | is this work strategically/economically worth accepting? |
| scope | what exact outcome is promised and excluded? |
| commitment | who may create price/scope/time/support obligations? |
| customer input readiness | are required data, access, examples and acceptance criteria available? |
| delivery readiness | is the result technically and operationally safe to expose? |
| customer acceptance | what evidence makes the obligation complete? |
| change request | defect, agreed scope, or new paid/unpaid scope? |
| support | what continuity/support obligation actually exists? |
| learning/reuse | what can lawfully and economically be retained/generalized? |
| closure | are delivery, acceptance, payment/receivable, data handling and follow-up resolved? |

AC-103 does not assign these control points to invented Positions. AC-201–AC-205 will derive accountable structure from this and the remaining M1 evidence.

## 10. Minimum lifecycle state model for later Company design

A sufficiently general state model for current work is:

```text
Opportunity
→ Qualified / Declined
→ Scoped
→ Committed
→ In Delivery
→ Internal Review
→ Customer Validation
→ Accepted
→ Support / Follow-up
→ Closed
```

Additional explicit states should exist where needed:

- `Blocked — customer input`;
- `Change requested`;
- `Rework`;
- `Payment / receivable pending` where contractually relevant;
- `Stopped`;
- `Cancelled`.

This is a Company-level lifecycle vocabulary, not a software schema decision.

## 11. Evidence that should be captured prospectively

Without recreating CRM/accounting prematurely, future real engagements should make it possible to answer:

- source/type of opportunity;
- customer job/problem;
- accepted scope and exclusions;
- promised outcome and acceptance evidence;
- start/end or cycle time at a useful level;
- material Owner interventions;
- major rework/change causes;
- support obligation and incidents;
- customer-confirmed outcome/usefulness;
- revenue/margin class through the management-finance interface where needed;
- reusable learning candidate and rights boundary;
- close/continue/expand decision.

Exact tools and registers belong later, especially AC-401/AC-404. The important result here is the information need, not a CRM implementation.

## 12. Direct implications for AC-104

AC-104 should measure where the Owner currently performs or must approve work across this lifecycle, especially:

- lead/opportunity judgment;
- discovery and ambiguous requirement interpretation;
- scope and commitment decisions;
- technical decomposition and prioritization;
- customer communication and expectation management;
- review of exceptions and rework;
- acceptance/closure judgment;
- productization/reuse decisions.

The largest likely bottleneck is not raw coding alone; it is the concentration of commercial interpretation, prioritization, exception handling and customer-context continuity in one Principal. AC-104 must test that hypothesis rather than assume it.

## 13. AC-103 completion boundary

AC-103 is complete when the Company can distinguish:

- current real client-delivery lifecycle from future flagship lifecycle;
- the major real value streams currently evidenced;
- value-creating iteration from uncontrolled rework;
- technical delivery maturity from commercial/customer-success maturity;
- customer-specific work from reusable learning;
- the lifecycle control points that later Positions/authority must own;
- the information needed to measure customer value without building premature systems.

This publication satisfies that boundary without inventing market demand, a future sales organization, pricing, support SLAs or flagship repeatability.

Next roadmap action: `AC-104 — Owner workload, manual work and bottleneck map`.