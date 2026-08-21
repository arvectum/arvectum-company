# Реестр канонических источников Arvectum Company

Статус: `Active`
Версия: `3.6.0`
Обновлено: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`

## 1. Модель публикации

Эта редакция сохраняет полный реестр `3.5.0` по immutable git blob и добавляет утверждение AC-501, выбранный `WF-M5-001` и переход к AC-502.

Предыдущая редакция:

- версия: `3.5.0`;
- путь: `docs/CANONICAL-SOURCES.md`;
- immutable git blob SHA: `9171d2ef815b6a31f36da09dd940191979554369`.

Все ранее зарегистрированные Company Constitution/governance, M0–M4, AC-201…AC-407, portfolio, terminology, Company/Product/Arvectum OS boundaries, public/restricted-source rules и M4 operating cadence сохраняются, если прямо не изменены более новым approved artifact.

## 2. Порядок приоритета источников

В своей области действуют:

1. применимое право и действительные legal/corporate authorities;
2. утверждённые Company governance artifacts и явные attributable Owner decisions;
3. canonical Arvectum OS sources там, где Company фактически использует OS;
4. product repositories/decisions в пределах product scope;
5. roadmap как planning source, не источник authority;
6. chat/model memory/local copies/generated materials как context/evidence до explicit promotion.

## 3. Действующая дорожная карта

- `docs/roadmap/ROADMAP.md` — `Active 0.37.0`;
- текущий blob SHA: `95fe1f98b9f9c93cf90d8999d011eec7b37aca75`.

Текущее каноническое действие:

`AC-502 — Workflow, accountable Position, authority/data/evidence contract`.

Текущий milestone:

`M5 — First real governed Company operating contour proven`.

## 4. Approved AC-501

Canonical Approved publication:

- `docs/operations/FIRST-GOVERNED-WORKFLOW-CANDIDATE-SELECTION-v1.0.0.md` — `Approved 1.0.0`;
- immutable publication blob SHA: `c0e1bd3a0e247ef72cb79ebd988d78d4487618f7`.

Exact reviewed proposal:

- `docs/operations/FIRST-GOVERNED-WORKFLOW-CANDIDATE-SELECTION.md` — `Proposed 0.9.0`;
- immutable proposal blob SHA: `f6cbebfea1c2e6a56a0fd03c38b68a7211c6bbde`.

Cross-review:

- `docs/reviews/AC-501-FIRST-GOVERNED-WORKFLOW-CANDIDATE-SELECTION-CROSS-REVIEW.md`;
- `10 of maximum 10`;
- `Complete / PASS for explicit Owner approval`;
- immutable blob SHA: `10924469f889d9e97d6a6d11b61d57a70b69e22a`.

Owner decision:

- `docs/governance/decisions/DECISION-2026-08-21-AC-501-APPROVAL.md` — `Approved`;
- immutable blob SHA: `04d42d227c74c779e58d4298ad542e458821837b`;
- explicit Owner wording at the pending approval gate: `делай`.

`AC-501` — `Complete / PASS`.

## 5. First governed workflow selection

Первый выбранный M5 workflow:

`WF-M5-001 — Customer Feedback → Classified Correction → Verified Candidate → Customer Validation / Acceptance`.

Первый real-operation contour:

`PORT-002 — Discount Parser`.

Company authoritative scope здесь ограничен выбором workflow, accountable/authority/evidence semantics и M5 proof.

Product-specific implementation/status/domain truth остаётся в `arvectum/discount-parser`.

Выбор не создаёт customer commitment, budget/spend authority, portfolio reallocation, production-readiness claim, new Assignment/access grant или Arvectum OS dependency.

## 6. M5 navigation

M5 current sequence:

1. `AC-501` — First governed workflow candidate selection — `Complete / PASS`;
2. `AC-502` — Workflow, accountable Position, authority/data/evidence contract — `Current`;
3. `AC-503` — Arvectum OS reliance/admission mapping where applicable — `Planned`;
4. `AC-504` — Bounded workflow implementation — `Planned`;
5. `AC-505` — Supervised real-operation proof — `Planned`;
6. `AC-506` — Incident, uncertain-outcome, recovery and fallback drill — `Planned`;
7. `AC-507` — Business-value/economic review and continue/change/stop decision — `Planned`.

AC-502 должен сначала определить Company workflow contract. Arvectum OS reliance не выводится автоматически из наличия current P6.06/CAP-004 correspondence у PORT-002.

## 7. Authority and source-of-truth boundary for WF-M5-001

Продолжают применяться:

- AC-202 `ROD-01…ROD-09`;
- AC-203 `AM-0…AM-4` semantics;
- AC-204 Position Registry;
- AC-205 Assignment baseline;
- AC-206 access boundary;
- AC-207 continuity/fallback baseline;
- AC-401…AC-407 Company operating-control baseline.

Customer feedback/evidence остаётся customer-scoped source evidence. Customer validation/acceptance не может быть выведено только из technical PASS или internal workflow completion.

`arvectum/discount-parser` остаётся canonical для product implementation/status/domain semantics.

`arvectum/arvectum-os` остаётся canonical для Product Contracts/platform capabilities/governance. Exact OS reliance/admission mapping — AC-503.

## 8. Current Arvectum OS check boundary

Для AC-501 использован current checked Arvectum OS `main` commit:

`76504766353028540891ac1dfdbf1e5dc331a4af`.

Этот check подтверждает только отсутствие необходимости создавать OS reliance по импликации на этапе selection. Он не является будущим AC-503 admission decision и должен быть повторён, если current OS state materially изменится к AC-503.

## 9. Public repository boundary

Публичный Company repository не должен содержать secrets, reusable credentials, private keys/signatures, unnecessary PII, bank/payment payloads, transaction exports, confidential exact cash balances, non-public customer/vendor/contract materials, sensitive tax/accounting documents, privileged payment/fraud/incident/security details или chain-of-thought.

Для `WF-M5-001` public Company artifacts должны хранить только минимальные governance/evidence references и sanitized operational meaning. Raw customer evidence и confidential payload остаются в соответствующем authorized contour.

## 10. Final planned language stage

`M9 — Человекочитаемая документация полностью русифицирована и согласована` remains the final planned stage after M8 unless the Owner explicitly changes sequence.

`AC-901 — Полная русификация человекочитаемой документации и итоговая междокументная сверка` remains `Planned`.
