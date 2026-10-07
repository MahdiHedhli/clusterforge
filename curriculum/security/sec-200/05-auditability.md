# SEC-200-05: Auditability and evidence operations

**Status:** Draft. Runtime not verified. **Format:** two 30-minute blocks.

## Objective

Define which events must be recorded, verify a small event path, and identify gaps without mistaking ordinary Kubernetes events for a complete security audit trail.

## Prerequisites

SEC-200-01 and the [synthetic incident packet](../../practicals/levels-200-300/incident.json). A live extension needs an administrator-approved audit sink and access to relevant records. Do not enable broad request-body logging in a shared cluster.

## Learn

Audit coverage depends on policy, stages, levels, collection and retention. More detail can also expose sensitive request content. API auditing, application authorization logs, identity-provider events and runtime telemetry cover different portions of an investigation.

Treat evidence quality as a contract: source, clock, identity, action, resource, outcome, retention, access owner and known blind spots. File permissions or a hash alone do not establish independently protected retention or an immutable audit system.

## Practice

**Block A: design coverage.** Choose five actions: a permitted read, a denied read, a role change, a workload creation and an in-container process execution. Identify the intended evidence source for each. Use the packet to show which of those questions can and cannot be answered. Describe how an investigator would connect identity and workload records without publishing credentials.

**Block B: verify one event.** Where audit collection exists, perform one harmless, approved action on a synthetic lab ConfigMap, record the request time, and find the corresponding event. Verify subject, namespace, action and outcome. Document collection delay and missing fields. A failure to locate it is an unresolved visibility problem until policy, time range and collection path have been checked.

Where no sink exists, write the collection acceptance test and mark live verification NOT_RUN. Do not generate a fake record and call it observed telemetry.

Prepare a retention requirement response using only the fictional customer's stated requirement. Identify who would approve retention, retrieval access, integrity controls and deletion. Do not invent a legally mandated duration.

## Evidence and pass conditions

Submit a coverage matrix, one correlated live event or explicit limitation, and a minimal collection contract. Explain why API permission does not prove data-plane access and why missing logs do not prove absence of activity.

## Reset and resume

Remove any exercise marker object by exact name after evidence capture. Store raw telemetry only in its approved location. Record the missing source or query that should be checked next.

## Sources

- [Kubernetes auditing](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/)
- [Logging architecture](https://kubernetes.io/docs/concepts/cluster-administration/logging/)
- [Falco event sources](https://falco.org/docs/concepts/event-sources/)
