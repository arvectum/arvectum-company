# AC-305 — Сверка межпродуктовых зависимостей и контрактов продуктов с Arvectum OS

Статус: `Proposed`
Версия: `0.9.0`
Создано: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-305 — Inter-product dependency and Arvectum OS Product Contract reconciliation`
Предшествующий Company baseline: `AC-304 — Approved 1.0.0`
Статус утверждения: `Pending explicit Owner approval of the exact reviewed proposal`

## 1. Назначение

AC-305 фиксирует явную карту зависимостей между `PORT-001…PORT-007` и сверяет её с реально существующими Product Contract / integration-contract boundaries Arvectum OS.

Цель — не создать больше связей, а убрать неоднозначность между:

1. фактической runtime/code/data dependency;
2. историческим selective reuse/reference evidence;
3. Company-level reusable-module hypothesis;
4. Arvectum OS governed Product Contract dependency;
5. необязательным external-consumer/integration contour;
6. потенциальной будущей зависимостью.

Наличие reference implementation, общего стека, похожего кода, общего владельца или Product Contract не означает автоматически, что один продукт технически зависит от другого или что Arvectum OS обязателен для всего продукта.

## 2. Authority и evidence baseline

### 2.1 Company

Применимый Company baseline:

- `AC-301 — Approved 1.0.0`: `PORT-001…PORT-007` identities, canonical repository locators и dispositions;
- `AC-302 — Approved 1.0.0`: portfolio stewardship через `POS-003` с сохранением функциональных границ;
- `AC-303 — Approved 1.0.0`: investment/cost/risk treatments;
- `AC-304 — Approved 1.0.0`: standalone/reference/module-candidate/OS-candidate classification;
- `PORTFOLIO.md — Active 0.5.0`: текущая Company portfolio map;
- `ROADMAP.md — Active 0.26.0`: AC-305 является текущим действием.

Company governance остаётся источником Company-level identity, portfolio relation и investment interpretation, но не изменяет Product Contract Arvectum OS.

### 2.2 Arvectum OS

Проверен текущий `main` `arvectum/arvectum-os`:

- Constitution `1.2.0` — Ratified;
- RFC-0001…RFC-0008 — Accepted `1.0.0`;
- CAP-001…CAP-004 — `Incubating / Provisional`;
- Product Contracts / integration contracts, применимые к текущему Company portfolio:
  - `P6.02 — First Real Product Contract` — `Provisional 0.1.0`;
  - `P6.06 — Second Real Product Contract` — `Provisional 0.1.0`;
  - `P8.03 — EIS External-Authority Revalidation Integration Contract` — `Provisional 0.1.0`;
  - `P8.06 — Creative Test Agent external audit/reconstruction Product Contract` — `Provisional 0.1.0`.

Текущий OS roadmap прямо сохраняет эти четыре контракта Provisional и не делает ни один CAP `Active`, ни один Product Contract `Stable`.

### 2.3 Product evidence

Проверены текущие product repositories и наиболее релевантные manifests/docs:

- `PORT-001` — `arvectum/tender-agent`: `README.md`, `pyproject.toml`, `docs/product/tender_app_reuse_audit.md`;
- `PORT-002` — `arvectum/discount-parser`: `README.md`, `pyproject.toml`;
- `PORT-003` — `arvectum/proxy-launcher`: `README.md`;
- `PORT-004` — `arvectum/creative-test-agent`: `README.md`, `pyproject.toml`, `integrations/arvectum_os_p8_06_onboarding.json`;
- `PORT-005` — `arvectum/tender-app`: `README.md`, `pyproject.toml`;
- `PORT-006` — `arvectum/doors_parser`: `README.md`, `requirements.txt`;
- `PORT-007` — `arvectum/data-platform`: repository tree and `README.md`.

## 3. Нормативная типология зависимостей AC-305

AC-305 использует следующие Company-level labels. Они не являются новыми Arvectum OS lifecycle states.

| Label | Значение |
|---|---|
| `HARD_RUNTIME` | продукт не может выполнить заявленный текущий runtime contour без другого продукта/сервиса/контракта |
| `DECLARED_OS_BOUNDARY` | существует явный Provisional Product Contract / integration-contract contour Arvectum OS для ограниченного governed use |
| `OPTIONAL_OS_EXTENSION` | существует явный OS boundary, но core product остаётся независимо работоспособным без него |
| `REFERENCE_REUSE` | доказан исторический/селективный reuse идей, patterns или evidence без текущей runtime dependency |
| `FAMILY_EVIDENCE` | два/несколько продуктов дают evidence для общей продуктовой гипотезы, но общего runtime/shared implementation нет |
| `HYPOTHESIS_ONLY` | будущая зависимость/модуль обсуждается, но текущего обязательства нет |
| `NONE_EVIDENCED` | в проверенном canonical evidence текущая зависимость не установлена |

Одна пара может иметь reference relation и одновременно не иметь runtime dependency.

## 4. Межпродуктовая dependency map

### 4.1 Итоговая матрица

| Откуда | Куда | Класс | Текущий вывод |
|---|---|---|---|
| `PORT-005 Tender Small-Volume Calculator` | `PORT-001 Tender Agent` | `REFERENCE_REUSE` | selective reuse уже произошёл: перенесены архитектурные идеи read-only discovery, normalized result, attachment manifest, skip reasons и manual fallback; монолитного импорта кода/зависимостей нет |
| `PORT-002 Discount Parser` | `PORT-006 Doors Parser` | `FAMILY_EVIDENCE` | оба дают parser/data-acquisition evidence; shared runtime/library/data contract не установлен |
| `PORT-002 Discount Parser` | `PORT-007 Data Platform` | `HYPOTHESIS_ONLY` | возможный будущий consumer/source-family input для bounded data-acquisition module; текущей зависимости нет |
| `PORT-006 Doors Parser` | `PORT-007 Data Platform` | `HYPOTHESIS_ONLY` | возможный будущий consumer/source-family evidence; текущей зависимости нет |
| `PORT-001 Tender Agent` | `PORT-007 Data Platform` | `HYPOTHESIS_ONLY` | никакая current runtime dependency не установлена; shared data layer может появиться только после отдельного consumer/economic/contract decision |
| `PORT-003 Proxy Launcher` | любой другой `PORT-*` | `NONE_EVIDENCED` | продукт остаётся самостоятельным network utility; полезность для connectivity не создаёт hard dependency или Organizational Authority |
| `PORT-004 Creative Test Agent` | любой другой `PORT-*` | `NONE_EVIDENCED` | межпродуктовая runtime/code/data dependency не установлена |
| остальные пары `PORT-*` | друг друга | `NONE_EVIDENCED` | текущего cross-product обязательства в проверенном evidence нет |

### 4.2 Tender App → Tender Agent

Это единственный доказанный direct product-family reuse lineage.

`arvectum/tender-agent/docs/product/tender_app_reuse_audit.md` фиксирует, что из старого `tender-app` переиспользованы архитектурные идеи, а не монолитный код. Не перенесены browser fallback/Playwright, auth/cookies, production install scripts, dashboard/auth infrastructure, scheduler/monitoring, semi-automatic price search и старые connector contours.

Следовательно:

- `PORT-005` не является runtime dependency Tender Agent;
- Tender Agent не обязан поставляться вместе с Tender App;
- закрытие/containment Tender App не ломает текущий Tender Agent runtime по доказанному boundary;
- будущий перенос нового кода требует отдельного product-scope review, а не ссылки на существующий reuse audit.

### 4.3 Parser family

`Discount Parser` и `Doors Parser` действительно имеют общие технические patterns: source adapters/configuration, extraction, normalization, dedup/quality/review concerns.

Но текущие product manifests используют обычные внешние зависимости и не содержат declared package/runtime dependency друг на друга. `Data Platform` пока имеет только bootstrap repository surface и не предоставляет shared runtime contract.

Поэтому AC-305 запрещает трактовать `PORT-002 ↔ PORT-006 ↔ PORT-007` как уже существующий shared parser/data platform.

AC-304 `PORT-007 clarification-only candidate` остаётся только hypothesis until отдельный Company decision установит минимум:

- двух реальных consumers;
- общий bounded contract;
- economic advantage over duplication;
- data/right/security/sovereignty boundary;
- accountable operational ownership;
- migration/rollback/exit path.

## 5. Arvectum OS contract reconciliation

### 5.1 PORT-001 — Arvectum Tender Agent

Current Company identity:

- Company node: `PORT-001 — Arvectum Tender Agent`;
- canonical product repository: `arvectum/tender-agent`.

Applicable OS boundaries:

1. `P6.02 — Provisional 0.1.0`;
2. `P8.03 — Provisional 0.1.0`, supplemental EIS external-authority revalidation contour.

P6.02 Product identity remains:

`product/arvectum-tender-operator@<organization>`.

Exact P6.02 shared capability reliance:

- `CAP-001 — Document & Artifact Governance`;
- `CAP-004 — Audit / Reconstruction Support`.

P8.03 also relies on CAP-001/CAP-004 within its exact bounded EIS revalidation contour.

**Finding AC-305-01 — stale repository locator.**

P6.02 still names `arutyunoveth/ai-corporation`. Approved Company identity governance names `arvectum/tender-agent` as the current implementation repository. The current Tender Agent repository still visibly carries the same procurement/tender-operator implementation lineage: its package is still named `ai-corporation`, its README describes the same controlled pre-bid operator contour, and it contains the Tender App selective-reuse history.

This is a locator/provenance defect, not evidence of a second active Company product.

**Disposition:** prepare an Arvectum OS governed locator reconciliation that preserves:

- current locator `arvectum/tender-agent`;
- historical locator `arutyunoveth/ai-corporation`;
- unchanged P6.02 Product identity;
- unchanged P6.02 Product Contract version `0.1.0` and semantic boundary.

Exact OS proposal prepared by AC-305:

`arvectum/arvectum-os/docs/contracts/P6-02-REPOSITORY-LOCATOR-RECONCILIATION-PROPOSAL.md` — `Proposed 0.9.0`, reviewed blob to be pinned by AC-305 cross-review.

Because the proposal changes only implementation-locator provenance and explicitly leaves the semantic Product Contract boundary untouched, it avoids a false Product Contract version cascade into P8.03. Any semantic boundary change would still require a new Product Contract version.

### 5.2 PORT-002 — Discount Parser

Applicable OS boundary:

- `P6.06 — Provisional 0.1.0`.

Current mapping is aligned:

- OS contract repository: `arvectum/discount-parser`;
- Product identity: `product/arvectum-discount-parser@<organization>`;
- current Company node: `PORT-002 — Discount Parser`;
- current Company repository: `arvectum/discount-parser`.

Exact shared capability reliance:

- **CAP-004 only** — Audit / Reconstruction Support.

P6.06 explicitly omits CAP-001, CAP-002 and CAP-003. Parser source collection, Offer model, normalization, deduplication, classification, scheduler, publication rules and Telegram integration remain product-owned.

**Finding AC-305-02:** contract continuity is aligned; no refresh is required merely because the product continues to evolve inside the same declared bounded contract contour.

A new Product Contract version becomes necessary if the product seeks a different OS capability, operation set, stable/public boundary, organization scope, external-effect scope or other material contract change.

### 5.3 PORT-004 — Creative Test Agent

Applicable OS boundary:

- `P8.06 — Provisional 0.1.0`.

Exact shared capability reliance:

- **CAP-004 only** — read-only Audit / Reconstruction Support.

Consumer identity is an optional extension:

`extension:creative-test-agent-audit-reconstruction@arvectum`.

The current product-side declaration remains present at:

`arvectum/creative-test-agent/integrations/arvectum_os_p8_06_onboarding.json`.

It explicitly declares:

- `enabled_by_default: false`;
- read-only right;
- Authorization + DataGovernance gates;
- no canonical mutation;
- no internal table/import/private stream/undocumented endpoint reliance;
- no Organizational Authority grant;
- independent product operation when the extension is disabled or removed.

**Finding AC-305-03:** AC-304 `RI-OS-CONSUMER` is valid only as an external-consumer reference contour. It must not be restated as “Creative Test Agent core depends on Arvectum OS”.

Contract continuity is aligned; no refresh is needed absent a material boundary change.

### 5.4 PORT-003 / PORT-005 / PORT-006 / PORT-007

No current OS Product Contract is evidenced for:

- `PORT-003 — Arvectum Proxy Launcher`;
- `PORT-005 — Tender Small-Volume Calculator`;
- `PORT-006 — Doors Parser`;
- `PORT-007 — Data Platform`.

AC-305 does not create one.

A future Product Contract is required only when a product actually relies on Arvectum OS capabilities/shared history/canonical state in a way covered by RFC-0004. Product similarity, Company ownership, module-candidate status or future roadmap intent is not sufficient.

## 6. Reconciled OS dependency table

| Company node | OS boundary | Dependency | Nature | AC-305 status |
|---|---|---|---|---|
| `PORT-001 Tender Agent` | P6.02 `0.1.0` | CAP-001 + CAP-004 | `DECLARED_OS_BOUNDARY` for bounded pre-bid governed runs | semantic boundary aligned; repository locator requires OS reconciliation overlay |
| `PORT-001 Tender Agent` | P8.03 `0.1.0` | CAP-001 + CAP-004 | supplemental bounded EIS authority revalidation | aligned; no independent product identity created |
| `PORT-002 Discount Parser` | P6.06 `0.1.0` | CAP-004 only | `DECLARED_OS_BOUNDARY` for controlled publication external-effect reconstruction | aligned |
| `PORT-004 Creative Test Agent` | P8.06 `0.1.0` | CAP-004 only | `OPTIONAL_OS_EXTENSION`, read-only, disabled by default | aligned |
| `PORT-003/005/006/007` | none | none | no current governed OS reliance inferred | aligned |

No current Company product depends on CAP-002 or CAP-003 through the reviewed real-product/external-consumer Product Contracts.

## 7. Hidden-coupling check

### 7.1 Product ↔ product

The inspected current manifests for Tender Agent, Discount Parser, Creative Test Agent, Tender Small-Volume Calculator and Doors Parser show ordinary third-party dependencies rather than direct package references to another `PORT-*` repository.

`Data Platform` has no application implementation manifest in the current repository; it cannot currently be treated as a shared runtime dependency.

Proxy Launcher documentation presents an independently packaged local utility and no approved Company artifact establishes it as a mandatory runtime dependency of another portfolio node.

Result: **no current cross-product hard runtime/package coupling is admitted by AC-305 evidence**.

This does not prove no source file anywhere mentions another project. It establishes the governance conclusion that no current cross-product runtime obligation is evidenced strongly enough to be made canonical.

### 7.2 Product ↔ Arvectum OS

The applicable contracts explicitly reject hidden platform coupling through internal tables, private imports, undocumented endpoints/streams or implicit shared mutable state.

Creative Test Agent's consumer declaration independently repeats this prohibition.

Result: **all admitted OS reliance remains contract-scoped; product-contract possession does not grant authorization or Organizational Authority.**

## 8. Dependency registration rule after AC-305

After approval, a new Company-level cross-product dependency may be treated as real only when the evidence records at least:

1. source product and target product/service;
2. dependency class (`runtime`, `code/package`, `data`, `operational`, `reference/evidence`);
3. exact interface/contract or explicitly documented coupling;
4. accountable Position(s);
5. authority/data/access boundary;
6. failure/continuity/fallback behavior;
7. replacement/removal path;
8. whether the dependency changes cost, customer commitment, sovereignty or risk;
9. canonical source and version/reference.

A reference/evidence relation must never be silently upgraded to runtime dependency.

For OS reliance, RFC-0004 Product Contract requirements remain authoritative and this Company rule cannot replace them.

## 9. Refresh triggers

Re-run dependency/contract reconciliation when any of the following occurs:

- a product starts importing/calling/storing against another product's runtime surface;
- shared datastore/library/service is introduced;
- PORT-007 receives an approved module boundary and real consumers;
- a Product Contract is created, versioned, stabilized, deprecated or retired;
- a CAP dependency is added/removed;
- a repository locator changes;
- a Product Contract consumer identity changes;
- a cross-Organization/data-sharing boundary is proposed;
- a product requires an OS internal implementation detail to function;
- an external commitment makes an optional dependency effectively mandatory.

## 10. Non-effects

AC-305 does not:

- merge repositories or products;
- transfer code, customer data or IP rights;
- create shared implementation;
- create `Data Platform` runtime;
- create an Arvectum OS Platform Capability;
- make a CAP `Active`;
- make a Product Contract `Stable`;
- approve spend, relative portfolio priority or capital allocation;
- authorize production/customer commitments;
- grant access, Authorization or Organizational Authority;
- change legal/IP/data rights;
- widen any Product Contract beyond its current scope.

Relative capital/economics/Owner-attention ranking remains AC-306.

## 11. Proposed AC-305 decision

Subject to cross-review and explicit Owner approval, adopt the following Company-level conclusions:

1. no current hard runtime dependency exists between `PORT-001…PORT-007` on the evidence reviewed;
2. `PORT-005 → PORT-001` is selective `REFERENCE_REUSE`, not runtime coupling;
3. `PORT-002/006` are `FAMILY_EVIDENCE`; `PORT-007` remains `HYPOTHESIS_ONLY` until its separate clarification/admission gate;
4. Tender Agent maps to P6.02 + P8.03 and CAP-001/CAP-004; P6.02's repository locator requires the separately governed OS provenance repair;
5. Discount Parser maps to P6.06 and CAP-004 only; boundary is aligned;
6. Creative Test Agent maps to optional P8.06 CAP-004 extension only; core-product dependency must not be inferred;
7. PORT-003/005/006/007 have no current OS Product Contract;
8. no product currently has reviewed Product Contract reliance on CAP-002 or CAP-003;
9. future cross-product runtime/data/code dependencies require explicit Company registration and boundary evidence;
10. future OS reliance continues to require the applicable Arvectum OS Product Contract path.

## 12. Approval boundary and handoff

This document remains `Proposed 0.9.0` until explicit Owner approval of the exact cross-reviewed blob.

The OS locator reconciliation is a separate Arvectum OS governance subject even though it is prepared by AC-305. Company approval alone must not be treated as silent OS approval.

For full AC-305 closure the Owner should explicitly approve both:

1. the exact reviewed Company AC-305 proposal; and
2. the exact reviewed `P6-02-REPOSITORY-LOCATOR-RECONCILIATION-PROPOSAL.md` in `arvectum/arvectum-os`.

After both approvals:

- publish AC-305 as Approved `1.0.0`;
- publish the OS locator reconciliation with its own approval evidence;
- update `PORTFOLIO.md` with the reconciled dependency/Product Contract overlay;
- update `ROADMAP.md`, mark AC-305 `Complete / PASS` and advance current action to `AC-306 — Приоритизация портфеля по капиталу, экономике и вниманию собственника`.