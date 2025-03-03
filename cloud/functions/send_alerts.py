import requests

def send_worker_alert(worker_id, message):
    phone_number = get_worker_phone(worker_id)
    if phone_number:
        sms_api_url = "https://api.smsprovider.com/send"
        payload = {"to": phone_number, "message": message}
        requests.post(sms_api_url, json=payload)
        print(f"Alert sent to {worker_id}: {message}")
    else:
        print("⚠️ Worker phone number not found!")

def get_worker_phone(worker_id):
    worker_phones = {"worker_1": "+1234567890", "worker_2": "+0987654321"}
    return worker_phones.get(worker_id)