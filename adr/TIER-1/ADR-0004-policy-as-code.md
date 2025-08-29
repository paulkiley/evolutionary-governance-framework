# ADR-0004 – Policy as Code

### Status

Accepted

### Context

Some architectural and security rules cannot be captured by simple linters.  A more expressive mechanism is needed for infrastructure and configuration policies.

### Decision

Use [Open Policy Agent](https://www.openpolicyagent.org/) (OPA) to codify policies in Rego.  Policies are stored under `platform/policy/opa/policies` and tested using `conftest`.  The CI pipeline runs these policies to validate infrastructure and configuration.

### Consequences

Defining policies as code ensures that complex rules are versioned and automatically enforced.  Contributors must learn the basics of Rego to extend policies.