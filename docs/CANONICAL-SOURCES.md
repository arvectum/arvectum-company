# Реестр канонических источников Arvectum Company

Статус: `Active`
Версия: `3.7.0`
Обновлено: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`

## 1. Модель публикации

Эта редакция сохраняет полный реестр `3.6.0` по immutable git blob и добавляет утверждение AC-502, binding workflow contract `WF-M5-001` и переход к AC-503.

Предыдущая редакция:

- версия: `3.6.0`;
- путь: `docs/CANONICAL-SOURCES.md`;
- immutable git blob SHA: `288604a53ec8de8b1e743a9aaa005bb50bfd6c3d`.

Все ранее зарегистрированные Company Constitution/governance, M0–M4, AC-201…AC-501, portfolio, terminology, Company/Product/Arvectum OS boundaries, public/restricted-source rules и operating-control baseline сохраняются, если прямо не изменены более новым approved artifact.

## 2. Порядок приоритета источников

В своей области действуют:

1. применимое право и действительные legal/corporate authorities;
2. утверждённые Company governance artifacts и явные attributable Owner decisions;
3. canonical Arvectum OS sources там, где Company фактически использует OS;
4. product repositories/decisions в пределах product scope;
5. roadmap как planning source, не источник authority;
6. chat/model memory/local copies/generated materials как context/evidence до explicit promotion.

## 3. Действующая дорожная карта

- `docs/roadmap/ROADMAP.md` — `Active 0.38.0`;
- текущий blob SHA: `44b265a3a1816352eb66bd7e7252328f58bede24`.

Текущее каноническое действие:

`AC-503 — Arvectum OS reliance/admission mapping where applicable`.

Текущий milestone:

`M5 — First real governed Company operating contour proven`.

## 4. Approved AC-502

Canonical Approved publication:

- `docs/operations/FIRST-GOVERNED-WORKFLOW-AUTHORITY-DATA-EVIDENCE-CONTRACT-v1.0.0.md` — `Approved 1.0.0`;
- immutable publication blob SHA: `9b06e02a6d9afa8b6b4533d3a9f71690518c3ce1`.

Exact reviewed proposal:

- `docs/operations/FIRST-GOVERNED-WORKFLOW-AUTHORITY-DATA-EVIDENCE-CONTRACT.md` — `Proposed 0.9.0`;
- immutable proposal blob SHA: `b1df71839422e509cbfa76faec31bf788ca9842d`.

Cross-review:

- `docs/reviews/AC-502-FIRST-GOVERNED-WORKFLOW-CONTRACT-CROSS-REVIEW.md`;
- `10 of maximum 10`;
- `Complete / PASS for explicit Owner approval`;
- immutable blob SHA: `7c457c2b3145b0f2becb3b6e289d9496e02e2d15`.

Owner decision:

- `docs/governance/decisions/DECISION-2026-08-21-AC-502-APPROVAL.md` — `Approved`;
- immutable blob SHA: `08db32414f9f19c99b281d936a5eccaa0f456ede`;
- explicit Owner wording at the pending approval gate: `делай`.

`AC-502` — `Complete / PASS`.

## 5. Binding WF-M5-001 contract

Workflow:

`WF-M5-001 — Customer Feedback → Classified Correction → Verified Candidate → Customer Validation / Acceptance`.

First application contour:

`PORT-002 — Discount Parser`.

Binding Company semantics now include:

- workflow states `W0…W11`;
- classification `CL-1…CL-7`;
- `POS-002` end-to-end accountability;
- `POS-004` technical-segment accountability `W4 → W7`;
- initial human-attributable routine classification under current POS-002 Assignment;
- AI-led bounded engineering under POS-004 within existing `AM-0/1/2` and access ceilings;
- no `AM-3`/`AM-4` activation;
- explicit customer acceptance, data/access, evidence, escalation/failure and continuity boundaries.

Important invariants:

`technical PASS ≠ customer-facing approval ≠ customer acceptance`;

`Candidate Ready ≠ permission to deploy/send/promise`;

`customer silence ≠ acceptance` without stronger authoritative rule;

`technical task closed ≠ Company/customer obligation satisfied`.

## 6. Source-of-truth and data boundary

Company repository is canonical for the approved Company workflow governance semantics only.

It does not replace:

- `arvectum/discount-parser` for product implementation/status/domain truth;
- customer/workstream sources for raw feedback and customer validation/acceptance evidence;
- legal/corporate sources for legal acts/obligations;
- Arvectum OS canonical sources for Product Contracts/platform lifecycle;
- AC-401/402/403 registers where material control records are required.

Public Company artifacts store only public-safe references/sanitized meaning. Raw customer `DC-2` remains protected by default; reusable `DC-3` secrets do not enter ordinary AI/model context.

## 7. Authority and continuity boundary

AC-502 does not create Organizational Authority or access.

Existing AC-202…AC-207 remain controlling. In particular:

- `ROD-01…ROD-09` are unchanged;
- workflow participation does not broaden an Assignment;
- credential possession does not create authority;
- POS-002/Owner unavailability does not transfer customer/Owner authority to AI;
- POS-004 runtime replacement preserves Position meaning only inside valid Assignment/access conditions;
- actual incident/recovery/fallback drill remains AC-506 evidence work.

## 8. M5 navigation

1. `AC-501` — First governed workflow candidate selection — `Complete / PASS`;
2. `AC-502` — Workflow, accountable Position, authority/data/evidence contract — `Complete / PASS`;
3. `AC-503` — Arvectum OS reliance/admission mapping where applicable — `Current`;
4. `AC-504` — Bounded workflow implementation — `Planned`;
5. `AC-505` — Supervised real-operation proof — `Planned`;
6. `AC-506` — Incident, uncertain-outcome, recovery and fallback drill — `Planned`;
7. `AC-507` — Business-value/economic review and continue/change/stop decision — `Planned`.

## 9. AC-503 boundary

AC-503 must re-check current canonical Arvectum OS state and determine actual reliance/admission need for `WF-M5-001`.

Valid results include:

- `no additional OS reliance required for first M5 proof`;
- bounded existing reliance is sufficient;
- new/changed OS Product Contract/capability admission is required through the proper OS governance path.

AC-503 must not force OS integration for dogfooding, move Company-specific Position/customer/workflow semantics into OS, or infer lifecycle state from technical correspondence.

## 10. Public repository boundary

Публичный Company repository не должен содержать secrets, reusable credentials, private keys/signatures, unnecessary PII, bank/payment payloads, transaction exports, confidential exact cash balances, non-public customer/vendor/contract materials, sensitive tax/accounting documents, privileged payment/fraud/incident/security details или chain-of-thought.

## 11. Final planned language stage

`M9 — Человекочитаемая документация полностью русифицирована и согласована` remains the final planned stage after M8 unless the Owner explicitly changes sequence.

`AC-901 — Полная русификация человекочитаемой документации и итоговая междокументная сверка` remains `Planned`.
