# K8S-200-02: Scheduling, resources and probes

**Status:** Draft. Runtime not verified. **Format:** three 30-minute blocks.

## Objective

Distinguish an unschedulable Pod from a running-but-unready container and a restarting container. Repair the actual constraint rather than removing every safeguard.

## Prerequisites

K8S-200-01, the [shared practical](../../practicals/levels-200-300/README.md), and permission to inspect node metadata. Metrics Server is optional; its absence must not be reported as zero resource usage.

## Learn

Requests influence scheduling; current utilization alone does not determine whether a Pod fits. Limits govern runtime resource consumption. Readiness, liveness and startup probes answer different questions. A readiness failure is not itself an instruction to restart the container. Tolerating a taint permits consideration of a node; it does not force placement there.

Use the path admission -> scheduling -> image/container startup -> readiness -> application response. Locate the first failed transition before proposing a fix.

## Practice

**Block A: Pending.** Record requests, limits, node assignments and events for the baseline. Inspect node allocatable resources and labels. An instructor introduces an impossible Pod-level node selector or an excessive resource request on `cf-web`. Read the FailedScheduling evidence and compare it with the declared constraint. Do not remove control-plane taints, raise quotas, or modify node labels as a shortcut.

**Block B: running but unavailable.** In a fresh baseline, investigate a probe fault. Compare `k get pods`, `k describe pod <exact-pod>`, restart counts and Service EndpointSlice conditions. Contrast a failing readiness probe with an application process that exits. Do not disable probes solely to produce a green status.

**Block C: explain placement and capacity.** Design a two-replica placement policy for two workers. Discuss soft versus hard anti-affinity, what happens when only one worker remains, and whether the intended availability rule is satisfiable. Inspect a namespaced ResourceQuota or LimitRange only when one exists. Predict how quota rejection differs from scheduler rejection.

Do not create a memory-exhaustion experiment on the shared host. A controlled OOM exercise requires a separately bounded fixture and resource budget.

## Evidence and pass conditions

Submit one Pending investigation and one readiness investigation, including the decisive event or condition, the minimal correction and a successful application test. Explain why CPU usage below capacity did not disprove a scheduling constraint. Include a proposed placement policy with its degraded-capacity tradeoff.

## Reset and resume

Restore every exercise-added selector, request or probe field explicitly. Reapplying a manifest that omits an imperatively added field may not remove that field. Verify both replica availability and application response. Record any remaining capacity assumption.

## Sources

- [Resource management](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
- [Liveness, readiness and startup probes](https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/)
- [Taints and tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)
