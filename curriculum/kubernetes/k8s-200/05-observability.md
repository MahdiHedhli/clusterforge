# K8S-200-05: Observability and node triage

**Status:** Draft. Runtime not verified. **Format:** two 30-minute blocks.

## Objective

Build a defensible incident timeline across application, Kubernetes and node observations. Escalate a platform symptom with useful evidence rather than an unbounded diagnostic dump.

## Prerequisites

K8S-200-01 through 03. Namespaced log/event access and approved read access to node conditions. Host access is optional and separately authorized. Do not install a monitoring stack to satisfy this lesson.

## Learn

Application logs, Kubernetes events, metrics and API audit events answer different questions. A log stream can be missing because a container never started, restarted, was removed, or logs were not retained. A node reporting Ready does not prove every application path is working. Time ranges, object UIDs and container identities prevent confusing a replacement workload with its predecessor.

## Practice

**Block A: collect narrowly.** Choose an exact lab Pod. Record its UID, node, container state, restart count, relevant events and current logs. When a previous container instance exists, inspect its previous logs. Bound the timestamps and record timezone. Inspect node conditions and allocated requests. Use `k top pods` only when a metrics API exists; record a missing API as an observability gap.

Create an evidence table with source, timestamp, affected identity/object, observation, limitation and hypothesis supported. Redact credentials and unrelated workload metadata before sharing.

**Block B: investigate and escalate.** The instructor supplies a namespaced startup failure plus a separate sanitized node-condition excerpt. Decide whether the excerpt explains the failure or is merely correlated. Test a competing hypothesis. Produce a five-line escalation: impact, exact scope, timeline, evidence, requested owner/action.

If authorized host read access exists, map kubelet and runtime logs to the same Pod/container identity. Read the `crictl` documentation and explain how runtime state differs from API desired state. Do not restart kubelet, delete runtime state or drain nodes during this lesson.

## Evidence and pass conditions

Present a coherent timeline with at least three evidence types, one limitation and one disproved hypothesis. Distinguish API events from a durable security audit trail. State whether the available observations support a conclusion or only justify further investigation.

## Reset and resume

No platform mutations are required. Restore any instructor-created namespaced workload fault. Store raw observations outside the public repository and retain only a sanitized learning summary. Record the next evidence source needed.

## Sources

- [Logging architecture](https://kubernetes.io/docs/concepts/cluster-administration/logging/)
- [Debugging nodes with crictl](https://kubernetes.io/docs/tasks/debug/debug-cluster/crictl/)
- [Resource metrics pipeline](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/)
