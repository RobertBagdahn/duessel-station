from django.urls import include, path
from rest_framework_nested import routers

from . import views

router = routers.SimpleRouter()
router.register(r'temperature', views.TemperatureView)
router.register(r'save-temperature', views.SaveTemperature, basename="temperature")

urlpatterns = [
    path('', include(router.urls)),
]
