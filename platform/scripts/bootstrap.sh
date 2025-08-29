#!/usr/bin/env bash
set -euo pipefail

# Bootstrap script for EGF repositories.
# Installs pre-commit hooks and any other necessary dependencies.

echo "Installing pre-commit hooks..."
if command -v pre-commit >/dev/null 2>&1; then
    pre-commit install
else
    echo "pre-commit not found.  Please install it with pip or your package manager."
fi

echo "Bootstrap complete."