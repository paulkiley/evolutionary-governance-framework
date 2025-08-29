# ADR-0002 – Static and Pre-Commit Enforcement

### Status

Accepted

### Context

To make quality the default, static analysis and pre‑commit hooks should automatically enforce coding standards before code enters the main branch.

### Decision

* **Static Enforcement:** Tools such as [Black](https://github.com/psf/black), [Ruff](https://github.com/charliermarsh/ruff) and [Mypy](https://github.com/python/mypy) must be configured and run as part of the development workflow.
* **Pre‑Commit Hooks:** The repository must configure [pre-commit](https://pre-commit.com) to run linters, formatters and type checkers on every commit.

### Consequences

Developers receive rapid feedback on code quality.  Poorly formatted or type‑unsafe code cannot be committed.  Teams must occasionally update tool versions and configurations.