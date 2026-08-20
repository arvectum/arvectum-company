# AC-207 — Critical-Function Continuity, Replacement and Manual Fallback Baseline

Status: `Proposed`
Version: `0.9.0`
Created: `2026-08-21`
Updated: `2026-08-21`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-207 — Critical-function continuity, replacement and manual fallback baseline`
Review: `docs/reviews/AC-207-CRITICAL-FUNCTION-CONTINUITY-CROSS-REVIEW.md`
Depends on: AC-105 material risk/dependency baseline; AC-202 Reserved Owner Decisions `1.0.0`; AC-203 Delegated Position Authority Model `1.0.0`; AC-204 Initial Position Registry `1.0.0`; AC-205 Initial Assignments `1.0.0`; AC-206 Company access boundary `1.0.0`
Approval required: explicit Owner approval before this baseline becomes binding Company continuity governance

## 1. Purpose

AC-207 defines the minimum current Company continuity semantics for the six approved Positions and the material dependencies that can interrupt their work.

The objective is not uninterrupted operation at any cost. The objective is:

> preserve legitimate authority, customer/data rights, security controls, organizational meaning and recoverable state while allowing already-bounded safe work to continue where evidence supports it.

The baseline therefore distinguishes:

```text
continuity ≠ bypass
replacement ≠ authority transfer
technical recovery ≠ business approval
mirror availability ≠ canonical promotion
manual fallback ≠ assumed human competence
```

A deliberate Owner, legal, customer, signing or security gate may legitimately stop an action. A continuity design is defective if it bypasses that gate merely to keep a workflow moving.

This artifact is a continuity **governance baseline**, not a claim of production-grade business continuity. It does not fabricate RTO/RPO/SLA values, tested disaster-recovery results, alternate legal representatives, powers of attorney, redundant providers or credentials that are not evidenced.

## 2. Canonical and platform re-check

Arvectum Company `main` was re-checked before drafting AC-207. Canonical roadmap `0.19.0` identifies AC-207 as the current action and AC-206 as `Complete / PASS`.

Arvectum OS `main` was re-checked at commit `d7c70355c0bd13148c493500990f83b522805831`.

No AC-207 rule depends on treating Arvectum OS as the source of Company authority. Where a Company/product workflow uses an admitted OS contract, OS governs the applicable platform semantics and execution evidence, while Company Positions, Assignments, Reserved Owner Decisions and business continuity meaning remain Company-owned.

Accepted OS security/identity principles remain compatible with this baseline: identity, technical authorization and Organizational Authority are distinct; least privilege and deny-by-default apply; governed state must remain attributable and portable; technical recovery must not silently broaden cross-organization access or authority.

## 3. Continuity model

### 3.1 Continuity modes

AC-207 uses five operating modes. These are not AC-203 authority modes.

| Mode | Meaning | Allowed behavior |
|---|---|---|
| `CM-0 — Normal` | assigned executor/runtime and required authoritative sources are available | operate inside the approved Position/Assignment/access envelope |
| `CM-1 — Bounded Continuity` | one executor/runtime/provider is unavailable, but an already-authorized replacement path can preserve scope and attribution | continue only the already-approved class of work; no authority expansion |
| `CM-2 — Degraded` | some safe work can continue, but consequential decisions/external effects cannot | preserve state, prepare evidence, perform reversible/internal work, queue blocked decisions |
| `CM-3 — Fail Closed` | authority, rights, trusted state, required credential or material dependency is absent/ambiguous | stop the affected action; do not infer permission or authority from urgency |
| `CM-4 — Recovery / Reconciliation` | dependency returns or replacement is introduced | verify trusted state, reconcile divergent work, re-establish least privilege and resume only inside the prior or newly approved envelope |

### 3.2 Continuity evidence states

The Company MUST distinguish a designed fallback from a proven fallback.

| Evidence state | Meaning |
|---|---|
| `CE-0 — Unresolved` | no sufficient fallback/replacement path is evidenced |
| `CE-1 — Defined / Untested` | a path is specified and plausible but has not been tested in the relevant Company context |
| `CE-2 — Operational Evidence Exists` | current artifacts/history/configuration demonstrate that the path has actually been used or restored at least in materially relevant scope |
| `CE-3 — Tested and Reviewed` | a deliberate recovery/replacement exercise has evidence and review proportionate to consequence |

AC-207 does not upgrade any dependency to `CE-2` or `CE-3` without actual evidence.

### 3.3 Replacement categories

Replacement types MUST remain distinguishable:

- **runtime replacement** — another model, agent runtime, process, workstation or build host performs the same bounded execution under an existing valid Principal/Assignment where identity semantics permit;
- **Principal replacement** — a different human/service/workload Principal takes over a Position Assignment; this requires an explicit Assignment/access change rather than automatic inheritance;
- **external-provider replacement** — another accountant, hosting provider, bank, external source or supplier is engaged through the applicable legal/commercial/access path;
- **device replacement** — work moves to another machine/environment without broadening data/credential access;
- **legal/corporate authority replacement or succession** — a distinct legal/corporate matter requiring valid law/charter/corporate instruments; AC-207 does not create it.

A runtime swap may be routine. A new Principal, provider or legal representative is not.

## 4. Minimum continuity packet

A material active workstream SHOULD be reconstructable without relying on one person's memory or one AI session.

The minimum continuity packet, proportionate to the workstream, is:

1. workstream/customer/product identifier and accountable Position;
2. current approved scope, exclusions and current objective;
3. last authoritative decision/approval reference and the capacity in which it was made;
4. current status and next safe action;
5. open material commitments, obligations, due events and acceptance/validation state;
6. relevant canonical repository/source/version/commit references;
7. customer/data-rights and classification constraints;
8. required resource/access classes and restricted secret-location references without secret values;
9. current unresolved risks/exceptions and escalation destination;
10. rollback/recovery/reconciliation notes where relevant;
11. explicit stop conditions;
12. pending decisions that no replacement executor may infer.

The packet MAY be distributed across canonical systems if one index/pointer makes the state reconstructable. AC-207 does not require raw customer/financial/secret material to be copied into the public Company repository.

## 5. Position continuity baseline

### 5.1 `POS-001 — Company Executive`

Current realization: Owner human Position holder + AI advisory/preparation.

#### AI adviser/runtime unavailable

Mode: normally `CM-2 — Degraded` rather than Company stop.

The human Position holder can continue routine Company coordination, direct proposals, approvals in the applicable capacity and repository/state maintenance manually. AI-specific analysis/cross-review throughput is lost, but authority does not change.

Minimum fallback:

- current roadmap, decisions, Position/Assignment/access baselines and workstream pointers must remain reconstructable without the AI provider/session;
- no organizational meaning may exist only in a model's hidden state or chat context;
- AI output that has not been promoted through the applicable review/decision path is not continuity-critical authority.

Current evidence state: `CE-1 — Defined / Untested` for AI-provider replacement at Company level.

#### Owner human Position holder unavailable

Short absence enters `CM-2`/`CM-3` by work class.

AI may continue only the work already admitted to its Assignment, principally evidence preparation and bounded state/publication mechanics tied to an existing valid decision. The AI does not inherit POS-001 human `AM-2`, Owner `ROD-*`, participant competence or General Director power.

New cross-Position judgment, material prioritization, governance change and Owner/legal decisions stop until a valid human authority path exists.

Current evidence state: `CE-0 — Unresolved` for replacement human POS-001 Assignment and for extended Owner/legal-authority absence.

### 5.2 `POS-002 — Commercial & Customer Lead`

Current realization: Owner accountable human + AI commercial support + accounting interface; future human sellers are only conditional capacity.

#### AI search/outreach unavailable

Mode: `CM-2 — Degraded`.

The human Position holder can research, communicate and follow up manually using authorized Company channels. Prospecting throughput falls; customer/commercial authority does not change.

A future replacement AI/runtime may resume only if campaign state, target rules, sending identity, suppression/opt-out state and current message/follow-up boundary are reconstructable.

#### Owner human Position holder unavailable

Current Company state is materially constrained.

A pre-approved, already-provisioned outreach automation MAY continue only inside its exact existing campaign/message/recipient/frequency/follow-up envelope. AC-207 does not claim that such an operational sender currently exists.

The following MUST stop or queue absent another valid human Assignment/authority path:

- material or non-standard customer commitments;
- new prices/discounts/SLA/warranty/scope/legal/data promises;
- ambiguous qualification or acceptance decisions requiring human judgment;
- scope expansion or defect-vs-change disputes outside already-approved criteria;
- customer exceptions whose authority basis is unclear.

Future live sellers do not become active because the Owner is absent. They require actual engagement, explicit Assignment and access provisioning.

Current evidence state: `CE-0` for Owner-independent commercial continuity; `CE-1` for the future bounded seller/AI handoff design.

#### Customer system/data unavailable

Use `CM-2` only if a lawful, sufficiently fresh local/recoverable copy can support the narrow task. Otherwise use `CM-3` and mark the workstream blocked rather than reconstructing customer truth from memory or another customer's data.

### 5.3 `POS-003 — Portfolio & Product Lead`

Current realization: Owner human judgment + AI synthesis/advice.

#### AI unavailable

Mode: `CM-2 — Degraded`; Owner can continue portfolio judgment manually from Company/product canonical sources.

#### Owner unavailable

AI may continue evidence collection, cross-repository status synthesis and preparation only. It MUST NOT independently start/stop products, change material portfolio priority, allocate material capital, or redefine Company↔Product↔OS boundaries.

Routine portfolio decisions requiring the human Position holder stop unless a different Principal has been explicitly assigned and provisioned.

Current evidence state: `CE-0` for Owner-independent portfolio judgment; `CE-1` for AI-runtime replacement.

### 5.4 `POS-004 — Engineering & Release Lead`

Current realization: AI-led for admitted bounded technical work.

This Position has the strongest intended runtime-replacement requirement because the Position must survive a specific model, coding agent or vendor.

#### AI model/agent/runtime unavailable

Preferred path: `CM-1 — Bounded Continuity` by replacing the runtime while preserving the workstream's governed identity/Assignment semantics where valid.

Replacement requires reconstructable:

- repository/worktree and exact current commit/branch state;
- task/scope and accepted technical constraints;
- tests/validation expectations;
- known defects/limitations;
- dependency/toolchain state needed to reproduce the work;
- access through a valid workload/service identity or a newly approved one;
- no reliance on hidden model memory as the only source of engineering state.

If the replacement introduces a different Principal rather than merely a different runtime behind the same governed workload identity, an explicit Assignment/access change is required before execution.

If no valid replacement exists, the Position enters `CM-2` for deterministic CI/read-only evidence where already available or `CM-3` for new engineering execution.

#### Manual human fallback

Manual fallback is **not assumed** merely because a human exists.

A human may take over POS-004 only through an explicit temporary or permanent Assignment and corresponding least-privilege access. The Company must not infer engineering competence or authority from Owner status, repository ownership or emergency.

#### CI/build environment unavailable

Local or alternate build/test execution may be used only if product scope, dependencies and verification semantics remain equivalent enough for the claimed result. If they do not, the result must be labeled degraded/partial rather than presented as release-ready.

#### Production/deploy/signing boundary

Engineering continuity does not authorize consequential production deployment or signing outside an already-approved execution class. Missing production credential, signing token or release authority is a legitimate `CM-3` gate.

Current evidence state: `CE-1` for runtime replacement as Company semantics; actual per-product runtime/rebuild/release evidence varies and remains product-owned.

### 5.5 `POS-005 — Finance & Obligation Control Lead`

Current realization: Owner human management-finance judgment + outsourced accounting/tax interface.

#### Accounting provider unavailable

Mode: `CM-2 — Degraded` initially.

The Company should retain enough access to source documents, management obligation state and bank/accounting evidence to know what is due or unknown without pretending to perform professional/statutory accounting from this repository.

Until the provider or a valid replacement is available:

- current statutory/accounting truth that cannot be independently verified is marked unavailable/uncertain;
- material deadlines and unknown obligations escalate;
- the Company does not fabricate balances, tax positions or filing completion;
- a new accounting provider requires an actual service/legal/access transition.

Current evidence state: `CE-1` for source-document/provider replacement expectation; replacement has not been tested Company-wide.

#### Owner human Position holder unavailable

The accounting provider may continue work already validly delegated/contracted inside its professional contour. It does not inherit POS-005 management judgment, Company spending authority or Owner `ROD-*` authority.

New material commitments, capital decisions and ambiguous management-finance decisions pause absent another valid human Position/Owner path.

#### Bank/payment unavailable

A bank outage or unavailable authorized signer may legitimately block payment. AC-207 does not invent an alternative bank or payment route. Known due obligations remain visible and escalated; payment resumes only through a valid financial/legal path.

### 5.6 `POS-006 — Security, Risk & Continuity Lead`

Current realization: Owner human judgment + AI analysis/advice.

#### AI unavailable

Mode: `CM-2 — Degraded`; the human Position holder can perform security/risk/continuity judgment manually from available evidence.

#### Owner human Position holder unavailable

AI may continue analysis, evidence checks and decision preparation inside its current Assignment. It does not inherit material risk acceptance, data-sovereignty exception, critical dependency exception, security administration or Owner `ROD-*` authority.

Existing product/system security controls and separately authorized deterministic protections may continue in their own approved scopes. AC-207 does not create new automatic containment authority.

Material risk acceptance, control weakening, cross-customer/data-purpose exception and unresolved resumption decisions stop.

Current evidence state: `CE-0` for Owner-independent Company security/risk decision continuity; `CE-1` for AI-advisory runtime replacement.

## 6. Cross-cutting dependency continuity

### 6.1 GitHub canonical remote unavailable

GitHub remains the canonical Company remote under the current approved repository model.

If GitHub is temporarily unavailable:

- local clones and GitVerse MAY preserve work/history and support bounded local/internal work where access and state are trustworthy;
- GitVerse does **not** become canonically authoritative automatically;
- Company governance publication that requires the canonical remote may pause;
- divergent local/mirror commits must retain source commit/provenance for later reconciliation.

A temporary or permanent canonical promotion of another remote requires the applicable explicit Company decision. If the required authority is unavailable, the correct behavior is degraded operation, not silent promotion.

Recovery enters `CM-4`: verify the authoritative pre-outage head, inspect divergent history, reconcile explicitly, then resume normal publication.

Current evidence state: `CE-1` — mirror/local fallback exists conceptually and operational copies exist, but Company-wide restore/reconciliation has not been proven by AC-207 evidence.

### 6.2 Product repository unavailable or stale

The Company MUST NOT recreate product implementation truth in the Company repo as a continuity shortcut.

Use trusted local/mirror copies only with explicit provenance and later reconciliation. If the product source cannot be reconstructed with sufficient confidence, product engineering/release claims stop.

### 6.3 Arvectum OS unavailable/incompatible

Current Company governance remains repository-first and does not become invalid because OS is unavailable.

Only workflows/products that actually rely on an admitted OS contract are affected. Their fallback must follow the applicable Product Contract/product evidence. Product-local/manual fallback must not be described as OS-governed execution if OS governance/evidence was not actually used.

### 6.4 AI/model/provider unavailable

No Company authority, Position meaning, customer scope or canonical history may live only inside one model/provider account.

Hybrid Positions degrade to human execution where the current human Assignment can perform the work. AI-led POS-004 follows the explicit runtime/Principal replacement rules above.

The Company MUST preserve prompts/workflow specifications only to the extent they are durable organizational assets; model hidden state is not a continuity source.

### 6.5 Local workstation / VM unavailable

A replacement device is valid only if work/data/credentials can be re-established from controlled sources without copying unrestricted personal or Company secrets into the new environment.

Required path:

1. establish trusted device/environment;
2. obtain only the access required for the Assignment;
3. restore/re-clone code/data from authoritative or provenance-preserving sources;
4. rehydrate secrets through the approved restricted mechanism;
5. run proportionate verification;
6. resume only the previously authorized work class.

If a critical toolchain or signing device cannot be reproduced safely, that action stops.

Current evidence state: `CE-1` for general re-bootstrap expectation; actual per-device recovery is not Company-wide tested.

### 6.6 Credential loss or compromise

A lost/compromised credential is a security event, not a reason to broaden access.

Minimum behavior:

- affected external effects stop where appropriate;
- revoke/rotate/recover through the authoritative provider/control path;
- preserve event evidence without storing the secret itself;
- verify whether canonical state or customer data may have been altered;
- issue replacement access only inside AC-206 least-privilege ceilings;
- reconcile automation/workload identity before resumption.

If recovery material itself is unavailable, the applicable provider/account recovery path controls. AC-207 does not invent a bypass.

Current evidence state: `CE-0/CE-1` depending on resource; the complete current credential inventory and tested rotation/recovery remain outstanding.

### 6.7 Electronic signature / physical signing token unavailable

A signing mechanism is a deliberate technical/legal gate.

If the qualified signature, token, PIN/recovery path or legally authorized signer is unavailable, the affected signing action stops. AI, repository admin status or possession of an unsigned document does not create signature authority.

A replacement certificate/token, different signer or power to act requires the valid external/legal/corporate process. AC-207 creates none.

Current evidence state: `CE-0` for alternate lawful signing continuity unless separately evidenced outside this repository.

### 6.8 Bank/payment service unavailable

Known obligations remain recorded/escalated, but the Company does not route money through an unapproved substitute merely to preserve continuity.

If an already-established lawful alternate bank/payment route exists, it may be used only under its existing financial/legal authority. AC-207 does not assert that such a route currently exists.

Current evidence state: `CE-0` for generic alternate-bank continuity.

### 6.9 Outsourced accounting unavailable

Preserve source documents, decision-relevant obligation state and access/recovery metadata so another provider can be onboarded without reconstructing the Company solely from the former provider's private working state.

Replacement provider onboarding must preserve statutory/accounting source authority and does not make the Company repo the accounting system of record.

### 6.10 Customer input / acceptance unavailable

Mark the workstream explicitly blocked by customer input/validation. Internal engineering may continue only where the accepted scope and risk allow it.

The Company MUST NOT infer customer acceptance from silence, prior conversations or technical completion.

### 6.11 Customer data / rights continuity

Backup/recovery does not broaden purpose or audience.

A recovery copy remains subject to the same organization/customer isolation, classification, retention/deletion and purpose limitations as the original. A replacement runtime/provider must not receive cross-customer data merely because that would simplify restoration.

If the right to restore/use a copy is unclear, fail closed and obtain the proper authority/rights evidence.

## 7. Owner and legal-authority unavailability scenarios

### 7.1 Short absence

The Company SHOULD tolerate a short Owner absence by allowing already-bounded technical/internal work to continue and queuing decisions that genuinely require the Owner/human Position holder.

Expected safe behavior:

- POS-004 bounded engineering may continue while scope/access/risk remain clear;
- already-approved deterministic CI/build/test may continue;
- AI components of POS-001/002/003/006 may prepare evidence and perform only their already-admitted bounded mechanics;
- no executor infers `ROD-*`, legal-signing, bank-payment, customer-acceptance or privileged-access expansion authority;
- blocked items remain explicitly visible.

### 7.2 Approximately one week / operationally material absence

At current AC-205 Assignments, this becomes a material Company continuity gap because one human Principal occupies POS-001, POS-002, POS-003, POS-005 and POS-006.

The Company can preserve engineering throughput and evidence preparation more readily than it can preserve human commercial, portfolio, finance, security/risk and Company-integration judgment.

Therefore current target behavior is safe degraded operation rather than pretending full continuity:

- existing bounded engineering/workflow execution may continue;
- new material commitments, portfolio changes, risk acceptance, capital decisions and ambiguous customer matters pause;
- accounting may continue in its external contracted contour;
- state/evidence must remain reconstructable for the Owner or a later properly assigned Principal.

### 7.3 Extended Owner absence

Extended absence exposes two separate gaps:

1. **Position continuity gap** — several human-held Company Positions currently have no replacement human Principal;
2. **Owner/legal/corporate authority continuity gap** — Reserved Owner Decisions and legal representation require valid authority that AI/software cannot inherit.

AC-207 does not resolve the second gap by internal policy. A future legal/corporate continuity review may identify lawful corporate succession/representation instruments, but until such evidence exists the Company must treat extended Owner/legal-authority unavailability as a Company-critical unresolved dependency.

## 8. Recovery and reconciliation procedure

When a material dependency returns or a replacement is introduced, the minimum `CM-4` sequence is:

1. **identify scope** — which Position/workstream/resources were affected;
2. **identify authority** — who is entitled to authorize recovery/resumption and in what capacity;
3. **contain ambiguity** — pause consequential external effects while trusted state is uncertain;
4. **establish trusted source** — identify the canonical or provenance-preserving pre-failure state;
5. **restore execution environment** — least-privilege identity/access, tools, data and secret injection;
6. **compare state** — inspect divergent commits, pending messages, transactions, customer changes, automation effects and incident evidence;
7. **reconcile explicitly** — accept/reject/merge divergent work with attributable decision/evidence;
8. **verify controls** — customer scope, data rights, security, tests and acceptance gates remain valid;
9. **resume bounded work** — no wider scope than before unless a separate valid approval changes it;
10. **record learning** — promote validated improvements through Company/Product/OS governance as applicable.

Recovery success is technical evidence, not automatic proof of business/customer/legal readiness.

## 9. Current continuity evidence and unresolved gaps

AC-207 records the following current state without inflating readiness:

| Area | Current evidence assessment | Status |
|---|---|---|
| Company Position meanings/history in Git | durable repository artifacts exist | `CE-2` for existence/history, not restore test |
| GitHub canonical + GitVerse/local resilience copies | mirror/local-copy path exists | `CE-1` for controlled outage/reconciliation |
| hybrid Position operation without a specific AI adviser | human Position holder exists | `CE-1`; deliberate provider-switch test not evidenced |
| POS-004 AI runtime replaceability | executor-neutral model and repo-based engineering state defined | `CE-1`; per-product/runtime failover varies |
| replacement human POS-001/002/003/005/006 | no active alternate human Assignment evidenced | `CE-0` |
| future human seller handoff | scoped future Assignment model exists | `CE-1`; no live seller handoff evidenced |
| customer/commercial context reconstruction | requirement exists; completeness across live workstreams not proven | `CE-0/CE-1` |
| outsourced accounting replacement | external contour and source-document requirement defined | `CE-1`; transition not tested |
| bank alternate/payment continuity | no generic alternate evidenced | `CE-0` |
| legal/corporate representation continuity | no alternate lawful path evidenced in current Company baseline | `CE-0` |
| electronic-signature/physical-token continuity | deliberate gate identified | `CE-0` for alternate signing path |
| credential inventory/rotation/recovery | AC-206 model exists, complete live inventory/test not evidenced | `CE-0/CE-1` |
| local workstation/VM replacement | re-bootstrap expectation exists | `CE-1`; Company-wide exercise not evidenced |
| customer-data backup/recovery/expiry | product/workstream-specific and not inventoried Company-wide | `CE-0/CE-1` |
| security incident containment with Owner unavailable | no new automatic Company-level authority exists | `CE-0` for independent human/security decision continuity |

The Company MUST NOT describe itself as fully continuity-ready, disaster-recovery-tested or Owner-independent based on this baseline.

## 10. Required downstream implementation evidence

AC-207 identifies evidence to be produced later without making it a condition for the semantic baseline itself:

- restricted live credential/access inventory and recovery-owner mapping;
- freshness/restore/reconciliation exercise for Company canonical repository and mirror/local history;
- at least one POS-004 runtime-replacement exercise on a bounded real engineering workstream;
- re-bootstrap evidence for a material local engineering environment;
- customer/workstream continuity packet for a real active engagement before material scale;
- accounting-provider transition pack/source-document inventory sufficient for provider replacement;
- dedicated commercial sender/CRM state and handoff evidence before relying on autonomous outreach continuity;
- explicit legal/corporate review of extended Owner/authorized-representative absence if the business exposure justifies it;
- signing-token/certificate recovery/replacement procedure evidence where time-sensitive signed obligations exist;
- customer data backup/restore/retention/expiry evidence in each product/workstream where such data is material;
- review of any actual incident/recovery to update this baseline through evidence rather than assumption.

These are implementation/evidence tasks. They do not grant authority or justify secret disclosure.

## 11. Continuity review triggers

Review this baseline when:

- a Position changes Principal or executor class;
- a critical workflow becomes dependent on a new vendor/model/runtime/customer system;
- a new material credential/signing/banking dependency appears;
- a real outage, compromise, recovery or handoff contradicts the defined path;
- a customer obligation introduces stricter continuity/data requirements;
- a product becomes independently revenue/material enough that product continuity dominates Company generic rules;
- legal/corporate representation changes;
- GitHub/GitVerse/canonical remote policy changes;
- AC-206 access ceilings materially change;
- Company scale makes current Owner concentration an unacceptable operating risk.

## 12. Boundary with AC-208

AC-207 defines Arvectum Company's own continuity and replacement baseline.

AC-208 must decide which parts are reusable as a **method** for customer-specific AI-native organizations and which are specific to Arvectum Company's current Owner concentration, repositories, accounting provider, signing/banking arrangements, Russian-first operating environment and product portfolio.

The customer transfer pattern is not a fixed Arvectum Company fallback matrix. It is the derivation method:

```text
business-critical function
→ Position / authority
→ current executor
→ access/data dependencies
→ failure consequence
→ continue / degrade / stop boundary
→ replacement path
→ evidence / recovery / reconciliation
```

## 13. Completion and approval boundary

AC-207 is substantively complete when the Company can explain, without fabricated evidence:

- what each Position does if its current human/AI/provider/runtime becomes unavailable;
- which work may continue, degrade or must fail closed;
- how AI-led Engineering can replace a model/runtime without turning the model into the Position;
- why a human/manual fallback requires a real Assignment rather than Owner status;
- how GitHub/GitVerse/local copies preserve history without silent canonical promotion;
- how credentials, signing, bank, local-device and customer-data recovery preserve least privilege and rights;
- what outsourced accounting may continue without becoming Company authority;
- what short and extended Owner absence does to the current Company;
- which continuity paths are actual evidence, merely defined/untested or unresolved;
- how recovery reconciliation preserves authority, provenance and customer/security boundaries.

This `0.9.0` publication is a **proposal only**.

Approval materially establishes Company continuity/fail-closed expectations and therefore requires explicit Owner approval before it becomes binding Company governance.