# Practical assessment rubric

This is a proposed ClusterForge educational rubric, not an external certification scoring standard. Calibrate it using Candidate Zero outcomes before treating it as stable.

## Gates

| Gate | Brief |
| --- | --- |
| [K8S-200](k8s-200.md) | Restore an unsuccessful release from evidence |
| [SEC-200](sec-200.md) | Implement and verify a scoped access request |
| [K8S-300](k8s-300.md) | Harden a workload while preserving legitimate behavior |
| [SEC-300](sec-300.md) | Review and defend a customer security architecture |

## Scoring

| Dimension | Points | Full-credit evidence |
| --- | ---: | --- |
| Technical outcome | 25 | Required function works; prohibited behavior fails where specified |
| Evidence quality | 25 | Attributable observations, timestamps, before/after state and limitations |
| Reasoning | 20 | Competing hypotheses, justified minimal changes and residual risk |
| Scope and safety | 15 | Correct target, authorized changes, no secret disclosure or unsafe shortcut |
| Communication | 10 | Clear root cause/design rationale, impact, uncertainty and next action |
| Reset and handoff | 5 | Verified safe state and exact resume point |
| Total | 100 | |

Proposed pass: at least 80/100, at least half the available points in every dimension, and all 15 scope/safety points. Every explicitly required positive/negative test must also pass. Meeting the score without a required live observation does not satisfy an implementation gate.

A safety error stops the attempt for review and recovery. Correcting an unsafe action does not erase the event from the record. Do not intentionally permit harmful actions merely to test whether a learner notices.

## Assistance

H0: ordinary reference documentation, no scenario hints. H1: clarifying question. H2: directed investigative clue. H3: a concrete fix or solution. Record all assistance. An H3 attempt is guided practice; use a fresh unseen variant to demonstrate independent diagnosis. Do not subtract points mechanically without considering which competency the hint supplied.

## Assessor workflow

Confirm prerequisites and a working baseline. Select a compatible fault or requirement variant from the [instructor guide](../instructors/levels-200-300.md). Verify the intended symptom and recovery on the actual lab version before delivery. Keep the variant/answer out of learner and tutoring-agent context.

Assess the learner's observed investigation, not just the final state. Ask a short oral defense and a changed-assumption question. Record separate analytical, live-control and administrator qualifications. Use [Candidate Zero records](../templates/candidate-zero-session.md) to identify the next targeted practice task.

Automated checks may validate artifacts and deterministic assertions. They do not infer understanding, independent authorship, safe judgment or customer readiness.
