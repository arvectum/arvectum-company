# DECISION-2026-08-20 — AC-003 Canonical Repository Structure Approval

Status: `Approved`
Decision date: `2026-08-20`
Decision time: `09:20 +03:00`
Decision class: `Founding / Material Company Governance Boundary`
Decision authority: `Owner of Arvectum Company`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-003 — Canonical repository structure and artifact map`

## Decision

The Owner explicitly approved the exact proposal identified as:

- artifact: `docs/governance/CANONICAL-REPOSITORY-STRUCTURE.md`;
- proposal status/version: `Proposed 0.9.0`;
- approved proposal blob SHA: `2e6c70848beb3adcf9856a23fae2d26c0e20ff0e`;
- cross-review: `docs/reviews/AC-003-CANONICAL-REPOSITORY-STRUCTURE-CROSS-REVIEW.md`;
- cross-review result: `PASS — material consensus reached` after 7 of maximum 10 iterations.

Owner approval statement:

> Утверждаю AC-003 0.9.0

The proposal is therefore authorized for publication as `Approved 1.0.0` without changing its approved normative substance.

## Scope and authority effect

This decision approves the internal canonical repository structure and artifact-location rules for Arvectum Company.

It confirms, within Company governance scope, that:

- `arvectum/arvectum-company` is the canonical repository for durable, repository-suitable Company governance, planning, portfolio, organizational-model, operating-model and review artifacts;
- the repository is not a universal database or automatic canonical store for legal originals, banking, accounting, personnel, customer/supplier, product-domain or high-frequency runtime state;
- sensitive and restricted payloads are not admitted merely because Git storage is convenient;
- each durable artifact has one canonical home within its declared scope, while references and non-canonical copies must remain identifiable as such;
- Company, Product and Arvectum OS repository responsibilities remain distinct;
- logical directories are created only when a real admitted artifact requires them;
- GitHub `arvectum/arvectum-company` is the current canonical remote and GitVerse remains a non-authoritative resilience/sovereignty mirror unless a later approved decision changes that rule.

This approval does **not** amend the legal charter of ООО «Арвектум», make Git authoritative for facts governed by external legal/accounting/banking/product systems, amend Arvectum OS contracts, create a Product Contract, or authorize storage of secrets or restricted personal/customer data in the public repository.

## Publication actions authorized

1. Publish `docs/governance/CANONICAL-REPOSITORY-STRUCTURE.md` as `Approved 1.0.0`, preserving the exact approved `Proposed 0.9.0` blob reference.
2. Preserve the seven-iteration AC-003 cross-review as review evidence and record this Owner approval as the subsequent binding decision.
3. Update `docs/CANONICAL-SOURCES.md` so AC-003 and this decision are canonical Company governance sources.
4. Update `docs/roadmap/ROADMAP.md` to close `AC-003` as `Complete / PASS` and advance `AC-004 — Initial docs/portfolio/PORTFOLIO.md` to `Current`.
5. Perform read-after-write verification and merge the AC-003 pull request.

## Approval result

`APPROVED — AC-003 1.0.0 AUTHORIZED FOR PUBLICATION`
