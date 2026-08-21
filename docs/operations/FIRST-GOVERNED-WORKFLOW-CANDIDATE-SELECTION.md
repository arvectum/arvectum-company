# AC-501 — First Governed Workflow Candidate Selection

Статус: `Proposed`
Версия: `0.9.0`
Создано: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-501 — First governed workflow candidate selection`
Milestone: `M5 — First real governed Company operating contour proven`
Статус утверждения: `Pending explicit Owner approval of the exact reviewed proposal`
Cross-review: `docs/reviews/AC-501-FIRST-GOVERNED-WORKFLOW-CANDIDATE-SELECTION-CROSS-REVIEW.md`

## 1. Назначение

AC-501 выбирает **один первый реальный Company workflow** для последующего AC-502…AC-507.

Задача не состоит в выборе самого технически зрелого продукта, самого «AI-похожего» контура или workflow, который проще всего связать с Arvectum OS. Выбор должен максимизировать реальную бизнес-ценность и качество организационного evidence при минимально достаточном риске и стоимости управления.

Результат AC-501 — exact selection decision для одного bounded workflow candidate. AC-501 сам по себе не создаёт customer commitment, budget/spend authority, Product Contract, production approval, новый Assignment, новый credential/access grant или Arvectum OS lifecycle change.

## 2. Governing evidence baseline

Выбор опирается на текущий canonical Company state:

- `docs/constitution/COMPANY-CONSTITUTION.md` — Ratified `1.0.0`;
- `docs/roadmap/ROADMAP.md` — Active `0.36.0`, AC-501 current;
- `docs/business/M1-BUSINESS-BASELINE-REVIEW-AND-PRIORITY.md` — AC-106, `Complete / PASS`;
- `docs/business/CURRENT-CUSTOMER-LIFECYCLE-AND-VALUE-STREAM.md` — AC-103;
- `docs/business/OWNER-WORKLOAD-MANUAL-WORK-BOTTLENECK-MAP.md` — AC-104;
- `docs/organization/INITIAL-POSITION-REGISTRY-v1.0.0.md` — AC-204;
- `docs/organization/INITIAL-ASSIGNMENTS-AND-EXECUTOR-CLASSIFICATION-v1.0.0.md` — AC-205;
- `docs/security/COMPANY-DATA-TOOL-CREDENTIAL-ACCESS-BOUNDARY-v1.0.0.md` — AC-206;
- `docs/operations/CRITICAL-FUNCTION-CONTINUITY-REPLACEMENT-FALLBACK-BASELINE-v1.0.0.md` — AC-207;
- `docs/portfolio/PORTFOLIO.md` — Active `0.8.0`;
- `docs/operations/COMPANY-WORK-OBLIGATION-REGISTER-MODEL-v1.0.0.md` — AC-401;
- AC-402…AC-407 approved M4 control baseline and Owner Mission Control reference evidence.

Product-specific implementation truth remains product-owned. For the leading candidate current product evidence was re-checked in `arvectum/discount-parser` at `main` commit `a8c1b29702a8ce40bd30b5d972ac2541367900e1`.

Material recent product evidence includes a repeated customer-feedback sequence rather than one isolated defect:

- PR `#65` — customer feedback #4 → upgrade/source/manual-publishing correction;
- PR `#66` — feedback #5 → Sources hardening + offer images;
- PR `#67` — feedback #6 → canonical activation of Sources hotfix;
- PR `#68` — feedback #7 → runtime routing correction;
- PR `#69` — feedback #8 → SQLite datetime regression correction;
- PR `#70` — feedback #9 → upgrade/shortcut and source-mapping clarification;
- PR `#71` — feedback #10 → zero-technical source setup UX;
- PR `#73` — feedback #11 → one-time per-site mapping + internal-detail crawl model.

PR `#71` explicitly reduced normal customer participation to providing a URL, reviewing an automatically produced preview and confirming the result. PR `#73` further converted customer evidence into a reusable site-profile model while preserving specialist-only complexity behind the normal user path.

This sequence is evidence of a recurring operational loop, but it is **not** proof that the customer has finally accepted the current build, that all obligations are satisfied, or that the workflow is economically optimal.

## 3. Selection criteria

AC-501 applies the exact roadmap criteria:

1. real customer/revenue/obligation value or evidence acquisition;
2. current workload and Owner reconstruction/coordination burden;
3. repeatability;
4. bounded authority feasibility;
5. data/tool/access readiness;
6. risk and reversibility;
7. evidence quality and reconstructability;
8. continuity/fallback feasibility;
9. likely economic/operational value relative to implementation/control cost.

Ratings below are qualitative decision aids (`High / Medium / Low / Unknown`), not measured ROI, probability or money values.

## 4. Compared real candidates

### CAND-1 — Customer feedback → classified correction → verified candidate → customer validation/acceptance

**First real instance:** `PORT-002 — Discount Parser`.

Company-level meaning:

```text
customer feedback / observed mismatch
→ normalize evidence
→ classify: defect / incomplete input / environment / agreed-scope correction / new scope / product limitation
→ establish allowed next action
→ bounded technical correction where admitted
→ regression/build/verification evidence
→ candidate result for customer validation
→ customer confirms / rework / new-scope escalation / closure
```

Evidence basis:

- AC-103 identifies iterative correction to accepted outcome (`VS-2`) as a real current value stream;
- AC-104 identifies customer-context continuity, exception classification and rework as High Owner bottlenecks;
- PORT-002 is current Company portfolio `A1` and its decisive near-term evidence is real client acceptance/live-environment feedback;
- current product history contains repeated customer-feedback→correction→release cycles and substantial automated QA/build evidence.

Key unknowns:

- exact customer acceptance state and remaining obligation scope must remain source-backed outside the public Company repo;
- no measured cycle-time, Owner-time or margin baseline yet;
- customer communication and ambiguous scope/acceptance judgments remain human/authority-sensitive.

### CAND-2 — Flagship candidate qualification / discovery evidence loop

**Source:** AC-108 bounded discovery plan.

```text
candidate
→ qualification
→ evidence/research preparation
→ discovery conversation
→ evidence normalization
→ hypothesis update
→ continue/change/stop recommendation
```

Strengths:

- directly serves P1 flagship market evidence;
- repeatable and strategically important;
- bounded discovery semantics already exist.

Current gaps:

- dedicated commercial sender/CRM and seller handoff are not yet fully implemented/tested under AC-206/AC-207;
- external outreach/conversation is an external-effect/customer boundary;
- completed 8–12 high-information conversations and repeatable acquisition are not yet evidenced;
- first M5 contour would therefore partly test setup of the evidence engine rather than an already-recurring live operating obligation.

### CAND-3 — Tender Agent supervised pre-bid decision-support run

**First instance:** `PORT-001 — Arvectum Tender Agent`.

Strengths:

- bounded product workflow is well specified;
- human review and external-effect limits are strong;
- current Arvectum OS Product Contract evidence exists for bounded scopes;
- potentially high revenue/evidence value.

Current gaps:

- Company portfolio explicitly carries forward that real paid/pilot/deal economics and repeatability remain unproven;
- choosing it now risks selecting for technical/OS readiness, which AC-501 explicitly forbids;
- a suitable live case and current customer/commercial boundary must exist independently before M5 can claim real operation.

### CAND-4 — Management finance / obligation decision-packet preparation

**Source:** AC-404 + POS-005.

```text
material decision need
→ current source-backed cash/obligation evidence
→ management packet
→ constraint/unknown assessment
→ decision-ready Owner gate
```

Strengths:

- high consequence when a material commitment exists;
- directly reduces Owner reconstruction burden;
- clear fail-closed semantics.

Current gaps:

- public M4 snapshot explicitly states current bank/accounting/receivable/payable completeness is unknown in that projection;
- detailed finance data is sensitive and current AI access is intentionally narrow;
- first M5 implementation would require more restricted source integration/access work before recurring operational evidence could be collected safely.

### CAND-5 — Company governance proposal → review → Owner approval → publication

**Source:** AC-401…AC-407 observed workflow.

Strengths:

- already repeatedly executed and reconstructable;
- authority separation and bounded publication mechanics are strongly evidenced;
- low technical uncertainty.

Why it is not selected:

- M4 already proved this workflow class sufficiently for governance/reference observability;
- selecting it again would optimize for governance convenience, not extend the model into a real customer/business operating contour;
- business linkage and economic outcome remain indirect.

## 5. Comparative decision matrix

| Criterion | CAND-1 feedback→acceptance | CAND-2 flagship discovery | CAND-3 tender pre-bid | CAND-4 finance packet | CAND-5 governance publication |
|---|---|---|---|---|---|
| real customer/revenue/obligation/evidence value | **High** | High | Medium–High | High when triggered | Low–Medium |
| current Owner burden relevance | **High** | High | Medium | High | Medium, already improved |
| repeatability evidenced now | **High** | Medium | Medium–Low | Medium | High |
| bounded authority feasibility | **High** | Medium–High | High | Medium | High |
| data/tool/access readiness | **High** for technical slice; customer boundary human | Medium | High product-side | Low–Medium | High |
| risk / reversibility | **High** | High | Medium–High | Medium | High |
| reconstructable evidence | **High** | Medium–High | High | Medium until live sources | High |
| fallback feasibility | **High** manual/human correction path | Medium | High manual external actions | Medium | High |
| value relative to new control cost | **High** | Medium–High | Medium | Medium–Low initially | Low incremental value |

No candidate is rejected permanently. The matrix answers only which one should be **first** for M5.

## 6. Exact selection decision proposed

AC-501 proposes selection of:

> **`WF-M5-001 — Customer Feedback → Classified Correction → Verified Candidate → Customer Validation / Acceptance`**

with the first supervised real-operation instance on:

> **`PORT-002 — Discount Parser`**.

Selection rationale:

1. It is tied to an **existing real client/value/acceptance contour**, not a speculative future workflow.
2. It is already **recurring** in product evidence rather than merely designed.
3. It attacks three of the strongest Owner bottlenecks identified by AC-104: customer-context continuity, exception classification and rework routing.
4. The technical execution portion is unusually ready for bounded AI-led execution under existing POS-004/AC-205/AC-206 constraints.
5. Final customer validation and ambiguous scope/commitment decisions can remain human-gated, so the first contour does not require unsafe autonomy.
6. Manual fallback is straightforward: the current Owner-led correction loop already exists.
7. The workflow generates useful M5 evidence even if the result is negative: Owner intervention count, classification ambiguity, rework, cycle time, acceptance friction, technical failure, fallback use and control cost can all be observed.
8. It advances current portfolio `A1` work instead of creating a parallel demonstration project.
9. It does not require Arvectum OS merely to justify M5; OS reliance can be admitted in AC-503 only if an actual semantic dependency exists.

## 7. Selected workflow boundary

The selected workflow is **not** “all Discount Parser development” and not “all customer support”.

### In scope for M5 design

- one real customer feedback item or a small coherent feedback batch;
- source evidence needed to understand the reported mismatch;
- first-pass structured classification;
- explicit distinction between existing-scope correction and potential new scope;
- preparation of a bounded engineering task when action is admitted;
- AI/software-assisted code/test/build execution within product rules;
- verification evidence and candidate-release preparation;
- human review at the required customer/commitment/acceptance boundary;
- customer validation result represented as `confirmed / still failing / changed requirement / insufficient evidence / stopped` rather than inferred success;
- traceable rework, escalation or closure.

### Explicitly out of scope unless separately approved

- new price, discount, SLA, support promise or contract interpretation;
- automatic acceptance on behalf of the customer;
- automatic external customer messages or delivery merely because a build passes tests;
- new material customer obligation;
- unrestricted access to customer systems, credentials or private data;
- general redesign of Discount Parser outside the admitted feedback scope;
- cross-product shared parser/platform creation;
- PORT-007/Data Platform promotion;
- Arvectum OS Product Contract/lifecycle change;
- product roadmap reprioritization beyond the selected existing A1 acceptance contour;
- payment/refund/financial commitment;
- legal interpretation of customer rights or contract scope by AI.

If the feedback reveals new scope, material customer commitment, unclear rights, sensitive access, material security risk or product/Company/OS boundary change, the M5 workflow must escalate/fail closed rather than stretch its definition.

## 8. Position and authority hypothesis for AC-502

AC-501 does not finally assign workflow authority; AC-502 owns that work.

The leading accountability hypothesis is:

- **primary end-to-end accountable Position:** `POS-002 — Commercial & Customer Lead`, because the workflow begins with customer evidence and ends in customer validation/acceptance state;
- **bounded technical executor/accountability:** `POS-004 — Engineering & Release Lead` for admitted correction, test, build and release-candidate evidence;
- `POS-003 — Portfolio & Product Lead` consulted/escalated only when product scope, priority, reuse/productization or Company↔Product boundary materially changes;
- `POS-006` participates when security/data/continuity exceptions arise;
- Owner retains applicable `ROD-*`, material commitment, risk, ambiguous acceptance and other reserved decisions.

AC-502 must test this hypothesis and may change the primary accountable Position if the detailed workflow/authority analysis shows that another approved Position is semantically correct. AC-501 does not create a new Position.

## 9. Data/tool/access readiness finding

For the selected contour:

- product repository/build/test execution is already a credible technical substrate for `POS-004` bounded work;
- reusable secrets and customer-restricted payload remain outside ordinary AI/model context under AC-206;
- no bank/signing/general-mailbox privilege is needed for the core correction workflow;
- final customer communication/validation may remain through the current human channel for M5;
- a dedicated CRM or automatic sender is therefore **not a prerequisite** for the first slice.

This asymmetry is desirable: M5 can test governed work before broadening credentials or external-effect automation.

## 10. Continuity and fallback finding

The selected workflow has a credible initial fallback:

```text
AI/software preparation or engineering unavailable/uncertain
→ stop autonomous progression
→ preserve evidence/current state
→ human/Owner continues the existing manual feedback→correction loop
```

This is `defined` fallback, not yet Company-wide `CE-3` continuity proof.

AC-506 must later test at least one realistic failure/uncertain-outcome/recovery path. A passing product test suite alone is insufficient.

## 11. Evidence gaps carried into AC-502…AC-507

AC-501 intentionally does not invent the following facts:

1. current exact customer acceptance/obligation status;
2. contractual defect-vs-change interpretation for any specific feedback item;
3. baseline Owner minutes/hours per feedback cycle;
4. baseline cycle time from feedback to validated correction;
5. monetary value or margin of one correction cycle;
6. acceptable false classification rate;
7. actual cost of AI/runtime/CI/build per cycle;
8. customer satisfaction or willingness to pay;
9. whether the same workflow transfers cleanly to a second client/product;
10. whether Arvectum OS adds enough value to justify any dependency.

These become measurement or gate requirements, not assumptions.

## 12. Minimum evidence expected from the M5 implementation

AC-502…AC-507 should make it possible to observe, proportionately:

- feedback item/batch identity and source reference without copying restricted payload unnecessarily;
- classification and whether it changed after review;
- scope/commitment escalation count;
- Owner interventions by class: reserved decision / customer judgment / technical review / local gate / exception;
- elapsed workflow time at a useful level;
- blocked time waiting for Owner/customer/tool/access where material;
- engineering attempts/retries and regression result;
- customer validation outcome;
- rework count/cause;
- incident/uncertain outcome/fallback use;
- evidence completeness/reconstructability;
- control/coordination overhead introduced by the governed workflow;
- any observed reduction in Owner reconstruction or sequencing burden;
- outcome decision at AC-507: `continue / change / stop`.

No M5 metric should be reported as improved unless a real baseline/comparator supports it.

## 13. Why the other candidates remain valuable

Selection of WF-M5-001 does not de-prioritize all other real work.

- AC-108 discovery remains authorized parallel P1 evidence work under AC-106.
- PORT-001 Tender Agent remains A2 and can become a later governed contour when a real suitable case exists.
- finance/obligation packet automation remains important, but source/access readiness should be improved through actual need rather than forced for M5.
- governance publication remains an already-proven bounded workflow and useful control pattern, but not the first new business-operating proof.

P0 obligations/cash/material risk continue to preempt M5 roadmap convenience when a real time-sensitive condition exists.

## 14. Arvectum OS boundary

AC-501 selects a **Company workflow**, not an OS feature.

No Arvectum OS dependency is presumed merely because PORT-002 currently has P6.06/CAP-004 evidence in its product boundary.

AC-503 must separately answer:

- whether WF-M5-001 actually needs Arvectum OS;
- which exact OS capability/Product Contract semantics are applicable;
- whether the dependency creates net evidence/control value;
- what happens when OS is unavailable;
- whether product-local/manual execution remains the safer first implementation.

If no material OS reliance is needed, AC-503 should explicitly record `no required OS dependency for this M5 slice` rather than adding platform coupling for architectural completeness.

## 15. Stop conditions for selection before implementation

WF-M5-001 should be reselected or paused before AC-504 if AC-502/AC-503 establishes any of the following:

- there is no current real customer feedback/acceptance case suitable for supervised operation;
- current contract/customer-rights evidence makes the correction boundary materially ambiguous and cannot be resolved safely;
- required customer/restricted data cannot be handled within AC-206 limits;
- execution requires new material external authority or customer commitment merely to prove the workflow;
- the product is already accepted/closed and no genuine recurring case exists, making the proposed proof artificial;
- the implementation cost becomes disproportionate to the remaining customer/business evidence;
- a real P0 obligation or stronger live candidate clearly dominates and Owner explicitly re-prioritizes.

A stop/reselection under these conditions is a valid governance outcome, not AC-501 failure.

## 16. Decision-ready recommendation

Cross-review should approve AC-501 only if the exact statement below remains supported:

> **Select `WF-M5-001 — Customer Feedback → Classified Correction → Verified Candidate → Customer Validation / Acceptance`, first instantiated on `PORT-002 — Discount Parser`, as the first M5 governed Company operating-contour candidate. Proceed to AC-502 to define the exact workflow, accountable Position, authority/data/evidence contract. Do not infer customer acceptance, new commitment, spend, OS reliance or broader product readiness from this selection.**

Owner approval is required to convert this Proposed selection into Approved Company planning state.