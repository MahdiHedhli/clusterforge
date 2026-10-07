# K8S-200-01: Rollouts and evidence-driven diagnosis

**Status:** Draft. Runtime not verified. **Format:** two 30-minute blocks.

## Objective

Explain a failed release without destroying the evidence, distinguish controller intent from container behavior, and recover through a justified manifest change or rollback.

## Prerequisites

K8S-100 entry gate and the healthy [shared practical](../../practicals/levels-200-300/README.md). Use its `k` wrapper and dedicated namespace. No external customer application is involved.

## Learn

A Deployment revision records changes to its Pod template, not every dependency of the application. A rollback can restore an earlier template while a separately changed ConfigMap remains changed. A progressing controller, available replicas, and a successful application response are different observations. Consult the Deployment documentation before choosing your recovery action.

Build a four-column investigation table: observation, hypothesis, discriminating test, result. Write at least two plausible hypotheses before changing the workload. A useful test eliminates a possibility; repeating a command without a question does not.

## Practice

**Block A: establish the baseline.** Inspect `k get deploy,rs,pods -o wide`, `k describe deployment cf-web`, `k rollout history deployment/cf-web`, and recent namespaced events. Identify the owning ReplicaSet and the template used by each Pod. Record a successful client-to-Service response using the shared practical instructions.

**Block B: investigate a release ticket.** Ask the instructor to introduce one rollout fault from the separate instructor material. The ticket is: "The release was accepted, but the new version never became ready." Do not read the fault recipe during independent assessment. Capture deployment conditions, Pod status, events and available logs before making a change. An image that never starts may have no application logs; use the image-pull event rather than treating missing logs as proof of application failure.

Propose a minimal correction, predict the expected controller behavior, apply it only to the lab object, and observe the result. Then ask whether the current declarative source will reintroduce the defect on the next apply.

## Evidence and pass conditions

Provide the original symptom, two hypotheses, the evidence that distinguished them, the changed field or selected revision, and a successful client-to-Service test after recovery. Explain why deleting all Pods was not a root-cause fix. In a two-minute briefing, distinguish a restored template from a restored application configuration.

Pass requires recovery without widening access or silently discarding the evidence. Guided injection and self-repair count as practice, not independent diagnosis.

## Reset and resume

Restore the approved fixture, remove only exercise-owned additions, and repeat its health checks. Record the deployment revision and exact next investigation step in the [session record](../../../templates/candidate-zero-session.md). Do not mark completion merely because a controller reports Available.

## Sources

- [Kubernetes Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [Debug running Pods](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/)
