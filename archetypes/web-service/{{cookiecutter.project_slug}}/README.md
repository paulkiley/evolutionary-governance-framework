# Web Service Archetype

This directory is a cookiecutter template for a new FastAPI‑based web service.  When generating a project, the `{{cookiecutter.project_slug}}` variable is replaced with your project’s slug.

Key features:

* Pre‑configured `pyproject.toml` with FastAPI and Uvicorn.
* `Dockerfile` and `docker-compose.yml` for local and production deployment.
* Basic API scaffold with a health endpoint.