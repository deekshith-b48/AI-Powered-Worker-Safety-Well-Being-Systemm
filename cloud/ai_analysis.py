import numpy as np
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firebase_config.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def analyze_worker_risk(worker_id):
    doc = db.collection("workers").document(worker_id).get()
    if not doc.exists:
        return "Worker data not found"
    
    data = doc.to_dict()
    heart_rate = data.get("heart_rate", 70)
    temperature = data.get("temperature", 36.5)
    
    # AI-Based Risk Calculation
    if heart_rate > 100 or temperature > 38:
        risk = "high"
    elif 80 <= heart_rate <= 100:
        risk = "moderate"
    else:
        risk = "low"
    
    # Save risk level in the database
    db.collection("workers").document(worker_id).update({"risk_level": risk})
    return risk
