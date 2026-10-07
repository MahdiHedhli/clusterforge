# SEC-300-05: Incident investigation and leadership

**Status:** Draft. Runtime not verified. **Format:** three 30-minute blocks.

## Objective

Coordinate an evidence-led investigation, select proportionate containment, and communicate decisions without inventing impact or certainty.

## Prerequisites

K8S-300-06 analytical skills and SEC-300 architecture/threat modeling. Use the [synthetic incident packet](../../practicals/levels-200-300/incident.json). Real customer incidents require their own authorization and response procedures.

## Learn

Incident leadership includes declaring scope, assigning owners, recording decisions, preserving evidence and keeping service recovery distinct from security remediation. An investigator should separate "the API returned success," "the resource was accessed," "the data was copied" and "the data left the environment." Each requires supporting evidence.

Use a decision log with timestamp, known facts, options, chosen action, approver, anticipated impact and reversal condition. A recommendation is not an executed action.

## Practice

**Block A: triage.** Preserve and hash the packet. Build a timeline of identity, API and process observations. State affected assets, demonstrated actions, plausible paths and unknown scope. Choose the next three evidence requests by how much uncertainty they resolve. Account for missing network-transfer evidence explicitly.

**Block B: containment conference.** The instructor plays application owner, infrastructure owner and security reviewer. Propose identity, workload and network actions in order. Explain credential expiry/revocation limits, controller reconciliation, evidence loss and service impact. Select the minimum justified action and define a legitimate-operation check and an adversary-path check. Do not perform live changes in tabletop mode.

**Block C: changed information.** Receive an inject: the observed shell was approved debugging, the suspected identity is shared by several workloads, or the log sink has a collection gap. Revise the hypothesis and containment proposal. Deliver a customer update that includes impact known so far, actions actually taken, next actions and the next update trigger, without a fabricated completion time.

## Evidence and pass conditions

Submit the timeline, facts/inferences/unknowns table, decision log, evidence-preservation plan and customer update. Pass requires adapting to contradictory evidence and naming the operational tradeoff. Live containment credit requires separate controlled execution and retest records; the packet does not provide them.

## Reset and resume

Record unresolved investigation questions and owners. Keep originals unchanged and annotations separate. Any live variant must restore temporary controls only after the exercise owner approves closure.

## Sources

- [Kubernetes auditing](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/)
- [MITRE ATT&CK Containers matrix](https://attack.mitre.org/matrices/enterprise/containers/)
- [Kubernetes ServiceAccounts](https://kubernetes.io/docs/concepts/security/service-accounts/)
