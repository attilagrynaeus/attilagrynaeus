import tempfile
import unittest
from pathlib import Path
from tools.validate_profile import validate

SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><rect width="10" height="10"/></svg>'

class ProfileTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / 'assets').mkdir()
        (self.root / 'assets/a.svg').write_text(SVG)
        (self.root / 'README.md').write_text('<img src="assets/a.svg" alt="A diagram" />')

    def test_valid_local_image(self):
        self.assertEqual(validate(self.root), 1)

    def test_missing_image(self):
        (self.root / 'assets/a.svg').unlink()
        with self.assertRaisesRegex(ValueError, 'Missing'):
            validate(self.root)

    def test_malformed_svg(self):
        (self.root / 'assets/a.svg').write_text('<svg>')
        with self.assertRaisesRegex(ValueError, 'Invalid SVG'):
            validate(self.root)

    def test_script_is_rejected(self):
        (self.root / 'assets/a.svg').write_text(SVG.replace('</svg>', '<script>alert(1)</script></svg>'))
        with self.assertRaisesRegex(ValueError, 'Unsafe'):
            validate(self.root)

    def test_embedded_font_is_rejected(self):
        (self.root / 'assets/a.svg').write_text(SVG.replace('</svg>', '<style>@font-face{src:url(data:font/x)}</style></svg>'))
        with self.assertRaisesRegex(ValueError, 'Unsafe'):
            validate(self.root)

    def test_missing_alt_is_rejected(self):
        (self.root / 'README.md').write_text('<img src="assets/a.svg" />')
        with self.assertRaisesRegex(ValueError, 'alt'):
            validate(self.root)

    def test_outside_path_is_rejected(self):
        (self.root / 'README.md').write_text('[Outside](../other.md)')
        with self.assertRaisesRegex(ValueError, 'outside'):
            validate(self.root)

    def test_private_source_link_is_rejected(self):
        (self.root / 'README.md').write_text('[Game](https://github.com/attilagrynaeus/farm)')
        with self.assertRaisesRegex(ValueError, 'Private'):
            validate(self.root)

class PositioningRegressionTests(unittest.TestCase):
    """Keep public copy consistent with the approved professional experience."""

    def test_27_year_claim_on_all_surfaces(self):
        root = Path(__file__).resolve().parents[1]
        readme = (root / 'README.md').read_text(encoding='utf-8')
        self.assertIn('27+ years', readme)
        self.assertNotIn('25+ years', readme)
        for file_name in ('header.svg', 'header-mobile.svg'):
            svg = (root / 'assets' / file_name).read_text(encoding='utf-8')
            self.assertIn('27+ YEARS IN ENTERPRISE SOFTWARE', svg)
            self.assertNotIn('25+ YEARS IN ENTERPRISE SOFTWARE', svg)

    def test_ai_claim_is_backed_by_eventfrog_reference(self):
        root = Path(__file__).resolve().parents[1]
        readme = (root / 'README.md').read_text(encoding='utf-8')
        for phrase in ('LLM application architecture', 'Eventfrog', 'three typed tools', 'MCP'):
            self.assertIn(phrase, readme)
        self.assertIn('https://eventfrog.de/en/help/organizer/boostprofits/promotion/ai-search.html', readme)
        self.assertNotIn('OAuth integration completed', readme)

class EventfrogCaseStudyTests(unittest.TestCase):
    """Public case study must remain navigable, evidence-backed and privacy-safe."""

    def test_case_study_is_linked_from_featured_work(self):
        root = Path(__file__).resolve().parents[1]
        readme = (root / 'README.md').read_text(encoding='utf-8')
        eventfrog_section = readme.split('### Eventfrog', 1)[1].split('### R.A.M.', 1)[0]
        self.assertIn('docs/eventfrog-chatgpt-mcp.md', eventfrog_section)
        self.assertEqual(readme.count('(docs/eventfrog-chatgpt-mcp.md)'), 1)

    def test_case_study_has_public_sources_and_truthful_scope(self):
        root = Path(__file__).resolve().parents[1]
        case = (root / 'docs/eventfrog-chatgpt-mcp.md').read_text(encoding='utf-8')
        for expected in (
            'sole AI integration and MCP engineer',
            'August 2026',
            'Google Cloud Kubernetes',
            'list_rubrics', 'search_events', 'get_event',
            'https://eventfrog.ch/en/about-us/product-updates.html',
            'https://eventfrog.de/en/help/organizer/boostprofits/promotion/ai-search.html',
            'OAuth 2.0 integration was still in progress',
        ):
            self.assertIn(expected, case)
        self.assertNotIn('OAuth 2.0 is deployed', case)
        self.assertNotIn('github.com/attilagrynaeus/farm', case)

    def test_case_study_has_responsive_diagrams(self):
        root = Path(__file__).resolve().parents[1]
        case = (root / 'docs/eventfrog-chatgpt-mcp.md').read_text(encoding='utf-8')
        for svg in (
            'eventfrog-case-hero.svg',
            'eventfrog-case-hero-mobile.svg',
            'eventfrog-architecture.svg',
            'eventfrog-architecture-mobile.svg',
        ):
            self.assertIn(svg, case)
            self.assertTrue((root / 'assets' / svg).is_file())

if __name__ == '__main__':
    unittest.main()
