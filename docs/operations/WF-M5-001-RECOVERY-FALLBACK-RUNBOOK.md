# WF-M5-001 — Recovery, Uncertain-Outcome and Manual Fallback Runbook

Статус: `Active`
Версия: `1.0.0`
Создано: `2026-08-22`
Roadmap: `AC-506 — Incident, uncertain-outcome, recovery and fallback drill`
Workflow: `WF-M5-001 / 1.0.0`
Depends on: AC-207 continuity baseline `1.0.0`; AC-502 workflow contract `1.0.0`; AC-503 OS reliance decision `1.0.0`; AC-504 bounded implementation; AC-505 real-operation evidence

## 1. Purpose

Этот runbook определяет минимальный fail-closed recovery/fallback path для `WF-M5-001` после `W11 — Reclassified / Escalated / Blocked` и для случаев, когда helper/runtime недоступен или внешний outcome неизвестен.

Основной принцип:

```text
recovery ≠ rewrite
new evidence ≠ automatic reclassification
runtime replacement ≠ authority transfer
manual fallback ≠ weaker controls
uncertain external outcome ≠ assumed success
```

`W11` predecessor остаётся исторически неизменным. Возврат evidence открывает **successor case**, а не переписывает старый blocked case.

## 2. Why successor recovery

AC-504 намеренно сделал `W11` terminal для первой bounded implementation. AC-506 добавляет recovery без ослабления этого свойства.

Вместо `W11 → W2` внутри одного файла используется:

`blocked predecessor W11 → new attributable evidence → new linked case W0/W1/W2 → fresh POS-002 classification`.

Это сохраняет:

- исходную chronology;
- старую classification и blocker как immutable evidence;
- отдельный current product baseline;
- необходимость нового human-attributable classification;
- отсутствие скрытого технического admission.

## 3. Recovery helper

Implementation:

`tools/wf_m5_001_recovery.py`.

Он использует существующий `tools/wf_m5_001_case.py` и Python standard library only.

Helper допускает recovery только если:

1. predecessor существует и валиден;
2. predecessor находится в `W11` и имеет explicit blocker;
3. присутствует **новый** evidence reference, отличный от исходного feedback ref;
4. оператор явно задаёт current exact product baseline;
5. новый successor case id не коллидирует с существующим файлом;
6. новое evidence проходит existing secret/data guardrails.

Helper не выполняет classification, admission, customer messaging, deployment или acceptance.

## 4. Successor creation

Пример:

```bash
python tools/wf_m5_001_recovery.py \
  WF-M5-001-20260821-AC505001 \
  --source-ref protected://customer-feedback/new-evidence \
  --received-at 2026-08-22T06:00:00Z \
  --principal-ref principal/owner \
  --product-baseline <exact-current-product-commit> \
  --summary "sanitized meaning of new attributable evidence" \
  --unknown "reproduction result pending" \
  --classification-ready
```

Successor получает safe control refs:

- `predecessor-case:<case-id>`;
- `predecessor-blocker:<kind>`.

Predecessor file не изменяется.

## 5. Reclassification boundary

Даже если successor дошёл до `W2`, recovery helper **не** присваивает новый `CL-*`.

Следующий material gate остаётся:

`POS-002 human Principal / AM-2 classification`.

Если evidence всё ещё недостаточен, новый case может снова стать `CL-3` и fail closed.

Если evidence подтверждает `CL-1`, обычный AC-502/AC-504 path требует accepted-scope basis и отдельный bounded W4 admission прежде, чем POS-004 начнёт техническую работу.

## 6. Uncertain external outcome

Если после consequential external step неизвестно, произошёл ли эффект, запрещено повторять действие как будто первый attempt точно не произошёл.

Минимальный порядок:

1. зафиксировать outcome как `uncertain`;
2. не объявлять success/acceptance;
3. не повторять non-idempotent consequential effect без authoritative reconciliation;
4. получить authoritative source evidence;
5. затем либо создать successor/recovery case, либо продолжить через применимый approved path.

Для customer acceptance silence никогда не является authoritative confirmation.

## 7. Incident boundary

AC-506 drill может моделировать incident-like trigger, но это не создаёт реальный `INC-*` record автоматически.

Если evidence содержит security/data/material-risk признаки:

- raw suspected secret/restricted payload не помещается в public case;
- обычный technical path не форсируется;
- case классифицируется/эскалируется по AC-502/AC-403, включая `CL-6`/POS-006 where applicable;
- actual `INC-*` создаётся только если факты удовлетворяют approved incident semantics, а не потому что drill использовал incident scenario.

## 8. Helper/runtime unavailable — manual fallback

Если Python helper недоступен:

1. использовать private/non-git copy `docs/operations/WF-M5-001-CASE-TEMPLATE.json`;
2. восстановить minimum continuity packet из canonical Company/product refs и protected customer-source pointers;
3. сохранить Position/Principal/AM attribution и state history;
4. не копировать raw DC-2/DC-3 payload в public repo;
5. отметить отсутствующие данные как unknown/stale/uncertain;
6. не продолжать consequential path, если gate нельзя доказать;
7. после восстановления helper не переписывать историю — reconcile manual file against schema or open a linked successor case.

Manual fallback не получает дополнительную authority.

## 9. Runtime/process replacement drill

Для bounded helper достаточным техническим runtime-replacement evidence является запуск тех же deterministic tests в fresh checkout/process without prior model/session state.

Это доказывает только portability механики WF-M5-001. Оно **не** доказывает Company-wide AI-runtime replacement, POS-004 Principal replacement, disaster recovery или Owner-independent continuity.

## 10. Current real W11 application

Current real case:

`WF-M5-001-20260821-AC505001`.

Current state:

`CL-3 → W11 / unknown`.

Until new attributable evidence arrives:

- predecessor remains closed/unchanged;
- no POS-004 correction is admitted;
- no customer acceptance is inferred;
- no synthetic successor is created as real operational evidence.

AC-506 may use a synthetic temporary fixture only for the deliberate recovery drill, clearly labelled as test evidence rather than customer evidence.

## 11. Recovery acceptance checks

A bounded AC-506 recovery drill passes when evidence shows:

1. W11 predecessor cannot be silently reopened or overwritten;
2. successor requires new evidence;
3. exact product baseline is explicit;
4. successor has predecessor control linkage;
5. recovery does not auto-classify;
6. non-CL-1 cannot enter W4;
7. likely secret material remains rejected;
8. duplicate successor id fails closed;
9. manual fallback preserves minimum continuity semantics;
10. real W11 case remains honestly blocked until authoritative evidence changes.

## 12. Non-effects

This runbook does not create:

- customer promises or automatic follow-up sending;
- autonomous production deployment;
- new Position/Assignment/access grant;
- AM-3/AM-4;
- risk/incident acceptance;
- Arvectum OS reliance or Product Contract change;
- proof of full Company disaster recovery;
- permission to call synthetic drill evidence a real customer outcome.
