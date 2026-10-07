# SEC-200-03: Segmentation and private connectivity

**Status:** Draft. Runtime not verified. **Format:** three 30-minute blocks.

## Objective

Convert a data-flow requirement into testable network controls and diagnose which layer owns a failed connection.

## Prerequisites

K8S-200-03 or equivalent networking competence and an enforcing CNI. Use the [shared practical](../../practicals/levels-200-300/README.md). No changes to the physical network, VPN, private circuit or host firewall are authorized by this lesson.

## Learn

A private route, a firewall decision, workload segmentation, TLS and application authorization protect different boundaries. Private connectivity alone does not establish workload identity or encryption. A successful TLS session does not show that the caller was authorized for the requested data.

Write a flow matrix with source identity, source location, destination, protocol/port, purpose, enforcing layer and evidence. Avoid an unqualified statement that "the network is isolated."

## Practice

**Block A: operational flows.** Map administrator -> API, client -> web, workload -> DNS and workload -> artifact source for a fictional deployment. Classify each path as required, prohibited or unresolved. Identify the owner of each enforcement point and what observation would prove its behavior.

**Block B: live namespace control.** Use the supplied ingress policy to allow the approved client while denying the outsider. Capture successful baseline requests from both, then repeat after enforcement. Prove the server remains healthy while the prohibited source fails. Inspect labels, readiness and policy scope before attributing a timeout to enforcement.

**Block C: connectivity incident.** A hypothetical customer can reach the private network but not the application. Build a diagnostic sequence that separates routing, DNS, TLS, network policy and application authorization. Add a temporary exception proposal with owner, destination, expiry, logging and a removal test. Do not implement a real network exception during the exercise.

A previously completed K8S-300-03 matrix may be reused, but add private-connectivity ownership and customer-facing reasoning rather than rerunning identical commands for duplicate credit.

## Evidence and pass conditions

Supply the data-flow map, observed allow/deny tests and a layered diagnosis. Name one boundary your namespace test cannot establish, such as physical tenant isolation or private-circuit encryption. Pass requires a working legitimate flow and a prohibited flow failing for a supported reason.

## Reset and resume

Remove only lesson-created policies and verify the baseline. Keep physical-network questions as open design items, not inferred platform guarantees. Record the next unverified boundary.

## Sources

- [NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
- [Cilium policy concepts](https://docs.cilium.io/en/stable/security/policy/)
- [NIST Zero Trust Architecture publication overview](https://csrc.nist.gov/pubs/sp/800/207/final)
