# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.29.0`
Создано: `2026-08-19`
Обновлено: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Текущее каноническое действие: `AC-401 — Company work/obligation register model`
Русское название текущего действия: `Модель реестра работ и обязательств Компании`

## 1. Модель публикации

Эта редакция `0.29.0` сохраняет полное содержание дорожной карты `0.28.0` по immutable git blob и добавляет утверждение AC-307, закрытие M3 и переход к первому действию M4.

Предыдущая редакция:

- версия: `0.28.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `009f3aa9341c01039cf7b1d217fb246cf51855fe`.

Все ранее определённые этапы M0–M9, Company priority hierarchy, Company/Product/Arvectum OS boundaries, bounded AC-108 evidence loop и конечный AC-901 остаются в силе, если прямо не изменены более новым утверждённым решением.

## 2. Закрытие AC-307

`AC-307 — Итоговая проверка управления портфелем и закрытие M3` имеет статус:

`Complete / PASS`.

Утверждённая publication:

- `docs/portfolio/AC-307-PORTFOLIO-GOVERNANCE-REVIEW-AND-M3-CLOSURE-v1.0.0.md` — `Approved 1.0.0`, blob `ff9a07d8c7161bfdaf3628e1c8e21d2a2d0f4435`;
- exact reviewed proposal: `docs/portfolio/AC-307-PORTFOLIO-GOVERNANCE-REVIEW-AND-M3-CLOSURE.md` — `Proposed 0.9.0`, blob `904b9e5ffa12caeb082b3bf23a89aff251ebe8c4`;
- cross-review: `docs/reviews/AC-307-PORTFOLIO-GOVERNANCE-M3-CLOSURE-CROSS-REVIEW.md` — `10 of maximum 10`, PASS, blob `bc3c4992f12dabaeb155f055373da292278cd791`;
- Owner decision: `docs/governance/decisions/DECISION-2026-08-21-AC-307-APPROVAL-AND-M3-CLOSURE.md`;
- explicit Owner approval wording: `AC-307 утверждаю`.

Канонический portfolio map синхронизирован:

- `docs/portfolio/PORTFOLIO.md` — `Active 0.8.0`, blob `8a77be35225f9c8c4958531e52a4131abda13d0f`.

## 3. Закрытие M3

Этап:

`M3 — Product/module-candidate portfolio governed as investments`

закрыт со статусом:

`Complete / PASS`.

Итог M3:

- `PORT-001…PORT-007` имеют устойчивую Company identity, repository locator и disposition;
- каждый узел имеет primary accountable Position `POS-003 — Portfolio & Product Lead` при сохранении функциональных authority boundaries других Positions и `ROD-*`;
- AC-303 задаёт bounded investment/cost/risk treatment;
- AC-304 отделяет standalone product, reference implementation, Company/product-family module candidate и OS-capability hypothesis;
- AC-305 фиксирует отсутствие обязательной hard inter-product runtime/code/data dependency и текущую Arvectum OS Product Contract correspondence;
- AC-306 задаёт default discretionary capital/economics/Owner-attention order без создания budget/spend authorization;
- AC-307 подтвердил согласованность этих слоёв и явный carry-forward недостающего empirical evidence.

Закрытие M3 не означает profitability, market validation, legal compliance, customer readiness, production readiness, approved reusable production module, Stable Product Contract или Active Arvectum OS capability.

## 4. Phase 3 final status

| ID | Работа | Статус |
|---|---|---|
| `AC-301` | Сверка идентичности, границ и владения продуктами и инициативами портфеля | `Complete / PASS` |
| `AC-302` | Закрепление ответственной организационной позиции за каждым активным продуктом/инициативой | `Complete / PASS` |
| `AC-303` | Границы инвестиций, затрат и рисков; критерии продолжить/изменить/остановить | `Complete / PASS` |
| `AC-304` | Разделение standalone/reference/module/OS-capability candidate roles | `Complete / PASS` |
| `AC-305` | Сверка межпродуктовых зависимостей и контрактов продуктов с Arvectum OS | `Complete / PASS` |
| `AC-306` | Приоритизация портфеля по капиталу, экономике и вниманию собственника | `Complete / PASS` |
| `AC-307` | Итоговая проверка управления портфелем и закрытие M3 | `Complete / PASS` |

## 5. Phase 4 — Owner control and reference observability

Milestone:

`M4 — Owner control and reference-implementation observability established`.

Назначение M4: дать собственнику возможность видеть существенные работы, обязательства, решения, риски, cash/commitments и portfolio state без постоянного восстановления контекста из чатов и отдельных репозиториев, одновременно создавая наблюдаемое evidence того, работает ли AI-native organizational model на практике.

План M4:

| ID | Работа | Статус |
|---|---|---|
| `AC-401` | Company work/obligation register model | `Current` |
| `AC-402` | Decision, approval and escalation register model | `Planned` |
| `AC-403` | Risk, exception and incident register model | `Planned` |
| `AC-404` | Cash, commitment and management reporting baseline | `Planned` |
| `AC-405` | Portfolio/module/priority review cadence | `Planned` |
| `AC-406` | Owner Mission Control / reference-implementation evidence view | `Planned` |
| `AC-407` | Management operating cadence and control review | `Planned` |

Software dashboard не является предпосылкой M4: manual/simpler controls допустимы, если они надёжны, пропорциональны и уменьшают Owner reconstruction burden.

## 6. Текущее действие — AC-401

### AC-401 — Company work/obligation register model

Статус: `Current`.

AC-401 должен определить Company-level модель реестра существенных работ и обязательств, достаточную для operational visibility собственника и последующих AC-402…AC-406, не создавая параллельный бухгалтерский, продуктовый или project-tracker source of truth.

AC-401 должен сохранять уже утверждённые границы:

- реальное обязательство/риск/cash issue имеет приоритет по AC-106 `P0`;
- product implementation/status остаётся в product repository;
- юридические/договорные/финансовые первичные факты остаются в компетентных системах;
- register должен хранить Company-level operating meaning, ownership, status, due/trigger context, evidence/source reference и escalation need без избыточного копирования закрытых данных;
- Owner должен видеть исключения и решения, а не становиться ручным диспетчером каждого low-risk task;
- AC-401 не создаёт dashboard, runtime, automation, spending authority или external commitment автоматически.

## 7. M4 exit direction

M4 должен завершиться только когда собственник может из устойчивого Company control layer видеть как минимум material work, obligations, pending decisions/approvals, risks/exceptions, cash/commitment signals, portfolio priorities и evidence, достаточное для оценки внутренней reference implementation.

Конкретные register semantics, cadence и presentation должны выводиться по AC-401…AC-407, а не проектироваться заранее ради полноты.

## 8. Authority boundary

Roadmap координирует работу, но не создаёт Organizational Authority, budget, legal/corporate authority, customer/vendor commitment, Product Contract, access grant или production approval.

Material capital, external commitment, risk, legal/IP/data и Company↔Product↔Arvectum OS decisions продолжают проходить соответствующий evidence и authority path.