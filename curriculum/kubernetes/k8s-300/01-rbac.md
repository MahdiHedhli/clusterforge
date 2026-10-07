# K8S-300-01: Identity, RBAC and attack paths

**Status:** Draft. Runtime not verified. **Format:** three 30-minute blocks.

## Objective

Trace an identity's direct and indirect capabilities, validate least privilege, and explain why a role name is not an adequate security assessment.

## Prerequisites

SEC-200-01 and 02 or equivalent; K8S-200 troubleshooting; [shared practical](../../practicals/levels-200-300/README.md). Impersonation checks require separately authorized impersonation of the test identity and its relevant groups. Do not grant yourself impersonation privileges to make a test work.

## Learn

RBAC permissions are additive. A RoleBinding can reference a ClusterRole while granting its applicable permissions in that binding's namespace. Workload creation can introduce indirect capabilities through a chosen ServiceAccount, mounted data or runtime privileges; examine admission controls as well as RBAC. `bind`, `escalate` and impersonation deserve explicit review.

Separate four claims: the caller authenticated, authorization permitted an API action, admission accepted a proposed object, and the resulting workload could access an asset. Evidence for one does not establish the others.

## Practice

**Block A: map a benign reader.** Use the supplied `cf-reader` Role and binding. Record subject, roleRef, resources, verbs and scope. Predict access to ConfigMaps, Secrets, Pods and RoleBindings before running the approved authorization checks. Include relevant ServiceAccount groups when using impersonation. Record inability to impersonate as a test prerequisite gap, not a denied capability of the subject.

**Block B: analyze an escalation graph.** The instructor supplies a sanitized hypothetical role that permits creating Pods and a second, more privileged ServiceAccount in the same namespace. Draw the possible identity transition and name the controls required to prevent it. Do not use a production identity or mount a real credential. Proving a dangerous path live requires a separately reviewed, namespaced synthetic fixture; this baseline does not authorize a container escape or cluster-admin escalation.

**Block C: redesign and retest.** Produce a minimal role for the stated task and a list of denied operations. Retest the known reader and review how future RoleBindings could widen its authority. Explain what role deletion, binding deletion, token expiry and Pod deletion do at different layers rather than calling them all "revocation."

## Evidence and pass conditions

Submit the identity graph, expected/observed permission matrix, one indirect path, remediation proposal and residual risk. Authorization results are not proof that a token was accepted by an authentication service. Pass requires a legitimate operation and at least two relevant denied operations without overbroad grants.

## Reset and resume

Remove only the exercise-created bindings/identities after preserving evidence. Never dump token contents into the public record. Record any untested indirect capability separately.

## Sources

- [RBAC good practices](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)
- [Using RBAC authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
- [ServiceAccounts](https://kubernetes.io/docs/concepts/security/service-accounts/)
