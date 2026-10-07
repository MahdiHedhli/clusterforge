# Learning contract for 200/300

## Learn first, improve the curriculum second

Choose the next unfinished competency from a current learner report or evidence record. Missing public commits do not establish that no learning occurred. A session should normally produce one bounded investigation or control test, not an infrastructure redesign.

Use a healthy baseline. An unexpected setup failure is a setup blocker unless the instructor explicitly selected it as the exercise. Stop at a safe point before other commitments; record the exact next action.

## Separate roles

The environment administrator prepares and verifies the lab. The instructor supplies the brief, approves the bounded fault, controls hints and reviews evidence. The learner investigates and explains. An assistant may prepare material or offer graduated hints but must not silently solve an assessed task, execute unapproved mutations or invent learner results.

Keep instructor answer material outside the tutoring agent's assessment context. The public instructor directory is a teaching separation, not an access-control boundary. A learner who has seen the answer needs a fresh variant for independent assessment.

## Environment and mutation boundary

Use a dedicated lab kubeconfig, explicit context and exact approved namespace. Verify the API endpoint and namespace ownership before any mutation. A context name or namespace prefix alone is not proof of isolation or authorization.

The shared fixture uses `cf-lab-200-300` and disposable synthetic objects. It does not authorize changes to nodes, system namespaces, cluster-wide RBAC, admission engines, runtime sensors, audit configuration, CNI, storage backends or physical networks. Such changes require a separate reviewed administrator workflow and recovery plan.

Review every resource in a manifest before applying it, including scope and namespace. Do not pipe an unknown remote installer into a shell. Do not weaken an existing safety guard to make a lesson run. A wrapper adding context/namespace flags is an ergonomics aid, not a hardened sandbox.

Use short connection timeouts and exact resource names. No public listeners, host-path mounts, container escapes, real credential collection, arbitrary metadata probing or unrelated network scans are needed for these core exercises.

## Evidence and privacy

Use synthetic data. Keep credentials, kubeconfigs, private keys, raw internal logs, customer data, internal diagrams and employer-specific mappings outside the public checkout, in an approved location. Do not publish internal material merely because a filename is ignored by Git or because a personal repository is private.

Before any public contribution, review the actual diff and evidence provenance. A claim about a real platform requires its authoritative evidence and appropriate review, not inference from a lab analogy.

Use the [session template](../templates/candidate-zero-session.md). Capture objective, environment, observations, reasoning, remediation/conclusion, verification, assistance, gaps, safe state and resume point. Preserve original incident evidence before repair when appropriate. Do not treat a redacted copy as the unchanged original.

## What counts as a pass

A configured control is not automatically an effective control. Require a legitimate positive test, a meaningful negative test and an explanation of what those observations do and do not prove. Dry-run acceptance, static checks and synthetic packets cannot replace a required live observation.

The [assessment rubric](../assessments/README.md) is a proposed educational rubric to be calibrated through Candidate Zero. It is not an external certification standard. Human review remains responsible for final competency sign-off.
