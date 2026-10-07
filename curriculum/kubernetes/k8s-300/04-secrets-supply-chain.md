# K8S-300-04: Secrets and software supply chain

**Status:** Draft. Runtime not verified. **Format:** three 30-minute blocks.

## Objective

Trace how credentials and artifacts reach a workload, validate the intended trust decisions, and avoid claiming that encoding, a signature or an SBOM proves security.

## Prerequisites

SEC-200-04 and K8S-300-01 through 02 or equivalent. Use synthetic credentials only. Artifact tooling is an optional, explicitly installed local prerequisite; do not run an unknown image or build script to inspect it.

## Learn

Kubernetes Secret data encoding is not at-rest encryption. A workload receiving a mounted Secret follows a different access path from a principal reading that Secret through the API. Environment-based secret consumption and projected volume updates have different refresh behavior; applications still need an effective rotation strategy.

An image digest identifies content. Signature verification additionally requires a trust policy, such as an expected signing identity and issuer. An SBOM inventories components; it does not prove an artifact is vulnerability-free or safe to execute.

## Practice

**Block A: synthetic credential lifecycle.** Design a Secret containing only a non-sensitive training marker and two workload consumption methods. Review access, mount permissions and logging before use. Observe how a marker update reaches a volume consumer versus an environment consumer. Do not print real secrets. State whether a restart or application reload is required for the chosen design.

**Block B: artifact verification.** Inspect the baseline image reference and record the resolved image ID after an authorized run. Explain the difference between the example's version tag and a pinned digest. With a trusted synthetic signed artifact supplied by the instructor, perform a local verification using an explicit expected key or signing identity/issuer. Repeat with altered content or the wrong identity and require failure. No network keyless-signing publication is required by this exercise.

**Block C: supply-chain decision.** Review an SBOM and scanner result for a small approved artifact. Record source, digest, scanner/database versions, findings, reachability assumptions, remediation and exception owner. Propose an admission check that uses verified identity rather than trusting an arbitrary signature. Explain which controls prevent artifact replacement and which detect vulnerable content.

## Evidence and pass conditions

Supply a credential-access/rotation diagram, observed refresh behavior, positive and negative artifact verification results, and a defensible release decision. If tooling or a signed fixture is unavailable, label that portion BLOCKED; a written plan cannot pass the implementation portion.

## Reset and resume

Delete synthetic Secrets and consumers by exact name. Remove scratch signing material after the record is complete. Keep registry credentials, tokens and raw scan data out of public evidence.

## Sources

- [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)
- [Encryption at rest](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/)
- [Cosign signature verification](https://docs.sigstore.dev/cosign/verifying/verify/)
