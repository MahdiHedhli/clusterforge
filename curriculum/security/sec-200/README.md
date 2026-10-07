# SEC-200: Security Implementation and Operations

**Outcome:** implement, troubleshoot and explain cloud-native security controls, including their owners, dependencies and evidence limitations.

**Status:** Draft curriculum. Runtime not verified. No learner completion is implied.

## Entry gate

Demonstrate SEC-100 trust-boundary and shared-responsibility concepts and K8S-100 workload/identity fundamentals. Follow the [learning contract](../../../docs/learning-contract.md). K8S-200 can be studied alongside this track; matching practical evidence may be reused.

## Lessons

| ID | Lesson | Suggested blocks | Evidence product |
| --- | --- | --- | --- |
| SEC-200-01 | [Identity lifecycle and federation](01-identity.md) | 2 x 30 minutes | Authentication/provisioning/authorization chain |
| SEC-200-02 | [Least-privilege operations](02-authorization.md) | 2 x 30 minutes | Role design and authorization test matrix |
| SEC-200-03 | [Segmentation and private connectivity](03-segmentation.md) | 3 x 30 minutes | Data-flow and reachability matrix |
| SEC-200-04 | [Encryption, credentials and rotation](04-encryption.md) | 3 x 30 minutes | Key/secret lifecycle with verified boundaries |
| SEC-200-05 | [Auditability and evidence operations](05-auditability.md) | 2 x 30 minutes | Telemetry coverage and collection contract |
| SEC-200-06 | [Posture reviews and exceptions](06-posture.md) | 2 x 30 minutes | Evidence-backed control response and exception |

## Practical gate

Complete the [SEC-200 assessment](../../../assessments/sec-200.md). The gate requires a working authorized use case, a relevant rejected use case, a clear identity chain and an honest evidence record. A control being configured is not equivalent to the control being effective.

The [practical contract and packets](../../practicals/levels-200-300/README.md) define the instructor-supplied namespaced environment and provide synthetic identity/incident data. Runnable manifests and provisioning are not bundled. The material does not install an identity provider, KMS, audit sink, CNI, runtime sensor or external secrets platform. Mark missing live dependencies explicitly instead of inventing implementation evidence.

## Cross-credit and scope

SEC-200-02 evidence can support K8S-300-01 after the learner adds indirect-capability analysis. SEC-200-03 supports K8S-300-03 after bidirectional and implementation-specific tests. SEC-200-05 supports investigation after the learner establishes a timeline and containment logic. Reuse observations, not unearned scores.

See the [integrated route](../../levels-200-300.md) and [certification mapping](../../../docs/certification-map.md). This is broader than a Kubernetes certification and does not grant compliance status.
