#!/usr/bin/env python3
"""Small release-facing checks for generated static pages."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from content import PAGES

ROOT = Path(__file__).resolve().parent
HTML_FILES = [ROOT / "index.html", ROOT / "support.html"] + [ROOT / data["file"] for data in PAGES.values()]


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[str] = []
        self.ids: list[str] = []
        self.classes: list[str] = []
        self.h1_count = 0
        self.main_count = 0
        self.images_without_alt: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "a" and values.get("href"):
            self.links.append(values["href"] or "")
        if tag in {"img", "script", "link"}:
            url = values.get("src") or values.get("href")
            if url and url.startswith("./"):
                self.links.append(url)
        if tag == "img" and "alt" not in values:
            self.images_without_alt.append(values.get("src") or "")
        if values.get("id"):
            self.ids.append(values["id"] or "")
        if values.get("class"):
            self.classes.extend((values["class"] or "").split())
        if tag == "h1":
            self.h1_count += 1
        if tag == "main":
            self.main_count += 1


def parse(path: Path) -> PageParser:
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def main() -> None:
    parsed = {path.name: parse(path) for path in HTML_FILES}
    errors: list[str] = []
    for path in HTML_FILES:
        page = parsed[path.name]
        text = path.read_text(encoding="utf-8")
        if page.h1_count != 1 or page.main_count != 1:
            errors.append(f"{path.name}: expected one h1 and one main")
        if len(page.ids) != len(set(page.ids)):
            errors.append(f"{path.name}: duplicate IDs")
        if not {"lang-es", "lang-en"}.issubset(page.classes):
            errors.append(f"{path.name}: language content missing")
        if page.images_without_alt:
            errors.append(f"{path.name}: image without alt attribute")
        if path.name not in {"index.html", "support.html"}:
            if "document-meta" not in page.classes or 'datetime="2026-09-15"' not in text:
                errors.append(f"{path.name}: effective date or version missing")
        if any(marker in text.lower() for marker in ("borrador", "texto en revisión", "text under review", "still drafts", "noindex,nofollow")):
            errors.append(f"{path.name}: release placeholder remains")
        if "Google Play" in text or "June 2026" in text:
            errors.append(f"{path.name}: historical release copy remains")
        if any(marker in text for marker in ("+505", "Colonia 9 de Junio")):
            errors.append(f"{path.name}: private owner contact unexpectedly published")
        if path.name in {"index.html", "support.html"} and "Brandon Stevens" in text:
            errors.append(f"{path.name}: legal owner identity placed in brand-facing page")
        for link in page.links:
            parts = urlsplit(link)
            if parts.scheme or parts.netloc:
                continue
            target_name = unquote(parts.path).removeprefix("./") or path.name
            target = (ROOT / target_name).resolve()
            if not target.is_relative_to(ROOT) or not target.exists():
                errors.append(f"{path.name}: broken local link {link}")
                continue
            if parts.fragment and target.suffix == ".html":
                if parts.fragment not in parsed[target.name].ids:
                    errors.append(f"{path.name}: missing anchor {link}")
    if errors:
        raise SystemExit("\n".join(errors))
    for name in ("support.html", "privacy.html", "delete-account.html"):
        if "mailto:arvilolabs@gmail.com" not in parsed[name].links:
            raise SystemExit(f"{name}: public contact missing")
    for name in ("terms.html", "delete-account.html"):
        if "https://apps.apple.com/account/subscriptions" not in parsed[name].links:
            raise SystemExit(f"{name}: Apple subscription management link missing")
    for name in ("privacy.html", "terms.html"):
        if "Brandon Stevens Aragón Mejía" not in (ROOT / name).read_text(encoding="utf-8"):
            raise SystemExit(f"{name}: legal owner identity missing")
    print(f"Checked {len(HTML_FILES)} bilingual pages, local links, anchors, landmarks, legal identity, and effective dates.")


if __name__ == "__main__":
    main()
