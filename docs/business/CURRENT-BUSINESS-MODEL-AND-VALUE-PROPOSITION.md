# AC-101 — Current Business Model and Value Proposition Baseline

Status: `Active`
Version: `0.1.0`
Created: `2026-08-20`
Updated: `2026-08-20`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-101 — Current business model and value proposition baseline`
Review: `docs/reviews/AC-101-CURRENT-BUSINESS-MODEL-CROSS-REVIEW.md`

## 1. Purpose and completion boundary

This document records the current Company-level business model and value-proposition baseline of ООО «Арвектум» before the Company designs departments, Positions or AI Workforce around assumptions.

It answers a bounded question:

> What business is Arvectum currently building and operating, for whom does it intend or already attempt to create value, through which evidenced offers/product lines, and by which value-capture mechanisms?

This is a **business baseline**, not a profitability, revenue, market-size, legal-compliance, product-readiness or capital-allocation decision.

`AC-101` intentionally does not determine:

- booked revenue, cash receipts or current bank balances;
- gross margin, contribution margin, tax burden or recurring cost;
- payment terms, cash gaps, guarantees, credit or working-capital needs;
- current contractual obligations or customer concentration;
- sales funnel, conversion, CAC, retention or market share;
- owner workload and operational bottlenecks;
- a final portfolio priority or stop/continue decision;
- departments, Positions, delegations or AI Assignments.

Those questions belong primarily to `AC-102` through `AC-106`, then to later organizational and portfolio-governance phases.

## 2. Authority, evidence classes and promotion rule

This baseline is subordinate to applicable legal/corporate authority, the Ratified Company Constitution, approved Company governance and the canonical Company roadmap.

Product repositories remain authoritative for product implementation and current product status. `docs/portfolio/PORTFOLIO.md` remains the Company-level portfolio map. Arvectum OS remains authoritative for its own platform contracts and lifecycle state.

Because the business model had previously been discussed partly in owner conversations rather than in a durable Company artifact, AC-101 deliberately promotes only the business statements that are consistent with current canonical evidence and the Owner's previously explicit directions.

Statements in this document use four evidence classes:

- **Canonical current fact** — directly supported by current Company/product/platform canonical sources;
- **Owner-confirmed business direction** — explicitly stated or confirmed by the Owner in prior Company/product work and promoted here because it is consistent with the current canonical baseline;
- **Working hypothesis** — plausible intended economics or positioning that still requires real business evidence;
- **Unknown / deferred** — insufficiently evidenced and assigned to a later roadmap item.

Historical chat remains non-canonical after promotion. The promoted statement in this file becomes the current Company representation within the narrow scope of this baseline; later contradictory real evidence requires explicit refresh rather than silent reinterpretation.

## 3. Current Company business-model statement

Arvectum is currently best represented as a **procurement-centered AI/software company with a mixed operator/productization model and an adjacent portfolio of productized automation products**.

The model has four distinct layers:

1. **procurement supplier/contractor economic engine** — Arvectum participates in procurement as a commercial operator and supplier/contractor, using software and AI to reduce the amount of manual tender-office work required to source, evaluate and execute opportunities;
2. **procurement software/SaaS productization engine** — successful internal procurement workflows are intended to become reusable decision-support and automated-tender-office software for suppliers/tender companies;
3. **productized client automation and standalone software** — the Company builds focused automation products/solutions outside the core procurement loop when real client work or standalone product value justifies them;
4. **internal capability compounding** — Arvectum OS and other shared initiatives may reduce future marginal delivery/governance cost and preserve organizational intelligence, but they are not treated as direct revenue products without a separate evidenced decision.

The current evidence does **not** justify describing Arvectum as a pure SaaS company, a pure consulting/freelance company, a software holding company with seven equally important businesses, or an autonomous tender-execution agent.

## 4. Layer 1 — Procurement supplier/contractor economic engine

**Evidence class:** `Owner-confirmed business direction`, with product/portfolio evidence supporting the operating concept but not yet proving current revenue.

### 4.1 Business role

The starting procurement model is a supplier/contractor model in which ООО «Арвектум» may become the commercial counterparty to the procurement customer and separately source required goods from suppliers.

The intended operating chain is:

```text
Procurement opportunity
→ documentation / requirements / risk analysis
→ supplier search and questions
→ RFQ / collection of TKP and market prices
→ normalization and comparison
→ economics / margin / cash-gap / contract-risk review
→ human GO / NO-GO decision
→ bid / contracting within actual authority
→ supplier contracting / fulfilment / delivery
→ payment collection and case evidence
```

The workflow is **RFQ-first**. The starting assumption is not an owned product catalog with pre-known prices. Supplier search and current quotations are part of the value-creation process.

### 4.2 Initial market focus

The Owner-confirmed starting direction is:

- primary market: Russia;
- procurement emphasis: `223-ФЗ` and private industrial procurement;
- initial commercial object: goods rather than a general works/services business;
- starting domain advantage: standard and complex goods, with electrical equipment as the strongest previously evidenced procurement domain.

Current Tender Agent product validation also contains a bounded `44-ФЗ` pre-bid contour. That product evidence does **not** by itself change the Company commercial focus from the Owner-confirmed `223-ФЗ + private industrial` starting direction.

### 4.3 Customer, supplier and value capture

In this economic engine:

- the procurement customer/buyer is the revenue-side contractual counterparty when Arvectum wins and executes a supply contract;
- suppliers are source-side counterparties from whom Arvectum obtains TKP/quotes and goods;
- the intended value-capture mechanism is commercial gross margin between the customer-side contract economics and the full cost of fulfilment, subject to financing, tax, logistics, risk and other real costs.

The existence, amount and quality of current revenue, margin and cash conversion are **Unknown / deferred to AC-102**. This document does not claim that the procurement engine is currently profitable or that a specific contract has been booked by ООО «Арвектум».

## 5. Layer 2 — Procurement software / SaaS productization engine

**Evidence class:** `Owner-confirmed business direction` for productization/SaaS; `Canonical current fact` for the existence of the Tender Agent/Tender Operator product line; monetization remains partly unproven.

The second engine converts validated procurement operating practice into reusable software for external suppliers and tender operators.

### 5.1 Intended external users/customers

The relevant software customer/user group is not the same as the demand-side procurement customer in Layer 1.

Target users include:

- suppliers participating in public or corporate procurement;
- tender companies / outsourced tender departments;
- operators who must repeatedly analyze procurement documentation, source suppliers, collect TKP, calculate economics and prepare a controlled bid decision.

Earlier product work explicitly used tender companies as initial design-partner/client context and did not assume that those customers were manufacturers with a ready internal catalog and fixed prices.

### 5.2 Value proposition

The procurement software is intended to turn a fragmented manual tender-office process into a controlled decision-support workflow that can:

- structure tender documentation and requirements;
- identify material restrictions and risks;
- prepare supplier questions and RFQ material;
- collect/normalize TKP for comparison;
- calculate economics through deterministic rules where appropriate;
- assemble evidence and client/operator-ready reports;
- preserve human review and final consequential decision authority.

This is decision support and governed workflow automation, not an autonomous authority to submit bids, sign contracts, spend money or create binding commitments merely because software or AI can technically perform an action.

### 5.3 Value capture

The Owner-confirmed long-term direction includes `SaaS` / productized automated-tender-office revenue after internal and design-partner cases justify it.

The exact packaging — subscription, license, usage-based, managed service or a combination — is not canonically fixed by AC-101. Current recurring SaaS revenue is therefore **not claimed** and must be tested against AC-102/AC-103 evidence.

## 6. Layer 3 — Productized client automation and standalone software

**Evidence class:** `Canonical current fact` for the mapped product/initiative nodes and their purposes; individual revenue contribution is `Unknown / deferred` unless later financial evidence proves it.

The current portfolio shows that Arvectum does more than the procurement core. It has repeatedly built bounded automation products around real workflow problems.

Current portfolio evidence includes:

- **Discount Parser** — productized client solution/product for collecting, normalizing, deduplicating and classifying discount/promo data with controlled publication;
- **Doors Parser** — mature client-delivery/reusable parsing solution for structured catalog extraction from manufacturer sites;
- **Creative Test Agent** — local-first controlled-pilot solution for pre-testing marketing creatives before client presentation;
- **Arvectum Proxy Launcher** — owned local proxy-routing utility with a productized Windows track and potential standalone commercial/internal value;
- **Tender App / Small-Volume Procurement Calculator** — procurement experiment/product adjacent to the main Tender Agent line;
- **Data Platform** — internal/shared initiative whose external business role is not yet sufficiently evidenced.

These nodes demonstrate a repeatable Company pattern:

```text
Real manual/client problem
→ bounded software solution
→ delivery and evidence
→ reusable product component or product candidate
→ continue / productize / contain / retire based on economics
```

AC-101 does **not** infer that every repository is a separate durable business, that every product is monetized, or that all productized client work is legally invoiced through ООО «Арвектум». Actual revenue attribution belongs to AC-102.

## 7. Layer 4 — Internal capability compounding

**Evidence class:** `Canonical current fact` for the existence and governance role of Arvectum OS; `Working hypothesis` for the magnitude of economic leverage until measured.

Arvectum OS is the shared domain-neutral platform and Executable Organizational Model foundation used to preserve governance, organizational meaning, records, workflows, evidence and history where an applicable governed boundary exists.

At the current Company baseline:

- Arvectum OS is **not** an ordinary portfolio product in `PORTFOLIO.md`;
- Company ownership of Arvectum OS does not let products bypass OS Product Contracts or lifecycle rules;
- current OS Product Contracts relevant to the Company remain Provisional where so recorded;
- no external Arvectum OS SaaS, SLA or production-platform revenue is inferred by AC-101.

The intended internal economic value of shared platform/capability work is lower marginal cost, less repeated implementation, stronger continuity, safer delegation and accumulated organizational intelligence. The actual return on that investment is not yet measured.

## 8. Customer / beneficiary map

| Segment | Current job/problem | Current or intended Arvectum offer | Value-capture status | Evidence class |
|---|---|---|---|---|
| procurement customers / contracting authorities / large industrial buyers | obtain required goods under procurement/contract terms | Arvectum as supplier/contractor using internal tender and sourcing automation | commercial supply margin is the intended mechanism; actual revenue/margin not yet baselined | Owner-confirmed direction |
| suppliers and tender companies | repeatedly analyze tenders, source market prices, compare TKP, assess risks/economics and prepare a bid decision | Tender Agent / automated tender-office decision support | SaaS/productized revenue direction confirmed; exact packaging and current recurring revenue not yet proven | Owner-confirmed direction + canonical product fact |
| businesses/agencies with bounded repetitive data/marketing/operational work | replace manual collection, normalization, analysis, reporting or controlled publication | productized automation such as Discount Parser, Doors Parser, Creative Test Agent | project/product revenue mechanism plausible and client-delivery products exist; current LLC revenue attribution requires AC-102 | Canonical product fact + deferred financial evidence |
| standalone software users | solve a narrow local software/infrastructure problem | products such as Arvectum Proxy Launcher | commercial packaging/revenue model not yet established at Company level | Working hypothesis |
| Arvectum Company itself | reduce repeated implementation, preserve organizational knowledge and control AI/software execution | Arvectum OS and shared internal capabilities | internal cost/risk/productivity leverage, not external revenue by default | Canonical internal capability fact + economic hypothesis |

## 9. Current value proposition

The Company-level value proposition supported by current evidence is:

> **Arvectum turns repetitive, information-heavy commercial work into controlled software and AI-assisted workflows that move from raw opportunity/data to a reviewable decision or deliverable while preserving human/company authority over consequential commitments.**

This proposition has different concrete expressions by business layer.

### 9.1 For procurement customers

Arvectum's intended value is reliable commercial fulfilment of required goods, with internal automation used to source, evaluate and execute opportunities more systematically than an ad hoc manual process.

The customer buys the supply result, not Arvectum OS or the internal agent architecture.

### 9.2 For suppliers and tender operators

Arvectum's intended value is a controlled tender-office workflow that reduces fragmentation between documentation analysis, supplier/RFQ work, TKP comparison, economics, risk review and human GO/NO-GO decision.

Time savings, error reduction, win-rate improvement or ROI must be measured before being stated as proven market outcomes.

### 9.3 For automation clients

Arvectum's value is to convert a specific repeated manual workflow into a bounded software tool with explicit inputs, outputs, QA and a path to repeatable operation rather than leaving the client with one-off manual labor.

### 9.4 For standalone-product users

The product-level value proposition must remain product-specific. AC-101 does not create a single marketing promise for Proxy Launcher, parsers, marketing tools and procurement products merely because they share a Company owner.

## 10. Current differentiators — evidence-bounded

The following are current differentiator hypotheses supported by operating/product evidence, not yet proven market superiority claims:

1. **RFQ-first procurement logic.** The system is designed for cases where there is no owned catalog or known market price and supplier discovery/TKP collection are first-class workflow steps.
2. **Human control over consequential decisions.** AI/software may analyze, draft, calculate and execute bounded pre-authorized work, while final material commitments remain with the applicable authorized Principal.
3. **Local-first / controlled processing where the product requires it.** Tender and creative-testing work has been designed around controlled/local execution rather than mandatory dependence on public cloud LLMs.
4. **Russia-first technology-sovereignty discipline.** Critical dependencies should remain replaceable, with a preference for operation that does not surrender Company authority, canonical history or the only copy of critical data to an external vendor.
5. **Productization from real work.** Client/internal workflows can become reusable products only after actual implementation evidence rather than speculative platform generalization.
6. **Organizational learning as an asset.** Validated methods, workflows and evidence can be retained through Company/OS governance instead of disappearing in chats or a single runtime.

None of these statements proves superior price, performance, compliance, security, market fit or customer preference without separate evidence.

## 11. Value-creation and value-capture map

| Business engine | Value created | Intended value capture | Current proof boundary |
|---|---|---|---|
| procurement supplier/contractor | sourcing, bid decision support, contracting and fulfilment of goods | gross commercial margin after full fulfilment costs | mechanism Owner-confirmed; current revenue/margin/cash not baselined |
| procurement software / automated tender office | reusable tender analysis, RFQ/TKP/economics/risk workflow | recurring SaaS/productized software/service revenue | direction confirmed; current recurring revenue and pricing not proven |
| productized client automation | reduction/replacement of a bounded manual workflow through software | project fee, productized delivery or later recurring support/product revenue | product/delivery evidence exists; current LLC cash attribution deferred |
| standalone owned software | focused user utility | license/subscription/other product monetization | Company-level monetization model not yet fixed |
| internal shared platform/capabilities | lower future delivery/governance duplication and higher continuity/control | cost avoidance, reduced owner effort/risk, faster future product delivery | strategic/economic hypothesis until AC-102/AC-104 and later real evidence |

## 12. What AC-101 explicitly does not claim

This baseline does **not** claim that:

- ООО «Арвектум» is already profitable;
- every current portfolio node generates revenue;
- current client-delivery revenue is already booked to the LLC rather than another historical operating context;
- SaaS recurring revenue is live;
- a specific pricing model has been approved;
- `44-ФЗ` is the primary Company commercial focus merely because a current OS Product Contract validates a bounded `44-ФЗ` workflow;
- Arvectum OS is a customer-facing commercial product or Active production platform;
- Data Platform is already a separate product;
- Tender Agent and Tender App have been merged or rationalized;
- the parsers form a universal parser product/platform;
- AI may autonomously make final bid, legal, financial or contractual commitments;
- technical product PASS proves customer value, legal compliance, security readiness or business readiness.

## 13. Material unknowns carried into M1

### AC-102 — finance / obligations

Must establish from authoritative financial/operational sources:

- actual LLC revenue and cash receipts by business engine;
- accounts receivable/payable and payment timing;
- recurring software/infrastructure/admin costs;
- taxes and mandatory payments relevant to management cash view;
- procurement working-capital requirements, guarantees, financing and cash gaps where applicable;
- outstanding contractual/financial obligations;
- actual gross/contribution economics where supportable.

### AC-103 — customer/value stream

Must establish:

- which customer segments are actually active versus target-only;
- how leads/opportunities enter;
- who decides, buys, uses and pays in each model;
- current sales/delivery lifecycle and handoffs;
- where measurable customer value is created or lost.

### AC-104 — owner workload

Must establish where the Owner currently spends time across sales, tender operations, product delivery, development, administration, approvals and exception handling.

### AC-105 — risk/continuity

Must establish material dependencies and failure modes across procurement obligations, products, local infrastructure, third-party services, data, signing, banking/accounting and key-person concentration.

## 14. Current business-model baseline conclusion

The current Company is not one monolithic software product. Its most coherent current model is a **procurement-centered mixed business** that uses owned software/AI capabilities to create commercial operating leverage, while deliberately productizing validated workflows into software and maintaining adjacent automation products where real client or standalone value exists.

The strongest currently promoted economic thesis is:

```text
Real procurement / client work
→ owned automation and operating evidence
→ better/repeatable internal execution
→ productized reusable software
→ recurring or scalable revenue where customers validate it
→ organizational knowledge/capabilities retained for the next product and workflow
```

The model remains intentionally evidence-bounded. AC-101 fixes **what business the Company is in and how value is intended to move through it**; AC-102 must now establish whether and where that model is producing real revenue, cash, costs and obligations.

## 15. AC-101 completion result

AC-101 is complete when this artifact and its cross-review are canonical and the roadmap advances to AC-102.

Completion means the Company now has a durable current answer to:

- what its principal business model is;
- which materially different value-creation/value-capture engines exist;
- which customer/beneficiary groups correspond to each engine;
- what value proposition is supported without marketing overclaim;
- which business-model statements are facts, Owner-confirmed directions, hypotheses or unknowns;
- what financial evidence AC-102 must obtain next.

It does **not** constitute approval of pricing, budget, investment, contracts, external claims, portfolio prioritization, delegation or organizational design.