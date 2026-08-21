# AC-303 — Перекрёстная проверка границ инвестиций, затрат и рисков портфеля

Статус: `Complete / PASS for Owner approval`
Дата проверки: `2026-08-21`
Итераций выполнено: `10 of maximum 10`
Результат: `PASS — для всех PORT-001…PORT-007 определены bounded Company-level investment treatments, cost/risk/Owner-attention evidence requirements и continue/change/contain/stop-retire review triggers без invented financial thresholds, без расширения authority и без преждевременного выполнения AC-304/305/306`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-303 — Investment, cost and risk boundaries; continue/change/stop criteria`
Проверенный документ: `docs/portfolio/AC-303-PORTFOLIO-INVESTMENT-COST-RISK-BOUNDARIES.md`
Проверенная редакция: `Proposed 0.9.0`
Проверенный git blob SHA: `e246d06e87b4221ad85718d2aeeb4e3486bf388e`
Максимум итераций: `10`
Статус утверждения: `Pending explicit Owner approval of the exact reviewed proposal`

## 1. Назначение проверки

AC-303 — первый Phase 3 шаг, который связывает portfolio governance с будущими capital/risk decisions. Поэтому проверка должна одновременно доказать business usefulness и отсутствие скрытого budget/authority expansion.

Proposal должен быть отклонён, если он:

- повторяет AC-301 identity reconciliation вместо canonical AC-303;
- придумывает финансовые суммы/пороги при отсутствии evidence;
- считает `continue` автоматическим funding authorization;
- считает `contain` автоматическим delete/abandon;
- считает `clarify` разрешением строить Data Platform;
- смешивает POS-003 stewardship с finance/risk/customer/engineering authority;
- ослабляет `ROD-*`;
- использует technical PASS, repository activity или sunk cost как самостоятельный investment argument;
- делает product status authoritative в Company artifact;
- предрешает AC-304 classification, AC-305 dependency/OS reconciliation или AC-306 priority ranking.

## 2. Итерация 1 — пользовательская формулировка не должна повторно открыть AC-301

**Критика:** пользователь назвал AC-303, но повторил словесное описание «сверка идентичности, границ и владения продуктов и инициатив портфеля», которое соответствует уже Approved AC-301. Буквальное следование тексту создало бы competing Phase 3 scope и переписало бы закрытый baseline.

**Сверка:** canonical ROADMAP `0.24.0` однозначно определяет AC-303 как `Investment, cost and risk boundaries; continue/change/stop criteria`. Proposal использует Approved AC-301 identities/dispositions как вход и не повторяет их reconciliation.

**Результат:** PASS.

## 3. Итерация 2 — нельзя подменить отсутствие финансовых данных произвольными лимитами

**Критика:** формулировка `investment/cost boundaries` провоцирует придумать рублёвые бюджеты, проценты или часы, хотя Company artifacts не содержат подтверждённого budget baseline для семи nodes.

**Сверка:** proposal вводит границы по типу воздействия и review trigger, а не fictitious numeric thresholds. Прямо установлено `Unknown = evidence required, not zero`. Actual amounts/hours/invoices должны фиксироваться только из надёжного evidence, когда появляются.

Это соответствует Company Constitution business-first/proportionality и AC-202 consequence-based materiality без invented numbers.

**Результат:** PASS.

## 4. Итерация 3 — `continue` нельзя читать как автоматическое финансирование или расширение scope

**Критика:** PORT-001/002/003/004 уже имеют AC-301 disposition `continue`. Если AC-303 просто повторит это слово, оно может стать неявным blanket approval на любые дальнейшие расходы и productization.

**Сверка:** proposal меняет семантику на `continue within envelope`: только текущий bounded scope и только при наличии applicable assignment/authority/access/evidence. Новый material cash/recurring spend, customer commitment, production expansion, data scope или critical dependency вызывает refresh/escalation.

Technical completion не создаёт business readiness; material expansion остаётся применимым `ROD-*` decision.

**Результат:** PASS.

## 5. Итерация 4 — POS-003 synthesis не должен поглотить functional accountability

**Критика:** AC-302 сделал POS-003 primary accountable Position для всех nodes. Теперь investment packet может случайно превратить POS-003 в finance/risk/commercial/engineering approver.

**Сверка:** proposal явно разделяет evidence routing:

- POS-002 — customer/demand/commitment/delivery;
- POS-004 — engineering/release/maintenance/feasibility;
- POS-005 — cash/recurring cost/economics/obligations;
- POS-006 — security/data/risk/dependency/sovereignty/continuity;
- POS-001 — integration/escalation;
- POS-003 — node-level synthesis/stewardship.

POS-003 сохраняет только approved AM-0/1/2 envelope; material financial/risk/portfolio authority не создаётся.

**Результат:** PASS.

## 6. Итерация 5 — contained nodes должны сохранять обязательства и evidence, но не получать growth mandate

**Критика:** PORT-005 и PORT-006 уже `contain`. Слишком жёсткий stop criterion может привести к silent abandonment существующих customer/support/history obligations; слишком мягкий — снова открыть growth investment.

**Сверка:** proposal определяет `contain` как freeze growth/scope expansion с сохранением:

- фактически существующих обязательств;
- bounded maintenance/safety/security work;
- required delivery/history/evidence;
- preparation of reuse/retire decision.

PORT-005 не объединяется автоматически с Tender Agent; PORT-006 не превращается в generic parser. Любой material restart/new customer/productization проходит новый Owner gate.

**Результат:** PASS.

## 7. Итерация 6 — Data Platform должна остаться hypothesis/discovery, а не стать speculative platform build

**Критика:** PORT-007 называется `Data Platform`, и само слово `platform` может создавать platform gravity: инфраструктура, shared schemas, data lake, warehouse/vector/search stack и cross-product contracts начнут строиться до наличия потребителя.

**Сверка:** proposal даёт PORT-007 самый узкий `clarify before investment` envelope: business problem, consumers, bounded use case, economic/operational hypothesis, data/rights/risk/sovereignty constraints и boundary evidence. Production data ingestion, recurring infra, shared data contracts и OS/platform admission запрещены по импликации.

Отдельно сохранён AC-305 как formal Company/Product/OS reconciliation gate.

**Результат:** PASS.

## 8. Итерация 7 — node-specific правила должны опираться на product sources, не превращая snapshot в новый source of truth

**Критика:** generic portfolio criteria без product evidence были бы слишком абстрактны; но копирование текущего product state в Company document создаёт stale competing truth.

**Сверка:** proposal использует bounded product snapshot через exact blob references:

- Tender Agent STATUS;
- Discount Parser README;
- Proxy Launcher README;
- Creative Test Agent README;
- Tender Small-Volume Calculator README;
- Doors Parser README;
- Data Platform README.

Company artifact фиксирует только decision-relevant interpretation и прямо требует refresh source evidence при material product change. Product repository остаётся canonical в product scope.

Node envelopes therefore учитывают реальные текущие ограничения: Tender Agent controlled quality stage, Discount Parser live acceptance boundary, Proxy Launcher Windows-only verified track/unsigned production state, Creative Test Agent local-first pilot scope, contained Tender Calculator/Doors Parser и минимально определённый Data Platform.

**Результат:** PASS.

## 9. Итерация 8 — cost model обязан видеть не только деньги, но downside, Owner attention и sovereignty

**Критика:** у small AI-native company direct cash spend может быть низким, а реальная цена продукта возникает через founder bottleneck, support, customer promises, privileged data, fragile dependencies или external-service lock-in. Если AC-303 смотрит только на invoices, он будет системно недооценивать риск.

**Сверка:** proposal включает десять exposure categories: direct cash, recurring, engineering/delivery, Owner attention, customer/obligations, security/data/privacy, legal/IP/compliance, dependency/sovereignty, continuity и opportunity cost.

Universal review triggers отдельно охватывают new vendor/contractor, production, customer/data scope, critical dependency, technology-sovereignty exception, repeated Owner intervention, incident и material mismatch ожидаемой/фактической нагрузки.

Это сохраняет ROD-02/03/06/07/08 и Company Constitution technology-sovereignty/business-first requirements.

**Результат:** PASS.

## 10. Итерация 9 — investment decision должен быть forward-looking, а не защищать sunk cost

**Критика:** portfolio nodes уже содержат значительный код и выполненную техническую работу. Это создаёт риск escalation of commitment: «мы столько сделали, значит надо продолжать».

**Сверка:** proposal прямо исключает tests/CI/build PASS, число commits, demo, repository existence, technical attractiveness, AI recommendation и sunk cost как самостоятельные continue/investment grounds.

Decision packet требует future value, future cost, customer/use/economic evidence, obligations, downside, reversibility, alternatives, opportunity cost и Owner workload.

`stop/retire candidate` остаётся proposal, а не automatic deletion — поэтому anti-sunk-cost discipline не нарушает history/data/obligation governance.

**Результат:** PASS.

## 11. Итерация 10 — AC-303 не должен поглотить AC-304/305/306 и обязан оставить однозначный handoff

**Критика:** как только для node формулируются investment criteria, легко одновременно решить, что это reusable module, куда его интегрировать с OS и какой продукт приоритетнее. Это разрушит Phase 3 sequencing.

**Сверка:** proposal содержит explicit reconciliation register:

- concrete budgets/relative capital priority → отдельное decision + `AC-306` context;
- standalone/reference/module/OS-candidate classification → `AC-304`;
- cross-product/OS dependency/Product Contract changes → `AC-305`;
- primary accountability → сохраняется Approved AC-302;
- product implementation truth → остаётся product-owned.

После Owner approval AC-303 следующий canonical action остаётся `AC-304`.

**Результат:** PASS.

## 12. Acceptance matrix

| Проверка | Результат |
|---|---|
| canonical AC-303 scope используется вместо повторного AC-301 wording | PASS |
| все `PORT-001…PORT-007` покрыты | PASS |
| investment envelope не является budget authorization | PASS |
| invented financial thresholds отсутствуют | PASS |
| `Unknown` не трактуется как `zero` | PASS |
| direct cash exposure учтён | PASS |
| recurring cost учтён | PASS |
| engineering/delivery effort учтён | PASS |
| Owner attention/bottleneck учтён | PASS |
| opportunity cost учтён | PASS |
| customer/obligation downside учтён | PASS |
| security/data/privacy downside учтён | PASS |
| legal/IP/compliance downside учтён | PASS |
| critical dependency/sovereignty учтены | PASS |
| continuity/recovery учтены | PASS |
| existing AC-301 dispositions сохранены | PASS |
| existing AC-302 POS-003 mapping сохранён | PASS |
| POS-002 functional accountability сохранена | PASS |
| POS-004 functional accountability сохранена | PASS |
| POS-005 finance accountability сохранена | PASS |
| POS-006 risk accountability сохранена | PASS |
| POS-001 escalation/integration сохранена | PASS |
| `ROD-01…ROD-09` не ослаблены | PASS |
| AM ceiling не расширен | PASS |
| `continue` не означает automatic funding/growth | PASS |
| `contain` не означает silent abandonment/delete | PASS |
| `clarify` не означает platform implementation/admission | PASS |
| contained nodes не получают growth mandate | PASS |
| PORT-007 защищён от speculative platform build | PASS |
| product-specific facts привязаны к exact reviewed blobs | PASS |
| product repositories остаются canonical для implementation/status | PASS |
| technical PASS/repo activity не равны business readiness | PASS |
| sunk cost отвергнут как самостоятельный investment argument | PASS |
| AI recommendation не является Owner approval | PASS |
| stop/retire — proposal до competent decision | PASS |
| legal/customer/Product/OS authority не присваивается Company artifact | PASS |
| AC-304 classification не выполнена заранее | PASS |
| AC-305 dependency/OS reconciliation не выполнена заранее | PASS |
| AC-306 priority ranking не выполнен заранее | PASS |
| после approval следующим действием остаётся AC-304 | PASS |

## 13. Review-budget conclusion

Использованы все `10 of maximum 10` итераций. Причина — AC-303 затрагивает одновременно business value, capital exposure, Owner bottleneck, security/data/legal downside, technology sovereignty и семь portfolio states, а ошибка здесь могла бы создать либо скрытое blanket funding, либо преждевременное закрытие полезного/обязательного work.

После десятой итерации material contradiction в declared scope не осталось. Оставшиеся вопросы — реальные суммы/бюджеты, module/reference classification, OS/dependency contracts и relative portfolio priority — намеренно оставлены downstream governance, а не замаскированы как незавершённость AC-303.

## 14. Итог

`PASS — material consensus reached at 10 of maximum 10 iterations.`

AC-303 `Proposed 0.9.0`, точный проверенный blob `e246d06e87b4221ad85718d2aeeb4e3486bf388e`, готов к **явному Owner approval**.

До approval документ не создаёт бюджет, не меняет dispositions, не санкционирует spend/stop/retire, не обновляет `PORTFOLIO.md`/`ROADMAP.md` как будто AC-303 уже binding, и `AC-304` не становится Current.
