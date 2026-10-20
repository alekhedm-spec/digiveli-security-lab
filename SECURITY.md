# Security Policy

DigiVeli Security Lab takes vulnerability reports and coordinated disclosure seriously.

## Reporting a suspected vulnerability

**Do not submit a public GitHub issue, discussion, pull request, or comment containing exploit instructions, secrets, private data, or details of an unpatched vulnerability.**

If GitHub **Private vulnerability reporting** is enabled, use the repository's **Security → Report a vulnerability** feature. If it is not enabled, use a private contact method published by the repository maintainer; if none is published, request a private contact channel without disclosing technical exploit details. Do not assume an unpublished email address.

Helpful information in a private report:

- Affected component and version/commit, when known
- Clear reproduction steps using synthetic test data
- Impact and prerequisites, with uncertainty marked
- Suggested mitigation, if available
- Whether the issue has already been disclosed elsewhere

Please do not send credentials, customer data, sensitive log files, or destructive proof-of-concepts. Arrange a secure evidence channel if needed.

## Safe research boundaries

Only systems you own or have **explicit, documented permission** to test are in scope. A public repository, domain, or publicly accessible service is **not** permission to test it. Avoid availability-impacting activity, credential attacks, social engineering, persistence, and collection of personal data unless explicitly authorized by the system owner and legally permitted.

## Disclosure and handling

We aim to acknowledge reports, establish a private communication channel, assess impact, coordinate with affected maintainers, and publish only after a suitable remediation and disclosure decision. No fixed response or remediation deadline is promised at this early project stage.

Research notes or unconfirmed findings must not be presented as verified vulnerabilities. Public reports should redact secrets and sensitive technical details that could cause harm before mitigation.

## GitHub configuration needed

Repository maintainers should review **Settings → Code security and analysis / Advanced Security** (names may vary), enable **Private vulnerability reporting**, configure dependency alerts as applicable, and protect the default branch. These settings are not automatically enabled by this document.
