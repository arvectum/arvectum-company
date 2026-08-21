# Реестр канонических источников Arvectum Company

Статус: `Active`
Версия: `3.3.0`
Обновлено: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`

## 1. Модель публикации

Эта редакция сохраняет полный реестр `3.2.0` по immutable git blob и добавляет утверждение AC-405 и переход к AC-406.

Предыдущая редакция:

- версия: `3.2.0`;
- путь: `docs/CANONICAL-SOURCES.md`;
- immutable git blob SHA: `96e927705f5e40df2cf39763fcfdd79fd878c4d2`.

Все ранее зарегистрированные источники M0–M3, AC-201–AC-404, языково-терминологическая политика, Company/Product/Arvectum OS boundaries и правила внешних источников сохраняются без изменений, если прямо не уточнены более новым утверждённым артефактом.

## 2. Порядок приоритета источников

В своей области действуют:

1. применимое право и действительные юридические/корпоративные полномочия;
2. утверждённые документы управления Arvectum Company и явные решения собственника;
3. канонические документы Arvectum OS там, где Company фактически использует OS;
4. продуктовые репозитории и продуктовые решения в пределах продуктовой области;
5. дорожная карта как средство планирования, а не самостоятельный источник полномочий;
6. чаты, память модели, локальные копии и сгенерированные материалы как context/evidence, если они не были явно повышены до канонического источника.

## 3. Действующая дорожная карта

Канонический источник планирования:

- `docs/roadmap/ROADMAP.md` — `Active 0.34.0`;
- текущий blob SHA: `de67144e8e0650fb8290145bd5049d16f7020a1e`.

Текущее каноническое действие:

`AC-406 — Owner Mission Control / reference-implementation evidence view`.

Текущий этап:

`M4 — Owner control and reference-implementation observability established`.

## 4. Approved AC-401 work/obligation model

- publication: `docs/operations/COMPANY-WORK-OBLIGATION-REGISTER-MODEL-v1.0.0.md` — `Approved 1.0.0`, blob `fa9f513b1434c7eda257ac412bf7472da400519d`;
- exact reviewed proposal blob: `0f4444fbd968e176a0a158771a7d0abe93549ecd`.

AC-401 устанавливает `WORK-*`/`OBL-*` как Company-level control identities и не заменяет underlying legal/accounting/customer/product/OS truth.

## 5. Approved AC-402 decision/approval/escalation model

- publication: `docs/operations/COMPANY-DECISION-APPROVAL-ESCALATION-REGISTER-MODEL-v1.0.0.md` — `Approved 1.0.0`, blob `ae013d7e93dc51573f56b1ded2e907ee58182e57`;
- exact reviewed proposal blob: `a48081ba3599e6f3c91b8a6562435ad1f0c152f4`;
- cross-review blob: `82cf1046178cde22387a04037e86cf7e1b224f9a`;
- Owner decision blob: `30dbae9a081b1dc1939923083b31e3f40be2a80c`.

AC-402 устанавливает `DEC-*`/`APR-*`/`ESC-*` и правило:

`recommendation ≠ decision ≠ approval ≠ legal/corporate act ≠ technical authorization ≠ execution`.

## 6. Approved AC-403 risk/exception/incident model

- publication: `docs/operations/COMPANY-RISK-EXCEPTION-INCIDENT-REGISTER-MODEL-v1.0.0.md` — `Approved 1.0.0`, blob `effef94f950d6d070c421a22c2eced00b5e561ad`;
- exact reviewed proposal blob: `857b601423f78fc3d4636dbf9754d5410d8a1c55`;
- cross-review blob: `37241051876a94f71035e532e19ed9cf69b4c785`;
- Owner decision blob: `524cad548204d8721117989f3940f3295ab7d932`.

AC-403 устанавливает `RSK-*`/`EXC-*`/`INC-*` и границы:

`risk evidence ≠ accepted risk`

`exception request ≠ approved exception`

`incident detection ≠ authority to act`

`containment ≠ risk acceptance`.

## 7. Approved AC-404 cash/commitment/management-reporting baseline

- publication: `docs/operations/COMPANY-CASH-COMMITMENT-MANAGEMENT-REPORTING-BASELINE-v1.0.0.md` — `Approved 1.0.0`, blob `519330a5460ef9c712d7e6045dbb07475b021954`;
- exact reviewed proposal blob: `80c7b620cf446ed28b76143a0325ce89b1939ac0`;
- cross-review blob: `3519f63ef7c09f075aa75b6d0d83ccd770911141`;
- Owner decision blob: `8e6ea741f14bb6471d250c6d39a76f15bdfb8ff3`.

Главное разделение AC-404:

`bank/accounting fact ≠ management interpretation ≠ forecast ≠ budget/limit ≠ planned spend ≠ approved internal commitment ≠ incurred obligation ≠ actual payment`.

AC-404 не создаёт parallel transaction ledger или spend/payment authority.

## 8. Approved AC-405 portfolio/module/priority review cadence

Каноническая approved publication:

- `docs/portfolio/AC-405-PORTFOLIO-MODULE-PRIORITY-REVIEW-CADENCE-v1.0.0.md` — `Approved 1.0.0`;
- immutable publication blob SHA: `8150c0b8ff009941220dd6d0ce48d721eb9e42d9`.

Exact reviewed proposal:

- `docs/portfolio/AC-405-PORTFOLIO-MODULE-PRIORITY-REVIEW-CADENCE.md` — `Proposed 0.9.0`;
- immutable proposal blob SHA: `13d19b2a5418c2d1d3349e889fe54817dd9ee126`.

Cross-review:

- `docs/reviews/AC-405-PORTFOLIO-MODULE-PRIORITY-REVIEW-CADENCE-CROSS-REVIEW.md`;
- `8 iterations`;
- `Complete / PASS for Owner approval`;
- immutable blob SHA: `1192472888da43de4160499d828e5def87391197`.

Owner decision:

- `docs/governance/decisions/DECISION-2026-08-21-AC-405-APPROVAL.md` — `Approved`;
- immutable blob SHA: `76bc7b8f9c560c3e2a3baf18b58c13de009e8eb4`;
- explicit wording: `AC-405 утверждаю`.

AC-405 является binding Company portfolio-review baseline в своём declared scope.

## 9. AC-405 canonicality and authority boundary

AC-405 устанавливает:

- immediate scoped review при material event;
- monthly asynchronous exception scan как initial light backstop;
- quarterly integrated portfolio revalidation как initial broader backstop;
- возможность корректировки cadence последующим operating evidence;
- `POS-003` `AM-2` stewardship только внутри уже approved envelope;
- material portfolio/module/investment/boundary changes только через applicable `DEC/APR/ROD` path.

Ключевые границы:

`review ≠ decision ≠ approval ≠ investment ≠ product roadmap change ≠ OS lifecycle change`

`P0 temporary execution priority ≠ permanent portfolio reclassification`

`named trigger ≠ automatic promotion/funding`

`reference/reuse evidence ≠ automatic module admission`.

AC-405 не меняет текущие `PORT-*` treatments по факту approval.

## 10. Действующий портфель и статус этапов

Канонический Company-level portfolio source:

- `docs/portfolio/PORTFOLIO.md` — `Active 0.8.0`;
- текущий blob SHA: `8a77be35225f9c4958531e52a4131abda13d0f`;
- governance baseline: `AC-307 — Approved 1.0.0 / M3 Complete / PASS`.

Статус этапов:

- `M0` — `Complete / PASS`;
- `M1` — `Complete / PASS`;
- `M2` — `Complete / PASS`;
- `M3` — `Complete / PASS`;
- `M4` — `Current`, AC-406 `Current`;
- `M5` — `Planned`;
- `M6` — `Planned`;
- `M7` — `Future`;
- `M8` — `Future`;
- `M9` — финальный плановый этап, AC-901 `Planned` после M8.

## 11. M4 navigation

M4 проходит так:

1. `AC-401` — work/obligation register model — `Complete / PASS`;
2. `AC-402` — decision/approval/escalation register model — `Complete / PASS`;
3. `AC-403` — risk/exception/incident register model — `Complete / PASS`;
4. `AC-404` — cash/commitment/management reporting baseline — `Complete / PASS`;
5. `AC-405` — portfolio/module/priority review cadence — `Complete / PASS`;
6. `AC-406` — Owner Mission Control / reference-implementation evidence view — `Current`;
7. `AC-407` — management operating cadence and control review.

Approved control models сами по себе не доказывают полноту live register population, current cash/liquidity, absence of risks/incidents, profitability, portfolio thesis validity или business readiness. Такие факты требуют current authoritative evidence.

## 12. Arvectum OS boundary

Company-specific control, management-finance и portfolio-review semantics принадлежат `arvectum/arvectum-company`.

При AC-405 current OS state был проверен на `76504766353028540891ac1dfdbf1e5dc331a4af`. OS M9-alpha остаётся `Achieved / PASS` только в exact private internal workspace scope; P9.07 был current на момент review. Это не создаёт Company portfolio authority, reusable module, Stable Product Contract или capability lifecycle state.

Arvectum OS MAY позднее предоставлять domain-neutral persistence/projection/composition/governed-execution mechanisms через отдельный admitted boundary. UI/runtime visibility не создаёт Company Organizational Authority.

## 13. Язык, терминология и публичная граница

Для новых человекочитаемых Company-документов действует русскоязычный режим и `docs/governance/TERMINOLOGY-GLOSSARY.md`.

Публичный Company repository не является местом хранения secrets, reusable credentials, private keys, signatures, избыточных персональных данных, банковских/платёжных payloads, transaction exports, confidential exact cash balances, непубличных договорных/customer/vendor материалов, sensitive tax/accounting documents, privileged payment/fraud или incident/security details и chain-of-thought.

## 14. Конечный этап M9

`M9 — Человекочитаемая документация полностью русифицирована и согласована` остаётся самым последним плановым этапом после M8, если собственник отдельно не изменит последовательность.

`AC-901 — Полная русификация человекочитаемой документации и итоговая междокументная сверка` остаётся `Planned`.