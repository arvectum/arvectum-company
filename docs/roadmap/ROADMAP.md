# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.37.0`
Создано: `2026-08-19`
Обновлено: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Текущее каноническое действие: `AC-502 — Workflow, accountable Position, authority/data/evidence contract`
Русское название текущего действия: `Формализация первого реального управляемого workflow: ответственность, полномочия, данные и evidence`

## 1. Модель публикации

Эта редакция `0.37.0` сохраняет полное содержание дорожной карты `0.36.0` по immutable git blob и добавляет утверждение/закрытие AC-501, выбор первого M5 workflow и переход к AC-502.

Предыдущая редакция:

- версия: `0.36.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `81c34c542a1ef5606f1ade6c28af300ba113f39e`.

Все ранее определённые M0–M9, Company priority hierarchy, Company/Product/Arvectum OS boundaries, bounded AC-108 evidence loop и конечный AC-901 сохраняются, если прямо не изменены более новым approved decision.

## 2. Закрытие AC-501

`AC-501 — First governed workflow candidate selection` имеет статус:

`Complete / PASS`.

Approved publication:

- `docs/operations/FIRST-GOVERNED-WORKFLOW-CANDIDATE-SELECTION-v1.0.0.md` — `Approved 1.0.0`, blob `c0e1bd3a0e247ef72cb79ebd988d78d4487618f7`;
- exact reviewed proposal: `docs/operations/FIRST-GOVERNED-WORKFLOW-CANDIDATE-SELECTION.md` — `Proposed 0.9.0`, blob `f6cbebfea1c2e6a56a0fd03c38b68a7211c6bbde`;
- cross-review: `docs/reviews/AC-501-FIRST-GOVERNED-WORKFLOW-CANDIDATE-SELECTION-CROSS-REVIEW.md` — `10 of maximum 10`, `Complete / PASS for explicit Owner approval`, blob `10924469f889d9e97d6a6d11b61d57a70b69e22a`;
- Owner decision: `docs/governance/decisions/DECISION-2026-08-21-AC-501-APPROVAL.md`, blob `04d42d227c74c779e58d4298ad542e458821837b`;
- explicit Owner wording at the pending approval gate: `делай`.

## 3. Первый выбранный governed workflow

Для M5 утверждён:

`WF-M5-001 — Customer Feedback → Classified Correction → Verified Candidate → Customer Validation / Acceptance`.

Первый real-operation contour:

`PORT-002 — Discount Parser`.

Выбор основан на реальном повторяющемся customer-feedback/correction/validation evidence, Owner-bottleneck relevance, bounded authority feasibility, data/tool readiness, reversibility, reconstructability и practical fallback.

Этот выбор не является:

- новым budget или portfolio reallocation;
- customer commitment;
- изменением `PORT-002` disposition;
- утверждением production/business/legal readiness;
- автоматическим OS dependency;
- доказательством M5 closure.

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

| ID | Работа | Статус |
|---|---|---|
| `AC-501` | First governed workflow candidate selection | `Complete / PASS` |
| `AC-502` | Workflow, accountable Position, authority/data/evidence contract | `Current` |
| `AC-503` | Arvectum OS reliance/admission mapping where applicable | `Planned` |
| `AC-504` | Bounded workflow implementation | `Planned` |
| `AC-505` | Supervised real-operation proof | `Planned` |
| `AC-506` | Incident, uncertain-outcome, recovery and fallback drill | `Planned` |
| `AC-507` | Business-value/economic review and continue/change/stop decision | `Planned` |

## 6. Текущее действие — AC-502

### AC-502 — Workflow, accountable Position, authority/data/evidence contract

Статус: `Current`.

AC-502 должен формализовать `WF-M5-001` до implementation и real-operation proof.

Минимальный scope AC-502:

- exact workflow purpose, start/end boundary и state transitions;
- accountable Position и participating Positions без fake headcount;
- permitted/excluded action classes и applicable `AM-*` ceilings;
- explicit customer scope/commitment/acceptance gates;
- Company/Product source-of-truth separation;
- data classes, tool/access needs и least-privilege requirements;
- evidence contract: какие source facts, classifications, implementation/test results, delivery candidate и customer validation outcome нужны для reconstructability;
- stale/unknown/ambiguous-input behavior;
- escalation/fail-closed conditions при scope change, non-standard commitment, material risk, missing rights/access/evidence или uncertain external effect;
- continuity/manual fallback expectations;
- lightweight M5 measurements, включая Owner interventions, rework cause, cycle/blocking evidence и outcome quality там, где это реально измеримо.

AC-502 не должен преждевременно:

- строить новый runtime/software layer;
- создавать customer promise;
- менять Product roadmap;
- выдавать credentials;
- активировать `AM-3`/`AM-4`;
- считать Arvectum OS обязательным.

Exact OS reliance/admission mapping остаётся отдельным `AC-503` после определения workflow contract.

## 7. M5 exit direction

M5 может быть закрыт только после actual supervised real-operation proof, где:

- workflow реально повторяется или имеет достаточную recurring basis;
- accountable Position/authority/Assignment/access semantics действуют, а не только описаны;
- consequential effects остаются внутри approved authority;
- material actions/evidence reconstructable;
- failure/uncertainty имеет safe fallback/recovery path;
- customer/business/Owner-load/quality/cost/risk evidence достаточно для continue/change/stop decision;
- broader Product/OS/business readiness не выводится по импликации.

## 8. Carry-forward from M4/AC-501

M5/M6 должны получать empirical evidence по gaps, которые M4 и AC-501 сознательно не закрыли: live control-record completeness, measured Owner-load reduction, AI execution quality/cost/reliability, actual continuity/replacement, current source-backed finance evidence и direct business linkage.

Для `WF-M5-001` отдельно должны быть проверены:

- может ли first-pass classification реально уменьшить Owner interruption без ошибочного scope/commitment решения;
- какой объём correction/verification может выполнять `POS-004` в bounded envelope;
- где customer validation/acceptance неизбежно требует human/customer authority;
- не становится ли workflow новым бюрократическим overhead относительно текущего быстрого feedback loop;
- создаёт ли evidence capture measurable reduction в reconstruction/rework cost.

## 9. Authority boundary

Roadmap координирует работу, но не создаёт Organizational Authority, budget, legal/corporate authority, customer/vendor commitment, Product Contract, access grant или production approval.

Material capital, spend, external commitment, portfolio investment, risk acceptance, legal/IP/data и Company↔Product↔Arvectum OS decisions продолжают проходить applicable evidence and authority path.
