# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.36.0`
Создано: `2026-08-19`
Обновлено: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Текущее каноническое действие: `AC-501 — First governed workflow candidate selection`
Русское название текущего действия: `Выбор первого реального управляемого рабочего контура Company`

## 1. Модель публикации

Эта редакция `0.36.0` сохраняет полное содержание дорожной карты `0.35.0` по immutable git blob и добавляет утверждение/закрытие AC-407, закрытие M4 и переход к M5/AC-501.

Предыдущая редакция:

- версия: `0.35.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `a3968f9a96474cc66adc7c6294e6a1d0265e8334`.

Все ранее определённые M0–M9, Company priority hierarchy, Company/Product/Arvectum OS boundaries, bounded AC-108 evidence loop и конечный AC-901 сохраняются, если прямо не изменены более новым approved decision.

## 2. Закрытие AC-407 и M4

`AC-407 — Management operating cadence and control review` имеет статус:

`Complete / PASS`.

Approved publication:

- `docs/operations/MANAGEMENT-OPERATING-CADENCE-AND-M4-CONTROL-REVIEW-v1.0.0.md` — `Approved 1.0.0`, blob `e8b99aea625718f6f38495b725179ad25c7a14e8`;
- exact reviewed proposal: `docs/operations/MANAGEMENT-OPERATING-CADENCE-AND-M4-CONTROL-REVIEW.md` — `Proposed 0.9.0`, blob `87453d69314da217d3bd02f4645ac3f3444ed788`;
- cross-review: `docs/reviews/AC-407-MANAGEMENT-OPERATING-CADENCE-AND-M4-CONTROL-REVIEW.md` — `8 iterations`, `Complete / PASS for Owner approval and M4 closure`, blob `6de916440b2d77957aed9ddde3eb0a47eba8a9b4`;
- evidence snapshot: `docs/operations/OWNER-MISSION-CONTROL-REFERENCE-SNAPSHOT-2026-08-21.md`, blob `09b056e99ecb066402bc1d2b12d2dab772898f1b`;
- Owner decision: `docs/governance/decisions/DECISION-2026-08-21-AC-407-APPROVAL-AND-M4-CLOSURE.md`, blob `365e30f7ebcd4ee7fda858cf874ffe6c790c801d`;
- explicit Owner wording: `AC-407 и закрытие M4 утверждаю`.

`M4 — Owner control and reference-implementation observability established` получает статус:

`Complete / PASS`.

Это closure exact owner-control/reference-observability scope. Оно не означает live-data completeness, current liquidity proof, profitability, market/customer/production readiness, Company-wide continuity readiness или доказанную broad AI autonomy.

## 3. Утверждённый operating cadence после M4

Current baseline:

```text
material event
→ immediate bounded update/review
→ Owner only for actual authority/action need

active operating week + material aggregate state
→ at most one short asynchronous Owner checkpoint

monthly
→ one integrated management checkpoint
   (finance + portfolio exception scan + open material controls + burden check)

quarterly
→ integrated portfolio / continuity-gap / control-fit / Owner-burden revalidation
```

Нет mandatory daily standup/dashboard acknowledgement.

Routine `AM-1`/`AM-2` execution использует уже approved envelope и не требует RFC-like governance ceremony. Material/reserved durable change требует evidence + exact authority gate. Material unknown/boundary exceedance требует escalation/fail-closed.

## 4. Status milestones

- `M0` — `Complete / PASS`;
- `M1` — `Complete / PASS`;
- `M2` — `Complete / PASS`;
- `M3` — `Complete / PASS`;
- `M4` — `Complete / PASS`;
- `M5 — First real governed Company operating contour proven` — `Current`;
- `M6 — First real AI-held Position proven economically and operationally` — `Planned`;
- `M7` — `Future`;
- `M8` — `Future`;
- `M9` — final planned human-readable Russian reconciliation stage after M8 unless Owner changes sequence.

## 5. Phase 5 — First governed Company operating contour

Milestone:

`M5 — First real governed Company operating contour proven`.

Purpose: connect the approved organization/control model to a real recurring Company workflow through the smallest high-value reversible contour.

The first workflow is **not predetermined**. Selection must use actual business/evidence criteria rather than convenience, architecture completeness or agent novelty.

| ID | Работа | Статус |
|---|---|---|
| `AC-501` | First governed workflow candidate selection | `Current` |
| `AC-502` | Workflow, accountable Position, authority/data/evidence contract | `Planned` |
| `AC-503` | Arvectum OS reliance/admission mapping where applicable | `Planned` |
| `AC-504` | Bounded workflow implementation | `Planned` |
| `AC-505` | Supervised real-operation proof | `Planned` |
| `AC-506` | Incident, uncertain-outcome, recovery and fallback drill | `Planned` |
| `AC-507` | Business-value/economic review and continue/change/stop decision | `Planned` |

## 6. Текущее действие — AC-501

### AC-501 — First governed workflow candidate selection

Статус: `Current`.

AC-501 должен выбрать один реальный Company workflow для M5 на основе:

- real customer/revenue/obligation value or evidence acquisition;
- current workload и Owner reconstruction/coordination burden;
- repeatability;
- bounded authority feasibility;
- data/tool/access readiness;
- risk and reversibility;
- evidence quality and reconstructability;
- continuity/fallback feasibility;
- likely economic/operational value relative to implementation/control cost.

Кандидат не должен выбираться только потому, что product технически готов, уже интегрирован с Arvectum OS, использует AI или удобен для демонстрации.

AC-501 должен сравнить реальных кандидатов, зафиксировать evidence gaps и предложить exact selection decision. Material external commitment, spend, customer promise, product roadmap change или OS boundary по факту selection не создаются.

## 7. M5 exit direction

M5 может быть закрыт только после actual supervised real-operation proof, где:

- workflow реально повторяется или имеет достаточную recurring basis;
- accountable Position/authority/Assignment/access semantics действуют, а не только описаны;
- consequential effects остаются внутри approved authority;
- material actions/evidence reconstructable;
- failure/uncertainty имеет safe fallback/recovery path;
- customer/business/Owner-load/quality/cost/risk evidence достаточно для continue/change/stop decision;
- broader Product/OS/business readiness не выводится по импликации.

## 8. Carry-forward from M4

M5/M6 должны получать empirical evidence по gaps, которые M4 сознательно не закрыл: live control-record completeness, measured Owner-load reduction, AI execution quality/cost/reliability, actual continuity/replacement, current source-backed finance evidence и direct business linkage.

## 9. Authority boundary

Roadmap координирует работу, но не создаёт Organizational Authority, budget, legal/corporate authority, customer/vendor commitment, Product Contract, access grant или production approval.

Material capital, spend, external commitment, portfolio investment, risk acceptance, legal/IP/data и Company↔Product↔Arvectum OS decisions продолжают проходить applicable evidence and authority path.
