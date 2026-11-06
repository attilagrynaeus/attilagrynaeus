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

if __name__ == '__main__':
    unittest.main()
