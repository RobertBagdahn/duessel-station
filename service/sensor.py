import environ
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()
from random import *
if env.bool('IS_RASPBERRY'):
    from sense_hat import SenseHat

from sensor import models as sensor_models

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

        temperature = sense.get_temperature_from_pressure()
        temperature = round(temperature, 1)
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