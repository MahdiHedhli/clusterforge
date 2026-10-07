# K8S-300-03: Network and egress enforcement

**Status:** Draft. Runtime not verified. **Format:** three 30-minute blocks.

## Objective

Prove a network control's allowed and denied paths, preserve required DNS/application behavior, and explain the limits of the tested boundary.

## Prerequisites

K8S-200-03 and SEC-200-03 or equivalent. Use the [shared practical](../../practicals/levels-200-300/README.md) and a CNI verified to enforce NetworkPolicy. A policy object accepted by the API is not evidence of enforcement.

## Learn

Standard NetworkPolicies are additive and select traffic directions independently. A connection may need permission from both the source's egress policy and destination's ingress policy. Empty selectors, namespace selectors and separate versus combined peer entries can radically change the admitted set. Namespace boundaries do not create network isolation by themselves.

Policy testing must distinguish failed DNS resolution, denied transport, an absent server and an application error. Standard L3/L4 policy is not a general FQDN, HTTP authorization or encryption mechanism.

## Practice

**Block A: baseline and ingress.** Prove that both `cf-client` and `cf-outsider` can reach `cf-web` before applying the supplied ingress policy. Predict its result. Apply it only in the lab namespace. Repeat both requests with short timeouts and confirm the server still serves the allowed client. Inspect policy selectors and endpoint readiness alongside the test results.

**Block B: egress design.** Author a separate namespaced egress policy for the client based on observed DNS and server topology. Permit only the required DNS transport and web destination. Account for the actual resolver path, including NodeLocal DNS or host-network exceptions when present; do not guess DNS labels. Validate expected allow and deny paths using instructor-approved internal test destinations. Do not probe cloud metadata endpoints or unrelated networks.

**Block C: Cilium extension.** When Cilium is already installed and approved, compare the standard policy with a namespaced CiliumNetworkPolicy design for a narrowly defined FQDN or L7 requirement. Record version-specific behavior and required observation tooling. Do not install Cilium, replace Calico or apply cluster-wide policies during this lesson. Without Cilium, mark this extension NOT_RUN.

## Evidence and pass conditions

Provide baseline, enforcement and recovery matrices, exact policy definitions and a negative test that failed for the intended reason. Explain how a user allowed to relabel Pods could affect label-based policy and why these labels are not sufficient for hostile-tenant isolation.

## Reset and resume

Remove only the policies created for this lesson, by exact name, and restore the baseline allow tests. Preserve unrelated policies. Record any untested traffic direction or DNS exception.

## Sources

- [Kubernetes NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
- [Cilium policy documentation](https://docs.cilium.io/en/stable/security/policy/)
