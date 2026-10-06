def evaluate_rules(payment):
    reasons=[]
    score=0
    if payment.device_risk >= 0.70:
        score += 30; reasons.append("high_device_risk")
    elif payment.device_risk >= 0.40:
        score += 15; reasons.append("medium_device_risk")
    if payment.velocity_1h >= 10:
        score += 30; reasons.append("high_velocity")
    elif payment.velocity_1h >= 5:
        score += 15; reasons.append("elevated_velocity")
    if payment.customer_age_days < 30:
        score += 20; reasons.append("new_customer")
    if payment.amount >= 5000:
        score += 15; reasons.append("high_value_transaction")
    if payment.country not in {"US","CA","GB","IN","AU"}:
        score += 10; reasons.append("country_outside_core_market")
    return min(score,100), reasons
