# K8S-200-04: Storage and stateful recovery

**Status:** Draft. Runtime not verified. **Format:** three 30-minute blocks.

## Objective

Trace claim provisioning and mount failures while preserving data. Distinguish a workload scheduling problem from a storage-class, binding, attachment or filesystem-permission problem.

## Prerequisites

K8S-200-02 and an administrator-approved disposable StorageClass. No production export, shared NAS data, hostPath volume or existing customer PVC may be used. Without a suitable provisioner, complete the design exercise and mark the live storage portion BLOCKED, not passed.

## Learn

A PVC is a request for storage; a PV represents provisioned storage. StorageClass binding mode can defer provisioning until a consumer is scheduled. ReadWriteOnce refers to access from one node, not necessarily one Pod. Reclaim policy changes the consequences of deleting a claim. Storage access modes are not a complete tenant-authorization model.

Before each mutation, answer: what data exists, who owns it, and what operation could destroy it?

## Practice

**Block A: inspect the contract.** Record the approved class's provisioner, binding mode, reclaim policy and relevant topology constraints. Draft a 1 GiB PVC with that explicit class and a non-privileged writer Pod in `cf-lab-200-300`. Obtain instructor review before applying. Write only a synthetic marker and record its hash. Recreate the writer Pod, not the claim, and verify the marker remains.

**Block B: diagnose a fresh failure.** The instructor supplies a separate, empty claim with an unavailable class, an unsatisfied topology requirement or a writer-permission defect. Inspect PVC events, Pod events, selected node and the provisioner's relevant evidence. An absent PV is a symptom to explain, not a reason to create a random hostPath PV. Do not edit an immutable claim field and assume it must succeed. Replacing an empty failed claim requires explicit confirmation that it contains no data.

**Block C: recovery design.** Explain the difference between replica count, a storage snapshot, backup and a tested restore. Propose an application-consistent recovery test with a separate destination and integrity check. Identify who owns encryption, export authorization and backend cleanup.

## Evidence and pass conditions

Supply the lifecycle trace, marker verification before/after Pod replacement, failure diagnosis, recovery plan and deletion consequences. Never award a pass for "fixed by deleting the PVC" without a justified data-disposition record.

## Reset and resume

Delete only the synthetic writer and explicitly approved disposable claim after capturing evidence. Confirm whether the backend retained or deleted the volume; escalate retained backend cleanup to its owner. Record any resource intentionally left behind.

## Sources

- [Persistent volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
- [Storage classes](https://kubernetes.io/docs/concepts/storage/storage-classes/)
- [Volume snapshots](https://kubernetes.io/docs/concepts/storage/volume-snapshots/)
