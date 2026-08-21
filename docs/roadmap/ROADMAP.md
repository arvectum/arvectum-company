# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.38.0`
Создано: `2026-08-19`
Обновлено: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Текущее каноническое действие: `AC-503 — Arvectum OS reliance/admission mapping where applicable`
Русское название текущего действия: `Проверка фактической необходимости и допустимости опоры первого workflow на Arvectum OS`

## 1. Модель публикации

Эта редакция `0.38.0` сохраняет полное содержание дорожной карты `0.37.0` по immutable git blob и добавляет утверждение/закрытие AC-502 и переход к AC-503.

Предыдущая редакция:

- версия: `0.37.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `95fe1f98b9f9c93cf90d8999d011eec7b37aca75`.

Все ранее определённые M0–M9, Company priority hierarchy, Company/Product/Arvectum OS boundaries, bounded AC-108 evidence loop, AC-501 workflow selection и конечный AC-901 сохраняются, если прямо не изменены более новым approved decision.

## 2. Закрытие AC-502

`AC-502 — Workflow, accountable Position, authority/data/evidence contract` имеет статус:

`Complete / PASS`.

Approved publication:

- `docs/operations/FIRST-GOVERNED-WORKFLOW-AUTHORITY-DATA-EVIDENCE-CONTRACT-v1.0.0.md` — `Approved 1.0.0`, blob `9b06e02a6d9afa8b6b4533d3a9f71690518c3ce1`;
- exact reviewed proposal: `docs/operations/FIRST-GOVERNED-WORKFLOW-AUTHORITY-DATA-EVIDENCE-CONTRACT.md` — `Proposed 0.9.0`, blob `b1df71839422e509cbfa76faec31bf788ca9842d`;
- cross-review: `docs/reviews/AC-502-FIRST-GOVERNED-WORKFLOW-CONTRACT-CROSS-REVIEW.md` — `10 of maximum 10`, `Complete / PASS for explicit Owner approval`, blob `7c457c2b3145b0f2becb3b6e289d9496e02e2d15`;
- Owner decision: `docs/governance/decisions/DECISION-2026-08-21-AC-502-APPROVAL.md`, blob `08db32414f9f19c99b281d936a5eccaa0f456ede`;
- explicit Owner wording at the pending approval gate: `делай`.

## 3. Утверждённый contract WF-M5-001

Для выбранного AC-501 workflow:

`WF-M5-001 — Customer Feedback → Classified Correction → Verified Candidate → Customer Validation / Acceptance`

в первом contour `PORT-002 — Discount Parser` утверждены:

- workflow states `W0…W11`;
- classification taxonomy `CL-1…CL-7`;
- `POS-002 — Commercial & Customer Lead` как end-to-end accountable Position;
- `POS-004 — Engineering & Release Lead` как accountable Position технического сегмента `W4 → W7`;
- existing `AM-0/AM-1/AM-2` only, без activation `AM-3`/`AM-4`;
- human-attributable initial `W3 — Classified` через current POS-002 Assignment;
- AI-led bounded engineering через POS-004 внутри existing Assignment/access ceilings;
- explicit customer acceptance/data/access/evidence/escalation/failure/continuity boundaries;
- customer/product/Company/control-register source-of-truth separation;
- lightweight M5 measurement inputs.

Ключевые инварианты:

`technical PASS ≠ customer-facing approval ≠ customer acceptance`;

`Candidate Ready ≠ permission to deploy/send/promise`;

`customer silence ≠ acceptance` без отдельного authoritative rule;

`technical task closed ≠ Company/customer obligation satisfied`.

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
| `AC-503` | Arvectum OS reliance/admission mapping where applicable | `Current` |
| `AC-504` | Bounded workflow implementation | `Planned` |
| `AC-505` | Supervised real-operation proof | `Planned` |
| `AC-506` | Incident, uncertain-outcome, recovery and fallback drill | `Planned` |
| `AC-507` | Business-value/economic review and continue/change/stop decision | `Planned` |

## 6. Текущее действие — AC-503

### AC-503 — Arvectum OS reliance/admission mapping where applicable

Статус: `Current`.

AC-503 должен определить **фактическую**, а не архитектурно желаемую, необходимость Arvectum OS для `WF-M5-001` до bounded implementation.

Минимальный scope:

1. re-check current canonical `arvectum/arvectum-os` state: Constitution, Accepted RFC/ADR/policies/Product Contracts/capability lifecycle и current roadmap/code evidence, где это применимо;
2. определить, какие части approved AC-502 workflow являются Company-owned organizational semantics и не должны переноситься в OS;
3. определить, есть ли у workflow реальная runtime/record/authority/provenance/document/knowledge/security dependency на OS;
4. проверить existing PORT-002 ↔ OS correspondence/admission evidence без вывода lifecycle state по импликации;
5. проверить Product Contract/capability admission requirements, если реальная dependency существует;
6. проверить sovereignty, portability, fallback and replacement path;
7. определить минимальный reversible integration/admission path только если он реально создаёт value или необходим для governed execution;
8. явно зафиксировать один из результатов:
   - `no additional OS reliance required for first M5 proof`;
   - `bounded existing OS reliance is sufficient`;
   - `new/changed OS contract or capability admission is required`, с отдельным OS governance path.

AC-503 не должен:

- внедрять Arvectum OS ради dogfooding;
- переносить Company-specific Position/customer/workflow semantics в OS;
- считать техническое соответствие Product Contract admission;
- создавать hidden cross-repository commitment;
- менять OS Constitution/RFC/ADR/Product Contract вне OS governance;
- преждевременно реализовывать AC-504.

## 7. M5 exit direction

M5 остаётся открытым. Он может быть закрыт только после AC-504…AC-507 и actual supervised real-operation evidence, включая:

- real governed workflow execution;
- valid Position/Assignment/authority/access behavior;
- reconstructable consequential evidence;
- actual uncertainty/failure/recovery path;
- customer/business outcome evidence;
- measured Owner intervention/reconstruction burden;
- technical/AI quality, cost and reliability evidence;
- continue/change/stop economic decision.

AC-502 approval — design/control readiness для implementation, а не empirical proof.

## 8. Authority and boundary rule

Roadmap не создаёт Organizational Authority, budget, legal/corporate authority, customer/vendor commitment, Product Contract, access grant, production approval или OS lifecycle transition.

Company workflow semantics остаются Company-owned; product implementation truth — product-owned; Arvectum OS universal platform contracts/lifecycle — OS-owned. Любая новая cross-repository dependency требует явного evidence/authority/governance path.
