import random

class PIRSensor:
    def __init__(self):
        pass

    def detect_motion(self):
        return random.choice([True, False])

if __name__ == "__main__":
    sensor = PIRSensor()
    print(sensor.detect_motion())