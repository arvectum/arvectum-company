# Arvectum Company Canonical Sources Registry

Status: `Active`
Version: `0.9.0`
Updated: `2026-08-20`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`

## 1. Purpose

This registry identifies the authoritative sources and convenience reference copies used when designing and operating Arvectum Company.

A file being available as a ChatGPT Project Source does **not** make it canonical. Project Sources are retrieval aids. Authority follows the applicable legal/corporate hierarchy and canonical repository records.

## 2. Authority rules

1. Applicable law and valid legal/corporate authority govern ООО «Арвектум» within their scope.
2. Approved Arvectum Company governance artifacts and explicit owner decisions govern Company-specific internal matters within their scope.
3. Where Company relies on Arvectum OS, the applicable canonical Arvectum OS Constitution, Accepted RFC/ADR, approved governance, Product Contracts and implementation/operational evidence govern that reliance within their declared scope.
4. Product-specific implementation authority remains in the applicable product repository and approved product decisions/contracts.
5. Roadmaps coordinate planning; they do not independently grant authority or readiness.
6. Chat history, model memory, generated source packs and local copies are not independent canonical authority.
7. If a convenience snapshot conflicts with its canonical original, the canonical original wins and the snapshot must be refreshed or removed.

## 3. Arvectum Company canonical sources

| Source | Status | Role |
|---|---|---|
| `docs/constitution/COMPANY-CONSTITUTION.md` | Ratified `1.0.0` | Company Constitution / Founding Charter; highest approved Company-specific internal governance artifact below applicable legal/corporate authority |
| `docs/governance/decisions/DECISION-2026-08-19-AC-001-RATIFICATION.md` | Approved | Owner ratification record for AC-001 and exact approved proposal reference |
| `docs/governance/COMPANY-OS-AUTHORITY-BOUNDARY.md` | Approved `1.0.0` | Canonical Company ↔ Arvectum OS authority and responsibility boundary |
| `docs/governance/decisions/DECISION-2026-08-20-AC-002-APPROVAL.md` | Approved | Owner approval record for exact AC-002 Proposed `0.9.0` and publication authority for `1.0.0` |
| `docs/governance/CANONICAL-REPOSITORY-STRUCTURE.md` | Approved `1.0.0` | Canonical repository structure and artifact-location map for durable Company assets |
| `docs/governance/decisions/DECISION-2026-08-20-AC-003-APPROVAL.md` | Approved | Owner approval record for exact AC-003 Proposed `0.9.0` and publication authority for `1.0.0` |
| `docs/reviews/AC-005-FOUNDING-BASELINE-CROSS-REVIEW.md` | Complete / PASS | Formal cross-review of AC-001 through AC-004 as one founding baseline; seven iterations and M0 closure recommendation |
| `docs/governance/decisions/DECISION-2026-08-20-M0-FOUNDING-BASELINE-CLOSURE.md` | Approved | Owner milestone-closure record for AC-005/M0 and planning transition to AC-101; creates no new substantive authority by implication |
| `docs/business/CURRENT-BUSINESS-MODEL-AND-VALUE-PROPOSITION.md` | Active `0.2.0` | Corrected AC-101 business-model/value-proposition baseline. Flagship direction: customer-specific AI-native company / «ИИ-компания под ключ» on Arvectum OS with organization-first design and reusable functional modules. Supersedes the initial procurement-centered `0.1.0` interpretation |
| `docs/reviews/AC-101-CURRENT-BUSINESS-MODEL-CROSS-REVIEW.md` | Complete / PASS | AC-101 cross-review completed at 10/10 after material Owner strategy correction; records why procurement is a domain/module line rather than the highest-level Company product identity |
| `docs/roadmap/ROADMAP.md` | Active | Canonical Company planning source |
| `docs/portfolio/PORTFOLIO.md` | Active `0.1.0` | Initial Company-level product/initiative ownership, repository/dependency and ambiguity map created by AC-004; does not itself approve investment, Positions, module admission or product readiness |
| `docs/CANONICAL-SOURCES.md` | Active | This source registry |

AC-101 deliberately promotes only the business-model statements actually recorded in the corrected `0.2.0` artifact. The Owner's material correction supersedes the earlier procurement-centered interpretation. Historical chat remains context/evidence and is not converted wholesale into canonical Company state.

## 4. External canonical Arvectum OS dependencies

Canonical repository: `arvectum/arvectum-os`.

Snapshot used to generate the current repository Project Source pack:
- branch: `main`;
- commit: `de59771281ce1b4c58d943bd003560384e332270`;
- commit timestamp: `2026-08-19T21:12:03+03:00`.

The snapshot SHA is provenance only. Before material work, current canonical repository state must still be checked.

AC-101 re-checked current Arvectum OS `main` on `2026-08-20` at `f4028cd8d84a1cdc81ae366c59dc4fb15d6a134c`. The Company-relevant governing baseline remains compatible with this registry: Constitution `1.2.0` is still Ratified; RFC-0001 through RFC-0008 remain Accepted `1.0.0`; the Decision Authority Policy remains Proposed `0.2.1`; CAP-001 through CAP-004 remain `Incubating / Provisional`; P6.02 and P6.06 remain `Provisional 0.1.0`; Phase 8 remains `Draft / Exploratory` while P8.00 performs pre-activation revalidation. No Project Source pack refresh is required solely for that roadmap movement.

| Canonical source | Known status at pack generation | Company relevance |
|---|---|---|
| `docs/constitution/CONSTITUTION.md` | Ratified `1.2.0` | Platform constitutional invariants |
| `docs/rfc/README.md` | Canonical RFC index | Current RFC status/provenance index |
| `docs/rfc/RFC-0001-arvectum-os-architecture.md` | Accepted `1.0.0` | Platform architecture and boundaries |
| `docs/rfc/RFC-0002-canonical-record-kernel-metamodel.md` | Accepted `1.0.0` | Canonical records, authority, relationships, organizational assets |
| `docs/rfc/RFC-0003-identity-security-privacy-tenant-sovereignty-portability.md` | Accepted `1.0.0` | Identity, security, sovereignty and portability |
| RFC-0004 accepted `1.0.0` | Accepted | Product Contract / extension boundary |
| RFC-0005 accepted `1.0.0` | Accepted | Governed Execution and Workflow |
| RFC-0006 accepted `1.0.0` | Accepted | Event, provenance and observability |
| RFC-0007 accepted `1.0.0` | Accepted | Memory, knowledge and governed learning |
| RFC-0008 accepted `1.0.0` | Accepted | Document and artifact architecture |
| `docs/governance/DECISION-AUTHORITY-POLICY.md` | **Proposed `0.2.1`** | Design reference only until approved; not binding policy |
| `docs/contracts/P6-02-FIRST-REAL-PRODUCT-CONTRACT.md` | Provisional `0.1.0` | Tender Agent governed reliance boundary; repository locator requires reconciliation |
| `docs/contracts/P6-06-SECOND-REAL-PRODUCT-CONTRACT.md` | Provisional `0.1.0` | Discount Parser governed reliance boundary |

## 5. ChatGPT Project Source convenience pack

Generated files live under `docs/project-sources/`. They are intentionally grouped to conserve Project Source slots.

| File | Contents | Authority |
|---|---|---|
| `01_ARVECTUM_OS_CONSTITUTION.md` | `Arvectum OS Constitution` | Convenience snapshot; uploadable Project Source |
| `02_ARVECTUM_OS_RFC_0001_ARCHITECTURE.md` | `Arvectum OS RFC-0001 — Architecture` | Convenience snapshot; uploadable Project Source |
| `03_ARVECTUM_OS_RFC_0002_RECORD_AUTHORITY_MODEL.md` | `Arvectum OS RFC-0002 — Canonical Record, Authority and Organizational Asset Model` | Convenience snapshot; uploadable Project Source |
| `04_ARVECTUM_OS_RFC_0003_IDENTITY_SECURITY_SOVEREIGNTY.md` | `Arvectum OS RFC-0003 — Identity, Security, Privacy, Sovereignty and Portability` | Convenience snapshot; uploadable Project Source |
| `05_ARVECTUM_OS_RFC_0004_0008_ACCEPTED.md` | `Arvectum OS Accepted RFC-0004 through RFC-0008` | Convenience snapshot; uploadable Project Source |
| `06_ARVECTUM_OS_GOVERNANCE_REFERENCE.md` | `Arvectum OS Governance Reference` | Convenience snapshot; uploadable Project Source |
| `07_ARVECTUM_OS_PRODUCT_CONTRACTS_REFERENCE.md` | `Arvectum OS Product Contracts Relevant to Initial Arvectum Company Portfolio` | Convenience snapshot; uploadable Project Source |

Recommended upload set: all seven generated files. This leaves Project Source capacity for private legal/corporate documents and future Company artifacts.

A repository source-pack refresh is not required merely because the Arvectum OS HEAD advances. Refresh is required when an included source changes materially.

## 6. Legal and corporate authority sources

Legal/corporate originals are owner-managed external authorities. They are available privately as ChatGPT Project Sources where useful and **must not be copied into this public repository by default**, especially where they contain personal data, signatures, tax identifiers, addresses, bank details or other unnecessary sensitive information.

Current verified source set:

| Private source | Status / date | Authority or evidentiary role |
|---|---|---|
| Типовой устав №23, утверждённый приказом Минэкономразвития России от 01.08.2018 №411 | Current governing charter form | Corporate governance framework of the Company within applicable law |
| Решение единственного учредителя №1 о создании ООО «Арвектум» | `2026-06-07` | Founding decision; establishes Company creation, charter choice, capital allocation and initial General Director appointment |
| Лист записи ЕГРЮЛ о создании ООО «Арвектум» | `2026-06-24` | State-registry evidence of creation and registered corporate facts |
| Выписка из Единого государственного реестра налогоплательщиков (форма по КНД 1121005) | `2026-06-24` | Tax-registration evidence |
| Банковские реквизиты ООО «Арвектум» | Current owner-managed operational reference | Operational payment reference; not a source of corporate governance authority |

Verified corporate baseline relevant to Company governance:
- ООО «Арвектум» operates under Типовой устав №23;
- the Company has one participant holding 100% of the charter capital;
- the founding decision appoints the General Director for a five-year term;
- the ЕГРЮЛ creation record identifies one person entitled to act for the Company without a power of attorney and records the Company as active at issuance.

The founding-decision date was visually re-checked during AC-005 as `2026-06-07`; convenience OCR output is not used to override the source image.

The registry does **not** require repeated procurement of a fresh ЕГРЮЛ extract solely for internal documentation freshness when there is no known corporate change or conflicting evidence. Re-verification is triggered when a consequential decision depends on a potentially changed registry fact, a corporate event occurs, existing evidence becomes inconsistent, or applicable law/contract requires a current extract.

If legal/corporate sources conflict with internal Company documentation, the conflict must be reconciled rather than hidden. Internal governance cannot create legal or contractual authority that the Company or Principal does not possess.

## 7. Refresh rule

The Project Source pack is a snapshot, not a mirror. Refresh it when:
- the OS Constitution changes;
- an included RFC changes status/version or is superseded;
- an included governance policy is approved/superseded/withdrawn;
- an included Product Contract changes materially;
- a material Company decision depends on source text newer than the current snapshot.

Routine OS roadmap or implementation movement alone does not require a refresh because those materials are intentionally not bundled as stable Project Sources.

## 8. Exclusions

Do not treat the following as stable Project Sources merely for convenience:
- fast-changing OS or product roadmaps;
- transient task notes and review drafts;
- GitHub issues as authority;
- model-generated summaries instead of canonical originals;
- source code/test output unless a specific decision requires it;
- secrets, private keys, tokens, passwords or unnecessary personal data.