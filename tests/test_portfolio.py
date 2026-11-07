"""Regression checks for the approved one-page hiring portfolio."""
from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
CONTACT = 'attila.grynaeus@gmail.com'

class PortfolioTests(unittest.TestCase):
    def setUp(self):
        self.readme = (ROOT / 'README.md').read_text(encoding='utf-8')

    def test_all_contact_links_have_approved_address(self):
        links = re.findall(r'mailto:([^\s\)\"<>]+)', self.readme)
        self.assertGreaterEqual(len(links), 2)
        self.assertEqual({x.split('?')[0] for x in links}, {CONTACT})
        self.assertIn(CONTACT, self.readme)

    def test_core_cases_are_inline_not_clickthrough(self):
        for anchor in ('ai-systems', 'shardforge-farm', 'enterprise-delivery', 'contact'):
            self.assertIn(f'id="{anchor}"', self.readme)
        for phrase in ('**Challenge.**', '**Built.**', '**Result.**'):
            self.assertGreaterEqual(self.readme.count(phrase), 3)
        self.assertNotIn('(docs/shardforge-farm.md)', self.readme)
        self.assertNotIn('(docs/velyndra-mcp-case-study.md)', self.readme)

    def test_main_readme_owns_both_responsive_diagrams(self):
        for name in ('system-dark-v2.svg', 'system-mobile-dark-v2.svg', 'velyndra-architecture-dark-v2.svg', 'velyndra-architecture-mobile-dark-v2.svg'):
            self.assertIn(f'assets/{name}', self.readme)

    def test_stories_precede_optional_activity(self):
        self.assertGreater(self.readme.index('## GitHub activity'), self.readme.index('## Code you can actually inspect'))
        self.assertIn('27+ years', self.readme)
        self.assertIn('three read-only MCP tools', self.readme)
        self.assertIn('fictional client alias', self.readme)
        self.assertIn('Software Architect', self.readme)
        self.assertIn('Staff', self.readme)

    def test_real_code_samples_stay_visible(self):
        self.assertIn('PromptCard.deleteConfirm.test.jsx', self.readme)
        self.assertIn('ApiSpecValidator.java', self.readme)
        self.assertIn('proof of concept', self.readme.lower())

    def test_no_repetitive_scale_disclaimers_or_fake_metrics(self):
        for phrase in ('No claims of', 'not presented as a shipped', '99.99%', 'million players', 'zero bugs'):
            self.assertNotIn(phrase, self.readme)
        self.assertLess(len(self.readme.split()), 1000)

    def test_compatibility_docs_route_to_canonical_inline_story(self):
        for filename, anchor in [('shardforge-farm.md', 'shardforge-farm'), ('velyndra-mcp-case-study.md', 'ai-systems')]:
            path = ROOT / 'docs' / filename
            self.assertTrue(path.is_file(), str(path))
            text = path.read_text(encoding='utf-8')
            self.assertIn('../README.md#' + anchor, text)
            self.assertLess(len(text.split()), 100)

    def test_project_headings_are_clear_and_unsuffixed(self):
        self.assertNotRegex(self.readme, r'(?m)^###\s*0[123]\s*/')
        for heading in ('SHARDFORGE FARM', 'Velyndra Event Systems', 'Bison Schweiz AG'):
            self.assertRegex(self.readme, r'(?m)^###\s+.*' + re.escape(heading))
        for name in ('shardforge', 'velyndra', 'enterprise'):
            self.assertIn(f'assets/project-{name}.svg', self.readme)
            self.assertIn(f'assets/project-{name}-mobile.svg', self.readme)

    def test_premium_dark_diagrams_instead_of_white(self):
        for filename in ('system-dark-v2.svg', 'system-mobile-dark-v2.svg',
                         'velyndra-architecture-dark-v2.svg', 'velyndra-architecture-mobile-dark-v2.svg'):
            path=ROOT/'assets'/filename
            doc=ET.parse(path).getroot()
            contents=path.read_text()
            self.assertIn('url(#night)', contents)
            self.assertIn('prefers-reduced-motion', contents)
            self.assertNotIn('#FFFFFF', contents)
            self.assertNotIn('#F5F8FE', contents)
            self.assertIn('@keyframes trace', contents)
            self.assertGreater(len(list(doc.iter())), 25)

    def test_activity_shows_real_profile_data_not_fabricated_numbers(self):
        self.assertIn('profile/activity-dark.svg', self.readme)
        self.assertIn('profile/stats.svg', self.readme)
        self.assertLess(self.readme.index('## Working stack'), self.readme.index('## GitHub activity'))
        self.assertIn('GitHub activity', self.readme)
        self.assertNotIn('10K stars', self.readme)

    def test_diagrams_agree_on_authority_and_connection_edges(self):
        required = {'client-api', 'client-gateway', 'gateway-runtime', 'runtime-api', 'api-postgres', 'api-directory'}
        for filename in ('system-dark-v2.svg', 'system-mobile-dark-v2.svg'):
            path = ROOT / 'assets' / filename
            self.assertTrue(path.is_file(), str(path))
            doc = ET.parse(path).getroot()
            ids = {x.get('id') for x in doc.iter()}
            self.assertTrue(required <= ids, (filename, required - ids))
            text = ''.join(doc.itertext())
            self.assertIn('PostgreSQL', text)
            self.assertIn('Redis', text)
            self.assertNotIn('AWS Architecture', text)

if __name__ == '__main__':
    unittest.main()
