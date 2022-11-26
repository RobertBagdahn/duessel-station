from rest_framework import generics
from .models import Temperature
from .serializers import TemperatureSerializer

class TemperatureView(generics.ListCreateAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer
