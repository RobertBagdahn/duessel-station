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

    def add_temperature(self):

        is_raspberry = env.bool('IS_RASPBERRY')
        if is_raspberry:
            print('Ich bin auf dem Raspberry')
        else:
            print('Ich bin Lokal')
            temperature = self.get_dummy_temperature()
            sensor_models.Temperature.objects.create(value = temperature)
            print(temperature)
        return True
