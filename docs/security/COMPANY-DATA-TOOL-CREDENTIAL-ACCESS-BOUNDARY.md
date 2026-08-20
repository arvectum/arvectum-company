# AC-206 — Company Data / Tool / Credential Access Boundary Baseline

Status: `Proposed`
Version: `0.9.0`
Created: `2026-08-20`
Updated: `2026-08-20`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-206 — Company data/tool/credential access boundary baseline`
Review: `docs/reviews/AC-206-COMPANY-ACCESS-BOUNDARY-CROSS-REVIEW.md`
Depends on: AC-202 Reserved Owner Decisions `1.0.0`; AC-203 Delegated Position Authority Model `1.0.0`; AC-204 Initial Position Registry `1.0.0`; AC-205 Initial Assignments `1.0.0`; AC-105 material dependency baseline
Approval required: explicit Owner approval before this baseline becomes binding Company access governance

## 1. Purpose

AC-206 defines the **Company-level access eligibility and least-privilege boundary** required by the six approved Positions and their AC-205 executor realizations.

It answers a narrower question than AC-203/AC-205:

> What data, repositories, accounts, tools, local environments and privileged capabilities may each current human, AI/software or external-service executor legitimately need in order to perform its approved Assignment — and what must remain outside that executor's technical reach?

The governing chain remains:

```text
Position authority envelope
∩ Assignment scope
∩ technical authorization/access
∩ current workflow/data/risk conditions
= maximum executable action
```

AC-206 governs the **technical-authorization/access term only**. It does not enlarge Position authority, create customer consent, create legal power, approve expenditure, activate `AM-3` or `AM-4`, or make possession of a credential evidence that an action is organizationally authorized.

This artifact is intentionally safe for a public repository. It defines classes, boundaries and required metadata. It MUST NOT contain reusable secrets, private keys, passwords, recovery codes, token values, bank details, signature/PIN material, non-public customer payloads or other sensitive operational values.

## 2. Canonical and architecture re-check

Arvectum Company `main` was re-checked before drafting AC-206 at commit `7c47d4f40e08e0ac1dfd896ed8d8f01911261ada`, where AC-205 is Approved and the canonical roadmap is `0.18.0` with AC-206 Current.

Arvectum OS `main` was re-checked at commit `608a796be255f2b2d350f75fb2a72af411cb615d`. The Company-relevant security baseline remains compatible:

- OS Constitution `1.2.0` remains Ratified;
- RFC-0003 `Identity, Security, Privacy, Tenant Sovereignty and Portability` remains Accepted `1.0.0`;
- RFC-0003 requires semantic separation of identity, authentication, authorization, Organizational Authority and data governance;
- authorization is deny-by-default and least privilege;
- possession of an identity, technical account or credential does not itself grant authority;
- reusable secrets must not be logged, placed in ordinary canonical records or exposed to model prompts merely for convenience;
- cross-organization access requires an explicit governed basis.

AC-206 does not create a new Arvectum OS dependency. Where a future Company workflow uses OS identity/access contracts, Company-specific Position/Assignment meaning remains owned here and must be mapped into the applicable OS contract rather than copied into platform-global semantics.

## 3. Access modeling rules

### 3.1 Access is not authority

The following are separate facts and MUST remain separately reconstructable:

```text
who/what the Principal is
≠ what Position the Principal is assigned to
≠ what the Position may decide
≠ what resource the Principal can technically access
≠ what the Principal is legally/corporately entitled to sign or represent
≠ what customer/data rights permit
```

A repository admin role, email password, API token, bank login, local root account, CI secret, signing token, DNS credential or customer-system account MUST NOT be interpreted as Company Organizational Authority.

### 3.2 Deny by default

If an access need is not required by the approved Assignment or a separately approved workflow, the default is **no access**.

Convenience, model capability, historical habit, prior access, shared-account availability or the fact that the Owner personally can reach a resource are not sufficient reasons to grant that access to another Principal or AI executor.

### 3.3 Least privilege is multi-dimensional

Least privilege is evaluated across:

- resource scope;
- operation scope;
- organization/customer scope;
- data classification;
- environment (development/test/production);
- duration;
- external-effect capability;
- administrative capability;
- secret/key exposure;
- ability to change access for others.

A Principal that needs repository content write does not automatically need repository administration. A workflow that needs a secret at execution time does not automatically need the secret value exposed to the AI/model/operator.

### 3.4 Access eligibility ceiling is not provisioning

This document defines the **maximum justified access class** for the current Assignment model.

Approval of AC-206 does not itself create an account, issue a token, add a repository collaborator, grant bank access, authorize a sender mailbox, expose customer data or install a secret on a machine.

Actual provisioning must still have attributable evidence that:

1. the Principal/Assignment exists and is current;
2. the requested resource is inside the approved access ceiling;
3. the required authority/customer/data basis exists;
4. the technical grant is minimum necessary;
5. privileged/restricted grants have an explicit human authorization path where required;
6. revocation/recovery ownership is known.

## 4. Data classes

AC-206 introduces four **Company access-governance classes**. They are internal control labels, not statutory legal classifications and do not replace product/customer/legal classification schemes.

| Class | Meaning | Typical examples | Default AI handling |
|---|---|---|---|
| `DC-0 — Public` | intended or already approved for public disclosure | public Company governance, public product repositories, public websites, approved public marketing content | allowed within approved task/tool scope |
| `DC-1 — Internal` | non-public operational information whose disclosure would be undesirable but not normally catastrophic | internal work queues, non-sensitive prospect lists, internal status, non-public drafts without customer secrets | only in approved Company/workstream tools; minimize and avoid unnecessary persistence |
| `DC-2 — Confidential` | customer/commercial/financial/security information requiring restricted purpose and audience | customer/project data, non-public proposals/contracts/pricing, detailed management finance, supplier terms, sensitive security evidence | only when explicitly needed, purpose-bounded and the runtime/tool is approved for that class; otherwise sanitize/minimize |
| `DC-3 — Restricted` | credentials, cryptographic/signing material, recovery secrets or highly sensitive payloads where disclosure can directly enable unauthorized action or material harm | passwords, API tokens, private keys, recovery codes, e-signature PIN/key material, bank signing/authentication secrets, master admin/recovery secrets | MUST NOT be placed in model prompts or ordinary AI context; use controlled secret injection/external mechanism if a future workflow legitimately requires machine use |

Personal, customer, contractual or security data may require stricter handling than the table's examples depending on the actual source and obligation. Uncertainty defaults to the more restrictive treatment until classified.

## 5. Technical capability markers

Access records and matrices use the following orthogonal markers:

- `R` — read/observe data or state;
- `W` — create/update ordinary content or non-privileged state;
- `X` — execute an approved technical operation;
- `P` — privileged administration, security/IAM/settings changes or ability to grant access to others;
- `K` — access to reusable secret/key material itself;
- `E` — capability to cause an external effect (send, publish, deploy, pay, sign, submit, delete externally, etc.).

These markers are **not authority modes**. They describe technical capability only.

`P`, `K` and consequential `E` are high-sensitivity capabilities and require stronger justification and attributable human authorization. A Principal may hold `X` or `E` only for an already bounded class of operations; technical capability never erases AC-202/AC-203 approval gates.

## 6. Resource classes

AC-206 recognizes the following Company-level resource classes. Product-specific systems may refine them locally without changing this Company boundary.

| ID | Resource class | Canonical/authority note |
|---|---|---|
| `RA-01` | Company canonical governance repository (`arvectum/arvectum-company`) | GitHub is canonical remote for repository-suitable Company state; GitVerse is mirror only |
| `RA-02` | Product source repositories | product repositories are canonical for product implementation/domain state |
| `RA-03` | Git mirrors / backup repository hosts | resilience copy; mirror possession does not change canonical authority |
| `RA-04` | Private customer/workstream data and documents | customer/project/private store or applicable system of record; never public Company repo by default |
| `RA-05` | Public web / market / supplier / prospect research sources | external source remains authority for its facts |
| `RA-06` | Company email and controlled outreach sending identities | communication channel; sending ability does not create commitment authority |
| `RA-07` | CRM / prospect / commercial work register | current/future operational store for contact, qualification and follow-up state; access purpose-limited |
| `RA-08` | Accounting/tax systems, reports and source-document interface | external accounting/statutory contour remains authoritative within its scope |
| `RA-09` | Bank/payment systems | external financial system; payment capability remains separately controlled |
| `RA-10` | Corporate/legal signing and qualified electronic-signature mechanisms | legal/technical capability only; must remain tied to valid legal/corporate authority |
| `RA-11` | Procurement/EIS/ETP or similar regulated/external transaction systems | workstream-specific; external authority and credential rules remain controlling |
| `RA-12` | Local engineering environments, workstations, VMs and test hosts | execution environment; no ambient access to unrelated personal/Company data |
| `RA-13` | CI/CD, build runners, artifact stores and release tooling | product/workstream execution; secrets should be injected without exposing values to AI where possible |
| `RA-14` | Hosting, domain/DNS, infrastructure and service-admin consoles | privileged operational infrastructure; scope only where Company/workstream need is established |
| `RA-15` | Credential/secret/recovery management | secret values remain outside public repo and ordinary AI context |
| `RA-16` | Security/incident/monitoring evidence and controls | may include `DC-2`/`DC-3`; access should be need-to-know |
| `RA-17` | Arvectum OS governed runtime/state where an admitted contract exists | OS access is contract/scope-specific; no ambient Company-wide OS admin right |
| `RA-18` | AI/model/agent runtimes and orchestration tools | replaceable execution mechanism; model/provider identity is not Position authority |

## 7. Assignment-class access baseline

### 7.1 Current Owner human Principal — general rule

The current Owner human Principal holds human Assignments for `POS-001`, `POS-002`, `POS-003`, `POS-005` and `POS-006` and may separately act in Owner, participant or General Director capacities.

Because the same human currently has several technical capabilities, AC-206 does **not** attempt to create artificial separate user accounts for every Position immediately. It requires that material actions remain attributable by **capacity/context** even when one account is used operationally.

For high-consequence actions, the durable record should distinguish whether the human acted as:

- a Position holder inside delegated scope;
- Owner under AC-202;
- participant/general-meeting authority;
- General Director / legally authorized representative;
- credential/system administrator performing technical mechanics after a valid decision.

The fact that the human can technically perform all of these does not merge their authority sources.

### 7.2 `POS-001 — Company Executive` access

#### Human Assignment

Required/eligible access:

- `RA-01`: `R/W`, with publication/branch/content mechanics required to maintain approved Company governance/state;
- `RA-02`: primarily `R` across relevant product repositories for Company-state reconstruction and decision preparation; product write remains product-scope-specific rather than implied by POS-001;
- `RA-03`: `R` and bounded synchronization/recovery mechanics where already approved;
- current Company planning/evidence sources needed to reconstruct Company state;
- decision-ready summaries from `RA-08`, `RA-16` and other Positions rather than unrestricted raw access where summaries suffice.

No POS-001-specific need is established for bank payment execution, legal signing keys or customer-system administrator rights merely because Company Executive integrates work.

#### AI advisory/execution component

Initial access ceiling:

- `RA-01`: `R` to public Company content; bounded `W` for proposals, reviews, roadmap/state synchronization and publication mechanics only when explicitly tasked and when the relevant decision already exists;
- `RA-02`: `R` to repositories/material needed for Company status/evidence; no default product code write through POS-001;
- `RA-05`: `R` for research when relevant;
- `RA-18`: runtime/tool access necessary to perform analysis and approved repository work.

Explicitly excluded by default:

- `P` repository/org administration;
- `K` access to reusable secrets;
- bank/payment/signing credentials;
- broad customer-confidential stores;
- owner personal/general mailbox;
- unrestricted infrastructure or security administration.

AI repository write is technical execution, not approval. The AI MUST NOT convert a favorable review, generated text or successful commit into a Company decision.

### 7.3 `POS-002 — Commercial & Customer Lead` access

#### Current Owner human Assignment

Eligible access:

- `RA-04`: scoped customer/workstream data needed for active discovery/delivery/acceptance;
- `RA-05`: `R` public research;
- `RA-06`: Company customer/commercial communication identities;
- `RA-07`: commercial/prospect/customer-workflow state when such a system/register exists;
- `RA-08`: decision-relevant invoice/payment/accounting facts through the accounting interface, not unrestricted statutory system administration by Position implication;
- selected `RA-02`/product evidence needed to communicate scope/readiness, normally `R` unless the same person separately acts under another Position.

Customer-confidential access is engagement/purpose scoped. One customer's access does not imply another customer's data access.

#### AI commercial search/outreach component

Initial access ceiling:

- `RA-05`: `R` public web/source research;
- `RA-07`: `R/W` to the scoped prospect/campaign register when implemented;
- `RA-06`: dedicated/scoped commercial sending identity with `E` only for an explicitly approved campaign/message class;
- dedicated reply/inbox scope where needed for classification and follow-up, rather than the Owner's unrestricted mailbox;
- `RA-18`: AI/runtime execution.

AI commercial access MUST be bounded by:

- declared campaign/workstream;
- target criteria;
- data purpose;
- recipient suppression/opt-out state where applicable;
- approved message class/template boundary;
- frequency/rate boundary;
- permitted follow-up behavior;
- no invented price, discount, SLA, warranty, scope, legal term or data promise;
- stop/escalate if recipient rights, identity, customer relationship, data source or commitment boundary is unclear.

Excluded by default:

- bank/payment and accounting administration;
- signing keys/tokens;
- full customer private repositories unrelated to the campaign;
- product source write;
- Company governance write except ordinary approved commercial evidence in its proper store;
- infrastructure/security admin;
- owner personal/general email account.

#### Future human sellers

A future seller Assignment should normally receive only:

- dedicated Company sales identity/mailbox;
- scoped `RA-05` public research;
- scoped `RA-07` CRM/prospect/customer commercial state;
- customer documents/information required for assigned accounts;
- approved sales enablement material.

No default seller access exists to bank/payment, signing keys, Company governance administration, engineering repository write, cross-customer private data, security administration or `ROD-*` approval evidence beyond what is needed to prepare an escalation.

### 7.4 `POS-003 — Portfolio & Product Lead` access

#### Human Assignment

Eligible access:

- `RA-01`: `R/W` to Company portfolio/planning/governance artifacts inside POS-003 scope;
- `RA-02`: broad `R` across sponsored/relevant product repositories for product status, roadmap, release and evidence analysis;
- `RA-13`: `R` to CI/release evidence where needed for portfolio decisions;
- customer/commercial evidence from POS-002 in summarized/minimized form unless raw detail is necessary.

Product repository write is not granted merely because a Position owns portfolio interpretation.

#### AI advisory component

Initial access ceiling:

- `RA-01`: `R` and bounded `W` to proposals/portfolio-state synchronization when tasked;
- `RA-02`: `R` across relevant product repositories;
- `RA-13`: `R` CI/release evidence;
- `RA-05`: `R` market/product research where relevant;
- no production, deploy, secret, bank, signing or customer-admin access.

AI may synthesize continue/change/stop/reuse evidence but cannot technically or organizationally start/stop a product or allocate material capital merely because it can edit a portfolio file.

### 7.5 `POS-004 — Engineering & Release Lead` — AI-led access

The AI-led engineering Position requires the broadest non-human **technical execution** capability, but its access must be narrower than the Owner's overall technical reach.

Initial access ceiling for the AI engineering Principal/workload class:

- `RA-02`: `R/W` only to product repositories/worktrees included in the active Assignment/workstream;
- `RA-12`: `R/W/X` inside approved engineering work directories, VMs/hosts and test environments required by the workstream;
- `RA-13`: `R/X`, and bounded `W` for build/test/artifact operations; may trigger CI and read results;
- product issue/spec/test artifacts required to understand accepted technical scope;
- `RA-18`: approved model/agent/runtime/orchestrator.

Where a build/test/release workflow uses a stored secret, the preferred pattern is:

```text
workflow/runtime receives secret through controlled secret injection
→ AI/workload invokes the bounded operation
→ raw secret value is not shown to the model, prompt, log or ordinary repository content
```

Explicitly excluded by default:

- GitHub organization/repository `P` administration, collaborator management or security-policy changes;
- raw `K` access to CI/CD secrets, owner tokens, private keys or recovery material;
- `RA-09` bank/payment;
- `RA-10` legal/corporate/e-signature private key or PIN material;
- `RA-06` general customer/commercial mailbox;
- `RA-07` CRM except a purpose-specific read-only requirement explicitly added later;
- production/customer systems unrelated to the assigned workstream;
- cross-customer confidential data;
- DNS/hosting/infrastructure `P` administration unless a separate bounded workstream explicitly requires and authorizes it;
- consequential production deploy, release publication, store submission or customer external effect outside an already approved execution class;
- Company Owner/governance approval operations.

For code signing or legally/operationally sensitive physical tokens, the default Company boundary is **human-controlled execution** unless a later explicit workflow proves a lawful, secure, bounded machine path. AC-206 does not authorize AI access to physical signing credentials.

The AI engineering Principal must fail closed when the required repository/workstream scope is absent or when an operation would need privilege outside this ceiling.

### 7.6 `POS-005 — Finance & Obligation Control Lead` access

#### Current Owner human Assignment

Eligible access:

- `RA-08`: `R` to accounting reports/source information required for management interpretation; any operational accounting write occurs only through valid accounting/service processes;
- `RA-09`: management visibility required to understand balances/payments/obligations, subject to the bank's own access model;
- private management-finance/obligation records (`DC-2`) in a suitable restricted store;
- `RA-01`: only safe aggregated/specification/decision artifacts suitable for the public repository, not live bank details or transaction payloads;
- relevant customer/supplier obligation evidence through POS-002/workstream interfaces.

Payment/signing capability is **not granted by POS-005**. Where the current Owner human has bank payment or signature capability, it remains a separate technical/legal capacity requiring the applicable Company decision and external authority.

No standing AI Assignment exists for POS-005 under AC-205. Therefore AC-206 does not create a standing AI right to detailed bank/accounting/management-finance data.

#### Outsourced accounting/tax interface

Eligible access remains limited to the provider's valid professional/legal/service contour and may include accounting source documents, accounting systems, statutory/tax interfaces and agreed bank-information channels as actually authorized.

AC-206 does not infer:

- payment authority;
- Company Organizational Authority;
- customer/commercial authority;
- Company repository administration;
- security/infrastructure administration;
- broader access merely because the provider needs accounting documents.

Provider access must be separately revocable and recoverable so provider replacement does not require exposing unrelated Company credentials.

### 7.7 `POS-006 — Security, Risk & Continuity Lead` access

#### Current Owner human Assignment

Eligible access:

- access/governance metadata across `RA-01`–`RA-18` sufficient to assess who/what can reach material resources;
- `RA-15` privileged credential/secret-management administration where the current Owner is the legitimate holder/admin;
- `RA-16` security/incident/continuity evidence;
- relevant `RA-14` infrastructure/IAM/security settings where required to administer or assess risk;
- repository/security configuration and audit metadata;
- recovery/rotation/revocation mechanisms for material credentials.

This technical reach does not permit POS-006 to accept a material risk exception that remains `ROD-06`, `ROD-07`, `ROD-08` or material `ROD-09`.

#### AI advisory component

Initial access ceiling:

- `R` to sanitized/minimized security configuration, inventory, dependency and incident evidence needed for analysis;
- `R/W` to Company security governance proposals/reviews in `RA-01` when tasked;
- `R` to public/vendor/product documentation and non-secret configuration evidence;
- no default `P` admin access;
- no default `K` raw secret/key/recovery access;
- no direct material risk acceptance or control waiver;
- no cross-customer confidential data beyond a specifically authorized incident/workstream scope.

If a future runbook allows AI/software to perform revocation, isolation, rotation or recovery mechanics, that must be separately admitted as `AM-1` or pre-authorized `AM-4` execution with explicit resource scope, evidence, failure behavior and rollback/reconciliation. AC-206 does not activate such automation.

## 8. Owner-only / human-controlled high-consequence capabilities

At the current baseline, the following capabilities remain human-controlled and are not granted to AI merely because AI participates in a Position:

1. `RA-10` legal/corporate signing and qualified electronic-signature private-key/PIN use;
2. bank/payment approval/signing or equivalent high-consequence `RA-09` transaction authorization;
3. master credential recovery/root-account recovery for Company-critical accounts;
4. creation of new broad privileged administrators;
5. release of a `DC-3` secret value to another Principal;
6. material cross-customer data-sharing permission;
7. privileged access that itself requires a material risk/data-sovereignty exception;
8. any technical operation whose organizational decision remains an AC-202 `ROD-*` final decision.

This is a current access baseline, not a permanent assertion that no secure automation can ever exist. A future change requires explicit authority, a bounded workflow and evidence strong enough to modify AC-203/Position/Assignment/access state as applicable.

## 9. Credential and access-register architecture

### 9.1 Public metadata vs restricted operational register

This public repository may contain only safe access-governance metadata and schemas.

A live restricted access/credential inventory must use an owner-controlled private store or other approved restricted system. Tool selection is not fixed by AC-206.

The public layer MAY record generic asset classes and accountable Position. It SHOULD NOT expose account identifiers, recovery channels, device serials, detailed attack surface, private endpoints or other metadata when publication would materially increase risk.

### 9.2 Minimum restricted access-record fields

For each material access grant/account/credential, the restricted register should be able to reconstruct:

- `access_asset_id` — stable internal reference, not the secret;
- `resource_class` / system;
- organization/customer/workstream scope;
- assigned Principal or service identity;
- Position/Assignment basis;
- technical capability (`R/W/X/P/K/E` as applicable);
- data classes permitted;
- environment scope (dev/test/prod where applicable);
- grant authority / approval reference;
- credential holder/custodian class;
- secret-storage location reference **without storing the secret value in the register** where possible;
- authentication/MFA/physical-token dependency metadata proportionate to risk;
- effective/expiry/review condition;
- revocation path;
- recovery/rebinding path;
- last access review evidence;
- incident/rotation trigger where applicable;
- continuity/fallback owner.

### 9.3 No shared anonymous machine identity for consequential work

AI agents, CI workloads and integrations should use attributable service/workload identities where practical.

A single shared owner token across unrelated AI/workflows should be treated as a transition risk, not a target design, because it destroys least privilege, revocation scope and attribution.

Where a temporary shared credential exists, AC-207/implementation work should prioritize replacement when its compromise or unavailability could produce material cross-workstream effects.

## 10. Grant, review and revocation semantics

### 10.1 Routine grant

A technical grant may be provisioned only when it is inside an approved Assignment access ceiling and does not itself require a separate material approval.

The grant record must identify the Principal, resource scope, technical capability, purpose and revocation path.

### 10.2 Privileged/restricted grant

`P`, `K`, broad production `E`, bank/signing capability, cross-customer access or equivalent high-consequence grants require explicit attributable human authorization under the applicable Company/legal/customer boundary.

Current lack of `AM-3` means a system or AI workflow cannot independently approve its own privileged access expansion.

### 10.3 Review triggers

Access must be reviewed when:

- Assignment changes, expires or is revoked;
- a seller/accounting provider/contractor leaves or changes scope;
- a product/workstream ends;
- a customer relationship or data purpose ends;
- a credential is suspected compromised;
- privilege is broader than current work requires;
- a new AI runtime/vendor materially changes data exposure;
- a device/runtime is replaced;
- a Position is split/merged/retired;
- a material incident shows access design was insufficient.

### 10.4 Revocation

Revocation must be possible without destroying historical attribution.

Removing current access must not erase evidence of who acted previously, which Assignment was active or which approval authorized the earlier grant.

## 11. AI-specific access invariants

1. AI capability does not create access eligibility.
2. AI should receive purpose-specific service/workload identity rather than the Owner's unrestricted credential where practical.
3. AI must not receive `DC-3` secret material in prompts, chat context, generated files, logs or ordinary canonical state.
4. Where a tool requires a secret, prefer execution-time secret injection that does not reveal the value to the model.
5. AI repository access should be repository/workstream scoped; organization-wide administration is not the default.
6. AI customer data access is customer/workstream scoped and purpose-limited; no cross-customer memory/reuse by default.
7. AI commercial sending is a bounded external effect and must have a dedicated sending boundary rather than unrestricted use of the Owner's general mailbox.
8. AI engineering may make bounded technical changes but cannot infer customer acceptance, release authority, spend authority or risk exception from successful tests.
9. AI security analysis should use sanitized configuration/evidence where raw credentials are not necessary.
10. Replacement of a model/provider/runtime must not require redefining Position authority or transferring the only copy of critical organizational history.

## 12. Customer and cross-organization boundary

Customer access is never ambient.

For every customer/workstream access grant, the applicable scope must be reconstructable:

- customer/organization;
- purpose;
- data/system class;
- Principal/Assignment;
- permitted operations;
- time/review condition;
- customer/contractual/other valid basis where required;
- deletion/return/revocation expectation when the work ends.

A Principal's access to Customer A does not grant access to Customer B even when the same tool/account could technically reach both.

Cross-customer reuse of data, prompts, knowledge, credentials or operational history is denied by default and requires an explicit rights/governance basis. Public/generalized learning may be promoted only after the applicable review/approval and without leaking customer-specific protected content.

## 13. Product and Arvectum OS boundary

Product repositories remain canonical for product-specific implementation access rules and secrets. AC-206 defines the Company-wide maximum semantics, not every product permission.

A product may narrow access further based on product risk, customer contract or deployment topology.

Arvectum OS may later represent Principal identities, authorization, Organization scope and governed access under an admitted contract. That technical representation does not create Company Position authority and does not authorize platform-global access to Company/customer data.

No Company Position receives OS platform admin authority merely because a Company product uses Arvectum OS.

## 14. Emergency / break-glass boundary

AC-206 does not claim that a production break-glass mechanism already exists.

Any future break-glass mechanism must:

- be reserved for a genuine recovery/security need;
- identify the actual acting Principal;
- limit scope and duration;
- preserve reason and evidence;
- not erase the represented/affected Principal or customer scope;
- not create a `ROD-*` decision or legal authority;
- be reviewed after use;
- revoke/return privilege after the emergency purpose ends;
- reconcile any state changed during the emergency.

Break-glass is an emergency technical access mechanism, not an emergency source of Company authority.

## 15. Current access-gap / implementation backlog

AC-206 identifies several implementation gaps without pretending they are already solved:

1. no complete restricted Company credential/access inventory is yet evidenced;
2. some Owner-held credentials/tokens/admin capabilities remain concentrated single points from AC-105;
3. AI/service-specific identities and narrowly scoped tokens are not proven uniformly across current tools/repositories;
4. the dedicated AI commercial sending identity/CRM boundary is not yet evidenced as operational;
5. product-repository and CI permissions are product-specific and not yet reconciled into one Company access review;
6. physical signing/e-signature and local-device dependencies remain human/Owner gates and require AC-207 continuity analysis;
7. accounting-provider recovery/replacement access is not yet tested;
8. customer-data authoritative stores, retention and recovery are workstream-specific and not yet Company-wide;
9. break-glass/recovery procedures are not yet tested Company-wide;
10. current technical permissions may be broader than the target least-privilege model and must not be misrepresented as approved authority.

These are explicit `Known / not yet proven` conditions rather than readiness claims.

## 16. AC-207 continuity handoff

AC-207 must use this access baseline to test continuity and replacement, including at minimum:

- loss/lockout of the Owner's GitHub/admin identity;
- replacement of AI engineering service identity/runtime without losing repository/workstream state;
- revocation/replacement of AI commercial sender credentials without losing suppression/follow-up state;
- replacement of outsourced accounting while preserving source documents and management interpretation;
- loss of a local engineering workstation/VM;
- loss/replacement of signing-token availability without bypassing legal/security controls;
- rotation/recovery of Company-critical credentials;
- GitHub outage with GitVerse/local history available but canonical authority unchanged;
- customer access expiry/revocation and handover;
- containment when a credential is suspected compromised;
- Owner short-term unavailability without allowing AI/software to infer reserved authority.

AC-207 should distinguish `recovery path exists on paper` from `recovery path has been tested`.

## 17. Completion boundary

AC-206 is substantively complete when the Company can explain:

- the difference between authority and technical access;
- the Company data classes and secret-handling boundary;
- the resource classes that matter now;
- the maximum justified access for each AC-205 executor class;
- why AI-led Engineering receives code/build execution without bank/signing/customer/governance privilege;
- why AI commercial outreach receives a dedicated bounded communication/data path rather than Owner-wide access;
- why outsourced accounting remains a restricted external-service contour;
- why finance and security access remain separately reconstructable even though one human currently holds both Positions;
- which capabilities remain human-controlled;
- how access grants, review and revocation should be represented without storing secrets publicly;
- the unresolved access/credential/recovery gaps that AC-207 must test.

This `0.9.0` publication is a **proposal only**. It creates no actual credential or permission and becomes binding Company access governance only after explicit Owner approval of the exact reviewed proposal.