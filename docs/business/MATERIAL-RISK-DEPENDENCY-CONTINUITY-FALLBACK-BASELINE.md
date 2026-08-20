# AC-105 — Material Risk, Dependency, Continuity and Fallback Baseline

Status: `Complete / PASS`
Version: `0.1.0`
Created: `2026-08-20`
Updated: `2026-08-20`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-105 — Material risk, dependency, continuity and fallback baseline`
Review: `docs/reviews/AC-105-MATERIAL-RISK-CONTINUITY-CROSS-REVIEW.md`

## 1. Purpose

This baseline identifies the material dependency and continuity risks that can stop, materially delay or materially damage the current operation of Arvectum Company.

It converts the economic/obligation boundary from AC-102, the real customer/value-stream boundary from AC-103 and the Owner/manual-work dependency map from AC-104 into a Company-level continuity view.

The purpose is to answer five questions before Phase 2 organizational design:

1. what current work can stop if a critical Principal, credential, workstation, repository, external service, customer input, supplier or platform dependency becomes unavailable;
2. which current gates are deliberate authority/security controls and which are accidental single points of failure;
3. what minimum degraded-mode, recovery, replacement or stop behavior should exist for material dependencies;
4. what evidence is still missing before Company data/tool/access design and tested continuity design can be completed;
5. which risks belong to Company governance and which remain product-, OS-, legal-, accounting- or customer-specific.

This artifact is a **baseline**, not a business-continuity plan, disaster-recovery runbook, access matrix, legal succession instrument, SLA, RTO/RPO commitment, vendor-selection decision or future organization design.

## 2. Authority and evidence boundary

### 2.1 Governing Company principles

The Ratified Company Constitution requires that critical functions should not depend on one irreplaceable combination of person, model, vendor, workstation, cloud account or proprietary representation without an accepted risk and recovery path. Critical workflows should have proportionate reconstruction, restore/re-bootstrap, credential recovery/rotation, replacement-runtime, degraded-mode and incident-escalation paths.

The Company repository structure additionally establishes that:

- GitHub `arvectum/arvectum-company` is the current canonical remote;
- GitVerse is a resilience/sovereignty mirror, not a co-equal authority;
- an outage does not silently change canonical authority;
- any emergency promotion/recovery path must identify source commit, decision authority and reconciliation path;
- critical history must remain recoverable without either hosting vendor becoming the owner of Organizational Authority or the only copy of history.

### 2.2 Input evidence

This baseline relies primarily on:

- `docs/constitution/COMPANY-CONSTITUTION.md`;
- `docs/governance/CANONICAL-REPOSITORY-STRUCTURE.md`;
- `docs/governance/COMPANY-OS-AUTHORITY-BOUNDARY.md`;
- `docs/business/REVENUE-CASH-COST-OBLIGATION-BASELINE.md`;
- `docs/business/CURRENT-CUSTOMER-LIFECYCLE-AND-VALUE-STREAM.md`;
- `docs/business/OWNER-WORKLOAD-MANUAL-WORK-BOTTLENECK-MAP.md`;
- `docs/portfolio/PORTFOLIO.md`;
- the private legal/corporate source set registered in `docs/CANONICAL-SOURCES.md`;
- current product/OS canonical repository evidence where dependency state materially matters.

The private legal/corporate source set currently evidences, at the minimum safe Company level, one participant holding 100% of the charter capital, one General Director appointed for a five-year term and one person registered as entitled to act for the Company without a power of attorney at issuance. This artifact does not reproduce personal identifiers, signatures, banking details or addresses.

### 2.3 Current Arvectum OS re-check

Arvectum OS `main` was re-checked for AC-105 at current commit `d26f9583393d4f3d9ef104f5408439da0471fd76`.

The current Company-relevant platform state remains bounded:

- Constitution `1.2.0` Ratified;
- RFC-0001 through RFC-0008 Accepted `1.0.0`;
- Decision Authority Policy still `Proposed 0.2.1`;
- CAP-001 through CAP-004 remain `Incubating / Provisional`;
- P6.02 and P6.06 remain `Provisional 0.1.0`;
- Phase 8 is active for bounded external-integration validation, but no Platform Capability becomes `Active` and no Product Contract becomes `Stable` by roadmap progress alone.

Therefore AC-105 must not treat Arvectum OS as an already universal, stable or externally supported Company runtime dependency.

## 3. Risk model without false precision

No Company-wide incident history, probability model, measured RTO/RPO set, complete asset inventory or complete credential register currently exists.

AC-105 therefore does **not** fabricate likelihood percentages, expected annual loss, MTTR, availability targets or recovery times.

Instead, materiality is classified by **failure consequence**:

- `Company-critical` — failure can block Company-level legal/authority operation, material obligations, critical cash/external action, or loss of critical organizational history/data;
- `Workstream-critical` — failure can stop or materially damage one customer/product/workstream while the Company remains governable;
- `Degrading` — failure materially reduces speed/quality/Owner capacity but a bounded manual or replacement path can preserve essential operation;
- `Not currently critical` — strategically relevant, but current Company operation does not yet depend on its continuous availability.

Dependency control state is classified as:

- `Deliberate gate` — unavailability is allowed to stop the consequential action because the gate protects authority/security/data integrity;
- `Single point / unresolved` — one unavailable person/resource can block material work and no sufficient alternate path is currently evidenced;
- `Fallback exists but is not yet tested Company-wide` — a plausible mirror/manual/product-local path exists, but restore/recovery evidence is incomplete;
- `Product/external-owned` — Company must understand the dependency but implementation/recovery remains canonical elsewhere;
- `Unknown` — evidence is insufficient and must be gathered later.

### 3.1 Deliberate gate versus single point of failure

A control is **not** a defect merely because it can block an action.

Examples of legitimate stop gates include:

- explicit Owner approval for material strategy/capital/risk/commitment decisions;
- legal-signature or corporate-representation actions requiring the proper authorized Principal;
- physical/credential-bound signing where bypass would weaken security or legal validity;
- customer approval/acceptance where the customer remains the authority for its own decision;
- fail-closed behavior when source authority, data scope, Organization scope or authorization is uncertain.

A legitimate gate becomes an operational single point of failure when the same unavailable Principal/resource also blocks work that **does not itself require that authority**, or when a material existing obligation has no bounded degraded/recovery path.

The target is therefore not “remove every gate”. The target is:

`preserve authority/security gate → prepare evidence and bounded work around it → allow safe work to continue → recover/replace execution without fabricating authority`.

## 4. Material dependency map

| ID | Dependency / failure mode | Current consequence | Materiality | Current control state | Minimum continuity expectation |
|---|---|---|---|---|---|
| `R-01` | Owner unavailable as residual strategic/organizational authority | new material strategy, capital, risk, portfolio and governance decisions pause; many current workstreams also lose interpretation/priority context | `Company-critical` for extended absence; `Degrading/Workstream-critical` sooner | `Deliberate gate` + `Single point / unresolved` around preparation/context | preserve reserved decisions, but separate evidence preparation/routine execution; later define succession/delegation/escalation and continuity behavior without converting technical access into authority |
| `R-02` | current legal/corporate representation concentrated in one evidenced General Director / person entitled to act without POA | legally/signature-sensitive actions may pause if the authorized representative cannot act | `Company-critical` where a time-sensitive legal obligation exists | `Deliberate gate`; alternative legal representation path not evidenced in current Company sources | later legal/corporate continuity review must identify lawful replacement/representation mechanisms and triggering conditions; AC-105 creates no power of attorney or corporate appointment by implication |
| `R-03` | customer/commercial context exists primarily in Owner memory | scoping, defect-vs-change classification, acceptance, support and promise interpretation can stall or be performed incorrectly | `Workstream-critical` | `Single point / unresolved` | keep scope, exclusions, current state, acceptance evidence, material commitments and open exceptions reconstructable in a suitable private/canonical source |
| `R-04` | Owner-held or narrowly held credentials / physical tokens / admin access | repository write, signing, banking, EIS/ETP, infrastructure or other external-effect work can stop; compromise can create unauthorized effect | `Company-critical` for some credential classes; otherwise `Workstream-critical` | mostly `Deliberate gate`, but recovery/holder coverage not yet mapped Company-wide | restricted credential inventory, accountable holder/owner, recovery/rotation/revocation path, no secrets in public repo, and no credential possession treated as Organizational Authority |
| `R-05` | Owner-controlled local workstation / OS / physical execution environment unavailable | packaging, local acceptance, signing, target-machine verification or other environment-specific work may stop even when engineering is complete | `Workstream-critical`; potentially `Company-critical` if tied to time-sensitive legal/external obligation | `Single point / unresolved` for some current paths | reproducible re-bootstrap/build/test instructions, replaceable machine path, data separated from device, and explicit rule that security/signing controls are not bypassed merely for continuity |
| `R-06` | GitHub unavailable, account locked or repository access lost | canonical Company publication and cross-repository work are blocked; history remains at risk if independent copies are stale/unusable | `Company-critical` for prolonged history loss; usually `Degrading` for short outage | `Fallback exists but is not yet tested Company-wide` | independent mirror/local copy, periodic freshness/restore evidence, explicit emergency source-commit decision and reconciliation; outage must not silently make GitVerse co-canonical |
| `R-07` | product repositories lost, inaccessible or internally stale | product implementation/history/status may become unreconstructable; Company portfolio state can diverge from product truth | `Workstream-critical`; aggregate effect can become Company-critical | mirror/restore coverage is not uniformly evidenced across portfolio | critical repos need independent recoverable history, restore test proportionate to importance and current canonical-status pointer; Company must not duplicate product truth as a substitute |
| `R-08` | customer/project data exists only in one local/runtime/vendor location | work may be impossible to resume; confidentiality or evidence may be lost; deletion/retention obligations may become impossible to prove | `Workstream-critical`, potentially `Company-critical` for material obligations | `Unknown` Company-wide; product/runtime specific | identify authoritative source, backup/reconstruction need, retention/deletion boundary, access control and restore path; no raw customer data copied into public Company repo |
| `R-09` | credential compromise or unauthorized privileged access | data exposure, unauthorized external action, repository tampering or customer-impacting change | `Company-critical` when privileged scope is material | security control boundary exists, detailed access model deferred | stop external effects where appropriate, revoke/rotate, preserve evidence, verify canonical state, restore from trusted history and escalate material risk; AC-206 owns the actual access boundary |
| `R-10` | external authoritative service/source unavailable or changes behavior/schema | EIS/ETP facts cannot be verified; websites/APIs may stop parsers; Telegram/other integration path may fail; cached/local state may become stale | mostly `Workstream-critical` | `Product/external-owned` | preserve external authority, fail/mark unavailable/uncertain rather than invent truth, support retry/manual/degraded path where contract permits, and treat source/schema change as evidence for product correction rather than hidden data mutation |
| `R-11` | Arvectum OS unavailable or incompatible | only the product/workflow slices that actually rely on admitted OS contracts should be affected; current Company governance remains repository-first | `Not currently Company-critical`; `Workstream-critical` for admitted slices | `Product/external-owned`; provisional boundaries | no hidden Company dependency; respect Product Contract failure/rollback semantics; where a product contract permits product-local/manual fallback, represent that path honestly and do not claim OS-governed completion |
| `R-12` | AI model/provider/runtime unavailable or degraded | coding, analysis and preparation throughput may fall; if organizational meaning lives in prompts/model state, reconstruction risk appears | currently `Degrading`; can become `Workstream-critical` if badly designed | replaceability principle exists; concrete runtime fallback not Company-wide | keep authority, workflow meaning, knowledge and history outside one model/vendor; allow human/manual or replacement-runtime execution; do not make model availability a source of authority |
| `R-13` | bank/payment service unavailable or banking access blocked | supplier/customer cash movements, mandatory payments or financing actions may be delayed | `Company-critical` when time-sensitive obligations exist | external financial dependency; detailed alternative path not evidenced | accounting/banking contour remains authoritative; Company management must know material due obligations and escalation; any alternate-bank/provider action follows proper financial/legal authority |
| `R-14` | outsourced accounting/provider unavailable | statutory/accounting execution and management information may be delayed; Company can lose visibility into due obligations | `Workstream-critical`, potentially Company-critical near statutory deadlines | `Product/external-owned` professional function | preserve source documents/access and transition/recovery expectations without rebuilding bookkeeping in Company repo; material deadline/exception must reach Owner management |
| `R-15` | procurement supplier/contractor unavailable, late or unable to perform | committed delivery may fail; working-capital, margin and customer obligation can worsen | `Workstream-critical`, potentially Company-critical for a material contract | supplier redundancy not established Company-wide | before material commitment, identify dependency, substitution feasibility, timing/cash downside and escalation; alternate sourcing is deal/product evidence, not a generic assumed fallback |
| `R-16` | customer input, access, validation or acceptance unavailable | delivery waits; rework may increase; internal team can misclassify a customer-blocked state as an engineering failure | `Workstream-critical` | external/customer authority dependency | explicit `Blocked — customer input` / validation state, current request/evidence, follow-up/escalation rule and no silent scope invention |
| `R-17` | commitment/acceptance/support terms are ambiguous or not reconstructable | open-ended rework, accidental overcommitment, missed obligation or dispute | `Workstream-critical`, aggregate business risk `High` | `Single point / unresolved` in current Owner-led lifecycle | preserve exact scope/exclusions, accepted deliverable, support boundary, change classification and closure evidence; later operating model owns control points |
| `R-18` | current cash / commitments / procurement cash-gap cannot be seen at decision time | Company can accept work or spend capital without understanding downside; procurement can create a working-capital gap | potentially `Company-critical`; current magnitude is unknown | management interface defined by AC-102; live view not yet implemented | no material new commitment when decision-relevant liquidity/obligation evidence is unavailable; use accounting/management sources rather than fabricate figures in repo |
| `R-19` | foreign/vendor technology becomes unavailable, restricted, commercially unacceptable or non-replaceable | critical workflow/repository/runtime may stop or become strategically dependent on an inaccessible provider | ranges `Degrading` to `Company-critical` | sovereignty principle exists; replacement evidence varies | record origin/jurisdiction/license/data/telemetry/replacement implications for material dependencies; critical organizational authority/history/data must remain independently recoverable |
| `R-20` | customer-specific data/knowledge leaks across organizations or is reused without rights | confidentiality, contractual, legal, security and trust impact | `Company-critical` for material exposure | explicit constitutional/OS boundary exists | isolation, purpose limitation, rights review, minimum data, no automatic cross-customer learning and fail-closed handling where scope/rights are unclear |

## 5. Owner-unavailability continuity horizons

AC-104 explicitly asked what stops if the Owner is unavailable for one day, one week or materially longer. The horizons below are **scenario tests**, not promised recovery targets.

### 5.1 Approximately one business day

The Company should be able to tolerate short Owner unavailability by **pausing** rather than bypassing material authority gates.

Expected current effects:

- new material strategy/capital/risk/governance/commitment decisions wait;
- routine automated/technical work may continue only where scope and authority were already bounded;
- customer/support exceptions requiring interpretation may queue;
- Owner-held local/credential actions may queue;
- no executor may infer that urgency creates new authority.

The main short-horizon requirement is not substitute ownership. It is enough state visibility to know what is waiting, what is safe to continue and what must stop.

### 5.2 Approximately one week

A one-week absence can become materially disruptive under the current operating model because Owner context is concentrated across customers, portfolio priority, local gates and external commitments.

Without later controls, likely failure modes include:

- unresolved customer acceptance/rework decisions;
- project priority drift or work proceeding on stale assumptions;
- time-sensitive signing/payment/contractual actions waiting on one Principal or credential path;
- blocked local acceptance/release work;
- missing interpretation of product/client exceptions;
- inability to distinguish routine work from a decision that exceeds authority.

The minimum later design target is that existing bounded obligations can be reconstructed and escalated without recreating the Owner's memory from chats.

### 5.3 Materially longer absence

Extended absence exposes two different problems that must not be conflated:

1. **organizational continuity** — routine functions, product/customer state, data, repositories, credentials and workflows must be reconstructable and transferable; and
2. **legal/corporate continuity** — lawful participant/director/representation decisions may require corporate/legal mechanisms outside internal Company governance.

AC-105 does not invent those legal mechanisms. It records the current single-Principal concentration as material evidence for later Owner/authority and continuity design.

## 6. Canonical history and repository continuity

### 6.1 Company repository

GitHub is currently canonical and GitVerse is a mirror. This already reduces pure hosting lock-in, but a mirror is not proof of continuity until freshness and restore/reconciliation are tested.

Minimum future evidence should establish:

- at least one independent usable copy of critical history;
- known last synchronized commit;
- ability to reconstruct the canonical branch from a trusted copy;
- access recovery for maintainers/authorized Principals;
- explicit emergency decision if canonical hosting changes;
- read-after-write/reconciliation after recovery.

### 6.2 Product repositories

The portfolio currently contains multiple material product repositories with uneven roadmap/status/mirror maturity.

Company baseline rule:

- product repos remain canonical for implementation/product state;
- Company must know whether a product is recoverable, but must not solve repository loss by copying the product into Company docs;
- mirror/backup/restore coverage should be proportional to portfolio importance and customer obligation;
- stale roadmap/status pointers are continuity defects when they prevent state reconstruction, even if source code remains intact.

### 6.3 Chats and model memory

Chats and model memory may accelerate work but are not acceptable as the only copy of a material decision, obligation, workflow or recovery fact.

If a chat service, model provider or session disappears, the Company should lose convenience and transient context — not its only authoritative organizational history.

## 7. Credential, device and privileged-access baseline

AC-105 does not create a credential register because that register would be security-sensitive and belongs to AC-206 / approved restricted storage.

The continuity baseline is nevertheless explicit.

For every **material credential class**, later design must be able to answer:

- what capability the credential unlocks;
- whether it permits only technical access or also enables a legally/consequentially sensitive action;
- accountable owner/holder and authorized use scope;
- recovery/reset/reissue path;
- revocation/rotation path;
- dependency on a specific device/physical token/phone/account;
- what stops when it is unavailable;
- how evidence is preserved if it is compromised;
- whether another Principal can lawfully act, or whether the correct fallback is simply to pause.

Material classes may include repository administration, banking/payment, corporate/signing, EIS/ETP/procurement, domain/mail, infrastructure, customer systems and product external-effect integrations.

**Secret values, private keys, recovery codes and reusable tokens must not be committed to this public repository.**

## 8. Data, customer evidence and restore boundary

A business can remain technically online and still fail continuity if the state needed to finish an obligation exists only in one inaccessible place.

For a material customer/product workflow, later continuity design should identify:

1. authoritative source of customer inputs and contractual facts;
2. current accepted scope, exclusions and acceptance evidence;
3. governed/product state required to resume work;
4. source code/configuration versions required to reproduce the output;
5. location/classification of customer data;
6. backup/reconstruction requirement and restore test proportionate to consequence;
7. retention/deletion obligations and what must not be retained;
8. rights boundary for any reusable learning;
9. safe degraded mode if content is unavailable;
10. customer notification/escalation responsibility if a material loss/outage occurs.

A backup is not sufficient merely because bytes exist. The Company must be able to identify what the copy means, whether it is current enough for the intended use and whether it is lawful to restore/use.

## 9. External systems, suppliers and source authority

External dependencies fall into four operational patterns.

### 9.1 Authoritative systems

Examples include legal registries, bank/accounting systems, EIS/ETP and customer/supplier authoritative sources.

Rule:

- unavailability does not make a cached/local copy newly authoritative;
- uncertain freshness must be exposed;
- consequential work should pause or use an explicitly allowed degraded path rather than silently rely on stale facts.

### 9.2 Data/content sources that change behavior

Websites, APIs and integration endpoints can change HTML/schema/rate limits/authorization behavior.

For parser/integration products, source drift is an expected operational risk, not proof that the Company should hard-code a universal fallback.

Product repositories own source-specific detection, parser correction, tests and release evidence. Company owns the obligation/continuity question: whether a committed customer outcome can still be met and what escalation/change boundary applies.

### 9.3 Suppliers and contractors

Before a material external commitment depends on one supplier/contractor, the accountable product/deal workflow should know:

- substitution feasibility;
- lead time and customer-deadline effect;
- commercial/cash downside;
- data/security/IP implications;
- whether the correct fallback is substitute, rescope, delay or stop.

AC-105 does not assume dual sourcing where economics do not justify it.

### 9.4 Financial and administrative providers

Banking and outsourced accounting remain external professional/authoritative contours.

Continuity means preserving a usable interface and transition/recovery ability, not duplicating the bank ledger or accounting system inside Arvectum Company.

## 10. Arvectum OS and product-runtime continuity boundary

### 10.1 Arvectum OS is strategically material but not yet a universal operational single point

Current Company durable governance remains repository-first. Only explicitly admitted product/workflow slices depend on Arvectum OS contracts.

Therefore an OS outage must not be described as a Company-wide outage by implication.

For an admitted product slice:

- the applicable Product Contract and OS capability lifecycle control what reliance is real;
- missing/incompatible contract evidence must fail closed;
- product-local/manual fallback may be used only where the applicable product boundary permits it;
- a fallback run must not be represented as OS-governed completion when the governed path did not execute;
- Provisional/Incubating state must not be marketed as Stable/Active continuity commitment.

### 10.2 AI/software runtime continuity

The same principle applies below OS:

`Position/workflow meaning → governed knowledge/state → Assignment → replaceable runtime`.

No model, coding tool, orchestrator, database, cloud or local runtime should own the only copy of the organizational meaning needed to continue the function.

## 11. Stop / fail-closed conditions

A material operation should stop, pause or escalate rather than improvise when any of the following is true:

- required Organizational Authority or legal authority cannot be established;
- a material approval is missing or stale;
- Organization/customer scope is uncertain;
- customer data rights/classification/purpose are unclear;
- authoritative source or material version cannot be resolved reliably;
- a privileged credential appears compromised;
- canonical history may have diverged after outage/recovery;
- continuing would create an external commitment not already within approved bounds;
- a required product/OS contract or supported dependency is unavailable/incompatible;
- a material financial commitment lacks decision-relevant cash/obligation evidence;
- the only available “fallback” would bypass security, customer authority or legal/corporate controls.

Degraded mode is acceptable only when the workflow can state **what is degraded, what evidence is missing, what external effects remain prohibited and what condition permits normal operation to resume**.

## 12. Minimum continuity expectations by dependency class

| Dependency class | Minimum baseline expectation now | Detailed owner later |
|---|---|---|
| Owner / authority | reserved decisions remain explicit; routine work must eventually be separable; absence queues rather than creates implicit authority | AC-202 / AC-203 / AC-207 |
| legal/corporate representation | current concentration recorded; lawful continuity mechanism must be reviewed separately | competent corporate/legal authority + AC-202/207 evidence |
| credentials / privileged access | no secrets in repo; recovery/rotation/revocation and holder scope required for material classes | AC-206 |
| local devices / physical tokens | no critical data/history only on device; re-bootstrap/replacement path; deliberate signing controls preserved | AC-206 / AC-207 + product runbooks |
| Company/product repositories | independent recoverable history; mirror/restore/reconciliation evidence proportionate to criticality | AC-207 + product repos |
| customer/project state | scope/obligation/current state reconstructable in suitable authoritative source | AC-201–205 / AC-401–403 |
| customer data | authoritative location, access, backup/restore, retention/deletion and rights boundary | AC-206 / AC-207 + product/customer contract |
| external source/service | authority/freshness explicit; fail/uncertain/degraded behavior | product workflow / Product Contract where applicable |
| supplier/contractor | material dependency and substitution/downside known before commitment | product/deal workflow + AC-303 later |
| bank/accounting | external authority preserved; due obligations/exceptions reach management; transition/recovery path understood | AC-404 + professional providers |
| Arvectum OS | reliance only through admitted boundary; no hidden dependency; product-local fallback only when declared | OS/Product Contract + AC-207 for Company workflows |
| AI/runtime/vendor | replaceable execution; no authority/canonical history solely in runtime | AC-205/206/207 and workflow-specific design |

## 13. Material gaps carried forward

AC-105 finds no evidence that would justify declaring the Company “continuity-ready” today.

The largest current gaps are:

1. **Owner/corporate concentration** — one Principal currently concentrates residual Company authority, legal representation evidence and large amounts of operational context;
2. **credential/access map absent at Company level** — material credential classes, recovery holders and replacement paths are not yet canonically mapped;
3. **local-environment dependence** — several workstreams can stop at physical device/token/target-machine gates;
4. **customer obligation/context reconstruction** — current work can depend on Owner memory and project-specific conversations rather than one reconstructable operating state;
5. **portfolio restore coverage not yet evidenced uniformly** — Company GitVerse mirror exists as a pattern, but product-level mirror/restore coverage is not established by the Company baseline;
6. **customer/product data recovery not yet inventoried** — authoritative locations, backup/restore and retention/deletion evidence are product/runtime specific and not yet closed Company-wide;
7. **management exception visibility not yet operationalized** — due obligations, blocked work, incidents and pending decisions still require later registers/Mission Control;
8. **external dependency failure semantics remain uneven** — product repositories own detailed behavior, but Company-level obligation fallback is not yet standardized;
9. **no tested Company-wide recovery exercise** — this artifact defines expectations, not proof that a restore/credential/replacement scenario has been executed.

These gaps are not reasons to stop M1. They are explicit inputs to the Phase 2/4 roadmap rather than hidden assumptions.

## 14. Strategic and commercial risks that AC-105 does not close

Some material Company risks are real but belong to later work rather than continuity design.

### 14.1 Flagship market risk

The flagship `«ИИ-компания под ключ»` direction is approved, but ICP, buyer, job-to-be-done, measurable customer outcome, willingness to engage, pricing and repeatable support/implementation economics are not yet validated.

That is a material business risk, but it belongs to AC-107/AC-108/AC-106 rather than being disguised as an operational continuity defect.

### 14.2 Product/module investment risk

Repository existence does not prove module value, reuse economics or portfolio priority. Phase 3 owns investment/stop-continue/module classification.

### 14.3 Legal/compliance applicability

AC-105 does not claim compliance with a specific regulation or customer regime. Consequential legal/compliance claims require current official-source verification and the applicable legal/corporate path.

### 14.4 Quantitative availability or recovery promises

No Company-wide RTO, RPO, SLA, backup frequency or incident-response time is approved by this baseline. Those numbers must come from actual obligation, risk and operational evidence.

## 15. Prospective continuity evidence to capture

Future real work should capture lightweight evidence when material:

- dependency that blocked or degraded the work;
- whether it was a deliberate gate or accidental single point;
- obligation/customer/workstream affected;
- current canonical state/version available at failure;
- whether data/history remained reconstructable;
- time-to-detect and time-to-recover when useful;
- fallback used and whether it was tested beforehand;
- manual Owner intervention required;
- credential/device/provider involved as a class, without storing secrets;
- customer/external effect caused or prevented;
- whether the incident should change a workflow/runbook/policy after review;
- whether a replacement dependency reduces total risk/economic cost.

This evidence will support AC-207, AC-403 and later vendor/runtime decisions without requiring heavyweight enterprise continuity tooling now.

## 16. Implications for Phase 2

AC-105 constrains Phase 2 organizational design in five ways.

1. A Position must not be designed around one current executor's private memory, device or credentials.
2. Reserved Owner authority must remain explicit, while preparation/routine work should continue without using the Owner as an unnecessary scheduler.
3. Assignment/access design must include replacement/revocation/recovery and must not conflate technical access with authority.
4. Critical workflows need a degraded/manual/stop path before they are treated as dependable Company operations.
5. Continuity evidence must be proportional: a small current Company needs tested essentials, not ceremonial enterprise BCP documentation.

## 17. AC-105 completion boundary

AC-105 is complete when the Company can distinguish and explain:

- deliberate authority/security gates from accidental single points of failure;
- short Owner absence from extended corporate/organizational continuity risk;
- credential access from Organizational Authority;
- local-device dependence from justified physical/security control;
- canonical repository continuity from hosting-vendor authority;
- current Company governance dependence from product/OS runtime dependence;
- external authoritative-source failure from permission to invent local truth;
- customer/supplier/bank/accounting dependencies from Company-owned semantics;
- customer data restore needs from unsafe duplication;
- qualitative materiality from still-unknown likelihood/RTO/RPO;
- minimum fallback expectations from unimplemented runbooks or future Positions;
- operational continuity risk from still-unvalidated flagship market risk.

This publication satisfies that boundary without inventing delegated authority, legal instruments, credential holders, private infrastructure topology, customer-confidential obligations, recovery-time promises, alternate suppliers, future Positions or AI Assignments.

Cross-review result: `PASS at iteration 9 of maximum 10`.

Next roadmap action: `AC-107 — Flagship ICP, buyer, job-to-be-done and measurable outcome hypotheses`.
