# AC-307 — Итоговая проверка управления портфелем и закрытие M3

Статус: `Proposed`
Версия: `0.9.0`
Создано: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-307 — Final portfolio governance review and M3 closure`
Предшествующий governance baseline: `AC-306 — Approved 1.0.0`
Статус утверждения: `Pending explicit Owner approval of the exact reviewed proposal`

## 1. Назначение

AC-307 проверяет AC-301…AC-306 как **единую систему Company-level portfolio governance** и отвечает на один итоговый вопрос:

> Сформирован ли для текущего портфеля ООО «Арвектум» достаточно цельный и управляемый baseline, чтобы считать M3 завершённым, не скрывая неопределённость, не превращая ranking в бюджет и не смешивая Company, продуктовые репозитории и Arvectum OS?

AC-307 не создаёт новый инвестиционный тезис и не повторно ранжирует продукты. Он проверяет уже утверждённые решения на совместимость, выявляет оставшиеся противоречия/пробелы, определяет carry-forward и, при PASS, рекомендует закрытие milestone:

`M3 — Product/module-candidate portfolio governed as investments`.

Закрытие M3 требует явного решения собственника, потому что это итоговый Company portfolio-governance milestone и переход к следующему этапу, а не чисто техническая отметка.

## 2. Проверяемый immutable evidence set

| Gate | Approved publication | Current publication blob | Reviewed proposal blob | Что закрепляет |
|---|---|---|---|---|
| `AC-301` | `AC-301-PORTFOLIO-IDENTITY-BOUNDARY-OWNERSHIP-RECONCILIATION-v1.0.0.md` | `96933e32263cbf1140ce257423eb5e9c16a49f07` | `146b5868a21c09cf20b633e309e587b7a631ad32` | устойчивые `PORT-*` identities, repository locators, dispositions и границы |
| `AC-302` | `AC-302-PORTFOLIO-ACCOUNTABLE-POSITION-MAPPING-v1.0.0.md` | `1f62dcfea885e564c8cd43926c72a04d00821328` | `29bec89402118ddfc061501b8b25f5c0000d65a4` | `PORT-* → POS-003` primary Company-level accountability |
| `AC-303` | `AC-303-PORTFOLIO-INVESTMENT-COST-RISK-BOUNDARIES-v1.0.0.md` | `3f7af8bd9e5b9c5f64045a54a723f8db4eab63d0` | `e246d06e87b4221ad85718d2aeeb4e3486bf388e` | bounded investment/cost/risk treatment и review triggers |
| `AC-304` | `AC-304-PORTFOLIO-ROLE-CLASSIFICATION-v1.0.0.md` | `0fef86ef01f3ce0c7c405b2f1c0e4dc79aaf8045` | `533ccef1d28bf9a154da9b99dd1c4226c19d166b` | standalone/reference/module/OS-candidate role separation |
| `AC-305` | `AC-305-CROSS-PRODUCT-DEPENDENCY-AND-OS-CONTRACT-RECONCILIATION-v1.0.0.md` | `42db07d2427b44647a8db3355cb66ed4c9a72a05` | `c27973c48b7bb5306e36f71d0f1007fc41896de9` | dependency map, OS Product Contract mapping и P6.02 locator reconciliation |
| `AC-306` | `AC-306-PORTFOLIO-PRIORITIZATION-CAPITAL-ECONOMICS-OWNER-ATTENTION-v1.0.0.md` | `d14718ee5eec55440dd8a3e0a34144ae0e8f4f06` | `d254c6441baca5f22828648ecfa701d04c8344b1` | default portfolio decision order и Owner-attention discipline |

Current aggregate sources перед AC-307:

- `docs/portfolio/PORTFOLIO.md` — `Active 0.7.0`, blob `e2e43ced1647d5fcbe6cd484b528770775097753`;
- `docs/roadmap/ROADMAP.md` — `Active 0.28.0`, blob `009f3aa9341c01039cf7b1d217fb246cf51855fe`;
- `docs/CANONICAL-SOURCES.md` — `Active 2.7.0`, blob `80a6e1c03cf4b7d15dcc93dc5dd92b7c9b7b189e`;
- `README.md` — synchronized navigation blob `b03dd62dd26a287a25d37ca9ee334d6988c9fd60`.

## 3. Canonicality and navigation reconciliation performed before review

AC-307 обнаружил один реальный repository-level drift, не меняющий утверждённую portfolio semantics:

- `README.md` всё ещё представлял AC-301 как текущее действие и не отражал фактически завершённые AC-301…AC-306;
- `docs/CANONICAL-SOURCES.md` всё ещё ссылался на roadmap `0.22.0` и AC-301 как current, хотя canonical roadmap уже был `0.28.0` с AC-307 current.

Это был **navigation/source-register drift**, а не конфликт утверждённых portfolio decisions.

Перед итоговой проверкой он устранён без переписывания исторических Approved artifacts:

- `README.md` синхронизирован с current M3/AC-307 state, commit `adfb0498cda518ed69a64f31c9a08d63895810e4`;
- `docs/CANONICAL-SOURCES.md` обновлён до `2.7.0`, commit `ba5ec19d749123d61261d3b60389cf0764843424`.

Исторические immutable blobs сохранены. AC-901 остаётся финальной полной междокументной русификацией/сверкой; AC-307 не пытается преждевременно выполнить весь AC-901 scope.

## 4. End-to-end portfolio governance matrix

| Node | Identity / disposition | Accountable Position | Investment treatment | Role | Dependency/OS boundary | Priority |
|---|---|---|---|---|---|---|
| `PORT-001` Tender Agent | stable; `continue` | `POS-003` | bounded product-development/pilot | standalone + `RI-OS-CONSUMER` | no hard peer dependency; P6.02 + P8.03, CAP-001+CAP-004 in bounded scopes | `A2` |
| `PORT-002` Discount Parser | stable; `continue` | `POS-003` | accepted client/product contour; material expansion gated | standalone + `RI-OS-CONSUMER + RI-PRODUCT-FAMILY` | no hard peer dependency; P6.06, CAP-004 only | `A1` |
| `PORT-003` Proxy Launcher | stable; `continue` | `POS-003` | bounded productization | standalone | no Product Contract / no hard peer dependency | `B1`, named trigger |
| `PORT-004` Creative Test Agent | stable; `continue` | `POS-003` | bounded controlled-pilot/productization | standalone + `RI-OS-CONSUMER` | no hard peer dependency; P8.06 optional CAP-004 extension | `B2`, named trigger |
| `PORT-005` Tender Small-Volume Calculator | stable; `contain` | `POS-003` | maintenance/evidence/reuse assessment only | `RI-PRODUCT-FAMILY` | reference reuse into PORT-001 only; no runtime coupling | `D1` |
| `PORT-006` Doors Parser | stable; `contain` | `POS-003` | completed-delivery support/reuse evidence only | `RI-PRODUCT-FAMILY` | parser-family evidence only; no shared runtime | `D2` |
| `PORT-007` Data Platform | stable; `clarify` | `POS-003` | clarify before investment | clarification-only Company/product-family module candidate | no hard dependency; no Product Contract | `C1`, no material build |

В этой матрице не обнаружено material semantic contradiction между AC-301…AC-306.

## 5. Проверка M3 exit criteria

### 5.1 Stable identity, locator, disposition

`PASS`.

Каждый `PORT-001…PORT-007` имеет устойчивую Company identity, current repository locator и явный disposition. Repository locator не подменяет Product Identity.

P6.02 historical locator conflict закрыт надлежащим Arvectum OS overlay: historical `arutyunoveth/ai-corporation`, current `arvectum/tender-agent`.

### 5.2 Accountable organizational Position

`PASS`.

Все узлы имеют primary Company-level accountable Position `POS-003 — Portfolio & Product Lead`.

Это не отменяет функциональные роли POS-001/POS-002/POS-004/POS-005/POS-006 и не превращает POS-003 в единоличного end-to-end исполнителя или источник Reserved Owner authority.

### 5.3 Investment treatment ↔ role classification

`PASS`.

Нет узла, где AC-303 `contain/clarify/continue` противоречит AC-304 role classification:

- active standalone products имеют bounded `continue`, а не unlimited growth;
- contained PORT-005/006 могут сохраняться как reference evidence без growth mandate;
- PORT-007 имеет module-candidate hypothesis, но именно `clarify before investment`, поэтому candidate status не превращён в build authorization.

### 5.4 Dependency/Product Contract map ↔ current portfolio state

`PASS`.

Повторная сверка current Arvectum OS показала:

- OS roadmap уже `Active 2.77.0`, но этот Phase 9 progress сам по себе не меняет M3 Product Contract map;
- P6.02 остаётся `Provisional 0.1.0`, current blob `bdf098776399a003f2df542f3ab3cd48ef83b003`;
- P6.06 остаётся `Provisional 0.1.0`, current blob `23bbe792b81ddc5da736333d8a92580a718f920e`;
- P8.03 остаётся `Provisional 0.1.0`, current blob `63d0954b27bca86b5e85945f28438cb7405f62b6`;
- P8.06 остаётся `Provisional 0.1.0`, current blob `0f8b8404b8b201d3aa29e88f146a7bf658c01d9b`;
- approved P6.02 repository-locator reconciliation remains the current provenance resolver and does not change P6.02 semantic version.

No new OS Product Contract evidence was found that invalidates AC-305.

### 5.5 Priority ranking ↔ capital/authority boundary

`PASS`.

AC-306 ranking is compatible with AC-303 because it ranks **decision attention**, not budget amounts. `A1/A2/B1/B2/C1/D1/D2` do not authorize spending, customer commitments, legal acts, data reuse, Product Contract changes or automatic lifecycle promotion.

AC-106 remains hierarchically above portfolio ranking:

`P0 obligations/cash/material risk → P1 flagship evidence + real operating model → P2 evidence/revenue-linked product work → P3 speculative expansion`.

### 5.6 Contained / clarification-only integrity

`PASS`.

- PORT-005 remains contained; its working code/reference value does not create a second active procurement growth line.
- PORT-006 remains a completed-delivery/support/reference asset; parser evidence does not create a generic-parser mandate.
- PORT-007 remains clarification-only; no production shared datastore, crawler platform, vector/search layer or compulsory cross-product runtime has been authorized.

### 5.7 Named-trigger discipline for Band B

`PASS`.

- PORT-003 receives discretionary attention on a credible commercial/obligation/IP-release trigger, not because blocked physical-host or speculative routing tasks exist.
- PORT-004 is activated on qualified design-partner/customer evidence rather than indefinite internal feature expansion.

### 5.8 Owner attention as scarce capital

`PASS`.

AC-306 explicitly requires `why now`, bounded outcome, exact Owner action, delegable preparation/execution, stop condition and next decision enabled by evidence.

This is compatible with AC-104/M2: Owner control is preserved while unnecessary Owner execution/context switching is reduced.

### 5.9 No hidden shared runtime/data/authority commitment

`PASS`.

M3 creates no:

- shared mutable cross-product state;
- mandatory shared service/library/runtime;
- data migration or customer-data pooling;
- ambient AI authority;
- product merge;
- Company-side rewriting of OS Product Contracts;
- implicit legal/IP ownership claim.

Reference/reuse relationships remain evidence until separately promoted through the applicable product/Company/OS decision path.

### 5.10 Source-of-truth separation

`PASS`.

- Company repository — `PORT-*` identity, portfolio relationship, accountability, investment treatment and Company priority;
- product repositories — product-specific implementation/status/domain semantics;
- Arvectum OS — Product Contracts, Platform Capability lifecycle and domain-neutral platform semantics;
- legal/corporate/accounting/customer authoritative systems — their respective legal, financial, contractual and confidential facts.

No M3 document is allowed to override a stronger source outside its scope.

## 6. Explicit carry-forward after M3

M3 closure must **not** erase unresolved evidence. The following items remain live after closure:

### PORT-001 — Tender Agent

- real paid/pilot/deal economics and repeatability remain unproven;
- next discretionary work remains bounded to concrete revenue/pilot/evidence needs;
- P6.02/P8.03 remain Provisional OS contours, not Stable/customer-production claims.

### PORT-002 — Discount Parser

- real client acceptance/live environment feedback remains the decisive near-term evidence;
- after accepted delivery the default is maintenance/freeze unless new paid or second-consumer evidence appears;
- generic parser/data platformization remains separately gated.

### PORT-003 — Proxy Launcher

- human/legal author→ООО rights-basis execution evidence remains a named gate for the clean-IP/refactor path;
- APL-WIN-014/APL-REL-014 remain blocked on a separate eligible physical host;
- per-application Windows enforcement remains behind its own product/dependency/signing stop-gate;
- none of these make PORT-003 a Company-wide infrastructure dependency.

### PORT-004 — Creative Test Agent

- real design-partner/customer inputs, success criteria and commercial conversion evidence remain absent/insufficient at Company level;
- pilot readiness is not market validation;
- optional P8.06 OS extension remains optional.

### PORT-005 / PORT-006

- remain contained/reference assets;
- customer/support obligation may temporarily create P0 work but does not silently re-band the node.

### PORT-007

- named consumers, common contract and economic/continuity case remain required before material build;
- repository existence and the word `Platform` remain insufficient evidence.

### Portfolio-wide

Still unproven and not claimed by M3:

- product profitability, ROI, CAC/LTV or repeatable acquisition;
- complete product-level unit economics;
- market validation of the flagship offer;
- legal/IP/data-right completeness for every product;
- customer/production readiness;
- Stable Product Contracts or Active Platform Capabilities in Arvectum OS;
- tested Company-wide disaster recovery;
- external design-partner deployment.

These are downstream evidence/decision subjects, not M3 defects unless a specific material action requires them now.

## 7. M3 closure result proposed by AC-307

AC-301…AC-306 now form a coherent Company-level portfolio governance baseline.

The final review finds:

- no unresolved material contradiction among the six approved Phase 3 gates;
- no portfolio node without stable identity/disposition/accountable Position;
- no hidden funding or growth mandate for contained/clarification-only nodes;
- no undeclared mandatory cross-product runtime/data dependency;
- no Company-side takeover of Product or Arvectum OS canonical semantics;
- no requirement to resolve empirical market/profitability/customer-readiness questions before closing M3 as a **governance milestone**;
- one navigation/source-register drift, already repaired before final review without rewriting historical approvals.

Therefore the proposed result is:

`AC-307 — Complete / PASS, subject to explicit Owner approval`.

И, при утверждении собственником:

`M3 — PRODUCT/MODULE-CANDIDATE PORTFOLIO GOVERNED AS INVESTMENTS: COMPLETE / PASS`.

Русская смысловая формулировка:

**портфель Arvectum Company имеет устойчивую идентичность, организационную ответственность, ограниченные инвестиционные режимы, явные роли/reuse boundaries, сверенные зависимости/OS contracts и относительный порядок конкуренции за капитал и внимание собственника.**

## 8. Следующий канонический этап после утверждения

Canonical roadmap `0.14.0`, включённый immutable publication chain в текущий roadmap, устанавливает после M3:

`M4 — Owner control and reference-implementation observability established`.

Первое действие M4:

`AC-401 — Company work/obligation register model`.

Цель следующего этапа — дать собственнику видимость material work, obligations, decisions, risks, cash/commitments и portfolio state без постоянного восстановления контекста из чатов и репозиториев.

AC-307 не выполняет AC-401 заранее.

## 9. Authority / non-effect boundary

Даже после утверждения AC-307 и закрытия M3 результат не:

- создаёт бюджет или разрешение на конкретный расход;
- утверждает цену, договор, SLA, customer promise или production deployment;
- меняет legal/corporate authority;
- создаёт или расширяет customer data rights;
- подтверждает исключительные права на все продуктовые активы;
- меняет Product Contract или Platform Capability Arvectum OS;
- создаёт shared module/service/runtime;
- запускает PORT-007 build;
- автоматически повышает Band B node;
- отменяет `ROD-01…ROD-09`;
- доказывает profitability, demand, customer readiness или scalability.

Любой такой эффект требует собственного applicable evidence и authority path.

## 10. Approval gate

Для утверждения требуется явное решение собственника по точной версии, прошедшей cross-review.

Рекомендуемая формулировка после PASS review:

`AC-307 утверждаю.`

До такого решения M3 остаётся `Current`, а AC-401 не становится canonical current action.
