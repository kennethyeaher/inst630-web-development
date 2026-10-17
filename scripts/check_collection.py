"""Verify source snapshots, local documentation targets, and JavaScript syntax."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


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
    documents = [ROOT / "README.md", ROOT / "index.html", *sorted((ROOT / "docs").glob("*.md"))]
    link_count = 0
    for document in documents:
        content = document.read_text()
        links = re.findall(r"\]\(([^)]+)\)", content)
        links += re.findall(r'(?:href|src)="([^"]+)"', content)
        for link in links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            target = (document.parent / unquote(parsed.path)).resolve()
            assert target.is_relative_to(ROOT), f"Link escapes collection: {link}"
            assert target.exists(), f"Missing target in {document.name}: {link}"
            link_count += 1
    print(f"PASS: {len(catalog)} snapshots, {count} file hashes, JavaScript syntax, {link_count} local links")


if __name__ == "__main__":
    check_collection()
