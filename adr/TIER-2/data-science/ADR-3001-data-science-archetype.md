# ADR-3001 – Data Science Archetype

### Status

Accepted

### Context

Data science projects have specific requirements around notebooks, reproducibility and dependency management.

### Decision

* Use [Jupyter notebooks](https://jupyter.org/) stored in the `notebooks/` directory.  Encourage modular code in `src/`.
* Use [Poetry](https://python-poetry.org/) for dependency management and environment isolation.
* Provide a `Dockerfile` and `docker-compose.yml` with common data science libraries (e.g., pandas, numpy, matplotlib).

### Consequences

This archetype accelerates data science work while promoting reproducibility.  Teams may customize dependencies and environments; such changes must be captured in Tier 3 ADRs.