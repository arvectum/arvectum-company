# AC-306 — Перекрёстная проверка приоритизации портфеля по капиталу, экономике и вниманию собственника

Статус: `Complete / PASS for Owner approval`
Дата проверки: `2026-08-21`
Итераций выполнено: `10 of maximum 10`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-306 — Portfolio prioritization by capital, economics and Owner attention`

Проверенный proposal:

- `docs/portfolio/AC-306-PORTFOLIO-PRIORITIZATION-CAPITAL-ECONOMICS-OWNER-ATTENTION.md`;
- статус: `Proposed 0.9.0`;
- immutable git blob SHA: `d254c6441baca5f22828648ecfa701d04c8344b1`.

Статус утверждения: `Pending explicit Owner approval of the exact reviewed proposal`.

## 1. Review gate

AC-306 должен быть отклонён, если он:

- превращает product ranking в новый Company flagship;
- игнорирует AC-106 `P0…P3` и реальные customer/cash obligations;
- выдумывает выручку, маржу, ROI, CAC/LTV, стоимость часа Owner или финансовые пороги;
- ранжирует продукты по объёму кода, технической зрелости или sunk cost;
- нарушает AC-303 `continue/contain/clarify` treatment;
- использует `RI-OS-CONSUMER` или `RI-PRODUCT-FAMILY` как автоматический funding claim;
- делает hard dependency там, где AC-305 установил только evidence/reference relation;
- направляет Owner attention в повторные попытки пройти известный недоступный local/external gate;
- превращает customer feedback loop в бесконечное бесплатное расширение scope;
- автоматически re-band'ит продукт без нового decision evidence;
- создаёт budget, spend/customer commitment, Product Contract или legal/IP/data effect;
- выполняет AC-307 вместо подготовки clean handoff.

## 2. Итерация 1 — Portfolio ranking не должен заменить Company business priority

**Критика:** ранжирование `PORT-*` легко сделать центром всей Company roadmap и тем самым фактически отменить утверждённый flagship `«ИИ-компания под ключ»` и AC-106 paired loop.

**Сверка:** proposal прямо подчиняет AC-306 AC-106:

- `P0` — obligations/cash/material risk;
- `P1` — flagship market evidence + minimal reference operating model;
- `P2` — product/OS work только при прямой связи с revenue/obligation/evidence/blocker;
- `P3` — speculative expansion.

В разделе 9 отдельно подтверждено, что flagship не переопределяется, а Arvectum OS не превращается в обычный `PORT-*`.

**Результат:** PASS.

## 3. Итерация 2 — Нельзя компенсировать отсутствие экономики псевдоточным score

**Критика:** AC-306 прямо требует capital/economics ranking, поэтому возникает соблазн назначить искусственные веса, ROI, баллы или проценты на основе технической зрелости.

**Сверка:** proposal:

- прямо запрещает фабрикацию revenue/margin/CAC/LTV/ROI/Owner-hours;
- использует семь качественных dimensions `D1…D7`;
- опирается на AC-102 rule `Unknown ≠ zero`;
- не создаёт numeric spend threshold или budget;
- требует refresh при появлении реального accounting/customer evidence.

Такой подход слабее количественной модели только внешне: на текущем evidence он честнее и соответствует AC-303.

**Результат:** PASS.

## 4. Итерация 3 — Почему Discount Parser выше Tender Agent

**Критика:** Tender Agent стратегически близок к procurement line и уже используется как OS reference consumer. Можно ошибочно поставить его первым из-за strategic familiarity или архитектурного значения.

**Сверка:** proposal ранжирует `PORT-002` как `A1`, а `PORT-001` как `A2` не по "важности продукта вообще", а по ближайшему evidence-backed use of scarce attention:

- AC-103 говорит, что bespoke client automation — самый доказанный реальный end-to-end customer lifecycle;
- Discount Parser имеет текущий client/product delivery contour и уже продвинут к acceptance/delivery;
- Tender Agent R0 functionally closed, но собственный `STATUS.md` ограничивает следующий этап quality/evidence work и прямо не разрешает mass external pilot.

`A1` означает сначала закрывать реальное acceptance/obligation/value loop, а не считать Discount Parser стратегическим центром Company.

Proposal также требует после accepted delivery вернуться к maintenance/freeze, если нет нового paid/second-consumer evidence. Это предотвращает вечное удержание `A1` по sunk cost.

**Результат:** PASS.

## 5. Итерация 4 — Tender Agent не должен получить broad growth mandate

**Критика:** `PORT-001` имеет много domain/OS evidence; Band A может быть прочитан как разрешение продолжать feature accumulation и автономизацию.

**Сверка:** `A2` ограничен:

- specific qualified pilot/procurement opportunity;
- measurable quality/evidence gap;
- flagship discovery hypothesis;
- quality/reliability over feature breadth;
- explicit exclusion of mass pilot, SaaS expansion, submission/EDS automation and broad customer commitment by implication.

Это соответствует AC-303 bounded continuation и текущему `STATUS.md`.

**Результат:** PASS.

## 6. Итерация 5 — Proxy Launcher: техническая зрелость не равна экономическому приоритету

**Критика:** Proxy Launcher технически очень зрел: productized Windows baseline, signing, cross-platform work. Если ranking вознаграждает engineering completeness, `PORT-003` должен оказаться в A. Но это воспроизведёт repository-driven strategy.

**Сверка:** proposal ставит его в `B1` потому что:

- Company-level standalone acquisition/purchase/renewal lifecycle пока не доказан;
- часть дальнейших шагов blocked by separate physical host;
- APL-IP path содержит human/legal gate;
- per-app routing имеет explicit production stop-gate и потенциально дорогую внешнюю signing/enforcement dependency.

При этом asset не обесценивается: разрешены support, baseline preservation и high-leverage IP/legal closure. Повышение требует credible paid demand/obligation или material issue, связанного с такой demand.

**Результат:** PASS.

## 7. Итерация 6 — Creative Test Agent: pilot readiness не должна имитировать market evidence

**Критика:** CTA имеет богатую feature/pilot/deployment базу и Arvectum OS external-consumer evidence. Это может создать ложное ощущение, что ещё один технический sprint приблизит коммерческий результат.

**Сверка:** `B2` отделяет technical readiness от customer evidence:

- AC-103 признаёт prepared pilot mechanics, но recurring conversion не доказан;
- реальный trigger — qualified design partner/customer с inputs, success criteria и plausible commercial/flagship-learning outcome;
- без trigger speculative model/scoring/deployment breadth откладывается;
- optional P8.06 OS consumer value не становится funding claim.

`docs/roadmap/CURRENT.md` имеет риск freshness drift относительно более поздних repository developments; proposal поэтому не использует его task pointer как самостоятельное доказательство коммерческой готовности. Business ranking опирается прежде всего на AC-103 и текущую runnable product foundation.

**Результат:** PASS.

## 8. Итерация 7 — Data Platform нельзя "чуть-чуть построить" под видом clarification

**Критика:** `PORT-007` уже существует как repository и AC-304 дал ему module-candidate hypothesis. Без hard boundary clarification может превратиться в постепенное создание shared datastore/crawler/platform до доказанных consumers.

**Сверка:** `C1` допускает только:

- named consumers;
- common contract sketch;
- boundary decomposition;
- migration/support burden estimate;
- rights/data/sovereignty/continuity/replacement review;
- measurable duplicated-cost/delivery-burden hypothesis.

Явно запрещены production shared datastore, generic crawler platform, data lake/vector/search и compulsory cross-product dependency. Promotion требует отдельного evidence-backed change/investment decision.

Это совместимо с AC-304 clarification-only и AC-305 no-hard-dependency baseline.

**Результат:** PASS.

## 9. Итерация 8 — Contain должен оставаться contain даже при полезном reuse evidence

**Критика:** `PORT-005` и `PORT-006` имеют рабочий код и полезные reference patterns. Ranking может незаметно вернуть их в growth queue, особенно если reuse кажется дешёвым.

**Сверка:** proposal сохраняет:

- `PORT-005` — maintenance/security/continuity/reference only; no parallel procurement growth product;
- `PORT-006` — completed-delivery support/evidence only; no generic-parser rewrite;
- real customer/support obligation может временно поднять **конкретную работу** в `P0`, но не меняет disposition автоматически.

Таким образом `P0 override` относится к obligation, а не к portfolio identity/status.

**Результат:** PASS.

## 10. Итерация 9 — Owner attention должен быть ограничителем, а не бесплатной переменной

**Критика:** даже правильные продуктовые идеи могут одновременно быть "маленькими", и Owner снова становится scheduler/reviewer для всех репозиториев.

**Сверка:** proposal требует для material work ответить:

1. why now;
2. exact bounded outcome;
3. exact Owner action;
4. what can proceed without Owner;
5. stop condition;
6. next decision enabled by evidence.

Также явно запрещена трата Owner attention на known-unavailable gate retries, raw test review, speculative polish и simultaneous feature expansion без ranked business reason.

Числовой cap concurrent workstreams намеренно не придуман: текущего evidence для оптимального числа нет. Вместо него установлена reason/trigger discipline и минимизация discretionary context switching.

**Результат:** PASS.

## 11. Итерация 10 — Ranking и trigger не должны стать скрытой авторизацией

**Критика:** термины `A`, `promotion trigger`, `elevate` и `bounded spend` могут быть неверно прочитаны как автоматическое разрешение денег, customer commitments или re-banding.

**Сверка:** proposal содержит четыре независимых предохранителя:

- Section 7: no budget / no numeric spend threshold;
- Section 8: при material new evidence нужно **prepare a new decision**;
- Section 10: AC-306 требует Owner approval как `ROD-02` + `ROD-04`, а specific material decisions всё равно проходят applicable authority/evidence path;
- Band B trigger означает причину для re-evaluation bounded slice, а не self-executing lifecycle/authority transition.

No Product Contract, shared module, legal/IP/data right, price, SLA, hiring, spend or customer commitment создаётся ranking'ом.

Handoff в AC-307 чистый: final M3 review остаётся отдельным gate.

**Результат:** PASS.

## 12. Acceptance matrix

| Проверка | Результат |
|---|---|
| AC-106 P0…P3 hierarchy preserved | PASS |
| flagship remains `ИИ-компания под ключ` | PASS |
| Arvectum OS not treated as ordinary PORT node | PASS |
| no fictional financial metrics | PASS |
| Unknown cost/risk not treated as zero | PASS |
| technical maturity not used as sole priority | PASS |
| sunk cost not used as priority claim | PASS |
| Owner attention treated as scarce capital | PASS |
| P0 obligation override is explicit | PASS |
| P0 override does not silently re-band node | PASS |
| PORT-002 A1 justified by real client-delivery evidence | PASS |
| PORT-002 growth/platformization remains gated | PASS |
| PORT-001 A2 bounded to revenue/evidence work | PASS |
| PORT-001 mass/autonomous expansion not authorized | PASS |
| PORT-003 maturity does not create A-band automatically | PASS |
| PORT-003 blocked host work does not consume continuous attention | PASS |
| PORT-003 per-app stop-gate preserved | PASS |
| PORT-004 pilot readiness separated from market evidence | PASS |
| PORT-004 OS reference status not funding claim | PASS |
| PORT-007 remains clarification-only | PASS |
| PORT-007 material build prohibited | PASS |
| PORT-005 contain preserved | PASS |
| PORT-006 contain preserved | PASS |
| AC-305 no-hard-dependency conclusion preserved | PASS |
| no automatic shared parser/procurement runtime created | PASS |
| no budget/spend authorization created | PASS |
| no customer commitment/price/SLA created | PASS |
| no legal/IP/data right created | PASS |
| ROD-02 capital gate preserved | PASS |
| ROD-04 portfolio decision gate preserved | PASS |
| applicable ROD-03/06/08/09 not weakened | PASS |
| trigger requires re-evaluation rather than automatic promotion | PASS |
| product roadmap ownership preserved | PASS |
| AC-307 not executed prematurely | PASS |
| clean handoff to AC-307 | PASS |

## 13. Review conclusion

Использованы все `10 of maximum 10` итераций, потому что AC-306 является первым Phase 3 gate, который не только классифицирует portfolio nodes, но и создаёт реальный default order конкуренции за scarce capital/engineering/Owner attention.

Главный вывод cross-review:

> Правильный результат AC-306 — не выбрать "любимый продукт", а сделать так, чтобы реальная obligation/revenue/evidence работа системно вытесняла speculative completeness, а blocked/contained/clarification-only узлы не забирали внимание только потому, что в их репозиториях есть следующий технический task.

Exact proposal blob `d254c6441baca5f22828648ecfa701d04c8344b1` прошёл review без оставшихся material objections.

**Verdict:** `Complete / PASS for explicit Owner approval`.

После Owner approval должны быть выполнены только publication/synchronization mechanics:

1. создать Owner decision с exact proposal/review blob references;
2. опубликовать AC-306 `Approved 1.0.0` без переписывания reviewed proposal;
3. обновить `docs/portfolio/PORTFOLIO.md` новым priority baseline;
4. обновить canonical `docs/roadmap/ROADMAP.md`: AC-306 → `Complete / PASS`, current → `AC-307`;
5. затем выполнить `AC-307 — Итоговая проверка управления портфелем и закрытие M3` как отдельный gate.