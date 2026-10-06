# Threat Model

| Threat | Example | Control |
|---|---|---|
| Input tampering | modified amount/device risk | validation + trusted upstream claims |
| Replay | duplicate request | idempotency key |
| Abuse | request flooding | gateway rate limiting |
| Data leakage | PII in logs | redaction + structured logging |
| Policy manipulation | unauthorized rule changes | RBAC + approvals |
| Model drift | reduced detection quality | monitoring + evaluation |

The sample project uses synthetic attributes only.
