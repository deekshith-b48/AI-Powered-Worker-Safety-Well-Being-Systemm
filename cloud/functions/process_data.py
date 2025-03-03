from ai_analysis import analyze_worker_risk

def process_worker_data(worker_id):
    risk_level = analyze_worker_risk(worker_id)
    if risk_level == "high":
        from send_alerts import send_worker_alert
        send_worker_alert(worker_id, "⚠️ High-Risk Detected! Immediate Action Needed!")
    return risk_level