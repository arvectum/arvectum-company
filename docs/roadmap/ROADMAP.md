# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.25.0`
Создано: `2026-08-19`
Обновлено: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Текущее каноническое действие: `AC-304 — Standalone product / reference implementation / module candidate / Arvectum OS capability candidate classification`
Русское название текущего действия: `Разделение: самостоятельный продукт / эталонная реализация / кандидат в модуль / кандидат в возможность Arvectum OS`

## 1. Модель публикации

Эта редакция `0.25.0` сохраняет полное содержание дорожной карты `0.24.0` по неизменяемой ссылке на git blob и добавляет только закрытие AC-303 и перевод текущего действия на AC-304.

Предыдущая редакция:

- версия: `0.24.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `d5e9d481b76365179e6f18708e8b892740e2813b`.

Все ранее определённые этапы M0–M9, принципы приоритизации, границы Company/Product/Arvectum OS, параллельные циклы и конечный AC-901 остаются в силе, если прямо не изменены более новым утверждённым решением.

## 2. Закрытие AC-303

`AC-303 — Границы инвестиций, затрат и рисков; критерии продолжить/изменить/остановить` имеет статус:

`Complete / PASS`.

Утверждённая публикация:

- `docs/portfolio/AC-303-PORTFOLIO-INVESTMENT-COST-RISK-BOUNDARIES-v1.0.0.md` — `Approved 1.0.0`;
- точная проверенная исходная редакция: `docs/portfolio/AC-303-PORTFOLIO-INVESTMENT-COST-RISK-BOUNDARIES.md` — `Proposed 0.9.0`, blob `e246d06e87b4221ad85718d2aeeb4e3486bf388e`;
- перекрёстная проверка: `docs/reviews/AC-303-PORTFOLIO-INVESTMENT-COST-RISK-CROSS-REVIEW.md` — `10 of maximum 10`, PASS, blob `f455a8652de57a4062c5d1c32d91b66b627b7e45`;
- решение собственника: `docs/governance/decisions/DECISION-2026-08-21-AC-303-APPROVAL.md`.

Канонический portfolio map синхронизирован:

- `docs/portfolio/PORTFOLIO.md` — `Active 0.4.0`.

AC-303 установил Company-level bounded investment/cost/risk treatment для всех `PORT-001…PORT-007`, evidence requirements и review semantics `continue / change / contain / stop-retire candidate`, сохранив `ROD-*`, функциональную accountability Positions, product-specific sources и границы Company/Product/Arvectum OS.

AC-303 не создаёт бюджет, не утверждает конкретный расход, не заменяет product implementation truth и не делает technical PASS инвестиционным решением.

## 3. Phase 3 — управление портфелем и кандидатами в повторно используемые модули

Этап: `M3 — Product/module-candidate portfolio governed as investments`.

Русская смысловая формулировка: **портфель продуктов и кандидатов в модули управляется как набор инвестиций, а не как список репозиториев**.

Текущий план Phase 3:

| ID | Работа | Статус |
|---|---|---|
| `AC-301` | Сверка идентичности, границ и владения продуктами и инициативами портфеля | `Complete / PASS` |
| `AC-302` | Закрепление ответственной организационной позиции за каждым активным продуктом/инициативой | `Complete / PASS` |
| `AC-303` | Границы инвестиций, затрат и рисков; критерии продолжить/изменить/остановить | `Complete / PASS` |
| `AC-304` | Разделение: самостоятельный продукт / эталонная реализация / кандидат в модуль / кандидат в возможность Arvectum OS | `Current` |
| `AC-305` | Сверка межпродуктовых зависимостей и контрактов продуктов с Arvectum OS | `Planned` |
| `AC-306` | Приоритизация портфеля по капиталу, экономике и вниманию собственника | `Planned` |
| `AC-307` | Итоговая проверка управления портфелем и закрытие M3 | `Planned` |

## 4. Текущее действие — AC-304

### AC-304 — Standalone product / reference implementation / module candidate / Arvectum OS capability candidate classification

Статус: `Current`.

Цель: для каждого `PORT-001…PORT-007` определить его текущую Company-level portfolio role без смешения четырёх разных понятий:

- самостоятельный продукт;
- эталонная/референсная реализация;
- кандидат в повторно используемый Company/product-family module;
- кандидат в domain-neutral Platform Capability Arvectum OS.

AC-304 должен как минимум:

- опираться на Approved AC-301 identities/dispositions, AC-302 accountability и AC-303 investment treatment;
- не считать repository reuse доказательством module status;
- не считать сходство функций или общего кода достаточным для platform promotion;
- не превращать Company-level classification в Product Contract, Arvectum OS capability lifecycle decision или product implementation change;
- сохранять правило, что reusable Company/product-family semantics и domain-neutral Arvectum OS capabilities — разные architectural ownership scopes;
- потребовать evidence business/reuse/consumer/control need для module/reference classification;
- оставить AC-305 точную dependency/Product Contract reconciliation и AC-306 относительную capital/economics priority.

## 5. Границы AC-304

AC-304 классифицирует portfolio role и promotion/reuse hypothesis, но сам по себе не:

- переносит код или schemas между репозиториями;
- создаёт shared library/service;
- изменяет Product Contract Arvectum OS;
- продвигает capability в `Candidate`, `Incubating` или `Active` без применимого OS governance path;
- объединяет продукты;
- создаёт budget или priority order;
- меняет юридические/IP/data права.

## 6. Язык и терминология

Для новых человекочитаемых Company-документов продолжает действовать русскоязычный режим и нормативный глоссарий, установленные действующими Company decisions.

## 7. Напоминание о полномочиях

Дорожная карта координирует работу, но сама по себе не создаёт организационные или юридические полномочия, не утверждает расходы, найм, клиентские обязательства, доступ, промышленное развёртывание и не изменяет Arvectum OS или продуктовые репозитории.
