# K8S-300-05: Node, runtime and detection boundaries

**Status:** Draft. Runtime not verified. **Format:** three 30-minute blocks.

## Objective

Explain the host/runtime attack surface and establish whether a runtime sensor can observe a specific harmless event with usable workload attribution.

## Prerequisites

K8S-200-05 and K8S-300-02. A compatible, administrator-installed Falco or Tetragon sensor is required for the live detection gate. Sensor installation, host privileges and tracing policies are outside the namespace-only fixture. Without a sensor, complete analysis only and record detection as NOT_RUN.

## Learn

Container isolation involves kernel mechanisms and runtime configuration; sharing a kernel is not equivalent to a separate virtual machine. RuntimeClass selection only works when its handler is actually configured. Compare runc, gVisor and Kata conceptually, then verify the capabilities of the environment rather than assuming a name provides a guarantee.

Falco primarily observes events and emits rule-based alerts; observing is not automatically blocking. Tetragon supports observability and enforcement features, but an installed agent alone does not establish an effective policy. Evaluate the configured feature and coverage, not the product label.

## Practice

**Block A: map the boundary.** Record kernel, runtime and relevant workload security settings from approved evidence. Draw application -> container -> runtime -> kernel -> node. Identify where seccomp, capabilities and a runtime sandbox would constrain behavior. Review host patches and exposed services through approved read-only evidence; do not change node configuration.

**Block B: prove visibility.** Have the instructor configure a narrowly scoped observation rule for a harmless command in the lab client. Verify sensor health, rule scope, node coverage and event-loss indicators. Run one approved `id` process through the explicit lab context. Correlate timestamp, process, container/Pod identity and node in the resulting event. Do not assume a default shell rule must alert on a non-interactive command.

**Block C: negative and operational tests.** Use an instructor-defined benign control event to test whether the rule is too broad. Explain how missing telemetry, mismatched rule scope and a genuinely absent event would look different. Propose a response workflow with human approval before disruptive containment.

## Evidence and pass conditions

Provide the boundary diagram, sensor/version prerequisites, matched event, benign comparison and telemetry limitations. Pass requires attribution to the intended workload. A screenshot saying the agent is Running is insufficient.

## Reset and resume

Remove only lesson-specific observation policy through its authorized owner. Do not uninstall shared sensors or change host hardening. Record untested sandbox or enforcement capabilities separately.

## Sources

- [Falco documentation](https://falco.org/docs/)
- [Tetragon documentation](https://tetragon.io/docs/)
- [Linux kernel security constraints](https://kubernetes.io/docs/concepts/security/linux-kernel-security-constraints/)
- [RuntimeClass](https://kubernetes.io/docs/concepts/containers/runtime-class/)
