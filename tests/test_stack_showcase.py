"""Public technology stack, identity and activity-art regression tests."""
import json
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
NAMES = ['Java','Spring Boot','TypeScript','Node.js','PostgreSQL','Redis','Kafka','Docker','Kubernetes','AWS','Azure','Google Cloud','GitLab CI','Grafana','GitHub Actions','UC4 / Automic']

class StackShowcaseTests(unittest.TestCase):
    def setUp(self):
        self.readme = (ROOT / "README.md").read_text(encoding="utf-8")

    def test_stack_is_visible_directly_above_activity(self):
        self.assertLess(self.readme.index("## Working stack"), self.readme.index("## GitHub activity"))
        self.assertIn('src="assets/stack-icons-v1.svg"', self.readme)
        self.assertIn('srcset="assets/stack-icons-mobile-v1.svg"', self.readme)
        self.assertIn("UC4 / Automic", self.readme)
        self.assertIn("AWS (target architecture)", self.readme)
        self.assertIn("profile/stats.svg", self.readme)

    def test_desktop_and_mobile_icons_are_local_complete_and_accessible(self):
        for filename in ("stack-icons-v1.svg", "stack-icons-mobile-v1.svg"):
            svg = ET.parse(ROOT / "assets" / filename).getroot()
            self.assertEqual(svg.tag, "{http://www.w3.org/2000/svg}svg")
            icons = [el.get("data-skill") for el in svg.iter() if el.get("data-skill")]
            self.assertEqual(icons, list(NAMES))
            desc = svg.find("{http://www.w3.org/2000/svg}desc")
            self.assertIsNotNone(desc)
            for name in NAMES:
                self.assertIn(name, desc.text)
            text = (ROOT / "assets" / filename).read_text(encoding="utf-8")
            self.assertNotIn("@font-face", text)
            self.assertNotIn("<script", text)
            self.assertNotIn("https://", text)
            self.assertNotIn("http://", text.replace("http://www.w3.org/2000/svg", ""))

    def test_activity_is_rainbow_generated_from_owned_account(self):
        profiles = json.loads((ROOT / "config/profile-3d.json").read_text(encoding="utf-8"))
        dark = next(row for row in profiles if row["fileName"] == "activity-dark.svg")
        self.assertEqual(dark["type"], "rainbow")
        self.assertTrue(dark["growingAnimation"])
        self.assertEqual(len(dark["contribLightness"]), 5)
        self.assertLess(dark["hueRatio"], 0)
        self.assertIn("profile/activity-dark.svg", self.readme)
        self.assertNotIn("Om Lahore's GitHub Stats", self.readme)

    def test_icon_license_and_authentic_career_boundaries(self):
        license = (ROOT / "assets/skill-icons-LICENSE.txt").read_text(encoding="utf-8")
        self.assertIn("MIT License", license)
        self.assertIn("Copyright (c) 2022 tandpfun", license)
        self.assertIn("UC4 / Automic", license)
        self.assertNotIn("millions of players", self.readme.lower())

if __name__ == "__main__":
    unittest.main()
