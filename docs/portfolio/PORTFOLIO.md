# Arvectum Company Portfolio

Status: `Active`
Version: `0.1.0`
Created: `2026-08-20`
Updated: `2026-08-20`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-004 — Initial docs/portfolio/PORTFOLIO.md`

## 1. Purpose

This document is the initial Company-level portfolio map for Arvectum Company.

It identifies the material product and initiative nodes currently evidenced by canonical repositories accessible to ООО «Арвектум», records their current Company-level purpose and portfolio role, points to the canonical product/status sources that remain authoritative for implementation detail, and exposes unresolved identity, ownership and dependency questions for later portfolio governance.

This file is intentionally an **initial map, not a final portfolio-governance decision**.

It does **not** by itself:

- rank products by priority;
- approve or allocate budget/capital;
- create a Position or Assignment;
- grant Organizational Authority or legal authority;
- approve customer, production, security, compliance or commercial readiness;
- approve a Product Contract or Arvectum OS dependency;
- merge, supersede, rename or retire a product;
- copy a product roadmap into the Company repository;
- convert repository existence into an investment commitment.

Those decisions remain in later Company roadmap items, especially `AC-301` through `AC-306`, and in the applicable product/OS governance paths.

## 2. Authority and repository boundary

This portfolio is subordinate to applicable legal/corporate authority, the Ratified Company Constitution, approved Company governance, the canonical Company roadmap and the approved Company ↔ Arvectum OS boundary.

Product repositories remain authoritative for product-specific implementation, domain semantics, product roadmaps, release/deployment evidence and product operational state.

`arvectum/arvectum-os` remains authoritative for Arvectum OS platform architecture, capability lifecycle, Product Contracts and governed platform behavior within their declared scopes.

The Company owns the portfolio-level decision about whether a product or initiative is sponsored, funded, prioritized, continued, changed, contained or stopped. No such material stop/continue or capital-allocation decision is made by this `0.1.0` initial map.

Because this repository is public, the portfolio records only repository-suitable information. Customer-confidential data, contracts, pricing, live financial figures, credentials and other restricted operational payloads are not admitted here.

## 3. Inclusion rule

A node is included in the initial map when current canonical repository evidence shows that ООО «Арвектум» owns or sponsors a material product, productized client solution or internal initiative that may require Company-level accountability, investment, dependency or continuity treatment.

Repository existence alone is insufficient.

Accordingly:

- `arvectum/arvectum-company` is the Company governance repository, not a portfolio product;
- `arvectum/arvectum-os` is a shared platform dependency and is mapped separately rather than treated as an ordinary Company product;
- the empty `arvectum/arvectum` repository is not admitted as a product/initiative node by this version.

## 4. Initial material portfolio map

The table below is descriptive. `Observed current state` summarizes evidence from the named product sources and is not a new Company readiness or investment approval.

| ID | Node | Current node type | Company-level business purpose / portfolio role | Canonical implementation repository | Current product/status source | Observed current state | Current Company accountability basis | Known Arvectum OS relation |
|---|---|---|---|---|---|---|---|---|
| `PORT-001` | Tender Agent / Tender Operator product line | Product | Procurement/tender automation product: controlled tender intake, analysis and human-reviewed pre-bid decision support; strategically relevant to the Company's procurement business direction | `arvectum/tender-agent` | `STATUS.md`; `README.md`; `docs/product/` | `STATUS.md` records `R0_CLOSED_FUNCTIONALLY`; repository evidence supports controlled intake/analysis/local-model/reporting with no broad autonomy or external procurement execution | Sponsored by ООО «Арвектум`; no Company Position is created by AC-004; material residual authority remains with the Owner until later delegation | OS `P6.02` Product Contract is `Provisional 0.1.0`, but its repository locator still names predecessor `arutyunoveth/ai-corporation`; identity/repository reconciliation is required before treating the contract locator as current |
| `PORT-002` | Discount Parser | Productized client solution / product | Collect, normalize, deduplicate and classify discount/promo data and support controlled Telegram publication | `arvectum/discount-parser` | `README.md`; `docs/ROADMAP.md` | README records MVP R1–R8 complete and R9 code/distribution implementation complete; live acceptance/CI claims remain bounded by target-machine, credentials and runner/environment evidence | Sponsored by ООО «Арвектум`; accountable Company Position not yet modeled | OS `P6.06` Product Contract `Provisional 0.1.0` explicitly names `arvectum/discount-parser` and the controlled Telegram-publication boundary; no Stable/Active inference follows |
| `PORT-003` | Arvectum Proxy Launcher | Product | Local proxy-routing utility with a productized Windows track; potential standalone commercial/internal infrastructure value | `arvectum/proxy-launcher` | `docs/ROADMAP.md`; `README.md`; `RELEASE_POLICY.md` | Windows `0.2.3` is the verified productization track; production Russian-first signing implementation is repository-complete with local physical-token acceptance still required; macOS/Linux readiness remains separately bounded | Sponsored by ООО «Арвектум`; accountable Company Position not yet modeled | No current Company evidence establishes an Arvectum OS Product Contract. Product operation must not be represented as an OS capability by implication |
| `PORT-004` | Creative Test Agent | Product / controlled-pilot solution | Local-first closed-loop pre-testing of marketing creatives before client presentation, with on-prem/local model operation and controlled reporting | `arvectum/creative-test-agent` | `docs/roadmap/CURRENT.md`; `docs/roadmap/CREATIVE_TEST_AGENT_CANONICAL_ROADMAP*`; `README.md` | Repository contains controlled-pilot, synthetic rehearsal and deterministic release-preparation evidence; the current roadmap pointer requires reconciliation because `CURRENT.md` still describes `CTA-PILOT-PREP-003` as next while later `main` commits record that work and release preparation as completed | Sponsored by ООО «Арвектум`; accountable Company Position not yet modeled | No current Company evidence establishes an Arvectum OS Product Contract for this product |
| `PORT-005` | Tender App / Small-Volume Procurement Calculator | Product / procurement experiment | Local procurement-small-volume workflow: import procurement opportunities, calculate margin/risk, support decisioning, export and dashboard operation | `arvectum/tender-app` | `README.md`; `docs/ROADMAP.md` | Repository exposes demo and production-oriented local paths plus real-source/manual-price caveats; roadmap is directional and does not resolve its long-term relation to Tender Agent | Sponsored by ООО «Арвектум`; accountable Company Position not yet modeled | No current Product Contract identified. Strategic/product-boundary overlap with `PORT-001` requires later reconciliation rather than silent merge |
| `PORT-006` | Doors Parser | Client-delivery product / reusable product experiment | Collect structured door-catalog data from manufacturer sites; also provides evidence of reusable extraction and source-specific parsing techniques | `arvectum/doors_parser` | `README.md` | README records a mature catalog-generation snapshot with 182/182 target lines represented and explicit QA/review outputs; no current canonical product roadmap was identified | Sponsored by ООО «Арвектум`; accountable Company Position not yet modeled | No current Product Contract identified. Any reuse into another parser/product remains a later explicit product/portfolio decision |
| `PORT-007` | Data Platform | Internal/shared initiative | Intended data-platform initiative; exact business boundary, consumers and platform-vs-product role are not yet sufficiently specified in its canonical repository | `arvectum/data-platform` | `README.md`; repository history | Current repository is a bootstrap: README contains only `Data Platform`, while repository history mainly establishes initial/mirror automation. No mature product contract, roadmap or business hypothesis is canonically evidenced there yet | Sponsored by ООО «Арвектум`; accountable Company Position not yet modeled | No OS dependency or Product Contract is inferred. Whether this remains Company/product-local, becomes a product, or proposes domain-neutral OS capability must be decided later from evidence |

## 5. Shared platform dependency — Arvectum OS

Arvectum OS is not an ordinary product node in this portfolio. It is the domain-neutral platform and Executable Organizational Model foundation that Company products or Company workflows may rely on only through applicable governed boundaries.

| Platform | Canonical repository | Current canonical planning source | Current evidenced state relevant to Company |
|---|---|---|---|
| Arvectum OS | `arvectum/arvectum-os` | `docs/roadmap/ROADMAP.md` | Phase 7 is `Complete / PASS` for the declared persistent internal owner-operated scope; Phase 8 remains `Draft / Exploratory`; CAP-001 through CAP-004 remain `Incubating / Provisional`; P6.02 and P6.06 remain `Provisional 0.1.0`; no Stable Product Contract, Active capability or external production/SLA claim follows |

Company sponsorship or ownership of Arvectum OS does not let a product bypass OS contracts, and OS technical capability does not create Company Organizational Authority.

## 6. Current Product Contract / OS reliance map

Only the currently evidenced OS Product Contracts are listed. Absence from this table does not prohibit future OS reliance; it means no current contract is being inferred by AC-004.

| Company portfolio node | OS contract | Status | Current boundary note |
|---|---|---|---|
| `PORT-001` Tender Agent | `arvectum/arvectum-os/docs/contracts/P6-02-FIRST-REAL-PRODUCT-CONTRACT.md` | `Provisional 0.1.0` | Bounded 44-ФЗ pre-bid governed workflow; contract repository locator still references predecessor `arutyunoveth/ai-corporation`, so repository/product identity must be reconciled before later portfolio dependency closure |
| `PORT-002` Discount Parser | `arvectum/arvectum-os/docs/contracts/P6-06-SECOND-REAL-PRODUCT-CONTRACT.md` | `Provisional 0.1.0` | Controlled Telegram publication external-effect/reconstruction boundary; product-domain parser semantics remain product-owned |

No other portfolio node is declared OS-dependent by this document.

## 7. Known portfolio ambiguities and reconciliation backlog

The following are **observed gaps, not decisions**. They are carried forward mainly to `AC-301` and `AC-304`.

1. **Tender Agent repository identity.** Current Company/product work uses `arvectum/tender-agent`, while OS P6.02 still names `arutyunoveth/ai-corporation`. The Product Identity, predecessor history, canonical repository locator and Product Contract references must be reconciled explicitly.
2. **Tender product-family overlap.** `PORT-001` Tender Agent and `PORT-005` Tender App both address procurement workflows. AC-004 does not decide whether they remain separate products, one becomes a module/experiment of the other, or one is retired.
3. **Parser reuse boundary.** `PORT-002` Discount Parser and `PORT-006` Doors Parser contain materially different domain/product logic but both provide parser/extraction evidence. AC-004 does not create a universal parser product, shared engine or OS capability. Reuse/promotion requires an explicit later decision.
4. **Creative Test Agent naming/status pointer.** Company planning has historically used language such as “Marketing Agent”, while the concrete repository is `creative-test-agent`. The canonical product identity and portfolio naming should be reconciled. The repository's `docs/roadmap/CURRENT.md` also appears stale relative to later main-branch completion commits.
5. **Discount Parser roadmap freshness.** `docs/ROADMAP.md` still presents the MVP roadmap as “ready for implementation”, while the current README records R1–R8 done and R9 implementation complete. Product-side canonical status should be reconciled without Company duplicating the roadmap.
6. **Doors Parser lifecycle.** The repository records a mature delivery snapshot but no current roadmap or explicit Company lifecycle state. Maintenance, containment, reuse or retirement criteria remain undefined.
7. **Data Platform definition.** The repository exists but its strategic/economic hypothesis, consumers, boundary and product/platform ownership are not yet canonically specified.
8. **Accountable Positions.** No portfolio node receives a newly invented Position in AC-004. Company Position/accountability design belongs to Phase 2 (`AC-201`–`AC-205`), with portfolio assignment closure later in `AC-302`.
9. **Investment and stop/continue criteria.** AC-004 does not rank capital or owner attention. Explicit investment boundaries and stop/continue criteria belong to `AC-303` and prioritization to `AC-305` after the M1 business/economic baseline exists.

## 8. Initial cross-product relationship hypotheses

These are hypotheses for later review and must not be treated as approved architecture or portfolio structure:

- the Tender Agent and Tender App may form a procurement product family, but current canonical evidence does not yet justify a merge;
- parser implementations may yield reusable product-local components, but validated reuse must precede any shared-platform promotion;
- Data Platform may become a shared Company/product capability only after real consumers, ownership and economics are established;
- Creative Test Agent may become a broader marketing product only through a product-side identity/scope decision;
- Proxy Launcher may support Company/product connectivity needs, but technical usefulness does not make it an Arvectum OS capability or an authority-bearing infrastructure component.

## 9. Portfolio source-of-truth rule

For each node:

- this file is canonical for the **Company-level fact that the node is currently mapped in the portfolio and for the Company-level portfolio relationship recorded here**;
- the product repository remains canonical for implementation, product status, product roadmap and product-domain meaning;
- Arvectum OS remains canonical for OS Product Contracts, capability lifecycle and platform behavior;
- legal, contractual, accounting, banking and customer facts remain in their applicable authoritative systems;
- if a referenced product source conflicts with this map on product implementation/status, the product source wins for product scope and this map must be refreshed rather than silently overriding it.

A future managed portfolio register may replace this Markdown file as the canonical runtime representation only through an explicit Company governance transition preserving history and authority.

## 10. Refresh triggers

Refresh this portfolio when any of the following becomes material:

- a product/initiative is created, admitted, merged, renamed, sold, stopped or retired;
- a canonical product repository changes;
- a Product Contract is created, superseded, stabilized, deprecated or retired;
- an accountable Position or portfolio owner is approved;
- investment/stop-continue criteria are approved;
- a product changes portfolio role materially;
- a cross-product dependency becomes a real commitment;
- an observed ambiguity above is reconciled.

Routine implementation commits do not require a Company portfolio update unless they materially change the Company-level state represented here.

## 11. AC-004 completion boundary

AC-004 is complete when this initial map exists and is sufficient for founding-baseline review without pretending that Phase 3 portfolio governance has already been performed.

This version establishes:

- seven evidence-backed material product/initiative nodes;
- one separately mapped shared platform dependency;
- canonical repository/status-source locators;
- the two currently evidenced OS Product Contract relationships;
- current accountability at the justified pre-Position level;
- explicit unresolved portfolio identities, overlaps and freshness defects for later reconciliation.

The next Company roadmap action is `AC-005 — Founding baseline cross-review and closure`.
