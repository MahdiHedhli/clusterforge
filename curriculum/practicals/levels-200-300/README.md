# Practical environment contract and case packets

**Status:** Draft curriculum contract. Runtime not verified. This release supplies lesson plans and synthetic analytical packets, not a runnable provisioning or lab-fixture bundle.

Do not interpret a named object in a lesson as evidence that it exists. A qualified instructor or environment owner must supply and verify the following disposable fixtures before a live attempt. When a required fixture is unavailable, record the exercise as BLOCKED rather than improvising on a shared environment.

## Healthy starting environment

Use a dedicated Linux Kubernetes lab with verified Pod networking, DNS, Service forwarding and authorized access. Record Kubernetes, runtime and CNI versions. NetworkPolicy lessons require an implementation with observed enforcement. Storage, federation, TLS, artifact-signing, audit and runtime-sensor lessons have additional explicit prerequisites in their lesson files.

Use a dedicated kubeconfig, an explicitly approved context and the exact namespace `cf-lab-200-300`. That namespace must be owned by the current exercise and must not be shared concurrently with another learner. Namespace creation and any cluster-wide configuration are separate administrator actions, not hidden setup inside an application exercise.

Read the [learning contract](../../../docs/learning-contract.md). Verify the API endpoint and resource ownership, not merely a context name. Do not weaken existing admission, authorization or runner checks to satisfy a lesson.

## Instructor-supplied baseline contract

| Object or capability | Required behavior |
| --- | --- |
| `cf-web` Deployment | Two replicas; non-root HTTP application; container named `web`; TCP/8080 readiness probe; label `app=cf-web` |
| `cf-web` Service | ClusterIP service selecting the web Pods, port/targetPort 8080 |
| `cf-client` Pod | Approved client with label `app=cf-client` and a bounded HTTP diagnostic capability |
| `cf-outsider` Pod | Control client with label `app=cf-outsider` |
| `cf-web-content` ConfigMap | Synthetic application configuration only |
| `cf-reader` ServiceAccount | Synthetic identity; no real external privileges |
| `cf-config-reader` Role and `cf-reader` RoleBinding | Get/list ConfigMaps in the exact lab namespace only, subject `cf-reader` |
| Ingress-control fixture | Select web Pods and allow TCP/8080 only from the approved same-namespace client label |

The two clients should reach the application before a policy exercise. After the intended ingress control is applied, the legitimate client must still succeed while the outsider fails for an evidence-supported reason. Overlapping policies, unrelated readiness failures and absent DNS must be excluded before claiming enforcement.

Choose a reviewed image compatible with the host architecture and application requirements. Record its resolved digest and provenance. A version tag is not immutable. No particular image, sensor, policy engine or CNI is reported as installed or verified by this release.

## Command convention

Lessons use `k` as shorthand for an instructor-reviewed kubectl wrapper that explicitly supplies the dedicated kubeconfig, context and namespace on every invocation. The environment owner must provide that wrapper before running lesson commands. It is an ergonomics convention, not an authorization boundary or a hardened sandbox.

Commands containing `<exact-pod>` or another placeholder require a verified exercise-owned resource, not a guessed target. Any impersonation test also requires pre-existing authorization to impersonate the synthetic subject and relevant ServiceAccount groups. Do not grant extra privileges merely to execute a check.

Review all resources before applying a manifest, including every document's kind, namespace and scope. The namespace exercise does not authorize node operations, host access, public listeners, cluster-wide RBAC, admission-engine installation, CNI migration, audit reconfiguration or storage-backend changes.

## Acceptance and restoration

Before the lesson, record expected nodes/system components healthy, actual client-to-Service responses, ready EndpointSlice backends and the exact baseline configuration. A port-forward alone is not a Service-path acceptance test.

Before an independent fault, record original field values and verify the intended symptom on the actual version. Restore each changed field explicitly and test both required function and the relevant security condition. Reapplying a manifest does not necessarily remove fields added through another workflow.

Cleanup must target exact exercise-owned objects. Do not delete the whole namespace, unrelated policies, PVCs or cluster components as a shortcut. Storage deletion requires its own data-disposition decision. Leave a safe state and [resume checkpoint](../../../templates/candidate-zero-session.md).

## Supplied analytical packets

- [Identity lifecycle](identity.json): descriptive claim and provisioning observations, not signed tokens or a live identity provider.
- [Incident investigation](incident.json): normalized fictional observations, not raw audit logs or proof of compromise.
- [Customer architecture](customer.json): fictional requirements and unknowns, not a description of a real platform.

These packets support analytical assessment only. They cannot establish successful deployment, control enforcement, token validation, live containment or learner implementation competency.

## Sources

- [Debug Services](https://kubernetes.io/docs/tasks/debug/debug-application/debug-service/)
- [NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
- [RBAC authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
