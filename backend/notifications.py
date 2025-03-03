from twilio.rest import Client

# Twilio Credentials
ACCOUNT_SID = "your_twilio_sid"
AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_PHONE = "your_twilio_phone_number"

def send_alert(worker_id, message):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    phone_number = get_worker_phone(worker_id)  # Fetch from database
    
    if phone_number:
        client.messages.create(body=message, from_=TWILIO_PHONE, to=phone_number)
        print(f"Alert sent to {worker_id}: {message}")
    else:
        print("⚠️ Worker phone number not found!")

def get_worker_phone(worker_id):
    # Simulate fetching worker phone number from database
    worker_phones = {"worker_1": "+1234567890", "worker_2": "+0987654321"}
    return worker_phones.get(worker_id)