# Решение собственника — утверждение AC-306

Статус: `Approved`
Дата: `2026-08-21`
Владелец решения: собственник ООО «Арвектум»
Репозиторий: `arvectum/arvectum-company`
Решение: `AC-306 — Portfolio prioritization by capital, economics and Owner attention`

## 1. Явное решение

Собственник явно утвердил AC-306 формулировкой:

> `AC-306 утверждаю`

Утверждение относится к точной проверенной редакции:

- proposal: `docs/portfolio/AC-306-PORTFOLIO-PRIORITIZATION-CAPITAL-ECONOMICS-OWNER-ATTENTION.md`;
- proposal status: `Proposed 0.9.0`;
- immutable proposal blob SHA: `d254c6441baca5f22828648ecfa701d04c8344b1`;
- cross-review: `docs/reviews/AC-306-PORTFOLIO-PRIORITIZATION-CROSS-REVIEW.md`;
- cross-review result: `10 of maximum 10`, `Complete / PASS for Owner approval`;
- immutable cross-review blob SHA: `329c87d6a63e08564e8b52362b8af02b159d7b74`.

Эти immutable blob SHA фиксируют именно те редакции, которые были представлены собственнику перед утверждением.

## 2. Утверждённый default portfolio order

Утверждается следующий default order конкуренции за discretionary product capital, engineering effort и Owner attention при отсутствии более высокого Company-level `P0` обязательства:

1. `A1 — PORT-002 Discount Parser` — finish / accept / stabilize / maintain;
2. `A2 — PORT-001 Arvectum Tender Agent` — bounded revenue / pilot / evidence work;
3. `B1 — PORT-003 Arvectum Proxy Launcher` — trigger-based investment, preservation of verified baseline;
4. `B2 — PORT-004 Creative Test Agent` — trigger-based pilot activation on real design-partner/customer evidence;
5. `C1 — PORT-007 Data Platform` — clarification-only, no material build;
6. `D1 — PORT-005 Tender Small-Volume Calculator` — contain / reference evidence;
7. `D2 — PORT-006 Doors Parser` — contain / support / reuse evidence.

Этот порядок является decision order, а не постоянной инженерной очередью и не меняет Company flagship.

## 3. Сохраняемая Company priority hierarchy

AC-306 подчинён ранее утверждённой AC-106 иерархии:

- `P0` — реальные обязательства, cash и material risk;
- `P1` — flagship market evidence + минимальная реальная operating model Arvectum Company;
- `P2` — product/OS work, прямо связанная с revenue, obligation, evidence или blocker removal;
- `P3` — speculative productization/module/platform expansion.

Portfolio band не даёт продукту права автоматически вытеснять `P0` или `P1` работу.

## 4. P0 override и re-evaluation rule

Реальный customer acceptance/support defect, material security/data/continuity issue или иное применимое обязательство может временно поднять конкретную работу в `P0` независимо от product band.

Такой override:

- относится к конкретному obligation/risk slice;
- не меняет portfolio disposition автоматически;
- после закрытия обязательства возвращает node к исходному treatment, если отдельное решение не установило иное.

Band B trigger означает основание для re-evaluation bounded slice, а не self-executing promotion.

## 5. Capital и Owner-attention boundary

AC-306 утверждает Owner attention как ограниченный management capital и требует для material product work явно показывать:

1. why now;
2. exact bounded outcome;
3. required Owner action;
4. what can proceed without Owner;
5. stop condition;
6. next decision enabled by evidence.

Не допускается систематически тратить Owner attention на известные недоступные physical/external gates, speculative polish, raw test-output review или параллельное feature expansion без business reason.

## 6. Authority boundary

Утверждение AC-306 является Reserved Owner Decision в части portfolio/capital priority (`ROD-02`, `ROD-04`). Оно не создаёт автоматического разрешения на конкретный material расход или внешний commitment.

Каждый конкретный material spend, customer/vendor commitment, price/SLA, legal/IP/data exception, dependency exception или Company↔Product↔Arvectum OS commitment продолжает требовать применимый evidence и authority path, включая соответствующие `ROD-*` gates.

## 7. Сохранённые границы

AC-306 не:

- меняет flagship `«ИИ-компания под ключ»`;
- создаёт budget или numeric spend threshold;
- утверждает выдуманные revenue, margin, ROI, CAC/LTV или Owner-hour estimates;
- отменяет AC-301…AC-305;
- меняет product implementation roadmap автоматически;
- создаёт shared module/service/runtime или новую Product Contract dependency;
- переводит `PORT-007` из clarification-only в build;
- выводит `PORT-005/006` из contain;
- разрешает mass pilot, SaaS expansion или autonomous consequential action по PORT-001;
- снимает legal/IP/physical-host stop-gates PORT-003;
- подменяет customer evidence технической готовностью PORT-004.

## 8. Следующее действие

После публикации AC-306 как `Approved 1.0.0` и синхронизации `PORTFOLIO.md` и `ROADMAP.md` следующим каноническим действием становится:

`AC-307 — Итоговая проверка управления портфелем и закрытие M3`.
