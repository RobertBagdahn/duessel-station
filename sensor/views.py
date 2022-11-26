from rest_framework import generics
from .models import Temperature
from .serializers import TemperatureSerializer
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from service.sensor import SensorModule

class TemperatureView(viewsets.ModelViewSet):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer


class SaveTemperature(viewsets.ModelViewSet):

    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

    def create(self, request, *args, **kwargs):
        
        SensorClass = SensorModule()
        SensorClass.add_temperature()
        return Response('Daten wurden geschrieben', status=status.HTTP_200_OK)
