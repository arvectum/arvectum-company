#!/usr/bin/env python3
"""Build stable ChatGPT Project source bundles from canonical Arvectum OS files.

The generated files are convenience snapshots only. Canonical authority remains in
arvectum/arvectum-os and applicable legal/corporate originals.
"""

from __future__ import annotations

import argparse
import hashlib
import subprocess
from pathlib import Path


GROUPS: list[tuple[str, str, list[str]]] = [
    (
        "01_ARVECTUM_OS_CONSTITUTION.md",
        "Arvectum OS Constitution",
        ["docs/constitution/CONSTITUTION.md"],
    ),
    (
        "02_ARVECTUM_OS_RFC_0001_ARCHITECTURE.md",
        "Arvectum OS RFC-0001 — Architecture",
        ["docs/rfc/RFC-0001-arvectum-os-architecture.md"],
    ),
    (
        "03_ARVECTUM_OS_RFC_0002_RECORD_AUTHORITY_MODEL.md",
        "Arvectum OS RFC-0002 — Canonical Record, Authority and Organizational Asset Model",
        ["docs/rfc/RFC-0002-canonical-record-kernel-metamodel.md"],
    ),
    (
        "04_ARVECTUM_OS_RFC_0003_IDENTITY_SECURITY_SOVEREIGNTY.md",
        "Arvectum OS RFC-0003 — Identity, Security, Privacy, Sovereignty and Portability",
        ["docs/rfc/RFC-0003-identity-security-privacy-tenant-sovereignty-portability.md"],
    ),
    (
        "05_ARVECTUM_OS_RFC_0004_0008_ACCEPTED.md",
        "Arvectum OS Accepted RFC-0004 through RFC-0008",
        [
            "docs/rfc/RFC-0004-product-contract-product-experiment-extension-model-v1.0.0.md",
            "docs/rfc/RFC-0005-governed-execution-workflow-model-v1.0.0.md",
            "docs/rfc/RFC-0006-event-provenance-observability-model-v1.0.0.md",
            "docs/rfc/RFC-0007-memory-knowledge-governed-learning-lifecycle-v1.0.0.md",
            "docs/rfc/RFC-0008-document-artifact-architecture-v1.0.0.md",
        ],
    ),
    (
        "06_ARVECTUM_OS_GOVERNANCE_REFERENCE.md",
        "Arvectum OS Governance Reference",
        [
            "docs/rfc/README.md",
            "docs/governance/DECISION-AUTHORITY-POLICY.md",
        ],
    ),
    (
        "07_ARVECTUM_OS_PRODUCT_CONTRACTS_REFERENCE.md",
        "Arvectum OS Product Contracts Relevant to Initial Arvectum Company Portfolio",
        [
            "docs/contracts/P6-02-FIRST-REAL-PRODUCT-CONTRACT.md",
            "docs/contracts/P6-06-SECOND-REAL-PRODUCT-CONTRACT.md",
        ],
    ),
]


def git(repo: Path, *args: str) -> str:
    return subprocess.check_output(
        ["git", "-C", str(repo), *args], text=True
    ).strip()


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def render_bundle(
    os_repo: Path,
    title: str,
    source_paths: list[str],
    source_commit: str,
    source_commit_time: str,
) -> str:
    out: list[str] = [
        f"# {title}",
        "",
        "Project Source Status: `Convenience Snapshot / Non-Canonical Copy`",
        "Canonical repository: `arvectum/arvectum-os`",
        "Canonical branch sampled: `main`",
        f"Snapshot commit: `{source_commit}`",
        f"Source commit timestamp: `{source_commit_time}`",
        "",
        "> Authority rule: this file is optimized for ChatGPT Project retrieval. "
        "It is not an independent source of truth. If this snapshot conflicts with "
        "the current canonical Arvectum OS repository, applicable Company governance, "
        "or applicable legal/corporate authority, the higher-authority canonical source wins.",
        "",
        "## Included canonical sources",
        "",
    ]

    source_data: list[tuple[str, str, str, str]] = []
    for rel in source_paths:
        path = os_repo / rel
        if not path.is_file():
            raise FileNotFoundError(f"Missing canonical source: {rel}")
        raw = path.read_bytes()
        blob = git(os_repo, "hash-object", rel)
        digest = sha256(raw)
        text = raw.decode("utf-8")
        source_data.append((rel, blob, digest, text))
        out.append(f"- `{rel}` — git blob `{blob}`, SHA-256 `{digest}`")

    for index, (rel, blob, digest, text) in enumerate(source_data, start=1):
        out.extend(
            [
                "",
                "---",
                "",
                f"# Source Document {index}: `{rel}`",
                "",
                f"Canonical git blob: `{blob}`  ",
                f"Content SHA-256: `{digest}`",
                "",
                text.rstrip(),
                "",
            ]
        )

    return "\n".join(out).rstrip() + "\n"


def render_registry(source_commit: str, source_commit_time: str) -> str:
    bundle_rows = "\n".join(
        f"| `{filename}` | `{title}` | Convenience snapshot; uploadable Project Source |"
        for filename, title, _ in GROUPS
    )

    return f"""# Arvectum Company Canonical Sources Registry

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
- commit: `{source_commit}`;
- commit timestamp: `{source_commit_time}`.

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
{bundle_rows}

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
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--os-repo", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--registry",
        type=Path,
        default=Path("docs/CANONICAL-SOURCES.md"),
    )
    args = parser.parse_args()

    os_repo = args.os_repo.resolve()
    output = args.output.resolve()
    registry = args.registry.resolve()

    source_commit = git(os_repo, "rev-parse", "HEAD")
    source_commit_time = git(os_repo, "show", "-s", "--format=%cI", "HEAD")

    output.mkdir(parents=True, exist_ok=True)
    for stale in output.glob("*_ARVECTUM_OS_*.md"):
        stale.unlink()

    for filename, title, source_paths in GROUPS:
        text = render_bundle(
            os_repo,
            title,
            source_paths,
            source_commit,
            source_commit_time,
        )
        (output / filename).write_text(text, encoding="utf-8")

    registry.parent.mkdir(parents=True, exist_ok=True)
    registry.write_text(
        render_registry(source_commit, source_commit_time), encoding="utf-8"
    )

    print(f"Generated {len(GROUPS)} Project Source bundles from {source_commit}")
    print(f"Registry: {registry}")


if __name__ == "__main__":
    main()
