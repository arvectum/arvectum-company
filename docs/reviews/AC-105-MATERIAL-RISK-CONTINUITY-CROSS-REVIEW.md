# AC-105 — Material Risk, Dependency, Continuity and Fallback Baseline Cross-Review

Status: `Complete / PASS`
Review date: `2026-08-20`
Iterations completed: `9 of maximum 10`
Result: `PASS — material dependency and continuity risks are separated from legitimate authority/security gates, minimum fallback expectations are explicit, and unresolved implementation details are correctly handed to later roadmap items without inventing authority, RTO/RPO, private infrastructure or future Positions`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-105 — Material risk, dependency, continuity and fallback baseline`
Reviewed artifact: `docs/business/MATERIAL-RISK-DEPENDENCY-CONTINUITY-FALLBACK-BASELINE.md`
Reviewed publication: `0.1.0`
Maximum review iterations authorized by Owner: `10`

## 1. Review purpose

This cross-review tests whether AC-105 establishes a sufficiently rigorous Company-level material risk/dependency/continuity baseline to close the risk portion of M1 without prematurely performing AC-202/203, AC-206/207, AC-401–404 or product-specific continuity engineering.

The review must preserve the Company principles that:

- AI/software are execution means, not authority sources;
- legitimate Owner/legal/security gates may stop work rather than be bypassed;
- critical organizational meaning/history/data must survive replacement of people, runtimes and vendors;
- customer and external authority boundaries remain intact during degraded operation;
- technology sovereignty means replaceability and recoverability, not ceremonial vendor avoidance;
- public Company artifacts must not expose secrets, customer-confidential data or unnecessary personal data.

## 2. Review lenses

The review uses fourteen functional perspectives:

1. Owner / Founder;
2. General Director / Corporate Authority;
3. Commercial / Customer Commitment;
4. Delivery / Operations;
5. Customer Success / Support;
6. Product / Portfolio;
7. Finance / Liquidity / Procurement Exposure;
8. Technology / Architecture;
9. Security / Identity / Credentials;
10. Data / Privacy / Customer Sovereignty;
11. Technology Sovereignty / Vendor Portability;
12. Arvectum OS / Product Contract Boundary;
13. Risk / Business Continuity;
14. Organizational Design / AI Workforce.

These are review lenses only. They create no Positions, committees, authority or delegation.

## 3. Iteration 1 — False precision and enterprise-BCP theater

**Primary lenses:** Risk, Finance, Operations, Owner.

**Criticism:** The initial risk concept could become a pseudo-enterprise risk register with invented probabilities, availability percentages, annualized losses, RTO/RPO or recovery promises that current evidence cannot support.

**Reconciliation:** The artifact explicitly rejects fabricated probability/MTTR/RTO/RPO and uses consequence-based materiality only: `Company-critical`, `Workstream-critical`, `Degrading`, `Not currently critical`.

It also labels dependency control state rather than assigning unsupported likelihood scores.

The later measurement section captures actual incidents/recovery evidence prospectively.

**Result:** PASS after correction.

## 4. Iteration 2 — Legitimate gate is not automatically a continuity defect

**Primary lenses:** Owner, Corporate Authority, Security, Governance.

**Criticism:** A naive continuity analysis would label Owner approval, legal signature, physical token or customer acceptance as “single points of failure” and recommend bypassing them.

That would violate the owner-operated governance model and could convert technical continuity into unauthorized action.

**Reconciliation:** Section 3.1 now distinguishes deliberate gates from accidental single points of failure.

The artifact states that the correct design pattern is:

`preserve authority/security gate → prepare evidence and bounded work around it → allow safe work to continue → recover/replace execution without fabricating authority`.

A gate becomes a structural bottleneck only when it also blocks work that does not require that authority or when an existing material obligation has no lawful degraded/recovery path.

**Result:** PASS.

## 5. Iteration 3 — Owner absence and legal/corporate continuity must remain separate

**Primary lenses:** General Director, Owner, Legal/Corporate, Risk.

**Criticism:** The current private corporate evidence shows one participant and one person registered to act without power of attorney, but an internal Company document must not invent powers of attorney, successor directors, emergency signatories or legal workarounds.

At the same time, ignoring the concentration would hide a real Company-critical continuity risk.

**Reconciliation:** The main artifact records only the minimum safe evidence already registered by the canonical source registry: one participant, one General Director with a five-year appointment and one person registered as entitled to act without POA at issuance.

It identifies extended unavailability as a material concentration risk but explicitly defers lawful replacement/representation mechanics to the competent corporate/legal path and later authority/continuity work.

The one-day / one-week / extended scenarios distinguish routine organizational continuity from legal corporate continuity.

**Result:** PASS.

## 6. Iteration 4 — Credentials, physical tokens and devices

**Primary lenses:** Security, Operations, Technology, Corporate Authority.

**Criticism:** AC-104 showed recurring Owner-gated local/credential work. AC-105 needed to state what continuity requires without exposing secrets or treating a working credential as proof of Organizational Authority.

It also needed to preserve legitimate physical/signing controls rather than recommending insecure cloning or shared accounts.

**Reconciliation:** `R-04`, `R-05`, `R-09` and Section 7 establish:

- material credential classes must have holder/owner scope, recovery, revocation and rotation semantics later;
- public repo stores no reusable secrets/private keys/recovery codes;
- credential possession is not organizational/legal authority;
- physical/security gates may correctly stop an action;
- local-machine dependency requires re-bootstrap/replacement and data separation rather than bypass of signing/security controls;
- detailed credential topology is explicitly deferred to AC-206.

**Result:** PASS.

## 7. Iteration 5 — Repository sovereignty, mirror semantics and recovery

**Primary lenses:** Technology Sovereignty, Architecture, Risk, Governance.

**Criticism:** Saying “GitVerse mirror exists” is not enough to prove continuity, while saying “GitHub outage means switch to GitVerse” would silently create a new source of truth and conflict with approved repository governance.

Product repositories also have uneven mirror/roadmap maturity.

**Reconciliation:** `R-06`, `R-07` and Section 6 preserve GitHub as canonical, treat GitVerse/local copies as recovery evidence rather than ambient authority, and require an explicit source-commit/authority/reconciliation decision for emergency promotion.

The artifact also records that portfolio-wide mirror/restore coverage is **not uniformly evidenced** and must be proven proportionately later rather than assumed.

Stale product roadmap/status pointers are correctly treated as reconstruction defects, not as a reason for Company to duplicate product truth.

**Result:** PASS.

## 8. Iteration 6 — Customer data, confidentiality and restore semantics

**Primary lenses:** Data, Privacy, Customer Sovereignty, Delivery, Security.

**Criticism:** A continuity plan can create a security/privacy failure if it solves data-loss risk by indiscriminately copying customer data into repositories, backups or shared learning systems.

A byte-level backup may also be operationally useless if authority, version, classification or retention meaning is lost.

**Reconciliation:** `R-08`, `R-20` and Section 8 require identification of authoritative source, scope/acceptance state, data location/classification, backup/reconstruction need, restore meaning, retention/deletion and reuse-rights boundaries.

The public Company repository remains explicitly unsuitable for raw customer data and secrets.

The artifact states that a backup is insufficient merely because bytes exist; restored data must remain current enough, semantically interpretable and lawful for the intended use.

Cross-customer learning remains denied by default without rights/purpose/governance basis.

**Result:** PASS.

## 9. Iteration 7 — External authoritative systems, source drift and suppliers

**Primary lenses:** Product, Procurement, Delivery, Customer Commitment, Risk.

**Criticism:** Current products and procurement work depend on websites, APIs, EIS/ETP, customer inputs, suppliers, contractors, financial providers and other external systems. A Company-level continuity artifact must not pretend it can define product-specific parser fixes, EIS behavior or supplier substitution globally.

It must nevertheless prevent silent stale-data use and expose obligation risk.

**Reconciliation:** `R-10`, `R-13` through `R-18` and Section 9 separate four patterns:

- authoritative external system;
- changing source/API;
- supplier/contractor;
- bank/accounting provider.

The Company rule is explicit: outage or source drift does not convert local/cache data into authority; uncertainty is surfaced; the product/deal workflow owns technical correction/substitution; the Company owns the customer/obligation/risk decision.

Dual sourcing and alternative providers are not invented where economics/evidence do not justify them.

**Result:** PASS.

## 10. Iteration 8 — Arvectum OS must not become an invented Company-wide single point

**Primary lenses:** Arvectum OS, Architecture, Product, Governance, Risk.

**Criticism:** The flagship strategy uses Arvectum OS, so AC-105 could incorrectly describe OS availability as already Company-critical or imply Stable/Active platform commitments that do not exist.

Conversely, ignoring OS Product Contract failure/rollback semantics would hide real product-slice dependencies.

**Reconciliation:** AC-105 re-checks current OS `main` at `d26f9583393d4f3d9ef104f5408439da0471fd76` and records the bounded state: CAP-001–004 remain Incubating/Provisional; P6.02/P6.06 remain Provisional; no Active capability or Stable Product Contract is inferred.

`R-11` and Section 10 therefore state:

- Company durable governance is currently repository-first;
- only admitted product/workflow slices should fail with OS unavailability;
- no hidden Company dependency is permitted;
- product-local/manual fallback is valid only where the applicable product/contract boundary permits it;
- a fallback run cannot be misrepresented as OS-governed completion.

**Result:** PASS.

## 11. Iteration 9 — Completion scope, market risk and handoff discipline

**Primary lenses:** Owner, Commercial, Finance, Organizational Design, all remaining lenses.

**Criticism:** A broad “material risk” task can expand indefinitely into market validation, pricing, portfolio investment, legal compliance, access-control implementation, tested disaster recovery, future Positions and incident tooling.

If AC-105 attempted to close all of those, it would either invent unsupported facts or collapse later roadmap stages.

**Reconciliation:** Sections 13–17 explicitly separate:

- current continuity gaps from evidence of continuity readiness;
- operational dependency risk from still-unvalidated flagship market risk;
- Company baseline from product-specific continuity engineering;
- access/credential expectations from the actual AC-206 matrix;
- baseline fallback requirements from AC-207 tested runbooks;
- management visibility requirements from AC-401–404;
- market/ICP/outcome uncertainty from AC-107/108/106;
- qualitative materiality from future quantitative incident/recovery evidence.

The artifact therefore creates a strong handoff without pre-designing Positions, Assignments, alternate suppliers, legal instruments or infrastructure topology.

**Result:** PASS.

## 12. Acceptance test

| Test | Result |
|---|---|
| identifies material Owner, corporate, credential, device, repository, data, external-service, supplier, financial, product/OS and vendor-sovereignty dependencies | PASS |
| distinguishes deliberate authority/security gates from accidental single points of failure | PASS |
| models one-day, one-week and extended Owner-unavailability effects without inventing authority | PASS |
| preserves distinction between internal Owner authority and legal/corporate representation | PASS |
| does not expose secrets, private keys, credentials, signatures, bank details or unnecessary personal data | PASS |
| treats GitHub as canonical and GitVerse as mirror/recovery evidence rather than ambient co-authority | PASS |
| requires recoverability without claiming that mirror existence proves tested restoration | PASS |
| keeps product repos authoritative for product implementation/continuity detail | PASS |
| preserves external source authority and stale/uncertain state instead of inventing local truth | PASS |
| preserves customer isolation, purpose, retention/deletion and reuse-right boundaries | PASS |
| treats banking/accounting as external professional/authoritative contours rather than recreating them | PASS |
| captures procurement supplier and working-capital continuity risk without fabricating live exposure | PASS |
| re-checks current Arvectum OS state and does not infer Stable/Active platform maturity | PASS |
| distinguishes OS product-slice dependency from Company-wide governance dependency | PASS |
| keeps AI/model/runtime replaceable and non-authoritative | PASS |
| defines fail-closed/degraded-mode expectations | PASS |
| does not fabricate probability, RTO/RPO, SLA, MTTR or incident history | PASS |
| does not invent alternate signatories, credential holders, Positions, headcount or AI Assignments | PASS |
| identifies explicit gaps for AC-202/203, AC-206/207 and AC-401–404 | PASS |
| separates AC-105 continuity scope from AC-107/108 market-validation risk | PASS |
| creates a clear roadmap handoff to AC-107 | PASS |

## 13. Why the review closes at iteration 9 of 10

The Owner authorized a maximum of ten iterations, not a requirement to consume all ten.

After iteration 9, the remaining unresolved items are intentionally downstream work rather than defects in the AC-105 baseline:

- final Reserved Owner Decisions → AC-202;
- delegated Position authority and escalation limits → AC-203;
- actual Position/Assignment model → AC-201/204/205;
- credential/tool/data-access matrix and restricted credential inventory → AC-206;
- tested recovery/replacement/manual-fallback runbooks → AC-207;
- live risk/incident/obligation registers and Mission Control → AC-401–406;
- product-specific backup/restore/source-failure engineering → product repositories;
- OS contract/capability continuity semantics → Arvectum OS/Product Contracts;
- flagship ICP, buyer, measurable outcome and market evidence → AC-107/108/106;
- legal/corporate representation changes → competent legal/corporate authority.

A tenth review iteration would therefore either repeat already passed lenses or prematurely perform one of these later tasks.

## 14. Final conclusion

`PASS — material consensus reached at 9 of maximum 10 iterations.`

AC-105 is complete as a Company-level material risk, dependency, continuity and fallback baseline.

It does **not** claim that Arvectum Company is currently continuity-ready. It establishes what must be preserved, what may safely pause, what cannot be bypassed and which evidence later continuity/access/operating-model work must produce.

Recommended roadmap transition:

`AC-105 Complete / PASS → AC-107 Current`.
