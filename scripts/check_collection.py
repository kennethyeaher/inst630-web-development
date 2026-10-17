"""Verify source snapshots, local documentation targets, and JavaScript syntax."""
from pathlib import Path
import hashlib
import html
import json
import re
import subprocess
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def document_anchors(path):
    """Return Markdown heading slugs and explicit HTML ids for local fragment checks."""
    text = path.read_text()
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    anchors = set(re.findall(r'id=["\']([^"\']+)["\']', text))
    counts = {}
    for heading in re.findall(r"^#{1,6} +(.+)$", text, re.MULTILINE):
        label = html.unescape(re.sub(r"<[^>]+>", "", heading)).lower()
        slug = re.sub(r"[^\w -]", "", label).replace(" ", "-")
        count = counts.get(slug, 0)
        anchors.add(f"{slug}-{count}" if count else slug)
        counts[slug] = count + 1
    return anchors


def check_collection():
    """Raise on missing, changed, or unexpected snapshot files and broken local links."""
    catalog = json.loads((ROOT / "catalog.json").read_text())
    count = 0
    for project in catalog:
        base = ROOT / "projects" / project["id"]
        tracked = subprocess.check_output(
            ["git", "ls-files", "--", str(base.relative_to(ROOT))], cwd=ROOT, text=True
        ).splitlines()
        actual = {str(Path(path).relative_to(base.relative_to(ROOT))) for path in tracked}
        assert actual == set(project["files"]), f"Snapshot file list differs: {base.name}"
        for name, expected in project["files"].items():
            file = base / name
            assert hashlib.sha256(file.read_bytes()).hexdigest() == expected, str(file)
            count += 1
            if file.suffix in {".js", ".mjs", ".cjs"}:
                subprocess.run(["node", "--check", str(file)], check=True, capture_output=True)

    # Imported documentation keeps its original context; validate new collection docs.
    documents = [ROOT / "README.md", ROOT / "index.html", *sorted((ROOT / "docs").glob("*.md")), *sorted((ROOT / "docs").glob("*.html"))]
    anchor_cache = {}
    link_count = 0
    for document in documents:
        content = document.read_text()
        links = re.findall(r"\]\(([^)]+)\)", content)
        links += re.findall(r'(?:href|src)="([^"]+)"', content)
        for srcset in re.findall(r'srcset="([^"]+)"', content):
            links.extend(candidate.strip().split()[0] for candidate in srcset.split(","))
        for link in links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            target = (document.parent / unquote(parsed.path)).resolve() if parsed.path else document
            assert target.is_relative_to(ROOT), f"Link escapes collection: {link}"
            assert target.exists(), f"Missing target in {document.name}: {link}"
            if parsed.fragment and target.suffix in {".md", ".html"}:
                if target not in anchor_cache:
                    anchor_cache[target] = document_anchors(target)
                assert unquote(parsed.fragment) in anchor_cache[target], f"Missing fragment in {document.name}: {link}"
            link_count += 1
    subprocess.run(["node", "--check", str(ROOT / "scripts/render_showcase.cjs")], check=True, capture_output=True)
    print(f"PASS: {len(catalog)} snapshots, {count} file hashes, JavaScript syntax, {link_count} local links")


if __name__ == "__main__":
    check_collection()
