# ClusterForge

**Build it. Break it. Secure it. Explain it.**

ClusterForge is a hands-on Kubernetes engineering and security curriculum built around practical competency rather than passive coursework. Learners build real environments, introduce and diagnose failures, attack deliberately vulnerable configurations, apply defenses, and explain their reasoning as if working with a customer or engineering team.

## Learning model

Every module follows a common loop:

1. **Learn** the underlying system and mental model.
2. **Build** a working implementation.
3. **Break** it intentionally or investigate an injected failure.
4. **Diagnose** from evidence rather than guessing.
5. **Defend** the system where security is involved.
6. **Explain** the root cause, tradeoffs, and remediation clearly.

Troubleshooting exercises use a consistent evidence trail:

`SYMPTOM -> EVIDENCE -> HYPOTHESIS -> TEST -> ROOT CAUSE -> REMEDIATION -> VERIFICATION`

## Curriculum

### Kubernetes Engineering

- **K8S-100: Foundations** - architecture, workloads, services, storage, scheduling fundamentals, kubectl, and basic RBAC.
- **K8S-200: Field Engineering** - cluster lifecycle, CNI/CSI, scheduling, observability, failure analysis, and customer-style troubleshooting.
- **K8S-300: Kubernetes Security** - advanced RBAC, workload hardening, network policy, admission control, secrets, supply chain, runtime security, and incident response.
- **K8S-400: Kubernetes at Scale and Accelerated Compute** - runtime internals, advanced networking and scheduling, topology, GPUs, distributed compute, isolation, and observability.

### Security

- **SEC-100: Security Foundations** - trust boundaries, shared responsibility, identity, authorization, encryption, isolation, and foundational threat modeling.
- **SEC-200: Security Implementation and Operations** - workload identity, RBAC design, network enforcement, auditability, policy, encryption, and troubleshooting controls.
- **SEC-300: Security Architecture and Investigation** - architecture reviews, threat modeling, advanced isolation, incident investigation, AI workload security, and customer security patterns.
- **SEC-400: First-Principles Platform Security** - hardware through application trust, kernel primitives, zero trust, confidential computing, advanced threat modeling, and identity-chain analysis.
- **SEC-500+: Security Engineering and Attestation** - confidential-compute engineering, attestation, verifiable trust boundaries, and advanced platform security research.

The curriculum is vendor-neutral. Platform-specific implementations can be mapped onto these competencies without becoming dependencies of the public curriculum.

## 200/300 learning paths

The [integrated learning route](curriculum/levels-200-300.md) connects 24 lessons across four tracks:

| Track | Curriculum | Practical gate |
| --- | --- | --- |
| K8S-200 | [Kubernetes Field Engineering](curriculum/kubernetes/k8s-200/README.md) | [Unsuccessful release](assessments/k8s-200.md) |
| SEC-200 | [Security Implementation and Operations](curriculum/security/sec-200/README.md) | [Contractor access](assessments/sec-200.md) |
| K8S-300 | [Kubernetes Security](curriculum/kubernetes/k8s-300/README.md) | [Harden without breaking](assessments/k8s-300.md) |
| SEC-300 | [Security Architecture and Investigation](curriculum/security/sec-300/README.md) | [Customer security review](assessments/sec-300.md) |

Lessons use bounded work blocks, explicit prerequisites, evidence requirements and safe resume points. Read the [learning contract](docs/learning-contract.md), [fixture contract and synthetic case packets](curriculum/practicals/levels-200-300/README.md), and [assessment rubric](assessments/README.md).

**Current maturity:** authored Draft curriculum. Runnable provisioning/manifests are not bundled in this release. An instructor must supply and verify the specified live fixtures. Synthetic packets support analytical work only. No live cluster validation or learner completion is claimed.

## Candidate Zero

ClusterForge is dogfooded through **Candidate Zero**. Before a lab or assessment is treated as mature, it is completed as a learner would complete it and evaluated for ambiguity, realism, difficulty, hidden assumptions, and whether success demonstrates actual understanding.

Candidate Zero records evidence of competency, not just completion.

See [`docs/candidate-zero.md`](docs/candidate-zero.md) and the expanded [session record](templates/candidate-zero-session.md). Store real or company-specific evidence in an approved location outside the public repository.

## Start here

The first learning path begins with [`curriculum/kubernetes/k8s-100/day-01.md`](curriculum/kubernetes/k8s-100/day-01.md): **From API Request to Running Pod**.

With those fundamentals demonstrated, continue to the [200/300 route](curriculum/levels-200-300.md). Missing public commits do not establish an unfinished lesson; use a current learner report or evidence checkpoint.

## Certification alignment

ClusterForge is not affiliated with or endorsed by the Linux Foundation or CNCF. The Kubernetes tracks develop competencies that overlap with KCNA, CKA, CKAD and CKS while extending into troubleshooting, investigation, architecture and accelerated compute.

The [certification crosswalk](docs/certification-map.md) records official-domain overlap and explicit remaining qualification gaps. Curriculum completion is not a claim of external certification or exam readiness.

## Validation

Run the [offline curriculum checks](docs/validation-200-300.md). They validate structure and references, not a live cluster or learner competency.

## Status

ClusterForge is under active development. New material is Draft until exercised and reviewed through the Candidate Zero process.

## License

Apache License 2.0. See [`LICENSE`](LICENSE).
