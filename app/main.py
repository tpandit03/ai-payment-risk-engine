from fastapi import FastAPI
from .models import PaymentRequest,RiskResponse
from .risk_engine import score_payment

app=FastAPI(title="AI Payment Risk Decision Engine",version="1.0.0",description="Explainable deterministic payment risk scoring reference implementation.")

@app.get("/health")
def health(): return {"status":"ok"}

@app.post("/v1/risk/score",response_model=RiskResponse)
def risk_score(payment: PaymentRequest): return score_payment(payment)
