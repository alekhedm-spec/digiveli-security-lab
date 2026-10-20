# DigiVeli Security Lab

**Secure AI. Secure Software. Safer World.**

DigiVeli Security Lab (DV-SecLab) is a Finland-based, independent initiative for **defensive cybersecurity research**, secure software engineering, AI agent safety, and responsible open-source collaboration.

> **Status: Foundation v0.1.0 — planning and documentation.** No security findings, independent certifications, production security guarantees, or OpenAI/Daybreak affiliation are claimed by this repository.

## Mission

Make software and AI-enabled systems safer by publishing reproducible defensive methods, independently verified fixes, and actionable learning resources. We work only on systems we own or are explicitly authorized to assess.

## Research areas

1. **AI agent security:** prompt-injection resilience, tool permissions, workspace boundaries, process isolation, and auditability.
2. **Application security:** authentication, authorization, input handling, secure integrations, and regression testing.
3. **Software supply-chain security:** dependency management, CI/CD isolation, least-privilege permissions, and artifact integrity.
4. **Security engineering education:** practical guides, transparent methodology, and responsible disclosure.

## First research track

**AI Harness Security Boundary Validation** — establish a threat model and test plan for agent-to-tool boundaries, workspace isolation, process containment, secret exposure, and provenance. This project does not currently claim verified vulnerabilities or test outcomes.

See [research plan](research/ai-harness-boundaries/PLAN.md), [scope and authorization](docs/SCOPE_AND_AUTHORIZATION.md), and [roadmap](docs/ROADMAP.md).

## Working principles

- **Authorized testing only.** No scanning, exploitation, or testing of third-party systems without explicit authorization and agreed scope.
- **Evidence over claims.** Distinguish hypotheses, reproductions, fixes, and independently confirmed results.
- **Protect people and data.** No real secrets, private logs, customer data, or unpatched exploitation details in public contributions.
- **Human responsibility.** AI assistance does not replace review, consent, or human accountability.
- **Responsible disclosure.** Give affected maintainers a private, reasonable path to resolve issues before publication.

Read [SECURITY.md](SECURITY.md), [CONTRIBUTING.md](CONTRIBUTING.md), and [research policy](docs/SCOPE_AND_AUTHORIZATION.md) before participating.

## Project status

- [x] Public repository and project charter prepared
- [ ] Review and approve the initial project documentation
- [ ] Choose an open-source license before publishing reusable implementation code
- [ ] Configure GitHub private vulnerability reporting, branch protection, and security features
- [ ] Complete first authorized AI Harness threat model
- [ ] Add a reproducible defensive regression test suite
- [ ] Publish a reviewed, non-sensitive research report

## Language and collaboration

English is the default for publicly shared technical documentation. Finnish summaries may be published for accessibility. Constructive contributions are welcome within the rules in [CONTRIBUTING.md](CONTRIBUTING.md).

## Independence and trademarks

DigiVeli Security Lab is an independent project. References to OpenAI Daybreak, OWASP, CISA, ENISA, or other organizations do not imply sponsorship, approval, membership, or affiliation.

## License status

**No license has been selected yet.** Public availability of these files does not grant permission to reuse or redistribute them. A license decision will be made before accepting external code contributions or publishing reusable software.
