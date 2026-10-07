# SEC-300-01: Architecture review and discovery

**Status:** Draft. Runtime not verified. **Format:** three 30-minute blocks.

## Objective

Turn an incomplete customer brief into a testable architecture review, separating facts, assumptions, requirements and open questions.

## Prerequisites

SEC-200 fundamentals and K8S-200 troubleshooting. Use the [fictional customer brief](../../practicals/levels-200-300/customer.json). Keep real customer discovery and internal platform details outside the public repository.

## Learn

Start with assets and allowed workflows, not a catalog of tools. A review needs the administration path, workload path, data path and recovery path. Each crosses identities and ownership boundaries. A design is incomplete when it says a control exists without identifying who configures it, who can bypass it and how it will be verified.

Use a decision register: requirement, proposed control, owner, evidence, alternative, tradeoff and unresolved dependency. Review scope before recommending changes.

## Practice

**Block A: discovery.** Ask the instructor six targeted questions about the fictional customer's data sensitivity, administrative roles, workload tenancy, external artifact access, availability needs and incident ownership. Distinguish a business requirement from a preferred implementation. Do not silently supply missing platform guarantees.

**Block B: architecture.** Draw identity issuer -> API -> workload -> storage/artifact access and mark administration, node/runtime, network and data boundaries. Include audit collection and recovery. Identify where plaintext, privileged credentials and model artifacts exist. Show at least two deployment options, such as a shared cluster with bounded namespaces versus separate clusters/nodes, and state the evidence each choice requires.

**Block C: review finding.** Produce five prioritized findings. Each needs an affected asset, plausible path, existing control, missing evidence or defect, recommendation, owner and verification method. Select one finding that can be tested with a namespaced lab and one that needs platform-owner evidence. Do not treat the inability to test hardware isolation locally as proof it is absent.

Explain the recommendation in five minutes to a platform engineer and then in one minute to a non-specialist stakeholder.

## Evidence and pass conditions

Submit a requirements register, annotated data-flow diagram, two-option comparison and five findings. Pass requires every major recommendation to trace to a requirement or threat. Unsupported assurance claims and unexplained product-name substitutions must be corrected before sign-off.

## Reset and resume

This is a design exercise and authorizes no infrastructure mutation. Save assumptions and the next unanswered question. Record which proposed controls still need implementation evidence.

## Sources

- [Kubernetes multi-tenancy](https://kubernetes.io/docs/concepts/security/multi-tenancy/)
- [NIST Zero Trust Architecture publication overview](https://csrc.nist.gov/pubs/sp/800/207/final)
