import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASE_MODULE = ROOT / "tools" / "wf_m5_001_case.py"
RECOVERY_MODULE = ROOT / "tools" / "wf_m5_001_recovery.py"

case_spec = importlib.util.spec_from_file_location("wf_case", CASE_MODULE)
wf = importlib.util.module_from_spec(case_spec)
assert case_spec.loader is not None
case_spec.loader.exec_module(wf)

recovery_spec = importlib.util.spec_from_file_location("wf_recovery", RECOVERY_MODULE)
recovery = importlib.util.module_from_spec(recovery_spec)
assert recovery_spec.loader is not None
recovery_spec.loader.exec_module(recovery)

OWNER = "principal/owner"
PRE = "WF-M5-001-20260822-AAAABBBB"
NEXT = "WF-M5-001-20260822-CCCCDDDD"
BASELINE = "a8c1b29702a8ce40bd30b5d972ac2541367900e1"


class RecoveryTests(unittest.TestCase):
    def blocked(self, store: Path):
        c = wf.new_case(
            "protected://customer-feedback/original",
            "2026-08-20T13:44:29Z",
            OWNER,
            PRE,
            BASELINE,
        )
        wf.intake(
            c,
            OWNER,
            "Customer symptom exists but reproduction evidence is incomplete.",
            None,
            None,
            None,
            ["affected build unknown"],
            True,
        )
        wf.classify(c, OWNER, "CL-3", "Evidence insufficient / not reproduced.")
        wf.block(
            c,
            OWNER,
            "unknown",
            "Current evidence is insufficient for technical admission.",
            "POS-002/customer-evidence follow-up",
        )
        wf.save(store, c)
        return c

    def test_w11_successor_preserves_predecessor(self):
        with tempfile.TemporaryDirectory() as d:
            store = Path(d)
            self.blocked(store)
            before = wf.path(store, PRE).read_text(encoding="utf-8")
            predecessor, successor = recovery.recover_successor(
                store,
                PRE,
                "protected://customer-feedback/new-evidence",
                "2026-08-22T05:30:00Z",
                OWNER,
                BASELINE,
                "New attributable evidence arrived; classification must be repeated.",
                unknowns=["reproduction result pending"],
                classification_ready=True,
                case_id=NEXT,
            )
            after = wf.path(store, PRE).read_text(encoding="utf-8")
            self.assertEqual(before, after)
            self.assertEqual(predecessor["state"], "W11")
            self.assertEqual(successor["state"], "W2")
            self.assertIsNone(successor["classification"])
            self.assertIsNone(successor["blocker"])
            self.assertEqual(successor["product"]["baseline_ref"], BASELINE)
            self.assertIn(f"predecessor-case:{PRE}", wf.refs(successor, "control"))
            wf.validate(successor)

    def test_recovery_requires_w11_predecessor(self):
        with tempfile.TemporaryDirectory() as d:
            store = Path(d)
            c = wf.new_case(
                "protected://customer-feedback/original",
                "2026-08-20T13:44:29Z",
                OWNER,
                PRE,
                BASELINE,
            )
            wf.save(store, c)
            with self.assertRaises(recovery.wf.CaseError):
                recovery.recover_successor(
                    store,
                    PRE,
                    "protected://customer-feedback/new-evidence",
                    "2026-08-22T05:30:00Z",
                    OWNER,
                    BASELINE,
                    "New evidence.",
                    case_id=NEXT,
                )

    def test_recovery_requires_new_evidence_ref(self):
        with tempfile.TemporaryDirectory() as d:
            store = Path(d)
            self.blocked(store)
            with self.assertRaises(recovery.wf.CaseError):
                recovery.recover_successor(
                    store,
                    PRE,
                    "protected://customer-feedback/original",
                    "2026-08-22T05:30:00Z",
                    OWNER,
                    BASELINE,
                    "No genuinely new evidence.",
                    case_id=NEXT,
                )

    def test_recovery_does_not_auto_classify_or_admit(self):
        with tempfile.TemporaryDirectory() as d:
            store = Path(d)
            self.blocked(store)
            _, successor = recovery.recover_successor(
                store,
                PRE,
                "protected://customer-feedback/new-evidence",
                "2026-08-22T05:30:00Z",
                OWNER,
                BASELINE,
                "New evidence requires review.",
                classification_ready=True,
                case_id=NEXT,
            )
            self.assertEqual(successor["state"], "W2")
            self.assertIsNone(successor["classification"])
            with self.assertRaises(wf.CaseError):
                wf.admit(successor, OWNER, "Attempt unsupported technical admission.", [])

    def test_recovered_cl3_still_fails_closed(self):
        with tempfile.TemporaryDirectory() as d:
            store = Path(d)
            self.blocked(store)
            _, successor = recovery.recover_successor(
                store,
                PRE,
                "protected://customer-feedback/new-evidence",
                "2026-08-22T05:30:00Z",
                OWNER,
                BASELINE,
                "New evidence is still insufficient.",
                classification_ready=True,
                case_id=NEXT,
            )
            wf.classify(successor, OWNER, "CL-3", "Still insufficient / not reproduced.")
            with self.assertRaises(wf.CaseError):
                wf.admit(successor, OWNER, "Do not admit non-CL-1.", [])

    def test_secret_like_recovery_evidence_is_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            store = Path(d)
            self.blocked(store)
            with self.assertRaises(recovery.wf.CaseError):
                recovery.recover_successor(
                    store,
                    PRE,
                    "protected://feedback/token=supersecretvalue",
                    "2026-08-22T05:30:00Z",
                    OWNER,
                    BASELINE,
                    "Unsafe evidence reference.",
                    case_id=NEXT,
                )

    def test_duplicate_successor_id_is_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            store = Path(d)
            self.blocked(store)
            recovery.recover_successor(
                store,
                PRE,
                "protected://customer-feedback/new-evidence-1",
                "2026-08-22T05:30:00Z",
                OWNER,
                BASELINE,
                "First recovery attempt.",
                case_id=NEXT,
            )
            with self.assertRaises(recovery.wf.CaseError):
                recovery.recover_successor(
                    store,
                    PRE,
                    "protected://customer-feedback/new-evidence-2",
                    "2026-08-22T05:31:00Z",
                    OWNER,
                    BASELINE,
                    "Duplicate successor id must fail closed.",
                    case_id=NEXT,
                )


if __name__ == "__main__":
    unittest.main()
