from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)

def test_health():
    r=client.get("/health"); assert r.status_code==200 and r.json()["status"]=="ok"

def test_risk_endpoint():
    r=client.post("/v1/risk/score",json={"transaction_id":"tx-1001","amount":1250,"currency":"USD","country":"US","customer_age_days":14,"velocity_1h":8,"device_risk":0.72})
    assert r.status_code==200 and r.json()["decision"]=="REVIEW"
