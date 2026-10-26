from django.http import JsonResponse
from .models import Measurement
from .services import get_measurement_stats

def health_check(request):
    """Простой эндпоинт для проверки работоспособности."""
    return JsonResponse({"status": "ok"})

def location_stats(request, location_id, parameter):
    """Эндпоинт со статистикой."""
    stats = get_measurement_stats(location_id, parameter)
    if stats is None:
        return JsonResponse({"error": "No data"}, status=404)
    return JsonResponse(stats)