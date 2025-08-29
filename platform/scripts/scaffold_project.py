#!/usr/bin/env python3
"""
Scaffold a new project from an EGF archetype.

This script accepts an archetype name (e.g. 'web-service') and a project slug
and copies the corresponding cookiecutter template to a new directory,
rendering variables as needed.
"""
import argparse
import os
import shutil

TEMPLATE_ROOT = os.path.join(os.path.dirname(__file__), "..", "..", "archetypes")


def scaffold(archetype: str, slug: str) -> None:
    template_dir = os.path.join(TEMPLATE_ROOT, archetype, "{{cookiecutter.project_slug}}")
    target_dir = os.path.join(os.getcwd(), slug)
    if os.path.exists(target_dir):
        raise SystemExit(f"Target directory {target_dir} already exists")
    shutil.copytree(template_dir, target_dir)
    # Replace placeholder in file names and contents
    for root, _, files in os.walk(target_dir):
        for name in files:
            file_path = os.path.join(root, name)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            content = content.replace("{{cookiecutter.project_slug}}", slug)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
    print(f"Project scaffolded at {target_dir}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Scaffold a new EGF project")
    parser.add_argument("archetype", choices=["web-service", "cli-tool", "data-science"])
    parser.add_argument("slug")
    args = parser.parse_args()
    scaffold(args.archetype, args.slug)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())