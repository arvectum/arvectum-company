# Реестр канонических источников Arvectum Company

Статус: `Active`
Версия: `3.2.0`
Обновлено: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`

## 1. Модель публикации

Эта редакция сохраняет полный реестр `3.1.0` по immutable git blob и добавляет утверждение AC-404 и переход к AC-405.

Предыдущая редакция:

- версия: `3.1.0`;
- путь: `docs/CANONICAL-SOURCES.md`;
- immutable git blob SHA: `8e1022670568fb697a307cb3a1988226dbce8e4b`.

Все ранее зарегистрированные источники M0–M3, AC-201–AC-403, языково-терминологическая политика, Company/Product/Arvectum OS boundaries и правила внешних источников сохраняются без изменений, если прямо не уточнены более новым утверждённым артефактом.

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

- `docs/roadmap/ROADMAP.md` — `Active 0.33.0`;
- текущий blob SHA: `a409b059771f78d26dc529cc5d8bee74acfadfc6`.

Текущее каноническое действие:

`AC-405 — Portfolio/module/priority review cadence`.

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

Каноническая approved publication:

- `docs/operations/COMPANY-CASH-COMMITMENT-MANAGEMENT-REPORTING-BASELINE-v1.0.0.md` — `Approved 1.0.0`;
- immutable publication blob SHA: `519330a5460ef9c712d7e6045dbb07475b021954`.

Exact reviewed proposal:

- `docs/operations/COMPANY-CASH-COMMITMENT-MANAGEMENT-REPORTING-BASELINE.md` — `Proposed 0.9.0`;
- immutable proposal blob SHA: `80c7b620cf446ed28b76143a0325ce89b1939ac0`.

Cross-review:

- `docs/reviews/AC-404-CASH-COMMITMENT-MANAGEMENT-REPORTING-CROSS-REVIEW.md`;
- `8 iterations`;
- `Complete / PASS for Owner approval`;
- immutable blob SHA: `3519f63ef7c09f075aa75b6d0d83ccd770911141`.

Owner decision:

- `docs/governance/decisions/DECISION-2026-08-21-AC-404-APPROVAL.md` — `Approved`;
- immutable blob SHA: `8e6ea741f14bb6471d250c6d39a76f15bdfb8ff3`;
- explicit wording: `AC-404 утверждаю`.

AC-404 является binding Company management-finance/control baseline в своём declared scope.

## 8. AC-404 canonicality and authority boundary

Главное разделение AC-404:

```text
bank/accounting fact
≠ management interpretation
≠ forecast
≠ budget/limit
≠ planned spend
≠ approved internal commitment
≠ incurred obligation
≠ actual payment
```

AC-404 не создаёт `FIN-*`, `PAY-*`, `TX-*` или другой parallel transaction ledger.

Bank/payment, accounting/tax/statutory, legal/corporate, customer/vendor, product/project economics и Arvectum OS facts остаются authoritative в своих contours. Company MAY быть canonical только для bounded management interpretation/control state.

Management report является derived decision-support projection. Он не является spend authorization, payment proof, budget approval или profitability proof.

`POS-005` accountability, наличие cash, banking access, report/dashboard visibility или prepared payment не создают spend/payment Organizational Authority.

## 9. Действующий портфель и статус этапов

Канонический Company-level portfolio source:

- `docs/portfolio/PORTFOLIO.md` — `Active 0.8.0`;
- текущий blob SHA: `8a77be35225f9c4958531e52a4131abda13d0f`;
- governance baseline: `AC-307 — Approved 1.0.0 / M3 Complete / PASS`.

Статус этапов:

- `M0` — `Complete / PASS`;
- `M1` — `Complete / PASS`;
- `M2` — `Complete / PASS`;
- `M3` — `Complete / PASS`;
- `M4` — `Current`, AC-405 `Current`;
- `M5` — `Planned`;
- `M6` — `Planned`;
- `M7` — `Future`;
- `M8` — `Future`;
- `M9` — финальный плановый этап, AC-901 `Planned` после M8.

## 10. M4 navigation

M4 проходит так:

1. `AC-401` — work/obligation register model — `Complete / PASS`;
2. `AC-402` — decision/approval/escalation register model — `Complete / PASS`;
3. `AC-403` — risk/exception/incident register model — `Complete / PASS`;
4. `AC-404` — cash/commitment/management reporting baseline — `Complete / PASS`;
5. `AC-405` — portfolio/module/priority review cadence — `Current`;
6. `AC-406` — Owner Mission Control / reference-implementation evidence view;
7. `AC-407` — management operating cadence and control review.

Approved control models сами по себе не доказывают полноту live register population, current cash/liquidity, absence of risks/incidents, profitability или business readiness. Такие факты требуют current authoritative evidence.

## 11. Arvectum OS boundary

Company-specific control и management-finance semantics принадлежат `arvectum/arvectum-company`.

При AC-404 current OS state был проверен на `76504766353028540891ac1dfdbf1e5dc331a4af`. OS roadmap `2.81.0` фиксирует `M9-alpha — Usable Internal Workspace` как `Achieved / PASS` в exact private internal scope и P9.07 как current. `docs/governance/DECISION-AUTHORITY-POLICY.md` Arvectum OS остаётся `Proposed 0.2.1` и не принят Company governance.

Arvectum OS MAY позднее предоставлять domain-neutral persistence/projection/composition/governed-execution mechanisms через отдельный admitted boundary. UI, technical roles, runtime availability и M9-alpha evidence не создают Company financial authority, Product Contract или capability lifecycle state.

## 12. Язык, терминология и публичная граница

Для новых человекочитаемых Company-документов действует русскоязычный режим и `docs/governance/TERMINOLOGY-GLOSSARY.md`.

Публичный Company repository не является местом хранения secrets, reusable credentials, private keys, signatures, избыточных персональных данных, банковских/платёжных payloads, transaction exports, confidential exact cash balances, непубличных договорных/customer/vendor материалов, sensitive tax/accounting documents, privileged payment/fraud или incident/security details и chain-of-thought.

## 13. Конечный этап M9

`M9 — Человекочитаемая документация полностью русифицирована и согласована` остаётся самым последним плановым этапом после M8, если собственник отдельно не изменит последовательность.

`AC-901 — Полная русификация человекочитаемой документации и итоговая междокументная сверка` остаётся `Planned`.