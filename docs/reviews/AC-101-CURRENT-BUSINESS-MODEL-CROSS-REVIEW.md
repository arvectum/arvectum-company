# AC-101 — Current Business Model and Value Proposition Cross-Review

Status: `Complete`
Review date: `2026-08-20`
Iterations completed: `10 of maximum 10`
Result: `PASS — material consensus reached after Owner strategy correction`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-101 — Current business model and value proposition baseline`
Reviewed artifact: `docs/business/CURRENT-BUSINESS-MODEL-AND-VALUE-PROPOSITION.md`
Initial reviewed publication: `0.1.0`, commit `eb81a1a6967f881a303161131af88a2b2fbef3a3`
Corrected reviewed publication: `0.2.0`, commit `7b305eb33e081f7a7bd68c5f8841dd4e3ce7d1ed`
Company baseline before AC-101: `831a5dcd2eb6d1c29aa34bd9fb9513d39f82d6a3`
Arvectum OS main checked for boundary consistency: `f4028cd8d84a1cdc81ae366c59dc4fb15d6a134c`

## 1. Review purpose and reopening event

This review tests whether AC-101 captures the business Arvectum is actually building without turning historical conversations, product repositories or future ambitions into unsupported facts.

The first seven iterations reached consensus around a **procurement-centered** interpretation. Immediately after closure, the Owner rejected that strategic center and clarified the intended flagship product:

> Arvectum's primary product direction is an **«ИИ-компания под ключ»**: build a customer-specific corporate/organizational structure on Arvectum OS, following the same organization-first principles being proven in Arvectum Company, and adapt the functional/module content to the customer's business model.

That correction is material. It changes the highest-level business thesis, the role of procurement and the interpretation of the current product portfolio. Therefore the earlier strategic conclusion could not remain canonical merely because the first review had technically passed.

The review was reopened and continued through the maximum allowed `10/10` iterations.

## 2. Review lenses

The review uses eleven functional lenses:

1. Owner / Founder;
2. General Director;
3. Finance;
4. Operations;
5. Product & Portfolio;
6. Technology & Architecture;
7. Commercial;
8. Legal & Compliance;
9. Security & Data;
10. People & Organization;
11. Risk & Continuity.

The labels are review perspectives only. They do not create Positions, delegations or executive authority.

## 3. Iterations 1–7 — initial interpretation and useful retained findings

Iterations 1–7 produced several findings that remain valid after the strategy correction:

- value-capture mechanisms must not be confused with proven revenue;
- customer, user, supplier and payer roles must be separated;
- procurement is RFQ-first and must not assume a fixed catalog/known prices;
- `223-ФЗ + private industrial` Company direction and bounded `44-ФЗ` validation scope belong to different layers and must not be conflated;
- AI/software execution must not become organizational or legal authority by implication;
- public-repository safety and Company/Product/OS boundaries must remain explicit;
- AC-101 must not create departments, Positions or AI Workforce prematurely;
- actual revenue, cash, costs and obligations belong to AC-102.

However, the Iteration-1 strategic conclusion that procurement should organize the whole Company business model was invalidated by the Owner correction and is superseded.

## 4. Iteration 8 — Owner/Product reset: identify the actual flagship product

**Primary lenses:** Owner, Product & Portfolio, Commercial, Operations.

**Material criticism:**

- the previous artifact confused a mature domain/product line with the Company's highest-level commercial product;
- building Arvectum Company and Arvectum OS makes most strategic sense when they themselves form the reference architecture for a replicable customer transformation offer;
- procurement should be treated as one business domain/module, not the identity of the whole Company;
- “ИИ-компания под ключ” must not degrade into “copy our org chart” or “install many agents”.

**Reconciliation:**

- the artifact is rewritten as `0.2.0` and explicitly supersedes the procurement-centered interpretation;
- flagship direction becomes: customer-specific AI-native organizational design + Arvectum OS substrate + reusable/customer-specific modules + governed human/AI/software execution;
- Arvectum Company becomes the first reference implementation/dogfooding organization;
- procurement is repositioned as a real business domain, proof environment and possible procurement/tender module;
- the transformation sequence is defined as `business model → functions → Positions/authority → workflows/knowledge → modules → Assignments → Governed Execution`.

**Result:** PASS. The business thesis now matches the Owner's intended Company/product relationship.

## 5. Iteration 9 — Architecture/Legal/Security: what can actually be replicated?

**Primary lenses:** Technology & Architecture, Legal & Compliance, Security & Data, People & Organization.

**Material criticism:**

- the phrase “по аналогии Arvectum Company” could be misread as copying Arvectum-specific departments, owner powers, customer data, decisions or governance history;
- Arvectum OS could accidentally become a source of corporate authority over the customer's organization;
- reusable modules could silently import Company-specific semantics into the domain-neutral OS;
- a managed deployment could create dangerous vendor lock-in or cross-customer data/knowledge leakage.

**Reconciliation:**

- the customer receives an **organization-specific** model adapted to its business; Arvectum Company is reference evidence, not a literal template;
- customer Organizational Authority remains with the customer's authorized Principals/governance and is never created by OS technical permission;
- Arvectum OS remains domain-neutral and owns reusable platform semantics, not customer departments or domain rules;
- functional modules remain product/domain-owned and are admitted/reused explicitly rather than becoming Kernel/platform semantics by convenience;
- customer organizations remain separate sovereignty scopes; their data, knowledge, decisions and history do not become Arvectum Company assets by processing;
- portability/replacement remains part of the value proposition rather than making one model/runtime/vendor indispensable.

**Result:** PASS. The flagship concept is compatible with the Company ↔ OS authority boundary and technology-sovereignty principle.

## 6. Iteration 10 — Finance/Commercial/Risk convergence: is this a business model or only an architecture vision?

**Primary lenses:** Finance, Commercial, Owner, General Director, Risk & Continuity, all remaining lenses.

**Material criticism:**

- “ИИ-компания под ключ” could remain a compelling architecture thesis without a buyer, packaging or monetization path;
- a large turnkey scope can create unlimited customization/support obligations and poor unit economics;
- current products should not be automatically relabeled as modules before reuse evidence exists;
- the roadmap should not proceed as though pricing, ICP or market validation are already settled.

**Reconciliation:**

- the artifact distinguishes the confirmed flagship **product direction** from unproven packaging/economics;
- plausible capture mechanisms are separated: implementation/project fee, recurring OS/runtime/support, module revenue, custom integration and standalone product revenue, with none declared proven;
- current products are called **module candidates/reference implementations**, not automatically approved modules;
- AC-102 must determine actual financial reality and current investment burden;
- AC-103 must determine the first credible buyer/ICP, customer outcome and real discovery→deployment→support value stream;
- later Phase 3 must decide module/product identity, investment, ownership and stop/continue criteria;
- no standard customer organization, price list, implementation duration, ROI or readiness claim is invented.

**Full acceptance test:**

1. Flagship Company product direction is explicit — PASS.
2. Arvectum Company reference role is explicit — PASS.
3. Arvectum OS substrate role is separated from customer authority — PASS.
4. Product/module boundaries remain explicit — PASS.
5. Customer-specific versus reusable semantics are separated — PASS.
6. Procurement is correctly repositioned as one domain/module, not Company center — PASS.
7. Value proposition is commercially intelligible without unsupported outcome claims — PASS.
8. Monetization paths exist as hypotheses without fabricated revenue/pricing — PASS.
9. No departments/Positions/AI Workforce are prematurely created — PASS.
10. AC-102/103 receive the missing financial and customer-evidence questions — PASS.

**Stop:** iteration `10/10` — maximum reached. No remaining material contradiction blocks the corrected AC-101 baseline. Remaining uncertainty is exactly the evidence intended for AC-102/AC-103 and later product/portfolio governance.

## 7. Final perspective matrix

| Review lens | Final result | Main follow-up |
|---|---|---|
| Owner / Founder | PASS | flagship strategy corrected to AI-company builder |
| General Director | PASS | external commitments/packaging require later approved commercial boundary |
| Finance | PASS with AC-102 follow-up | pricing, actual revenue, cost-to-deploy and support economics unproven |
| Operations | PASS | turnkey delivery workflow to be made real in AC-103/later workflow work |
| Product & Portfolio | PASS with Phase 3 follow-up | determine standalone product vs reusable module vs containment/retirement |
| Technology & Architecture | PASS | OS remains domain-neutral substrate; modules/customer semantics stay above it |
| Commercial | PASS with AC-103 follow-up | ICP, buyer, measurable outcome and sales/deployment journey need evidence |
| Legal & Compliance | PASS | customer/company authority remains separate from OS technical capability |
| Security & Data | PASS | organization isolation, customer sovereignty and portability preserved |
| People & Organization | PASS | reference organizational method does not create premature Arvectum/customer Positions |
| Risk & Continuity | PASS with AC-105 follow-up | customization/support burden, lock-in and dependency risks remain to measure |

## 8. Final conclusion

`PASS — material consensus reached at 10 of maximum 10 iterations.`

The canonical AC-101 conclusion is now:

> **Arvectum is building a real AI-native Company as the reference implementation for its flagship commercial offer: designing and deploying customer-specific AI-native organizations on Arvectum OS, with explicit organizational authority/workflows and reusable functional modules adapted to the customer's business model.**

The previous procurement-centered strategic classification is superseded. Procurement remains an important business/domain/module line, not the Company's highest-level product identity.

Recommended roadmap state remains:

`AC-101 Complete / PASS → AC-102 Current`

AC-102 must now measure the financial reality of the Company and the investment burden behind this flagship direction rather than assuming the flagship is already monetized.