# Day 1: From API Request to Running Pod

**Tracks:** K8S-100 + SEC-100  
**Estimated time:** 3 hours core + optional challenge  
**Theme:** Know the machine before securing the machine.

## Objectives

By the end of this lesson, the learner should be able to:

- Draw and explain the major Kubernetes control-plane and node components.
- Trace what happens after `kubectl apply`.
- Distinguish desired state from observed state and explain reconciliation.
- Navigate a cluster with core `kubectl` commands.
- Deploy and expose an application.
- Diagnose a failed workload using object state, events, logs, labels, selectors, and endpoints.
- Identify basic Kubernetes trust boundaries.
- Locate authentication, authorization, admission, and workload identity in the request path.
- Explain a Kubernetes failure clearly to another engineer or customer.

## 1. Mental model: Kubernetes reconciles state

Kubernetes is fundamentally a reconciliation system. A user declares desired state through the API. Controllers continuously compare desired state with observed state and act to reduce the difference.

If a Deployment declares three replicas, the instruction is not simply "create three containers." The declaration means that the system should continue attempting to maintain three replicas until the desired state changes.

### Core components

```text
                    CONTROL PLANE

                   +--------------+
kubectl ---------->|  API Server  |<---------------+
                   +------+-------+                |
                          |                        |
                 +--------+---------+              |
                 |                  |              |
              +--v---+       +------v------+       |
              | etcd |       | Controllers |       |
              +------+       +-------------+       |
                          |                        |
                    +-----v-----+                  |
                    | Scheduler |                  |
                    +-----+-----+                  |
                          |                        |
--------------------------+-----------------------------
                          |
                       WORKERS

              +-----------v-----------+
              |        Node           |
              |                       |
              |       kubelet --------+-----------+
              |          |            |
              |          v            |
              |         CRI           |
              |          |            |
              |      containerd       |
              |          |            |
              |      +---v---+        |
              |      |  Pod  |        |
              |      +-------+        |
              +-----------------------+
```

Know these components well enough to explain their responsibility rather than merely define them:

- **API server:** primary interface to Kubernetes control-plane state and operations.
- **etcd:** persistent backing store for Kubernetes API state.
- **scheduler:** selects an eligible node for an unscheduled Pod.
- **controller manager:** runs reconciliation controllers.
- **kubelet:** node agent responsible for driving assigned Pods toward their declared state.
- **container runtime:** manages containers through the CRI integration used by the kubelet.

## 2. Follow the Pod

Trace a simplified `kubectl apply -f deployment.yaml` request:

```text
kubectl
   |
   v
API Server
   |
Authentication
   |
Authorization
   |
Admission
   |
etcd
   |
Deployment Controller
   |
ReplicaSet
   |
Pod created
   |
Scheduler selects Node
   |
Pod binding
   |
kubelet observes assignment
   |
CRI / container runtime
   |
image + container
   |
running workload
```

### Checkpoint

Explain the flow without notes. Then answer:

1. Which component accepts the original request?
2. Which component persists API state?
3. Does the Deployment directly create running containers?
4. Who chooses the node?
5. Who acts on that node assignment?

## 3. Security lens

Trace the same path as a sequence of security decisions:

```text
User
 |
Identity
 |
API Server
 |
RBAC
 |
Admission
 |
Kubernetes Object
 |
Scheduler
 |
Node
 |
kubelet
 |
container runtime
 |
workload
 |
network / storage / devices
```

Ask these questions:

- Who is making the request?
- How is that identity authenticated?
- What is the identity authorized to do?
- Should an otherwise authorized configuration be admitted?
- What identity does the resulting workload receive?
- What kernel/runtime privileges does the workload receive?
- What may it communicate with?
- What data or devices may it access?

These questions become deeper throughout SEC-100 through SEC-500+.

## 4. Lab: Meet the cluster

Run:

```bash
kubectl cluster-info
kubectl get nodes -o wide
kubectl get namespaces
kubectl get pods -A
kubectl get deployments -A
kubectl get services -A
kubectl describe node <node>
```

Find and record:

- Kubernetes version
- container runtime
- node internal IP
- capacity
- allocatable resources
- node conditions
- taints
- running Pods

**Question:** Why can `Capacity` and `Allocatable` differ? Form a hypothesis before looking up the answer.

## 5. Lab: Deploy a workload

Create the namespace:

```bash
kubectl create namespace candidate-zero
```

Create `web.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
  namespace: candidate-zero
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
        - name: web
          image: nginx:alpine
          ports:
            - containerPort: 80
```

Apply and inspect:

```bash
kubectl apply -f web.yaml
kubectl get deployments -n candidate-zero
kubectl get replicasets -n candidate-zero
kubectl get pods -n candidate-zero -o wide
```

Delete one Pod and watch reconciliation:

```bash
kubectl delete pod <pod-name> -n candidate-zero
kubectl get pods -n candidate-zero -w
```

Explain:

- Why did another Pod appear?
- Which object expressed the desired replica count?
- Which controller ultimately caused a replacement Pod to be created?
- Why is deleting a managed Pod different from changing the Deployment replica count?

## 6. Lab: Expose and inspect the application

```bash
kubectl expose deployment web \
  --namespace candidate-zero \
  --port=80 \
  --target-port=80

kubectl get svc -n candidate-zero
kubectl describe svc web -n candidate-zero
kubectl get endpoints -n candidate-zero
kubectl port-forward service/web 8080:80 -n candidate-zero
```

Verify the application locally.

**Question:** How does the Service determine which Pods belong behind it?

## 7. Incident INC-001: Break it

Introduce a selector mismatch so the Service selects `app: website` while the Pods remain labeled `app: web`.

### Ticket

> Customer reports their application stopped responding after a configuration change. Pods appear to be running. Determine root cause and restore service.

Use evidence rather than redeploying everything. Useful tools include:

```bash
kubectl get
kubectl describe
kubectl logs
kubectl get events
kubectl get endpoints
```

Report the incident using:

```text
SYMPTOM
EVIDENCE
HYPOTHESIS
TEST
ROOT CAUSE
REMEDIATION
VERIFICATION
```

## 8. Lab: Security reconnaissance

Inspect a Pod:

```bash
kubectl get pod <pod> -n candidate-zero -o yaml
```

Identify:

- ServiceAccount
- image
- image pull policy
- security context
- resource requests and limits
- mounted volumes
- environment variables
- assigned node
- Pod IP

Enter the container:

```bash
kubectl exec -it <pod> -n candidate-zero -- sh
```

Investigate without attempting privilege escalation:

- What user is the process running as?
- What filesystem is visible?
- What network interfaces are visible?
- Can Kubernetes services be resolved?
- Is projected ServiceAccount identity material present?
- Is the Kubernetes API reachable from the workload network?

The goal is attack-surface mapping, not exploitation.

## 9. First threat model

For the simple web Deployment, identify:

- assets
- actors
- entry points
- trust boundaries
- privileged components
- plausible attacker objectives

Do this before introducing a formal threat-modeling framework. Preserve the result so it can be compared with the learner's SEC-300 threat model later.

## 10. Optional Boss Fight: The Missing Pod

Start with a Deployment where desired replicas are 3 but available replicas are 2.

**Objective:** Restore the Deployment to 3/3 healthy replicas without recreating the cluster or redeploying the entire application from scratch.

The learner must produce the full troubleshooting evidence chain:

```text
SYMPTOM -> EVIDENCE -> HYPOTHESIS -> TEST -> ROOT CAUSE -> REMEDIATION -> VERIFICATION
```

## Day 1 practical assessment

Answer without notes:

1. What is the difference between a Pod and a Deployment?
2. Why does deleting a Deployment-managed Pod not permanently remove the workload?
3. What is the API server's role?
4. Why does Kubernetes need etcd?
5. How do scheduler and kubelet responsibilities differ?
6. What does a Service do?
7. Why are labels and selectors operationally important?
8. Where do authentication, authorization, and admission occur?
9. What is a ServiceAccount?
10. A customer says, "My Pods are Running but my application is unavailable." How do you investigate?

## Candidate Zero baseline

Record evidence and confidence for each competency rather than treating completion as proof of mastery.

| Competency | Initial Day 1 target |
| --- | ---: |
| Architecture | 70% |
| kubectl fluency | 60% |
| Workloads | 60% |
| Networking | 40% |
| Troubleshooting | 50% |
| Security reasoning | 60% |
| Technical explanation | 50% |

A perfect Day 1 score is not the objective. The baseline exists to reveal gaps that subsequent labs can target.
