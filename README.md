# OCX-LIVE-001: OpsChugex Live Service Evidence

**Classification:** Verified live service  
**Scope:** OpsChugex-owned public API only

The validation script calls the public health endpoint and verifies:
- API health
- Database connectivity
- Scheduler state

It does not access customer systems, cloud accounts or credentials.

Run from the repository root:

```bash
python reference-implementations/live-service-evidence/verify_opschugex_api.py
```

A successful CI result is a time-bound verification of the running OpsChugex API. It is not an uptime guarantee or a customer outcome.