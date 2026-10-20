# Research Scope and Authorization Policy

## Default rule

**Nothing is authorized merely because it is reachable or public.** Conduct active security tests only against environments owned by the tester or explicitly approved in writing by the responsible owner.

## Initial permitted environments

- Local disposable test fixtures created specifically for research.
- Lab copies of software owned and controlled by the repository maintainer.
- Separately approved third-party projects with a documented security policy and permission to test the exact target and method.

**Out of scope until separately authorized:** production customer systems, partner repositories, unknown internet hosts, services under third-party ownership, and any infrastructure containing real user data.

## Authorization record (template)

| Field | Record |
| --- | --- |
| Owner / approving party | TBD |
| Target(s) / commit(s) | TBD |
| Environment | TBD |
| Permitted methods | TBD |
| Excluded methods/assets | TBD |
| Dates and contact | TBD |
| Data handling / retention | TBD |
| Stop conditions | TBD |

Store actual signed permissions and sensitive details **outside** the public repository.

## Safety controls

- Prefer offline fixtures, container/sandbox boundaries, test accounts, and synthetic credentials.
- Limit rates and resource use; do not affect availability without specific permission.
- Stop immediately on unexpected personal data, production impact, or scope uncertainty.
- Redact secrets, internal endpoints, and identifying user information from public results.
- Handle suspected vulnerabilities privately per [SECURITY.md](../SECURITY.md).
- Keep AI-generated conclusions provisional until validated by a human.

## Publication gate

Before making a research report public, confirm authorization, accuracy, remediation/disclosure status, redaction, reproducibility with synthetic data, and absence of unnecessary exploit detail.
