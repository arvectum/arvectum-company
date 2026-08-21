# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.39.0`
Создано: `2026-08-19`
Обновлено: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Текущее каноническое действие: `AC-504 — Bounded workflow implementation`
Русское название текущего действия: `Минимальная обратимая реализация первого реального governed workflow`

## 1. Модель публикации

Эта редакция `0.39.0` сохраняет полное содержание дорожной карты `0.38.0` по immutable git blob и добавляет утверждение/закрытие AC-503 и переход к AC-504.

Предыдущая редакция:

- версия: `0.38.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `44b265a3a1816352eb66bd7e7252328f58bede24`.

Все ранее определённые M0–M9, Company priority hierarchy, Company/Product/Arvectum OS boundaries, bounded AC-108 evidence loop, AC-501 workflow selection, AC-502 workflow contract и конечный AC-901 сохраняются, если прямо не изменены более новым approved decision.

## 2. Закрытие AC-503

`AC-503 — Arvectum OS reliance/admission mapping where applicable` имеет статус:

`Complete / PASS`.

Approved publication:

- `docs/operations/FIRST-GOVERNED-WORKFLOW-ARVECTUM-OS-RELIANCE-ADMISSION-MAPPING-v1.0.0.md` — `Approved 1.0.0`, blob `8984d4c094da87a2c9d201fd9cffcd617c641f8f`;
- exact reviewed proposal: `docs/operations/FIRST-GOVERNED-WORKFLOW-ARVECTUM-OS-RELIANCE-ADMISSION-MAPPING.md` — `Proposed 0.9.0`, blob `3b7bef8f227d17990ced164aa0de16874bb2ec61`;
- cross-review: `docs/reviews/AC-503-FIRST-GOVERNED-WORKFLOW-ARVECTUM-OS-RELIANCE-CROSS-REVIEW.md` — `10 of 10`, `Complete / PASS for explicit Owner approval`, blob `67623301fbc2a370433d94952ee3ed6c2f0ef608`;
- Owner decision: `docs/governance/decisions/DECISION-2026-08-21-AC-503-APPROVAL.md`, blob `5197aa78a48d5d4373f6bf24e887bf58607d2d75`;
- exact Owner wording: `AC-503 утверждаю`.

## 3. Утверждённый AC-503 result

Для первого M5 proof `WF-M5-001` в contour `PORT-002 — Discount Parser` утверждено:

**`NO-ADDITIONAL-OS-RELIANCE — no additional Arvectum OS reliance required for the first M5 proof of WF-M5-001`.**

Следствия:

- AC-504 не обязан делать Arvectum OS execution/history canonical для первого proof;
- новый/изменённый OS Product Contract не требуется до первого proof, пока implementation не пересекает actual governed-OS reliance trigger;
- existing `P6.06` не расширяется за controlled Telegram publication/reconstruction scope;
- CAP-004 не становится WF-M5-001 dependency по импликации;
- никакой OS Product Contract/Capability lifecycle transition не создаётся;
- Company/product/customer sources остаются достаточным canonical/evidence contour для первого proof;
- implementation должен сохранять OS-neutral exact references, чтобы future admission оставался обратимым.

Это bounded решение для первого M5 proof, а не общий отказ Company от Arvectum OS.

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

| ID | Работа | Статус |
|---|---|---|
| `AC-501` | First governed workflow candidate selection | `Complete / PASS` |
| `AC-502` | Workflow, accountable Position, authority/data/evidence contract | `Complete / PASS` |
| `AC-503` | Arvectum OS reliance/admission mapping where applicable | `Complete / PASS` |
| `AC-504` | Bounded workflow implementation | `Current` |
| `AC-505` | Supervised real-operation proof | `Planned` |
| `AC-506` | Incident, uncertain-outcome, recovery and fallback drill | `Planned` |
| `AC-507` | Business-value/economic review and continue/change/stop decision | `Planned` |

## 6. Текущее действие — AC-504

### AC-504 — Bounded workflow implementation

Статус: `Current`.

Цель AC-504 — превратить утверждённые AC-501/AC-502/AC-503 semantics в минимально достаточную реальную implementation-механику для одного WF-M5-001 case, не выдавая implementation readiness за empirical proof.

Минимальный scope:

1. определить exact implementation home для Company-level case/evidence mechanics и product-level technical execution без дублирования canonical truth;
2. реализовать lightweight case/evidence representation с exact workflow/version reference и safe case identifier;
3. поддержать material `W0…W11` state transitions и `CL-1…CL-7` classification evidence без превращения их в generic platform DSL;
4. сохранить attributable POS-002 classification/customer gates и POS-004 bounded technical segment;
5. связать protected customer-source refs, product issue/PR/commit/test/build/release-candidate refs и Company control refs;
6. обеспечить fail-closed/blocked/unknown/stale/uncertain representation;
7. не помещать raw customer DC-2 или DC-3 secrets в public Company repo;
8. реализовать только реально нужные scripts/templates/records/tests, достаточные для supervised AC-505 proof;
9. сохранить manual fallback и executor/runtime replaceability;
10. зафиксировать runbook/acceptance checks для передачи в AC-505.

AC-504 должен быть **OS-neutral** в пределах утверждённого AC-503 result. Это значит, что implementation не должна зависеть от OS canonical state/shared history/Execution Context/CAP-004 без повторного admission check.

AC-504 не должен:

- строить generic workflow engine, event bus, Company-wide orchestration platform или локальный substitute Arvectum OS;
- переносить Company-specific Position/customer/workflow semantics в `arvectum/arvectum-os`;
- расширять P6.06;
- создавать новый OS Product Contract/capability transition;
- активировать AM-3/AM-4;
- создавать customer promise/acceptance или autonomous consequential external effect;
- считать unit tests или technical PASS завершением AC-505/M5.

## 7. AC-504 expected evidence

До перехода к AC-505 должны существовать проверяемые evidence того, что implementation:

- может открыть/вести один sanitized workflow case;
- фиксирует exact workflow/version and current state;
- сохраняет attributable classification decision;
- связывает bounded technical work и verification evidence;
- различает Candidate Ready, customer-facing handoff и customer acceptance;
- умеет явно остановиться/заблокироваться на ambiguity/missing authority/evidence/access;
- не требует secrets/raw confidential customer data в public repo;
- допускает manual fallback;
- достаточно проста для реального supervised использования.

AC-504 completion не является AC-505 empirical proof.

## 8. M5 exit direction

M5 остаётся открытым. Он может быть закрыт только после AC-504…AC-507 и actual supervised real-operation evidence, включая:

- real governed workflow execution;
- valid Position/Assignment/authority/access behavior;
- reconstructable consequential evidence;
- actual uncertainty/failure/recovery path;
- customer/business outcome evidence;
- measured Owner intervention/reconstruction burden;
- technical/AI quality, cost and reliability evidence;
- continue/change/stop economic decision.

## 9. Authority and boundary rule

Roadmap не создаёт Organizational Authority, budget, legal/corporate authority, customer/vendor commitment, Product Contract, access grant, production approval или OS lifecycle transition.

Company workflow semantics остаются Company-owned; product implementation truth — product-owned; Arvectum OS universal platform contracts/lifecycle — OS-owned. Если AC-504 обнаружит реальную OS reliance need, работа должна остановиться на соответствующей границе и пройти applicable OS governance/admission path до consequential reliance.