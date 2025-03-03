def main():
    from sensors.fingerprint import authenticate_user
    from sensors.ultrasonic import get_distance
    from sensors.pir import detect_motion
    from sensors.sound import detect_distress_call
    from sensors.temperature import get_temperature
    from alerts import trigger_alert
    from config import SERVER_URL
    import requests
    import time

    while True:
        data = {
            "fingerprint": authenticate_user(),
            "distance": get_distance(),
            "motion": detect_motion(),
            "sound": detect_distress_call(),
            "temperature": get_temperature()
        }
        
        if data["motion"] or data["sound"] or data["temperature"] > 40:
            trigger_alert()
        
        requests.post(f"{SERVER_URL}/api/data", json=data)
        time.sleep(2)

if __name__ == "__main__":
    main()
