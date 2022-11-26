import environ
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()
from random import *

from sensor import models as sensor_models

class SensorModule:
    def get_dummy_temperature(self):
        smallest = 19
        largest = 25

        return randint(smallest, largest - 1)
    
    def get_sensor_temperature(self):
        # todo for Julius
        return 1

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
