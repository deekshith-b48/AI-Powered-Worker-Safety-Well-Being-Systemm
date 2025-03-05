import random

class UltrasonicSensor:
    def __init__(self):
        pass

    def get_distance(self):
        return random.uniform(0.1, 5.0)  # Simulated distance in meters

if __name__ == "__main__":
    sensor = UltrasonicSensor()
    print(sensor.get_distance())