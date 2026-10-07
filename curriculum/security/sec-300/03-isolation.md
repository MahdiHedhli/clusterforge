# SEC-300-03: Tenant and accelerator trust boundaries

**Status:** Draft. Runtime not verified. **Format:** three 30-minute blocks.

## Objective

Evaluate isolation across identity, namespace, node, network, storage and accelerator layers, and state precisely what a lab observation can establish.

## Prerequisites

SEC-300-01/02 and K8S-300 identity/network/hardening evidence. No GPU hardware is required for the analytical portion. Any hardware test requires an approved disposable accelerator environment and model-specific documentation.

## Learn

A namespace organizes scope but is not, by itself, a complete hostile-tenant boundary. Scheduling, runtime privilege, shared kernel access, network enforcement and storage authorization all affect the design. Quotas and QoS govern consumption; they do not automatically establish confidentiality.

GPU sharing modes must be distinguished. NVIDIA documents that time-slicing does not provide the memory and fault isolation offered by MIG. That distinction is not a blanket guarantee that every MIG configuration, GPU model, interconnect or operator path satisfies a particular tenant threat model.

## Practice

**Block A: isolation matrix.** For two fictional tenants, list each asset and boundary, the enforcement component, privileged bypass actors, positive/negative test and residual risk. Include API identity, workload creation, node placement, east-west traffic, storage access and model artifacts.

**Block B: demonstrate only what is local.** Reuse or perform the approved RBAC and NetworkPolicy tests. Explain why a denied API Secret read does not establish that a process cannot receive data via a permitted volume mount. Review storage authorization separately from PVC access mode and storage quota. Do not create privileged Pods or access another tenant's real data to demonstrate a concern.

**Block C: accelerator and offload review.** Compare dedicated GPU assignment, time-slicing, MIG and a separately attested confidential-compute design as different options. List hardware/firmware/driver/runtime evidence required before making claims about memory clearing, DMA/RDMA, interconnect exposure or operator access. For network-offload enforcement, identify control-plane owner, firmware trust and fail-open/fail-closed questions without claiming to reproduce a provider's implementation.

Recommend a tenancy option for the fictional customer's highest-value asset and state what would cause you to reject that recommendation.

## Evidence and pass conditions

Submit the isolation matrix, two reused or new local test results, and an accelerator evidence-request list. Pass requires explicit distinctions between resource sharing, isolation and attestation. Local namespace tests must not be presented as silicon-level assurance.

## Reset and resume

Restore any namespaced test controls and record unqualified hardware claims as questions. No GPU, node, DPU or storage-backend mutation is authorized by this lesson.

## Sources

- [Kubernetes multi-tenancy](https://kubernetes.io/docs/concepts/security/multi-tenancy/)
- [NVIDIA GPU time-slicing and isolation limitations](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/gpu-sharing.html)
- [Persistent-volume access modes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
