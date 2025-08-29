# Rule Tier System

The Rule Tier System organises architectural decisions into three tiers:

* **Tier 1 – Universal Mandates:** These ADRs apply to every project without exception.  They encode organisational standards such as code formatting, licensing and the requirement for documentation.  See `adr/TIER-1/` for the current universal ADRs.

* **Tier 2 – Project Archetypes:** Each archetype defines an opinionated starting point for a class of projects (e.g. web services, CLI tools, data science).  Archetype ADRs capture domain‑specific best practices, preferred frameworks and default configurations.  New projects begin by selecting an archetype and inheriting its Tier 2 ADRs.

* **Tier 3 – Contextual Decisions:** These ADRs record project‑specific decisions that solve particular problems or constraints.  They may refine or override aspects of Tier 2, but must remain consistent with Tier 1.  Tier 3 ADRs live within the project repository.

This tiered approach streamlines decision making: most questions are answered by existing ADRs, leaving the architect free to focus on truly novel challenges.