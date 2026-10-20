# Roadmap

This is a proposal, not a record of completed security validation.

## F0 — Foundation and governance

- [x] Repository established (confirmed by maintainer screenshot, 2026-10-20)
- [ ] Review and commit foundation documents
- [ ] Confirm security contact method and enable private vulnerability reporting
- [ ] Protect default branch and enable appropriate dependency alerts
- [ ] Select an explicit license before publishing reusable code

## F1 — AI Harness threat model

- [ ] Inventory assets, entry points, data flows, trust boundaries, and agent permissions
- [ ] Document authorization and non-production fixtures
- [ ] Prioritize prompt injection, tool execution, workspace access, secret exposure, process groups, and evidence integrity

## F2 — Defensive validation

- [ ] Build local, isolated test fixtures with synthetic secrets
- [ ] Record expected/observed outcomes and environment details
- [ ] Fix reproducible failures and add regression coverage
- [ ] Review results independently where feasible

## F3 — Software supply-chain safety

- [ ] Review CI permissions and action dependencies
- [ ] Enable dependency scanning and review artifact provenance
- [ ] Document secure defaults and operational runbooks

## F4 — Community publication

- [ ] Publish reviewed results without sensitive unresolved vulnerability details
- [ ] Create accessible guidance in English; add Finnish summaries
- [ ] Contribute improvements upstream through approved maintainer channels

## Exit criteria

Each phase advances only with recorded evidence, explicit scope, and reviewable artifacts. Passing a local test does not prove universal security.
