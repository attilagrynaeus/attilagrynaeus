"""Validate local README references and SVGs using only the Python standard library."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import xml.etree.ElementTree as ET


class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'img' and not attrs.get('alt', '').strip():
            raise ValueError('Image is missing descriptive alt text')
        for key in ('href', 'src'):
            if attrs.get(key):
                self.urls.append(attrs[key])
        if attrs.get('srcset'):
            self.urls.extend(part.strip().split()[0] for part in attrs['srcset'].split(','))


def validate(root: Path) -> int:
    root = root.resolve()
    assets = set()
    documents = [root / 'README.md', *sorted((root / 'docs').glob('*.md'))]
    for document in documents:
        text = document.read_text(encoding='utf-8')
        if re.search(r'github\.com/attilagrynaeus/farm(?:[/\s)#"?]|$)', text):
            raise ValueError(f'Private source link in {document.name}')
        parser = References()
        parser.feed(text)
        urls = parser.urls + re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', text)
        for url in urls:
            parts = urlsplit(url)
            if parts.scheme:
                if parts.scheme not in ('https', 'mailto'):
                    raise ValueError(f'Unsafe link scheme: {parts.scheme}')
                continue
            if parts.netloc:
                raise ValueError('Use explicit HTTPS for external links')
            if not parts.path:
                continue
            path = (document.parent / unquote(parts.path)).resolve()
            if not path.is_relative_to(root):
                raise ValueError(f'Reference outside repository: {url}')
            if not path.is_file():
                raise ValueError(f'Missing local reference: {url}')
            if path.suffix == '.svg':
                assets.add(path)
    for path in assets:
        data = path.read_text(encoding='utf-8')
        if path.stat().st_size > 2_000_000:
            raise ValueError(f'Oversized SVG: {path.name}')
        if re.search(r'<script\b|<foreignObject\b|\bon\w+\s*=|data:font|@font-face|<!DOCTYPE|<!ENTITY', data, re.I):
            raise ValueError(f'Unsafe SVG: {path.name}')
        try:
            svg = ET.fromstring(data)
        except ET.ParseError as error:
            raise ValueError(f'Invalid SVG: {path.name}') from error
        if svg.tag != '{http://www.w3.org/2000/svg}svg' or not svg.get('viewBox'):
            raise ValueError(f'Invalid SVG root/viewBox: {path.name}')
        if 'Something went wrong' in data:
            raise ValueError(f'Upstream error card: {path.name}')
    return len(assets)


if __name__ == '__main__':
    count = validate(Path(__file__).resolve().parents[1])
    print(f'Profile validation passed: {count} local SVGs and all local document links')
