# AC-406 — Cross-review: Owner Mission Control / Reference-Implementation Evidence View

Статус: `Complete / PASS for Owner approval`
Дата проверки: `2026-08-21`
Итераций выполнено: `8`
Лимит Owner для AC-406: `не задан`; review остановлен после закрытия всех material objections по proportional-governance principle
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-406 — Owner Mission Control / reference-implementation evidence view`

Проверенный exact proposal:

- `docs/operations/OWNER-MISSION-CONTROL-REFERENCE-IMPLEMENTATION-EVIDENCE-VIEW.md`;
- статус: `Proposed 0.9.0`;
- immutable git blob SHA: `f9e4d0f8e2e2a13f1147a8518461b35cd5264724`.

Статус утверждения: `Pending explicit Owner approval of the exact reviewed proposal`.

## 1. Review gate

AC-406 должен быть отклонён, если Owner Mission Control:

- становится новым source of truth вместо AC-401…AC-405/product/customer/accounting/legal/OS sources;
- превращает visibility в Organizational Authority или позволяет button/UI самому создавать approval/external effect;
- смешивает recommendation, decision, approval, legal/corporate act и execution;
- делает Owner очередью для routine delegated work/alerts;
- показывает stale/unknown/conflicted evidence как current/safe;
- заставляет Owner принять material decision при недостаточном evidence;
- превращает receivable/forecast в available cash;
- копирует restricted bank/customer/legal/security payload в public repository;
- создаёт vanity metrics, AI-autonomy %, maturity/readiness score без measurement evidence;
- считает approved governance доказательством actual AI-native operation;
- считает technical PASS доказательством business value/Owner-load reduction;
- создаёт новый `MC/DASH/ALERT` authority namespace;
- автоматически закрывает или изменяет WORK/OBL/DEC/APR/ESC/RSK/EXC/INC/PORT state;
- re-rank portfolio или продвигает module candidate из dashboard logic;
- переносит Company-specific semantics в Arvectum OS по удобству UI;
- создаёт Stable Product Contract/Active Capability из M9-alpha/P9.07/P9.10;
- делает новый software dashboard prerequisite M4;
- заявляет фактическое снижение Owner workload до реального использования;
- создаёт budget, payment, customer commitment, product change или automated consequential execution по импликации.

## 2. Итерация 1 — Mission Control не должен стать новой канонической базой данных

**Критика:** единый owner-facing view естественно начинает восприниматься как “главная правда”, особенно если он агрегирует work, risk, finance и portfolio.

**Сверка:** proposal Sections 1–3 определяют Mission Control как `derived evidence projection`; Section 2 переиспользует existing identities без `MC-*`; Section 15 оставляет durable history underlying records; Section 7 требует source reference / as-of / freshness / conflict behavior.

Company projection может быть authoritative только для собственной bounded interpretation, но underlying customer/accounting/product/legal/OS facts не переписывает.

**Результат:** PASS.

## 3. Итерация 2 — Owner Action queue не должен воспроизвести bottleneck, который AC-406 должен устранить

**Критика:** если Owner видит каждый warning, delegated task, overdue tracker row и informational item, Mission Control увеличит Owner load.

**Сверка:** Section 4 отделяет `Protect Now`, `Owner Action Required` и `Delegated Work / No Owner Action`. Section 6 требует material consequence + actual Owner action need, suppresses routine/AI/warning/low-level triggers и отдельно удерживает `waiting_external` вне false Owner tasks.

Это прямо поддерживает AC-104 target: preserve Owner control without scheduler/memory-layer execution.

**Результат:** PASS.

## 4. Итерация 3 — Decision card/UI не должен создавать authority через presentation

**Критика:** Mission Control — наиболее опасное место для silent “Approve/Pay/Send” semantics, потому что owner-facing UI может визуально смешать legal/corporate capacity, internal Position и technical access.

**Сверка:** Sections 3, 5 и 12 разделяют source fact / interpretation / recommendation / decision / approval / legal act / technical authorization / execution. Decision card требует `owner_capacity`, exact authority basis, requested act, excluded effects, remaining gates и execution handoff.

Section 12 делает view read-oriented by default; consequential interaction требует authenticated attributable Principal, correct capacity, current authority, exact scope/evidence/approvals, technical authorization и external-effect/idempotency safeguards.

Button existence ≠ approval authority.

**Результат:** PASS.

## 5. Итерация 4 — Finance/customer/security visibility не должна нарушить minimization

**Критика:** реальный Owner view полезен именно потому, что может содержать sensitive cash, customer, contract и incident context; public Company repo для live dashboard непригоден.

**Сверка:** Section 11 прямо разделяет public semantic specification и restricted live projection; credentials, transaction exports, confidential exact cash, customer/vendor payload, privileged legal/tax/security/fraud details и chain-of-thought запрещены к публикации ради dashboard convenience.

Section 4.4 допускает restricted exact values вне public/lower-privilege view. Visibility не предоставляет underlying source access.

**Результат:** PASS.

## 6. Итерация 5 — Reference-implementation evidence не должно стать “AI maturity theater”

**Критика:** AC-406 впервые показывает Owner evidence, что Company реально AI-native. Есть риск объявить модель работающей потому, что существуют Positions, policies и агенты.

**Сверка:** Sections 4.6, 8 и 9 требуют source-backed operational claims по authority separation, Position accountability, bounded AI execution/fail-closed, Owner reconstruction burden, continuity/replacement, business linkage, provenance и learning loop.

Approved governance document, token/agent/commit count, technical PASS и красивый dashboard отдельно названы insufficient evidence.

Claim format требует observed scope/period, evidence refs, repeatability basis, limitations и next validation. Global autonomy/maturity/readiness score запрещён без measurement model/evidence.

AC-208 boundary также сохраняется: M2 design не доказывает фактическое снижение Owner load, доказанную AI Position или external readiness.

**Результат:** PASS.

## 7. Итерация 6 — Stale/unknown/conflicted evidence должно блокировать ложную уверенность

**Критика:** aggregate view опасен тем, что визуально “сглаживает” разную свежесть источников и заставляет Owner принимать binary decision на неполном основании.

**Сверка:** Section 7 вводит current/stale/unknown/conflicted/not-time-sensitive presentation states без arbitrary universal TTL; Section 5 прямо требует `known_unknowns` и позволяет `not decision-ready` вместо forcing approve/reject.

Material stale/unknown/conflicted evidence не может silently стать safe/approved/paid/accepted/closed/ready. AC-404 distinction forecast/receivable ≠ cash preserved.

**Результат:** PASS.

## 8. Итерация 7 — Company / Product / Arvectum OS boundary

**Критика:** current OS уже имеет M9-alpha Workspace, P9.07 product composition и planned P9.10 Company composition. Удобно было бы немедленно объявить Mission Control OS surface и встроить Company semantics в platform.

**Сверка:** Section 13 фиксирует current OS at `76504766353028540891ac1dfdbf1e5dc331a4af`, roadmap `2.81.0`, M9-alpha exact private scope, P9.07 Current, P9.10 Planned и отсутствие Active Capability/Stable Product Contract по импликации.

AC-406 только формирует Company-side requirements/evidence. Любой future OS rendering требует explicit admitted boundary/Product Contract or applicable OS governance; source truth/authority/external effect remain separated.

Product repositories retain product implementation/status/domain semantics.

**Результат:** PASS.

## 9. Итерация 8 — Не строить dashboard раньше реального use evidence

**Критика:** AC-406 может завершиться software project, хотя roadmap прямо говорит, что dashboard не prerequisite, а реальная проблема — reconstruction burden.

**Сверка:** Section 14 задаёт минимальный путь `semantic model → restricted Markdown/structured projection → actual Owner-use evidence in AC-407 → only then UI/OS composition decision`.

Section 17 прямо говорит, что approval не populates live snapshot, не доказывает reduced Owner workload и не создаёт dashboard requirement. Section 18 передаёт actual cadence/usability/control-burden test в AC-407.

Это минимальный обратимый business-first шаг.

**Результат:** PASS.

## 10. Acceptance matrix

| Проверка | Результат |
|---|---|
| Mission Control is derived projection, not source of truth | PASS |
| no new MC/DASH/ALERT authority namespace | PASS |
| existing WORK/OBL/DEC/APR/ESC/RSK/EXC/INC/PORT identities reused | PASS |
| source fact separated from Company interpretation | PASS |
| recommendation separated from decision/approval | PASS |
| legal/corporate/customer act separated from internal approval | PASS |
| technical authorization/execution separated from authority | PASS |
| Protect Now limited to material/time-sensitive conditions | PASS |
| Owner Action queue requires actual Owner authority/action need | PASS |
| delegated healthy work does not require Owner micromanagement | PASS |
| waiting_external is not false Owner task | PASS |
| decision card identifies exact capacity/authority/question | PASS |
| decision card exposes unknowns/downside/remaining gates | PASS |
| insufficient evidence may be `not decision-ready` | PASS |
| stale/unknown/conflicted evidence cannot become safe/ready | PASS |
| AC-404 forecast/receivable ≠ cash preserved | PASS |
| restricted financial/customer/security data not forced public | PASS |
| live Mission Control default may be restricted | PASS |
| reference evidence requires actual operational traces | PASS |
| governance design ≠ operational proof | PASS |
| AI agent/token/commit count not accepted as value evidence | PASS |
| no unsupported global autonomy/maturity/readiness score | PASS |
| business linkage included in AI-native evidence | PASS |
| Owner-load reduction must be observed, not asserted | PASS |
| continuity definition/test distinction preserved | PASS |
| portfolio view does not re-rank automatically | PASS |
| module/reuse evidence does not auto-promote | PASS |
| Product implementation/status stays product-owned | PASS |
| OS Product Contract/capability lifecycle stays OS-owned | PASS |
| M9-alpha/P9.07/P9.10 create no Company authority by implication | PASS |
| consequential UI interaction fail-closed unless governed | PASS |
| software dashboard not prerequisite | PASS |
| no live snapshot population by approval | PASS |
| AC-407 receives actual-use/cadence/control-burden validation | PASS |
| no budget/payment/customer/product/external effect created | PASS |

## 11. Residual limitations intentionally carried forward

AC-406 proposal does **not** prove:

- completeness/currentness of live Company control records;
- current cash/liquidity or actual receivables/payables;
- current absence/presence of material incidents/risks;
- current validity of all portfolio theses;
- actual reduction in Owner reconstruction burden;
- actual AI executor quality/cost/reliability/replacement performance;
- profitability, market validation or customer readiness;
- usefulness of a software Mission Control UI;
- suitability of Arvectum OS P9.10 as final Company surface;
- final management cadence or M4 closure.

Эти gaps должны быть measured/observed in actual operation, primarily AC-407 and later business/product evidence.

## 12. Cross-review conclusion

После 8 последовательных review iterations по source canonicality, Owner workload, authority-safe decisions, confidentiality, AI-native evidence quality, freshness/fail-closed behavior, Company↔Product↔OS boundary и implementation proportionality material blocking objections не осталось.

Итог:

`AC-406 cross-review — COMPLETE / PASS FOR OWNER APPROVAL`.

Exact reviewed proposal:

- `docs/operations/OWNER-MISSION-CONTROL-REFERENCE-IMPLEMENTATION-EVIDENCE-VIEW.md`;
- `Proposed 0.9.0`;
- blob `f9e4d0f8e2e2a13f1147a8518461b35cd5264724`.

Cross-review не является Owner approval и не делает Mission Control model binding.

## 13. Required next gate

Для закрытия AC-406 требуется явный attributable Owner act, однозначно утверждающий exact reviewed proposal.

Рекомендуемая краткая формулировка:

`AC-406 утверждаю`.

До такого акта:

- AC-406 остаётся `Proposed`;
- live Mission Control snapshot не создаётся по импликации;
- roadmap остаётся на AC-406;
- Approved `1.0.0` publication не создаётся;
- AC-407 не становится current canonical action.
