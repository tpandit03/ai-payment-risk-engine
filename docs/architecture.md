# Architecture Notes

1. Client sends a payment-risk request.
2. FastAPI validates the contract.
3. Deterministic rules produce signals.
4. The engine creates a bounded 0-100 score.
5. A policy maps the score to APPROVE, REVIEW, or DECLINE.
6. Reasons provide explainability.

## Production evolution

Kafka/event streaming, Redis velocity features, PostgreSQL policy/audit storage, feature store integration, model serving behind the same interface, OpenTelemetry, immutable audit storage, policy versioning, human review, and Kubernetes deployment are natural next steps.
