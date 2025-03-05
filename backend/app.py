from flask import Flask, request, jsonify
from database import save_worker_data, get_worker_status
from ai_model import analyze_risk
from notifications import send_alert

app = Flask(__name__)

# Endpoint to receive IoT sensor data from Raspberry Pi
@app.route("/rpi-sensor-data", methods=["GET"])
def rpi_sensor_data():
    data = request.args  # Receive data from Raspberry Pi
    worker_id = data.get("worker_id")
    
    # Save data to Firebase
    save_worker_data(worker_id, data)
    
    # Analyze Risk Level
    risk_level = analyze_risk(data)
    
    # If high risk detected, send alert
    if risk_level == "high":
        send_alert(worker_id, "⚠️ High Risk Detected! Immediate Action Needed.")
    
    return jsonify({"status": "Data received", "risk_level": risk_level})

# Endpoint to receive IoT sensor data
@app.route("/sensor-data", methods=["POST"])
def sensor_data():
    data = request.json  # Receive data from other sources
    worker_id = data.get("worker_id")
    
    # Save data to Firebase
    save_worker_data(worker_id, data)
    
    # Analyze Risk Level
    risk_level = analyze_risk(data)
    
    # If high risk detected, send alert
    if risk_level == "high":
        send_alert(worker_id, "⚠️ High Risk Detected! Immediate Action Needed.")
    
    return jsonify({"status": "Data received", "risk_level": risk_level})

# Endpoint to fetch worker status for the dashboard
@app.route("/worker-status/<worker_id>", methods=["GET"])
def worker_status(worker_id):
    status = get_worker_status(worker_id)
    return jsonify(status)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)