# snippets/serializers
from rest_framework import serializers
from .models import *
import math


"""Serializer Dummy

class HumiditySerializer(serializers.ModelSerializer):

    class Meta:
        model = Humidity
        fields = ('created', 'value')



"""


class TemperatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Temperature
        fields = ('created', 'value')



class PressureSerializer(serializers.ModelSerializer):

    height = serializers.SerializerMethodField()
    class Meta:
        model = Pressure
        fields = ('created', 'value', 'height')
    
    def get_height(self, obj):
        field_name = 'value'
        field_object = Pressure._meta.get_field(field_name)
        value = field_object.value_from_object(obj)
        
        value2 = (145366.45*(1.0-((value-16)/1013.25)))**0.190284
        return value2

class HumiditySerializer(serializers.ModelSerializer):

    class Meta:
        model = Humidity
        fields = ('created', 'value')


