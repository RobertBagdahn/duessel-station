from rest_framework import generics
from .models import *
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from .serializers import *

from service.sensor import SensorModule

# temperature


class TemperatureView(viewsets.ModelViewSet):
    queryset = Temperature.objects.all().order_by('-created')
    serializer_class = TemperatureSerializer


class SaveTemperature(viewsets.ModelViewSet):

    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

    def create(self, request, *args, **kwargs):

        SensorClass = SensorModule()
        SensorClass.add_temperature()
        return Response('Daten wurden geschrieben', status=status.HTTP_200_OK)

# pressure


class PressureView(viewsets.ModelViewSet):
    queryset = Pressure.objects.all().order_by('-created')
    serializer_class = PressureSerializer


class SavePressure(viewsets.ModelViewSet):

    queryset = Pressure.objects.all()
    serializer_class = PressureSerializer

    def create(self, request, *args, **kwargs):

        SensorClass = SensorModule()
        SensorClass.add_pressure()
        return Response('Daten wurden geschrieben', status=status.HTTP_200_OK)


class HumidityView(viewsets.ModelViewSet):
    queryset = Humidity.objects.all().order_by('-created')
    serializer_class = HumiditySerializer


class SaveHumidity(viewsets.ModelViewSet):

    queryset = Humidity.objects.all()
    serializer_class = HumiditySerializer

    def create(self, request, *args, **kwargs):

        SensorClass = SensorModule()
        SensorClass.add_humidity()
        return Response('Daten wurden geschrieben', status=status.HTTP_200_OK)
