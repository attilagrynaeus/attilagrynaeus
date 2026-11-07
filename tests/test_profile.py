import re
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

    def test_missing_local_anchor_is_rejected(self):
        (self.root / 'README.md').write_text('[Jump](#missing)')
        with self.assertRaisesRegex(ValueError, 'anchor'):
            validate(self.root)

    def test_explicit_anchor_and_heading_are_accepted(self):
        (self.root / 'README.md').write_text('<a id="case"></a>\n## Working stack\n[Case](#case) [Stack](#working-stack)')
        self.assertEqual(validate(self.root), 0)

    def test_cross_document_anchor_is_validated(self):
        (self.root / 'docs').mkdir()
        (self.root / 'docs/a.md').write_text('[Case](../README.md#missing)')
        with self.assertRaisesRegex(ValueError, 'anchor'):
            validate(self.root)

    def test_invalid_mailto_is_rejected(self):
        (self.root / 'README.md').write_text('[Email](mailto:attila.grynaeus.gmail.com)')
        with self.assertRaisesRegex(ValueError, 'email'):
            validate(self.root)

    def test_valid_mailto_with_subject_is_accepted(self):
        (self.root / 'README.md').write_text('[Email](mailto:attila.grynaeus@gmail.com?subject=Hello)')
        self.assertEqual(validate(self.root), 0)

    def test_external_svg_resource_is_rejected(self):
        (self.root / 'assets/a.svg').write_text(SVG.replace('</svg>', '<image href="https://example.com/track.png"/></svg>'))
        with self.assertRaisesRegex(ValueError, 'external'):
            validate(self.root)

    def test_internal_svg_gradient_is_accepted(self):
        (self.root / 'assets/a.svg').write_text(SVG.replace('</svg>', '<defs><linearGradient id="a"/></defs><rect fill="url(#a)"/></svg>'))
        self.assertEqual(validate(self.root), 1)

    def test_javascript_link_is_rejected(self):
        (self.root / 'README.md').write_text('<a href="javascript:alert(1)">Bad</a>')
        with self.assertRaisesRegex(ValueError, 'Unsafe'):
            validate(self.root)

    def test_empty_markdown_image_alt_is_rejected(self):
        (self.root / 'README.md').write_text('![](assets/a.svg)')
        with self.assertRaisesRegex(ValueError, 'alt'):
            validate(self.root)

    def test_mobile_image_source_must_exist(self):
        (self.root / 'README.md').write_text('<picture><source media="(max-width:600px)" srcset="assets/missing.svg"/><img src="assets/a.svg" alt="A diagram"/></picture>')
        with self.assertRaisesRegex(ValueError, 'Missing'):
            validate(self.root)

class PositioningRegressionTests(unittest.TestCase):
    """Retain approved experience, anonymization and privacy guarantees."""

    def test_27_year_claim_on_all_surfaces(self):
        root = Path(__file__).resolve().parents[1]
        readme = (root / 'README.md').read_text(encoding='utf-8')
        self.assertIn('27+ years', readme)
        self.assertNotIn('25+ years', readme)
        for file_name in ('header.svg', 'header-mobile.svg'):
            svg = (root / 'assets' / file_name).read_text(encoding='utf-8')
            self.assertIn('27+ YEARS IN ENTERPRISE SOFTWARE', svg)
            self.assertNotIn('25+ YEARS IN ENTERPRISE SOFTWARE', svg)

    def test_llm_case_study_is_anonymized(self):
        root = Path(__file__).resolve().parents[1]
        readme = (root / 'README.md').read_text(encoding='utf-8')
        case = (root / 'docs/velyndra-mcp-case-study.md').read_text(encoding='utf-8')
        legacy = 'event' + 'frog'
        for text in (readme, case):
            self.assertNotIn(legacy, text.lower())
        self.assertIn('LLM application architecture', readme)
        self.assertIn('three read-only MCP tools', readme)
        self.assertIn('fictional client alias', readme)
        self.assertIn('fictional client alias', case)

    def test_anonymized_story_has_no_original_endpoints(self):
        root = Path(__file__).resolve().parents[1]
        texts = [(root / 'README.md').read_text(), (root / 'docs/velyndra-mcp-case-study.md').read_text()]
        for content in texts:
            for removed in ('list_' + 'rubrics', 'search_' + 'events', 'get_' + 'event'):
                self.assertNotIn(removed, content)

    def test_old_branded_assets_are_not_part_of_current_tree(self):
        root = Path(__file__).resolve().parents[1]
        forbidden = 'event' + 'frog'
        for path in (root / 'docs').glob('*.md'):
            self.assertNotIn(forbidden, path.name.lower())
        for path in (root / 'assets').glob('*.svg'):
            self.assertNotIn(forbidden, path.name.lower())

    def test_retired_game_brand_absent_from_public_tree(self):
        root = Path(__file__).resolve().parents[1]
        pattern = re.compile(r'\br\.?\s*a\.?\s*m\.?[\s_-]*farm\b', re.I)
        for file_path in root.rglob('*'):
            if not file_path.is_file() or '.git' in file_path.parts:
                continue
            if file_path.suffix.lower() not in {'.md', '.svg', '.py', '.yml', '.yaml', '.json'}:
                continue
            relative_path = file_path.relative_to(root)
            self.assertIsNone(pattern.search(str(relative_path)), str(relative_path))
            self.assertIsNone(pattern.search(file_path.read_text(encoding='utf-8')), str(relative_path))

    def test_repository_documents_and_assets_validate(self):
        self.assertEqual(validate(Path(__file__).resolve().parents[1]), 6)

if __name__ == '__main__':
    unittest.main()
