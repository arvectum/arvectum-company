# AC-302 — Перекрёстная проверка закрепления ответственной Position за узлами портфеля

Статус: `Complete / PASS for Owner approval`
Дата проверки: `2026-08-21`
Итераций выполнено: `10 of maximum 10`
Результат: `PASS — все семь portfolio nodes получают одну ясную Company-level accountability связь с существующей POS-003 без создания fake product headcount; functional accountability POS-001/POS-002/POS-004/POS-005/POS-006, ROD boundaries, Assignments, access, continuity, Product/OS/customer authority и scopes AC-303…AC-306 сохранены`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-302 — Assign accountable Position to each active product/initiative`
Проверенный документ: `docs/portfolio/AC-302-PORTFOLIO-ACCOUNTABLE-POSITION-MAPPING.md`
Проверенная редакция: `Proposed 0.9.0`
Проверенный git blob SHA: `29bec89402118ddfc061501b8b25f5c0000d65a4`
Максимум итераций: `10`
Статус утверждения: `Pending explicit Owner approval of the exact reviewed proposal`

## 1. Назначение проверки

AC-302 следует каноническому ROADMAP `0.23.0`: его scope — **закрепить accountable Position за каждым активным/materially retained portfolio node**, а не повторять уже закрытую AC-301 identity/boundary reconciliation.

Проверка должна отвергнуть proposal, если он:

- создаёт по Position на каждый repository без evidence;
- смешивает Company-level node stewardship с product implementation ownership;
- делает текущего Owner Principal или AI executor персональным «владельцем продукта»;
- превращает POS-003 в коммерческую, инженерную, финансовую или security authority;
- молча делегирует `ROD-*` decisions;
- расширяет AC-205 Assignment или AC-206 access;
- оставляет contained/clarify nodes без accountable custodian;
- предрешает AC-303 investment criteria, AC-304 module classification, AC-305 OS dependencies или AC-306 prioritization.

## 2. Итерация 1 — scope должен соответствовать каноническому AC-302

**Критика:** в пользовательской формулировке повторено русское название AC-301 — «сверка идентичности, границ и владения». Если следовать ему буквально, работа продублирует уже Approved AC-301 и нарушит roadmap sequencing.

**Сверка:** ROADMAP `0.23.0` однозначно определяет AC-302 как `Assign accountable Position to each active product/initiative`. Proposal следует именно этому binding scope и использует AC-301 как вход, а не переписывает его.

**Результат:** PASS.

## 3. Итерация 2 — одна POS-003 для семи nodes может выглядеть как чрезмерная централизация

**Критика:** назначить одну Position primary accountable для всех семи nodes легко интерпретировать как новый bottleneck или фиктивное «управление продуктами из центра».

**Сверка:** AC-204 уже специально создал `POS-003 — Portfolio & Product Lead` под `F-04` и определил accountable outcome: каждый material portfolio node должен иметь purpose/status/accountable question, а continue/change/stop/reuse evidence — быть подготовлено до material decision. Это ровно Company-level accountability, требуемая AC-302.

Proposal не утверждает, что POS-003 выполняет все функции продуктов. Он отдельно сохраняет commercial/customer, engineering/release, finance и security accountability у POS-002/004/005/006 и operating integration у POS-001.

**Результат:** PASS.

## 4. Итерация 3 — нельзя применять скрытое правило «один продукт — одна должность»

**Критика:** четыре `continue` products могут казаться достаточным основанием создать четыре Product Manager/Product Owner Positions.

**Сверка:** AC-204 прямо запрещает создавать one Product Manager/Product Owner per repository без evidence и допускает product-specific Positions только при достаточной independent revenue/customer obligations/roadmap complexity/investment/domain accountability. AC-302 не располагает новыми operating evidence, доказывающими такой split.

Proposal поэтому сохраняет Initial Position Registry без изменения и вводит explicit future split triggers вместо fake headcount.

**Результат:** PASS.

## 5. Итерация 4 — node accountability не должна поглощать functional accountability

**Критика:** слово `accountable` может быть прочитано как end-to-end ownership продукта, включая customer promise, release, economics и risk acceptance.

**Сверка:** proposal задаёт узкий предмет `PORT-* → POS-003`: identity/status/lifecycle/question/evidence/escalation на Company portfolio level.

Он явно сохраняет:

- POS-002 — commercial/customer scope;
- POS-004 — engineering/release scope;
- POS-005 — finance/obligations evidence;
- POS-006 — security/risk/continuity assurance;
- POS-001 — Company operating integration and decision routing.

Technical PASS, customer acceptance, finance evidence или security exception не становятся portfolio decision по импликации.

**Результат:** PASS.

## 6. Итерация 5 — текущий Owner Principal нельзя сделать постоянным product owner

**Критика:** AC-205 сейчас реализует POS-003 как Hybrid с текущим Owner Principal. Если AC-302 просто «назначает владельца», может возникнуть персонально-зависимая модель и смешение Owner capacity с Position capacity.

**Сверка:** proposal назначает **Position**, а не Principal. Сохраняется цепочка `PORT node → POS-003 → valid Assignment → runtime/access → execution`. Current Owner Principal остаётся текущим Assignment evidence, но replacement Principal/runtime не меняет node accountability автоматически.

Owner capacity, General Director/legal capacity и POS-003 остаются разными authority sources/capacities.

**Результат:** PASS.

## 7. Итерация 6 — `contain` и `clarify` nodes тоже должны иметь владельца вопроса, но не growth mandate

**Критика:** PORT-005/006/007 не являются обычными active growth products. Назначение POS-003 может быть воспринято как их автоматическое продолжение или финансирование.

**Сверка:** proposal различает accountability и investment disposition:

- `PORT-005` и `PORT-006` получают POS-003 как portfolio custodian, сохраняющий contained asset и подготавливающий merge/reuse/retire/continue evidence;
- `PORT-007` получает POS-003 только за clarification/admission package;
- никакой scope expansion, budget или growth decision не следует из mapping.

AC-303/304/306 остаются обязательными downstream gates.

**Результат:** PASS.

## 8. Итерация 7 — Reserved Owner Decisions и delegation ceiling должны остаться неизменны

**Критика:** Product/portfolio accountability особенно близка к `ROD-04 — Major portfolio, initiative and investment decisions`, а также может затронуть `ROD-01/02/03/06/07/08/09`.

**Сверка:** proposal оставляет POS-003 только в approved initial ceiling `AM-0/1/2`; AC-202 `ROD-01…ROD-09` перечислены как hard escalation boundary. Major start/stop/merge/investment, material capital, external commitment, risk/data/IP/sovereignty и cross-repository/OS decisions не делегируются.

AC-302 therefore creates accountability for **preparation, bounded stewardship and escalation**, not material final authority.

**Результат:** PASS.

## 9. Итерация 8 — Company/Product/Arvectum OS/customer boundaries не должны размыться

**Критика:** одна Company Position, отвечающая за portfolio node, может начать считаться владельцем product code, customer authority или OS contract.

**Сверка:** proposal сохраняет product repositories canonical для implementation/status/roadmap, customer authority — customer-owned, OS Product Contracts/platform semantics — OS-owned. POS-003 отвечает только за Company-level relationship to those sources.

P6.02 stale locator остаётся вопросом AC-305/OS governance, а не правкой или новой authority AC-302.

**Результат:** PASS.

## 10. Итерация 9 — Assignment, access и continuity не должны расширяться от mapping

**Критика:** product accountability может использоваться как оправдание product repository admin, production credentials, customer data access или расширения AI permissions.

**Сверка:** AC-302 прямо не меняет AC-205 Assignments и AC-206 ceilings. POS-003 mapping не создаёт W/P/K/E access в product/customer/financial systems. Access remains least-privilege and separately provisioned.

AC-207 также сохраняется: AI loss/human loss/replacement runtime не передают authority; при Owner absence AI может готовить evidence, но не наследует human AM-2/ROD/legal power.

**Результат:** PASS.

## 11. Итерация 10 — end-to-end Phase 3 handoff должен оставить AC-303 следующим шагом

**Критика:** AC-302 может незаметно начать отвечать на вопросы «сколько инвестировать», «что закрыть», «что сделать модулем», «что подключить к OS», то есть поглотить AC-303…AC-306.

**Сверка:** proposal оставляет только accountability mapping и node-specific accountable questions. Он не отвечает на них. Reconciliation register направляет:

- investment/cost/risk/continue-change-stop criteria → AC-303;
- product/reference/module/OS-candidate classification → AC-304;
- inter-product/OS dependencies/contracts → AC-305;
- capital/economic/Owner-attention priority → AC-306.

После approval AC-302 следующий roadmap action остаётся `AC-303`.

**Результат:** PASS.

## 12. Acceptance matrix

| Проверка | Результат |
|---|---|
| scope соответствует canonical ROADMAP AC-302 | PASS |
| все `PORT-001…PORT-007` получают primary accountable Position | PASS |
| primary Position = существующая `POS-003`, а не новая role/headcount | PASS |
| mapping выведен из approved F-04/POS-003 scope | PASS |
| правило «один продукт — одна должность» отвергнуто | PASS |
| current Position Registry не требует изменения | PASS |
| current AC-205 Assignments не изменены | PASS |
| Owner Principal не превращён в постоянный product identity/authority | PASS |
| AI/runtime не превращён в authority source | PASS |
| POS-002 commercial/customer accountability сохранена | PASS |
| POS-004 engineering/release accountability сохранена | PASS |
| POS-005 finance/obligation accountability сохранена | PASS |
| POS-006 security/risk/continuity accountability сохранена | PASS |
| POS-001 operating integration/escalation preserved | PASS |
| `ROD-01…ROD-09` hard boundary preserved | PASS |
| AM ceiling remains `AM-0/1/2` | PASS |
| contained nodes have custodian without growth authorization | PASS |
| clarify node has clarification owner without admission by implication | PASS |
| Product implementation truth remains product-owned | PASS |
| customer authority remains customer-owned | PASS |
| OS contracts/semantics remain OS-owned | PASS |
| access ceilings are not broadened | PASS |
| continuity/replacement does not transfer authority | PASS |
| no budget/investment/priority decision is made | PASS |
| no reusable-module classification is made | PASS |
| no OS dependency/Product Contract change is made | PASS |
| future product-specific Position requires explicit evidence/change proposal | PASS |
| AC-303 remains next canonical Phase 3 action | PASS |

## 13. Review-budget conclusion

Использованы все `10 of maximum 10` итераций, потому что AC-302 связывает семь portfolio identities с общей M2 Position model и должен одновременно доказать отсутствие fake headcount, over-centralization, authority broadening и functional-boundary collapse.

После десятой итерации material contradiction в declared scope не осталось. Оставшиеся вопросы являются именно содержанием AC-303…AC-306 или будущими operating-evidence triggers для Position-model change, а не дефектами AC-302.

## 14. Итог

`PASS — material consensus reached at 10 of maximum 10 iterations.`

AC-302 `Proposed 0.9.0`, точный проверенный blob `29bec89402118ddfc061501b8b25f5c0000d65a4`, готов к **явному Owner approval**.

До approval mapping `PORT-001…PORT-007 → POS-003` остаётся reviewed proposal, действующий `PORTFOLIO.md` и ROADMAP не переводятся на новый binding state, а AC-303 не становится Current.
