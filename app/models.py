from pydantic import BaseModel, Field

class PaymentRequest(BaseModel):
    transaction_id: str = Field(min_length=3)
    amount: float = Field(gt=0)
    currency: str = Field(min_length=3, max_length=3)
    country: str = Field(min_length=2, max_length=2)
    customer_age_days: int = Field(ge=0)
    velocity_1h: int = Field(ge=0)
    device_risk: float = Field(ge=0, le=1)

class RiskResponse(BaseModel):
    transaction_id: str
    decision: str
    risk_score: int
    reasons: list[str]
