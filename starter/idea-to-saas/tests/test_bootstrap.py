"""Deterministic tests for the non-destructive discovery initializer."""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "bootstrap.py"
EXPECTED = {"PRODUCT.md", "DECISIONS.md", "NEXT.md", "INTERVIEWER.md", "QUESTION-COVERAGE.md"}


class BootstrapTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.workspace = self.root / "product"
        self.workspace.mkdir()

    def run_bootstrap(self, *arguments):
        return subprocess.run(
            [sys.executable, str(SCRIPT), *arguments, str(self.workspace)],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

    def test_creates_five_records(self):
        result = self.run_bootstrap()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual({p.name for p in (self.workspace / "discovery").iterdir()}, EXPECTED)
        self.assertIn("single", (self.workspace / "discovery" / "INTERVIEWER.md").read_text(encoding="utf-8"))

    def test_existing_records_are_never_overwritten(self):
        first = self.run_bootstrap()
        self.assertEqual(first.returncode, 0, first.stderr)
        record = self.workspace / "discovery" / "PRODUCT.md"
        record.write_text("USER CORRECTED THIS", encoding="utf-8")
        second = self.run_bootstrap()
        self.assertEqual(second.returncode, 0, second.stderr)
        self.assertEqual(record.read_text(encoding="utf-8"), "USER CORRECTED THIS")
        self.assertIn("SKIP (exists)", second.stdout)

    def test_dry_run_changes_nothing(self):
        result = self.run_bootstrap("--dry-run")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("WOULD CREATE", result.stdout)
        self.assertFalse((self.workspace / "discovery").exists())

    def test_missing_workspace_does_not_get_created(self):
        missing = self.root / "missing"
        result = subprocess.run(
            [sys.executable, str(SCRIPT), str(missing)],
            text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
        )
        self.assertEqual(result.returncode, 2)
        self.assertFalse(missing.exists())

    def test_symlinked_discovery_path_is_rejected(self):
        outside = self.root / "outside"
        outside.mkdir()
        try:
            (self.workspace / "discovery").symlink_to(outside, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("Symbolic links unavailable")
        result = self.run_bootstrap()
        self.assertEqual(result.returncode, 2)
        self.assertEqual(list(outside.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
