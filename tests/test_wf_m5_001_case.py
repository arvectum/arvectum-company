import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1] / "tools" / "wf_m5_001_case.py"
spec = importlib.util.spec_from_file_location("wf", MODULE)
wf = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(wf)

OWNER="principal/owner"; ENGINEER="principal/ai-engineering"
CID="WF-M5-001-20260821-ABCDEF12"

class Tests(unittest.TestCase):
    def new(self):
        return wf.new_case("protected://customer-feedback/001","2026-08-21T18:00:00Z",OWNER,CID)

    def technical(self,c):
        wf.intake(c,OWNER,"Reproducible mismatch inside accepted behavior.","0.1.11",
                  "protected://customer-environment/001","product://accepted-scope/001",[],True)
        wf.classify(c,OWNER,"CL-1","In-scope defect; no new commitment.")
        wf.admit(c,OWNER,"Correct reported behavior only.",["No redesign","No automatic customer delivery"])
        wf.start(c,ENGINEER)

    def test_happy_path_needs_explicit_customer_result(self):
        c=self.new(); self.technical(c)
        wf.verify(c,ENGINEER,["product://tests/case-001"],[("commit","git://discount-parser/example")],"none known")
        self.assertEqual(c["state"],"W7")
        wf.handoff(c,OWNER,"protected://customer-handoff/001")
        self.assertEqual(c["state"],"W8")
        wf.customer_result(c,OWNER,"accepted","protected://customer-validation/001")
        self.assertEqual(c["state"],"W10"); wf.validate(c)

    def test_new_scope_cannot_be_admitted_as_correction(self):
        c=self.new()
        wf.intake(c,OWNER,"Request exceeds accepted scope.","0.1.11",None,None,[],True)
        wf.classify(c,OWNER,"CL-4","Change/new scope.")
        with self.assertRaises(wf.CaseError): wf.admit(c,OWNER,"Build feature.",[])

    def test_candidate_ready_fails_without_test_and_provenance(self):
        c=self.new(); self.technical(c)
        with self.assertRaises(wf.CaseError): wf.verify(c,ENGINEER,[],[],"none known")

    def test_secret_like_material_rejected(self):
        with self.assertRaises(wf.CaseError):
            wf.new_case("protected://feedback/token=supersecretvalue","2026-08-21T18:00:00Z",OWNER,CID)

    def test_unknown_block_is_explicit(self):
        c=self.new()
        wf.intake(c,OWNER,"Insufficient evidence.",None,None,None,["affected build unknown"],False)
        wf.block(c,OWNER,"unknown","Reproduction evidence missing.","POS-002/customer-clarification")
        self.assertEqual(c["state"],"W11"); self.assertEqual(c["blocker"]["kind"],"unknown"); wf.validate(c)

    def test_acceptance_cannot_close_without_validation_ref(self):
        c=self.new(); self.technical(c)
        wf.verify(c,ENGINEER,["product://tests/case-001"],[("pr","git://discount-parser/pull/999")],"none known")
        wf.handoff(c,OWNER,"protected://customer-handoff/001")
        c["customer_validation"]["status"]="accepted"
        with self.assertRaises(wf.CaseError):
            wf.move(c,"W10","POS-002",OWNER,"AM-2","attempt closure",[])

    def test_round_trip_store(self):
        c=self.new()
        with tempfile.TemporaryDirectory() as d:
            p=wf.save(Path(d),c); loaded=wf.load(Path(d),CID)
            self.assertTrue(p.exists()); self.assertEqual(loaded["workflow"]["approved_publication_blob"],wf.WF_BLOB)

if __name__=="__main__": unittest.main()
