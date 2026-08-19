# Arvectum Company Canonical Sources Registry

Status: `Active`
Version: `0.1.0`
Updated: `2026-08-19`
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
| `docs/roadmap/ROADMAP.md` | Active | Canonical Company planning source |
| `docs/constitution/...` | Pending `AC-001` | Company Constitution / Founding Charter |
| Company ↔ Arvectum OS authority artifact | Pending `AC-002` | Explicit Company/OS authority and responsibility boundary |
| `docs/portfolio/PORTFOLIO.md` | Pending `AC-004` | Company portfolio map |
| `docs/CANONICAL-SOURCES.md` | Active | This source registry |

## 4. External canonical Arvectum OS dependencies

Canonical repository: `arvectum/arvectum-os`.

Snapshot used to generate the current Project Source pack:
- branch: `main`;
- commit: `fbab170ab337c1631b40d0d36ea58a02f6512f6e`;
- commit timestamp: `2026-08-19T20:38:20+03:00`.

The snapshot SHA is provenance only. Before material work, current canonical repository state must still be checked.

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

Recommended upload set: all seven generated files. This leaves Project Source capacity for private legal/corporate documents and future Company founding artifacts.

## 6. Legal and corporate authority sources

The owner maintains the applicable legal originals. They should be added privately to the ChatGPT Project when useful, but **should not be copied into this public repository by default**, especially where they contain personal data, signatures, identifiers or other unnecessary sensitive information.

Expected categories include, as applicable:
- current charter / Устав ООО «Арвектум»;
- founding / sole participant decisions;
- appointment and authority of the General Director;
- current ЕГРЮЛ evidence;
- material powers of attorney or other standing legal delegations.

Status: `Owner-managed / pending Project Source addition`.

If these sources conflict with internal Company documentation, the conflict must be reconciled rather than hidden. Internal governance cannot create legal or contractual authority that the Company or Principal does not possess.

## 7. Refresh rule

The Project Source pack is a snapshot, not a mirror. Refresh it when:
- the OS Constitution changes;
- an included RFC changes status/version or is superseded;
- an included governance policy is approved/superseded/withdrawn;
- an included Product Contract changes materially;
- a material Company decision depends on source text newer than the current snapshot.

Routine OS roadmap movement alone does not require a refresh because the OS roadmap is intentionally not bundled as a static Project Source.

## 8. Exclusions

Do not treat the following as stable Project Sources merely for convenience:
- fast-changing OS or product roadmaps;
- transient task notes and review drafts;
- GitHub issues as authority;
- model-generated summaries instead of canonical originals;
- source code/test output unless a specific decision requires it;
- secrets, private keys, tokens, passwords or unnecessary personal data.
