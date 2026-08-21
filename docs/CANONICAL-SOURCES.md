# Реестр канонических источников Arvectum Company

Статус: `Active`
Версия: `3.9.0`
Обновлено: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`

## 1. Модель публикации

Эта редакция сохраняет полный реестр `3.8.0` по immutable git blob и добавляет AC-504 bounded implementation/evidence/cross-review и переход к AC-505.

Предыдущая редакция:

- версия: `3.8.0`;
- путь: `docs/CANONICAL-SOURCES.md`;
- immutable git blob SHA: `7b7a2092f19d96719cef5e430378c16b98656f5d`.

Все ранее зарегистрированные Company Constitution/governance, M0–M4, AC-201…AC-503, portfolio, terminology, Company/Product/Arvectum OS boundaries, public/restricted-source rules и operating-control baseline сохраняются, если прямо не изменены более новым approved artifact/evidence.

## 2. Порядок приоритета источников

В своей области действуют:

1. применимое право и действительные legal/corporate authorities;
2. утверждённые Company governance artifacts и явные attributable Owner decisions;
3. canonical Arvectum OS sources там, где Company фактически использует OS;
4. product repositories/decisions в пределах product scope;
5. verified Company implementation/evidence внутри approved governance boundary;
6. roadmap как planning source, не источник authority;
7. chat/model memory/local copies/generated materials как context/evidence до explicit promotion.

Implementation evidence не создаёт authority и не заменяет external/customer/product source of truth.

## 3. Действующая дорожная карта

- `docs/roadmap/ROADMAP.md` — `Active 0.40.0`;
- текущий blob SHA: `069a08d22f0d0bc5b9f8a6e71c6d3f0c64870eb9`.

Текущее каноническое действие:

`AC-505 — Supervised real-operation proof`.

Текущий milestone:

`M5 — First real governed Company operating contour proven`.

## 4. AC-504 implementation evidence

Canonical implementation evidence:

- `docs/operations/AC-504-BOUNDED-WORKFLOW-IMPLEMENTATION-EVIDENCE.md` — `Complete / PASS 1.0.0`;
- immutable blob SHA: `ad3855fc08448dbb190b1d486f255e5592f59d71`;
- exact implementation payload head: `8aa82ccfe49001063e8416c21bf673bfa3941b26`.

Cross-review:

- `docs/reviews/AC-504-BOUNDED-WORKFLOW-IMPLEMENTATION-CROSS-REVIEW.md`;
- `10 of 10`;
- result: `PASS for AC-505 transition`;
- immutable blob SHA: `f18251a813a002fdeb2e1c7d066ec5c9c34287f4`.

`AC-504` — `Complete / PASS`.

No separate Owner decision is required for AC-504 closure because implementation remains inside the exact AC-502/AC-503 approved scope, creates no new Reserved Owner Decision, no AM-3/AM-4 authority, no budget/customer commitment and no Arvectum OS lifecycle/contract transition.

## 5. AC-504 implementation artifacts

Exact bounded implementation artifacts:

| Artifact | Immutable blob SHA | Canonical role |
|---|---|---|
| `tools/wf_m5_001_case.py` | `19373811e761226c3e418fa1b8086828c9caded6` | replaceable OS-neutral case/evidence helper |
| `tests/test_wf_m5_001_case.py` | `14e20464fd2aea2d0b85c5b286950ae7ac55f86a` | scoped regression/negative-path evidence definition |
| `.github/workflows/wf-m5-001-case.yml` | `f09e3969cb4e56cdc8cc59917439bb4ee32d493e` | repeatable regression command, not authority |
| `docs/operations/WF-M5-001-BOUNDED-IMPLEMENTATION-RUNBOOK.md` | `c51b522d66ce80ca4e2e46e5494fa32c3301ee27` | operator procedure for supervised case handling |
| `docs/operations/WF-M5-001-CASE-TEMPLATE.json` | `b66fc43e1fa47e13c5f251588324a7a813bfd9fa` | manual fallback representation |
| `.gitignore` | `516cb25b279ec91757230e37242ecb3fbd38f060` | prevents default `.local/` case storage from entering git |

Executed AC-504 test evidence:

`7 tests / 7 PASS / 0 failures / 0 errors` using the local-equivalent unittest command recorded in AC-504 evidence.

No remote GitHub Actions run is claimed as AC-504 execution evidence.

## 6. Binding governance pins carried into implementation

The helper pins:

- AC-502 Approved publication blob `9b06e02a6d9afa8b6b4533d3a9f71690518c3ce1`;
- AC-502 exact reviewed proposal blob `b1df71839422e509cbfa76faec31bf788ca9842d`;
- AC-503 Approved publication blob `8984d4c094da87a2c9d201fd9cffcd617c641f8f`;
- workflow `WF-M5-001 / 1.0.0`;
- first contour `PORT-002 / arvectum/discount-parser`;
- default product baseline at implementation start `a8c1b29702a8ce40bd30b5d972ac2541367900e1`.

AC-503 binding result remains:

`NO-ADDITIONAL-OS-RELIANCE` for the first M5 proof.

AC-504 does not alter this result.

## 7. Source-of-truth and data boundary

Company repository is canonical for approved Company workflow semantics and the bounded helper/runbook/evidence definition.

It is **not** canonical for:

- raw customer feedback, screenshots, confidential environment or acceptance payloads;
- Discount Parser implementation/issues/PRs/commits/tests/build/release truth;
- legal/corporate facts outside Company governance artifacts;
- Arvectum OS Product Contracts/platform capability lifecycle.

Real AC-505 case records default to `.local/wf-m5-001/` and must not be committed merely because they exist locally.

Public Company artifacts use protected opaque customer references and sanitized summaries. `DC-3` reusable secrets remain prohibited from ordinary model/helper context. The helper secret-pattern guard is not a comprehensive DLP/compliance system.

## 8. Authority boundary

AC-504 software does not create Organizational Authority.

Binding operational limits remain:

- Company/customer gates are attributable to current POS-002 human Principal;
- technical execution is bounded to POS-004 existing Assignment/access;
- only `AM-0/AM-1/AM-2` are admitted by helper v1;
- `AM-3/AM-4` are not activated;
- Candidate Ready does not authorize handoff/deploy/promise;
- customer acceptance requires real explicit authoritative customer evidence;
- credentials/access do not create authority.

## 9. Current AC-505 evidence rule

AC-505 must use an **actual** customer/workstream feedback source and actual product technical evidence. A synthetic/demo case cannot satisfy AC-505.

The public-safe AC-505 evidence should preserve references sufficient to verify:

- real source existed;
- exact case/workflow/product baseline;
- attributable POS-002 classification/customer gates;
- bounded POS-004 technical execution if performed;
- real product issue/PR/commit/test/build/release-candidate evidence;
- explicit handoff/customer validation evidence where reached;
- honest blocked/rework/unknown/stale/uncertain state where applicable;
- lightweight Owner intervention/cycle/rework evidence.

Technical/unit-test PASS alone is not AC-505 or M5 proof.

## 10. M5 navigation

1. `AC-501` — candidate selection — `Complete / PASS`;
2. `AC-502` — workflow/Position/authority/data/evidence contract — `Complete / PASS`;
3. `AC-503` — OS reliance/admission mapping — `Complete / PASS`;
4. `AC-504` — bounded workflow implementation — `Complete / PASS`;
5. `AC-505` — supervised real-operation proof — `Current`;
6. `AC-506` — incident/uncertain-outcome/recovery/fallback drill — `Planned`;
7. `AC-507` — business-value/economic continue/change/stop — `Planned`.

## 11. Public repository boundary

Публичный Company repository не должен содержать secrets, reusable credentials, private keys/signatures, unnecessary PII, bank/payment payloads, transaction exports, confidential exact cash balances, non-public customer/vendor/contract materials, sensitive tax/accounting documents, privileged payment/fraud/incident/security details или chain-of-thought.

## 12. Final planned language stage

`M9 — Человекочитаемая документация полностью русифицирована и согласована` remains the final planned stage after M8 unless the Owner explicitly changes sequence.

`AC-901 — Полная русификация человекочитаемой документации и итоговая междокументная сверка` remains `Planned`.
