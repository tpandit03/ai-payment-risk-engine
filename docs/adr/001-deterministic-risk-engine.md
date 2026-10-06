# ADR 001: Deterministic Risk Engine

## Decision
Use a deterministic rule engine as the baseline decision layer.

## Why
Payment decisions need repeatability, explainability, low latency, and predictable failure modes. An ML model can be introduced behind the same interface later.

## Consequence
The baseline is transparent and testable; it is not a validated production fraud model.
