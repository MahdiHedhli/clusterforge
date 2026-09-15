# Candidate Zero

Candidate Zero is ClusterForge's curriculum dogfooding and evidence model.

A lesson is not considered effective simply because its author believes it teaches the intended skill. Candidate Zero completes the material as a learner, records the investigation process, and evaluates whether successful completion demonstrates the competency the lesson claims to measure.

## Principles

### Evidence over completion

A checked box is weak evidence. ClusterForge records how a learner reached an answer, what evidence they gathered, what hypotheses they formed, and how they verified remediation.

### Diagnose before changing

Troubleshooting scenarios should discourage random configuration changes. Use the standard investigation chain:

```text
SYMPTOM
  |
EVIDENCE
  |
HYPOTHESIS
  |
TEST
  |
ROOT CAUSE
  |
REMEDIATION
  |
VERIFICATION
```

### Practical competency over trivia

Assessments should prefer tasks such as deploying, troubleshooting, securing, investigating, threat modeling, and explaining systems. Knowledge questions are useful when they validate the mental model required for those tasks.

### Explain it

Technical competency includes communication. Learners should be able to explain what failed, why it failed, what risk existed, what changed, and what tradeoffs the remediation introduced.

### Preserve failures

A failed attempt can provide more curriculum evidence than an immediate success. Candidate Zero should record misleading instructions, hidden prerequisites, unrealistic failure modes, accidental shortcuts, and places where a lab tests something other than its stated objective.

## Candidate Zero record

For each lab or scenario, capture:

```markdown
# Candidate Zero Record

## Exercise

## Objective

## Starting confidence

## Symptom / task

## Evidence collected

## Hypotheses

## Tests performed

## Root cause or conclusion

## Remediation

## Verification

## Explanation / customer briefing

## Competencies demonstrated

## Gaps discovered

## Lab quality notes

## Difficulty (1-5)

## Suggested changes
```

## Maturity

Suggested curriculum maturity states:

- **Draft:** authored but not completed by Candidate Zero.
- **Candidate Zero:** completed at least once with evidence captured.
- **Validated:** repeated successfully and reviewed for objective alignment.
- **Stable:** suitable for broader learners with known prerequisites and scoring criteria.

## Why this matters

ClusterForge is intended to measure whether someone can operate and reason about real systems. Candidate Zero provides a feedback loop between curriculum design and actual learner behavior, and creates structured data that can later support human or agent-assisted assessment.
