# Решение собственника — утверждение AC-303

Статус: `Approved`
Дата: `2026-08-21`
Владелец решения: собственник ООО «Арвектум»
Репозиторий: `arvectum/arvectum-company`

## 1. Явное решение

Собственник явно утвердил AC-303 формулировкой:

> `AC-303 утверждаю`

Утверждение относится к точной проверенной редакции:

- документ: `docs/portfolio/AC-303-PORTFOLIO-INVESTMENT-COST-RISK-BOUNDARIES.md`;
- статус: `Proposed 0.9.0`;
- git blob SHA: `e246d06e87b4221ad85718d2aeeb4e3486bf388e`;
- перекрёстная проверка: `docs/reviews/AC-303-PORTFOLIO-INVESTMENT-COST-RISK-CROSS-REVIEW.md`;
- результат проверки: `10 of maximum 10`, `Complete / PASS for Owner approval`;
- git blob SHA cross-review: `f455a8652de57a4062c5d1c32d91b66b627b7e45`.

Перед фиксацией решения proposal и cross-review были повторно сверены в canonical `main`; проверенная редакция и review связываются указанными immutable blob SHA.

## 2. Утверждённый результат

Собственник утверждает Company-level модель AC-303 для `PORT-001…PORT-007`, включающую:

- bounded investment treatment для каждого portfolio node;
- обязательную видимость cash/recurring cost, engineering/operational effort, Owner-attention exposure, customer obligations, security/data/legal/IP/dependency/sovereignty/continuity risk и opportunity cost там, где они применимы;
- правило `Unknown = evidence required, not zero`;
- evidence-based review semantics `continue / change / contain / stop-retire candidate`;
- review triggers при выходе за ранее одобренный envelope, появлении materially new cost/risk/external effect или недостаточности evidence;
- отделение investment decision от technical `PASS`, repository activity, sunk cost и AI recommendation.

## 3. Утверждённые node-level treatments

### `PORT-001 — Arvectum Tender Agent`

`continue within bounded product-development/pilot envelope`.

Material capital expansion, new external commitments, production/customer-risk expansion, materially new dependencies or cross-repository/OS commitments требуют применимого evidence и Owner gate.

### `PORT-002 — Discount Parser`

`continue to complete/maintain accepted client/product contour`.

Новые recurring cost, существенное расширение scope, превращение решения в generic shared product/module/platform или новые material commitments требуют review.

### `PORT-003 — Arvectum Proxy Launcher`

`continue bounded productization on the verified track`.

Material signing, dependency/sovereignty, platform expansion, commercial/market commitments и иные существенные exposure остаются отдельными gated decisions.

### `PORT-004 — Creative Test Agent`

`continue bounded controlled-pilot/productization`.

Material customer, data, operational, deployment или recurring-cost expansion требует review; controlled-pilot status не равен production/business-readiness approval.

### `PORT-005 — Tender Small-Volume Calculator`

`contain`.

Разрешены только bounded maintenance, evidence preservation, reuse/merge assessment и обязательные corrective actions; growth investment или возвращение в active product track требует отдельного review/decision.

### `PORT-006 — Doors Parser`

`contain`.

Сохраняются completed-delivery evidence, support obligations и reuse evidence; новый product-growth contour не возникает по импликации.

### `PORT-007 — Data Platform`

`clarify before investment`.

До определения business problem, consumers, boundary, strategic/economic hypothesis, dependencies и risk/cost evidence инициатива не получает автоматического build/funding/product/module/Arvectum OS status.

## 4. Authority и Reserved Owner Decisions

AC-303 не делегирует final authority по material investment решениям.

Остаются применимыми, в частности:

- `ROD-02` — Capital allocation and material financial exposure;
- `ROD-04` — Major portfolio, initiative and investment decisions;
- `ROD-06` — Risk appetite and material exception acceptance;
- `ROD-08` — Core IP, critical dependency and technology-sovereignty exceptions;
- `ROD-09` — Material Company↔Product↔Arvectum OS boundary and cross-repository commitments;
- и иные `ROD-*`, если фактическое решение попадает в их scope.

`POS-003` сохраняет Company-level stewardship/evidence-preparation accountability, но не получает автоматическую authority утверждать material spending, риск, customer commitment, hiring, production deployment, OS lifecycle или cross-repository obligation.

Functional evidence остаётся распределённой по POS-002/POS-004/POS-005/POS-006, а POS-001 сохраняет Company operating integration/escalation boundary.

## 5. Сохранённые границы

Утверждение AC-303:

- не создаёт денежный бюджет и не разрешает конкретный расход;
- не изменяет юридические или корпоративные полномочия;
- не меняет AC-301 portfolio identities/dispositions молча;
- не меняет AC-302 accountable-Position mapping;
- не меняет AC-205 Assignments, AC-206 access или AC-207 continuity;
- не выполняет AC-304 module/reference/OS-capability classification;
- не выполняет AC-305 inter-product/Arvectum OS Product Contract reconciliation;
- не выполняет AC-306 relative portfolio prioritization;
- не изменяет product implementation truth, customer authority, legal/IP/data rights или Arvectum OS governance state.

## 6. Следующий этап

После публикации AC-303 как Approved и синхронизации `PORTFOLIO.md` и canonical roadmap следующим действием становится:

`AC-304 — Standalone product / reference implementation / module candidate / Arvectum OS capability candidate classification`.

По-русски: **разделение узлов портфеля на самостоятельные продукты, эталонные реализации, кандидаты в повторно используемые модули и кандидаты в возможности Arvectum OS**.

## 7. Границы решения

Это решение является Company-internal governance approval. Оно не заменяет отдельные юридически необходимые действия, бюджетные/банковские полномочия, product decisions, customer approvals или Arvectum OS governance approvals, когда они требуются соответствующей сферой authority.
