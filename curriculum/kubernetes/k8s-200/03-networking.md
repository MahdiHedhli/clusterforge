# K8S-200-03: Services, DNS and network paths

**Status:** Draft. Runtime not verified. **Format:** three 30-minute blocks.

## Objective

Trace a request from a client Pod through DNS and a Service to the application. Isolate selector, readiness, port, DNS and network-enforcement failures with contrasting tests.

## Prerequisites

K8S-200-01 and the [shared practical](../../practicals/levels-200-300/README.md). Know which CNI and Service-proxy implementation the lab uses. Do not replace that implementation during the lesson.

## Learn

A selector-based Service obtains backend information through EndpointSlices. Inspect all slices associated with the Service, not an assumed single object. A direct Pod-IP request, a ClusterIP request and a DNS-name request exercise different portions of the path. A port-forward reaches a selected Pod through a debugging channel; it is not proof that normal Service forwarding works.

Draw the request path and name the evidence source for each hop. Avoid declaring "DNS issue" just because a DNS name appears in the failing command.

## Practice

**Block A: build the comparison.** From `cf-client`, test the Service name, its ClusterIP and one ready backend Pod IP using short timeouts. Inspect `k get service cf-web -o yaml`, `k get endpointslices -l kubernetes.io/service-name=cf-web -o yaml`, Pod labels and the actual container listen port. Record the expected response body, not only an exit code.

**Block B: investigate.** Receive a ticket with healthy-looking Pods and failed application requests. The instructor changes one namespaced configuration field. Form alternatives: selection, target port, readiness, name resolution or policy. Use paired tests to discriminate; preserve evidence before applying the smallest correction. Repeat the original failing request after repair.

**Block C: explain the surrounding platform.** Identify the CNI's Pod-connectivity responsibility and the actual Service-forwarding component. Explain ClusterIP, NodePort and LoadBalancer exposure as different choices, without creating public listeners. Review an Ingress or Gateway/HTTPRoute example from official documentation. State that an API object alone does not install a controller or provision an external network path.

## Evidence and pass conditions

Produce a path diagram, three baseline connectivity results, the broken-state result and the recovered result. Identify whether traffic reached a backend. Explain one test that would separate DNS failure from Service forwarding failure. A successful port-forward alone cannot satisfy the gate.

## Reset and resume

Restore the original selector/port or instructor-controlled fault. Remove any temporary probe Pods by exact name. Keep the shared clients only while continuing the course. Record the next untested network boundary.

## Sources

- [Debug Services](https://kubernetes.io/docs/tasks/debug/debug-application/debug-service/)
- [EndpointSlices](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/)
- [Gateway API concepts](https://kubernetes.io/docs/concepts/services-networking/gateway/)
