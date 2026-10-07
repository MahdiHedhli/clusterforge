# K8S-300-02: Workload hardening and admission

**Status:** Draft. Runtime not verified. **Format:** three 30-minute blocks.

## Objective

Reduce workload privilege and test enforcement without confusing a compliant manifest, an admitted object and a healthy application.

## Prerequisites

K8S-300-01, the [shared practical](../../practicals/levels-200-300/README.md), and an administrator-approved namespace admission profile. Changing namespace policy labels is an explicit administrator action. Never relabel system namespaces or weaken a cluster-wide policy to satisfy the lab.

## Learn

Authentication, authorization and admission are separate decisions. Pod Security Standards describe policy levels; Pod Security Admission is one enforcement mechanism. Restricted requirements depend on the selected policy version. A read-only root filesystem is a useful additional control, but is not itself a universal requirement of the Restricted profile.

A Deployment may be accepted while its controller's Pods are rejected. Check controller events as well as the original apply result. Hardening must include the application's write paths, runtime user, capabilities and syscall needs.

## Practice

**Block A: inspect effective privilege.** Review the baseline's non-root user, dropped capabilities, `allowPrivilegeEscalation`, seccomp profile, filesystem writes and token automount setting. Inspect the running container with a harmless `id` command. Explain which controls the image could request and which the platform must enforce.

**Block B: test admission.** With the administrator's approved namespace policy in place, create two local candidate manifests: one compliant, one deliberately noncompliant. Submit server-side dry-run tests first. Record the API decision and message. A dry run contacts admission but does not establish runtime behavior. Do not create a privileged workload live merely to show that admission would allow it.

If dry-run rejection and approval match expectations, deploy only the compliant candidate and test the real application path. Check that required writes use a narrowly scoped writable volume, not a globally writable root filesystem.

**Block C: handle an exception.** A fictional workload asks for a forbidden capability. Write the operational need, safer alternative, minimum scope, owner, expiry, compensating control and verification plan. Compare built-in policy with a reviewed Kyverno or Gatekeeper policy design. Installing an admission engine or CRD is not part of this namespace exercise.

## Evidence and pass conditions

Provide compliant and rejected dry-run results, the policy version, live application verification, and the exception decision. Explain why a successful Deployment apply is insufficient. Pass requires no broad exception and no silent disabling of enforcement.

## Reset and resume

Delete only the compliant exercise candidate by exact name. Have the authorized owner restore any namespace-policy changes to their recorded prior values. Preserve no privileged test workload.

## Sources

- [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)
- [Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/)
- [Configure a security context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)
