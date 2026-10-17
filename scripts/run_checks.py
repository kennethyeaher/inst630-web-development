"""Run each collected JavaScript project's locked checks and browser suite."""
from pathlib import Path
import argparse
import os
import subprocess

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ["04-rsvp-interaction", "05-array-methods", "06-async-directory", "07-external-libraries"]


def run_checks(install):
    """Optionally install locked dev packages, then stop on any failed project check."""
    for name in PROJECTS:
        folder = ROOT / "projects" / name
        print(f"Checking {name}", flush=True)
        if install:
            subprocess.run(["npm", "ci", "--ignore-scripts"], cwd=folder, check=True)
            if not os.environ.get("BROWSER_CHANNEL"):
                subprocess.run(["npx", "--no-install", "playwright", "install", "chromium"], cwd=folder, check=True)
        subprocess.run(["npm", "run", "check"], cwd=folder, check=True)
        subprocess.run(["npm", "test"], cwd=folder, check=True)
    print("PASS: all four project checks and test suites", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--install", action="store_true", help="Install locked development packages and Chromium when needed")
    run_checks(parser.parse_args().install)
