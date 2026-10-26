from django.urls import path

from . import views

urlpatterns = [
    path("health/", views.health_check, name="health_check"),
    path("stats/<int:location_id>/<str:parameter>/", views.location_stats, name="location_stats"),
]
