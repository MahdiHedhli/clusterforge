# Offline validation for the 200/300 curriculum

Run from the repository root with Python 3.10 or newer:

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 tooling/validate_curriculum.py
```

No third-party Python packages, cluster credentials or external network access are needed. The checker does not run lesson commands, provision infrastructure, fetch external links or contact Kubernetes.

## Checks

The checker verifies the four track IDs, six lesson files per track, required lesson sections, draft/runtime statements, four assessment paths, three explicitly synthetic packets, unique JSON object keys and existing repository-relative Markdown link targets. It rejects local links that escape the repository.

The regression suite exercises valid input, missing lessons/sections, broken links, external-link handling, repository escape, duplicate JSON keys, missing synthetic labels, misleading runtime status and duplicate tracks.

The catalog's NOT_RUN and NOT_RECORDED values are the release authoring baseline, not a current learner progress tracker. Record later runtime and learner evidence separately; revise the release metadata and checker deliberately when promoting curriculum maturity.

## Limits

These are structural checks, not Kubernetes API schema validation, shell linting, external URL validation, security certification, factual review or live-control qualification. Links to a document's fragment are checked at file level only. The instructor must still review commands, qualify the environment, verify fault behavior, review evidence and assess the learner.

The public release contains fixture contracts and synthetic case packets, not runnable lab manifests. Static success must not be presented as proof that any exercise has run.
