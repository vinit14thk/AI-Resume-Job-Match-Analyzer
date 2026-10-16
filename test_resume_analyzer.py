import os
import subprocess
import sys
import unittest
from pathlib import Path

from skill_matcher import skill_is_present

PROJECT_DIR = Path(__file__).resolve().parent


class ResumeAnalyzerTests(unittest.TestCase):

    def test_sample_resume_analysis(self):
        result = subprocess.run(
            [sys.executable, "resume_analyzer.py"],
            input="3\n1\n",
            cwd=PROJECT_DIR,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
            timeout=60
        )

        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn("Analysis completed successfully!", result.stdout)
        self.assertIn("Weighted Skill Match Score:", result.stdout)
        self.assertIn("PDF report generated successfully", result.stdout)

        matching_section = result.stdout.split(
            "Matching Skills:"
        )[1].split("Missing Skills:")[0]

        missing_section = result.stdout.split(
            "Missing Skills:"
        )[1].split("Resume text extracted")[0]

        self.assertIn("data analysis", matching_section)
        self.assertIn("statistics", matching_section)
        self.assertNotIn("machine learning", matching_section)
        self.assertIn("machine learning", missing_section)

    def test_skill_synonyms(self):
        self.assertTrue(
            skill_is_present("scikit-learn", "Experience with sklearn")
        )
        self.assertTrue(
            skill_is_present(
                "data analysis", "Experienced in analysing data"
            )
        )
        self.assertFalse(
            skill_is_present("scikit-learn", "Experience with Java")
        )


if __name__ == "_main_":
    unittest.main(verbosity=2)


