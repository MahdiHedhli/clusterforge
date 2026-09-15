# Contributing to ClusterForge

ClusterForge welcomes contributions that improve practical Kubernetes engineering and security education.

## What makes a good ClusterForge exercise?

A strong exercise should state the competency it measures, use a reproducible environment where practical, require evidence rather than guessing, include a clear verification condition, and test skills that transfer beyond a single vendor or platform.

Troubleshooting exercises should generally follow:

`SYMPTOM -> EVIDENCE -> HYPOTHESIS -> TEST -> ROOT CAUSE -> REMEDIATION -> VERIFICATION`

Security exercises should be safe, isolated, and explicitly scoped to environments the learner owns or is authorized to test.

## Curriculum contributions

When proposing a lesson, lab, challenge, or assessment, include:

- intended track and level
- prerequisites
- learning objectives
- estimated time
- environment requirements
- learner instructions
- expected evidence
- success criteria
- cleanup/reset instructions where relevant
- security and safety considerations

Avoid solutions in learner-facing challenge material when the solution would undermine assessment. Instructor or grading material can be separated as the project evolves.

## Vendor neutrality

Public ClusterForge curriculum should teach transferable concepts. Vendor-specific technologies may be used as examples or lab implementations when appropriate, but exercises should distinguish general competencies from implementation-specific behavior.

Do not contribute confidential, proprietary, employer-internal, customer, or otherwise non-public information.

## Candidate Zero

New practical material should initially be treated as Draft. Candidate Zero testing should record ambiguity, hidden assumptions, accidental shortcuts, difficulty, and whether the exercise actually measures its stated objectives. See `docs/candidate-zero.md`.

## Responsible security training

Adversarial material exists to teach defense, investigation, and authorized security testing. Labs should default to disposable or isolated environments and should not require attacking third-party infrastructure.
