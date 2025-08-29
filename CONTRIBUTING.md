# Contributing

Thank you for your interest in contributing to the Evolutionary Governance Framework (EGF)!  We welcome contributions in the form of bug reports, feature requests, documentation improvements and pull requests.

## Getting Started

1. Fork the repository and clone your fork locally.
2. Install development dependencies by running `pre-commit install` (see `.pre-commit-config.yaml`).
3. Create a new branch for your contribution (e.g. `feature/awesome‑thing`).
4. Make your changes, including updating or adding ADRs under the appropriate Tier.  Every significant decision should have an accompanying ADR.
5. Commit your changes following conventional commit guidelines.
6. Push your branch and open a pull request against the `main` branch.  Fill in the pull request template describing your change.

## ADRs

Architectural decisions are tracked in the `adr/` directory.  Use the `adr/template.md` file as a starting point and assign a unique ID.  Tier 1 ADRs define universal mandates for all projects; Tier 2 ADRs define archetype best practices; Tier 3 ADRs capture project‑specific decisions.  See `docs/adr/adr-guide.md` for details.