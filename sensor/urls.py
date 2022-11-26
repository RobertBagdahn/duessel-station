
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from sensor import views

urlpatterns = [
    path('temperature/', views.TemperatureView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
