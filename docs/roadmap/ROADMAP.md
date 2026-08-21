# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.24.0`
Создано: `2026-08-19`
Обновлено: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Текущее каноническое действие: `AC-303 — Investment, cost and risk boundaries; continue/change/stop criteria`
Русское название текущего действия: `Границы инвестиций, затрат и рисков; критерии продолжить/изменить/остановить`

## 1. Модель публикации

Эта редакция `0.24.0` сохраняет полное содержание дорожной карты `0.23.0` по неизменяемой ссылке на git blob и добавляет только закрытие AC-302 и перевод текущего действия на AC-303.

Предыдущая редакция:

- версия: `0.23.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `158497c1807af4528fdb7f3bc95189e71b13c4c5`.

Все ранее определённые этапы M0–M9, принципы приоритизации, границы Company/Product/Arvectum OS, параллельные циклы и конечный AC-901 остаются в силе, если прямо не изменены более новым утверждённым решением.

## 2. Закрытие AC-302

`AC-302 — Закрепление ответственной организационной позиции за каждым активным продуктом/инициативой` имеет статус:

`Complete / PASS`.

Утверждённая публикация:

- `docs/portfolio/AC-302-PORTFOLIO-ACCOUNTABLE-POSITION-MAPPING-v1.0.0.md` — `Approved 1.0.0`;
- точная проверенная исходная редакция: `docs/portfolio/AC-302-PORTFOLIO-ACCOUNTABLE-POSITION-MAPPING.md` — `Proposed 0.9.0`, blob `29bec89402118ddfc061501b8b25f5c0000d65a4`;
- перекрёстная проверка: `docs/reviews/AC-302-PORTFOLIO-ACCOUNTABLE-POSITION-CROSS-REVIEW.md` — `10 of maximum 10`, PASS;
- решение собственника: `docs/governance/decisions/DECISION-2026-08-21-AC-302-APPROVAL.md`.

Канонический portfolio map синхронизирован:

- `docs/portfolio/PORTFOLIO.md` — `Active 0.3.0`.

AC-302 закрепил для всех семи текущих `PORT-001…PORT-007` primary Company-level accountable Position:

`POS-003 — Portfolio & Product Lead`.

Это Company-level portfolio stewardship relation, а не end-to-end ownership всех продуктовых функций. Functional accountability POS-001/POS-002/POS-004/POS-005/POS-006, AC-202 Reserved Owner Decisions, AC-205 Assignments, AC-206 access и AC-207 continuity остаются неизменными.

## 3. Phase 3 — управление портфелем и кандидатами в повторно используемые модули

Этап: `M3 — Product/module-candidate portfolio governed as investments`.

Русская смысловая формулировка: **портфель продуктов и кандидатов в модули управляется как набор инвестиций, а не как список репозиториев**.

Текущий план Phase 3:

| ID | Работа | Статус |
|---|---|---|
| `AC-301` | Сверка идентичности, границ и владения продуктами и инициативами портфеля | `Complete / PASS` |
| `AC-302` | Закрепление ответственной организационной позиции за каждым активным продуктом/инициативой | `Complete / PASS` |
| `AC-303` | Границы инвестиций, затрат и рисков; критерии продолжить/изменить/остановить | `Current` |
| `AC-304` | Разделение: самостоятельный продукт / эталонная реализация / кандидат в модуль / кандидат в возможность Arvectum OS | `Planned` |
| `AC-305` | Сверка межпродуктовых зависимостей и контрактов продуктов с Arvectum OS | `Planned` |
| `AC-306` | Приоритизация портфеля по капиталу, экономике и вниманию собственника | `Planned` |
| `AC-307` | Итоговая проверка управления портфелем и закрытие M3 | `Planned` |

## 4. Текущее действие — AC-303

### AC-303 — Границы инвестиций, затрат и рисков; критерии продолжить/изменить/остановить

Статус: `Current`.

Цель: для каждого `PORT-001…PORT-007` определить Company-level investment envelope и evidence-based критерии, по которым узел может продолжаться, требовать изменения/containment или быть предложен к остановке, не смешивая эти правила с product implementation truth, юридическими правами или Arvectum OS lifecycle.

AC-303 должен как минимум:

- определить применимые категории затрат, recurring cost, capital/time/Owner-attention exposure и downside для каждого узла;
- установить пропорциональные risk/cost boundaries без выдумывания неподтверждённых финансовых чисел;
- определить evidence requirements и review triggers для `continue / change / contain / stop/retire candidate`;
- сохранить `ROD-02`, `ROD-04`, `ROD-06`, `ROD-08`, `ROD-09` и иные применимые Reserved Owner Decisions;
- отделить investment decision от technical PASS, repository activity, sunk cost и AI recommendation;
- учитывать current AC-301 dispositions и AC-302 accountability mapping, не меняя их молча;
- не выполнять AC-304 module classification, AC-305 OS/dependency reconciliation или AC-306 portfolio prioritization заранее.

## 5. Границы AC-303

AC-303 не создаёт бюджет автоматически, не утверждает конкретный расход без отдельного applicable authority action, не меняет юридические полномочия, product implementation, customer commitments, Product Contracts Arvectum OS или Position/Assignment/access model.

## 6. Язык и терминология

Для новых человекочитаемых Company-документов продолжает действовать русскоязычный режим и нормативный глоссарий, установленные действующими Company decisions.

## 7. Напоминание о полномочиях

Дорожная карта координирует работу, но сама по себе не создаёт организационные или юридические полномочия, не утверждает расходы, найм, клиентские обязательства, доступ, промышленное развёртывание и не изменяет Arvectum OS или продуктовые репозитории.
