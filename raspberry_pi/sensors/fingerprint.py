import random

class FingerprintSensor:
    def __init__(self):
        pass

    def authenticate_user(self):
        return random.choice(["Authorized", "Unauthorized"])

if __name__ == "__main__":
    sensor = FingerprintSensor()
    print(sensor.authenticate_user())