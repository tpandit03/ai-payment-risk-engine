from app.models import PaymentRequest
from app.risk_engine import score_payment

def make_payment(**o):
    d={"transaction_id":"tx-1","amount":100,"currency":"USD","country":"US","customer_age_days":365,"velocity_1h":1,"device_risk":0.1}
    d.update(o); return PaymentRequest(**d)

def test_low_risk_is_approved():
    r=score_payment(make_payment()); assert r["decision"]=="APPROVE" and r["risk_score"]<50

def test_medium_risk_is_reviewed():
    r=score_payment(make_payment(device_risk=0.8,velocity_1h=10)); assert r["decision"]=="REVIEW"

def test_high_risk_is_declined():
    r=score_payment(make_payment(amount=7000,customer_age_days=3,velocity_1h=12,device_risk=0.95,country="ZZ")); assert r["decision"]=="DECLINE"
