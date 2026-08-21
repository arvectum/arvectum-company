# Решение собственника — утверждение AC-305

Статус: `Approved`
Дата: `2026-08-21`
Владелец решения: собственник ООО «Арвектум»
Репозиторий: `arvectum/arvectum-company`
Связанный Arvectum OS approval: `arvectum/arvectum-os/docs/governance/decisions/DECISION-2026-08-21-P6-02-REPOSITORY-LOCATOR-RECONCILIATION-APPROVAL.md`

## 1. Явное решение

Собственник явно утвердил AC-305 и связанное Arvectum OS reconciliation формулировкой:

> `AC-305 и P6.02 repository locator reconciliation в Arvectum OS утверждаю`

Company-часть утверждения относится к точной проверенной редакции:

- документ: `docs/portfolio/AC-305-CROSS-PRODUCT-DEPENDENCY-AND-OS-CONTRACT-RECONCILIATION.md`;
- статус: `Proposed 0.9.0`;
- immutable git blob SHA: `c27973c48b7bb5306e36f71d0f1007fc41896de9`;
- cross-review: `docs/reviews/AC-305-CROSS-PRODUCT-DEPENDENCY-AND-OS-CONTRACT-CROSS-REVIEW.md`;
- результат: `7 of maximum 7`, `Complete / PASS for dual Owner approval`;
- immutable git blob SHA cross-review: `369c42f8066ac8a10d3b00a0afd2fc034b8c7fe3`.

Связанная OS-часть утверждения относится к точной проверенной редакции:

- repository: `arvectum/arvectum-os`;
- document: `docs/contracts/P6-02-REPOSITORY-LOCATOR-RECONCILIATION-PROPOSAL.md`;
- status: `Proposed 0.9.0`;
- immutable git blob SHA: `95f32a2625a3df2c18615021aa2ca46f83faa946`.

## 2. Утверждённый dependency baseline

Собственник утверждает, что в текущем evidence baseline:

- между `PORT-001…PORT-007` не установлено ни одной обязательной hard runtime/code/data dependency;
- selective reuse, reference implementation и common-stack similarity не считаются hard dependency;
- `PORT-005 → PORT-001` является только selective procurement-family reuse/evidence relation;
- `PORT-002`, `PORT-006` и `PORT-007` не образуют автоматически общий parser engine, shared runtime, datastore или platform;
- `PORT-007` остаётся `clarification-only` Company/product-family module hypothesis без разрешения material build или shared operational reliance;
- `PORT-003` не становится скрытой инфраструктурной зависимостью Company/OS/product portfolio.

## 3. Утверждённый Arvectum OS contract map

| Portfolio node | Governed OS boundary | Exact current OS dependency |
|---|---|---|
| `PORT-001 — Arvectum Tender Agent` | `P6.02` + supplemental `P8.03` | `CAP-001 + CAP-004` в точных bounded scopes |
| `PORT-002 — Discount Parser` | `P6.06` | `CAP-004 only` |
| `PORT-004 — Creative Test Agent` | `P8.06` optional external extension | `CAP-004 only`, optional/disabled-by-default product extension |
| `PORT-003` | none | none inferred |
| `PORT-005` | none | none inferred |
| `PORT-006` | none | none inferred |
| `PORT-007` | none | none inferred |

`RI-OS-CONSUMER` остаётся evidence/reuse classification и не означает обязательность Arvectum OS для всего core-product, если конкретный Product Contract этого не устанавливает.

## 4. P6.02 locator reconciliation

Утверждено, что stale P6.02 repository locator:

- historical/predecessor locator: `arutyunoveth/ai-corporation`;
- current implementation repository locator: `arvectum/tender-agent`;
- Company portfolio correspondence: `PORT-001 — Arvectum Tender Agent`.

Это locator/provenance reconciliation, а не изменение Product Contract semantic boundary.

Не изменяются:

- Product identity `product/arvectum-tender-operator@<organization>`;
- P6.02 Product Contract subject/version identities;
- lifecycle `Provisional 0.1.0`;
- compatibility line `restricted-paid-pilot/44fz-prebid-v1`;
- CAP-001/CAP-004 dependency set;
- human-review/external-action restrictions;
- Organization/authority/security/data boundary;
- P8.03 continuity.

Исторический P6.02 artifact не переписывается задним числом; current locator разрешается через отдельную утверждённую Arvectum OS reconciliation publication.

## 5. Сохранённые границы

Утверждение AC-305 не:

- объединяет repositories или product identities;
- переносит code/data/history;
- создаёт shared library/service/runtime;
- создаёт новую Platform Capability;
- делает Product Contract `Stable` или capability `Active`;
- создаёт funding/priority order;
- расширяет customer commitments, legal/IP/data rights или Organizational Authority;
- отменяет AC-301…AC-304;
- выполняет AC-306.

## 6. Следующий этап

После публикации AC-305 как Approved и синхронизации `PORTFOLIO.md` и `ROADMAP.md` следующим Company action становится:

`AC-306 — Приоритизация портфеля по капиталу, экономике и вниманию собственника`.

## 7. Граница решения

Это решение является Company-internal governance approval. Связанное изменение canonical interpretation внутри Arvectum OS фиксируется отдельным Arvectum OS Owner decision и Approved reconciliation artifact; Company decision сам по себе не изменяет OS canonical sources.
