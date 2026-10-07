# Certification alignment for 200/300

**Reviewed against official public certification pages: 2026-10-07.** Recheck the linked domains and exam prerequisites before planning an exam attempt. ClusterForge is not affiliated with or endorsed by CNCF or the Linux Foundation.

This is a competency crosswalk, not a claim of complete syllabus coverage, exam readiness or credential equivalence. Module authorship, lab qualification and learner evidence are separate.

## Crosswalk

| ClusterForge evidence | External domain overlap | Limitation |
| --- | --- | --- |
| K8S-200-01 rollouts | CKA workloads/troubleshooting; CKAD deployment and observability | Does not cover every deployment strategy |
| K8S-200-02 placement/resources | CKA workloads/scheduling; CKAD environment/configuration | HPA and resource-driven autoscaling need additional live practice |
| K8S-200-03 Service/DNS path | CKA services/networking; CKAD services/networking | Live Gateway, Ingress and external load balancing remain separate |
| K8S-200-04 PVC recovery | CKA storage | Requires a qualified CSI/backend; paper analysis is not storage implementation credit |
| K8S-200-05 layered triage | CKA troubleshooting; CKAD observability/maintenance | Metrics and node access must be verified, not presumed |
| K8S-200-06 lifecycle review | CKA architecture/installation/configuration | Build, HA, upgrade, restore, Helm and operators need hands-on qualification beyond a reviewed plan |
| K8S-300-01 identity/RBAC | CKS cluster hardening | API authorization checks do not prove full credential lifecycle |
| K8S-300-02 workload/admission | CKS microservice/system hardening | Actual policy and runtime support must be available |
| K8S-300-03 network enforcement | CKS cluster setup and microservice protection | Pod-to-Pod encryption, host protection and implementation-specific features need extra live tests |
| K8S-300-04 secrets/artifacts | CKS supply chain and microservice protection | Scanner, signing and admission integration are not all supplied by the small fixture |
| K8S-300-05 runtime boundary | CKS system hardening and runtime security | Requires sensor/OS prerequisites; a Running agent is not sufficient evidence |
| K8S-300-06 investigation | CKS monitoring/logging/runtime security | Analytical and live response qualifications remain separate |
| SEC-200 operational controls | Selected CKA/CKS identity, networking and audit skills | OIDC/SCIM/federation, control ownership and assurance extend beyond that overlap |
| SEC-300 architecture/investigation | Applies relevant CKS skills in larger scenarios | No direct certification equivalence; adds customer discovery, AI assets, isolation analysis and communication |

## Explicit remaining exam-preparation work

For CKA, validate the current official domains and add hands-on cluster build/lifecycle, HA, restore, Helm/Kustomize, operators/CRDs, autoscaling and external routing practice as needed. For CKAD, separately verify application-design coverage such as Jobs/CronJobs, multi-container patterns and the full current deployment/configuration domain. For CKS, qualify system hardening, component baseline review, platform binary verification, TLS/Pod encryption and the chosen runtime/supply-chain tooling in a suitable environment.

These gaps are not solved by marking a lesson read. Maintain an external-domain checklist linked to actual evidence before making an exam-readiness claim. The Linux Foundation states that candidates must have passed CKA before attempting CKS; this is an exam prerequisite, not a prerequisite to study these ClusterForge lessons.

## Official references

- [CKA domains and prerequisites](https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/)
- [CKAD domains and prerequisites](https://training.linuxfoundation.org/certification/certified-kubernetes-application-developer-ckad/)
- [CKS domains and prerequisites](https://training.linuxfoundation.org/certification/certified-kubernetes-security-specialist/)

Primary technical references are linked in each lesson. Prefer documentation matching the installed Kubernetes, CNI, runtime and tool versions rather than assuming a moving latest page matches the lab.
