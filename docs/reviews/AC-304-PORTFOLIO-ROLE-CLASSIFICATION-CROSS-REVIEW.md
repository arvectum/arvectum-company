# AC-304 — Перекрёстная проверка классификации ролей портфеля

Статус: `Complete / PASS for Owner approval`
Дата проверки: `2026-08-21`
Итераций выполнено: `10 of maximum 10`
Результат: `PASS — PORT-001…PORT-007 разделены по standalone/reference/module-candidate/OS-promotion-hypothesis без смешения product identity, reuse evidence, Company module ownership и Arvectum OS capability lifecycle; новых Company-side OS capability candidates не создано; PORT-007 ограничен clarification-only module hypothesis`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-304 — Standalone product / reference implementation / module candidate / Arvectum OS capability candidate classification`
Проверенный документ: `docs/portfolio/AC-304-PORTFOLIO-ROLE-CLASSIFICATION.md`
Проверенная редакция: `Proposed 0.9.0`
Проверенный git blob SHA: `533ccef1d28bf9a154da9b99dd1c4226c19d166b`
Максимум итераций: `10`
Статус утверждения: `Pending explicit Owner approval of the exact reviewed proposal`

## 1. Назначение проверки

AC-304 опасен двумя противоположными ошибками:

1. **platform gravity** — объявить общий код, похожие функции или слово `platform` доказательством shared module / OS capability;
2. **under-reuse** — оставить уже доказанные reusable patterns и Product Contract reference consumers неявными, из-за чего Компания продолжит повторно изобретать решения.

Proposal должен быть отклонён, если он:

- меняет AC-301 identity/disposition;
- превращает AC-302 stewardship в architecture/platform authority;
- нарушает AC-303 contain/clarify investment boundaries;
- считает independently runnable repository самостоятельным growth product автоматически;
- считает code similarity или common stack достаточным для module candidate;
- считает Product Contract consumer реализацией OS capability;
- присваивает Company document lifecycle status `Candidate/Incubating/Active` в Arvectum OS;
- делает `Data Platform` platform по названию;
- создаёт скрытый merge/rewrite между Discount Parser и Doors Parser;
- использует reference classification как разрешение копировать code/customer data;
- преждевременно выполняет AC-305 dependency reconciliation или AC-306 priority ranking.

## 2. Итерация 1 — четыре роли должны быть различимы и не обязаны быть взаимоисключающими

**Критика:** формулировка AC-304 через `/` может быть ошибочно прочитана как четыре взаимоисключающих корзины. Тогда реальный standalone product, который одновременно является Product Contract reference consumer, пришлось бы искусственно поместить только в одну категорию.

**Сверка:** proposal разделяет смысл ролей:

- standalone — product identity/current portfolio role;
- reference — evidence/reuse role;
- module candidate — Company/product-family shared-mechanism hypothesis;
- OS candidate — только Company-side promotion hypothesis, не OS lifecycle.

Прямо разрешено сочетание standalone + reference. Candidate labels не меняют product identity.

**Результат:** PASS.

## 3. Итерация 2 — AC-304 не должен переписать AC-301/302/303

**Критика:** новая role matrix может незаметно отменить disposition `contain/clarify` либо превратить reference/module label в новый growth mandate.

**Сверка:** proposal сохраняет:

- `PORT-001…PORT-007` identities и repositories из AC-301;
- `PORT-* → POS-003` Company stewardship из AC-302;
- AC-303 treatments `continue / contain / clarify before investment`.

Особенно важно:

- PORT-005/006 остаются contained, несмотря на reference role;
- PORT-007 остаётся `clarify before investment`, несмотря на module-candidate label;
- standalone PORT-001…004 не получают funding authorization сверх AC-303 envelope.

**Результат:** PASS.

## 4. Итерация 3 — independently runnable artifact не равен текущему standalone product mandate

**Критика:** PORT-005 и PORT-006 технически могут существовать самостоятельно. Если это автоматически считать `standalone product = YES`, classification будет противоречить approved containment и размоет portfolio discipline.

**Сверка:** proposal различает runtime independence и Company portfolio role. PORT-005/006 получают `standalone = NO as current Company portfolio role`, потому что AC-301/303 уже определили их как contained experiment/completed delivery asset. Их самостоятельный код/история сохраняются, но growth product mandate не создаётся.

PORT-001/002/003/004 имеют действующий product contour, самостоятельный use/customer problem и approved `continue` envelope, поэтому `standalone = YES` подтверждён.

**Результат:** PASS.

## 5. Итерация 4 — Product Contract validation делает продукт reference consumer, но не реализацией OS capability

**Критика:** Tender Agent, Discount Parser и Creative Test Agent действительно используются Arvectum OS как реальные validation/onboarding targets. Термин `reference implementation` может ошибочно превратить их в reference implementations самой платформы или владельцев CAP-* semantics.

**Сверка:** proposal вводит subtype `RI-OS-CONSUMER` и явно говорит, что это **product-side consumer implementation**:

- P6.02 — first real tender Product Contract target с CAP-001/CAP-004;
- P6.06 — second materially distinct Discount Parser target с CAP-004;
- P8.06 — external Creative Test Agent consumer onboarding через CAP-004.

Во всех трёх случаях domain semantics остаются product-owned. Existing CAP-* remain OS-owned.

Отдельно proposal не чинит stale P6.02 locator `arutyunoveth/ai-corporation`; это оставлено AC-305.

**Результат:** PASS.

## 6. Итерация 5 — Tender Small-Volume Calculator должен быть reference source, а не автоматически shared procurement module

**Критика:** PORT-005 и Tender Agent находятся в одном procurement domain. Это создаёт соблазн либо слить продукты, либо вынести общую procurement library без доказательства многопотребительской потребности.

**Сверка:** direct evidence `tender_app_reuse_audit.md` показывает фактический selective reuse:

- использованы архитектурные идеи read-only discovery, normalized result, attachment manifest, skip reasons, manual fallback;
- code не перенесён монолитно;
- browser/auth/install/scheduler/price-search части намеренно не перенесены из-за boundary/risk mismatch.

Поэтому PORT-005 классифицирован как `RI-PRODUCT-FAMILY`, но `module candidate = NO`. Это соответствует evidence и предотвращает false generalization.

**Результат:** PASS.

## 7. Итерация 6 — Discount Parser + Doors Parser дают evidence для parser-family hypothesis, но не образуют generic platform автоматически

**Критика:** оба продукта парсят внешние источники, нормализуют/дедуплицируют/проверяют данные. Простое сходство могло бы привести к преждевременному объединению репозиториев или generic crawler/data platform.

**Сверка:** proposal делает более узкое решение:

- PORT-002 остаётся standalone product и reference evidence source;
- PORT-006 остаётся contained completed-delivery reference implementation;
- весь Discount Parser или Doors Parser не становится shared module;
- reusable hypothesis вынесена только в PORT-007;
- PORT-007 boundary ограничен source/adapter, intake/fetch, extraction envelope, normalization hooks, provenance, run/error isolation, dedup/quality/review hooks;
- Offer/Telegram, door-domain schemas, tender semantics, shared customer datastore, data lake/vector/search и OS semantics исключены.

Это соответствует AC-301 запрету считать PORT-002/006/007 generic parser/platform автоматически.

**Результат:** PASS.

## 8. Итерация 7 — PORT-007 module candidate не должен обойти AC-303 `clarify before investment`

**Критика:** само слово `candidate` легко становится de facto approval на shared implementation, особенно когда repository уже называется `data-platform`.

**Сверка:** proposal использует `YES — clarification-only candidate` и устанавливает hard pre-build evidence:

- конкретные consumers;
- common contract;
- economic case;
- migration cost;
- rights/data;
- sovereignty;
- continuity;
- owner/support responsibility;
- exit path.

До этого разрешены только discovery, contract sketch, evidence inventory и bounded proof внутри уже действующих authority/investment limits. Production/shared operational reliance не создаётся.

**Результат:** PASS.

## 9. Итерация 8 — Proxy Launcher нельзя искусственно сделать reference/module только потому, что его release engineering полезен

**Критика:** PORT-003 имеет сильные Windows productization patterns: installer/portable release, recovery, rollback, DPAPI, repair/uninstall, signing path. Это полезно и может соблазнить объявить его Company reference implementation или shared desktop toolkit без второго consumer/evidence.

**Сверка:** proposal оставляет PORT-003 `standalone = YES`, остальные роли `NO`. Возможная будущая release-tooling/standard hypothesis прямо требует отдельного consumer/economic evidence и не создаётся AC-304.

Такой результат показывает, что reference status присваивается не за техническое качество, а за доказанную reuse/validation функцию.

**Результат:** PASS.

## 10. Итерация 9 — пустой список новых OS capability candidates должен быть доказанным boundary result, а не упущением

**Критика:** задача явно содержит категорию `кандидат в возможность Arvectum OS`, и может возникнуть давление обязательно поместить туда хотя бы один node.

**Сверка:** RFC-0001 требует domain-neutral organizational ability, outcome, owner, consumers/strategic need и reuse hypothesis. Proposal показывает, что текущий real reuse уже происходит через **существующие** OS capabilities:

- Tender Agent → CAP-001/CAP-004;
- Discount Parser → CAP-004;
- Creative Test Agent → CAP-004.

Product-domain semantics и parser/data-extraction module hypothesis не должны становиться OS capabilities ради заполнения категории. Поэтому `0` новых Company-side OS capability candidates — корректный anti-platform-gravity результат.

**Результат:** PASS.

## 11. Итерация 10 — AC-304 должен оставить clean handoff в AC-305/306 и не создавать hidden authority/IP/data effects

**Критика:** role classification почти неизбежно касается dependencies, migration, funding и reusable code. Без explicit boundary proposal мог бы скрыто создать:

- cross-repo dependency;
- Product Contract change;
- code/data copy authorization;
- priority/funding order;
- access/authority expansion.

**Сверка:** proposal явно оставляет:

- dependency/Product Contract reconciliation, stale P6.02 locator и exact OS dependencies → AC-305;
- relative capital/economics/Owner-attention ranking → AC-306;
- module implementation → отдельный Company/product decision;
- OS lifecycle admission → Arvectum OS governance;
- IP/license/customer-data rights → применимые legal/contractual sources;
- spend/access/external commitment → existing authority gates.

После approval следующим canonical action остаётся AC-305.

**Результат:** PASS.

## 12. Acceptance matrix

| Проверка | Результат |
|---|---|
| покрыты все `PORT-001…PORT-007` | PASS |
| standalone и reference разделены | PASS |
| reference и module candidate разделены | PASS |
| Company module и OS capability разделены | PASS |
| допускается standalone + reference без identity conflict | PASS |
| AC-301 identities сохранены | PASS |
| AC-301 dispositions сохранены | PASS |
| AC-302 accountability сохранена | PASS |
| AC-303 investment treatments сохранены | PASS |
| PORT-001 standalone evidence есть | PASS |
| PORT-002 standalone evidence есть | PASS |
| PORT-003 standalone evidence есть | PASS |
| PORT-004 standalone evidence есть | PASS |
| PORT-005 не получает growth product mandate | PASS |
| PORT-006 не получает growth product mandate | PASS |
| PORT-007 не объявлен standalone product | PASS |
| P6.02 использован как reference-consumer evidence без silent locator repair | PASS |
| P6.06 использован как materially distinct reference-consumer evidence | PASS |
| P8.06 использован как external consumer reference evidence | PASS |
| Tender App selective reuse доказан direct audit | PASS |
| Tender App не объявлен shared procurement module | PASS |
| Discount Parser сохраняет product-owned Offer/Telegram semantics | PASS |
| Doors Parser сохраняет door/client-specific semantics | PASS |
| PORT-002/006 не сливаются автоматически | PASS |
| PORT-007 ограничен data acquisition/extraction module hypothesis | PASS |
| PORT-007 не получает generic data lake/vector/search scope | PASS |
| PORT-007 candidate не разрешает material build | PASS |
| Proxy Launcher не получает speculative reference/module status | PASS |
| новых Company-side OS capability candidates = 0 обосновано | PASS |
| existing CAP-001/CAP-004 не присвоены Company/Product scope | PASS |
| Company artifact не присваивает OS lifecycle status | PASS |
| code similarity/common stack недостаточны для promotion | PASS |
| reference status не является code/data copy permission | PASS |
| customer/cross-customer rights не создаются | PASS |
| legal/IP rights не создаются | PASS |
| access/authority не расширяются | PASS |
| funding/priority не создаются | PASS |
| AC-305 не выполнен заранее | PASS |
| AC-306 не выполнен заранее | PASS |
| clean handoff в AC-305 сохранён | PASS |

## 13. Review-budget conclusion

Использованы все `10 of maximum 10` итераций, потому что AC-304 одновременно затрагивает семь разных product states, реальное Product Contract evidence из Arvectum OS, уже состоявшийся selective reuse между Tender App и Tender Agent и потенциальную parser-family consolidation через PORT-007.

Главный результат review — не максимизация числа reusable layers, а **минимально достаточная классификация**:

- standalone products: `PORT-001, PORT-002, PORT-003, PORT-004`;
- reference implementations/consumers: `PORT-001, PORT-002, PORT-004, PORT-005, PORT-006`;
- Company/product-family module candidates: `PORT-007` only, clarification-only;
- new Company-side Arvectum OS capability candidates: `none`.

После десятой итерации material contradiction в declared AC-304 scope не осталось. Реальные dependency contracts и relative investment priority намеренно оставлены AC-305/306.

## 14. Итог

`PASS — material consensus reached at 10 of maximum 10 iterations.`

AC-304 `Proposed 0.9.0`, точный проверенный blob `533ccef1d28bf9a154da9b99dd1c4226c19d166b`, готов к **явному Owner approval**.

До approval документ не меняет canonical `PORTFOLIO.md`, не создаёт module implementation, не изменяет Arvectum OS и не закрывает AC-304 в roadmap.
