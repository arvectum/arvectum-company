# AC-208 — Reference-Model Transferability Boundary and M2 Operating-Model Closure

Status: `Proposed`
Version: `0.9.0`
Created: `2026-08-21`
Updated: `2026-08-21`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-208 — Reference-model transferability boundary and operating-model cross-review`
Review: `docs/reviews/AC-208-REFERENCE-MODEL-TRANSFERABILITY-CROSS-REVIEW.md`
Depends on: M1 business baseline and AC-201 through AC-207
Approval required: explicit Owner approval before M2 closure and this transferability boundary become binding Company state

## 1. Purpose

AC-208 closes the design/review loop for Phase 2 by testing the complete Arvectum Company operating-model chain and separating **what is reusable as a method/reference pattern** from **what is specific to the current organization instance of ООО «Арвектум»**.

The Phase 2 chain under review is:

```text
M1 business / economic / obligation / workload / risk evidence
→ AC-201 durable functions
→ AC-202 Reserved Owner Decisions
→ AC-203 delegated Position authority semantics
→ AC-204 concrete Positions
→ AC-205 Principal / Assignment / executor realization
→ AC-206 data / tool / credential access ceilings
→ AC-207 continuity / replacement / fallback semantics
```

The purpose is not to declare the organization “finished”, production-ready, profitable, customer-ready or fully autonomous. The purpose is to determine whether the **reference operating model and authority architecture are coherent enough to become the stable Phase 2 baseline** while preserving all explicitly unresolved empirical and implementation questions.

The governing distinction is:

```text
reusable derivation method
≠ reusable organization instance
≠ reusable product/module
≠ Arvectum OS platform semantics
```

## 2. Canonical-state re-check

Arvectum Company `main` was re-checked immediately before AC-208 drafting. The current canonical roadmap is `0.20.0`; AC-201 through AC-207 are `Complete / PASS`; AC-208 is the current action.

The underlying full roadmap `0.14.0` remains incorporated by immutable history and defines:

- milestone `M2 — Arvectum Company reference operating model and authority established`;
- M2 exit criteria centered on real Position justification, explicit authority/escalation, executor-neutrality, bounded access/fallback, replacement without loss of organizational meaning, and a clear reusable-vs-non-reusable boundary;
- the next planned milestone `M3 — Product/module-candidate portfolio governed as investments` beginning with `AC-301 — Portfolio product/node identity and ownership reconciliation`.

Arvectum OS `main` was re-checked at current commit `2c0cc461504bab489cd5d4fe89456e634ef81e59` (`P8.11 — ecosystem architecture hardening and lifecycle disposition`). The Company-relevant authority boundary remains unchanged for AC-208 purposes:

- OS remains the domain-neutral platform/governed-execution layer rather than the source of Company corporate authority;
- the OS `DECISION-AUTHORITY-POLICY.md` remains `Proposed 0.2.1` and is not used as binding Company authority;
- no current OS roadmap progress automatically creates a Company Position, customer authority, Product Contract, Company delegation or Company readiness claim.

## 3. End-to-end coherence result

### 3.1 Business evidence → functions

`PASS`.

AC-201 did not begin from agents, departments or a target org chart. It derived eight durable function domains from current value creation, customer delivery, management control, portfolio workload, financial obligations, organizational-state reconstruction, security and continuity evidence.

The exact eight-function result is **Arvectum-specific**. The reusable element is the admission test:

```text
real value / obligation / workload / control / continuity need
→ distinguishable durable responsibility
→ function only if the responsibility survives executor replacement
```

### 3.2 Functions → Reserved Owner Decisions

`PASS`.

AC-202 reserves decision gates rather than reserving whole functions. This prevents two opposite failures:

- every difficult action remaining with the Owner forever; and
- “automation” silently consuming strategic, capital, material commitment, risk, sovereignty or Company↔Product↔OS authority.

The exact `ROD-01` through `ROD-09` catalog is the approved Arvectum Company instance. It is reference evidence, **not a universal customer catalog**.

### 3.3 Reserved decisions → delegated Position authority

`PASS`.

AC-203 creates an executor-neutral delegation model (`AM-0` through `AM-4`), deny-by-default authority, explicit escalation and the effective-execution intersection:

```text
Position authority envelope
∩ Assignment scope
∩ technical authorization/access
∩ current workflow/data/risk conditions
= maximum executable action
```

This remains coherent with AC-202 because the `ROD-*` catalog is a hard negative boundary and because Assignment/access/runtime capability cannot expand authority.

### 3.4 Authority model → concrete Positions

`PASS`.

AC-204 creates six durable Positions from the eight functions rather than one Position per function:

- `POS-001 — Company Executive` (`F-01 + F-07`);
- `POS-002 — Commercial & Customer Lead` (`F-02 + F-03`);
- `POS-003 — Portfolio & Product Lead` (`F-04`);
- `POS-004 — Engineering & Release Lead` (`F-05`);
- `POS-005 — Finance & Obligation Control Lead` (`F-06`);
- `POS-006 — Security, Risk & Continuity Lead` (`F-08`).

The split between Finance and Security/Risk/Continuity and the bundling of Organizational State/Evidence with Company Executive are justified for **current Arvectum evidence**. Neither choice is a reusable default organization chart.

No Position receives `AM-3` or `AM-4` merely by existing.

### 3.5 Positions → Assignments/executors

`PASS`.

AC-205 preserves Position meaning while mapping the current executor reality:

- POS-001 hybrid Owner + AI advisory/preparation;
- POS-002 hybrid Owner + AI search/research/qualification/drafting/bounded outreach + accounting support + conditional future human sales capacity;
- POS-003 hybrid Owner + AI synthesis/advice;
- POS-004 AI-led bounded engineering execution;
- POS-005 Owner + outsourced accounting/tax interface;
- POS-006 hybrid Owner + AI analysis/advice.

This is a current Assignment baseline, not a target staffing plan and not a requirement for customer organizations.

The same human Principal currently holding multiple Positions does not merge their authority or evidence contexts.

### 3.6 Assignments → access

`PASS`.

AC-206 derives technical access after Assignment rather than treating credentials as authority. Deny-by-default / least privilege, the `DC-*`, `RA-*` and `R/W/X/P/K/E` model, customer isolation and the prohibition on putting reusable secrets in public Git/ordinary model context remain consistent with the executor design.

The access model gives AI-led Engineering meaningful bounded write/build/test capability rather than reducing it to advisory work, while excluding ambient Owner-wide bank/signing/admin/customer/commercial access.

Therefore access control does not defeat the AI-native objective and does not create hidden AI authority.

### 3.7 Access → continuity/replacement

`PASS`.

AC-207 preserves the distinction between continuity and bypass through `CM-0` through `CM-4` and `CE-0` through `CE-3`.

Runtime replacement, Principal replacement, provider replacement, device replacement and legal/corporate succession remain distinct. A replacement executor does not inherit authority merely because the previous executor or dependency is unavailable.

The model is therefore structurally compatible with the constitutional requirement that Positions, authority and organizational history survive technology/executor replacement.

## 4. M2 exit-criteria review

| M2 exit criterion | Result | AC-208 finding |
|---|---|---|
| every modeled Position exists because of real responsibility, workload, control need or economic value | `PASS` | AC-201/204 trace all six Positions to current durable functions; no department/headcount is admitted for symmetry |
| authority and escalation boundaries are explicit | `PASS within Phase 2 design scope` | AC-202/203 establish reserved/delegated/fail-closed semantics; concrete Position ceilings and exclusions exist |
| humans, AI and software remain Assignments/executors rather than authority sources | `PASS` | AC-204/205 separate Position from executor; AI-led POS-004 does not become an authority source |
| sensitive access and critical fallback paths are bounded | `PASS as governance baseline; implementation evidence incomplete` | AC-206/207 establish ceilings/modes and explicitly retain untested/unresolved gaps |
| replacing an executor does not destroy Position meaning/history | `PASS as model` | executor-neutral Position model and AC-207 runtime/Principal replacement distinction are explicit |
| Company can explain what is transferable and what must not be copied | `PASS upon approval of AC-208` | sections 5–8 establish the binding transferability boundary |

Conclusion: **M2 is eligible for closure within its declared planning/governance scope** if the Owner approves this exact reviewed AC-208 publication.

## 5. Transferability classification

AC-208 establishes five reuse dispositions for Phase 2 artifacts and lessons.

### `TR-1 — Reusable derivation method`

A method for deriving an organization from its own evidence. Strong candidate for reuse across customer diagnostics and future AI-company implementations.

Examples:

- business/value/obligation/risk evidence before organization design;
- function admission/minimality test;
- Position-before-executor sequence;
- explicit reserved-vs-delegable decision analysis;
- Assignment/access/continuity derived only after Position and authority boundaries;
- evidence/proportionality/fail-closed discipline.

### `TR-2 — Reusable governance/control pattern, customer-specific parameters required`

A pattern may be reused as a starting mechanism, but the customer's authority sources, consequence classes, data rights, systems and risk appetite must supply the actual values and boundaries.

Examples:

- executor-neutral Position authority;
- `AM-0`…`AM-4` style separation between preparation, execution, bounded decision, delegated approval and pre-authorized automation;
- deny-by-default delegation;
- separation of approval from execution;
- least-privilege access after Assignment;
- continuity/degraded/fail-closed/reconciliation model;
- minimum continuity packet;
- explicit capacity/context when one person holds multiple responsibilities.

### `TR-3 — Arvectum Company organization instance; do not copy by default`

Company-specific facts/configuration that require complete re-derivation in every customer organization.

Includes:

- the exact `F-01` through `F-08` set and grouping;
- the exact `POS-001` through `POS-006` registry;
- the placement of `F-07` with POS-001;
- the Finance/Security Position split as the current Arvectum result;
- the exact `ROD-01` through `ROD-09` catalog;
- the current Owner holding POS-001/002/003/005/006;
- POS-004 being AI-led;
- outsourced accounting under the current POS-005 interface;
- future sellers being scoped under POS-002;
- the exact `RA-01` through `RA-18` resource set;
- current `CE-0`/`CE-1` continuity gaps;
- Arvectum-specific repository, product, bank, signing, infrastructure and customer-system topology.

A customer may coincidentally reach similar results, but similarity is not evidence of applicability.

### `TR-4 — Product/module candidate; Phase 3 evidence required`

A workflow, component or practice that might become reusable implementation but has **not** become a module merely because Arvectum uses it.

Examples include commercial-search/outreach mechanics, engineering automation, state synchronization, continuity tooling, portfolio evidence synthesis or product-derived functionality.

Admission as a reusable module requires Phase 3/5 evidence on function/job, inputs/outputs, authority assumptions, data/tool boundary, quality/cost/risk, configuration/customization, versioning, support, fallback and ownership.

### `TR-5 — Arvectum OS domain-neutral semantics; OS-owned governance path`

Domain-neutral semantics that already belong to or may legitimately be proposed to Arvectum OS must remain in the OS governance domain.

Examples include identity, canonical-record/version semantics, authorization architecture, organization isolation, governed execution, provenance, portability and other accepted platform contracts.

A Company lesson does not become OS capability or contract merely because it appears reusable. Promotion requires the applicable OS RFC/ADR/capability/Product Contract path.

## 6. Customer-specific re-derivation rule

A future customer-specific AI-native company MUST begin from that customer's own sources and evidence, not from `POS-001`…`POS-006`.

The reference derivation sequence is:

```text
customer legal/corporate authority + contracts
→ customer business model / value streams / obligations / economics / risks
→ durable functions
→ reserved decisions + legal/customer gates
→ Position/accountability boundaries
→ delegated authority and escalation
→ Principal / Assignment / executor choices
→ data/tool/credential access
→ continuity/replacement/fallback
→ workflows + knowledge + evidence
→ reusable/customer-specific module selection
→ Arvectum OS governed representation/execution where admitted
```

At every step, customer Organizational Authority remains with authorized customer Principals. Arvectum Company, Arvectum OS, an implementation engineer or an AI executor cannot manufacture that authority through technical configuration.

## 7. Transferability admission test

Before reusing any Arvectum Company artifact/pattern in another organization, the implementation must answer:

1. **Business basis:** what customer value/obligation/workload/control need justifies it?
2. **Authority basis:** what customer legal/corporate/organizational source creates the relevant authority?
3. **Scope:** what exactly is reusable — method, pattern, implementation module or platform contract?
4. **Customer specificity:** which Arvectum assumptions must be removed or re-derived?
5. **Data/rights:** what customer data, confidentiality, purpose, retention and sovereignty constraints apply?
6. **Risk/consequence:** what reversibility, materiality and escalation boundary applies in that customer?
7. **Executor independence:** would the meaning survive changing the current person, model, agent, service or vendor?
8. **Evidence maturity:** is the reuse only a plausible pattern, internally evidenced, or externally repeated?
9. **Canonical ownership:** does the resulting artifact belong to the customer, a product, Arvectum Company or Arvectum OS?
10. **Exit/replacement:** can the customer recover, replace or exit without Arvectum/runtime possession becoming the source of organizational meaning or authority?

If these questions cannot be answered sufficiently, the artifact is not admitted as a reusable customer pattern/module yet.

## 8. Phase 2 artifact disposition

| Artifact | Reusable lesson | Must be re-derived / must not be copied literally |
|---|---|---|
| `AC-201` function model | evidence-first minimal-function derivation | exact eight functions and their boundaries |
| `AC-202` Reserved Owner Decisions | identify reserved decision gates separately from delegable work | exact nine ROD classes, materiality interpretation and corporate source |
| `AC-203` delegated authority model | executor-neutral authority, explicit envelopes, approval/execution separation, escalation/fail closed | actual customer delegations, limits, approvers and legal/customer constraints |
| `AC-204` Position Registry | derive smallest accountable Position set from function/control evidence | six Arvectum Positions and current bundling/splits |
| `AC-205` Assignments | choose human/AI/software/external realization only after Position/authority | current Owner concentration, AI-led Engineering, accounting/sales arrangement |
| `AC-206` access boundary | access ≠ authority; least privilege after Assignment; protect secrets | exact resource/data topology, accounts, customer rights and provisioning |
| `AC-207` continuity | continue/degrade/fail-closed/reconcile; replacement ≠ authority transfer | exact dependencies, evidence maturity and fallback availability |

## 9. Business-first and readiness review

Phase 2 improves governance and creates reference evidence, but it does **not** resolve the empirical questions deliberately left by M1.

The following remain unproven and MUST NOT be inferred from M2 closure:

- validated flagship demand;
- willingness to pay or pricing;
- customer ROI;
- repeatable acquisition/onboarding;
- implementation/support unit economics;
- profitability of the flagship offer;
- measured Owner-time reduction caused by Phase 2;
- full access-model implementation;
- production-grade continuity/DR;
- legal succession/alternate-representation readiness;
- first reusable governed module;
- first AI-held Position proven economically/operationally/replaceably;
- first external customer deployment;
- customer-ready or multi-customer Arvectum OS operating claim.

In particular, POS-004 being classified as `AI-led` in AC-205 is an **organizational Assignment baseline**, not completion of milestone M6. M6 still requires real supervised operating, quality, cost, risk, value and replacement evidence.

The AC-108 bounded market-discovery loop remains a parallel P1 evidence activity under the approved M1 priority decision. M2 closure does not create a pilot, price, SLA, production access or customer commitment.

## 10. Owner bottleneck review

Phase 2 has made Owner concentration explicit rather than pretending it has been solved.

Current human concentration remains:

- POS-001, POS-002, POS-003, POS-005 and POS-006 are held by the current Owner Principal;
- extended Owner/legal-representation continuity remains unresolved;
- many concrete delegation thresholds and actual alternative human Assignments do not yet exist;
- AC-206 access provisioning and AC-207 continuity drills are not fully implemented/tested.

This does not invalidate M2 because the milestone establishes the **reference operating model and authority architecture**. It does mean that later implementation and evidence must measure whether the model actually reduces Owner workload.

A future increase in automation or headcount MUST be justified by real workload/economic/control evidence rather than by the existence of a Position.

## 11. Company ↔ Product ↔ Arvectum OS ↔ Customer closure rule

The combined Phase 2 model remains coherent only while the following ownership boundary is preserved:

- **Company:** Company business identity, portfolio sponsorship, Company functions/Positions/Assignments, Company authority, Company-specific access/continuity requirements and Company decisions;
- **Product:** product-domain implementation, schemas, product workflows, prompts/agents/validators, release truth and product-specific evidence;
- **Arvectum OS:** domain-neutral platform contracts/mechanisms, governed execution, identity/security/provenance/portability semantics within accepted governance;
- **Customer:** customer business meaning, customer corporate/organizational authority, customer data rights, customer acceptance and customer-specific organizational model.

No Phase 2 artifact creates a hidden cross-repository commitment. If later Company/customer needs require new OS behavior, the requirement must be classified and routed through the applicable OS governance path rather than being implemented as Company-specific platform semantics.

## 12. M2 closure recommendation

AC-208 concludes:

`M2 — ARVECTUM COMPANY REFERENCE OPERATING MODEL AND AUTHORITY ESTABLISHED: PASS FOR OWNER APPROVAL`

The conclusion is limited to the Phase 2 planning/governance scope.

If approved:

- AC-208 becomes `Complete / PASS`;
- milestone M2 becomes `Complete / PASS`;
- AC-201 through AC-208 become the current canonical reference operating-model baseline;
- the exact Arvectum organization instance remains revisable when real evidence changes;
- reusable customer work is governed by the transferability rules above;
- unresolved operational/market evidence remains explicitly open rather than being upgraded by milestone closure.

## 13. Next roadmap handoff

The incorporated canonical roadmap already defines Phase 3:

`M3 — Product/module-candidate portfolio governed as investments`.

The next primary Company action after approved M2 closure is therefore:

`AC-301 — Portfolio product/node identity and ownership reconciliation`.

This is the correct business-first handoff because the Company now has an approved accountable operating model and can revisit its seven mapped portfolio nodes without inventing a separate product owner for every repository or prematurely declaring products to be reusable modules.

AC-301 must reconcile portfolio identity/ownership facts before AC-302 maps accountable Positions, AC-303 sets investment/stop-continue boundaries and AC-304 decides standalone-product/reference/module/OS-capability roles.

## 14. Non-effect boundary

Approval of AC-208 / M2 closure does **not** by itself:

- hire or appoint another person;
- activate a future seller Assignment;
- provision any account/credential/access;
- activate `AM-3` or `AM-4`;
- delegate a `ROD-*` final decision;
- create legal/corporate power, power of attorney or succession mechanism;
- approve a budget, investment or product stop/continue decision;
- change any product repository or product roadmap;
- classify any current product as a reusable module;
- create or promote an Arvectum OS capability/Product Contract;
- make Arvectum Company's six Positions a customer template;
- claim market validation, profitability, production readiness, continuity readiness or external customer readiness.

Those effects require their own evidence and applicable authority path.
