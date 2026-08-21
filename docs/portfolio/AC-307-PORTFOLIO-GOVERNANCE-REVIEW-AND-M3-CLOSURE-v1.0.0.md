# AC-307 — Итоговая проверка управления портфелем и закрытие M3

Статус: `Approved`
Версия: `1.0.0`
Утверждено: `2026-08-21`
Опубликовано: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-307 — Final portfolio governance review and M3 closure`
Approval: `docs/governance/decisions/DECISION-2026-08-21-AC-307-APPROVAL-AND-M3-CLOSURE.md`
Cross-review: `docs/reviews/AC-307-PORTFOLIO-GOVERNANCE-M3-CLOSURE-CROSS-REVIEW.md`
Approved proposal: `Proposed 0.9.0`, blob `904b9e5ffa12caeb082b3bf23a89aff251ebe8c4`

## 1. Модель утверждённой публикации

Эта публикация фиксирует утверждение точной проверенной редакции AC-307 без переписывания прошедшего cross-review текста задним числом.

Утверждённая исходная редакция:

- `docs/portfolio/AC-307-PORTFOLIO-GOVERNANCE-REVIEW-AND-M3-CLOSURE.md`;
- статус: `Proposed 0.9.0`;
- immutable git blob SHA: `904b9e5ffa12caeb082b3bf23a89aff251ebe8c4`.

Перекрёстная проверка:

- `docs/reviews/AC-307-PORTFOLIO-GOVERNANCE-M3-CLOSURE-CROSS-REVIEW.md`;
- iterations: `10 of maximum 10`;
- result: `Complete / PASS for Owner approval`;
- immutable git blob SHA: `bc3c4992f12dabaeb155f055373da292278cd791`.

Решение собственника:

- `docs/governance/decisions/DECISION-2026-08-21-AC-307-APPROVAL-AND-M3-CLOSURE.md` — `Approved`;
- явная формулировка: `AC-307 утверждаю`.

Полное нормативное содержание proposal `0.9.0` включается в эту Approved publication по immutable content reference и считается утверждённым в пределах заявленного scope.

## 2. Утверждённый интегральный portfolio-governance result

AC-301…AC-306 образуют согласованную цепочку:

```text
PORT identity / disposition
→ accountable Position
→ bounded investment / cost / risk treatment
→ standalone / reference / module / OS-candidate classification
→ inter-product dependency + Arvectum OS Product Contract boundary
→ capital / economics / Owner-attention prioritization
```

Материальных semantic contradictions, блокирующих M3 closure, не обнаружено.

Current integrated state:

| Node | Disposition | Accountable Position | Role | Dependency/OS boundary | Priority treatment |
|---|---|---|---|---|---|
| `PORT-001 — Arvectum Tender Agent` | `continue` | `POS-003` | standalone + `RI-OS-CONSUMER` | no hard peer dependency; P6.02 + P8.03 bounded CAP-001/CAP-004 | `A2` bounded revenue/pilot/evidence |
| `PORT-002 — Discount Parser` | `continue` | `POS-003` | standalone + `RI-OS-CONSUMER + RI-PRODUCT-FAMILY` | no hard peer dependency; P6.06 CAP-004 only | `A1` finish/accept/stabilize/maintain |
| `PORT-003 — Arvectum Proxy Launcher` | `continue` | `POS-003` | standalone | no Product Contract; no hard peer dependency | `B1` named-trigger |
| `PORT-004 — Creative Test Agent` | `continue` | `POS-003` | standalone + `RI-OS-CONSUMER` | P8.06 optional CAP-004 extension | `B2` named-trigger |
| `PORT-005 — Tender Small-Volume Calculator` | `contain` | `POS-003` | `RI-PRODUCT-FAMILY` | reference reuse only | `D1` contain/reference |
| `PORT-006 — Doors Parser` | `contain` | `POS-003` | `RI-PRODUCT-FAMILY` | parser-family evidence only | `D2` contain/support/reference |
| `PORT-007 — Data Platform` | `clarify` | `POS-003` | clarification-only Company/product-family module candidate | no hard dependency / no Product Contract | `C1` clarification-only; no material build |

## 3. Утверждённые системные ограничения

1. Repository locator не является Product Identity и не доказывает legal/IP ownership.
2. `POS-003` отвечает за Company-level portfolio stewardship, но не поглощает authority POS-001/POS-002/POS-004/POS-005/POS-006 или `ROD-*`.
3. `continue`, reference status, `A1/A2` и named trigger не являются бюджетом, spend authorization или unlimited growth mandate.
4. PORT-005/006 сохраняют `contain`; PORT-007 сохраняет `clarify` и не получает material-build authorization.
5. Между `PORT-001…PORT-007` не установлено обязательной hard runtime/code/data dependency.
6. Reference/reuse evidence не создаёт shared service/library/datastore/runtime автоматически.
7. Product repositories остаются canonical для product-specific implementation/status/domain semantics.
8. Arvectum OS остаётся canonical для Product Contracts, Platform Capability lifecycle и platform semantics.
9. AC-106 `P0 → P1 → P2 → P3` остаётся выше AC-306 portfolio order.
10. Technical PASS, repository maturity или sunk cost не доказывают profitability, market validation или customer readiness.

## 4. Carry-forward после M3

M3 closure не скрывает недостающие empirical evidence. В downstream остаются, в частности:

- Tender Agent — paid/pilot/deal economics и repeatability;
- Discount Parser — live client acceptance, bounded support/change economics и решение после accepted delivery;
- Proxy Launcher — human/legal rights-basis evidence, separate-host gates и отдельный per-app stop-gate;
- Creative Test Agent — real design-partner/customer inputs, success criteria и commercial conversion evidence;
- Data Platform — named consumers, minimal common contract и economic/continuity case до material build;
- portfolio-wide — profitability, unit economics, CAC/LTV/ROI, market validation, legal/IP/data completeness и customer/production readiness там, где они реально требуются.

Эти неизвестные не блокируют governance milestone M3, но должны быть получены до соответствующих material business/investment/customer/legal decisions.

## 5. Закрытие M3

Этап:

`M3 — Product/module-candidate portfolio governed as investments`

имеет статус:

`Complete / PASS`.

Результат M3 означает, что Company имеет достаточно согласованный governance baseline, чтобы управлять текущими продуктами/инициативами как инвестиционным портфелем с явными identity, accountability, boundaries, dependencies и priority rules.

M3 closure не означает profitability, market validation, legal compliance, customer readiness, production readiness, approved reusable production module, Stable Product Contract или Active Arvectum OS capability.

## 6. Canonical handoff

Следующий этап:

`M4 — Owner control and reference-implementation observability established`.

Следующее каноническое действие:

`AC-401 — Company work/obligation register model`.

AC-307 publication/approval переводит roadmap в M4, но не выполняет AC-401 и не создаёт программный dashboard или новый runtime по импликации.

## 7. Результат

`AC-307 — Complete / PASS`.

`M3 — Complete / PASS`.