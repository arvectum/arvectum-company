# AC-307 — Перекрёстная проверка итогового управления портфелем и закрытия M3

Статус: `Complete / PASS for Owner approval`
Дата проверки: `2026-08-21`
Итераций выполнено: `10 of maximum 10`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-307 — Final portfolio governance review and M3 closure`

Проверенный proposal:

- `docs/portfolio/AC-307-PORTFOLIO-GOVERNANCE-REVIEW-AND-M3-CLOSURE.md`;
- статус: `Proposed 0.9.0`;
- immutable git blob SHA: `904b9e5ffa12caeb082b3bf23a89aff251ebe8c4`.

Статус утверждения: `Pending explicit Owner approval of the exact reviewed proposal`.

## 1. Review gate

AC-307 должен быть отклонён, если итоговая M3 closure:

- скрывает конфликт AC-301…AC-306 вместо его разрешения;
- считает repository locator юридическим/IP ownership;
- превращает `POS-003` accountability в полную product authority;
- превращает `continue` или AC-306 Band A в бюджет/безусловный growth mandate;
- превращает reference implementation в approved reusable module;
- превращает PORT-007 module hypothesis в material build authorization;
- создаёт hard runtime/data dependency из reuse evidence;
- подменяет Arvectum OS Product Contracts Company-side интерпретацией;
- игнорирует более свежий OS contract state;
- считает technical maturity доказательством profitability/customer readiness;
- закрывает M3 при stale active navigation/source registry, вводящем собственника в заблуждение;
- считает unresolved empirical evidence обязательным блокером governance milestone либо, наоборот, скрывает его как уже доказанный результат;
- переводит roadmap на AC-401 без требуемого Owner approval M3 closure;
- выполняет M4 work раньше утверждения AC-307.

## 2. Итерация 1 — Полнота цепочки AC-301…AC-306

**Критика:** финальный review может проверить только последние PORTFOLIO/ROADMAP и пропустить несовместимость ранних approvals.

**Сверка:** proposal использует отдельный immutable evidence set для всех шести Approved publications и их reviewed proposal blobs. Проверена причинная цепочка:

```text
identity/disposition
→ accountable Position
→ investment/cost/risk treatment
→ role/reuse classification
→ dependency/Product Contract map
→ capital/economics/Owner-attention priority
```

Каждый более поздний gate явно сохраняет scope более раннего либо добавляет новый слой без silent supersession.

**Результат:** PASS.

## 3. Итерация 2 — Product identity / repository / legal-IP нельзя смешать

**Критика:** M3 closure может создать ложный вывод, что Company identity + canonical repository доказывают юридическое владение всем кодом/данными.

**Сверка:** AC-301 и proposal сохраняют три разные вещи:

- `PORT-*` — Company-level product/node identity;
- repository path — implementation locator/source;
- legal/IP/data rights — отдельный внешний evidence/authority subject.

P6.02 locator reconciliation также не переписывает историю: `arutyunoveth/ai-corporation` остаётся historical predecessor locator, `arvectum/tender-agent` — current implementation locator.

Proposal отдельно перечисляет product-level legal/IP/data completeness как carry-forward и не делает её M3 claim.

**Результат:** PASS.

## 4. Итерация 3 — Accountable Position не должен поглотить functional authority

**Критика:** раз все PORT-* закреплены за `POS-003`, closure может превратить Portfolio & Product Lead в универсального владельца commercial/engineering/finance/security решений.

**Сверка:** proposal сохраняет AC-302/M2 split:

- POS-003 — Company-level portfolio stewardship/evidence synthesis;
- POS-002 — customer/commercial;
- POS-004 — engineering/release;
- POS-005 — finance/economics/obligations;
- POS-006 — security/data/risk/continuity;
- POS-001 — Company operating integration/escalation.

`ROD-01…ROD-09` и AC-203 authority modes не меняются. Repository access/technical ability также не является Organizational Authority.

**Результат:** PASS.

## 5. Итерация 4 — Investment treatment и role classification должны быть совместимы

**Критика:** reference/module status способен незаметно отменить `contain/clarify` и вернуть узел в growth queue.

**Сверка:** end-to-end matrix показывает:

- PORT-005/006: `contain` + `RI-PRODUCT-FAMILY`; reference value не создаёт growth mandate;
- PORT-007: `clarify before investment` + clarification-only module candidate; material build не разрешён;
- PORT-001/002/003/004: `continue` означает bounded continuation, а не unlimited productization.

Таким образом AC-303 и AC-304 не противоречат друг другу.

**Результат:** PASS.

## 6. Итерация 5 — OS Product Contract freshness и P6.02 исторический header

**Критика:** между AC-305 и AC-307 Arvectum OS мог измениться. Кроме того, P6.02 по-прежнему буквально содержит старый repository header, что можно принять за незакрытый conflict.

**Сверка current Arvectum OS main:** roadmap уже `2.77.0`, однако применимые contracts имеют те же lifecycle/version/content blobs:

- P6.02 `Provisional 0.1.0` — `bdf098776399a003f2df542f3ab3cd48ef83b003`;
- P6.06 `Provisional 0.1.0` — `23bbe792b81ddc5da736333d8a92580a718f920e`;
- P8.03 `Provisional 0.1.0` — `63d0954b27bca86b5e85945f28438cb7405f62b6`;
- P8.06 `Provisional 0.1.0` — `0f8b8404b8b201d3aa29e88f146a7bf658c01d9b`.

P6.02 historical artifact намеренно не переписан. Current locator resolution существует в отдельной Approved OS reconciliation publication, поэтому буквальный historical header не является unresolved conflict.

AC-305 dependency semantics остаются актуальными: Tender Agent CAP-001+CAP-004 в bounded contours; Discount Parser CAP-004 only; CTA optional CAP-004 extension.

**Результат:** PASS.

## 7. Итерация 6 — AC-306 ranking не должен стать скрытым funding/strategy change

**Критика:** closure может сделать `A1/A2` чем-то похожим на утверждённый бюджет или новый Company flagship.

**Сверка:** proposal сохраняет два независимых уровня:

1. AC-106 Company priority: `P0 → P1 → P2 → P3`;
2. AC-306 default discretionary portfolio decision order внутри применимого product-work layer.

Band A не создаёт spend authorization, price, customer commitment, SLA, legal/IP exception или lifecycle promotion. ROD-02/03/04/06/08/09 остаются отдельными gates.

Flagship `«ИИ-компания под ключ»` не изменён.

**Результат:** PASS.

## 8. Итерация 7 — Contain / clarification-only / named-trigger nodes

**Критика:** даже без формального изменения статуса backlog может постепенно потреблять Owner attention.

**Сверка:** proposal фиксирует operational discipline:

- PORT-005/006 — reactive support/evidence only;
- PORT-007 — clarification-only, no material build;
- PORT-003/004 — named-trigger investment, не continuous speculative activity;
- P0 obligation может временно повысить конкретный work slice, но не меняет portfolio band/disposition автоматически.

Это совместимо с AC-104 Owner-bottleneck evidence и AC-306 rule `why now → bounded outcome → exact Owner action → stop condition`.

**Результат:** PASS.

## 9. Итерация 8 — Active navigation/source registry drift

**Критика:** README и CANONICAL-SOURCES до AC-307 оставались на AC-301/roadmap 0.22.0. Закрывать M3 при таком current navigation state нельзя: собственник получал бы конфликтующий статус.

**Сверка:** drift исправлен до final review:

- README → current M3/AC-307, commit `adfb0498cda518ed69a64f31c9a08d63895810e4`, resulting blob `b03dd62dd26a287a25d37ca9ee334d6988c9fd60`;
- CANONICAL-SOURCES → `Active 2.7.0`, current roadmap `0.28.0`, portfolio `0.7.0`, AC-307 current, commit `ba5ec19d749123d61261d3b60389cf0764843424`, resulting blob `80a6e1c03cf4b7d15dcc93dc5dd92b7c9b7b189e`.

Исторические Approved documents не редактировались. Полная documentation reconciliation остаётся AC-901, поэтому AC-307 не разрастается до финального M9 scope.

**Результат:** PASS.

## 10. Итерация 9 — Открытые вопросы: carry-forward или blocker?

**Критика:** M3 closure может быть либо слишком строгим («нет точного ROI — нельзя закрыть governance milestone»), либо слишком оптимистичным («M3 закрыт — значит продукты экономически доказаны»).

**Сверка:** proposal чётко разделяет **governance completeness** и **empirical business evidence**.

Carry-forward остаются:

- Tender Agent paid/pilot/deal economics;
- Discount Parser live acceptance/support boundary;
- Proxy Launcher human/legal rights basis, separate-host gates и per-app stop-gate;
- CTA real design-partner/customer evidence;
- PORT-007 consumers/common contract/economic case;
- portfolio-wide profitability/ROI/CAC-LTV/unit economics/market validation/legal-IP-data completeness/customer readiness.

Эти вопросы не нужны, чтобы доказать, что Company знает **как ими управлять**. Но они обязательны перед конкретными material decisions, которые от них зависят.

Proposal не заявляет profitability, demand, production readiness, Stable OS contracts или Active capabilities.

**Результат:** PASS.

## 11. Итерация 10 — Closure authority и handoff в M4

**Критика:** AC-307 может сам себя объявить завершённым и автоматически перевести roadmap на AC-401 без Owner decision.

**Сверка:** proposal явно остаётся `Proposed 0.9.0` и требует Owner approval exact reviewed blob. До этого:

- M3 остаётся `Current`;
- roadmap остаётся `0.28.0` с AC-307 current;
- AC-401 не выполняется.

Canonical roadmap publication chain (полный roadmap `0.14.0`, сохранённый последующими overlays) устанавливает после M3:

`M4 — Owner control and reference-implementation observability established`

и первым действием:

`AC-401 — Company work/obligation register model`.

После Owner approval AC-307 допустимы только publication/decision/PORTFOLIO/ROADMAP sync и переход current action на AC-401. Это не является выполнением AC-401.

**Результат:** PASS.

## 12. Acceptance matrix

| Проверка | Результат |
|---|---|
| AC-301…AC-306 exact approved evidence set complete | PASS |
| stable `PORT-*` identities and locators | PASS |
| repository locator ≠ Product Identity ≠ legal/IP ownership | PASS |
| each node has explicit disposition | PASS |
| each node has accountable Position | PASS |
| POS-003 does not absorb functional/Owner authority | PASS |
| AC-303 investment treatment compatible with AC-304 roles | PASS |
| PORT-005 contain preserved | PASS |
| PORT-006 contain preserved | PASS |
| PORT-007 clarification-only / no material build preserved | PASS |
| Band B named-trigger discipline preserved | PASS |
| no mandatory hard inter-product runtime/code/data dependency | PASS |
| reference/reuse evidence not turned into shared implementation | PASS |
| current OS Product Contract state re-checked | PASS |
| P6.02 locator reconciliation remains valid | PASS |
| P6.02/P6.06/P8.03/P8.06 remain Provisional | PASS |
| no Stable/Active OS claim | PASS |
| AC-306 ranking does not create budget/spend authorization | PASS |
| AC-106 P0…P3 hierarchy remains above ranking | PASS |
| flagship remains unchanged | PASS |
| Owner attention treated as scarce capital | PASS |
| no hidden Product/Company/OS authority transfer | PASS |
| no legal/IP/data rights inferred | PASS |
| README current-state drift repaired | PASS |
| CANONICAL-SOURCES current-state drift repaired | PASS |
| historical reviewed/approved blobs preserved | PASS |
| unresolved empirical questions explicitly carried forward | PASS |
| profitability/demand/customer-readiness not claimed | PASS |
| M3 closure requires explicit Owner approval | PASS |
| AC-401 identified from canonical roadmap chain | PASS |
| AC-401 not executed prematurely | PASS |

## 13. Review conclusion

Использованы все `10 of maximum 10` итераций, потому что AC-307 закрывает не отдельную классификацию, а весь milestone M3 и должен проверить одновременно portfolio identity, organizational accountability, investment discipline, reuse classification, cross-repository/OS boundaries, priority order, Owner attention и canonical navigation state.

Material contradictions, блокирующих M3 governance closure, не обнаружено.

Единственный найденный repository-level coherence defect — stale README/CANONICAL-SOURCES navigation — был устранён **до** итогового PASS без изменения утверждённой portfolio semantics и без переписывания исторических approvals.

Итог cross-review:

`AC-307 — Complete / PASS for Owner approval`.

Рекомендуемый milestone result после явного утверждения собственником:

`M3 — Product/module-candidate portfolio governed as investments: Complete / PASS`.

Следующее каноническое действие после утверждения и синхронизации:

`AC-401 — Company work/obligation register model`.

Для Owner gate достаточно формулировки:

`AC-307 утверждаю.`
