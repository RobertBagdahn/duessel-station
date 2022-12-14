from sensor import models as sensor_models
from random import *
import environ
import time
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()
if env.bool('IS_RASPBERRY'):
    from sense_hat import SenseHat

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
    # temp
    def get_dummy_temperature(self):
        smallest = 19
        largest = 25

        return randint(smallest, largest - 1)
    
    def get_sensor_temperature(self):
        # todo for Julius
        sense = SenseHat()
        sense.clear()
        
        temperature = 0
        j=0
        for i in range(10):
            temperature = temperature + sense.get_temperature_from_pressure()
            time.sleep(0.01)
            j= j+1

        temperature = round(temperature/j, 1)
        
        print(temperature)

        return temperature

    def add_temperature(self):

        is_raspberry = env.bool('IS_RASPBERRY')
        if is_raspberry:
            temperature = 0
            for i in range(10):
                temperature = temperature + self.get_sensor_temperature()
                time.sleep(0.05)

            temperature = temperature/10
            temperature = round(temperature, 1)
            sensor_models.Temperature.objects.create(value=temperature)

        else:
            print('Ich bin Lokal')
            temperature = self.get_dummy_temperature()
            sensor_models.Temperature.objects.create(value=temperature)
            print(temperature)
        return True

    # pressure
    def get_dummy_pressure(self):
        smallest = 19
        largest = 25

        return randint(smallest, largest - 1)

    def get_sensor_pressure(self):
        sense = SenseHat()
        sense.clear()
       
        pressure = 0
        j = 0
    
        for i in range(10):
            pressure_moment = sense.get_pressure()
            if pressure_moment>0:
                j = j+1
            pressure = pressure + pressure_moment
            time.sleep(0.01)
            

        pressure = round(pressure/j, 3)
        print(pressure)
        return pressure-6.0

    def add_pressure(self):
        is_raspberry = env.bool('IS_RASPBERRY')
        if is_raspberry:
            pressure = self.get_sensor_pressure()
            sensor_models.Pressure.objects.create(value=pressure)
        else:
            print('Ich bin Lokal')
            pressure = self.get_dummy_temperature()
            sensor_models.Pressure.objects.create(value=pressure)
            print(pressure)
        return True

    # humidity

    def get_dummy_humidity(self):
        smallest = 0
        largest = 100

        return randint(smallest, largest - 1)

    def get_sensor_humidity(self):
        # todo for Julius
        sense = SenseHat()
        sense.clear()

        humidity = 0
        j = 0
        for i in range(10):
            humidity = humidity + sense.get_humidity()
            time.sleep(0.05)
            j = j+1

        humidity = round(humidity/j, 1)
 

        if humidity > 100:
            humidity = 100.0
            
        print(humidity)
        return humidity

    def add_humidity(self):
        is_raspberry = env.bool('IS_RASPBERRY')
        if is_raspberry:
            humidity = self.get_sensor_humidity()
            sensor_models.Humidity.objects.create(value=humidity)
        else:
            print('Ich bin Lokal')
            humidity = self.get_dummy_humidity()
            sensor_models.Humidity.objects.create(value=humidity)
            print(humidity)
        return True
