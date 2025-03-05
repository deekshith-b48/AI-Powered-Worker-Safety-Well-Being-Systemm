import random

class TemperatureSensor:
    def __init__(self):
        pass

    def get_temperature(self):
        return random.uniform(20, 45)  # Simulated temperature in Celsius

if __name__ == "__main__":
    sensor = TemperatureSensor()
    print(sensor.get_temperature())