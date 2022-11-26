from django.db import models

class Temperature(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"{str(self.created)} -  {str(self.value)}"

class Pressure(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"{str(self.created)} -  {str(self.value)}"
