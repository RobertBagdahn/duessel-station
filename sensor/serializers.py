# snippets/serializers
from rest_framework import serializers
from .models import Temperature
from .models import Pressure


class TemperatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Temperature
        fields = ('created', 'value')



class PressureSerializer(serializers.ModelSerializer):

    height = serializers.SerializerMethodField()
    class Meta:
        model = Pressure
        fields = ('created', 'value', 'height')
    
    def get_height(self, object):
        return 1


