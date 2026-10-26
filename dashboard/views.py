from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from monitoring.models import Measurement


@login_required
def index(request):
    # Получаем последние измерения по каждому параметру
    latest_measurements = {}
    parameters = ["PM2.5", "CO2", "NO2"]
    for param in parameters:
        m = Measurement.objects.filter(parameter=param).order_by("-timestamp").first()
        if m:
            latest_measurements[param] = m

    return render(request, "dashboard/index.html", {"measurements": latest_measurements})
