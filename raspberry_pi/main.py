import threading
import time
import requests
from queue import Queue
from sensors.fingerprint import FingerprintSensor
from sensors.ultrasonic import UltrasonicSensor
from sensors.pir import PIRSensor
from sensors.sound import SoundSensor
from sensors.temperature import TemperatureSensor
from alerts import trigger_alert
from config import SERVER_URL

data_queue = Queue()

fingerprint_sensor = FingerprintSensor()
ultrasonic_sensor = UltrasonicSensor()
pir_sensor = PIRSensor()
sound_sensor = SoundSensor()
temperature_sensor = TemperatureSensor()

def read_sensor_data():
    data = {}
    try:
        data["fingerprint"] = fingerprint_sensor.authenticate_user()
    except Exception as e:
        print(f"Error reading fingerprint sensor: {e}")
        data["fingerprint"] = None

    try:
        data["distance"] = ultrasonic_sensor.get_distance()
    except Exception as e:
        print(f"Error reading ultrasonic sensor: {e}")
        data["distance"] = None

    try:
        data["motion"] = pir_sensor.detect_motion()
    except Exception as e:
        print(f"Error reading PIR sensor: {e}")
        data["motion"] = None

    try:
        data["sound"] = sound_sensor.detect_distress_call()
    except Exception as e:
        print(f"Error reading sound sensor: {e}")
        data["sound"] = None

    try:
        data["temperature"] = temperature_sensor.get_temperature()
    except Exception as e:
        print(f"Error reading temperature sensor: {e}")
        data["temperature"] = None
    
    data_queue.put(data)

def send_data_to_server():
    while True:
        data = data_queue.get()
        try:
            if data["motion"] or data["sound"] or data["temperature"] > 40:
                trigger_alert(data)
            requests.post(f"{SERVER_URL}/rpi-sensor-data", json=data)
        except Exception as e:
            print(f"Error sending data to server: {e}")
        finally:
            data_queue.task_done()
        time.sleep(2)

if __name__ == "__main__":
    sensor_thread = threading.Thread(target=read_sensor_data)
    sensor_thread.daemon = True
    sensor_thread.start()

    server_thread = threading.Thread(target=send_data_to_server)
    server_thread.daemon = True
    server_thread.start()

    while True:
        time.sleep(0.1)
