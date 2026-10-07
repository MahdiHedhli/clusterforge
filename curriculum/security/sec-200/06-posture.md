# SEC-200-06: Posture reviews and exceptions

**Status:** Draft. Runtime not verified. **Format:** two 30-minute blocks.

## Objective

Answer a security-control question with scoped evidence, identify unsupported assurances, and manage a temporary exception without silently making it permanent.

## Prerequisites

SEC-200-01 through 05 or equivalent. Use synthetic customer requirements and your lab observations. Real internal policies or customer questionnaires belong in an approved internal workspace, not this public repository.

## Learn

A baseline configuration, a scanner result, a control implementation and an independent assurance statement are different evidence types. A control can be present but ineffective because of an exception, an untested path or a missing operational owner. Checklists help organize review but cannot establish complete security posture.

Use the response structure: claim -> scope -> evidence -> limitation -> owner -> next test. Prefer an honest partial answer over an unsupported yes/no assurance.

## Practice

**Block A: review five claims.** Evaluate: "developers cannot read production credentials," "workload traffic is encrypted," "every administrative action is attributable," "other teams cannot access our storage," and "only approved artifacts run." For each, identify the control layer, owner, actual lab evidence and remaining gap. Do not turn a namespace-level observation into a platform-wide guarantee.

**Block B: handle an exception.** A fictional team needs temporary artifact-download access to complete a test. Write the purpose, narrow destinations, authorized identity, duration, compensating controls, approver, verification and removal owner. Define a test that proves the exception was removed while normal work still functions. Keep this as a design unless the exact synthetic lab change is separately approved.

Draft a five-line customer answer for the weakest-supported claim. Include what is known, what remains unverified, and who needs to validate it. Avoid claiming legal or regulatory compliance from a lab or product certification.

## Evidence and pass conditions

Provide a five-row claim/evidence register, a complete exception record, and a customer response with no invented guarantees. Pass requires a named verification gap and an actionable owner, not just a list of security products.

## Reset and resume

No mutations are required. Any approved live exception must be reversed and retested before closure. Record the control claim that needs the next practical test.

## Sources

- [Kubernetes application security checklist](https://kubernetes.io/docs/concepts/security/application-security-checklist/)
- [Kubernetes multi-tenancy](https://kubernetes.io/docs/concepts/security/multi-tenancy/)
- [NIST Zero Trust Architecture publication overview](https://csrc.nist.gov/pubs/sp/800/207/final)
