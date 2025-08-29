# ADR-0003 – Continuous Integration as the Ultimate Gate

### Status

Accepted

### Context

Automated gates are required to ensure that only high‑quality code is merged.

### Decision

* All pull requests must run through a continuous integration (CI) pipeline that executes tests, linters, type checkers and any policy checks.
* The CI system (e.g. GitHub Actions) is considered the final authority; code may not be merged if the CI fails.

### Consequences

This decision enforces a high bar for code quality and reliability.  It may lengthen feedback cycles slightly but prevents regressions and ensures consistent enforcement.