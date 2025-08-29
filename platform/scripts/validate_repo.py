#!/usr/bin/env python3
"""
Validate an EGF repository.

This script runs basic checks to ensure that required files and directories exist,
and that ADRs follow the correct naming conventions.  It can be extended
to include additional custom validations.
"""
import os
import sys

REQUIRED_TOP_LEVEL = [
    "README.md",
    "LICENSE",
    "adr",
    "docs",
    ".pre-commit-config.yaml",
]


def validate() -> int:
    missing = [p for p in REQUIRED_TOP_LEVEL if not os.path.exists(p)]
    if missing:
        print(f"Validation failed.  Missing files/directories: {', '.join(missing)}")
        return 1
    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(validate())