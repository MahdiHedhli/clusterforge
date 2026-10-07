"""Regression tests for the offline curriculum checker."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tooling"))
from validate_curriculum import HEADINGS, local_target, read_json, validate


class CurriculumValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.addCleanup(self.tmp.cleanup)
        tracks = []
        for track_id in ("K8S-200", "K8S-300", "SEC-200", "SEC-300"):
            folder = self.root / "curriculum" / track_id
            folder.mkdir(parents=True)
            (folder / "README.md").write_text("# Track\n", encoding="utf-8")
            assessment = self.root / "assessments" / f"{track_id}.md"
            assessment.parent.mkdir(exist_ok=True)
            assessment.write_text("# Assessment\n", encoding="utf-8")
            lessons = []
            for number in range(1, 7):
                name = f"{number:02d}.md"
                lessons.append(name)
                text = f"# {track_id}-{number:02d}: Test\n\n**Status:** Draft. Runtime not verified.\n"
                text += "\n".join(HEADINGS) + "\n[Source](https://kubernetes.io/)\n"
                (folder / name).write_text(text, encoding="utf-8")
            tracks.append({"id": track_id, "path": str((folder / "README.md").relative_to(self.root)), "assessment": str(assessment.relative_to(self.root)), "lessons": lessons})
        self.catalog_path = self.root / "curriculum/catalog-200-300.json"
        self.catalog_path.write_text(json.dumps({"tracks": tracks, "content_status": "Draft", "runtime_validation": "NOT_RUN", "learner_progress": "NOT_RECORDED"}), encoding="utf-8")
        packet_dir = self.root / "curriculum/practicals/levels-200-300"
        packet_dir.mkdir(parents=True)
        for name in ("identity", "incident", "customer"):
            (packet_dir / f"{name}.json").write_text(json.dumps({"synthetic": True, "scenario_id": name}), encoding="utf-8")

    def test_valid_repository(self):
        errors, counts = validate(self.root)
        self.assertEqual(errors, [])
        self.assertEqual(counts["lessons"], 24)
        self.assertEqual(counts["packets"], 3)

    def test_missing_lesson(self):
        (self.root / "curriculum/K8S-200/01.md").unlink()
        self.assertTrue(any("missing lesson" in e for e in validate(self.root)[0]))

    def test_missing_required_heading(self):
        path = self.root / "curriculum/K8S-200/01.md"
        path.write_text(path.read_text().replace("## Evidence and pass conditions", "## Other"))
        self.assertTrue(any("missing ## Evidence" in e for e in validate(self.root)[0]))

    def test_broken_relative_link(self):
        (self.root / "README.md").write_text("[Missing](missing.md)\n")
        self.assertTrue(any("broken local link" in e for e in validate(self.root)[0]))

    def test_existing_and_external_links(self):
        (self.root / "README.md").write_text("[Local](curriculum/K8S-200/README.md) [External](https://example.test/)\n")
        self.assertEqual(validate(self.root)[0], [])
        self.assertEqual(validate(self.root)[1]["local_links"], 1)

    def test_repository_escape(self):
        with self.assertRaises(ValueError):
            local_target(self.root, self.root / "README.md", "../outside.md")

    def test_duplicate_json_key(self):
        path = self.root / "duplicate.json"
        path.write_text('{"a": 1, "a": 2}')
        with self.assertRaises(ValueError):
            read_json(path)

    def test_synthetic_marker_required(self):
        path = self.root / "curriculum/practicals/levels-200-300/identity.json"
        path.write_text('{"synthetic": false, "scenario_id": "identity"}')
        self.assertTrue(any("not explicitly synthetic" in e for e in validate(self.root)[0]))

    def test_no_implied_runtime_pass(self):
        catalog = json.loads(self.catalog_path.read_text())
        catalog["runtime_validation"] = "PASS"
        self.catalog_path.write_text(json.dumps(catalog))
        self.assertTrue(any("must not imply qualification" in e for e in validate(self.root)[0]))

    def test_duplicate_track(self):
        catalog = json.loads(self.catalog_path.read_text())
        catalog["tracks"][1]["id"] = "K8S-200"
        self.catalog_path.write_text(json.dumps(catalog))
        self.assertTrue(any("four track IDs" in e for e in validate(self.root)[0]))


if __name__ == "__main__":
    unittest.main()
