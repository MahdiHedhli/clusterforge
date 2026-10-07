# SEC-300-02: Threat models and attack paths

**Status:** Draft. Runtime not verified. **Format:** three 30-minute blocks.

## Objective

Build a threat model that connects attacker capability to an asset, a feasible path, a control and an observable verification condition.

## Prerequisites

SEC-300-01 architecture and the [fictional customer brief](../../practicals/levels-200-300/customer.json). Know the difference between observed behavior, a plausible path and an unsupported speculation.

## Learn

A useful threat statement names actor, starting access, action, boundary crossed and impact. Technique taxonomies can normalize terminology after the path is understood; a list of technique names is not a threat model. Prioritize using exposure, prerequisites, impact and uncertainty rather than unsupported numerical precision.

Consider a compromised workload, overprivileged developer, malicious artifact, mistaken administrator and service outage. These are different scenarios with different evidence and control owners.

## Practice

**Block A: model.** Identify at least five assets and four trust boundaries in the customer architecture. Write six threats spanning identity, workload execution, networking, storage, artifact provenance and administration. Include one non-malicious failure that threatens integrity or availability.

**Block B: trace paths.** Choose three threats and draw their required steps. For each edge, identify prerequisite access and the evidence that would show the transition. Map applicable behavior to current MITRE ATT&CK Containers or ATLAS entries using their primary pages; record the cited entry and retrieval date. Do not invent technique IDs or force an AI taxonomy onto an ordinary infrastructure failure.

**Block C: challenge controls.** Select one high-priority threat and construct a safe validation plan. Include a positive legitimate action, a prohibited action, the expected observations and a rollback. Identify at least one way the chosen control could be bypassed within the model, such as a privileged identity changing its enforcement configuration. Do not implement an exploit against a host or real tenant.

Have the instructor change one assumption: the artifact source is external, a contractor gains workload-creation access, or training moves to shared accelerators. Update the affected paths rather than rewriting the entire model.

## Evidence and pass conditions

Submit the threat register, three path diagrams, source-backed taxonomy mappings and the changed-assumption delta. Pass requires the ability to defend prioritization and to name the observation that would disprove a favored hypothesis.

## Reset and resume

No attack execution is required. Store the versioned model and exact next validation question. Keep any real architecture substitutions in approved internal material.

## Sources

- [MITRE ATT&CK Containers matrix](https://attack.mitre.org/matrices/enterprise/containers/)
- [MITRE ATLAS](https://atlas.mitre.org/)
- [Kubernetes RBAC good practices](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)
