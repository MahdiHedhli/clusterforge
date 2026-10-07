# K8S-200: Kubernetes Field Engineering

**Outcome:** investigate workload and platform symptoms, make the smallest justified repair, and explain the result with evidence.

**Status:** Draft curriculum. Runtime not verified. No learner completion is implied.

## Entry gate

Demonstrate the K8S-100 fundamentals: trace Deployment -> ReplicaSet -> Pod, interpret readiness, inspect a Service and its EndpointSlices, target the intended context/namespace, and distinguish an infrastructure setup defect from an injected exercise fault. An existing competency record can satisfy this gate; repeating a lesson is not mandatory.

Start with the [learning contract](../../../docs/learning-contract.md) and [shared practical environment](../../practicals/levels-200-300/README.md). A healthy cluster is a prerequisite, not an undisclosed examination. Namespace-level exercises do not authorize node or control-plane mutations.

## Lessons

| ID | Lesson | Suggested blocks | Evidence product |
| --- | --- | --- | --- |
| K8S-200-01 | [Rollouts and evidence-driven diagnosis](01-rollouts.md) | 2 x 30 minutes | Incident timeline and verified recovery |
| K8S-200-02 | [Scheduling, resources and probes](02-scheduling.md) | 3 x 30 minutes | Pending-versus-unready decision tree |
| K8S-200-03 | [Services, DNS and network paths](03-networking.md) | 3 x 30 minutes | Client-to-backend path with test results |
| K8S-200-04 | [Storage and stateful recovery](04-storage.md) | 3 x 30 minutes | PVC lifecycle and data-preservation plan |
| K8S-200-05 | [Observability and node triage](05-observability.md) | 2 x 30 minutes | Layered evidence bundle and escalation |
| K8S-200-06 | [Lifecycle, packaging and recovery planning](06-lifecycle.md) | 3 x 30 minutes | Reviewed change and restore plan |

These are planning estimates, not deadlines. Stop at a safe checkpoint between work commitments. Separate administrator-supervised rebuild/restore work requires its own uninterrupted window.

## Practical gate

Complete the [K8S-200 assessment](../../../assessments/k8s-200.md). The operator gate evaluates bounded application recovery and platform reasoning. It does not certify that a learner has performed a real control-plane upgrade or etcd restoration. Track those qualifications separately.

## Relationship to other tracks

K8S-200 explains why the system is behaving this way. SEC-200 applies operational security controls. K8S-300 hardens the Kubernetes mechanisms; SEC-300 evaluates the larger customer design and incident implications. Reuse relevant evidence across tracks, but complete the additional reasoning or negative tests a second track requires.

See the [integrated route](../../levels-200-300.md), [assessment rubric](../../../assessments/README.md), and [certification mapping](../../../docs/certification-map.md). CKA and CKAD alignment is partial; it is not an exam-readiness claim.
