# SEC-300-04: AI workload and artifact integrity

**Status:** Draft. Runtime not verified. **Format:** three 30-minute blocks.

## Objective

Trace the trust chain from dataset and build inputs through training, checkpoints, model release and serving. Design controls for integrity, confidentiality and authorized use.

## Prerequisites

K8S-300-04, SEC-300-01 and the [fictional customer brief](../../practicals/levels-200-300/customer.json). Use tiny synthetic text files as stand-ins for datasets, checkpoints and model artifacts. Do not download or deserialize untrusted model files.

## Learn

The container image is only one part of an AI workload's supply chain. Data, tokenizer/configuration, training code, dependencies, weights and checkpoints can each change the resulting behavior. A hash detects change relative to a trusted reference; a hash delivered by the same untrusted source is not independent provenance. A signature requires an explicit trusted signer policy.

Integrity, provenance, confidentiality and behavioral safety are separate claims. A correctly signed model can still be unsuitable or unsafe for a use case.

## Practice

**Block A: lineage record.** Create small synthetic dataset, checkpoint and model marker files in a local scratch directory. Build a manifest of their hashes, creator/build identity, version, dependencies and allowed destinations. State which fields are assertions versus independently verified observations. Never place real weights or sensitive training data in the repository.

**Block B: controlled tampering.** Preserve an original file and manifest, change one byte in a copy, and verify that comparison with the trusted original fails. Explain why recomputing and replacing both artifact and manifest from the same untrusted location defeats this limited test. Extend the design with an approved signing identity and access-controlled publication process. Reuse a validated signature test from K8S-300-04 instead of claiming hashing alone establishes authenticity.

**Block C: recovery and export.** Design checkpoint write, resume, promotion and rollback controls for the customer. Include storage identities, least-privilege artifact access, egress exceptions, release approval and a failed-integrity response. Discuss whether loading an artifact could execute code and require a safe format/loading policy. Do not prove that risk by executing a malicious payload.

## Evidence and pass conditions

Provide the lineage manifest, original/tampered comparison, trust-policy design and a checkpoint-recovery decision. Explain at least three claims the hash test does not establish. Pass requires a clear trusted reference and an explicit distinction between a synthetic integrity exercise and real model qualification.

## Reset and resume

Remove only the scratch copies after retaining the synthetic evidence. No live training job or model registry mutation is required. Record the next missing provenance or recovery test.

## Sources

- [Sigstore verification and trust policy](https://docs.sigstore.dev/cosign/verifying/verify/)
- [MITRE ATLAS](https://atlas.mitre.org/)
- [Kubernetes application security checklist](https://kubernetes.io/docs/concepts/security/application-security-checklist/)
