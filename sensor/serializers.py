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
    
    def get_height(self, obj):
        field_name = 'value'
        field_object = Pressure._meta.get_field(field_name)
        value = field_object.value_from_object(obj)
        return 1


