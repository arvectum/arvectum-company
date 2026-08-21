#!/usr/bin/env python3
"""OS-neutral WF-M5-001 case/evidence helper for AC-504.

Records references and governed state only. It does not send customer messages,
deploy software, approve commitments, or create Organizational Authority.
"""
from __future__ import annotations
import argparse, copy, json, re, secrets, sys
from datetime import datetime, timezone
from pathlib import Path

SCHEMA="wf-m5-001.case.v1"; WF="WF-M5-001"; WF_VER="1.0.0"
WF_BLOB="9b06e02a6d9afa8b6b4533d3a9f71690518c3ce1"
PROPOSAL_BLOB="b1df71839422e509cbfa76faec31bf788ca9842d"
OS_DECISION_BLOB="8984d4c094da87a2c9d201fd9cffcd617c641f8f"
PRODUCT="PORT-002"; REPO="arvectum/discount-parser"
BASELINE="a8c1b29702a8ce40bd30b5d972ac2541367900e1"
STATES={f"W{i}" for i in range(12)}; CLASSES={f"CL-{i}" for i in range(1,8)}
POSITIONS={f"POS-00{i}" for i in range(1,7)}; AMS={"AM-0","AM-1","AM-2"}
REF_TYPES={"feedback","environment","handoff","validation","issue","pr","commit","test","build","release_candidate","artifact","run","control"}
BLOCK_KINDS={"blocked","unknown","stale","uncertain"}
ALLOWED={"W0":{"W1","W11"},"W1":{"W2","W11"},"W2":{"W3","W11"},"W3":{"W4","W11"},
"W4":{"W5","W11"},"W5":{"W6","W11"},"W6":{"W5","W7","W11"},"W7":{"W8","W9","W11"},
"W8":{"W9","W10","W11"},"W9":{"W2","W4","W11"},"W10":set(),"W11":set()}
CASE_RE=re.compile(r"^WF-M5-001-\d{8}-[A-F0-9]{8}$")
SECRETS=[re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
         re.compile(r"(?i)\b(password|passwd|token|secret|api[-_ ]?key)\s*[:=]\s*\S+"),
         re.compile(r"\b\d{6,12}:[A-Za-z0-9_-]{20,}\b")]

class CaseError(ValueError): pass

def now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")

def iso(v):
    try:
        d=datetime.fromisoformat(v[:-1]+"+00:00" if v.endswith("Z") else v)
    except ValueError as e: raise CaseError(f"invalid ISO-8601 timestamp: {v}") from e
    if d.tzinfo is None: raise CaseError("timestamp must include timezone or Z")
    return d.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")

def safe(v, field, limit=600):
    if v is None: return None
    if not isinstance(v,str) or len(v)>limit or "\x00" in v: raise CaseError(f"{field}: invalid/too long")
    for p in SECRETS:
        if p.search(v): raise CaseError(f"{field}: possible DC-3 secret; store only a protected reference")
    return v.strip()

def ref(v, field="reference"):
    v=safe(v,field,500)
    if not v or "\n" in v or "\r" in v: raise CaseError(f"{field}: single-line reference required")
    return v

def cid():
    return f"{WF}-{datetime.now(timezone.utc):%Y%m%d}-{secrets.token_hex(4).upper()}"

def path(store, case_id):
    if not CASE_RE.match(case_id): raise CaseError("case_id must match WF-M5-001-YYYYMMDD-XXXXXXXX")
    return store/f"{case_id}.json"

def scan(x, p="$"):
    if isinstance(x,dict):
        for k,v in x.items(): scan(v,f"{p}.{k}")
    elif isinstance(x,list):
        for i,v in enumerate(x): scan(v,f"{p}[{i}]")
    elif isinstance(x,str):
        for q in SECRETS:
            if q.search(x): raise CaseError(f"{p}: possible DC-3 secret detected")

def validate(c):
    if c.get("schema_version")!=SCHEMA or not CASE_RE.match(c.get("case_id","")): raise CaseError("invalid schema/case_id")
    w=c.get("workflow",{})
    expected={"id":WF,"version":WF_VER,"approved_publication_blob":WF_BLOB,
              "reviewed_proposal_blob":PROPOSAL_BLOB,"os_reliance_decision_blob":OS_DECISION_BLOB,
              "os_reliance":"NO-ADDITIONAL-OS-RELIANCE"}
    if any(w.get(k)!=v for k,v in expected.items()): raise CaseError("workflow evidence pins changed")
    if c.get("state") not in STATES or c.get("product",{}).get("repository")!=REPO: raise CaseError("invalid state/product boundary")
    if c.get("classification") is not None and c["classification"] not in CLASSES: raise CaseError("invalid classification")
    scan(c)
    s=c["state"]
    if s in {"W3","W4","W5","W6","W7","W8","W9","W10"} and not c["classification"]: raise CaseError("classified-or-later state lacks classification")
    if s in {"W4","W5","W6","W7","W8","W9"} and c["classification"]!="CL-1": raise CaseError("normal technical correction path requires CL-1")
    if s in {"W7","W8","W9","W10"} and c["verification"]["result"]!="passed": raise CaseError("candidate/customer path requires passed verification")
    if s in {"W8","W9","W10"} and not c["customer_validation"]["handoff_ref"]: raise CaseError("customer path requires handoff reference")
    if s=="W10" and not c["customer_validation"]["validation_ref"]: raise CaseError("W10 requires explicit validation reference")
    prev=None
    for i,e in enumerate(c["transitions"]):
        if e["from"]!=prev or e["to"] not in STATES or e["authority_mode"] not in AMS or e["actor_position"] not in POSITIONS:
            raise CaseError(f"invalid transition history at {i}")
        prev=e["to"]
    if prev!=s: raise CaseError("current state differs from transition history")
    return c

def load(store, case_id):
    p=path(store,case_id)
    if not p.exists(): raise CaseError(f"case not found: {p}")
    return validate(json.loads(p.read_text(encoding="utf-8")))

def save(store,c):
    validate(c); store.mkdir(parents=True,exist_ok=True); p=path(store,c["case_id"])
    t=p.with_suffix(".json.tmp"); t.write_text(json.dumps(c,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); t.replace(p); return p

def new_case(source_ref,received_at,principal_ref,case_id=None,baseline=BASELINE):
    case_id=case_id or cid()
    if not CASE_RE.match(case_id): raise CaseError("invalid case_id")
    source_ref=ref(source_ref,"source_ref"); principal_ref=ref(principal_ref,"principal_ref"); received_at=iso(received_at); created=now()
    c={"schema_version":SCHEMA,"case_id":case_id,
       "workflow":{"id":WF,"version":WF_VER,"approved_publication_blob":WF_BLOB,"reviewed_proposal_blob":PROPOSAL_BLOB,
                   "os_reliance_decision_blob":OS_DECISION_BLOB,"os_reliance":"NO-ADDITIONAL-OS-RELIANCE"},
       "product":{"portfolio_id":PRODUCT,"repository":REPO,"baseline_ref":ref(baseline,"product_baseline")},
       "state":"W0","classification":None,"classification_history":[],
       "intake":{"received_at":received_at,"affected_version":None,"environment_ref":None,"sanitized_summary":None,
                 "scope_basis_ref":None,"unknowns":[],"data_boundary_assessed":False},
       "technical_scope":{"summary":None,"exclusions":[],"known_limitations":None},
       "refs":[{"type":"feedback","ref":source_ref,"data_class":"DC-2","at":received_at}],
       "verification":{"result":"not_started","at":None},
       "customer_validation":{"status":"not_started","handoff_ref":None,"validation_ref":None},
       "blocker":None,"measurements":{"owner_interventions":0,"owner_minutes":None,"rework_count":0},
       "transitions":[{"from":None,"to":"W0","at":created,"actor_position":"POS-002","principal_ref":principal_ref,
                       "authority_mode":"AM-0","reason":"feedback intake opened","evidence_refs":[source_ref]}],
       "created_at":created,"updated_at":created}
    return validate(c)

def add_ref(c,t,v,data_class="DC-1"):
    if t not in REF_TYPES: raise CaseError(f"unsupported ref type: {t}")
    if data_class not in {"DC-0","DC-1","DC-2"}: raise CaseError("DC-3 payload/reference storage is prohibited here")
    c["refs"].append({"type":t,"ref":ref(v), "data_class":data_class,"at":now()})

def refs(c,t): return [x["ref"] for x in c["refs"] if x["type"]==t]

def gate(c,target,actor,am,evidence):
    if target in {"W1","W2","W3","W4","W8","W10"} and actor!="POS-002": raise CaseError(f"{target} requires POS-002")
    if target in {"W5","W6","W7"} and actor!="POS-004": raise CaseError(f"{target} requires POS-004")
    if target=="W1" and (not refs(c,"feedback") or not c["intake"]["data_boundary_assessed"]): raise CaseError("W1 intake/data gate failed")
    if target=="W2" and not c["intake"]["sanitized_summary"]: raise CaseError("W2 requires sanitized summary")
    if target=="W3" and (not c["classification"] or am!="AM-2"): raise CaseError("W3 requires attributable POS-002 AM-2 classification")
    if target=="W4":
        if c["classification"]!="CL-1" or not c["intake"]["scope_basis_ref"] or not c["technical_scope"]["summary"] or c["blocker"]:
            raise CaseError("W4 correction-admission gate failed")
    if target=="W7":
        if c["verification"]["result"]!="passed" or not refs(c,"test") or not any(refs(c,x) for x in ("commit","pr","build","release_candidate","artifact")) or not c["technical_scope"]["known_limitations"]:
            raise CaseError("W7 verification/provenance gate failed")
    if target=="W8" and not c["customer_validation"]["handoff_ref"]: raise CaseError("W8 requires handoff reference")
    if target=="W9" and not evidence: raise CaseError("W9 requires disproving evidence")
    if target=="W10" and (c["customer_validation"]["status"] not in {"accepted","no_correction_required"} or not c["customer_validation"]["validation_ref"]):
        raise CaseError("W10 requires explicit customer result")
    if target=="W11" and not c["blocker"]: raise CaseError("W11 requires explicit block/escalation reason")

def move(c,target,actor,principal,am,reason,evidence=()):
    cur=c["state"]
    if target not in ALLOWED[cur]: raise CaseError(f"transition {cur}->{target} not allowed")
    if actor not in POSITIONS or am not in AMS: raise CaseError("invalid actor/authority; AM-3/AM-4 not allowed")
    ev=[ref(x,"evidence_ref") for x in evidence]; gate(c,target,actor,am,ev); ts=now()
    c["transitions"].append({"from":cur,"to":target,"at":ts,"actor_position":actor,"principal_ref":ref(principal,"principal_ref"),
                             "authority_mode":am,"reason":safe(reason,"reason",500),"evidence_refs":ev})
    c["state"]=target; c["updated_at"]=ts

def intake(c,principal,summary,affected=None,environment=None,scope_basis=None,unknowns=(),ready=False):
    if c["state"]!="W0": raise CaseError("intake requires W0")
    c["intake"].update({"sanitized_summary":safe(summary,"summary",500),"affected_version":safe(affected,"affected_version",120),
                        "environment_ref":ref(environment) if environment else None,"scope_basis_ref":ref(scope_basis) if scope_basis else None,
                        "unknowns":[safe(x,"unknown",200) for x in unknowns],"data_boundary_assessed":True})
    if environment: add_ref(c,"environment",environment,"DC-2")
    move(c,"W1","POS-002",principal,"AM-0","intake normalized; data boundary assessed",refs(c,"feedback"))
    if ready: move(c,"W2","POS-002",principal,"AM-0","classification evidence reviewed; unknowns explicit",refs(c,"feedback"))

def classify(c,principal,cl,summary):
    if cl not in CLASSES: raise CaseError("invalid classification")
    if c["state"]=="W1": move(c,"W2","POS-002",principal,"AM-0","classification evidence reviewed",refs(c,"feedback"))
    if c["state"]!="W2": raise CaseError("classify requires W1/W2")
    if cl=="CL-1" and not c["intake"]["scope_basis_ref"]: raise CaseError("CL-1 requires accepted-scope basis reference")
    c["classification"]=cl; c["classification_history"].append({"classification":cl,"summary":safe(summary,"classification_summary",500),
        "at":now(),"actor_position":"POS-002","principal_ref":ref(principal,"principal_ref"),"authority_mode":"AM-2"})
    move(c,"W3","POS-002",principal,"AM-2",f"classified as {cl}",refs(c,"feedback"))

def admit(c,principal,scope,exclusions=()):
    if c["state"]!="W3": raise CaseError("admit requires W3")
    c["technical_scope"]["summary"]=safe(scope,"technical_scope",600)
    c["technical_scope"]["exclusions"]=[safe(x,"exclusion",250) for x in exclusions]
    move(c,"W4","POS-002",principal,"AM-2","bounded in-scope correction admitted",[c["intake"]["scope_basis_ref"]])

def start(c,principal):
    if c["state"]!="W4": raise CaseError("start requires W4")
    move(c,"W5","POS-004",principal,"AM-1","bounded technical execution started")

def verify(c,principal,test_refs,candidate_refs,limitations):
    if c["state"]!="W5": raise CaseError("verify requires W5")
    move(c,"W6","POS-004",principal,"AM-1","candidate entered internal verification")
    for x in test_refs: add_ref(c,"test",x)
    for t,v in candidate_refs: add_ref(c,t,v)
    c["technical_scope"]["known_limitations"]=safe(limitations,"known_limitations",500)
    c["verification"]={"result":"passed","at":now()}
    move(c,"W7","POS-004",principal,"AM-2","bounded candidate verification passed",[x["ref"] for x in c["refs"] if x["type"] in {"test","commit","pr","build","release_candidate","artifact"}])

def handoff(c,principal,handoff_ref):
    if c["state"]!="W7": raise CaseError("handoff requires W7")
    add_ref(c,"handoff",handoff_ref,"DC-2"); c["customer_validation"].update({"status":"pending","handoff_ref":ref(handoff_ref)})
    move(c,"W8","POS-002",principal,"AM-1","customer handoff recorded; explicit result pending",[handoff_ref])

def customer_result(c,principal,result,validation_ref,target=None):
    if c["state"]!="W8": raise CaseError("customer-result requires W8")
    add_ref(c,"validation",validation_ref,"DC-2"); c["customer_validation"]["validation_ref"]=ref(validation_ref)
    if result in {"accepted","no_correction_required"}:
        c["customer_validation"]["status"]=result; move(c,"W10","POS-002",principal,"AM-2",f"explicit customer result: {result}",[validation_ref])
    elif result=="still_failing":
        c["customer_validation"]["status"]=result; c["measurements"]["rework_count"]+=1
        move(c,"W9","POS-002",principal,"AM-2","customer evidence requires rework",[validation_ref])
    else: block(c,principal,"unknown" if result=="insufficient_evidence" else "blocked",f"customer result: {result}",target or "POS-002/review",validation_ref)

def block(c,principal,kind,reason,target,evidence=None):
    if c["state"] in {"W10","W11"} or kind not in BLOCK_KINDS: raise CaseError("invalid block action")
    c["blocker"]={"kind":kind,"reason":safe(reason,"block_reason",500),"target":safe(target,"block_target",250),"at":now()}
    move(c,"W11","POS-002",principal,"AM-0",f"{kind}: {reason}",[evidence] if evidence else [])

def public_projection(c): return copy.deepcopy(validate(c))

def candidate_pairs(values):
    out=[]
    for x in values:
        if "=" not in x: raise CaseError("candidate refs use TYPE=REF")
        t,v=x.split("=",1)
        if t not in {"commit","pr","build","release_candidate","artifact"}: raise CaseError("unsupported candidate ref type")
        out.append((t,v))
    return out

def parser():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("--store",type=Path,default=Path(".local/wf-m5-001"))
    s=p.add_subparsers(dest="cmd",required=True)
    q=s.add_parser("new"); q.add_argument("--source-ref",required=True); q.add_argument("--received-at",required=True); q.add_argument("--principal-ref",required=True); q.add_argument("--case-id"); q.add_argument("--product-baseline",default=BASELINE)
    q=s.add_parser("intake"); q.add_argument("case_id"); q.add_argument("--principal-ref",required=True); q.add_argument("--summary",required=True); q.add_argument("--affected-version"); q.add_argument("--environment-ref"); q.add_argument("--scope-basis-ref"); q.add_argument("--unknown",action="append",default=[]); q.add_argument("--classification-ready",action="store_true")
    q=s.add_parser("classify"); q.add_argument("case_id"); q.add_argument("--principal-ref",required=True); q.add_argument("--class",dest="cl",choices=sorted(CLASSES),required=True); q.add_argument("--summary",required=True)
    q=s.add_parser("admit"); q.add_argument("case_id"); q.add_argument("--principal-ref",required=True); q.add_argument("--scope",required=True); q.add_argument("--exclude",action="append",default=[])
    q=s.add_parser("start"); q.add_argument("case_id"); q.add_argument("--principal-ref",required=True)
    q=s.add_parser("verify"); q.add_argument("case_id"); q.add_argument("--principal-ref",required=True); q.add_argument("--test-ref",action="append",default=[],required=True); q.add_argument("--candidate-ref",action="append",default=[]); q.add_argument("--known-limitations",required=True)
    q=s.add_parser("handoff"); q.add_argument("case_id"); q.add_argument("--principal-ref",required=True); q.add_argument("--handoff-ref",required=True)
    q=s.add_parser("customer-result"); q.add_argument("case_id"); q.add_argument("--principal-ref",required=True); q.add_argument("--result",choices=["accepted","no_correction_required","still_failing","changed_requirement","insufficient_evidence","stopped"],required=True); q.add_argument("--validation-ref",required=True); q.add_argument("--target")
    q=s.add_parser("block"); q.add_argument("case_id"); q.add_argument("--principal-ref",required=True); q.add_argument("--kind",choices=sorted(BLOCK_KINDS),required=True); q.add_argument("--reason",required=True); q.add_argument("--target",required=True); q.add_argument("--evidence-ref")
    q=s.add_parser("link"); q.add_argument("case_id"); q.add_argument("--type",choices=sorted(REF_TYPES),required=True); q.add_argument("--ref",required=True); q.add_argument("--data-class",choices=["DC-0","DC-1","DC-2"],default="DC-1")
    q=s.add_parser("measure-owner"); q.add_argument("case_id"); q.add_argument("--interventions",type=int,required=True); q.add_argument("--minutes",type=float)
    q=s.add_parser("show"); q.add_argument("case_id")
    q=s.add_parser("validate"); q.add_argument("case_id")
    q=s.add_parser("export-public"); q.add_argument("case_id"); q.add_argument("--out",type=Path)
    return p

def main(argv=None):
    a=parser().parse_args(argv); store=a.store
    try:
        if a.cmd=="new":
            c=new_case(a.source_ref,a.received_at,a.principal_ref,a.case_id,a.product_baseline); p=save(store,c)
        else:
            c=load(store,a.case_id)
            if a.cmd=="intake": intake(c,a.principal_ref,a.summary,a.affected_version,a.environment_ref,a.scope_basis_ref,a.unknown,a.classification_ready)
            elif a.cmd=="classify": classify(c,a.principal_ref,a.cl,a.summary)
            elif a.cmd=="admit": admit(c,a.principal_ref,a.scope,a.exclude)
            elif a.cmd=="start": start(c,a.principal_ref)
            elif a.cmd=="verify": verify(c,a.principal_ref,a.test_ref,candidate_pairs(a.candidate_ref),a.known_limitations)
            elif a.cmd=="handoff": handoff(c,a.principal_ref,a.handoff_ref)
            elif a.cmd=="customer-result": customer_result(c,a.principal_ref,a.result,a.validation_ref,a.target)
            elif a.cmd=="block": block(c,a.principal_ref,a.kind,a.reason,a.target,a.evidence_ref)
            elif a.cmd=="link": add_ref(c,a.type,a.ref,a.data_class)
            elif a.cmd=="measure-owner":
                if a.interventions<0 or (a.minutes is not None and a.minutes<0): raise CaseError("measurements cannot be negative")
                c["measurements"].update({"owner_interventions":a.interventions,"owner_minutes":a.minutes}); c["updated_at"]=now()
            elif a.cmd=="show": print(json.dumps(c,ensure_ascii=False,indent=2)); return 0
            elif a.cmd=="validate": validate(c); print(json.dumps({"case_id":c["case_id"],"state":c["state"],"valid":True})); return 0
            elif a.cmd=="export-public":
                text=json.dumps(public_projection(c),ensure_ascii=False,indent=2)+"\n"
                if a.out: a.out.parent.mkdir(parents=True,exist_ok=True); a.out.write_text(text,encoding="utf-8"); print(a.out)
                else: print(text,end="")
                return 0
            p=save(store,c)
        print(json.dumps({"case_id":c["case_id"],"state":c["state"],"path":str(p)},ensure_ascii=False)); return 0
    except (CaseError,OSError,json.JSONDecodeError) as e:
        print(f"ERROR: {e}",file=sys.stderr); return 2

if __name__=="__main__": raise SystemExit(main())
