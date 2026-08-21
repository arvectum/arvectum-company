# AC-301 — Перекрёстная проверка идентичности, границ и владения портфелем

Статус: `Complete / PASS for Owner approval`
Дата проверки: `2026-08-21`
Итераций выполнено: `10 of maximum 10`
Результат: `PASS — семь текущих существенных узлов получили однозначные Company-level identities, repository locators отделены от product identity и legal/IP ownership, Company/Product/Arvectum OS boundaries сохранены, потенциальные дубли не объединены молча, каждому узлу присвоен bounded disposition без подмены инвестиционных решений AC-303/AC-306, а AC-302 остаётся следующим действием`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-301 — Portfolio product/node identity and ownership reconciliation`
Проверенный документ: `docs/portfolio/AC-301-PORTFOLIO-IDENTITY-BOUNDARY-OWNERSHIP-RECONCILIATION.md`
Проверенная редакция: `Proposed 0.9.0`
Проверенный git blob SHA: `146b5868a21c09cf20b633e309e587b7a631ad32`
Максимум итераций: `10`
Статус утверждения: `Pending explicit Owner approval of the exact reviewed proposal`

## 1. Назначение проверки

AC-301 — первая material portfolio-governance работа после закрытия M2. Проверка должна отвергнуть предложение, если оно хотя бы одним из способов:

- создаёт competing product identities;
- принимает repository name/account ownership за product/legal ownership;
- переносит product semantics в Company или OS;
- исправляет OS Product Contract из Company repository;
- молча объединяет Tender Agent/Tender App или parser-family repositories;
- объявляет модуль/платформу до AC-304;
- превращает `continue/contain/clarify` в бюджетное или stop/continue investment approval;
- создаёт новые Positions/Assignments вместо AC-302;
- делает неподтверждённый legal/IP claim.

## 2. Итерация 1 — product identity должна переживать repository rename/move

**Критика:** начальный портфель был repository-centric. Если Product Identity фактически равна GitHub path, последующий rename или split снова создаст identity ambiguity.

**Сверка:** proposal сохраняет стабильные `PORT-001…PORT-007` как Company-level identities и прямо устанавливает, что repository — locator реализации, а не сама product identity. Новая identity требуется только для реально нового самостоятельного объекта ответственности/инвестирования.

**Результат:** PASS.

## 3. Итерация 2 — organizational ownership нельзя превращать в legal/IP title

**Критика:** формулировка «владение продуктом» особенно рискованна для клиентских решений и кода, созданного до текущего corporate baseline. GitHub account, sponsorship и Company portfolio decision не доказывают исключительные права.

**Сверка:** proposal даёт узкое определение organizational ownership, отделяет его от legal title/IP/data/contract rights и отдельно запрещает вывод прав из repository placement или admin permission. Для Doors Parser эта оговорка повторена прямо в node boundary.

**Результат:** PASS.

## 4. Итерация 3 — Tender Agent: одна product line, но две authority scopes

**Критика:** P6.02 использует старый locator `arutyunoveth/ai-corporation` и собственную OS Product Identity `product/arvectum-tender-operator@<organization>`. Неправильная «сверка» могла либо создать второй Company product, либо переписать OS identity из Company artifact.

**Сверка:** proposal устанавливает `PORT-001 / Arvectum Tender Agent / arvectum/tender-agent` как Company/current product identity+locator, а P6.02 identity оставляет OS-scoped Product Contract identity для bounded interaction contour. Старый repository path классифицирован как stale OS contract locator, исправляемый через AC-305/OS governance с сохранением lineage.

**Результат:** PASS.

## 5. Итерация 4 — Tender Agent и Tender Small-Volume Calculator нельзя объединять по домену

**Критика:** оба repository работают с закупками; простая portfolio cleanup могла слить их без анализа semantics/history или, наоборот, узаконить бессрочное дублирование.

**Сверка:** proposal сохраняет две identities. `PORT-001` — продолжаемый самостоятельный procurement product. `PORT-005` переименован на Company-level в evidence-backed `Tender Small-Volume Calculator` и классифицирован как contained product experiment. `contain` запрещает молчаливое расширение, но не удаляет repository и не решает merge/retirement; AC-304/AC-306 остаются gate.

**Результат:** PASS.

## 6. Итерация 5 — parser/data similarity не создаёт Universal Parser

**Критика:** Discount Parser, Doors Parser и Data Platform легко представить как один «супер-парсер» и тем самым преждевременно создать module/platform commitment.

**Сверка:** proposal сохраняет три identities и три разных states: Discount Parser `continue`, Doors Parser `contain`, Data Platform `clarify`. Он прямо запрещает автоматическое создание `Universal Parser`, generic module или OS capability. Reuse остаётся AC-304/product evidence question.

**Результат:** PASS.

## 7. Итерация 6 — Creative Test Agent нельзя переименовать в Marketing Agent без product decision

**Критика:** историческое Company-language `Marketing Agent` шире текущей реализации и могло бы размыть product boundary.

**Сверка:** canonical identity закреплена как `Creative Test Agent` по repository/product evidence. `Marketing Agent` остаётся historical/future family concept и не admitted как отдельный node или alias, определяющий текущий scope.

**Результат:** PASS.

## 8. Итерация 7 — Data Platform: слово Platform не является architecture evidence

**Критика:** пустой/bootstrap repository с названием `Data Platform` может получить необоснованный shared-platform статус и начать конкурировать с Arvectum OS или поглощать parser semantics.

**Сверка:** proposal присваивает `clarify`, требует business problem, consumers, boundary, cost/risk/sovereignty и relationship evidence перед material development. Он прямо запрещает вывод Product/OS ownership из имени repository.

**Результат:** PASS.

## 9. Итерация 8 — disposition не должен подменять инвестиционный governance

**Критика:** `continue`, `contain` и `clarify` могут читаться как окончательные capital allocation или stop/continue decisions, хотя roadmap относит investment boundaries к AC-303 и prioritization к AC-306.

**Сверка:** proposal определяет dispositions как bounded identity/boundary states. `continue` не утверждает бюджет; `contain` сохраняет asset и запрещает scope creep без следующего решения; `clarify` требует определения перед material investment; ни один node не становится `retire candidate` без достаточных evidence. AC-303/AC-306 authority сохранена.

**Результат:** PASS.

## 10. Итерация 9 — organizational owner не равен accountable Position/Assignment

**Критика:** фраза «ООО «Арвектум» — product organizational owner» могла стать shortcut и либо оставить accountability навсегда на Owner human, либо неявно создать новые роли.

**Сверка:** proposal разделяет Company sponsorship/portfolio authority и future accountable Position. Никакой Position или Assignment не создаётся. AC-302 обязан привязать nodes к уже утверждённой M2 Position model либо отдельно обосновать изменение registry; GitHub access остаётся техническим доступом, а не authority.

**Результат:** PASS.

## 11. Итерация 10 — end-to-end integrity и handoff в AC-302

**Критика:** AC-301 должен закрыть именно identity/boundary ambiguity и не увести Phase 3 в AC-304/305/306 раньше accountability mapping.

**Сверка:** все семь nodes имеют основное имя, canonical repository/status source, type, organizational owner, Company↔Product↔OS boundary и disposition. Reconciliation register переносит оставшиеся материальные вопросы в правильные gates: Position accountability → AC-302; investment boundaries → AC-303; module classification → AC-304; OS dependencies/contracts → AC-305; capital/priority → AC-306. Proposal не закрывает ни один из этих пунктов заранее.

**Результат:** PASS.

## 12. Acceptance matrix

| Проверка | Результат |
|---|---|
| семь текущих material nodes имеют одну Company-level identity | PASS |
| `PORT-*` стабилен относительно rename/move repository | PASS |
| repository locator не равен Product Identity | PASS |
| GitHub ownership/admin не равен Organizational Authority | PASS |
| organizational ownership не заявлен как legal/IP title | PASS |
| product-specific semantics остаются в product repositories | PASS |
| Arvectum OS semantics/contracts остаются в OS governance | PASS |
| P6.02 stale repository locator выявлен | PASS |
| Company artifact не переписывает P6.02 | PASS |
| Tender Agent и Tender App не слиты молча | PASS |
| `Tender Small-Volume Calculator` основан на product evidence | PASS |
| parser/data family не превращена в Universal Parser | PASS |
| Creative Test Agent не превращён в Marketing Agent | PASS |
| Data Platform не получает platform status из имени | PASS |
| каждый node имеет disposition | PASS |
| dispositions не утверждают budget/ROI/priority | PASS |
| `contain` не означает automatic retirement | PASS |
| ни один node не объявлен retire candidate без evidence | PASS |
| AC-301 не создаёт Position/Assignment | PASS |
| AC-302 остаётся следующим каноническим шагом | PASS |
| AC-303/304/305/306 scopes сохранены | PASS |
| никакой новый Product Contract/OS capability не создан | PASS |
| никакой customer/SLA/production claim не создан | PASS |

## 13. Review-budget conclusion

Использованы все `10 of maximum 10` итераций, потому что AC-301 одновременно затрагивает семь product/initiative identities, старые repository aliases, два procurement nodes, три parser/data nodes и существующий OS Product Contract defect.

После десятой итерации material contradiction в заявленном scope не осталось. Оставшиеся вопросы требуют либо решения следующего roadmap gate, либо product/OS-specific governance, а не дополнительного переписывания AC-301.

## 14. Итог

`PASS — material consensus reached at 10 of maximum 10 iterations.`

AC-301 `Proposed 0.9.0`, точный проверенный blob `146b5868a21c09cf20b633e309e587b7a631ad32`, готов к **явному Owner approval**.

До такого approval действующий `docs/portfolio/PORTFOLIO.md` не заменяется, roadmap не переводится на AC-302, а proposal остаётся проверенным, но не binding Company portfolio baseline.