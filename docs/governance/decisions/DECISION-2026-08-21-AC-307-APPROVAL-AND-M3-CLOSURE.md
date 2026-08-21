# Решение собственника — утверждение AC-307 и закрытие M3

Статус: `Approved`
Дата: `2026-08-21`
Владелец решения: собственник ООО «Арвектум»
Репозиторий: `arvectum/arvectum-company`
Решение: `AC-307 — Final portfolio governance review and M3 closure`

## 1. Явное решение

Собственник явно утвердил AC-307 формулировкой:

> `AC-307 утверждаю`

Утверждение относится к точной проверенной редакции:

- proposal: `docs/portfolio/AC-307-PORTFOLIO-GOVERNANCE-REVIEW-AND-M3-CLOSURE.md`;
- proposal status: `Proposed 0.9.0`;
- immutable proposal blob SHA: `904b9e5ffa12caeb082b3bf23a89aff251ebe8c4`;
- cross-review: `docs/reviews/AC-307-PORTFOLIO-GOVERNANCE-M3-CLOSURE-CROSS-REVIEW.md`;
- cross-review result: `10 of maximum 10`, `Complete / PASS for Owner approval`;
- immutable cross-review blob SHA: `bc3c4992f12dabaeb155f055373da292278cd791`.

Эти blob SHA фиксируют именно те редакции, которые были представлены собственнику перед утверждением.

## 2. Утверждённый результат AC-307

Собственник утверждает вывод итоговой проверки о том, что AC-301…AC-306 образуют внутренне согласованный Company-level portfolio-governance baseline:

`identity/disposition → accountable Position → investment/cost/risk treatment → role/reuse classification → dependency/Product Contract map → capital/economics/Owner-attention priority`.

Материальных противоречий, блокирующих закрытие M3, не обнаружено.

Утверждается, в частности, что:

- `PORT-001…PORT-007` имеют стабильные Company identities, repository locators, dispositions и accountable Position;
- `POS-003 — Portfolio & Product Lead` является primary Company-level portfolio steward, но не поглощает commercial/engineering/finance/security или Reserved Owner authority;
- `continue`, reference status и Band A/B не являются бюджетом или безусловным growth mandate;
- `PORT-005` и `PORT-006` остаются `contain`;
- `PORT-007` остаётся `clarify` / clarification-only module candidate без material-build authorization;
- между текущими portfolio nodes не установлено обязательной hard runtime/code/data dependency;
- Arvectum OS остаётся каноническим источником Product Contracts/platform semantics, product repositories — implementation/status/domain semantics;
- AC-106 `P0…P3` hierarchy остаётся выше AC-306 portfolio ranking;
- unresolved profitability, market, legal/IP/data, customer-readiness и product-economics evidence переносится дальше как carry-forward, а не объявляется доказанным.

## 3. Закрытие M3

В соответствии с утверждённым AC-307 этап:

`M3 — Product/module-candidate portfolio governed as investments`

закрывается со статусом:

`Complete / PASS`.

Русская смысловая формулировка результата:

**портфель продуктов и кандидатов в повторно используемые модули ООО «Арвектум» имеет согласованные Company-level identity, accountability, investment/risk boundaries, reuse/dependency boundaries и priority discipline, достаточные для управления им как набором инвестиций, а не как списком репозиториев.**

## 4. Что закрытие M3 не означает

Закрытие M3 само по себе не доказывает и не создаёт:

- прибыльность продуктов или Компании;
- подтверждённый рыночный спрос, CAC/LTV, ROI или repeatable acquisition;
- готовность к production/customer deployment;
- юридическую чистоту всех product IP/data rights;
- бюджет, расход, цену, SLA, customer/vendor commitment;
- approved reusable production module;
- Stable Product Contract или Active Platform Capability Arvectum OS;
- обязательную shared runtime/data infrastructure между продуктами.

Для конкретных material effects продолжают действовать соответствующие evidence и authority gates, включая применимые `ROD-*`.

## 5. Следующий этап

Следующий канонический этап по уже утверждённой roadmap chain:

`M4 — Owner control and reference-implementation observability established`.

Следующее каноническое действие:

`AC-401 — Company work/obligation register model`.

По-русски: **модель реестра работ и обязательств Компании**.

Это решение разрешает только каноническую публикацию AC-307, синхронизацию `PORTFOLIO.md`, `ROADMAP.md`, реестра источников/навигации и перевод current action на AC-401. Оно не является выполнением AC-401.

## 6. Границы решения

Решение не создаёт новых юридических полномочий, не утверждает конкретный расход, найм, договор, клиентское обязательство, Product Contract Arvectum OS, shared module, production deployment или изменение product implementation roadmap.