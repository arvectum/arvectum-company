# AC-003 — Canonical Repository Structure and Artifact Map

Status: `Proposed`
Version: `0.9.0`
Created: `2026-08-20`
Updated: `2026-08-20`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-003 — Canonical repository structure and artifact map`
Review: `docs/reviews/AC-003-CANONICAL-REPOSITORY-STRUCTURE-CROSS-REVIEW.md`
Approval: `Pending explicit Owner decision`
Canonical remote: `GitHub / arvectum/arvectum-company`
Mirror: `GitVerse — non-authoritative mirror unless a later approved decision changes this rule`

## 1. Purpose

This artifact defines the canonical repository structure and artifact-location rules for Arvectum Company.

Its purpose is not to turn Git into the database of the Company or to create a directory for every imaginable function. Its purpose is to make durable Company artifacts discoverable, attributable and unambiguous while preserving the separation among:

- legal/corporate authority;
- Company-specific governance and organizational semantics;
- Arvectum OS platform contracts and governed execution;
- product-specific implementation and product roadmaps;
- sensitive/high-frequency operational records that require a different canonical store;
- transient drafts, chats and generated working material.

The structure serves the business. A directory or artifact class exists only when it provides real governance, continuity, discoverability, accountability or operating value.

## 2. Authority and governing baseline

This map is subordinate to:

1. applicable law and valid legal/corporate authority of ООО «Арвектум»;
2. `docs/constitution/COMPANY-CONSTITUTION.md`;
3. approved Company governance artifacts and explicit competent decisions within their scope;
4. applicable Arvectum OS Constitution, Accepted RFC/ADR, approved governance and Product Contracts where Company relies on Arvectum OS;
5. applicable product governance and product repositories for product-specific implementation.

`docs/CANONICAL-SOURCES.md` remains the registry of current authoritative and convenience sources. This artifact defines **where classes of Company artifacts belong and how they become canonical**; it does not replace the source registry.

The approved Company ↔ OS boundary in `docs/governance/COMPANY-OS-AUTHORITY-BOUNDARY.md` remains controlling where this map touches Arvectum OS.

## 3. Repository role

### 3.1 What this repository is

`arvectum/arvectum-company` is the canonical repository for durable, repository-suitable Arvectum Company governance, planning, portfolio, organizational-model, operating-model and review artifacts.

Within that scope, Git history provides useful provenance, reviewability and portability.

### 3.2 What this repository is not

This repository is **not** automatically the canonical store for every fact or operational record of ООО «Арвектум».

The following may have an external canonical source when that is safer, legally required, operationally superior or already authoritative:

- legal/corporate originals and registry records;
- accounting and tax records;
- banking and payment records;
- contracts and customer/supplier documents;
- personnel and personal-data records;
- credentials, keys and secrets;
- high-volume runtime Events, executions and logs;
- product-domain operational state;
- external systems of record;
- Arvectum OS canonical records where an approved OS contract establishes that responsibility.

When an external source remains authoritative, this repository MAY contain a safe governed locator, policy, metadata reference or source-registry entry. It MUST NOT create a competing authoritative copy merely for convenience.

### 3.3 Canonical home is a responsibility decision, not a storage slogan

For this artifact, **canonical home** means the approved place responsible for the authoritative representation within a declared scope.

A canonical home may be:

- a file in this repository;
- a product repository;
- the canonical Arvectum OS repository or governed OS state;
- an owner-controlled private repository/store;
- an external legal, accounting, banking, customer or supplier system of record.

Physical possession of a copy does not transfer authority.

## 4. Public-repository safety boundary

At approval time this GitHub repository is public. Therefore repository suitability is a mandatory admission test, not an assumption.

The following MUST NOT be committed to this public repository unless a later explicit authority and data-classification decision establishes a safe and lawful publication basis:

- passwords, tokens, private keys, recovery material or reusable credentials;
- personal identifiers that are not necessary for the public governance purpose;
- signatures or identity-document images;
- bank-account/payment details and non-public financial transaction data;
- non-public customer, supplier, tender, contract or commercial-confidential content;
- employee/contractor personal files, compensation or sensitive HR data;
- private incident payloads, security evidence or exploit details whose disclosure increases risk;
- raw production prompts/context containing protected or customer data;
- personal addresses, tax identifiers or other unnecessary personal data copied from legal/corporate documents.

Legal/corporate originals remain owner-managed external authorities by default, consistent with `docs/CANONICAL-SOURCES.md`.

A future change of repository visibility from public to private does **not** automatically authorize migration of sensitive data into Git. The responsible artifact class, access model, retention/deletion requirements and operational need must still justify storage.

Because Git preserves history, deleting a sensitive file in a later commit is not sufficient remediation. If a secret or restricted payload is committed accidentally, the response MUST include containment appropriate to the material, including credential rotation/revocation where applicable and history remediation when required.

## 5. Current physical repository baseline

At AC-003 drafting time, the repository already contains:

```text
/
├── README.md
├── LICENSE
├── .github/
│   └── workflows/
├── docs/
│   ├── CANONICAL-SOURCES.md
│   ├── constitution/
│   ├── governance/
│   │   └── decisions/
│   ├── project-sources/
│   ├── reviews/
│   └── roadmap/
└── tools/
```

This existing structure is valid and is extended logically rather than replaced by a speculative full enterprise tree.

## 6. Canonical logical structure

The approved logical structure is:

```text
/
├── README.md                         # repository entry point, non-authoritative summary
├── LICENSE
├── .github/
│   └── workflows/                    # repository automation, not Company authority by itself
├── docs/
│   ├── CANONICAL-SOURCES.md          # current authority/source registry
│   ├── constitution/                 # Company Constitution and approved amendments/publications
│   ├── governance/                   # Company-wide governance boundaries, policies and authority artifacts
│   │   ├── decisions/                # explicit durable Company decisions/approval records
│   │   ├── policies/                 # created only when first real approved policy exists
│   │   ├── delegations/              # created only when explicit durable delegation records are required
│   │   └── exceptions/               # created only when material governed exceptions require a home
│   ├── roadmap/                      # canonical Company planning source
│   ├── portfolio/                    # Company portfolio map and portfolio-level governance artifacts
│   ├── business/                     # durable business/economic baseline models suitable for this repo
│   ├── organization/                 # functions, Positions and non-sensitive organizational model
│   ├── operations/                   # workflow specifications, continuity models and operating procedures
│   ├── security/                     # Company-specific security/data/access governance suitable for this repo
│   ├── management/                   # management-control models, registers/schemas and review cadence definitions
│   ├── reviews/                      # cross-reviews and formal review evidence
│   └── project-sources/              # generated convenience snapshots; non-canonical copies
└── tools/                             # repository-local helper tooling
```

### 6.1 Logical does not mean eagerly materialized

Directories in the logical map MUST be created only when the first real artifact for that class is admitted.

Git does not need empty placeholder directories. AC-003 therefore does not create `business/`, `organization/`, `operations/`, `security/`, `management/`, `policies/`, `delegations/` or `exceptions/` merely to make the tree look complete.

This rule prevents fake organizational complexity at the filesystem level.

### 6.2 One artifact, one canonical home

A durable Company artifact MUST have one canonical home within its declared scope.

References, exports and rendered copies MAY exist elsewhere, but they MUST identify the canonical source or be clearly marked non-canonical.

When a material artifact moves to a new canonical home, the transition MUST be explicit and preserve enough history/redirect information to avoid two live authoritative copies.

## 7. Artifact map

### 7.1 Founding and governance artifacts

| Artifact class | Canonical home | Canonicality / authority rule | Notes |
|---|---|---|---|
| Company Constitution / Founding Charter | `docs/constitution/` | Ratified Company governance, below applicable legal/corporate authority | Current: `COMPANY-CONSTITUTION.md` |
| Company-wide governance boundary | `docs/governance/` | Binding only after applicable approval | Current: Company ↔ OS boundary |
| Durable Company decision / approval record | `docs/governance/decisions/` | Canonical evidence of the internal decision within its scope | Must identify real decision authority; AI draft/review is not approval |
| Company policy | `docs/governance/policies/` | Binding only after approval by competent Company authority | Directory created on first real policy |
| Internal Organizational Authority delegation | `docs/governance/delegations/` or a canonical governed system explicitly approved later | Must be explicit, scoped, revocable and distinguish internal authority from legal power | Legal powers of attorney/corporate acts remain separate legal artifacts |
| Material governance exception/waiver | `docs/governance/exceptions/` | Must identify scope, authority, rationale, expiry/review and exit | No directory until needed |
| Canonical source registry | `docs/CANONICAL-SOURCES.md` | Registry/locator; does not override higher authority | Current source inventory |

### 7.2 Planning, portfolio and business artifacts

| Artifact class | Canonical home | Canonicality / authority rule | Notes |
|---|---|---|---|
| Company roadmap | `docs/roadmap/ROADMAP.md` | Canonical planning source only; does not grant authority | One current Company roadmap |
| Portfolio map | `docs/portfolio/PORTFOLIO.md` | Company-level product/initiative ownership and investment map | Product implementation details stay in product repos |
| Portfolio governance supporting artifacts | `docs/portfolio/` | Company owns prioritization, investment, accountable Position and stop/continue criteria | Avoid copying product roadmaps |
| Business model/value proposition baseline | `docs/business/` | Company business baseline when suitable for repository publication | AC-101 |
| Economic/cost model specification | `docs/business/` | Model/definition may be in repo; sensitive live figures MAY remain in a private authoritative store | AC-102 and later management reporting |
| Customer/value-stream model | `docs/business/` or `docs/operations/` according to whether it is strategic or workflow-specific | No customer-confidential payload in public repo | AC-103 |
| Owner workload/bottleneck model | `docs/business/` or `docs/organization/` | Use aggregated/non-sensitive representation where possible | AC-104 |
| Material dependency/risk baseline | `docs/business/`, `docs/security/` or `docs/operations/` according to dominant concern | Avoid duplicating one risk as multiple authorities | AC-105 |

### 7.3 Organization and authority artifacts

| Artifact class | Canonical home | Canonicality / authority rule | Notes |
|---|---|---|---|
| Function / minimal organizational model | `docs/organization/` | Company-specific organizational semantics | AC-201 |
| Reserved Owner Decisions | `docs/governance/` | Company authority boundary requiring explicit Owner approval | AC-202 |
| Delegated Position authority / approval / escalation model | `docs/governance/` | Defines internal authority architecture; actual delegations remain separately attributable | AC-203 |
| Position Registry | `docs/organization/` or approved governed runtime later | Position exists independently of executor | AC-204 |
| Assignment model / non-sensitive assignment registry | `docs/organization/` or approved governed runtime later | Assignment is not the source of legal authority; personal/sensitive data may require private store | AC-205 |
| Organization relationships / accountability model | `docs/organization/` or governed OS state under an admitted contract later | Company owns meaning; OS may govern representation/execution when admitted | No ambient OS authority |

### 7.4 Operations, security and management artifacts

| Artifact class | Canonical home | Canonicality / authority rule | Notes |
|---|---|---|---|
| Company workflow definition/specification | `docs/operations/` until/except where an admitted governed runtime becomes canonical | Versioned when operationally significant | Product-domain workflow stays product-owned unless explicitly Company-wide |
| Procedure/runbook | `docs/operations/` | Canonical when approved/activated for Company operation | Keep proportional to risk/frequency |
| Continuity/fallback model | `docs/operations/` | Company-owned continuity requirement; implementation may reference product/OS evidence | AC-207 |
| Company data/tool/credential access boundary | `docs/security/` | Governance/specification only; never store reusable secrets here | AC-206 |
| Security/data-handling policy | `docs/security/` or `docs/governance/policies/` depending on whether it is domain-specific control vs Company-wide policy | Must preserve deny-by-default/least-privilege where applicable | No duplication of OS RFCs |
| Work/obligation register **model** | `docs/management/` | Schema/control model may be public; live sensitive register may require private authoritative store | AC-401 |
| Decision/approval/escalation register **model** | `docs/management/` | Does not replace canonical decision records | AC-402 |
| Risk/exception/incident register **model** | `docs/management/` | Sensitive live incident evidence may remain outside public repo | AC-403 |
| Cash/commitment management-reporting **model** | `docs/management/` | Live cash/payment/tax/accounting data remains in appropriate private/accounting source unless explicitly approved otherwise | AC-404 |
| Management review cadence / Mission Control specification | `docs/management/` | Defines view/process, not independent source of underlying facts | AC-405–AC-407 |

### 7.5 Review, evidence and convenience artifacts

| Artifact class | Canonical home | Canonicality / authority rule | Notes |
|---|---|---|---|
| Formal cross-review evidence | `docs/reviews/` | Review evidence, not approval by itself | Simulated management lenses create no Positions or authority |
| ChatGPT Project Source pack | `docs/project-sources/` | Convenience snapshot only | Canonical original always wins |
| Repository helper tooling | `tools/` | Implementation helper, not governance authority | Must not silently change canonical meaning |
| GitHub Actions workflows | `.github/workflows/` | Automation only | Successful workflow ≠ business/legal/governance approval |
| README | `README.md` | Navigational summary | Must point to canonical artifacts rather than restating them as competing truth |

## 8. Company ↔ Product ↔ Arvectum OS repository boundary

### 8.1 Company repository owns

This repository owns Company-specific durable semantics such as:

- Company Constitution and internal governance;
- Company roadmap and portfolio governance;
- organizational functions, Positions, authority boundaries and operating-model artifacts;
- Company-wide workflow/management specifications;
- Company decisions and review evidence;
- Company-specific policies and continuity expectations.

### 8.2 Product repositories own

Product repositories own product-specific:

- source code and implementation;
- domain schemas and rules;
- product roadmaps;
- product-specific workflows, prompts, agents and validators;
- product release/deployment evidence;
- product customer/pilot implementation details;
- product-level integration artifacts except Company portfolio references.

A Company artifact MAY reference a product artifact by stable repository/path/version/commit where useful. It MUST NOT copy the product roadmap or implementation into this repository and then treat the copy as authoritative.

### 8.3 Arvectum OS repository owns

`arvectum/arvectum-os` owns domain-neutral platform architecture, Kernel semantics, platform governance, capability contracts, Product Contract architecture, Governed Execution semantics and other OS-specific canonical artifacts.

This repository MAY contain convenience snapshots under `docs/project-sources/`, but those files MUST remain clearly non-canonical.

A Company need does not become an OS commitment merely because it is recorded here. Cross-repository changes follow the applicable Company and OS governance paths separately.

## 9. Operational state and governed runtime boundary

Git is appropriate for low-frequency durable textual governance and design artifacts. Git is generally not the preferred canonical store for high-frequency or restricted operational state.

When a Company workflow later relies on Arvectum OS or another governed runtime, the applicable Product Contract/client boundary, authority mode, retention, data handling, portability and reconstruction rules determine which operational records belong in that runtime.

The Company repository SHOULD then retain only the durable Company specification, approval/decision references, compatible contract reference and safe operational evidence summary needed for governance and continuity.

No operational system becomes the source of Company Organizational Authority merely because it persists or enforces a Company record.

## 10. Artifact admission and lifecycle rules

### 10.1 Minimum metadata for significant durable artifacts

A significant Company artifact committed as a durable governed document SHOULD identify, proportionate to consequence:

- title and subject;
- status;
- version where meaningful;
- owner/accountable authority;
- created/updated date;
- roadmap/work-item or decision context where applicable;
- approval/decision reference when binding;
- superseded-by or replacement reference when no longer current.

### 10.2 Draft is not authority

`Draft`, `Working`, `Proposed`, review material and generated text do not become binding merely because they are committed.

A material governance artifact requiring Owner or other competent approval MUST preserve the exact proposal/version/blob or equivalent immutable reference that was approved.

AI-generated analysis, review or recommendation MUST NOT be recorded as if it were actual Owner approval.

### 10.3 Significant change

A significant change to a binding artifact SHOULD create a new identifiable version or an explicit superseding artifact according to the artifact's lifecycle.

Git history alone is useful evidence but MUST NOT be the only way to determine which materially different version is currently effective.

### 10.4 No approval by merge alone

A merge, CI PASS, branch protection result, code review or successful automation does not create Company Organizational Authority unless the applicable governance explicitly delegates that decision to that mechanism/Principal.

## 11. Naming and file conventions

Default conventions:

- durable markdown artifacts use descriptive uppercase filenames with `-` separators where practical;
- roadmap IDs appear in artifact metadata rather than becoming a mandatory directory hierarchy;
- decision records use `DECISION-YYYY-MM-DD-<SUBJECT>.md`;
- formal AC reviews use `AC-<NNN>-<SUBJECT>-CROSS-REVIEW.md`;
- canonical main documents should avoid filenames such as `FINAL-v7-really-final.md`;
- superseded files remain traceable rather than silently overwritten when historical interpretation would otherwise be ambiguous;
- generated convenience files MUST declare that they are non-canonical snapshots.

A more elaborate naming standard MUST NOT be created until real repository growth justifies it.

## 12. GitHub and GitVerse rule

GitHub repository `arvectum/arvectum-company` is the canonical remote at this stage.

GitVerse is a mirror for resilience/sovereignty and MUST NOT be treated as an independent co-equal source of truth merely because a mirrored commit exists there.

Mirror rules:

1. normal authoritative changes originate through the canonical GitHub repository and its approved workflow;
2. mirror automation MAY replicate the canonical history to GitVerse;
3. mirror failure does not silently change the canonical source;
4. if GitHub becomes unavailable and an emergency recovery path is activated, the recovery decision MUST identify the authority, source commit and reconciliation path;
5. if GitVerse is ever promoted to canonical or dual-write status, that change requires an explicit Company governance decision defining conflict resolution and recovery semantics.

The repository MUST remain recoverable without giving either hosting vendor ownership of Company Organizational Authority or the only copy of critical history.

## 13. Change and migration rules

A new directory/artifact class SHOULD be added only when at least one of these is true:

- a roadmap item creates a real durable artifact needing a canonical home;
- repeated artifacts create discoverability or ownership ambiguity;
- risk/compliance/continuity requires separation;
- an approved workflow/runtime creates a new governed boundary;
- existing placement causes duplication or conflicting authority.

A directory MUST NOT be created solely to imitate a conventional corporate org chart.

When changing canonical home:

1. identify current authority and source;
2. identify target authority/source;
3. preserve history and provenance required for the declared consequence;
4. define cutover/effective point;
5. prevent two live authoritative copies;
6. update `docs/CANONICAL-SOURCES.md` where applicable;
7. update references in roadmap/portfolio/governance artifacts where material;
8. record a decision when the move changes material authority, exposure, retention or operational dependency.

## 14. Mapping to the current Company roadmap

This map creates homes without pre-implementing later work.

| Roadmap range | Primary artifact home |
|---|---|
| `AC-001–AC-005` | `docs/constitution/`, `docs/governance/`, `docs/reviews/`, `docs/roadmap/`, `docs/portfolio/` |
| `AC-101–AC-106` | `docs/business/` with `docs/operations/` / `docs/security/` where the dominant artifact belongs there |
| `AC-201–AC-208` | `docs/organization/`, `docs/governance/`, `docs/security/`, `docs/operations/` |
| `AC-301–AC-306` | `docs/portfolio/` plus stable references to product repositories |
| `AC-401–AC-407` | `docs/management/` plus private/operational sources for live sensitive facts where required |
| `AC-501–AC-507` | `docs/operations/` for Company specification; governed runtime/OS/product repositories for their own execution evidence |
| `AC-601–AC-707` | `docs/organization/`, `docs/operations/`, `docs/management/` and admitted governed runtime state according to actual assignments/workflows |
| `M8` scale work | extend only from evidence; no pre-created departmental filesystem |

This table is a locator, not authorization to create later artifacts or make later roadmap decisions now.

## 15. AC-003 completion conditions

AC-003 may be closed only when:

1. this map passes cross-review and receives explicit competent approval;
2. the root `README.md` provides a correct repository entry point and safe navigation to canonical sources;
3. `docs/CANONICAL-SOURCES.md` registers the approved AC-003 artifact and decision;
4. `docs/roadmap/ROADMAP.md` marks AC-003 `Complete / PASS` and advances `AC-004 — Initial docs/portfolio/PORTFOLIO.md` to `Current`;
5. read-after-write verification confirms the approved publication, registry and roadmap state;
6. the canonical GitHub branch history is preserved and mirror automation remains an implementation concern rather than an authority source.

## 16. Deliberate deferrals

AC-003 does **not** create or approve:

- Reserved Owner Decisions (`AC-202`);
- delegated Position authority thresholds (`AC-203`);
- Position Registry or Assignments (`AC-204/205`);
- concrete data/tool/credential access matrix (`AC-206`);
- continuity policy (`AC-207`);
- live accounting, cash or commitment records;
- customer/supplier/tender record storage policy beyond the public-repository safety boundary;
- a new Arvectum OS client type, Product Contract or capability;
- a software document-management platform;
- departments or executive Positions;
- a private Company operational repository that has not yet been justified by real data/workflow needs.

These are later decisions triggered by actual business and operational evidence.

## 17. Approval status

Cross-review may establish proposal quality but cannot supply Owner approval.

This `Proposed 0.9.0` becomes binding only after an explicit decision by the competent Company authority against this exact proposal/version/blob or equivalent immutable reference.

Until then:

- the existing repository structure remains valid;
- this proposal may guide review and implementation planning but is not yet binding governance;
- `AC-003` remains `Current` in the canonical roadmap;
- `AC-004` must not be advanced merely by this draft.
