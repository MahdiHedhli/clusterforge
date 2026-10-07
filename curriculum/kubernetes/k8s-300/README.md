# K8S-300: Kubernetes Security

**Outcome:** explain Kubernetes attack paths, implement layered controls, and validate both protection and application behavior.

**Status:** Draft curriculum. Runtime not verified. No learner competency is asserted.

## Entry gate

Demonstrate K8S-200 workload/network troubleshooting and SEC-200 identity/control fundamentals, or equivalent evidence. The entry gate is practical competence, not possession of an external certificate. Read the [learning contract](../../../docs/learning-contract.md).

Use the [shared practical](../../practicals/levels-200-300/README.md) for namespaced work. Node hardening, admission-engine installation, audit configuration and runtime sensors require explicit administrator authorization. A namespace guard is not a security sandbox.

## Lessons

| ID | Lesson | Suggested blocks | Evidence product |
| --- | --- | --- | --- |
| K8S-300-01 | [Identity, RBAC and attack paths](01-rbac.md) | 3 x 30 minutes | Identity-to-capability graph |
| K8S-300-02 | [Workload hardening and admission](02-hardening.md) | 3 x 30 minutes | Positive/negative admission tests |
| K8S-300-03 | [Network and egress enforcement](03-network-policy.md) | 3 x 30 minutes | Reproducible allow/deny matrix |
| K8S-300-04 | [Secrets and software supply chain](04-secrets-supply-chain.md) | 3 x 30 minutes | Artifact and secret trust records |
| K8S-300-05 | [Node, runtime and detection boundaries](05-runtime.md) | 3 x 30 minutes | Sensor coverage and safe event test |
| K8S-300-06 | [Kubernetes incident investigation](06-investigation.md) | 3 x 30 minutes | Timeline, containment and retest |

## Practical gate

The [K8S-300 assessment](../../../assessments/k8s-300.md) tests hardening without breaking a legitimate workload. It requires actual allow and deny observations for live controls. Tabletop evidence is accepted only for the explicitly labeled analytical portion; it does not replace runtime qualification.

## Scope and progression

This track focuses on Kubernetes mechanisms. SEC-300 asks whether those mechanisms satisfy a customer's end-to-end design and investigation requirements. The [integrated route](../../levels-200-300.md) identifies reusable evidence and avoids treating the two tracks as duplicate courses.

The [certification mapping](../../../docs/certification-map.md) identifies CKS domain overlap and remaining hands-on gaps. A checklist, security scanner score or green policy object is not proof of either a secure platform or CKS readiness.
