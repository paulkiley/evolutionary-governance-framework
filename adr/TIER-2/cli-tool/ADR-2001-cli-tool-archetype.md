# ADR-2001 – CLI Tool Archetype

### Status

Accepted

### Context

Command‑line applications require ergonomic interfaces and packaging.

### Decision

* Use [Typer](https://typer.tiangolo.com/) for building command‑line interfaces in Python.
* Package the tool using `pyproject.toml` with entry points configured.
* Provide a `Dockerfile` for running the CLI in containerized environments.

### Consequences

This archetype standardizes CLI development around Typer, simplifying argument parsing and automatic help pages.  Alternative frameworks may be used with justification in a Tier 3 ADR.