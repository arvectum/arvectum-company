# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.35.0`
Создано: `2026-08-19`
Обновлено: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Текущее каноническое действие: `AC-407 — Management operating cadence and control review`
Русское название текущего действия: `Проверка управленческого рабочего ритма, нагрузки системы контроля и закрытия M4`

## 1. Модель публикации

Эта редакция `0.35.0` сохраняет полное содержание дорожной карты `0.34.0` по immutable git blob и добавляет утверждение/закрытие AC-406 с переходом к AC-407.

Предыдущая редакция:

- версия: `0.34.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `de67144e8e0650fb8290145bd5049d16f7020a1e`.

Все ранее определённые этапы M0–M9, Company priority hierarchy, Company/Product/Arvectum OS boundaries, bounded AC-108 evidence loop и конечный AC-901 остаются в силе, если прямо не изменены более новым утверждённым решением.

## 2. Закрытие AC-406

`AC-406 — Owner Mission Control / reference-implementation evidence view` имеет статус:

`Complete / PASS`.

Утверждённая publication:

- `docs/operations/OWNER-MISSION-CONTROL-REFERENCE-IMPLEMENTATION-EVIDENCE-VIEW-v1.0.0.md` — `Approved 1.0.0`, blob `b8348c8d9951416e6dbb101b5a8061b98b113db6`;
- exact reviewed proposal: `docs/operations/OWNER-MISSION-CONTROL-REFERENCE-IMPLEMENTATION-EVIDENCE-VIEW.md` — `Proposed 0.9.0`, blob `f9e4d0f8e2e2a13f1147a8518461b35cd5264724`;
- cross-review: `docs/reviews/AC-406-OWNER-MISSION-CONTROL-REFERENCE-EVIDENCE-CROSS-REVIEW.md` — `8 iterations`, PASS, blob `f6db950a29f30da0065277e50da41a2d84e3b2ed`;
- Owner decision: `docs/governance/decisions/DECISION-2026-08-21-AC-406-APPROVAL.md`, blob `06dd01874fcabc2e6e6a4e9bc8cf7b5285ae85b4`;
- explicit Owner approval wording: `AC-406 утверждаю`.

AC-406 устанавливает Owner Mission Control как derived evidence projection:

```text
source/control evidence
→ bounded owner-facing projection
→ protect-now / Owner-action / delegated-work / finance / portfolio / reference-evidence views
→ exact decision packet where Owner authority is actually needed
→ governed execution handoff
```

Ключевые ограничения:

- `Mission Control ≠ source of truth ≠ authority ≠ approval ≠ execution`;
- `source fact ≠ Company interpretation ≠ recommendation ≠ decision ≠ approval ≠ legal/corporate/customer act ≠ technical authorization ≠ execution evidence`;
- `not decision-ready` допустим и обязателен при недостаточном/stale/unknown/conflicted material evidence;
- forecast/receivable не отображаются как available cash;
- governance design, technical PASS, agent/token/commit count или UI existence не являются доказательством работающей AI-native Company;
- software dashboard не является prerequisite;
- live restricted evidence не публикуется в public Company repository по импликации.

## 3. Утверждённый M4 control baseline после AC-406

Company имеет шесть связанных уровней управления и видимости:

1. `WORK-*` / `OBL-*` — material work и obligations;
2. `DEC-*` / `APR-*` / `ESC-*` — material decisions, approval gates/acts и escalations;
3. `RSK-*` / `EXC-*` / `INC-*` — material risks, control exceptions и incidents;
4. AC-404 management-finance projection — decision-relevant cash/commitment signals поверх authoritative sources;
5. AC-405 portfolio review cadence — event-driven и bounded calendar revalidation поверх M3 portfolio semantics и AC-401…AC-404 evidence;
6. AC-406 Owner Mission Control — derived owner-facing evidence view и reference-implementation claim discipline поверх предыдущих уровней.

Шестой уровень не создаёт новый source of truth, authority namespace, automatic execution или software requirement.

Сохраняются общие границы:

- Company control/management representation не подменяет legal/accounting/customer/product/OS truth;
- `P0…P3` — sequencing context, не spend authorization;
- visibility, recommendation, risk/incident/finance/portfolio status не являются approval;
- material spend/commitment, portfolio investment, risk acceptance, module admission и Company↔Product↔OS boundary changes требуют applicable attributable authority act;
- stale/missing/conflicted evidence требует explicit uncertainty/review/fail-closed behavior;
- public repository использует minimization и reference-over-copy;
- Company-specific semantics не переносятся в Arvectum OS по импликации.

## 4. Предыдущие этапы

- `M0` — `Complete / PASS`;
- `M1` — `Complete / PASS`;
- `M2` — `Complete / PASS`;
- `M3 — Product/module-candidate portfolio governed as investments` — `Complete / PASS`.

Полный prior baseline остаётся доступным через immutable roadmap chain и утверждённые AC-001…AC-406 artifacts.

## 5. Phase 4 — Owner control and reference observability

Milestone:

`M4 — Owner control and reference-implementation observability established`.

Текущий статус:

| ID | Работа | Статус |
|---|---|---|
| `AC-401` | Company work/obligation register model | `Complete / PASS` |
| `AC-402` | Decision, approval and escalation register model | `Complete / PASS` |
| `AC-403` | Risk, exception and incident register model | `Complete / PASS` |
| `AC-404` | Cash, commitment and management reporting baseline | `Complete / PASS` |
| `AC-405` | Portfolio/module/priority review cadence | `Complete / PASS` |
| `AC-406` | Owner Mission Control / reference-implementation evidence view | `Complete / PASS` |
| `AC-407` | Management operating cadence and control review | `Current` |

Software dashboard не является предпосылкой M4: manual/restricted Markdown/structured projection допустимы, если они надёжны, пропорциональны и реально уменьшают Owner reconstruction burden.

## 6. Текущее действие — AC-407

### AC-407 — Management operating cadence and control review

Статус: `Current`.

AC-407 должен провести итоговую проверку M4 не как ещё один design-only документ, а как проверку того, насколько утверждённые AC-401…AC-406 controls образуют жизнеспособный operating cadence и где они нуждаются в корректировке до закрытия M4.

Минимальные вопросы AC-407:

- какой фактический operating rhythm нужен для P0/Owner attention, work/obligations, decisions/approvals, risk/incidents, finance, portfolio и Mission Control;
- какие checks должны быть event-driven, какие monthly/quarterly backstops достаточны, а какие создают лишний control burden;
- можно ли Owner увидеть material Company state и exact required action без полной реконструкции чатов/repos/source systems;
- какие routine activities реально продолжаются без Owner intervention внутри valid Position/Assignment/authority/access boundaries;
- есть ли evidence, что control preparation/publication/state synchronization отделены от reserved Owner decisions;
- где freshness/unknown/conflict handling реально fail-closed, а где остаётся риск ложной уверенности;
- какие reference-implementation claims уже подтверждены actual traces, а какие остаются design hypotheses;
- появились ли observed cases bounded AI execution, correct escalation/fail-closed, continuity/replacement и business linkage;
- создаёт ли текущая система больше administrative burden, чем предотвращает, и что нужно упростить;
- требуется ли менять AC-405 monthly/quarterly defaults по actual evidence;
- нужен ли software Mission Control/UI сейчас или Markdown/structured projection остаётся достаточным;
- достаточно ли evidence для M4 `Complete / PASS`, либо должны остаться exact carry-forward gaps.

AC-407 должен сохранять business-first принцип: проверять usefulness/control burden/evidence, а не добавлять новые registers, dashboards, meetings или automation ради полноты модели.

AC-407 не должен по импликации создавать budget, authority, customer/vendor commitment, product roadmap change, reusable module, Arvectum OS Product Contract/capability transition или утверждать profitability/business readiness без evidence.

## 7. M4 exit criteria direction

M4 может быть закрыт только если одновременно подтверждено, что:

1. Owner имеет устойчивую owner-facing visibility material Company control state без обязательной chat-memory reconstruction;
2. real Owner actions отделены от routine delegated execution;
3. work/obligation, decision/approval, risk/incident, finance и portfolio controls не противоречат друг другу и не создают parallel sources of truth;
4. stale/unknown/conflicted evidence не маскируется как ready/safe/approved;
5. reference-implementation claims ограничены actual evidence и не превращаются в vanity maturity claims;
6. operating cadence пропорционален текущему масштабу Company и не делает governance самой большой работой;
7. unresolved empirical gaps явно carry-forward, а не объявлены закрытыми по факту model approval.

M4 closure не будет означать profitability, market validation, legal compliance, customer readiness, production readiness, доказанную полную автономность AI workforce или необходимость software dashboard.

## 8. Authority boundary

Roadmap координирует работу, но не создаёт Organizational Authority, budget, legal/corporate authority, customer/vendor commitment, Product Contract, access grant или production approval.

Material capital, spend, external commitment, portfolio investment, risk acceptance, legal/IP/data и Company↔Product↔Arvectum OS decisions продолжают проходить соответствующий evidence и authority path.