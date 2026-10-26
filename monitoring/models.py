from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError


class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


class Measurement(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='measurements')
    parameter = models.CharField(max_length=50)
    value = models.FloatField(validators=[MinValueValidator(0.0)])
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def clean(self):
        super().clean()
        if self.parameter == 'PM2.5' and self.value > 1000:
            raise ValidationError({'value': 'PM2.5 value is too high'})