# AC-302 — Закрепление ответственной организационной позиции за продуктами и инициативами портфеля

Статус: `Approved`
Версия: `1.0.0`
Дата утверждения: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-302 — Assign accountable Position to each active product/initiative`

## 1. Модель утверждённой публикации

Эта публикация фиксирует утверждение точной проверенной редакции AC-302 без переписывания прошедшего cross-review текста задним числом.

Утверждённая исходная редакция:

- файл: `docs/portfolio/AC-302-PORTFOLIO-ACCOUNTABLE-POSITION-MAPPING.md`;
- статус исходной редакции: `Proposed 0.9.0`;
- immutable git blob SHA: `29bec89402118ddfc061501b8b25f5c0000d65a4`.

Перекрёстная проверка:

- файл: `docs/reviews/AC-302-PORTFOLIO-ACCOUNTABLE-POSITION-CROSS-REVIEW.md`;
- iterations: `10 of maximum 10`;
- result: `Complete / PASS for Owner approval`;
- reviewed blob: `29bec89402118ddfc061501b8b25f5c0000d65a4`.

Решение собственника:

- `docs/governance/decisions/DECISION-2026-08-21-AC-302-APPROVAL.md` — `Approved`;
- явная формулировка: `AC-302 утверждаю.`

Полное нормативное содержание AC-302 `1.0.0` — это reviewed proposal `0.9.0`, включённый в эту Approved publication по неизменяемой ссылке на git blob.

## 2. Утверждённая accountability map

Для всех семи текущих Company portfolio nodes primary accountable Position устанавливается как:

`POS-003 — Portfolio & Product Lead`.

| Portfolio ID | Узел | AC-301 disposition | Primary accountable Position |
|---|---|---|---|
| `PORT-001` | Arvectum Tender Agent | `continue` | `POS-003 — Portfolio & Product Lead` |
| `PORT-002` | Discount Parser | `continue` | `POS-003 — Portfolio & Product Lead` |
| `PORT-003` | Arvectum Proxy Launcher | `continue` | `POS-003 — Portfolio & Product Lead` |
| `PORT-004` | Creative Test Agent | `continue` | `POS-003 — Portfolio & Product Lead` |
| `PORT-005` | Tender Small-Volume Calculator | `contain` | `POS-003 — Portfolio & Product Lead` |
| `PORT-006` | Doors Parser | `contain` | `POS-003 — Portfolio & Product Lead` |
| `PORT-007` | Data Platform | `clarify` | `POS-003 — Portfolio & Product Lead` |

Primary accountability относится к Company-level stewardship узла, а не к полному функциональному владению продуктом.

## 3. Сохранённые функциональные и authority boundaries

AC-302 сохраняет действующую M2 модель:

- `POS-002 — Commercial & Customer Lead` — commercial/customer accountability;
- `POS-004 — Engineering & Release Lead` — engineering/release accountability;
- `POS-005 — Finance & Obligation Control Lead` — finance/economics/obligation evidence;
- `POS-006 — Security, Risk & Continuity Lead` — security/data/dependency/risk/continuity assurance;
- `POS-001 — Company Executive` — Company operating integration, decision routing and escalation.

`POS-003` остаётся в initial authority ceiling `AM-0`, `AM-1`, `AM-2`. `ROD-01…ROD-09` остаются Reserved Owner Decisions. Assignment, access and continuity boundaries остаются AC-205, AC-206 и AC-207 соответственно.

## 4. Не создаваемые эффекты

Approval AC-302 не:

- создаёт product-specific Positions;
- назначает нового Principal;
- расширяет access/credentials;
- утверждает investment limits или budget;
- принимает continue/change/stop material decision;
- классифицирует reusable module/reference implementation/OS capability;
- создаёт или меняет Product Contract;
- переносит product implementation semantics в Company repository;
- создаёт legal/IP ownership или customer authority.

Contained и clarify nodes получают accountable custodian/question owner, но не growth mandate.

## 5. Approval result

`AC-302 — Assign accountable Position to each active product/initiative` является `Complete / PASS` и binding Company portfolio-governance state в пределах заявленного scope.

Следующее каноническое действие после синхронизации дорожной карты:

`AC-303 — Investment, cost and risk boundaries; continue/change/stop criteria`.
