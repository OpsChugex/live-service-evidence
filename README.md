# OCX-LIVE-001: OpsChugex Live Service Evidence

[![Verify OpsChugex live service](https://github.com/OpsChugex/live-service-evidence/actions/workflows/verify.yml/badge.svg)](https://github.com/OpsChugex/live-service-evidence/actions/workflows/verify.yml)

**Classification:** Verified live-service check

**Scope:** OpsChugex-owned public API only

This repository verifies the public health contract of the OpsChugex API. The check confirms:

- HTTPS endpoint responds successfully
- API reports a healthy service state
- service identity is `opschugex-api`
- database reports connected
- scheduler reports running
- observed request latency is recorded
- UTC verification time is recorded

It does not access customer systems, cloud accounts or credentials.

## Run locally

```bash
python verify_opschugex_api.py
python verify_opschugex_api.py --output evidence.json
```

The JSON output is suitable for a time-bound evidence record.

## Automated evidence

GitHub Actions runs the same verification on changes, on manual request and once daily. Each successful run uploads a JSON evidence artifact retained for 30 days.

The workflow has read-only repository permissions and all actions are pinned to immutable commit SHAs.

## Evidence interpretation

A successful result proves only that the public OpsChugex health endpoint satisfied the documented contract at the recorded time.

It is **not** an uptime guarantee, SLA result, customer outcome, penetration test, SOC 2 attestation or proof that every internal dependency is healthy.
