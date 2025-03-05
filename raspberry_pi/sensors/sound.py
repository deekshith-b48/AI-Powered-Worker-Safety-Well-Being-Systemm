import random

class SoundSensor:
    def __init__(self):
        pass

    def detect_distress_call(self):
        return random.choice([True, False])

if __name__ == "__main__":
    sensor = SoundSensor()
    print(sensor.detect_distress_call())