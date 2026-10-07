# SEC-300: Security Architecture and Investigation

**Outcome:** review an end-to-end customer design, identify evidence-backed security gaps, investigate incidents and defend tradeoffs without overstating platform guarantees.

**Status:** Draft curriculum. Runtime not verified. No learner completion is asserted.

## Entry gate

Demonstrate SEC-200 control design/verification and K8S-200 troubleshooting. For implementation sign-off, add K8S-300 identity, workload, network and evidence competencies. Architecture reading may begin earlier, but does not replace those practical prerequisites.

Read the [learning contract](../../../docs/learning-contract.md). This is a development target, not a fixed-date finish line. Reuse validated observations from other tracks and add the architecture or investigation reasoning required here.

## Lessons

| ID | Lesson | Suggested blocks | Evidence product |
| --- | --- | --- | --- |
| SEC-300-01 | [Architecture review and discovery](01-architecture.md) | 3 x 30 minutes | Requirements, data flows and review findings |
| SEC-300-02 | [Threat models and attack paths](02-threat-modeling.md) | 3 x 30 minutes | Prioritized threat/control/evidence matrix |
| SEC-300-03 | [Tenant and accelerator trust boundaries](03-isolation.md) | 3 x 30 minutes | Isolation claims with proof limits |
| SEC-300-04 | [AI workload and artifact integrity](04-ai-workloads.md) | 3 x 30 minutes | Dataset/model/checkpoint trust chain |
| SEC-300-05 | [Incident investigation and leadership](05-incident-response.md) | 3 x 30 minutes | Decision log, timeline and customer updates |
| SEC-300-06 | [Assurance, exceptions and architecture defense](06-assurance.md) | 3 x 30 minutes | Defensible recommendation and evidence plan |

## Practical gate

Complete [The customer security review](../../../assessments/sec-300.md). The capstone combines discovery, architecture, threat modeling, a selected live-control demonstration and an incident/change inject. A design-only pass is recorded as analytical credit, not full implementation qualification.

Use the [fictional customer brief](../../practicals/levels-200-300/customer.json) and [synthetic incident packet](../../practicals/levels-200-300/incident.json). These are public teaching fixtures, not descriptions of any company's infrastructure.

## Boundaries and progression

Namespaces, policy objects and lab tests do not prove every tenant boundary. GPU, storage, network-offload and operator-access claims require technology-specific evidence and explicit ownership. First-principles hardware/firmware analysis and confidential-compute engineering remain extensions into SEC-400/500+, not presumed SEC-300 mastery.

The [certification mapping](../../../docs/certification-map.md) labels these architecture and communication skills as additional to Kubernetes exam domains, not equivalent to an external certification.
