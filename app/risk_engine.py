from .rules import evaluate_rules

def score_payment(payment):
    score,reasons=evaluate_rules(payment)
    decision="DECLINE" if score>=75 else "REVIEW" if score>=50 else "APPROVE"
    return {"transaction_id":payment.transaction_id,"decision":decision,"risk_score":score,"reasons":reasons}
