# AC-005 — Founding Baseline Cross-Review and Closure

Status: `Complete`
Review date: `2026-08-20`
Iterations completed: `7 of maximum 10`
Result: `PASS — material consensus reached; M0 closure recommended`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-005 — Founding baseline cross-review and closure`
Company baseline reviewed: `AC-001` through `AC-004`
Company main baseline before review: `6b1a1d0bb68c6aa68f329e85f4d9aaa2c715c269`
Arvectum OS main checked during review: `f4028cd8d84a1cdc81ae366c59dc4fb15d6a134c`

## 1. Review purpose

AC-005 reviews the complete Phase 0 founding baseline as one coherent Company system rather than re-approving AC-001 through AC-004 in isolation.

The review asks one closure question:

> Is the current founding baseline sufficiently authoritative, internally coherent, business-safe and bounded to declare `M0 — Company canonically founded` achieved and move to the real business/economic baseline?

The review does not require Phase 0 to solve later organizational, financial, portfolio-governance or runtime questions. It requires those questions to be correctly identified, assigned to later roadmap work and prevented from masquerading as already solved facts.

The executive labels used below are **functional review lenses only**. Except for legally existing capacities, they do not create Positions, appointments, departments, delegations, employment relationships or Organizational Authority.

## 2. Baseline reviewed

### 2.1 Company canonical artifacts

The review covered the currently canonical Company founding set:

- `docs/constitution/COMPANY-CONSTITUTION.md` — Ratified `1.0.0` (`AC-001`);
- `docs/governance/COMPANY-OS-AUTHORITY-BOUNDARY.md` — Approved `1.0.0` (`AC-002`);
- `docs/governance/CANONICAL-REPOSITORY-STRUCTURE.md` — Approved `1.0.0` (`AC-003`);
- `docs/portfolio/PORTFOLIO.md` — Active `0.1.0` initial portfolio map (`AC-004`);
- `docs/CANONICAL-SOURCES.md` — current authority/source registry;
- `docs/roadmap/ROADMAP.md` — canonical Company planning source;
- prior AC-001, AC-002 and AC-003 review and approval evidence.

### 2.2 Legal/corporate baseline

Private legal/corporate sources were checked only for the minimum facts relevant to founding-governance consistency. No personal identifiers, signatures, addresses, tax identifiers or banking data are reproduced here.

The checked source set supports the following safe baseline:

- the legal entity was created and recorded in the state register on `2026-06-24`;
- the Company operates under Типовой устав №23;
- there is one participant holding 100% of the charter capital at the verified baseline;
- the founding decision appoints the General Director / sole executive body for a five-year term;
- the state-registry record identifies one person entitled to act for the Company without a power of attorney and records the Company as active at issuance;
- the tax-registration source confirms registration from `2026-06-24`.

The founding-decision date was visually re-checked in the original page image as `2026-06-07`. A convenience OCR rendering that can be read as another month is therefore not used as authority.

### 2.3 Arvectum OS current canonical state

The canonical OS repository was re-checked rather than relying only on the ChatGPT Project Source snapshot.

Observed current state relevant to Company founding closure:

- Arvectum OS Constitution remains Ratified `1.2.0`;
- RFC-0001 through RFC-0008 remain Accepted `1.0.0`;
- `DECISION-AUTHORITY-POLICY.md` remains `Proposed 0.2.1` and therefore is not a binding OS authority matrix;
- CAP-001 through CAP-004 remain `Incubating / Provisional`;
- P6.02 and P6.06 Product Contracts remain `Provisional 0.1.0`;
- Phase 8 remains `Draft / Exploratory`; current work is pre-activation boundary revalidation and does not itself activate Phase 8 or change Product Contract/capability lifecycle.

The current OS movement therefore does not invalidate AC-002 or convert any Company roadmap statement into an OS commitment.

## 3. Review lenses

The cross-review used eleven functional lenses:

1. Owner / Founder — mission, residual authority, capital and anti-bureaucracy;
2. General Director — current executive management and external representation;
3. Finance — capital, cash/commitment boundary and accounting adjacency;
4. Operations — usability, workflow continuity and execution realism;
5. Product & Portfolio — product ownership, repository boundaries and portfolio sufficiency;
6. Technology & Architecture — canonical sources, OS boundary and replaceability;
7. Commercial — customer-facing commitments and market truthfulness;
8. Legal & Compliance — corporate authority, charter consistency and source supremacy;
9. Security & Data — public-repository exposure, secrets, customer/partner data and least privilege;
10. People & Organization — Position/Principal/Assignment semantics and fake-headcount risk;
11. Risk & Continuity — source conflict, platform dependency, recovery and de-platformization.

## 4. Iterative review record

### Iteration 1 — Legal/corporate facts vs internal organizational language

**Primary lenses:** Legal & Compliance, General Director, Owner.

**Material criticism:**

- the internal terms `Owner`, `Principal`, `Position` and `Organizational Authority` could be dangerous if they were treated as substitutes for participant decisions, General Director powers, powers of attorney or other legally required forms;
- a founding baseline cannot close if its legal facts disagree with the governing charter or registry evidence;
- OCR-derived text from scanned private documents must not silently override the source image.

**Checks and reconciliation:**

- AC-001 explicitly states that the Company Constitution is an internal governance artifact and not the legal charter, corporate decision or power of attorney;
- AC-001 distinguishes Owner, participant, General Director, Position and Principal even when several capacities are held by one physical person;
- AC-002 reinforces the non-substitution rule across legal/corporate, Company, OS, product and technical authority domains;
- Типовой устав №23, the founding decision and registry/tax evidence are consistent with the safe corporate baseline recorded in `docs/CANONICAL-SOURCES.md`;
- the founding-decision date was visually confirmed from the source image as `2026-06-07`, resolving a convenience-OCR ambiguity.

**Result:** no material legal/corporate contradiction remains in the founding artifacts.

### Iteration 2 — Company authority vs Arvectum OS governance and technical access

**Primary lenses:** Technology & Architecture, Owner, Security & Data, Operations.

**Material criticism:**

- because ООО «Арвектум» owns Arvectum OS and intends to use it as an organizational execution substrate, the Company could accidentally treat OS persistence, IAM, workflow execution or admin power as the source of Company authority;
- conversely, Company roadmap or Owner priorities could be misread as authority to change OS contracts;
- recent OS roadmap movement could make the Project Source pack look stale.

**Checks and reconciliation:**

- AC-002 clearly separates Company Organizational Authority, OS governance authority and technical Authorization;
- `Native`, `External Reference` and `Governed Replica` authority modes are explicitly prevented from being misread as corporate power;
- direct Company use of OS is not granted a fictional bypass around RFC-0004/Product Contract/client boundaries;
- cross-repository change requires the applicable governance path in each repository;
- the current OS canonical Constitution/RFC/Decision Authority Policy/Product Contract lifecycle state was re-checked at the current OS main baseline and remains compatible with AC-002;
- current Phase 8 work remains pre-activation and does not create an undeclared Company commitment.

**Result:** Company↔OS authority boundary remains valid; no founding amendment is required.

### Iteration 3 — Canonical repository vs external systems of record and public exposure

**Primary lenses:** Security & Data, Finance, Legal & Compliance, Commercial, Technology & Architecture.

**Material criticism:**

- the Company repository is public and cannot safely become a universal store for legal originals, banking, customer, supplier, personnel, runtime or sensitive financial data;
- a founding baseline is incomplete if “canonical” simply means “put everything in Git”;
- future Company management views must not become competing truth beside accounting, product or external systems.

**Checks and reconciliation:**

- AC-003 defines the repository as canonical only for durable, repository-suitable Company artifacts;
- legal/corporate originals, accounting, banking, contracts, personnel data, secrets, customer/supplier material and high-frequency runtime state may remain in their appropriate authoritative systems;
- public-repository exclusion rules are explicit and include Git-history remediation/credential rotation where relevant after accidental exposure;
- `docs/CANONICAL-SOURCES.md` is a registry/locator and does not override higher authority;
- future dashboards/registers are defined as models/projections unless separately promoted to a canonical runtime.

**Result:** no source-of-truth or public-data contradiction blocks M0.

### Iteration 4 — Portfolio sufficiency vs premature portfolio governance

**Primary lenses:** Product & Portfolio, Finance, Owner, Commercial.

**Material criticism:**

- AC-004 contains unresolved product identity, roadmap-freshness, overlap, accountability and investment questions;
- M0 exit criteria prohibit unresolved **material founding conflict**, so these gaps must be classified correctly rather than waved away;
- a portfolio map can create hidden capital or lifecycle commitments if descriptive repository facts are mistaken for Company approval.

**Checks and reconciliation:**

- AC-004 explicitly states that it is an initial map and does not rank priority, allocate capital, create Positions, grant authority, approve readiness or merge/retire products;
- seven material nodes and the shared Arvectum OS dependency are represented with canonical product/status locators rather than copied product roadmaps;
- the P6.02 Tender Agent repository-locator mismatch is disclosed instead of silently repaired; it must be reconciled before later governed reliance depends on that locator;
- Tender Agent/Tender App overlap, parser reuse, Creative Test Agent naming, Doors Parser lifecycle and Data Platform definition are assigned to later portfolio/product work;
- missing accountable Positions and investment/stop-continue criteria are explicitly reserved for M2/M3 after M1 business evidence exists.

**Finding:** these are real portfolio governance gaps, but they are **not founding contradictions**. They do not undermine the authority hierarchy, canonical-source model or the fact that an initial portfolio map exists. Treating them as already solved would be a failure; deferring them is the correct Phase 0 behavior.

**Result:** AC-004 is sufficient for M0 and correctly bounded.

### Iteration 5 — Organization model principles vs absence of a real operating model

**Primary lenses:** People & Organization, Operations, Owner, Finance.

**Material criticism:**

- AC-001 defines Position, Principal, Assignment and Runtime, but the Company does not yet have a Position Registry, delegated authority matrix or full operating model;
- there is a risk of declaring the Company “founded” and then treating constitutional concepts as if actual departments/Positions already exist;
- equally, forcing an org chart into M0 would violate business-first sequencing and create fake headcount.

**Checks and reconciliation:**

- AC-001 defines semantic principles without inventing concrete Positions;
- AC-003 gives later organization/authority artifacts canonical homes but deliberately does not materialize empty structure;
- AC-004 records sponsorship/accountability only at the justified pre-Position level;
- `AC-201` through `AC-208` remain the explicit M2 path for functions, Reserved Owner Decisions, delegation, Position Registry, Assignments, access and fallback;
- the roadmap intentionally requires M1 business reality before deriving M2 organization.

**Result:** absence of a detailed operating model is an intentional M0 boundary, not a founding failure.

### Iteration 6 — Business-first sequencing, economics and owner bottleneck risk

**Primary lenses:** Owner, Finance, Operations, Risk & Continuity.

**Material criticism:**

- extensive governance work can become self-referential if it proceeds into organizational design before the real business, revenue/cost/obligations and owner workload are captured;
- the founding baseline must provide enough control to move forward without claiming profitability or operational maturity that has not been evidenced;
- M0 should close only if the next step shifts from governance architecture to business reality.

**Checks and reconciliation:**

- AC-001 and the roadmap both state that architecture/governance serve business and that technical/documentary PASS does not prove profitability, compliance or customer readiness;
- the current roadmap sequence moves immediately from M0 to `AC-101–AC-106` business/economic evidence before M2 organizational design;
- the portfolio does not allocate capital or claim readiness;
- Product and OS work may continue in parallel under their own authorities, so Company founding does not become an artificial blocker for real client/product obligations.

**Result:** the correct anti-bureaucracy action is to close M0 and advance to `AC-101`, not to add more founding artifacts.

### Iteration 7 — Full-management convergence and M0 exit-criteria test

**Primary lenses:** all eleven lenses.

The panel re-tested the complete founding baseline against the roadmap M0 exit criteria:

1. **Company Constitution approved and canonical** — PASS.
2. **Corporate/legal authority not confused with OS governance** — PASS.
3. **Company ↔ OS ↔ Product ownership boundaries explicit** — PASS.
4. **Repository structure identifies canonical homes for durable Company assets** — PASS.
5. **Initial portfolio map exists without copying product roadmaps** — PASS.
6. **No unresolved material founding conflict remains** — PASS.

The remaining open items are either:

- later business/economic evidence (`AC-101–AC-106`);
- later organizational authority/Position work (`AC-201–AC-208`);
- later portfolio identity/investment/dependency reconciliation (`AC-301–AC-306`);
- later management controls and live operational sources (`AC-401–AC-407`);
- later governed Company workflow/OS reliance (`AC-501+`);
- product-side corrections in the relevant product repositories.

No open item requires changing the current Company Constitution, AC-002 boundary or AC-003 source-of-truth model before business-baseline work can begin.

**Stop:** iteration `7/10`. Additional iterations would primarily re-litigate intentionally deferred M1–M3 work or produce wording refinements rather than remove a founding contradiction.

## 5. Final perspective matrix

| Review lens | Final result | Closure condition preserved |
|---|---|---|
| Owner | PASS | founding governance is sufficient; next work returns to business reality rather than more ceremony |
| General Director | PASS | internal governance does not substitute for legally required executive/corporate acts |
| Finance | PASS with M1 follow-up | capital/cash economics are not invented in M0 and move next to AC-102 |
| Operations | PASS | durable boundaries exist without pretending operational workflows are already modeled |
| Product & Portfolio | PASS with Phase 3 follow-up | initial map is sufficient; identity/investment/dependency decisions remain explicit later work |
| Technology & Architecture | PASS | Company/Product/OS ownership and canonical-source rules are coherent with current OS state |
| Commercial | PASS | no founding artifact creates unsupported customer, readiness, SLA or product-lifecycle claims |
| Legal & Compliance | PASS | legal/corporate sources remain controlling and source facts are consistent at the checked baseline |
| Security & Data | PASS | public-repository boundary, secret/data exclusions and OS least-privilege rules remain explicit |
| People & Organization | PASS with M2 follow-up | no fake Positions/delegations are created before real business evidence |
| Risk & Continuity | PASS | OS and external dependencies remain replaceable/bounded; later continuity work is explicitly scheduled |

## 6. Material issues and their disposition

No material founding issue remains unresolved.

The review records the following non-blocking items so they cannot disappear into chat history:

1. **Tender Agent Product Contract repository identity** — reconcile P6.02 predecessor repository locator before later consequential reliance uses it as current product identity. Primary future home: `AC-301/AC-304`, and again `AC-503` if the first Company workflow depends on that contract.
2. **Tender product-family overlap** — remain separate until product/portfolio evidence supports merge, containment or retirement. Primary future home: `AC-301`.
3. **Parser reuse hypothesis** — no universal parser/platform capability is inferred from Doors Parser and Discount Parser. Promotion requires validated reuse and the applicable Product/OS governance path.
4. **Product status-pointer freshness** — correct in product repositories; Company portfolio refreshes only when Company-level state changes materially.
5. **No accountable Positions yet** — intentional; derive functions/Positions after M1 under `AC-201–AC-205`.
6. **No investment/stop-continue criteria yet** — intentional; establish after business/economic evidence under `AC-303/AC-305`.
7. **OS Decision Authority Policy remains Proposed** — no Company governance is allowed to treat it as binding; current OS residual authority remains with the OS owner until approved governance changes it.
8. **Project Source pack is a snapshot** — current canonical OS state must continue to be checked before material reliance; snapshot staleness alone does not transfer authority.

## 7. Closure conclusion

Cross-review result:

`PASS — MATERIAL CONSENSUS REACHED AT ITERATION 7/10`

Recommended milestone decision:

`M0 — COMPANY CANONICALLY FOUNDED: COMPLETE / PASS`

The founding baseline is sufficient because it establishes the minimum durable answers to:

- what Arvectum Company is and is not;
- where Company authority comes from and where it does not;
- how Company, Product and Arvectum OS responsibilities are separated;
- which repository/source owns which class of durable meaning;
- what the initial material portfolio contains;
- which questions are intentionally not yet solved.

Closure does **not** mean that the Company has a completed operating model, delegated authority matrix, financial baseline, profitable portfolio, production-ready AI workforce or comprehensive compliance state.

It means Phase 0 has done enough to stop designing the foundation and start measuring the actual business.

## 8. Required closure actions

To close AC-005 and M0:

1. preserve this review in `docs/reviews/`;
2. record the M0 closure/planning-transition decision without creating new substantive governance authority;
3. synchronize `docs/CANONICAL-SOURCES.md` with the AC-005 review/closure evidence and exact tax-source title;
4. update `docs/roadmap/ROADMAP.md` so AC-005 is `Complete / PASS`, M0 is explicitly achieved, and `AC-101 — Current business model and value proposition baseline` becomes `Current`;
5. update repository navigation if useful;
6. perform read-after-write verification.

No amendment of AC-001, AC-002, AC-003 or AC-004 is required by this review.