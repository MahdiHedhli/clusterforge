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

## Candidate Zero

ClusterForge is dogfooded through **Candidate Zero**. Before a lab or assessment is treated as mature, it is completed as a learner would complete it and evaluated for ambiguity, realism, difficulty, hidden assumptions, and whether success demonstrates actual understanding.

Candidate Zero records evidence of competency, not just completion.

See [`docs/candidate-zero.md`](docs/candidate-zero.md).

## Start here

The first learning path begins with [`curriculum/kubernetes/k8s-100/day-01.md`](curriculum/kubernetes/k8s-100/day-01.md): **From API Request to Running Pod**.

## Certification alignment

ClusterForge is not affiliated with or endorsed by the Linux Foundation or CNCF. The Kubernetes tracks are designed to develop practical competencies that overlap with common industry certification domains, including KCNA, CKA, CKAD, and CKS, while extending beyond exam preparation into troubleshooting, security investigation, architecture, and accelerated compute.

## Status

ClusterForge is under active development. Early curriculum and labs should be treated as Candidate Zero material until they have been repeatedly exercised and reviewed.

## License

Apache License 2.0. See [`LICENSE`](LICENSE).
