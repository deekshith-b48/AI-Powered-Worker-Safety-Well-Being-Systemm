import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("path/to/firebase_config.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def save_worker_data(worker_id, data):
    db.collection("workers").document(worker_id).set(data, merge=True)

def get_worker_status(worker_id):
    doc = db.collection("workers").document(worker_id).get()
    return doc.to_dict() if doc.exists else {"error": "Worker not found"}