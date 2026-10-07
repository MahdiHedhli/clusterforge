# K8S-300-06: Kubernetes incident investigation

**Status:** Draft. Runtime not verified. **Format:** three 30-minute blocks.

## Objective

Reconstruct an incident from bounded evidence, separate observed actions from inferred intent, and propose containment that preserves evidence and legitimate service.

## Prerequisites

SEC-200-05 and K8S-300-01 through 05, with unavailable live sensor work explicitly recorded. Use the [synthetic incident packet](../../practicals/levels-200-300/incident.json) for the analytical path. Live validation requires an administrator-approved audit and runtime collection path.

## Learn

API audit events describe requests and their recorded outcomes; they do not automatically reveal every action inside a process or prove data left the environment. A successful API read is not the same as proven external exfiltration. Bind events to object UIDs and identities where available, account for missing stages/time ranges, and label confidence.

Containment can alter the evidence. Decide what to capture first and which risk justifies an immediate interruption. Deleting a Pod does not necessarily revoke every credential already copied from it or remove the controller that will recreate it.

## Practice

**Block A: establish facts.** Read the packet without the instructor notes. Build a timeline separating actor identity, attempted action, outcome and source. Identify one denied action, one authorized but concerning action, and an important unanswered question. Do not invent packet contents or a network transfer event.

**Block B: design containment.** Propose the smallest reversible identity, workload or network change that interrupts the supported path. State owner, expected effect, operational risk and rollback. Preserve original evidence and hash the local packet before annotating a copy. In tabletop mode, do not claim the proposal was executed.

**Block C: verify and communicate.** In an approved live variant, verify that the blocked operation fails and a required legitimate operation still succeeds. In the packet variant, identify the evidence needed to perform those tests and mark runtime verification outstanding. Prepare a three-minute update that separates facts, likely interpretations and unknowns.

## Evidence and pass conditions

Submit a timeline, competing hypothesis, containment decision, credential-lifecycle analysis and validation plan/results. Analytical credit requires explicit uncertainty. Live incident-control credit requires the actual negative and positive retests. Missing audit coverage is a finding, not proof of no activity.

## Reset and resume

Retain evidence in the approved location, remove synthetic resources only after the exercise owner releases them, and document any temporary restriction remaining. Do not publish raw telemetry or real identity data.

## Sources

- [Kubernetes auditing](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/)
- [ServiceAccount credential behavior](https://kubernetes.io/docs/concepts/security/service-accounts/)
- [MITRE ATT&CK Containers matrix](https://attack.mitre.org/matrices/enterprise/containers/)
