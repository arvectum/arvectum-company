# Реестр канонических источников Arvectum Company

Статус: `Active`
Версия: `3.1.0`
Обновлено: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`

## 1. Модель публикации

Эта редакция сохраняет полный реестр `3.0.0` по immutable git blob и добавляет утверждение AC-403 и переход к AC-404.

Предыдущая редакция:

- версия: `3.0.0`;
- путь: `docs/CANONICAL-SOURCES.md`;
- immutable git blob SHA: `7caae6ff6a607fb57b180243a3867080d94eb629`.

Все ранее зарегистрированные источники M0–M3, AC-201–AC-402, языково-терминологическая политика, Company/Product/Arvectum OS boundaries и правила внешних источников сохраняются без изменений, если прямо не уточнены более новым утверждённым артефактом.

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

- `docs/roadmap/ROADMAP.md` — `Active 0.32.0`;
- текущий blob SHA: `9b373bba42b1270a521cbcf6855aa84f23fb358c`.

Текущее каноническое действие:

`AC-404 — Cash, commitment and management reporting baseline`.

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

Каноническая approved publication:

- `docs/operations/COMPANY-RISK-EXCEPTION-INCIDENT-REGISTER-MODEL-v1.0.0.md` — `Approved 1.0.0`;
- immutable publication blob SHA: `effef94f950d6d070c421a22c2eced00b5e561ad`.

Exact reviewed proposal:

- `docs/operations/COMPANY-RISK-EXCEPTION-INCIDENT-REGISTER-MODEL.md` — `Proposed 0.9.0`;
- immutable proposal blob SHA: `857b601423f78fc3d4636dbf9754d5410d8a1c55`.

Cross-review:

- `docs/reviews/AC-403-COMPANY-RISK-EXCEPTION-INCIDENT-REGISTER-CROSS-REVIEW.md`;
- `10 of maximum 10`;
- `Complete / PASS for Owner approval`;
- immutable blob SHA: `37241051876a94f71035e532e19ed9cf69b4c785`.

Owner decision:

- `docs/governance/decisions/DECISION-2026-08-21-AC-403-APPROVAL.md` — `Approved`;
- immutable blob SHA: `524cad548204d8721117989f3940f3295ab7d932`;
- explicit wording: `AC-403 утверждаю`.

AC-403 является binding Company risk-control model в своём declared scope.

## 7. AC-403 canonicality and authority boundary

AC-403 устанавливает:

- `RSK-*` — material risk exposure/control record;
- `EXC-*` — material control-exception request/decision control record;
- `INC-*` — material incident control record.

Исторические `R-01…R-20` AC-105 остаются baseline references и не заменяются live `RSK-*` по импликации.

Главные границы:

- `risk evidence ≠ accepted risk`;
- `exception request ≠ approved exception`;
- `incident detection ≠ authority to act`;
- `containment ≠ risk acceptance`;
- `recovery ≠ automatic obligation/risk closure`.

Risk acceptance и exception approval требуют applicable attributable authority acts. Company control record не заменяет product/security/legal/customer/OS authoritative source.

## 8. Действующий портфель и статус этапов

Канонический Company-level portfolio source:

- `docs/portfolio/PORTFOLIO.md` — `Active 0.8.0`;
- текущий blob SHA: `8a77be35225f9c4958531e52a4131abda13d0f`;
- governance baseline: `AC-307 — Approved 1.0.0 / M3 Complete / PASS`.

Статус этапов:

- `M0` — `Complete / PASS`;
- `M1` — `Complete / PASS`;
- `M2` — `Complete / PASS`;
- `M3` — `Complete / PASS`;
- `M4` — `Current`, AC-404 `Current`;
- `M5` — `Planned`;
- `M6` — `Planned`;
- `M7` — `Future`;
- `M8` — `Future`;
- `M9` — финальный плановый этап, AC-901 `Planned` после M8.

## 9. M4 navigation

M4 проходит так:

1. `AC-401` — work/obligation register model — `Complete / PASS`;
2. `AC-402` — decision/approval/escalation register model — `Complete / PASS`;
3. `AC-403` — risk/exception/incident register model — `Complete / PASS`;
4. `AC-404` — cash/commitment/management reporting baseline — `Current`;
5. `AC-405` — portfolio/module/priority review cadence;
6. `AC-406` — Owner Mission Control / reference-implementation evidence view;
7. `AC-407` — management operating cadence and control review.

Approved control models сами по себе не доказывают полноту live register population, current cash, absence of risks/incidents или business readiness. Такие факты требуют current authoritative evidence.

## 10. Arvectum OS boundary

Company-specific control semantics принадлежат `arvectum/arvectum-company`.

При AC-403 current OS state был проверен на `c2be41ad8d1b144bea2ab0b030c57bcf3c59a3ae`. P9.06 governed-actions UX сохраняет independent governance gates и fail-closed behavior. `docs/governance/DECISION-AUTHORITY-POLICY.md` Arvectum OS остаётся `Proposed 0.2.1` и не принят Company governance.

Arvectum OS MAY позднее предоставлять domain-neutral persistence/projection/governed-execution mechanisms через отдельный admitted boundary. UI, technical roles и runtime availability не создают Company Organizational Authority.

## 11. Язык, терминология и публичная граница

Для новых человекочитаемых Company-документов действует русскоязычный режим и `docs/governance/TERMINOLOGY-GLOSSARY.md`.

Публичный Company repository не является местом хранения secrets, reusable credentials, private keys, signatures, избыточных персональных данных, банковских/платёжных payloads, непубличных договорных/customer материалов, privileged incident/security details или chain-of-thought.

## 12. Конечный этап M9

`M9 — Человекочитаемая документация полностью русифицирована и согласована` остаётся самым последним плановым этапом после M8, если собственник отдельно не изменит последовательность.

`AC-901 — Полная русификация человекочитаемой документации и итоговая междокументная сверка` остаётся `Planned`.