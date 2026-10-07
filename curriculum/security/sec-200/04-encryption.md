# SEC-200-04: Encryption, credentials and rotation

**Status:** Draft. Runtime not verified. **Format:** three 30-minute blocks.

## Objective

Explain what is protected at each storage/transport boundary, who can decrypt it, and what evidence is needed to verify credential or key rotation.

## Prerequisites

SEC-200-01 and 02. Synthetic credentials only. TLS testing requires a separately approved test endpoint and trust bundle. KMS and control-plane encryption changes require administrator ownership and are not part of the namespace fixture.

## Learn

Separate transport encryption, API datastore encryption, storage-backend encryption and application-level encryption. An authorized API read can return plaintext even when stored data is encrypted. Encryption therefore does not replace authorization. Kubernetes Secret encoding should never be described as an encryption control.

A key-ownership claim needs a lifecycle: generation, custody, access, rotation, backup, recovery and destruction. Do not infer operator exclusion solely from a customer-managed-key option.

## Practice

**Block A: boundary inventory.** For the shared application's configuration and a hypothetical training dataset, draw where plaintext exists and which principals can access it. Add certificates, data keys, wrapping keys and service credentials only where the design actually uses them. Identify which claims a namespace user can observe and which require platform evidence.

**Block B: credential refresh.** Use a harmless marker in an exercise-owned Secret and compare an environment consumer with a volume consumer. Observe the application behavior before and after rotation; do not assume that a changed Kubernetes object means a process has reloaded the value. Document restart/reload requirements and revoke the old test credential in the downstream test service when one exists. Without such a service, do not claim revocation was demonstrated.

**Block C: transport evidence.** For an approved TLS endpoint, verify the trust chain and expected server name with certificate verification enabled. Test an incorrect name or untrusted certificate as a negative case without weakening verification. If no endpoint exists, produce the test design and mark live TLS validation BLOCKED. Describe what evidence would substantiate encryption at rest without dumping raw datastore secrets.

## Evidence and pass conditions

Provide the plaintext/key boundary map, observed marker refresh, transport test results or explicit blocker, and a rotation/recovery runbook. Separate configured, observed and unverified claims. A Secret manifest or HTTPS URL alone cannot pass the encryption verification gate.

## Reset and resume

Delete exercise-owned synthetic consumers and Secrets, retire test certificates through their owner, and record outstanding key-recovery tests. Do not publish private keys, credentials or internal endpoints.

## Sources

- [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)
- [Encryption at rest](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/)
- [Application security checklist](https://kubernetes.io/docs/concepts/security/application-security-checklist/)
