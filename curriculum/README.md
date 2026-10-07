# ClusterForge Curriculum Roadmap

ClusterForge develops Kubernetes engineering and security competency in parallel. The levels describe increasing capability, not course length or organizational seniority.

## Authored 200/300 curricula

Start with the [integrated route](levels-200-300.md), then select [K8S-200](kubernetes/k8s-200/README.md), [K8S-300](kubernetes/k8s-300/README.md), [SEC-200](security/sec-200/README.md), or [SEC-300](security/sec-300/README.md).

Each track contains six lessons and a practical gate. These are authored Draft curricula, with fixture contracts and synthetic analytical packets. Live runtime qualification and learner evidence are separate. The release does not bundle runnable provisioning or live-lab manifests.

## Kubernetes track

### K8S-100: Foundations

Outcome: operate common Kubernetes workloads and explain the architecture and reconciliation model.

Core domains include control-plane architecture, API objects, Pods, Deployments, StatefulSets, DaemonSets, Jobs, Services, DNS, ConfigMaps, Secrets, storage fundamentals, resource requests and limits, probes, scheduling fundamentals, kubectl, and basic RBAC.

### K8S-200: Field Engineering

Outcome: diagnose and remediate realistic cluster and workload failures.

Core domains include cluster lifecycle, CNI and CSI fundamentals, scheduling constraints, affinity, taints and tolerations, observability, node and workload failures, DNS, networking, storage, resource pressure, and technical communication.

### K8S-300: Kubernetes Security

Outcome: identify, exploit in controlled labs, detect, and remediate Kubernetes security weaknesses.

Core domains include RBAC escalation, workload identity, workload hardening, network policy, admission control, secrets, software supply chain, runtime detection, eBPF observability, node security, container isolation, attack paths, and incident response.

### K8S-400: At Scale and Accelerated Compute

Outcome: reason about Kubernetes behavior in high-performance, large-scale, and accelerator-heavy environments.

Core domains include CRI/container runtime internals, advanced networking, scheduling and topology, failure domains, performance, device plugins, GPU operators, accelerator scheduling and isolation, RDMA concepts, distributed workloads, and accelerator observability.

## Security track

### SEC-100: Security Foundations

Outcome: identify fundamental trust boundaries and security responsibilities in cloud-native infrastructure.

### SEC-200: Security Implementation and Operations

Outcome: implement and troubleshoot identity, authorization, network, policy, encryption, and audit controls.

### SEC-300: Security Architecture and Investigation

Outcome: conduct security architecture reviews, threat-model complex workloads, investigate incidents, and design defensible customer security patterns.

### SEC-400: First-Principles Platform Security

Outcome: reason from hardware and firmware through kernel, orchestration, identity, storage, networking, accelerators, and application trust boundaries.

### SEC-500+: Security Engineering and Attestation

Outcome: contribute to advanced platform security, confidential-compute architectures, attestation systems, and customer-verifiable trust.

## Assessment model

ClusterForge uses knowledge checks, hands-on labs, troubleshooting incidents, adversarial scenarios, architecture exercises and technical explanation. Higher levels increasingly favor practical and scenario-based evidence over recall. See the [shared rubric](../assessments/README.md) and keep guided practice separate from independent assessment.

## External certification relationship

The curriculum overlaps with competencies found in KCNA, CKA, CKAD and CKS. ClusterForge is not an exam-prep product and is not affiliated with or endorsed by CNCF or the Linux Foundation. The [crosswalk](../docs/certification-map.md) identifies overlap and remaining hands-on gaps rather than claiming complete exam coverage.
