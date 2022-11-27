import environ
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()
from random import *
if env.bool('IS_RASPBERRY'):
    from sense_hat import SenseHat
from sensor import models as sensor_models

"""Sensor Dummy

    #humidity
    def get_dummy_humidity(self):
        smallest = 0
        largest = 100

        return randint(smallest, largest - 1)

    def get_sensor_humidity(self):
        # todo for Julius
        sense = SenseHat()
        sense.clear()
        humidity = sense.get_humidity()
        humidity = round(humidity, 1)
        print(humidity)

        if humidity > 100:
            humidity = 100.0

        return humidity

    def add_humidity(self):
        is_raspberry = env.bool('IS_RASPBERRY')
        if is_raspberry:
            humidity = self.get_sensor_humidity()
            sensor_models.Humidity.objects.create(value = humidity)
        else:
            print('Ich bin Lokal')
            humidity = self.get_dummy_humidity()
            sensor_models.Humidity.objects.create(value = humidity)
            print(humidity)
        return True

"""


class SensorModule:
    #temp
    def get_dummy_temperature(self):
        smallest = 19
        largest = 25

        return randint(smallest, largest - 1)
    
    def get_sensor_temperature(self):
        # todo for Julius
        sense = SenseHat()
        sense.clear()
        
        temperature = 0
        for i in range(10):
            temperature = temperature + sense.get_temperature_from_pressure()
            time.sleep(0.01)

        temperature = round(temperature/10, 1)
        
        print(temperature)

        return temperature

    def add_temperature(self):

        is_raspberry = env.bool('IS_RASPBERRY')
        if is_raspberry:
            temperature = self.get_sensor_temperature()
            sensor_models.Temperature.objects.create(value = temperature)
        else:
            print('Ich bin Lokal')
            temperature = self.get_dummy_temperature()
            sensor_models.Temperature.objects.create(value = temperature)
            print(temperature)
        return True

    #pressure
    def get_dummy_pressure(self):
        smallest = 19
        largest = 25

        return randint(smallest, largest - 1)

    def get_sensor_pressure(self):
        # todo for Julius
        sense = SenseHat()
        sense.clear()
        pressure = sense.get_pressure()
        pressure = round(pressure, 1)
        print(pressure)

        return pressure

    def add_pressure(self):
        is_raspberry = env.bool('IS_RASPBERRY')
        if is_raspberry:
            pressure = self.get_sensor_pressure()
            sensor_models.Pressure.objects.create(value = pressure)
        else:
            print('Ich bin Lokal')
            pressure = self.get_dummy_temperature()
            sensor_models.Pressure.objects.create(value = pressure)
            print(pressure)
        return True



    #humidity
    def get_dummy_humidity(self):
        smallest = 0
        largest = 100

        return randint(smallest, largest - 1)

    def get_sensor_humidity(self):
        # todo for Julius
        sense = SenseHat()
        sense.clear()
        humidity = sense.get_humidity()
        humidity = round(humidity, 1)
        print(humidity)

        if humidity > 100:
            humidity = 100.0

        return humidity

    def add_humidity(self):
        is_raspberry = env.bool('IS_RASPBERRY')
        if is_raspberry:
            humidity = self.get_sensor_humidity()
            sensor_models.Humidity.objects.create(value = humidity)
        else:
            print('Ich bin Lokal')
            humidity = self.get_dummy_humidity()
            sensor_models.Humidity.objects.create(value = humidity)
            print(humidity)
        return True
