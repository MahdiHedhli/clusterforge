# K8S-200-06: Lifecycle, packaging and recovery planning

**Status:** Draft. Runtime not verified. **Format:** three 30-minute planning blocks; a separate approved administrator window for execution.

## Objective

Design a repeatable cluster change and recovery procedure, identify the blast radius of extensions, and distinguish a reviewed plan from demonstrated rebuild/restore skill.

## Prerequisites

K8S-200-01 through 05. A version inventory, provider-specific recovery ownership and access to version-matched official documentation. Live execution requires a separate disposable cluster, backups, out-of-band access and explicit approval. The namespace-scoped practical does not grant that approval.

## Learn

Cluster lifecycle crosses host, runtime, control-plane, networking and storage boundaries. A PodDisruptionBudget constrains voluntary evictions through supported mechanisms; it is not protection against every failure and does not create spare capacity. A VM snapshot is not automatically an application-consistent or independently tested cluster restore.

## Practice

**Block A: packaging review.** Render a small application overlay locally with Kustomize and review the resulting namespace, images, labels and resources. Inspect a Helm chart locally using its documented rendering command; do not install it. Inventory namespaced versus cluster-scoped objects and note CRDs, webhooks, RBAC and controller permissions. Explain why an operator installation is more than adding a workload.

**Block B: lifecycle plan.** Write an ordered kubeadm build/upgrade plan for the exact installed and target versions. Cover host prerequisites, API access, certificates, runtime/CNI compatibility, backup, maintenance impact, control-plane sequencing, workers, and post-change tests. For a managed cluster, substitute the supported provider workflow and state what the customer cannot operate directly. Do not paste commands for a different release or assume skipped minor versions are supported.

**Block C: recovery rehearsal on paper.** Define an injected failure, stop conditions, restore destination, control-plane recovery owner, data recovery owner and validation checks. Include the loss of the only control-plane node and the loss of a storage backend as different cases. Explain what an HA design would change and what a single-host VM lab cannot establish.

Optional live extension: an authorized instructor supervises a fresh build and a documented restore on a separate disposable environment. Capture actual outputs and restore verification. Leave this extension NOT_RUN until it occurs.

## Evidence and pass conditions

Submit rendered-object review, change sequence, recovery decision tree and verification checklist. The planning gate can pass after review. Full lifecycle implementation credit requires separate live evidence; it is not inferred from this plan or the operator capstone.

## Reset and resume

Remove only local render outputs from the scratch directory. No cluster changes occur in the planning path. Record approvals and environmental prerequisites still needed for a live rehearsal.

## Sources

- [Upgrading kubeadm clusters](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)
- [Disruption budgets](https://kubernetes.io/docs/tasks/run-application/configure-pdb/)
- [Kustomize](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/)
- [Helm template](https://helm.sh/docs/helm/helm_template/)
