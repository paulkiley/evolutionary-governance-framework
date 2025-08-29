# ADR-1001 – Web Service Archetype

### Status

Accepted

### Context

Web services have unique requirements around API design, deployment, and observability.

### Decision

* Use [FastAPI](https://fastapi.tiangolo.com/) with Pydantic for type‑safe API development.
* Include a `Dockerfile` and `docker-compose.yml` for local development and deployment.
* Configure OpenTelemetry tracing by default.  Provide a starter `otel-collector-config.yaml`.

### Consequences

This archetype accelerates web service development with sensible defaults.  Teams may adjust components but should document deviations in Tier 3 ADRs.