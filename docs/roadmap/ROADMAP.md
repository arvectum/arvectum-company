# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.26.0`
Создано: `2026-08-19`
Обновлено: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Текущее каноническое действие: `AC-305 — Inter-product dependency and Arvectum OS Product Contract reconciliation`
Русское название текущего действия: `Сверка межпродуктовых зависимостей и контрактов продуктов с Arvectum OS`

## 1. Модель публикации

Эта редакция `0.26.0` сохраняет полное содержание дорожной карты `0.25.0` по неизменяемой ссылке на git blob и добавляет только закрытие AC-304 и перевод текущего действия на AC-305.

Предыдущая редакция:

- версия: `0.25.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `e6d32d76c710b9956f7902ac838c429f32829358`.

Все ранее определённые этапы M0–M9, принципы приоритизации, границы Company/Product/Arvectum OS, параллельные циклы и конечный AC-901 остаются в силе, если прямо не изменены более новым утверждённым решением.

## 2. Закрытие AC-304

`AC-304 — Разделение: самостоятельный продукт / эталонная реализация / кандидат в модуль / кандидат в возможность Arvectum OS` имеет статус:

`Complete / PASS`.

Утверждённая публикация:

- `docs/portfolio/AC-304-PORTFOLIO-ROLE-CLASSIFICATION-v1.0.0.md` — `Approved 1.0.0`;
- точная проверенная исходная редакция: `docs/portfolio/AC-304-PORTFOLIO-ROLE-CLASSIFICATION.md` — `Proposed 0.9.0`, blob `533ccef1d28bf9a154da9b99dd1c4226c19d166b`;
- перекрёстная проверка: `docs/reviews/AC-304-PORTFOLIO-ROLE-CLASSIFICATION-CROSS-REVIEW.md` — `10 of maximum 10`, PASS, blob `94c70f2d9f168f54e4d4f948b754b22d177872ec`;
- решение собственника: `docs/governance/decisions/DECISION-2026-08-21-AC-304-APPROVAL.md`.

Канонический portfolio map синхронизирован:

- `docs/portfolio/PORTFOLIO.md` — `Active 0.5.0`.

AC-304 установил Company-level role/reuse classification для `PORT-001…PORT-007` без смешения product identity, reference implementation, Company/product-family module hypothesis и Arvectum OS capability lifecycle.

Ключевые результаты:

- `PORT-001`, `PORT-002`, `PORT-003`, `PORT-004` подтверждены как самостоятельные продукты;
- `PORT-001`, `PORT-002`, `PORT-004` подтверждены как `RI-OS-CONSUMER` в пределах существующего evidence;
- `PORT-002`, `PORT-005`, `PORT-006` дают `RI-PRODUCT-FAMILY` evidence, не образуя автоматически общий module;
- `PORT-007` получает только `clarification-only` Company/product-family module-candidate hypothesis для bounded data acquisition/extraction layer;
- новых Company-side кандидатов в Platform Capability Arvectum OS не создано;
- никакой OS lifecycle `Candidate/Incubating/Active` не присвоен Company artifact.

AC-304 не создаёт shared implementation, Product Contract, budget, repository merge, code/data migration, production deployment или customer commitment.

## 3. Phase 3 — управление портфелем и кандидатами в повторно используемые модули

Этап: `M3 — Product/module-candidate portfolio governed as investments`.

Русская смысловая формулировка: **портфель продуктов и кандидатов в модули управляется как набор инвестиций, а не как список репозиториев**.

Текущий план Phase 3:

| ID | Работа | Статус |
|---|---|---|
| `AC-301` | Сверка идентичности, границ и владения продуктами и инициативами портфеля | `Complete / PASS` |
| `AC-302` | Закрепление ответственной организационной позиции за каждым активным продуктом/инициативой | `Complete / PASS` |
| `AC-303` | Границы инвестиций, затрат и рисков; критерии продолжить/изменить/остановить | `Complete / PASS` |
| `AC-304` | Разделение: самостоятельный продукт / эталонная реализация / кандидат в модуль / кандидат в возможность Arvectum OS | `Complete / PASS` |
| `AC-305` | Сверка межпродуктовых зависимостей и контрактов продуктов с Arvectum OS | `Current` |
| `AC-306` | Приоритизация портфеля по капиталу, экономике и вниманию собственника | `Planned` |
| `AC-307` | Итоговая проверка управления портфелем и закрытие M3 | `Planned` |

## 4. Текущее действие — AC-305

### AC-305 — Inter-product dependency and Arvectum OS Product Contract reconciliation

Статус: `Current`.

Цель: сверить фактические зависимости между `PORT-001…PORT-007`, существующие reuse relationships и все применимые Product Contract/extension boundaries Arvectum OS так, чтобы ни Company, ни продукты, ни OS не создавали скрытых cross-repository обязательств.

AC-305 должен как минимум:

- построить явную dependency map между portfolio nodes, отделив runtime/code/data dependency от reference/evidence relationship;
- проверить, не зависят ли продукты от внутренних деталей друг друга или Arvectum OS вне declared contract boundary;
- сверить реальные Product Contracts и external-consumer contracts Arvectum OS с текущими Company/product identities и repository locators;
- исправить stale locator `arutyunoveth/ai-corporation` в P6.02 через применимый Arvectum OS governance path, а не Company-side silent rewrite;
- проверить Product Contract continuity для Tender Agent, Discount Parser и Creative Test Agent;
- определить, где существующий Product Contract действительно отражает текущий product boundary, а где нужен proposal/version refresh;
- проверить, что `RI-OS-CONSUMER` classification AC-304 не превратилась в undeclared platform dependency;
- проверить, что `RI-PRODUCT-FAMILY` evidence не создаёт скрытой shared-library/data coupling;
- оставить AC-306 relative capital/economics prioritization отдельно.

## 5. Границы AC-305

AC-305 сверяет и фиксирует dependency/contract state, но сам по себе не:

- объединяет repositories или продукты;
- переносит код/data/history;
- создаёт новый shared module;
- создаёт новую Platform Capability;
- автоматически меняет Product Contract без применимого OS governance action;
- утверждает budget, spend или priority order;
- расширяет customer commitments;
- меняет legal/IP/data rights.

Если reconciliation требует изменения Arvectum OS canonical artifact, изменение должно проходить в `arvectum/arvectum-os` через его собственный governance path и не может быть создано одной Company-side записью.

## 6. Язык и терминология

Для новых человекочитаемых Company-документов продолжает действовать русскоязычный режим и нормативный глоссарий, установленные действующими Company decisions.

## 7. Напоминание о полномочиях

Дорожная карта координирует работу, но сама по себе не создаёт организационные или юридические полномочия, не утверждает расходы, найм, клиентские обязательства, доступ, промышленное развёртывание и не изменяет Arvectum OS или продуктовые репозитории.
