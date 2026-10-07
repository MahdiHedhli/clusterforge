# SEC-300-06: Assurance, exceptions and architecture defense

**Status:** Draft. Runtime not verified. **Format:** three 30-minute blocks.

## Objective

Defend an architecture against explicit customer requirements, distinguish product capability from supported assurance, and translate gaps into engineering work.

## Prerequisites

SEC-300-01 through 05 and the [fictional customer brief](../../practicals/levels-200-300/customer.json). Its retention and availability targets are teaching requirements, not legal mandates. Real regulatory interpretation belongs with qualified compliance/legal owners.

## Learn

An assurance claim needs scope, evidence, ownership and limitations. Platform certification, customer configuration and the customer's overall compliance obligations are different things. Do not infer a provider's current certifications or contract terms from a generic lab.

An engineering-ready gap states current behavior, required behavior, affected workflow, security consequence, acceptance test and owner. "Improve security" is not an actionable requirement.

## Practice

**Block A: requirement mapping.** Map each fictional customer requirement to preventive, detective and recovery controls. Attach actual lab evidence where relevant and label architecture-only assertions as unverified. Identify dependencies on platform owners, identity administrators, storage operators and application teams. Do not copy internal answers into public material.

**Block B: design tradeoffs.** Compare two architectures using the same dimensions: isolation, identity, data protection, observability, operational complexity, recovery and evidence gaps. Record assumptions instead of inventing cloud-product defaults or prices. Present one risk acceptance and one engineering gap with a testable acceptance condition.

**Block C: oral defense.** The instructor changes two requirements, such as restricted outbound access and urgent contractor troubleshooting. Update the design and exception process without resorting to an all-powerful shared identity. Explain which goals conflict, what evidence would settle the choice, and who can accept residual risk.

Close with a one-page recommendation: scope, selected design, top risks, evidence demonstrated, outstanding qualifications and next actions. Separate the statement "we tested this in a lab" from "this deployed customer environment meets the requirement."

## Evidence and pass conditions

Provide a complete requirement/control/evidence matrix, an architecture comparison, one actionable engineering issue and a defensible recommendation. Pass requires explicit owners for unresolved claims and no invented compliance guarantees. Use the common rubric's communication and safety gates.

## Reset and resume

No platform mutation is required. Preserve the decision history and record the next highest-value verification activity. Keep company-specific assurance evidence in an approved internal system.

## Sources

- [NIST Zero Trust Architecture publication overview](https://csrc.nist.gov/pubs/sp/800/207/final)
- [Kubernetes multi-tenancy](https://kubernetes.io/docs/concepts/security/multi-tenancy/)
- [Kubernetes application security checklist](https://kubernetes.io/docs/concepts/security/application-security-checklist/)
