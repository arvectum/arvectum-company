# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.23.0`
Создано: `2026-08-19`
Обновлено: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Текущее каноническое действие: `AC-302 — Assign accountable Position to each active product/initiative`
Русское название текущего действия: `Закрепление ответственной организационной позиции за каждым активным продуктом/инициативой`

## 1. Модель публикации

Эта редакция `0.23.0` сохраняет полное содержание дорожной карты `0.22.0` по неизменяемой ссылке на git blob и добавляет только закрытие AC-301 и перевод текущего действия на AC-302.

Предыдущая редакция:

- версия: `0.22.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `261c67b4223ce66f5b11b3caa0708d5da29715c6`.

Все ранее определённые этапы M0–M9, принципы приоритизации, границы Company/Product/Arvectum OS, параллельные циклы и конечный AC-901 остаются в силе, если прямо не изменены более новым утверждённым решением.

## 2. Закрытие AC-301

`AC-301 — Сверка идентичности, границ и владения продуктами и инициативами портфеля` имеет статус:

`Complete / PASS`.

Утверждённая публикация:

- `docs/portfolio/AC-301-PORTFOLIO-IDENTITY-BOUNDARY-OWNERSHIP-RECONCILIATION-v1.0.0.md` — `Approved 1.0.0`;
- точная проверенная исходная редакция: `docs/portfolio/AC-301-PORTFOLIO-IDENTITY-BOUNDARY-OWNERSHIP-RECONCILIATION.md` — `Proposed 0.9.0`, blob `146b5868a21c09cf20b633e309e587b7a631ad32`;
- перекрёстная проверка: `docs/reviews/AC-301-PORTFOLIO-IDENTITY-BOUNDARY-OWNERSHIP-CROSS-REVIEW.md` — `10 of maximum 10`, PASS;
- решение собственника: `docs/governance/decisions/DECISION-2026-08-21-AC-301-APPROVAL.md`.

Канонический portfolio map синхронизирован:

- `docs/portfolio/PORTFOLIO.md` — `Active 0.2.0`.

AC-301 закрепил семь устойчивых Company-level identities `PORT-001…PORT-007`, отделил Product Identity от repository locator и legal/IP ownership, сохранил Company/Product/Arvectum OS boundaries и не допустил молчаливого объединения procurement/parser/data узлов.

Текущие bounded dispositions:

| ID | Узел | Disposition |
|---|---|---|
| `PORT-001` | Arvectum Tender Agent | `continue` |
| `PORT-002` | Discount Parser | `continue` |
| `PORT-003` | Arvectum Proxy Launcher | `continue` |
| `PORT-004` | Creative Test Agent | `continue` |
| `PORT-005` | Tender Small-Volume Calculator | `contain` |
| `PORT-006` | Doors Parser | `contain` |
| `PORT-007` | Data Platform | `clarify` |

Эти dispositions не являются бюджетными, инвестиционными или stop/continue решениями AC-303/AC-306.

## 3. Phase 3 — управление портфелем и кандидатами в повторно используемые модули

Этап: `M3 — Product/module-candidate portfolio governed as investments`.

Русская смысловая формулировка: **портфель продуктов и кандидатов в модули управляется как набор инвестиций, а не как список репозиториев**.

Текущий план Phase 3:

| ID | Работа | Статус |
|---|---|---|
| `AC-301` | Сверка идентичности, границ и владения продуктами и инициативами портфеля | `Complete / PASS` |
| `AC-302` | Закрепление ответственной организационной позиции за каждым активным продуктом/инициативой | `Current` |
| `AC-303` | Границы инвестиций, затрат и рисков; критерии продолжить/изменить/остановить | `Planned` |
| `AC-304` | Разделение: самостоятельный продукт / эталонная реализация / кандидат в модуль / кандидат в возможность Arvectum OS | `Planned` |
| `AC-305` | Сверка межпродуктовых зависимостей и контрактов продуктов с Arvectum OS | `Planned` |
| `AC-306` | Приоритизация портфеля по капиталу, экономике и вниманию собственника | `Planned` |
| `AC-307` | Итоговая проверка управления портфелем и закрытие M3 | `Planned` |

## 4. Текущее действие — AC-302

### AC-302 — Закрепление ответственной организационной позиции за каждым активным продуктом/инициативой

Статус: `Current`.

Цель: связать утверждённые AC-301 portfolio identities с уже утверждённой M2 Position model так, чтобы каждый активный или materially retained узел имел однозначную организационную accountability без превращения текущего исполнителя, GitHub ownership или технического доступа в источник authority.

AC-302 должен как минимум:

- определить accountable Position для каждого `PORT-001…PORT-007` либо явно обосновать, почему для contained/clarify node допустима временная portfolio-level accountability без отдельной постоянной product Position;
- проверить соответствие существующему `INITIAL-POSITION-REGISTRY-v1.0.0.md` и approved M2 authority model;
- не создавать новый Position только ради симметрии портфеля или по принципу «один продукт — одна должность»;
- отделить accountable Position от текущего Principal/Assignment/runtime;
- сохранить Reserved Owner Decisions и утверждённые delegation boundaries;
- определить escalation path для продукта там, где решение выходит за authority соответствующей Position;
- не утверждать бюджет, инвестиционный лимит, reusable-module classification или OS dependency, которые относятся к AC-303…AC-305;
- зафиксировать любые реальные gaps в Position model как отдельный change proposal, а не молчаливо расширять существующие Position scopes.

## 5. Границы AC-302

AC-302 не изменяет юридические полномочия ООО, Product Contracts Arvectum OS, legal/IP ownership, бюджеты, SLA, клиентские обязательства или product implementation.

Accountability должна следовать business function и authority boundary, а не repository ownership или имени продукта.

## 6. Язык и терминология

Для новых человекочитаемых Company-документов продолжает действовать русскоязычный режим и нормативный глоссарий, установленные более ранними действующими решениями, включёнными в сохранённую редакцию `0.22.0`.

## 7. Напоминание о полномочиях

Дорожная карта координирует работу, но сама по себе не создаёт организационные или юридические полномочия, не утверждает расходы, найм, клиентские обязательства, доступ, промышленное развёртывание и не изменяет Arvectum OS или продуктовые репозитории.
