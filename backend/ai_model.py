import numpy as np

def analyze_risk(data):
    heart_rate = data.get("heart_rate", 70)
    temperature = data.get("temperature", 36.5)
    
    # Simple risk analysis logic
    if heart_rate > 100 or temperature > 38:
        return "high"
    elif 80 <= heart_rate <= 100:
        return "moderate"
    else:
        return "low"