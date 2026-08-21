# Реестр канонических источников Arvectum Company

Статус: `Active`
Версия: `3.8.0`
Обновлено: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`

## 1. Модель публикации

Эта редакция сохраняет полный реестр `3.7.0` по immutable git blob и добавляет утверждение AC-503, approved no-additional-OS-reliance decision и переход к AC-504.

Предыдущая редакция:

- версия: `3.7.0`;
- путь: `docs/CANONICAL-SOURCES.md`;
- immutable git blob SHA: `bdd98d86354bdc86c9e418b0239c762ce14daac5`.

Все ранее зарегистрированные Company Constitution/governance, M0–M4, AC-201…AC-502, portfolio, terminology, Company/Product/Arvectum OS boundaries, public/restricted-source rules и operating-control baseline сохраняются, если прямо не изменены более новым approved artifact.

## 2. Порядок приоритета источников

В своей области действуют:

1. применимое право и действительные legal/corporate authorities;
2. утверждённые Company governance artifacts и явные attributable Owner decisions;
3. canonical Arvectum OS sources там, где Company фактически использует OS;
4. product repositories/decisions в пределах product scope;
5. roadmap как planning source, не источник authority;
6. chat/model memory/local copies/generated materials как context/evidence до explicit promotion.

## 3. Действующая дорожная карта

- `docs/roadmap/ROADMAP.md` — `Active 0.39.0`;
- текущий blob SHA: `5e7cc89eb384ea0fc1cf6cb74cf30d0e55338d33`.

Текущее каноническое действие:

`AC-504 — Bounded workflow implementation`.

Текущий milestone:

`M5 — First real governed Company operating contour proven`.

## 4. Approved AC-503

Canonical Approved publication:

- `docs/operations/FIRST-GOVERNED-WORKFLOW-ARVECTUM-OS-RELIANCE-ADMISSION-MAPPING-v1.0.0.md` — `Approved 1.0.0`;
- immutable publication blob SHA: `8984d4c094da87a2c9d201fd9cffcd617c641f8f`.

Exact reviewed proposal:

- `docs/operations/FIRST-GOVERNED-WORKFLOW-ARVECTUM-OS-RELIANCE-ADMISSION-MAPPING.md` — `Proposed 0.9.0`;
- immutable proposal blob SHA: `3b7bef8f227d17990ced164aa0de16874bb2ec61`.

Cross-review:

- `docs/reviews/AC-503-FIRST-GOVERNED-WORKFLOW-ARVECTUM-OS-RELIANCE-CROSS-REVIEW.md`;
- `10 of 10`;
- `Complete / PASS for explicit Owner approval`;
- immutable blob SHA: `67623301fbc2a370433d94952ee3ed6c2f0ef608`.

Owner decision:

- `docs/governance/decisions/DECISION-2026-08-21-AC-503-APPROVAL.md` — `Approved`;
- immutable blob SHA: `5197aa78a48d5d4373f6bf24e887bf58607d2d75`;
- exact Owner wording: `AC-503 утверждаю`.

`AC-503` — `Complete / PASS`.

## 5. Binding AC-503 result

For the first M5 proof of:

`WF-M5-001 — Customer Feedback → Classified Correction → Verified Candidate → Customer Validation / Acceptance`

in first contour:

`PORT-002 — Discount Parser`

binding Company result is:

**`NO-ADDITIONAL-OS-RELIANCE — no additional Arvectum OS reliance required for the first M5 proof of WF-M5-001`.**

This means:

- first proof may use Company/product/customer-owned sources and current authorized tools;
- OS Execution Context/shared history/CAP-004 are not mandatory for first proof;
- no new/changed OS Product Contract is required unless actual implementation crosses a governed-reliance trigger;
- existing P6.06 remains unchanged in its controlled Telegram publication/reconstruction scope;
- no Product Contract or Platform Capability lifecycle transition is implied;
- OS-neutral exact evidence/version references are required so later admitted reliance remains possible and reversible.

This is a bounded first-proof decision, not a general policy against Arvectum OS.

## 6. Arvectum OS decision baseline

AC-503 re-checked `arvectum/arvectum-os` at commit:

`76504766353028540891ac1dfdbf1e5dc331a4af`.

Decision-time current facts included:

- Constitution `1.2.0` — `Ratified`;
- RFC-0001…RFC-0008 — `Accepted 1.0.0`;
- OS roadmap `2.81.0`, current `P9.07`;
- CAP-001…CAP-004 — `Incubating / Provisional`;
- P6.06 — `Provisional 0.1.0` in its exact scope.

This commit is evidence of the decision-time re-check only. If AC-504 or later work triggers actual OS reliance, then-current OS canonical state must be checked again before consequential reliance.

## 7. Source-of-truth and data boundary

Company repository remains canonical for Company governance semantics of WF-M5-001.

It does not replace:

- `arvectum/discount-parser` for product implementation/status/domain truth;
- customer/workstream sources for raw feedback and customer validation/acceptance evidence;
- legal/corporate sources for legal acts/obligations;
- Arvectum OS canonical sources for platform contracts/lifecycle;
- AC-401/402/403 control records where their material qualification rules trigger.

Public Company artifacts store only public-safe references/sanitized meaning. Raw customer `DC-2` remains protected by default; reusable `DC-3` secrets do not enter ordinary AI/model context.

## 8. Authority and continuity boundary

AC-503 creates no Organizational Authority or access.

Existing AC-202…AC-207 remain controlling, as do AC-401…AC-407 and AC-502. In particular:

- technical access does not create authority;
- AI/software does not become a Principal;
- POS-004 technical PASS does not create customer-facing approval/acceptance;
- POS-002/Owner unavailability does not transfer their authority to AI;
- manual fallback remains valid without authority transfer;
- actual incident/recovery/fallback drill remains AC-506 evidence work.

## 9. Re-admission triggers

Re-open Company↔OS reliance mapping before consequential use if actual implementation requires, rather than merely benefits from:

- shared OS canonical state;
- OS Execution Context / Governed Execution;
- CAP-004 or another Platform Capability as material control dependency;
- Productive Workspace as admitted operating surface;
- OS-held Organization/Actor/authorization enforcement;
- shared OS event/provenance history;
- stronger domain-neutral enforcement for later AM-4/autonomy;
- deliberate evidence migration into OS canonical/replica semantics;
- validated cross-product reusable platform demand.

Any such path must use applicable current OS Product Contract/capability/RFC/ADR governance before reliance. Hidden coupling is prohibited.

## 10. M5 navigation

1. `AC-501` — First governed workflow candidate selection — `Complete / PASS`;
2. `AC-502` — Workflow, accountable Position, authority/data/evidence contract — `Complete / PASS`;
3. `AC-503` — Arvectum OS reliance/admission mapping where applicable — `Complete / PASS`;
4. `AC-504` — Bounded workflow implementation — `Current`;
5. `AC-505` — Supervised real-operation proof — `Planned`;
6. `AC-506` — Incident, uncertain-outcome, recovery and fallback drill — `Planned`;
7. `AC-507` — Business-value/economic review and continue/change/stop decision — `Planned`.

## 11. AC-504 boundary

AC-504 must implement the smallest reversible OS-neutral mechanics needed to operate one real WF-M5-001 case and capture reconstructable evidence.

It must not build a generic workflow engine/event bus/Company-wide platform abstraction, create autonomous consequential authority, expand P6.06, or treat technical PASS as AC-505/M5 proof.

If implementation uncovers an actual OS-reliance trigger, AC-504 must stop at that boundary and re-open the applicable admission/governance path.

## 12. Public repository boundary

Публичный Company repository не должен содержать secrets, reusable credentials, private keys/signatures, unnecessary PII, bank/payment payloads, transaction exports, confidential exact cash balances, non-public customer/vendor/contract materials, sensitive tax/accounting documents, privileged payment/fraud/incident/security details или chain-of-thought.

## 13. Final planned language stage

`M9 — Человекочитаемая документация полностью русифицирована и согласована` remains the final planned stage after M8 unless the Owner explicitly changes sequence.

`AC-901 — Полная русификация человекочитаемой документации и итоговая междокументная сверка` remains `Planned`.