from django.contrib import admin
from .models import Location, Measurement


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "latitude", "longitude")


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ("id", "location", "parameter", "value", "timestamp")
    list_filter = ("parameter", "location")