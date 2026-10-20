# AI Harness Security Boundary Validation — Research Plan

**Status:** Proposed; no execution or findings claimed.
**Objective:** Validate that AI-assisted workflows respect explicitly authorized tool, workspace, process, and evidence boundaries.

## Initial system model

Candidate boundaries: user intent → agent planning → tool invocation → workspace filesystem → process execution → network calls → evidence store / CI.

The actual implementation, scope, and controls must be verified from the specific repository commit before drawing conclusions.

## Defensive test hypotheses

| ID | Risk | Desired control | Proposed safe fixture |
| --- | --- | --- | --- |
| AH-001 | Untrusted instructions alter tool use | Untrusted content cannot override authorized instructions | Local harmless document containing conflicting directions |
| AH-002 | Path traversal or symlink escape | Filesystem operations remain within allowed workspace | Temporary fixture directory and external sentinel file |
| AH-003 | Child process survives run cancellation | Descendant processes are terminated and accounted for | Local sleep subprocess tree in a disposable sandbox |
| AH-004 | Secrets exposed in logs or traces | Sensitive strings are redacted, never exported | Synthetic canary credential only |
| AH-005 | Evidence integrity ambiguous | Changes to evidence invalidate integrity checks | Non-sensitive fixture artifact with expected digest |
| AH-006 | CI job has excess privileges | Jobs use least-privilege identities and trusted inputs | Static review of workflow permissions |

## Method

1. Obtain and record authorization for the **exact** source and test environment.
2. Inventory source, existing tests, known fixes, and expected behavior.
3. Create isolated fixtures; avoid production credentials and external targets.
4. Execute one bounded test at a time; collect sanitized observations.
5. Separate expected behavior, actual result, environmental errors, and limitations.
6. Privately coordinate genuine unpatched findings; publish only reviewed defensive outcomes.

## Completion evidence

- Versioned threat model with accepted assumptions
- Test matrix with pass / fail / inconclusive and reproduction context
- At least three safe automated regression tests and code-reviewed fixes **if needed**
- Sanitized public report approved for release

## Stop conditions

Immediately stop on unexpected access to third-party systems, real credentials, non-test data, production impact, unclear permission, or unstable isolation.
