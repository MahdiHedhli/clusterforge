# SEC-200-01: Identity lifecycle and federation

**Status:** Draft. Runtime not verified. **Format:** two 30-minute blocks.

## Objective

Separate identity provisioning, authentication, authorization and workload federation. Diagnose which layer could explain a denied request or access that persists after offboarding.

## Prerequisites

SEC-100 identity fundamentals and the [synthetic identity packet](../../practicals/levels-200-300/identity.json). The packet contains descriptive test data, not signed tokens or a running identity provider. No live endpoint is supplied or contacted.

## Learn

OIDC conveys authentication information and claims; SCIM manages provisioned identity resources. Removing a provisioned user or group membership is not proof that every previously issued credential has become unusable. The relying party's validation, session lifecycle and authorization state must be examined. Workload identity is a separate identity path, not simply a human login placed inside a container.

Draw an identity chain with issuer, subject, audience, group mapping, credential lifetime, authorization target and data-plane identity. Mark the component that makes each decision.

## Practice

**Block A: human lifecycle.** Read the packet's two token descriptors and offboarding timeline. Compare audience and group claims with the declared relying-party contract. Identify the earliest point at which each request should be rejected. Explain why a claim's presence does not prove its cryptographic validity or that a resource server accepted it.

Build a joiner/mover/leaver test plan: provision an identity, change group membership, remove access, expire a session and repeat a previously successful action. State which system must provide the evidence for each step. Do not assume the directory, token issuer and resource server share instantaneous state.

**Block B: workload lifecycle.** Trace Kubernetes ServiceAccount -> projected token -> external federation trust -> target permission. Specify the intended subject and audience restrictions, short-lived credential behavior and target-resource scope. Explain how a broad trust condition could authorize an unintended workload. Use a paper design unless an approved test identity provider and destination already exist.

For a live extension, validate an allowed identity and a wrong-audience or wrong-subject case against a dedicated test service. Never use production accounts or publish token contents.

## Evidence and pass conditions

Provide two annotated identity chains, a lifecycle test plan and an offboarding finding with explicit unknowns. Packet analysis can pass the conceptual gate. Live federation qualification requires actual issuer/relying-party evidence and is separately marked NOT_RUN until tested.

## Reset and resume

There are no cluster mutations in the packet exercise. Keep any real identity records in an approved internal location. Record the exact trust condition or lifecycle behavior that remains unverified.

## Sources

- [OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0.html)
- [SCIM protocol, RFC 7644](https://www.rfc-editor.org/rfc/rfc7644.html)
- [Kubernetes ServiceAccounts](https://kubernetes.io/docs/concepts/security/service-accounts/)
