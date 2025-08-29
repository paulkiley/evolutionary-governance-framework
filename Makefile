.PHONY: help setup lint test validate

help:
	@echo "Available targets:"
	@echo "  setup    Install development dependencies."
	@echo "  lint     Run linters and type checkers."
	@echo "  test     Run test suite (if applicable)."
	@echo "  validate Run conftest against OPA policies."

setup:
	pip install -r requirements.txt || true
	pre-commit install

lint:
	pre-commit run --all-files

validate:
	conftest test platform/policy/opa