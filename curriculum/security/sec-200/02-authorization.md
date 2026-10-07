# SEC-200-02: Least-privilege operations

**Status:** Draft. Runtime not verified. **Format:** two 30-minute blocks.

## Objective

Translate a concrete operational task into a scoped role and prove expected permissions without confusing caller privileges with the subject being tested.

## Prerequisites

SEC-200-01 and the [shared practical](../../practicals/levels-200-300/README.md), including its optional `cf-reader` role fixture. The instructor must authorize impersonation before impersonation-based checks. An inability to impersonate is not an authorization result for the target ServiceAccount.

## Learn

A task specification should say which API resources, operations and namespace are required. "Read-only" is too vague: reading configuration can still expose sensitive data, and some subresources convey capabilities beyond reading a parent object's metadata. Effective permission can come from several bindings.

Distinguish failed authentication, denied authorization, denied admission and unavailable infrastructure. Do not respond to all four with a broader role.

## Practice

**Block A: design.** The task is: a diagnostics workload may get/list ConfigMaps in its assigned lab namespace. It must not read Secrets, create Pods, change Roles or operate in another namespace. Review the supplied Role, RoleBinding and ServiceAccount against that statement. Predict every row in a permission matrix before testing.

**Block B: verify.** Use the practical's approved authorization-check pattern, including ServiceAccount groups, to test required and prohibited operations. Record the exact subject and scope used. Inspect all relevant binding sources within the permission granted to the examiner. If you cannot inspect broader bindings, state that limitation rather than asserting the inventory is complete.

Introduce an instructor-selected binding defect on the synthetic role only. Diagnose the mismatch and correct the narrowest field. Retest allowed and forbidden operations. Explain what the authorization check establishes and why it is not proof of a successful end-to-end authenticated workload request.

Add a short operational runbook: access request, owner approval, expiry/review, verification and removal. Do not grant wildcard permissions for convenience.

## Evidence and pass conditions

Submit the task-to-permission table, predicted and observed results, the binding defect's root cause and a removal/retest plan. Pass requires the required operation to be allowed and at least three relevant forbidden operations to be denied. State any uninspected scope.

## Reset and resume

Restore or remove only the synthetic role/binding changes. Keep real credentials out of command transcripts and public evidence. Record whether token authentication and actual resource access remain untested.

## Sources

- [RBAC authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
- [RBAC good practices](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)
- [kubectl auth can-i](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_auth/kubectl_auth_can-i/)
