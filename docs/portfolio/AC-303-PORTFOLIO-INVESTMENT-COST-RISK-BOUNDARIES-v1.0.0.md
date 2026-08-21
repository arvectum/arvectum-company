# AC-303 — Границы инвестиций, затрат и рисков; критерии продолжить / изменить / ограничить / предложить остановку

Статус: `Approved`
Версия: `1.0.0`
Утверждено: `2026-08-21`
Опубликовано: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-303 — Investment, cost and risk boundaries; continue/change/stop criteria`
Approval: `docs/governance/decisions/DECISION-2026-08-21-AC-303-APPROVAL.md`
Cross-review: `docs/reviews/AC-303-PORTFOLIO-INVESTMENT-COST-RISK-CROSS-REVIEW.md`
Approved proposal: `Proposed 0.9.0`, blob `e246d06e87b4221ad85718d2aeeb4e3486bf388e`

## 1. Модель утверждённой публикации

Эта публикация фиксирует утверждение точной проверенной редакции AC-303 без переписывания прошедшего cross-review текста задним числом.

Утверждённая исходная редакция:

- файл: `docs/portfolio/AC-303-PORTFOLIO-INVESTMENT-COST-RISK-BOUNDARIES.md`;
- статус исходной редакции: `Proposed 0.9.0`;
- immutable git blob SHA: `e246d06e87b4221ad85718d2aeeb4e3486bf388e`.

Перекрёстная проверка:

- файл: `docs/reviews/AC-303-PORTFOLIO-INVESTMENT-COST-RISK-CROSS-REVIEW.md`;
- iterations: `10 of maximum 10`;
- result: `Complete / PASS for Owner approval`;
- immutable git blob SHA: `f455a8652de57a4062c5d1c32d91b66b627b7e45`.

Решение собственника:

- `docs/governance/decisions/DECISION-2026-08-21-AC-303-APPROVAL.md` — `Approved`.

Нормативное содержание `Proposed 0.9.0` включается в эту публикацию **в полном объёме по указанному immutable blob SHA** и считается утверждённым в пределах заявленного scope.

## 2. Утверждённая модель AC-303

AC-303 `1.0.0` устанавливает binding Company-level portfolio investment/cost/risk governance для `PORT-001…PORT-007`.

Утверждены следующие принципы:

1. investment envelope описывается через допустимый тип и масштаб воздействия, evidence requirements и review triggers, а не через выдуманные финансовые пороги;
2. `Unknown` cost/risk/exposure означает `evidence required`, а не ноль;
3. `continue` означает продолжение только внутри уже одобренного bounded envelope и не создаёт автоматического funding authorization;
4. `change` требует decision-ready proposal при material drift business/commercial/technical/risk/cost boundary;
5. `contain` ограничивает рост, сохраняя обязательства, evidence, reusable assets и необходимую поддержку;
6. `stop / retire candidate` является предложением к отдельному competent decision, а не автоматическим результатом технического статуса;
7. technical `PASS`, repository activity, sunk cost и AI recommendation сами по себе не являются investment decision evidence;
8. POS-003 отвечает за Company-level portfolio stewardship и подготовку evidence, но functional evidence и authority остаются разделёнными;
9. `ROD-01…ROD-09` и особенно применимые `ROD-02`, `ROD-04`, `ROD-06`, `ROD-08`, `ROD-09` остаются hard material-decision boundary;
10. AC-304, AC-305 и AC-306 не предрешаются этой публикацией.

## 3. Утверждённые node-level treatments

| ID | Узел | AC-303 treatment |
|---|---|---|
| `PORT-001` | Arvectum Tender Agent | `continue within bounded product-development/pilot envelope` |
| `PORT-002` | Discount Parser | `continue accepted client/product contour; review material scope/recurring-cost/platformization expansion` |
| `PORT-003` | Arvectum Proxy Launcher | `continue bounded productization on verified track` |
| `PORT-004` | Creative Test Agent | `continue bounded controlled-pilot/productization` |
| `PORT-005` | Tender Small-Volume Calculator | `contain; maintenance/evidence/reuse assessment only until explicit change decision` |
| `PORT-006` | Doors Parser | `contain completed-delivery asset; preserve support/reuse evidence without implicit growth` |
| `PORT-007` | Data Platform | `clarify before investment` |

Эта таблица является Company-level investment treatment, а не заменой product-specific implementation/status sources.

## 4. Cost/risk evidence boundary

Для material decision preparation должны быть видимы, где применимо:

- cash и recurring cost;
- engineering/operational effort;
- Owner attention и bottleneck exposure;
- customer commitments и delivery obligations;
- legal/IP/data/security/privacy/reputational exposure;
- technology sovereignty, dependency и replacement path;
- continuity/recovery implications;
- downside, reversibility и opportunity cost.

Фактические суммы, часы, цены и иные числа должны поступать из надёжного evidence. Эта публикация не создаёт fictional financial baseline.

## 5. Authority и accountability boundary

AC-303 не меняет:

- AC-202 `ROD-01…ROD-09`;
- AC-203 delegated authority model;
- AC-204 Position Registry;
- AC-205 Assignments;
- AC-206 access ceilings;
- AC-207 continuity/replacement rules;
- AC-302 `PORT-* → POS-003` accountability mapping.

Functional accountability сохраняется:

- `POS-002` — customer/commercial;
- `POS-004` — engineering/release;
- `POS-005` — finance/economics/obligations;
- `POS-006` — security/data/dependency/risk/continuity;
- `POS-001` — Company operating integration/escalation;
- `POS-003` — portfolio stewardship, evidence synthesis and decision preparation.

## 6. Company / Product / Arvectum OS / legal boundary

Product repositories остаются canonical для product-specific implementation/status/roadmaps.

Arvectum OS остаётся canonical для OS Product Contracts, platform lifecycle и platform semantics.

Legal/IP/data rights и customer authority не устанавливаются Company portfolio artifact по импликации.

AC-303 не создаёт бюджет, не разрешает расход, найм, договор, SLA, customer promise, production deployment, provisioning доступа или OS governance transition.

## 7. Cross-review и approval evidence

Cross-review использовал все `10 of maximum 10` итераций и завершён с `PASS` без material contradiction в declared scope.

Exact reviewed proposal:

`e246d06e87b4221ad85718d2aeeb4e3486bf388e`.

Owner approval:

`docs/governance/decisions/DECISION-2026-08-21-AC-303-APPROVAL.md`.

## 8. Результат

`AC-303 — Complete / PASS`.

Следующее каноническое действие:

`AC-304 — Standalone product / reference implementation / module candidate / Arvectum OS capability candidate classification`.
